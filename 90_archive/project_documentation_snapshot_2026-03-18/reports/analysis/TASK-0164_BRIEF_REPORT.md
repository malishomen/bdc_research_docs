# TASK-0164 BRIEF REPORT

## Goal
Enforce safer default online posture: no unintended public API exposure; VPN-first with explicit operator opt-in for remote access.

## Changes Applied

1. Docker runtime bind strategy
- `tools/hive_core_mvp/docker-compose.yml`
  - Host publish default changed to loopback:
    - `"${HIVE_PUBLISH_BIND:-127.0.0.1}:8080:8080"`
  - Added env controls:
    - `HIVE_BIND_HOST`
    - `HIVE_PORT`

2. Uvicorn bind env support
- `tools/hive_core_mvp/hive_core/Dockerfile`
  - CMD now respects env:
    - `--host ${HIVE_BIND_HOST:-127.0.0.1}`
    - `--port ${HIVE_PORT:-8080}`

3. Env defaults and knobs
- `tools/hive_core_mvp/.env.example`
  - Added:
    - `HIVE_BIND_HOST=0.0.0.0` (compose override for container networking)
    - `HIVE_PORT=8080`
    - `HIVE_PUBLISH_BIND=127.0.0.1` (safe default)

4. Runbook hardening
- `tools/hive_core_mvp/README_RUNBOOK.md`
  - Explicit default posture and VPN opt-in flow.
  - Bind/Exposure controls section.
  - Windows firewall playbook with allowlist/blocklist commands and rollback.
  - Mode matrix retained and clarified (LAN/VPN/Tunnel/raw public no-go).

## Verification (L0)

Commands:
```powershell
docker compose -f tools/hive_core_mvp/docker-compose.yml up -d --build
docker compose -f tools/hive_core_mvp/docker-compose.yml ps
curl.exe http://127.0.0.1:8080/v1/ping
```

Observed:
- `hive-mvp-core` published as `127.0.0.1:8080->8080/tcp`.
- Local ping remained OK (`ok:true`).

Interpretation:
- Default posture now loopback-only publication at host level.
- Remote reachability requires explicit opt-in (`HIVE_PUBLISH_BIND=0.0.0.0`) and firewall constraints.

## Threat Model Notes
- This is hardening for exposure control and basic abuse resistance, not full production security.
- Limitations remain: bearer-token model, no mTLS/device attestation, rate limiting is in-memory per instance.

## Status
- PARTIAL for full VPN reachability validation because Tailscale on Queen was `NeedsLogin` in this session.
- SUCCESS for repository/config hardening changes and local verification of safer default posture.
