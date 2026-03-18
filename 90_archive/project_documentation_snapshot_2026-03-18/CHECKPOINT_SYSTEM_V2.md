# BDC Checkpoint System V2

**Version:** 2.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Replaces:** Monolithic checkpoint system (failed in TRL-10.1)

---

## Overview

This document defines the sharded, resume-safe checkpoint architecture for BDC. It explicitly prohibits monolithic checkpoints and defines what is saved, when, where, and why.

---

## TRL-10.1 Checkpoint Failure: Root Cause

### Incident Summary

**Date:** 2026-01-24  
**Phase:** TRL-10.1 8-hour Full Wikipedia Training  
**Problem:** Checkpoints were not saved (directory missing, files absent)

### Root Causes

1. **Monolithic checkpoint design:**
   - Single `.pt` file containing all model states
   - Size: >1.7GB (exceeded git artifact policy)
   - Save operation failed silently or was disabled

2. **No sharding:**
   - All agent networks in one file
   - Text encoder, population dynamics, optimizer states combined
   - Result: Too large to save reliably

3. **Missing error handling:**
   - Checkpoint save failures not logged
   - No fallback mechanism
   - No validation that checkpoints were actually written

4. **Git artifact policy violation:**
   - Attempted to save >50MB files
   - Violated GIT_ARTIFACT_POLICY.md
   - Files correctly excluded from git, but also not saved externally

### Impact

- **Warm restart impossible:** Cannot resume TRL-10.2 from TRL-10.1 state
- **Reproducibility limited:** Only metrics.json available, not full state
- **Training time lost:** 8 hours of training cannot be continued

---

## Checkpoint System V2: Architecture

### Design Principles

1. **Sharded storage:** Split checkpoints into multiple files (<50MB each)
2. **Resume-safe:** Can restore exact training state
3. **External-only:** Never in git (per GIT_ARTIFACT_POLICY.md)
4. **Validated:** Checksums and integrity verification
5. **Incremental:** Save only changed components when possible

### Checkpoint Structure

```
checkpoints/
├── checkpoint_ep{episode:06d}/
│   ├── metadata.json           # Episode, timestamp, config hash
│   ├── text_encoder.pt          # Text encoder state (<50MB)
│   ├── population_dynamics.pt   # Population network state (<50MB)
│   ├── optimizer.pt             # Optimizer state (<50MB)
│   ├── agent_states/
│   │   ├── agent_000.pt        # Individual agent states (<10MB each)
│   │   ├── agent_001.pt
│   │   └── ...
│   ├── metrics.json             # Episode metrics snapshot
│   └── checksum.sha256          # Integrity verification
└── checkpoint_final/            # Final checkpoint (same structure)
```

### Sharding Rules

**Maximum File Size:** 50MB per file (git artifact policy limit)

**Sharding Strategy:**
1. **Text encoder:** Single file (typically <50MB)
2. **Population dynamics:** Single file (typically <50MB)
3. **Optimizer:** Single file (typically <50MB)
4. **Agent states:** One file per agent (N files, each <10MB)
5. **Metadata:** JSON file (<1MB)

**If any component >50MB:**
- Split into multiple shards (e.g., `text_encoder_part1.pt`, `text_encoder_part2.pt`)
- Record shard count in metadata.json
- Validate all shards on restore

---

## What Is Saved

### Required Components

1. **Model States:**
   - Text encoder: `state_dict()`
   - Population dynamics: `state_dict()`
   - Agent networks: `state_dict()` for each agent

2. **Training State:**
   - Optimizer: `state_dict()` (learning rates, momentum, etc.)
   - Episode number
   - Random number generator state (if applicable)

3. **Configuration:**
   - Hyperparameters (batch size, learning rate, etc.)
   - Architecture parameters (num_agents, embed_dim, etc.)
   - Dataset configuration (paths, sizes, etc.)

4. **Metrics Snapshot:**
   - Current episode metrics
   - Last 100 episodes of history (for warm restart analysis)

5. **Metadata:**
   - Timestamp (ISO 8601)
   - Commit hash
   - Experiment ID
   - Checkpoint version (for compatibility)

### Optional Components

1. **GPU Control State:**
   - Batch multiplier
   - Compute iterations
   - Utilization history (last 100 entries)

2. **Knowledge Extractor State:**
   - Entity mentions dictionary
   - Fact database snapshot

**Rule:** Optional components only if <10MB total and resume requires them.

---

## When Checkpoints Are Saved

### Automatic Checkpoints

1. **Interval-based:**
   - Every N episodes (default: 100)
   - Configurable via `checkpoint_interval` parameter

