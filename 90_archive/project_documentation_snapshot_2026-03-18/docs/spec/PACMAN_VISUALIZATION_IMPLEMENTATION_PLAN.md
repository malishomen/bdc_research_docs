# Pac-Man Visualization — Implementation Plan (L0-first, file-based, quaternary, read-only)

Authoritative UX spec:
- `docs/EXPERIMENT_VISUALIZATION_PACMAN.md` (this plan must not contradict it)

Design guarantee (canonical):
- Visualization is **read-only** and **file-based**.
- Visualization must not affect training correctness, PASS/FAIL, or evidence. It is monitoring/analysis only.

Repository scaffold (implementation targets in this repo):
- `ui/pacman_viz/schema/run_snapshot.schema.json` (normalized snapshot schema; derived from artifacts)
- `ui/pacman_viz/src/normalize_run_snapshot.py` (read-only normalizer: run_dir -> snapshot JSON)
- `ui/pacman_viz/src/viewer.html` (single-file Canvas viewer; offline by default)
- `ui/pacman_viz/README.md` (runbook)

## 1) Scope And Canon Constraints

In-scope:
- A standalone visualization app that reads experiment artifacts from disk (polling) and renders Pac-Man metaphor.
- Quaternary state visualization (YES/NO/MAYBE_YES/MAYBE_NO) per `docs/EXPERIMENT_VISUALIZATION_PACMAN.md`.
- L0 traceability: paths, sha256, reproducible commands for the viewer.

Out-of-scope:
- Any coupling to training loops (no sockets into training, no callbacks, no in-process imports of training code).
- Any mutation of experiment outputs (no rewriting logs, no patching metrics).
- Any change in exp_0017 semantics, policy thresholds, or dataset build.

## 2) Data Sources (L0) And Update Strategy

### 2.1 Primary Files (already produced by exp_0017 today)

Per run directory, read:
- `RUN_STATUS.json` (heartbeat + state)
- `RUN_METADATA.json` (static config, device, dataset_root, tokenizer, masking, training knobs)
- `metrics_by_step.jsonl` (time series; RUN_START + EVAL points)
- `metrics.json` (terminal summary, val/test + baselines) OR `CRASH.json`
- Optional sidecar (external tooling; viewer-only evidence):
  - `policy_eval.json` (produced by `tools/analysis/exp0017_write_policy_sidecar.py`; atomic writes)

Discovery:
- user provides `--runs_root` (e.g. `logs/exp_0017_comprehension_v0_cloze`)
- viewer discovers runs by folder name pattern `run_*_<run_tag>` and/or by scanning `RUN_METADATA.json.run_tag` (present in exp_0017 today)

### 2.2 Polling Defaults

- default polling interval: 60s (configurable; minimum 5s for local use)
- update strategy:
  - read file `LastWriteTimeUtc` / size to detect changes
  - for `metrics_by_step.jsonl`, read incrementally (seek to last offset) when possible

### 2.2.1 1-Minute Snapshot Mode (offline-first)

For long runs, prefer writing a normalized snapshot every 60s to a separate (gitignored) directory:
- tool: `ui/pacman_viz/src/snapshot_daemon.py`
- outputs (example): `ui/pacman_viz/_snapshots/<run_tag>/snapshot_YYYYmmddTHHMMSSZ.json` + optional `LATEST.json`

This keeps the viewer simple (it only reads snapshots) and avoids repeatedly parsing large JSONL.

### 2.3 Partial/Concurrent Writes Handling (robustness)

Assume files can be mid-write:
- JSON parse failures: treat as `MAYBE_NO` snapshot (viewer-side only), retry next poll.
- For JSONL: ignore the last line if it is not valid JSON (common partial write pattern), retry next poll.

Note: exp_0017 crash-safe artifacts use atomic JSON writes for `RUN_STATUS.json` and `metrics.json`, reducing partial-write risk.

## 3) Snapshot Schema Contract (viewer-internal; derived without changing training)

The viewer assembles an in-memory snapshot per run:

```json
{
  "snapshot_ts_utc": "2026-02-09T12:00:00Z",
  "run_dir": "logs/exp_0017.../run_..._tag",
  "run_tag": "task0144_quality_2h_io",
  "state": "RUNNING|COMPLETED|CRASHED|UNKNOWN",
  "git_head_run": "9708fec...",
  "dataset_root": "D:\\datasets\\...",
  "masking": {"mask_rate": 0.15, "mask_span_max": 3, "mask_salt": "..." },
  "training": {"batch_size": 32, "eval_every": 1000, "eval_max_docs": 2000, "num_workers": 4, "pin_memory": true, "prefetch_factor": 2, "persistent_workers": true},
  "latest": {
    "step": 91000,
    "val_acc": 0.5346,
    "val_loss": 3.09,
    "test_acc": 0.5134,
    "baseline_shuffled_val_acc": 0.0276
  },
  "timeline": {
    "eval_count": 91,
    "first_eval_step": 1000,
    "last_eval_step": 91000
  },
  "gates": {
    "dataset_integrity": "PASS|FAIL|UNKNOWN",
    "artifact_integrity": "PASS|FAIL|UNKNOWN",
    "policy_exit_code": 0,
    "policy_verdict": "PASS|FAIL|ERROR|UNKNOWN"
  },
  "quaternary_state": "YES|NO|MAYBE_YES|MAYBE_NO"
}
```

Optional: write snapshots to disk as `snapshots/<run_id>.json` for offline playback (must be gitignored).

Policy sidecar contract (if present):
- `policy_eval.json` schema: `ui/pacman_viz/schema/policy_eval.schema.json`
- Snapshot must include:
  - `quat_source = "policy_eval"` when sidecar is present and parseable
  - `policy` object snippet (exit_code/verdict/problems/tool provenance)

