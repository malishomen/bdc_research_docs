# TASK-0148 BRIEF REPORT — Pac-Man viz: policy sidecar + 1-min snapshots + governed 45m run (L0-first; no metric loss)

Branch/HEAD (start): `test` @ `bd2120a3cb8bae8052f6474ef41b9c2af412adf8`

## What Changed (In Git)

- Policy sidecar writer (external tooling; file-based):
  - `tools/analysis/exp0017_write_policy_sidecar.py`
  - Writes `<run_dir>/policy_eval.json` atomically with explicit exit_code->quaternary mapping.
- Snapshot daemon (read-only; separate process):
  - `ui/pacman_viz/src/snapshot_daemon.py`
  - Writes snapshots to `ui/pacman_viz/_snapshots/...` (gitignored) and optional `LATEST.json`.
- Schema updates:
  - `ui/pacman_viz/schema/policy_eval.schema.json`
  - `ui/pacman_viz/schema/run_snapshot.schema.json` (adds `quat_source` + optional `policy` snippet; adds `running/crashed`)
- Normalizer updated for sidecar ingestion:
  - `ui/pacman_viz/src/normalize_run_snapshot.py`
- Docs:
  - `reports/analysis/TASK_0148_MONITORING_COMMANDS.md`
  - `docs/spec/PACMAN_VISUALIZATION_IMPLEMENTATION_PLAN.md` (policy sidecar + 1-min snapshot mode)
- Tests:
  - `tests/test_pacman_viz_policy_sidecar_ingestion.py`
  - `tests/test_snapshot_daemon_deterministic_write.py`
  - `tests/test_exp0017_write_policy_sidecar_exitcode_mapping.py`

## Canon Constraints (Upheld)

- Visualization pipeline is read-only and offline-first (no network required).
- No changes to exp_0017 training semantics or metric definitions.
- No synthetic signals: missing/stale artifacts -> `data_status` indicates `no_data/incomplete/running/crashed`.
- Large runtime artifacts are not committed (`logs/**`, `ui/pacman_viz/_snapshots/**` are gitignored).

## Quaternary Policy Sidecar (L0)

Sidecar file:
- `<run_dir>/policy_eval.json` (schema: `ui/pacman_viz/schema/policy_eval.schema.json`)

Exit-code mapping (explicit; L0; viewer-only):
- exit_code `0` => `YES`
- exit_code `2` => `NO`
- exit_code `1` => `MAYBE_NO` (error/unknown; never treated as YES)

## Governed Run Protocol (45m) + Monitoring

Runbook:
- `reports/analysis/TASK_0148_MONITORING_COMMANDS.md` (Terminal A/B/C + post-run checks)

Required post-run L0 checks:
- Training artifacts: `RUN_STATUS.json`, `metrics_by_step.jsonl`, and terminal `metrics.json` OR `CRASH.json`
- Artifact integrity: `python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash` => PASS
- Policy sidecar exists and is parseable
- Snapshots: `>= 40` files for a 45-minute run (plus optional `LATEST.json`)

## Verification (Code)

- `pytest -q` PASS.

## Run Results (To Be Filled After Execution)

This section is intentionally L0-only. After the 45m run completes, record:
- run_tag: `task0148_quality_45m_viz`
- resolved run_dir: `<RUN_DIR>`
- git_head_run (from `RUN_METADATA.json`): `<SHA>`
- final_step (from `metrics.json`): `<INT>`
- final val/test acc + baselines (from `metrics.json`)
- policy_eval.json sha256 + key fields: exit_code, quaternary_state, verdict
- snapshot_dir: `ui/pacman_viz/_snapshots/task0148_quality_45m_viz` (gitignored)
- snapshot_count + example snapshot sha256

