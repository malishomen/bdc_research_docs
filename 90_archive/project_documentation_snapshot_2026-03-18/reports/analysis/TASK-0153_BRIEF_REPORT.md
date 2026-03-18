# TASK-0153 BRIEF REPORT — power-loss safe run artifacts + localhost STOP control (opt-in) + rehearsal runbook

Branch: `test`

## What Changed (In Git)

- Durability contract spec:
  - `docs/spec/POWERLOSS_SAFE_RUN_ARTIFACTS.md`
- exp_0017 crash-safe artifacts hardened:
  - `experiments/exp_0017_comprehension_v0_cloze/src/train.py`
  - Added terminal marker (`RUN_END`) in `metrics_by_step.jsonl` for completion/crash/stop.
  - Added `STOPPED.json` terminal artifact for cooperative stop.
  - Added `run_tag` into `RUN_METADATA.json` (traceability).
  - Added knobs: `--durable_writes`, `--status_every_sec`, `--stop_file`, `--stop_check_every_steps`.
- Localhost server STOP endpoint (loopback-only, token-gated, opt-in):
  - `ui/pacman_viz/src/localhost_server.py` (`POST /control/stop` writes `<run_dir>/STOP_REQUEST.json` atomically)
  - `ui/pacman_viz/schema/control.schema.json`
- Viewer STOP button (Live mode; no training coupling):
  - `ui/pacman_viz/src/viewer.html`
- Orchestrator wiring for STOP (token generation; passes run_dir to server):
  - `tools/launchers/exp0017_live_run.py` (`--enable_stop_control`)
- Tests (CPU-only):
  - `tests/test_powerloss_safety_contract.py`
  - `tests/test_localhost_stop_endpoint_loopback_token.py`
  - `tests/test_train_stop_graceful_writes_metrics_or_crash.py`

## Canon Guarantees

- No changes to exp_0017 learning semantics or metric definitions.
- STOP control is opt-in, localhost-only (`127.0.0.1`), and implemented via a cooperative file request:
  - server writes `STOP_REQUEST.json`
  - trainer polls and writes `STOPPED.json` + `RUN_END` marker

## How To Rehearse (Short)

Runbook: `reports/analysis/TASK-0153_MONITORING_COMMANDS.md`

## Verification

- `pytest -q` PASS.