## 4) Quaternary Logic Mapping (viewer-only; does not control training)

Color mapping (per UX spec `docs/EXPERIMENT_VISUALIZATION_PACMAN.md`):
- YES: green
- NO: red
- MAYBE_YES: yellow
- MAYBE_NO: blue

Run-level quaternary state derivation (L0, file-based; visual-only):
Rule order:
1. If `policy_eval.json` exists and is parseable (sidecar evidence):
   - exit_code 0 => `YES` + label `policy_pass`
   - exit_code 2 => `NO` + label `policy_fail`
   - exit_code 1 => `MAYBE_NO` + label `policy_error`
2. Else if `CRASH.json` exists OR `data_status in {"incomplete","crashed","no_data"}` => `MAYBE_NO` + label `incomplete`.
3. Else if `metrics.json.verdict_kc_sanity != "PASS"` => `NO` + label `sanity_fail`.
4. Else if `metrics.json` exists and sanity PASS and run is complete => `MAYBE_YES` + label `unknown_policy`.
5. Else => `MAYBE_NO` + label `unknown_policy`.

Note: if policy output is not present, the viewer must not "invent" it; it must display `unknown_policy`.

Aggregation mechanic (per task requirement; affects only visualization size/behavior):
- 3 x MAYBE_YES -> +1 level toward YES ("growth")
- 3 x MAYBE_NO -> +1 level toward NO ("shrink")

Implementation note:
- Keep an internal counter per run: `maybe_yes_streak`, `maybe_no_streak`.
- Reset the opposite streak on each update.

## 5) Pac-Man Mechanics (visual, not governing)

Entity mapping (MVP):
- One Pac-Man per run_tag (run = "agent").
- Size = monotonic transform of `latest.val_acc` (clamped), e.g. `size = base + scale * val_acc`.
- Direction/speed = sign/magnitude of last delta in val_acc (based on last 2 EVAL points).
- Trails = previous positions per snapshot (fade).

Toxins (visualization of failure conditions; no compute coupling):
- Toxin appears if any of:
  - dataset_integrity FAIL
  - artifact_integrity FAIL
  - `metrics.json.verdict_kc_sanity != PASS`
  - policy exit_code 2 (only if captured as evidence)
- Contact with toxin:
  - Pac-Man shrinks; if below min size, disappears (visual "killed")

Reproduction:
- If size exceeds threshold for N consecutive snapshots, spawn a child Pac-Man (visual only) representing the same run with a suffix id; child inherits trajectory but starts small.

## 6) Phase Behavior (Phase 0/1/2)

Phase display source (canon-safe):
- If the run artifacts include an explicit `phase` field (future metadata-only addition), show it.
- Otherwise, display `phase: unknown` (do not infer phase from heuristics).

## 7) Performance Constraints

Targets (align with UX spec):
- 60 FPS target, acceptable >= 30 FPS
- < 100 MB RAM target

Constraints/strategies:
- Canvas 2D first (no heavy shaders).
- Limit visible entities (e.g. show top K runs by recency, default K=50).
- Downsample trails (keep last 200 points).
- Parse JSON incrementally; avoid loading full JSONL into memory when tailing.

## 8) Security And Privacy (no HIVE; local-first)

Principles:
- Read-only file access.
- Strict input validation of JSON (treat as untrusted).
- No dynamic HTML injection from log fields.

If a local HTTP server is used (optional):
- Serve static frontend + a minimal read-only API that returns snapshots.
- Enforce allowlist root directory; reject path traversal.
- Rate limit polling endpoints; cap response sizes.

## 9) Threat Model (concrete attacks + mitigations)

1. Path traversal (`..\\..\\`) in run_dir selection:
   - Mitigation: canonicalize paths and enforce `run_dir` under `runs_root` allowlist.
2. JSON-based XSS (malicious strings in title/text fields):
   - Mitigation: never inject raw strings into HTML; render text via DOM text nodes; escape.
3. Log poisoning / replay (stale metrics copied in place of new ones):
   - Mitigation: display sha256 + file mtimes; highlight when hashes regress.
4. Partial write / corruption causing crashes:
   - Mitigation: tolerant parser; ignore invalid last JSONL line; retry.
5. DoS via huge files / too many runs:
   - Mitigation: cap max file bytes read per poll; cap number of runs; incremental tailing.
6. Supply chain (malicious npm deps / build scripts):
   - Mitigation: lockfiles; minimal deps; review; prefer vanilla JS/Canvas for MVP.
7. Symlink tricks (run_dir points outside allowlist):
   - Mitigation: resolve realpath; reject symlinks/junctions outside root.

## 10) MVP Roadmap (TASK-0147+)

Small, testable steps:
1. TASK-0147: build `tools/pacman_viewer/` skeleton (static HTML + Canvas) + snapshot reader CLI; L0 report.
2. TASK-0148: implement run discovery + incremental JSONL tailing + quaternary mapping; unit tests on synthetic artifacts.
3. TASK-0149: add optional policy-eval runner (read-only) with cached outputs; add "policy snapshot" file format (gitignored).
4. TASK-0150: performance pass (K caps, trail downsampling, memory checks) + threat-model checklist verification.

## 11) Kill-Criteria And Success Criteria (visualization-only)

Kill-criteria:
- Any evidence of training slowdown due to viewer presence (should be 0; viewer separate process).
- Viewer crashes repeatedly on valid artifacts (parser robustness failure).
- Unbounded memory growth (> 200 MB) or sustained FPS < 30.

Success criteria:
- Correct, stable reading of run_dir artifacts with partial-write tolerance.
- Quaternary colors match mapping and are derived only from file-based evidence.
- L0 traceability visible: paths + sha256 + reproducible commands in docs.
