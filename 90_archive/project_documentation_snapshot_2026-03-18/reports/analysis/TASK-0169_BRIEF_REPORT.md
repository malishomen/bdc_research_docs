# TASK-0169 BRIEF REPORT

- Task: `TASK-0169`
- Date (UTC): `2026-02-17`
- Branch: `hive`
- Status: `PARTIAL`

## Implemented

1. macOS one-click launcher:
- `tools/hive_core_mvp/drone_client_macos/START_HIVE.command`

2. Safe macOS config template:
- `tools/hive_core_mvp/drone_client_macos/config.ini`

3. Friend one-line instruction:
- `tools/hive_core_mvp/drone_client_macos/README_FOR_FRIEND.txt`

4. macOS bundle builder:
- `tools/hive_core_mvp/drone_client_macos/build_zip.sh`

5. Runbook updates:
- `tools/hive_core_mvp/README_RUNBOOK.md` (macOS section + build instructions)

6. Dist artifacts:
- `dist/HIVE_DRONE_ONECLICK_MACOS15.zip.sha256`
- `dist/BUNDLE_MANIFEST_MACOS15.json`

## Launcher Behavior

- Reads `QUEEN_URL`, `INVITE_CODE`, `HOST_LABEL` from `config.ini`.
- Best-effort hardware profile via:
  - `sw_vers`
  - `sysctl -n hw.logicalcpu`
  - `sysctl -n hw.memsize`
  - `system_profiler SPDisplaysDataType`
- Tailscale checks:
  - if CLI missing or logged out: friendly stop with instruction to install/login and rerun.
- API flow:
  - `/v1/ping` -> `/v1/drones/register` -> `/v1/tasks/poll` -> `/v1/tasks/result`
- Logging:
  - `drone_mvp_log_<UTC>.txt` in same folder
  - includes timestamps + `drone_id/task_id/task_hash/accepted`
  - invite code masked; token never printed.
- UX:
  - clear SUCCESS/FAIL banner
  - pause at end (`HIVE_NO_PAUSE=1` for non-interactive verification)

## Build and Traceability Evidence

Build command:
```bash
bash tools/hive_core_mvp/drone_client_macos/build_zip.sh
```

ZIP hash:
- `8a917f53afdc31f715532f46ec91c8da2fa7c96a3cd2b9aa673fd23f9b7d9220`

Matching outputs:
- `shasum -a 256 dist/HIVE_DRONE_ONECLICK_MACOS15.zip`
- `dist/HIVE_DRONE_ONECLICK_MACOS15.zip.sha256`
- `dist/BUNDLE_MANIFEST_MACOS15.json`

ZIP contents:
- `config.ini` (placeholder invite only)
- `README_FOR_FRIEND.txt`
- `START_HIVE.command`

Forbidden secret files absent from ZIP:
- `hive_join.conf`
- `.env`
- token files

## Verification Runs (Current Host)

1. Placeholder invite check:
- command: `HIVE_NO_PAUSE=1 bash tools/hive_core_mvp/drone_client_macos/START_HIVE.command`
- result: friendly fail `INVITE_CODE is not set...`
- log file created.

2. Missing Tailscale CLI check:
- with temporary non-placeholder invite in local config
- result: friendly fail `Install Tailscale and log in once, then rerun.`
- log file created.

## Remaining Gap

- Full SUCCESS flow (`accepted=true`) was not executed on an actual macOS 15 machine connected via Tailscale in this session.
- After first live macOS run, append DB correlation evidence (drone/task/result + task_hash + timestamps) to close this as `SUCCESS`.
