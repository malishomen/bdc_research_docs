# TASK-0181 PACMAN/STOP INVENTORY (L0, Read-Only)

## Scope
- Read-only inventory of existing Pac-Man visualization and STOP controls in repo.
- Determine how to reuse current components for HIVE bridge (Cloudflare read-only view + owner-only stop) without building a parallel system.

## Baseline Evidence
- Branch: `hive`
- Working tree at start: clean (`git status --short` returned empty)
- Head at audit time: `e60002d`

## Repo Findings (Pac-Man Components)

### Core implementation
- `ui/pacman_viz/src/normalize_run_snapshot.py`
  - Builds normalized snapshot from run artifacts (`RUN_STATUS.json`, `metrics_by_step.jsonl`, `metrics.json`, `CRASH.json`, optional `policy_eval.json`).
  - Evidence: lines around artifact paths and parse flow (`normalize_run_snapshot.py`:230-334 via grep output).
- `ui/pacman_viz/src/snapshot_daemon.py`
  - Periodically writes `snapshot_*.json` + optional `LATEST.json` and daemon status.
  - Evidence: `latest_path = out_dir / "LATEST.json"` (`snapshot_daemon.py`:89).
- `ui/pacman_viz/src/viewer.html`
  - Live URL defaults to `http://127.0.0.1:8848/LATEST.json`.
  - Contains STOP UI controls and posts to same-origin control endpoints.
  - Evidence: `liveUrl` (`viewer.html`:158), stop buttons (`viewer.html`:174/176), POST endpoints (`viewer.html`:484).
- `ui/pacman_viz/src/localhost_server.py`
  - Loopback-only by design (`ALLOWED_BIND = "127.0.0.1"`).
  - Serves only `viewer.html` and direct-child `*.json` from snapshot root.
  - Blocks traversal and non-json file serving.
  - Optional stop control endpoints when control mode enabled.

### Documentation/spec
- `ui/pacman_viz/README.md`
  - Documents offline mode, snapshot daemon, and localhost serving at `127.0.0.1:8848`.
- `docs/EXPERIMENT_VISUALIZATION_PACMAN.md`
  - UX-level visualization spec (higher-level metaphor/UI), not operational stop/auth wiring.

### Orchestrator integration (exp_0017)
- `tools/launchers/exp0017_live_run.py`
  - Orchestrates 4 processes: train, policy sidecar loop, snapshot daemon, localhost server.
  - Emits `VIEWER_URL http://127.0.0.1:<port>/viewer.html` and `LATEST_URL .../LATEST.json`.
  - Can enable stop control via `--enable_stop_control` and token.
  - Evidence: `exp0017_live_run.py`:343-359, 414-416, 454-459.

## Repo Findings (STOP Controls)

### STOP write path (viewer -> file contract)
1. `viewer.html` POSTs to:
   - `/control/stop_emergency`
   - `/control/stop_graceful`
2. `localhost_server.py` validates:
   - endpoint is one of above,
   - `control_token` present and matches JSON body `token`,
   - `control_run_dir` exists.
3. On success server atomically writes `<run_dir>/STOP_REQUEST.json` with mode/reason/ts.
4. `train.py` polls stop file (`--stop_file` or default `<out_dir>/STOP_REQUEST.json`) every N steps and applies:
   - emergency: immediate stop path
   - graceful: stop at next safe boundary (after eval boundary when available)
5. `CrashSafeRunArtifacts` writes terminal artifacts:
   - `STOPPED.json` for stopped flow,
   - `RUN_END` marker in `metrics_by_step.jsonl`,
   - `RUN_STATUS.json` final state update.

Evidence anchors:
- Server endpoints/tokens/write: `ui/pacman_viz/src/localhost_server.py`:127, 156-163.
- Train stop polling/mode handling: `experiments/exp_0017_comprehension_v0_cloze/src/train.py`:454-455, 618-624, 742-743.
- Terminal stop artifacts: `train.py`:910, 987, 1036-1047.
- Tests:
  - `tests/test_localhost_stop_endpoint_loopback_token.py` (403 without token; writes `STOP_REQUEST.json` with emergency mode).
  - `tests/test_localhost_server_loopback_only.py` (loopback bind + traversal protection).

## Dependency on exp_0017 Artifacts
Current Pac-Man implementation is directly artifact-driven and currently expects exp_0017 run_dir structure:
- `RUN_STATUS.json`
- `metrics_by_step.jsonl` (RUN_START/EVAL/RUN_END semantics)
- `metrics.json` or `CRASH.json`
- optional `policy_eval.json`

