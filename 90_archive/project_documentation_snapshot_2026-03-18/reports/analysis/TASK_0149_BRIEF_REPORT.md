# TASK-0149 BRIEF REPORT — Pac-Man viz Variant B (localhost-only) + live auto-refresh + atomic snapshots (runbook)

Branch/HEAD (start): `test` @ `e87c5f48c5d4f35e46e7ef9ee3c2bcffcfbe4af9`

## What Changed (In Git)

- Localhost server (loopback-only; snapshot-root only):
  - `ui/pacman_viz/src/localhost_server.py`
  - Binds strictly to `127.0.0.1` and serves:
    - `/viewer.html` (single file)
    - `/*.json` only (direct children of `--root_dir`; blocks traversal)
  - JSON responses include `Cache-Control: no-store`.
- Viewer live mode (no deps; polling; explicit NO DATA/STALE/ERROR):
  - Updated: `ui/pacman_viz/src/viewer.html`
  - Keeps offline file-picker mode intact.
  - Live mode polls a user-provided URL (default `http://127.0.0.1:8848/LATEST.json`) with `cache:'no-store'`.
  - STALE rule (viewer-only): if `snapshot.ts_utc` unchanged for `> 2 * snapshot_interval_sec` => banner `STALE`.
- Readme updated for Variant B:
  - `ui/pacman_viz/README.md`
- Monitoring/runbook:
  - `reports/analysis/TASK_0149_MONITORING_COMMANDS.md`
- Tests:
  - `tests/test_localhost_server_loopback_only.py`
  - `tests/test_snapshot_daemon_atomic_latest.py`
  - `tests/test_viewer_live_mode_smoke.py`

## Canon Constraints (Upheld)

- No changes to exp_0017 training semantics or metric definitions.
- Visualization is read-only and offline-first; localhost server is optional and loopback-only.
- No fabricated visuals: viewer displays explicit LIVE/ERROR/STALE states; missing artifacts must not be interpolated.
- Runtime outputs remain gitignored (`logs/**`, `ui/pacman_viz/_snapshots/**`).

## How To Run (Variant B)

Runbook:
- `reports/analysis/TASK_0149_MONITORING_COMMANDS.md` (Terminal A/B/C/D + post-run checks)

Bind proof (expected server stdout line):
- `BIND_OK host=127.0.0.1 port=8848 root_dir=... viewer=...`

## Verification

- `pytest -q` PASS.

## 45m Run Results

Not executed in this task by design (runbook + tooling only). Record outcomes in a follow-on L0 report after running the protocol.

