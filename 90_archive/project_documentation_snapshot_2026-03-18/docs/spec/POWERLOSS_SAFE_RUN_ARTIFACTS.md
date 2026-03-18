# Power-Loss Safe Run Artifacts (exp_0017) (Spec)

Status: CANON (control-plane + durability only; does not change learning semantics).

## Scope / Canon Constraints

- Applies to: `experiments/exp_0017_comprehension_v0_cloze`.
- Guarantees are about *artifact durability and auditability* only.
- No changes to training objective, model behavior, data semantics, masking, loss, optimizer, or metrics definitions.
- All guarantees must hold without relying on stdout/stderr (power loss, terminal closed, etc).

## Required Files (Per Run Directory)

Minimum contract (L0):

1. `RUN_METADATA.json`
   - Written once at run start.
   - Must include: `git_head`, `run_tag`, `seed`, `device`, `dataset_root`, `masking`, `training` knobs, `torch_*` fields.
2. `metrics_by_step.jsonl`
   - Exists immediately at run start.
   - First line is JSON with `{"event":"RUN_START", ...}`.
   - Append-only; EVAL records may be plain `{"step":..., "val":{...}}` for compatibility.
   - Terminal marker appended as `{"event":"RUN_END", ...}` with `reason` and `state`.
3. `RUN_STATUS.json`
   - Heartbeat + state machine (atomic replace).
   - Must include non-null `ts_utc`, `state`, `step`, and `wall_s`.
4. Terminal artifact (exactly one required; more than one allowed but discouraged):
   - `metrics.json` (normal completion), or
   - `CRASH.json` (exception), or
   - `STOPPED.json` (user-requested cooperative stop).

## Durability Rules

All durability rules are *power-loss oriented*:

- Atomic JSON writes:
  - Write `*.tmp` in the same directory, `flush`, `fsync`, then `os.replace`.
  - Used for: `RUN_METADATA.json`, `RUN_STATUS.json`, `metrics.json`, `CRASH.json`, `STOPPED.json`.
- JSONL append:
  - Open in append mode, write one line + `\n`, `flush`, `fsync`.
  - Used for: `metrics_by_step.jsonl` (`RUN_START`, each EVAL record, `RUN_END`).
- Heartbeat cadence:
  - Default: `RUN_STATUS.json` updates at least every `--status_every_sec` (default `15s`) while running.

Durability staleness window (bounded data-loss window):

- `--durable_interval_sec` (default `300`): intermediate writes may `flush` frequently but will `fsync` no less often than this interval, bounding expected power-loss staleness to ~5 minutes.
- Terminal artifacts are always written durably immediately (atomic + `fsync`), regardless of `--durable_interval_sec`.

Knobs:

- `--durable_writes` (default `true`): if `false`, the implementation may skip `fsync` calls for throughput at the cost of power-loss resilience.
- `--durable_interval_sec` (default `300`): max staleness window for intermediate artifacts (see above).

## STOP Control Plane (Localhost-Only; Opt-In)

STOP is a control-plane feature. It must never delete artifacts and must not modify the dataset.

- The localhost server (loopback-only) can accept a token-gated STOP request and write:
  - `<run_dir>/STOP_REQUEST.json` atomically.
- Training process polls the stop request file and exits cooperatively:
  - updates `RUN_STATUS.json` to `STOPPING`,
  - Emergency stop: writes `STOPPED.json` (atomic + fsync) and appends a `RUN_END` record.
  - Graceful stop: tries to stop on a safe boundary (preferably after the next scheduled eval); writes `metrics.json` and appends a `RUN_END` record.

Localhost constraints:

- Server must bind strictly to `127.0.0.1`.
- Token must be random per run and never written into dataset artifacts.

## Verification (L0)

Commands:

```powershell
# integrity + hashes
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash

# check RUN_START + RUN_END markers quickly
Get-Content <RUN_DIR>/metrics_by_step.jsonl -TotalCount 1
Get-Content <RUN_DIR>/metrics_by_step.jsonl -Tail 1
```
