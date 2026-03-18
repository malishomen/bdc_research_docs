# TASK-0154 BRIEF REPORT — 5m durability cadence + dual STOP controls + orchestrated live runs

Branch: `test`

## What Changed (In Git)

- Durability cadence + dual STOP:
  - `experiments/exp_0017_comprehension_v0_cloze/src/train.py`
  - `tools/analysis/exp0017_artifact_integrity_check.py`
  - `tools/analysis/exp0017_write_policy_sidecar.py` (run_tag resolution fix when invoked with `--run_dir`)
  - `docs/spec/POWERLOSS_SAFE_RUN_ARTIFACTS.md`
- Dual STOP endpoints (localhost-only; token-gated):
  - `ui/pacman_viz/src/localhost_server.py`
  - `ui/pacman_viz/schema/control.schema.json`
  - `ui/pacman_viz/src/viewer.html`
- Orchestrator: fixed `--control_token` option + final sidecar write:
  - `tools/launchers/exp0017_live_run.py`
- Monitoring + validation:
  - `reports/analysis/TASK_0154_MONITORING_COMMANDS.md`
  - `reports/analysis/TASK_0154_L0_VALIDATION_BUNDLE.md`

## Key Canon Points

- No changes to exp_0017 learning semantics or metric definitions (control-plane + durability only).
- STOP control is localhost-only (`127.0.0.1`) and opt-in; viewer only sends requests; training polls a STOP request file.
- Durability window: intermediate artifacts may be up to `--durable_interval_sec=300` stale under power loss, while terminal artifacts are always durable immediately.

## Verification

- `pytest -q` PASS.