2. **Milestone-based:**
   - Every 1000 episodes
   - Fitness improvement milestones (e.g., +0.1)
   - Diversity recovery milestones (e.g., after injection)

3. **Final checkpoint:**
   - Always saved at end of training
   - Marked as `checkpoint_final/`

### Manual Checkpoints

**Trigger:** User command or API call

**Use Cases:**
- Before major parameter changes
- Before long training runs
- After significant fitness improvements

### Emergency Checkpoints

**Trigger:** System signals (SIGTERM, SIGINT)

**Behavior:**
- Save current state immediately
- Mark as `checkpoint_emergency/`
- May be incomplete (log warning)

---

## Where Checkpoints Are Saved

### Storage Location

**Primary:** `results/{experiment_id}/checkpoints/`

**External Archive (for long-term):**
- External storage (not in git)
- Path: `{external_storage}/{experiment_id}/checkpoints/`
- Symlink or copy from primary location

### Git Exclusion

**Rule:** Checkpoints NEVER in git (per GIT_ARTIFACT_POLICY.md)

**Enforcement:**
- `.gitignore` includes `**/checkpoints/**`
- Pre-commit hook validates no checkpoint files staged
- CI/CD fails if checkpoints detected in git

### Backup Strategy

1. **Local backup:** Copy to `backup/{experiment_id}_{timestamp}/`
2. **External backup:** Copy to external storage (if available)
3. **Retention:** Keep last 10 checkpoints, archive older ones

---

## Why Checkpoints Are Saved

### Primary Reasons

1. **Resume training:** Continue from last state (warm restart)
2. **Reproducibility:** Exact state for result verification
3. **Analysis:** Inspect intermediate states for debugging
4. **Recovery:** Restore after crashes or interruptions

### Secondary Reasons

1. **Experimentation:** Try different hyperparameters from same state
2. **Comparison:** Compare different training runs from same checkpoint
3. **Debugging:** Inspect model states for anomalies

---

## Resume Safety

### Requirements

A checkpoint is **resume-safe** if:

1. **Complete state:** All required components present
2. **Integrity verified:** Checksums match
3. **Compatible:** Checkpoint version matches current code
4. **Validated:** Restore test passes (load → verify → continue)

### Resume Procedure

```
1. Load metadata.json → verify version compatibility
2. Load all shards → verify checksums
3. Restore model states → verify shapes match
4. Restore optimizer state → verify parameters match
5. Restore episode number → verify continuity
6. Test forward pass → verify no errors
7. Resume training → verify metrics continue correctly
```

### Validation Tests

**Pre-restore:**
- Checksum verification (SHA-256)
- File existence and size checks
- Version compatibility check

**Post-restore:**
- Model parameter shape verification
- Forward pass test (no errors)
- Metric continuity check (no sudden jumps)

---

## Prohibited Patterns

### Monolithic Checkpoints

**FORBIDDEN:**
```python
# ❌ BAD: Single large file
torch.save({
    'text_encoder': text_encoder.state_dict(),
    'agent_networks': [net.state_dict() for net in agent_networks],
    'population_dynamics': population_dynamics.state_dict(),
    'optimizer': optimizer.state_dict(),
    # ... all in one file >1GB
}, 'checkpoint.pt')
```

**REQUIRED:**
```python
# ✅ GOOD: Sharded files
save_checkpoint_sharded(
    text_encoder=text_encoder.state_dict(),
    agent_networks=[net.state_dict() for net in agent_networks],
    population_dynamics=population_dynamics.state_dict(),
    optimizer=optimizer.state_dict(),
    checkpoint_dir='checkpoints/checkpoint_ep001000/',
    max_file_size=50*1024*1024  # 50MB
)
```

### Git Storage

**FORBIDDEN:**
- Storing checkpoints in git (even if <50MB)
- Committing checkpoint metadata to git (except experiment IDs)
- Including checkpoint paths in tracked files

**REQUIRED:**
- External storage only
- `.gitignore` enforcement
- Pre-commit validation

### Silent Failures

**FORBIDDEN:**
- Saving checkpoints without error handling
- Not validating that files were written
- Not logging checkpoint save status

**REQUIRED:**
- Try-except blocks around save operations
- File existence verification after save
- Logging success/failure status

---

## Implementation Example

### Save Function

