# TASK-0175 BRIEF REPORT

## Scope
- Remove public `0.0.0.0:8080` exposure for `hive-core`.
- Keep Cloudflare Access path functional.
- Align cloudflared runtime toward internal service routing.

## Changes
- Updated `tools/hive_core_mvp/docker-compose.yml`:
  - `hive-core` publish fixed to `127.0.0.1:8080:8080`.
  - Added shared Docker network `hive_mvp_net`.
  - Added optional `cloudflared` service (profile `ingress`) on same network.
- Updated `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`:
  - Attached to external `hive_mvp_net`.
  - Added `--url http://hive-core:8080` in command.
- Added guardrail script:
  - `tools/hive_core_mvp/tools/ingress/cloudflared/check_no_public_ports.ps1`
- Updated docs:
  - `tools/hive_core_mvp/tools/ingress/cloudflared/README.md`
  - `tools/hive_core_mvp/README_RUNBOOK.md`

## Verification (L0)
- Command: `cd tools/hive_core_mvp && docker compose ps`
- Result: `hive-mvp-core ... 127.0.0.1:8080->8080/tcp` (no `0.0.0.0:8080`).

- Command: `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/tools/ingress/cloudflared/check_no_public_ports.ps1`
- Result:
  - `PUBLIC_IPV4_8080=False`
  - `PUBLIC_IPV6_8080=False`
  - `PASS: no public 8080 mapping detected for hive-core.`

- Command: `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
- Result:
  - `STATUS=200`
  - `CONTENT_TYPE=application/json`
  - `LOOKS_JSON=True`

- Command: `docker logs hive-cloudflared --tail 40`
- Result includes runtime settings with internal URL flag:
  - `Settings: ... url:http://hive-core:8080`

## Artifacts
- `tools/hive_core_mvp/docker-compose.yml`
- `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
- `tools/hive_core_mvp/tools/ingress/cloudflared/check_no_public_ports.ps1`
- `tools/hive_core_mvp/tools/ingress/cloudflared/README.md`
- `tools/hive_core_mvp/README_RUNBOOK.md`

## Risks / Limitations
- Cloudflare dashboard ingress config can still be remotely pushed; operator should keep hostname service target aligned with internal service DNS policy.

## Rollback
- Revert compose changes.
- Restart prior containers (`docker compose down` / `up -d`).
- Restore previous cloudflared route target in Cloudflare dashboard if needed.