Conclusion:
- Reuse "as-is" is possible for any HIVE run that produces same contract files.
- If HIVE run artifacts differ, bridging adapter is required (map HIVE run outputs into this contract).

## How To Run Locally (Existing, No New System)

### Viz only (read-only)
```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$run = "logs/exp_0017_comprehension_v0_cloze/<run_dir>"
$out = "ui/pacman_viz/_snapshots/<tag>"
python ui/pacman_viz/src/snapshot_daemon.py --run_dir $run --out_dir $out --interval_sec 60 --write_latest_pointer
python ui/pacman_viz/src/localhost_server.py --root_dir $out --port 8848 --bind 127.0.0.1
# open http://127.0.0.1:8848/viewer.html
```

### Full exp_0017 live orchestration
```powershell
python tools/launchers/exp0017_live_run.py --dataset_root <DATASET_ROOT> --time_budget_minutes 45 --enable_stop_control
```
Outputs include printed `VIEWER_URL`/`LATEST_URL` and control token when stop control enabled.

## Security Boundary Analysis

### Safe for volunteer exposure (read-only)
- `viewer.html` + snapshot JSON (`LATEST.json`, `snapshot_*.json`) from localhost server.
- No training mutation path when stop control is disabled.

### Owner-only control path
- STOP endpoints are token-gated and only exist when server started with `--control_run_dir` + `--control_token`.
- Default binding is loopback-only (`127.0.0.1`), reducing accidental WAN exposure.

### Risks if exposed without policy
- If same server instance is internet-exposed with stop enabled and token leaks, remote stop is possible.
- Viewer currently includes stop UI elements; access control must be network/policy enforced, not UI-trust.

## Reuse Plan For HIVE (Minimal Bridge, No Parallel System)

### Keep as-is
- `normalize_run_snapshot.py`, `snapshot_daemon.py`, `viewer.html`, `localhost_server.py`, stop file contract, exp_0017 stop semantics.

### Minimal bridge steps
1. Keep Pac-Man server loopback-only on Queen (`127.0.0.1:<viz_port>`).
2. Start two operation modes from same codebase:
   - Volunteer view: server instance without control flags (read-only).
   - Owner control: either local-only owner session OR separate protected ingress with stronger Access policy and stop enabled.
3. If exposing via Cloudflare:
   - Route to Pac-Man server loopback target (through cloudflared internal mapping).
   - Apply read-only Access policy for volunteer app.
   - Keep stop-enabled endpoint owner-only (separate policy/app path, or do not expose stop-enabled instance publicly).
4. HIVE artifact bridge:
   - If HIVE emits exp_0017-compatible run artifacts, direct reuse.
   - Else add adapter that writes compatible run_dir contract; do not rewrite viz system.

## Existing Remote Exposure Readiness (Found)
- Cloudflare ingress scaffolding for HIVE exists:
  - `tools/hive_core_mvp/docker-compose.yml` (`cloudflared` -> `http://hive-core:8080`)
  - `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
  - `tools/hive_core_mvp/tools/ingress/cloudflared/check_no_public_ports.ps1`
  - `tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
- This ingress currently targets `hive-core`, not Pac-Man localhost server by default.

## UNVERIFIED Items + How To Verify
1. Direct HIVE->Pac-Man artifact compatibility beyond exp_0017 schema.
   - Verify by pointing `snapshot_daemon.py` at HIVE-produced run_dir and checking `LATEST.json` validity.
2. Production Cloudflare route for Pac-Man read-only endpoint.
   - Verify with dedicated route and `curl -i https://<viz-host>/LATEST.json` under Access policy.
3. Owner-only stop exposure model in live internet setup.
   - Verify with two policies: volunteer cannot POST stop; owner can POST with token; collect 403/200 evidence.

## L0 Command Evidence Used
- `git status`
- `git rev-parse --abbrev-ref HEAD`
- `ls -R ui/pacman_viz`
- `ls -R tools/launchers`
- `ls -R experiments/exp_0017_comprehension_v0_cloze`
- `rg -n "STOP_REQUEST\.json|/stop|graceful|emergency|localhost_server|snapshot_daemon|pacman_viz|LATEST\.json|RUN_STATUS\.json" -S .`
- `rg -n "EXPERIMENT_VISUALIZATION_PACMAN|COMPLETED|RUN_END|metrics_by_step" -S docs ui tools experiments`
- `rg -n "cloudflared|queen\.bdc-hive\.com|viz" -S tools/hive_core_mvp`

## Rollback
- N/A (read-only analysis/report only).