```python
def save_checkpoint_v2(
    episode: int,
    text_encoder: nn.Module,
    agent_networks: List[nn.Module],
    population_dynamics: nn.Module,
    optimizer: torch.optim.Optimizer,
    checkpoint_dir: Path,
    max_file_size: int = 50 * 1024 * 1024,  # 50MB
) -> bool:
    """Save checkpoint in sharded format."""
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    
    # Save metadata
    metadata = {
        'episode': episode,
        'timestamp': datetime.now().isoformat(),
        'commit_hash': get_git_commit_hash(),
        'checkpoint_version': '2.0',
        'shards': {}
    }
    
    # Save text encoder (shard if needed)
    encoder_path = checkpoint_dir / 'text_encoder.pt'
    encoder_state = text_encoder.state_dict()
    if get_state_dict_size(encoder_state) > max_file_size:
        save_sharded(encoder_state, encoder_path, max_file_size)
        metadata['shards']['text_encoder'] = get_shard_count(encoder_path)
    else:
        torch.save(encoder_state, encoder_path)
        metadata['shards']['text_encoder'] = 1
    
    # Save agent networks (one file per agent)
    agent_dir = checkpoint_dir / 'agent_states'
    agent_dir.mkdir(exist_ok=True)
    for i, agent_net in enumerate(agent_networks):
        agent_path = agent_dir / f'agent_{i:03d}.pt'
        torch.save(agent_net.state_dict(), agent_path)
    
    # Save population dynamics
    pop_path = checkpoint_dir / 'population_dynamics.pt'
    torch.save(population_dynamics.state_dict(), pop_path)
    
    # Save optimizer
    opt_path = checkpoint_dir / 'optimizer.pt'
    torch.save(optimizer.state_dict(), opt_path)
    
    # Save metadata
    metadata_path = checkpoint_dir / 'metadata.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    # Compute and save checksum
    checksum = compute_checksum(checkpoint_dir)
    checksum_path = checkpoint_dir / 'checksum.sha256'
    with open(checksum_path, 'w') as f:
        f.write(checksum)
    
    # Validate
    if not validate_checkpoint(checkpoint_dir):
        logger.error(f"Checkpoint validation failed: {checkpoint_dir}")
        return False
    
    logger.info(f"Checkpoint saved: {checkpoint_dir}")
    return True
```

### Load Function

```python
def load_checkpoint_v2(
    checkpoint_dir: Path,
    text_encoder: nn.Module,
    agent_networks: List[nn.Module],
    population_dynamics: nn.Module,
    optimizer: torch.optim.Optimizer,
) -> Dict:
    """Load checkpoint from sharded format."""
    # Verify checksum
    if not verify_checksum(checkpoint_dir):
        raise ValueError(f"Checksum verification failed: {checkpoint_dir}")
    
    # Load metadata
    metadata_path = checkpoint_dir / 'metadata.json'
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    
    # Verify version compatibility
    if metadata['checkpoint_version'] != '2.0':
        raise ValueError(f"Version mismatch: {metadata['checkpoint_version']}")
    
    # Load text encoder
    encoder_path = checkpoint_dir / 'text_encoder.pt'
    if metadata['shards']['text_encoder'] > 1:
        encoder_state = load_sharded(encoder_path, metadata['shards']['text_encoder'])
    else:
        encoder_state = torch.load(encoder_path)
    text_encoder.load_state_dict(encoder_state)
    
    # Load agent networks
    agent_dir = checkpoint_dir / 'agent_states'
    for i, agent_net in enumerate(agent_networks):
        agent_path = agent_dir / f'agent_{i:03d}.pt'
        agent_state = torch.load(agent_path)
        agent_net.load_state_dict(agent_state)
    
    # Load population dynamics
    pop_path = checkpoint_dir / 'population_dynamics.pt'
    pop_state = torch.load(pop_path)
    population_dynamics.load_state_dict(pop_state)
    
    # Load optimizer
    opt_path = checkpoint_dir / 'optimizer.pt'
    opt_state = torch.load(opt_path)
    optimizer.load_state_dict(opt_state)
    
    return metadata
```

---

## Migration from V1

### TRL-10.1 Checkpoints

**Status:** Not recoverable (checkpoints were never saved)

**Action:** TRL-10.2 must start from scratch or use TRL-10.0 baseline.

### Future Runs

**Requirement:** All new training runs MUST use V2 checkpoint system.

**Enforcement:**
- Code review checks for V2 usage
- CI/CD validates checkpoint structure
- Documentation updated to reference V2 only

---

## Validation Checklist

Before considering a checkpoint system "done":

- [ ] Sharded storage implemented (<50MB per file)
- [ ] Resume safety verified (load → verify → continue)
- [ ] Git exclusion enforced (.gitignore + pre-commit hook)
- [ ] Error handling present (try-except, validation)
- [ ] Checksums computed and verified
- [ ] Version compatibility checked
- [ ] External storage configured (if applicable)
- [ ] Documentation updated (this file)

---

**CHECKPOINT_SYSTEM_V2.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After checkpoint system implementation or major changes
