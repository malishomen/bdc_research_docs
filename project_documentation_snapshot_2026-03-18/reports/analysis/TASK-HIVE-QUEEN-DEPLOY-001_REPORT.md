# TASK-HIVE-QUEEN-DEPLOY-001 DEPLOY REPORT

## Scope
- Deploy HIVE core stack on Ubuntu laptop `bdc-queen`.
- Verify local operational readiness with L0 evidence.
- Configure external backup disk mount and backup automation.

## Environment (L0)
- Host: `bdc-queen`
- OS: `Ubuntu 24.04.4 LTS`
- Docker: `28.2.2`
- Docker Compose: `2.37.1`
- Storage driver: `overlay2`
- Repo path: `/home/bdc/bdc/Bio_digital_core`
- Branch/HEAD on Queen: `hive @ e9557a8`

## Deployment steps executed
1. Verified baseline OS/runtime/SSH.
2. Mounted external backup disk:
   - `/dev/sdb1` (`LABEL=HIVE`, UUID `3680D1BD80D183B1`) -> `/mnt/HIVE`.
   - Added persistent `/etc/fstab` entry and verified write access.
3. Deployed HIVE core stack:
   - `cd /home/bdc/bdc/Bio_digital_core/tools/hive_core_mvp`
   - `docker compose up -d --build`
4. Verified local API:
   - `curl -s http://127.0.0.1:8080/v1/ping | jq .`
5. Configured backup automation:
   - Manual backup PASS to `/mnt/HIVE/HIVE_BACKUPS/db`.
   - User timer `bdc-hive-backup.timer` enabled (`every 30 min`).
   - Fixed systemd execution context issue (user service missing docker group in systemd session) by wrapper-based launch.
6. Sanitized backup directory:
   - Removed truncated `.sql.gz` artifacts without sidecar.

## L0 verification evidence

### Core stack
- `docker compose ps`:
  - `hive-mvp-core` Up
  - `hive-mvp-postgres` Up (healthy)
  - `hive-mvp-redis` Up (healthy)
- Local health:
  - `/v1/ping` returned `ok=true`, `service=hive-core`, `version=0.1.0`

### Host and resources
- Load average baseline:
  - `0.40 0.19 0.13 ...`
- Free space:
  - `/` ~85G free
  - `/mnt/HIVE` ~932G free

### Backups
- Latest successful backups observed in `/mnt/HIVE/HIVE_BACKUPS/db`:
  - `hive_db_20260218T224333Z.sql.gz(.json)`
  - `hive_db_20260218T225006Z.sql.gz(.json)`
  - `hive_db_20260218T225129Z.sql.gz(.json)`
- Timer status:
  - `bdc-hive-backup.timer` active, next trigger scheduled
- Manual service run:
  - `bdc-hive-backup.service` finished successfully after wrapper fix

## Issues found and resolution

1. `bdc-hive-backup.service` failed with `203/EXEC` and later `status=1`.
- Root causes:
  - incorrect compose path defaults in non-interactive user service context;
  - systemd user session not carrying `docker` supplementary group.
- Resolution:
  - set explicit compose/backup paths;
  - run backup command via `sg docker` wrapper script in service `ExecStart`;
  - reload/reset/start service and verify success.

2. Cloudflare ingress on Queen laptop not finalized.
- `tools/ingress/cloudflared` container currently loops with:
  - `Provided Tunnel token is not valid.`
- This is a credentials/tunnel-control-plane issue, not HIVE core failure.

## Acceptance criteria status
- `docker compose ps` all core services Up: **PASS**
- postgres healthy: **PASS**
- `/v1/ping` returns `ok=true`: **PASS**
- no core restart loops: **PASS**
- backup automation operational: **PASS** (after service fix)
- cloudflared ingress on laptop: **FAIL** (invalid tunnel token)

## Final status
- **PARTIAL**
- Core Queen deployment is operational and backup-ready.
- Remaining blocker to full external cutover: valid Cloudflare tunnel token for laptop ingress.

## Next actions to close to SUCCESS
1. Generate/rotate valid `CLOUDFLARED_TUNNEL_TOKEN` for laptop connector.
2. Place token into:
   - `/home/bdc/bdc/Bio_digital_core/tools/hive_core_mvp/tools/ingress/cloudflared/.env`
3. Restart ingress stack:
   - `docker compose up -d` (in cloudflared dir)
4. Re-run external proof:
   - `https://queen.bdc-hive.com/v1/ping` with Access headers -> `STATUS=200` JSON.
