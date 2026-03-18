# BDC HIVE Architecture

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Type:** Distributed Island-Model Architecture

---

## Overview

BDC HIVE is a distributed island-model architecture for scaling BDC across multiple compute nodes. It implements Queen/Drone roles, minimal-trust API, redundancy validation, and explicit client compute boundaries.

**Core Principle:** Clients cannot own canonical state. Only Queen nodes maintain authoritative state.

---

## Architecture Overview

### Island Model

**Concept:** Multiple independent "islands" (compute nodes) evolve separate populations, with periodic migration between islands.

**Benefits:**
- Parallel evolution (faster exploration)
- Diversity maintenance (isolated populations)
- Fault tolerance (island failure doesn't kill entire system)
- Scalability (add islands as needed)

### Node Roles

#### Queen Node

**Responsibilities:**
- Maintain canonical state (authoritative)
- Coordinate island synchronization
- Validate and merge island results
- Enforce global constraints (kill-criteria, limits)
- Manage client API (read-only access)

**Characteristics:**
- Single Queen per HIVE (or consensus-based multiple Queens)
- Persistent storage (checkpoints, state)
- High availability (redundancy, failover)
- Trusted (runs canonical BDC code)

#### Drone Node

**Responsibilities:**
- Run evolution experiments (local population)
- Execute training runs (local compute)
- Report results to Queen
- Request migrations (agent transfers)

**Characteristics:**
- Multiple Drones per HIVE
- Stateless (can be replaced)
- Untrusted (may run modified code)
- Autonomous (local decisions, global constraints)

---

## Minimal-Trust API

### Design Principle

**Minimal Trust:** Drones are not trusted. All results must be validated before acceptance.

### API Endpoints

#### Queen → Drone

**1. Start Experiment**
```
POST /queen/experiments/{experiment_id}/start
Request: {
    "experiment_spec": {...},
    "initial_population": [...],  # Optional: seed population
    "constraints": {
        "max_agents": 50,
        "kill_criteria": {...},
        "stop_scaling_criteria": {...}
    }
}
Response: {
    "experiment_id": "...",
    "checkpoint_interval": 100,
    "report_interval": 10
}
```

**2. Request Migration**
```
POST /queen/migrations/request
Request: {
    "source_island": "drone_1",
    "target_island": "drone_2",
    "agent_ids": [1, 5, 10],
    "reason": "diversity_injection"
}
Response: {
    "migration_id": "...",
    "approved": true,
    "agent_states": [...]  # Encrypted/signed
}
```

#### Drone → Queen

**1. Report Results**
```
POST /drone/experiments/{experiment_id}/report
Request: {
    "episode": 1000,
    "metrics": {
        "fitness": 0.85,
        "diversity": 0.22,
        "signal_to_noise": 0.15
    },
    "checkpoint_hash": "sha256:...",
    "proof": "signature"  # Cryptographic proof of results
}
Response: {
    "accepted": true,
    "validation_status": "passed",
    "next_checkpoint": 1100
}
```

**2. Request Checkpoint**
```
GET /drone/checkpoints/{checkpoint_id}
Response: {
    "checkpoint_data": {...},  # Sharded checkpoint
    "checksum": "sha256:...",
    "signature": "queen_signature"
}
```

### Validation Requirements

**All Drone results MUST be validated:**

1. **Cryptographic proof:** Signature or hash chain
2. **Constraint compliance:** Check against kill-criteria, limits
3. **Reproducibility:** Verify with PiStream seeds (if applicable)
4. **Statistical validity:** Check sample sizes, confidence intervals

**Invalid results:** Rejected, Drone marked as untrusted

---

## Redundancy Validation

### Redundancy Strategy

**Multiple Drones** run same experiment with different seeds to validate results.

**Process:**
1. Queen assigns experiment to N Drones (N≥3 for redundancy)
2. Each Drone runs with different PiStream seed
3. Results compared for consistency
4. Consensus: Accept if ≥(N+1)/2 Drones agree (within tolerance)

### Validation Rules

**Fitness Validation:**
```
fitness_variance = variance([drone_1.fitness, drone_2.fitness, ...])
if fitness_variance > threshold:
    REJECT (results inconsistent)
else:
    ACCEPT (consensus reached)
```

**Diversity Validation:**
```
diversity_variance = variance([drone_1.diversity, drone_2.diversity, ...])
if diversity_variance > threshold:
    REJECT (diversity inconsistent)
else:
    ACCEPT (consensus reached)
```

### Tolerance Thresholds

**Fitness:** ±0.05 (5% tolerance)  
**Diversity:** ±0.02 (2% tolerance)  
**Signal-to-noise:** ±0.01 (1% tolerance)

**Rationale:** Account for numerical precision and environmental variance.

---

## Client Compute Boundaries

### Rule: Clients Cannot Own Canonical State

**Forbidden:**
- Clients modifying Queen state directly
- Clients storing authoritative checkpoints
- Clients making global decisions (kill-criteria, limits)

**Allowed:**
- Clients reading results (read-only API)
- Clients requesting experiments (via Queen)
- Clients running local simulations (non-canonical)

### Client API (Read-Only)

**Endpoints:**

**1. Query Results**
```
GET /client/experiments/{experiment_id}/results
Response: {
    "metrics": {...},
    "checkpoint_id": "...",
    "status": "completed"
}
```

**2. Query Population State**
```
GET /client/experiments/{experiment_id}/population
Response: {
    "agents": [...],  # Read-only, no state modification
    "diversity": 0.22,
    "fitness_distribution": {...}
}
```

**3. Request Experiment**
```
POST /client/experiments/request
Request: {
    "experiment_spec": {...},
    "priority": "normal"
}
Response: {
    "experiment_id": "...",
    "estimated_completion": "2026-01-28T12:00:00Z",
    "status": "queued"
}
```

**Note:** Client requests are validated by Queen before execution.

### Client Compute Limits

**Clients may:**
- Run local simulations (non-canonical, for exploration)
- Analyze results (read-only access)
- Request experiments (via Queen validation)

**Clients may NOT:**
- Modify canonical state
- Bypass kill-criteria
- Override population limits
- Store authoritative checkpoints

---

## Island Synchronization

### Migration Protocol

**Purpose:** Transfer agents between islands to maintain diversity and share knowledge.

**Process:**
1. Drone detects low diversity or convergence
2. Drone requests migration from Queen
3. Queen validates request (diversity check, resource availability)
4. Queen selects agents for migration (top performers, diverse samples)
5. Queen signs agent states (cryptographic proof)
6. Target Drone receives and validates agents
7. Target Drone integrates agents into local population

### Synchronization Frequency

**Migration Interval:** Every 100-500 episodes (configurable)

**Trigger Conditions:**
- Diversity < threshold on source island
- Convergence > 95% on source island
- Target island requests diversity injection
- Queen detects global convergence risk

### Conflict Resolution

**If multiple Drones request same agents:**
- Queen prioritizes by:
  1. Diversity need (higher priority)
  2. Resource availability (target island capacity)
  3. Request timestamp (FIFO for equal priority)

---

## Security and Trust

### Queen Trust Model

**Queen is trusted:**
- Runs canonical BDC code (verified)
- Maintains authoritative state
- Enforces global constraints
- Validates all results

**Queen redundancy:**
- Multiple Queens possible (consensus-based)
- Failover mechanism (if primary Queen fails)
- State replication (for availability)

### Drone Trust Model

**Drones are untrusted:**
- May run modified code
- May report false results
- May attempt to bypass constraints

**Mitigation:**
- Cryptographic validation (signatures, hashes)
- Redundancy validation (consensus from multiple Drones)
- Constraint enforcement (Queen validates all results)
- Reproducibility checks (PiStream seed verification)

### Client Trust Model

**Clients are untrusted:**
- May request malicious experiments
- May attempt to modify state
- May try to bypass limits

**Mitigation:**
- Read-only API (no state modification)
- Request validation (Queen checks all requests)
- Rate limiting (prevent abuse)
- Authentication/authorization (if applicable)

---

## Failure Handling

### Drone Failure

**Scenario:** Drone crashes or becomes unresponsive.

**Handling:**
1. Queen detects timeout (no reports for N intervals)
2. Queen marks Drone as failed
3. Queen reassigns experiment to backup Drone (if available)
4. Backup Drone loads last checkpoint and continues
5. Failed Drone's results discarded (if not validated)

**Recovery:** Failed Drone can rejoin with last known checkpoint.

### Queen Failure

**Scenario:** Primary Queen crashes.

**Handling:**
1. Backup Queen detects primary failure (heartbeat timeout)
2. Backup Queen promotes to primary
3. Backup Queen loads last state from persistent storage
4. Drones reconnect to new primary Queen
5. Experiments continue from last checkpoint

**Recovery:** Primary Queen can rejoin as backup (state sync required).

### Network Partition

**Scenario:** Islands cannot communicate.

**Handling:**
1. Islands continue local evolution (autonomous)
2. Islands cache results for later synchronization
3. When network restored, Queen merges results
4. Conflicts resolved by timestamp and validation

**Recovery:** Network restoration triggers full state sync.

---

## Implementation Status

**Current Status:** DESIGN PHASE

**Not Yet Implemented:**
- Queen/Drone node code
- Minimal-trust API endpoints
- Redundancy validation logic
- Migration protocol
- Client API

**Future Work:**
- Implement Queen node (canonical state management)
- Implement Drone node (local evolution)
- Implement API endpoints (REST or gRPC)
- Implement validation logic (cryptographic, statistical)
- Implement migration protocol (agent transfer)
- Implement client API (read-only access)

---

## Relationship to Other Documents

- **ARCHITECTURE.md:** Defines task classes and scaling limits (referenced)
- **POPULATION_AND_SCALING.md:** Defines agent count limits (implements)
- **CHECKPOINT_SYSTEM_V2.md:** Defines checkpoint format (uses)
- **RESEARCH_METHODOLOGY.md:** Defines validation requirements (implements)

---

**BDC_HIVE_ARCHITECTURE.md Status:** CANONICAL (DESIGN PHASE)  
**Next Review:** After implementation begins or major design changes
