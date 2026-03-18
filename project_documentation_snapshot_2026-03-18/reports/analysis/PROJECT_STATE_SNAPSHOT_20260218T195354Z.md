# PROJECT STATE SNAPSHOT

- **Captured UTC:** 2026-02-18T19:53:54Z
- **Repository:** `d:\projects\Bio_Digital_Core\Bio_digital_core`
- **Branch:** `main`
- **HEAD:** `7ee37ce2ab229754be067d2e0108e2beaf73a64a`
- **Working tree:** clean (`git status --short` empty)
- **Remote:** `origin git@github.com:malishomen/Bio_Digital_Core.git`

## Git (latest commits)

1. `7ee37ce` merge: bring TASK-0183 runtime compatibility fixes from hive
2. `e9557a8` fix(TASK-0183): stabilize Windows claim signatures and log L0 runtime proof
3. `e881583` docs(TASK-0183,TASK-0184,TASK-0185): append weekly status and hash backfill logs
4. `1c1eec5` docs(TASK-0185): add ubuntu migration runbook and linux backup automation scripts
5. `d34e078` docs(TASK-0184): document remote e2e proof closure checklist and status

## Runtime status

### HIVE core stack (`tools/hive_core_mvp/docker-compose.yml`)
- `hive-mvp-core`: Up, `127.0.0.1:8080->8080/tcp`
- `hive-mvp-postgres`: Up (healthy), `0.0.0.0:5433->5432/tcp`
- `hive-mvp-redis`: Up (healthy), `0.0.0.0:6379->6379/tcp`

### Cloudflare ingress stacks
- `tools/hive_core_mvp/tools/ingress/cloudflared`: running (`hive-cloudflared` Up)
- `tools/hive_core_mvp/tools/ingress/cloudflared_viz`: no running containers
- `tools/hive_core_mvp/tools/ingress/cloudflared_control`: no running containers

## L0 health checks

- Local ping:
  - Command: `curl.exe -s http://127.0.0.1:8080/v1/ping`
  - Result: `{"ok":true,...,"service":"hive-core","version":"0.1.0"}`
- Cloudflare Access ping:
  - Command: `pwsh -File tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
  - Result: `STATUS=200`, `CONTENT_TYPE=application/json`, `LOOKS_JSON=True`

## DB counters (Postgres `hive`)

- `hive_drones`: 15
- `hive_tasks`: 12
- `hive_results`: 11
- `hive_device_keys`: 4

Command used:
`docker compose exec -T postgres psql -U hive -d hive -c "select count(*) ..."`

## Artifacts inventory (recent)

- Recent analysis reports exist up to:
  - `reports/analysis/TASK-0185_BRIEF_REPORT.md`
  - `reports/analysis/TASK-0184_BRIEF_REPORT.md`
  - `reports/analysis/TASK-0183_BRIEF_REPORT.md`
  - `reports/analysis/TASK-0182A_BRIEF_REPORT.md` ... `TASK-0182D_BRIEF_REPORT.md`
- Dist bundles exist in:
  - `tools/hive_core_mvp/dist/`
  - Includes multiple `HIVE_FRIEND_*.zip`, `*.sha256`, `BUNDLE_MANIFEST_FRIEND_*.json`

## Notable open status from logs

- `TASK-0183`: PARTIAL (runtime claim flow works with `accepted=True`; anti-forwarded ZIP L0 test still pending).
- `TASK-0184`: PARTIAL (remote owner-context proofs for 0182A/B/C/D still pending).

