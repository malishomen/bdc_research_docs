# TASK-1000 INFRASTRUCTURE MAP (L0)

## Scope
- Read-only infrastructure intake for BDC + HIVE.
- No runtime/config mutation performed in this task.

## Git Branches (local + remote)
- Local:
  - `copilot/check-actions-errors` @ `ae02a20`
  - `feature/trl7_wiki_adaptation` @ `42fb1ae`
  - `feature/trl8_bootstrap` @ `7c6732c`
  - `hive` @ `e9557a8`
  - `main` @ `fbab0e5`
  - `test` @ `b70ef9f`
- Remote (`origin/*`):
  - `origin/copilot/check-actions-errors` @ `ae02a20`
  - `origin/deploy/queen-prod` @ `9001d4b`
  - `origin/feature/trl8_bootstrap` @ `b116a66`
  - `origin/main` @ `fbab0e5`
  - `origin/test` @ `0266e7e`

## Current HEAD Commit (all branches)
- Workspace host HEAD (`main`): `fbab0e5`
- Queen repo HEAD (`deploy/queen-prod`): `e9557a8`

## Active Deployment Branch
- Queen host (SSH L0): `deploy/queen-prod` (from `~/bdc/Bio_digital_core`).

## GitHub Actions Workflows (full list)
- `.github/workflows/dispatch.yml`

## Auto-deploy Configuration
- No autonomous CI deploy workflow found in `.github/workflows`.
- `dispatch.yml` contains manual `workflow_dispatch` only (echo + optional GitHub API ping with `ORCHESTRATOR_TOKEN`).

## Server IP / Hostname (secrets redacted)
- Queen hostname: `bdc-queen`
- Queen LAN IP (used for SSH in this intake): `192.168.1.100`
- Public hostnames referenced by runbooks:
  - `queen.bdc-hive.com`
  - `viz.bdc-hive.com`
  - `control.bdc-hive.com`

## SSH Connection Method
- Method in use: key-based SSH.
- Verified command (L0):
  - `ssh -o BatchMode=yes bdc@192.168.1.100 "hostname"`

## Deployment Directories (absolute paths)
- Workspace host repo:
  - `D:\projects\Bio_Digital_Core\Bio_digital_core`
- Queen repo:
  - `~/bdc/Bio_digital_core`
- Queen HIVE stack directory:
  - `~/bdc/Bio_digital_core/tools/hive_core_mvp`
- Queen external backup mount:
  - `/mnt/HIVE/HIVE_BACKUPS`

## Environment Variables (names only, no secrets)
- From `tools/hive_core_mvp/.env.example` + ingress `.env.example` + `main.py`:
  - `POSTGRES_DB`
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `HIVE_API_VERSION`
  - `HIVE_INVITE_CODE`
  - `TOKEN_TTL_HOURS`
  - `INVITE_TTL_HOURS`
  - `LOG_FILE`
  - `HIVE_BIND_HOST`
  - `HIVE_PORT`
  - `ENABLE_RATE_LIMIT`
  - `RATE_LIMIT_WINDOW_SEC`
  - `RATE_LIMIT_MAX_REQUESTS`
  - `RATE_LIMIT_REGISTER_MAX_REQUESTS`
  - `ENABLE_STRICT_CLIENT_PROOF`
  - `CLIENT_PROOF_MAX_SKEW_SEC`
  - `NONCE_TTL_SEC`
  - `REQUIRE_DEVICE_SIGNATURE`
  - `STATS_ADMIN_TOKEN`
  - `CONTROL_OWNER_TOKEN`
  - `CONTROL_STOP_ENABLED`
  - `CONTROL_STOP_SCRIPT`
  - `CONTROL_STOP_MAX_TIMEOUT_SEC`
  - `FRIEND_BUNDLE_SOURCE_DIR`
  - `FRIEND_BUNDLE_OUTPUT_DIR`
  - `ENABLE_EMAIL_DELIVERY`
  - `SMTP_HOST`
  - `SMTP_PORT`
  - `SMTP_USERNAME`
  - `SMTP_PASSWORD`
  - `SMTP_FROM`
  - `BUNDLE_BASE_URL`
  - `CF_ACCESS_CLIENT_ID`
  - `CF_ACCESS_CLIENT_SECRET`
  - `CLOUDFLARE_ACCESS_CLIENT_ID`
  - `CLOUDFLARE_ACCESS_CLIENT_SECRET`
  - `DIST_PUBLIC_DIR`
  - `PUBLIC_DRONE_HOST`
  - `CLOUDFLARED_TUNNEL_TOKEN`
  - `CLOUDFLARED_VIZ_TUNNEL_TOKEN`
  - `CLOUDFLARED_CONTROL_TUNNEL_TOKEN`
  - `PACMAN_VIZ_PORT`

## Runtime Services (systemd/docker/pm2/etc)
- Workspace host:
  - `systemctl` unavailable (Windows host).
  - Docker running, but containers are unrelated to HIVE (`crm-ops`, `infra-*`, `sadaf_db`).
