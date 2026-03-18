# TASK-0172 BRIEF REPORT

## Scope
- Live-validate backup ops readiness (manual + scheduler + additional backup + safe restore verification).
- Add Cloudflare Tunnel docker ingress scaffold for `queen.bdc-hive.com`.
- Switch friend one-click bundles (Windows/macOS) to `QUEEN_URL.txt` + `JOIN_CODE.txt`.

## Changes
- Added cloudflared ingress scaffold:
  - `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
  - `tools/hive_core_mvp/tools/ingress/cloudflared/.env.example`
  - `tools/hive_core_mvp/tools/ingress/cloudflared/README.md`
- Updated Windows one-click launcher to file-based inputs:
  - `tools/hive_core_mvp/drone_client/START_HIVE.bat` (reads `QUEEN_URL.txt`, `JOIN_CODE.txt`)
  - `tools/hive_core_mvp/drone_client/QUEEN_URL.txt`
  - `tools/hive_core_mvp/drone_client/JOIN_CODE.txt` (empty placeholder)
- Updated macOS one-click launcher to file-based inputs:
  - `tools/hive_core_mvp/drone_client_macos/START_HIVE.command`
  - `tools/hive_core_mvp/drone_client_macos/QUEEN_URL.txt`
  - `tools/hive_core_mvp/drone_client_macos/JOIN_CODE.txt` (empty placeholder)
- Updated bundle builders:
  - `tools/hive_core_mvp/drone_client/build_zip.ps1`
  - `tools/hive_core_mvp/drone_client_macos/build_zip.sh`
- Updated traceability artifacts:
  - `dist/BUNDLE_MANIFEST.json`
  - `dist/BUNDLE_MANIFEST_MACOS15.json`
  - `dist/HIVE_DRONE_ONECLICK_LAPTOP.zip.sha256`
  - `dist/HIVE_DRONE_ONECLICK_MACOS15.zip.sha256`
- Updated runbook: `tools/hive_core_mvp/README_RUNBOOK.md`.

## Verification (L0)

### A) Backup live checks
- Manual backup run: PASS
  - `hive_db_20260218T000609Z.sql.gz` + sidecar created.
- Scheduled task install/query: PASS
  - `BDC_HIVE_DB_BACKUP_30MIN` exists, 30-minute repetition visible in `schtasks /Query`.
- Additional backups observed: PASS (scheduler/manual trigger path)
  - `hive_db_20260218T000809Z.sql.gz`
  - `hive_db_20260218T000825Z.sql.gz`
- Safe restore verification (temporary container): PASS
  - Latest backup restored into `hive-restore-test` (`restore_db`)
  - Counts:
    - `hive_drones=8`
    - `hive_tasks=7`
    - `hive_results=7`

### B) Cloudflare tunnel
- Local baseline ping: PASS
  - `curl http://127.0.0.1:8080/v1/ping` => `ok:true`
- Cloudflared container launch with placeholder token: expected FAIL
  - Logs: `Provided Tunnel token is not valid.`
- Public HTTPS verification:
  - `curl https://queen.bdc-hive.com/v1/ping` => DNS resolve failure in this session.

### C) Client bundles and launcher behavior
- Windows launcher file-based input:
  - Empty `JOIN_CODE.txt` => friendly FAIL (expected).
  - Local test with temporary file values => PASS:
    - `drone_id=fc2556a9-a4d1-4795-89c6-2c90e4cb8277`
    - `task_id=cb35137e-4616-435d-b976-f4893fb33b79`
    - `accepted=True`
    - log: `tools/hive_core_mvp/drone_client/drone_mvp_log_20260218T001447Z.txt`
  - DB correlation for same run: PASS (drone/task/result rows aligned).
- macOS launcher:
  - Empty `JOIN_CODE.txt` => friendly FAIL (expected).
  - Full success run not executed in this Windows-hosted session.

### D) Bundle outputs
- Windows bundle manifest includes `QUEEN_URL.txt` and `JOIN_CODE.txt`:
  - ZIP hash: `19744c1dd806ffb1506882d05764494a689c8bc95776d5ef08f73dcd446cd0ec`
- macOS bundle manifest includes `QUEEN_URL.txt` and `JOIN_CODE.txt`:
  - ZIP hash: `48d93fdea45641f37f99e4165c2c0121fd1d31dd15774d74c948a4cbdac210c8`

## Artifacts
- `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
- `tools/hive_core_mvp/tools/ingress/cloudflared/.env.example`
- `tools/hive_core_mvp/tools/ingress/cloudflared/README.md`
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- `tools/hive_core_mvp/drone_client/QUEEN_URL.txt`
- `tools/hive_core_mvp/drone_client/JOIN_CODE.txt`
- `tools/hive_core_mvp/drone_client/build_zip.ps1`
- `tools/hive_core_mvp/drone_client_macos/START_HIVE.command`
- `tools/hive_core_mvp/drone_client_macos/QUEEN_URL.txt`
- `tools/hive_core_mvp/drone_client_macos/JOIN_CODE.txt`
- `tools/hive_core_mvp/drone_client_macos/build_zip.sh`
- `dist/BUNDLE_MANIFEST.json`
- `dist/BUNDLE_MANIFEST_MACOS15.json`
- `dist/HIVE_DRONE_ONECLICK_LAPTOP.zip.sha256`
- `dist/HIVE_DRONE_ONECLICK_MACOS15.zip.sha256`
- `tools/hive_core_mvp/README_RUNBOOK.md`

## Risks / Limitations
- `queen.bdc-hive.com` HTTPS path is not validated end-to-end in this session because real Cloudflare tunnel token and DNS route were not available.
- Second backup was validated via immediate trigger/manual execution, not by waiting full 30–40 minutes wall-clock in-session.
- macOS success run remains unverified on a real macOS host in this session.

## Rollback
- Stop ingress container:
  - `cd tools/hive_core_mvp/tools/ingress/cloudflared`
  - `docker compose down`
- Delete backup task if needed:
  - `schtasks /Delete /TN BDC_HIVE_DB_BACKUP_30MIN /F`
