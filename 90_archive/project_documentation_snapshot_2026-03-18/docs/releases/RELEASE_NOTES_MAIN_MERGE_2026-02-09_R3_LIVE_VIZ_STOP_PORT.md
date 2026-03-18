# Release Notes — Main Merge Checkpoint (2026-02-09) — R3 Live Viz + STOP + Port Auto-Select

Scope:
- Merge `test` -> `main` after TASK-0154 and TASK-0155.

Canon invariants (explicit):
- No changes to `exp_0017` learning semantics or metric definitions (model/tokenizer/masking/loss/optimizer unchanged).
- Changes are limited to durability/control-plane/orchestration/visualization plumbing and tests.
- Runtime artifacts are not committed: `logs/**` and `ui/pacman_viz/_snapshots/**` remain gitignored; datasets remain external-only.

What landed in `main`:
- **Durability cadence (power-loss window)**: bounded staleness via `--durable_interval_sec=300` while keeping terminal artifacts durable immediately.
  - `experiments/exp_0017_comprehension_v0_cloze/src/train.py`
  - Spec: `docs/spec/POWERLOSS_SAFE_RUN_ARTIFACTS.md`
- **Dual STOP controls (localhost-only, token-gated)**:
  - Emergency stop (fast stop; terminal `STOPPED.json` valid)
  - Graceful stop (stop at safe boundary; prefers producing `metrics.json`)
  - `ui/pacman_viz/src/localhost_server.py`, `ui/pacman_viz/src/viewer.html`, `ui/pacman_viz/schema/control.schema.json`
- **Single-command live run orchestrator** (train + policy sidecar loop + snapshot daemon + localhost server):
  - `tools/launchers/exp0017_live_run.py`
  - L0 sidecars: port selection and launch manifest under `logs/.../_launchers/` (gitignored)
- **Port auto-selection (loopback-only)**:
  - Preferred port is scanned upward on `127.0.0.1` to find a free port (Windows-safe).
  - `--port_preferred`, `--port_auto`, `--port_scan_max`
- **Pac-Man visualization scaffold (read-only, file-based)**:
  - `ui/pacman_viz/` (viewer + normalizer + snapshot daemon + schemas)
  - Implementation plan: `docs/spec/PACMAN_VISUALIZATION_IMPLEMENTATION_PLAN.md`
- **Tests**:
  - Added/expanded CPU-only tests for durability contracts, STOP endpoints, snapshot atomicity, and orchestrator port auto-select.

User-facing outcomes:
- Live viewer loads from `http://127.0.0.1:<port>/viewer.html` and polls `LATEST.json` (no-store).
- STOP buttons (emergency / graceful) are available only when stop control is enabled and a token is provided.
- Orchestrator prints `CHOSEN_PORT`, `VIEWER_URL`, `LATEST_URL`, `RUN_DIR`, and writes a `PORT_SELECTION_<run_tag>.json` (gitignored).