- Queen host:
  - Docker Compose services (`tools/hive_core_mvp/docker-compose.yml`):
    - `hive-mvp-core` (Up, `127.0.0.1:8080->8080`)
    - `hive-mvp-postgres` (Up healthy, internal `5432/tcp`)
    - `hive-mvp-redis` (Up healthy, internal `6379/tcp`)
  - systemd user units:
    - `bdc-hive-backup.timer` active
    - `bdc-hive-backup.service` triggered by timer
- PM2:
  - UNVERIFIED (no PM2 evidence in this intake).

## HIVE API Endpoints Currently Active (code-mapped)
- `GET /v1/ping`
- `POST /v1/drones/claim`
- `POST /v1/drone/register`
- `POST /v1/drones/register`
- `POST /v1/tasks/poll`
- `POST /v1/drone/poll`
- `POST /v1/tasks/result`
- `POST /v1/drone/submit`
- `GET /v1/stats/drones`
- `GET /v1/stats/summary`
- `POST /v1/control/stop`
- `POST /v1/tokens/revoke`

## Queen Location
- Physical location: UNVERIFIED in this intake.
- Network location: LAN host `192.168.1.100` (`bdc-queen`).

## Drone Execution Model
- One-click client flow (Windows/macOS): `ping -> register/claim -> poll -> execute -> submit`.
- Current friend full-runtime path uses:
  - `START_FULL_RUNTIME.bat`
  - `WindowsDroneOneClick.ps1`
  - local readonly viz runtime (`run_viz_readonly.ps1`).
- Device-bound auth mode implemented in current codebase: ECDSA P-256 claim/signature path (per existing reports).

## Checkpoint Storage Location
- Canonical policy: large artifacts/checkpoints external-only.
- Referenced locations:
  - repo examples under `results/.../checkpoints` (historical artifacts)
  - external dataset/build roots under `D:\datasets\...` (from manifests/specs)
- Active Queen checkpoint path for real training:
  - UNVERIFIED in this intake (no running train shard observed here).

## External Artifact Storage Configuration
- External backup target on Queen:
  - `/mnt/HIVE/HIVE_BACKUPS`
  - subdirs: `db`, `logs`, `manifests`, `ops`
- Dataset external roots referenced:
  - `D:\datasets\wikimedia\simplewiki\20260201\...`
  - `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Wiki Dataset Location
- Source manifest:
  - `datasets/simplified_wiki_v0/MANIFEST.json`
- External dataset pointer:
  - `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Wiki Preprocessing Pipeline Location
- Builder script:
  - `datasets/simplified_wiki_v0/build_dataset.py`
- TRL-7 fetch pipeline (legacy branch path, present in repo history):
  - `experiments/exp_0006_wiki_adaptation/fetch_wikitext.py`

## GPU Detection Logic
- Windows drone:
  - `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1` (hardware probe/log fields include GPU vendor/name).
- macOS drone:
  - `tools/hive_core_mvp/drone_client_macos/START_HIVE.command` (GPU vendor/name/VRAM detection and payload fields).

## CPU Fallback Logic
- Drone payload includes CPU thread count and resource prefs.
- Execution path supports CPU-only operation when GPU unavailable.
- Explicit fallback policy evidence in production runtime:
  - PARTIAL/UNVERIFIED in this intake (no dedicated fallback test executed now).

## Log Directories
- Repo-level logs: `logs/`
- HIVE core logs:
  - `tools/hive_core_mvp/logs/`
  - `tools/hive_core_mvp/logs/hive-core.log`
  - `tools/hive_core_mvp/logs/control/`
  - `tools/hive_core_mvp/logs/pacman_viz_runtime/`
- Drone logs:
  - `tools/hive_core_mvp/drone_client/drone_mvp_log_*.txt`

## Metrics Storage Directories
- HIVE stats persisted in Postgres tables (`hive_stats_daily`, drone/volunteer counters).
- Experiment metrics files (repo/historical):
  - `results/**/metrics.json`
  - `logs/exp_0017_comprehension_v0_cloze/<run>/metrics.json`
- Dataset-derived manifests:
  - `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`

## Verification (L0 Commands Used)
- `git status`
- `git branch -a`
- `git remote -v`
- `git log --oneline -n 5`
- `Get-ChildItem -Recurse | Select-Object -First 200`
- `docker ps`
- `nvidia-smi`
- `python --version`
- `node --version`
- `docker --version`
- `Get-CimInstance Win32_OperatingSystem`
- `Get-CimInstance Win32_Processor`
- `Get-PSDrive -PSProvider FileSystem`
- `ssh ... bdc@192.168.1.100 ...`

## Limits
- This is an intake snapshot. It does not claim real Wiki training currently running.
- `systemctl`, `free -h`, `df -h` are unavailable on Windows workspace host; Linux equivalents were collected from Queen via SSH.
