# TASK-0159 HIVE MVP Plan and L0 Execution Guide

## Objective

Bring up HIVE v1 MVP Queen/Core on Windows 11 and validate remote Drone handshake over secure online path.

Branch target: `hive`
Task: `TASK-0159`

## MVP Boundaries

In scope:
- `/v1/ping`
- `/v1/drones/register` (invite-code gated)
- `/v1/tasks/poll` (bearer token)
- `/v1/tasks/result` (bearer token)
- Postgres durable truth tables
- Audit logging for task issue and result receive
- Windows `.bat` Drone stub

Out of scope:
- Training/eval compute scheduler
- mTLS and attestation (future hardening)
- Public internet anonymous API exposure

## L0 Truth Sources

- API logs: `tools/hive_core_mvp/logs/hive-core.log`
- DB rows: `hive_drones`, `hive_invites`, `hive_tokens`, `hive_tasks`, `hive_results`
- Drone local log: `drone_mvp_log_<ts>.txt`

All claims must map to one of these artifacts.

## Architecture (MVP)

- `hive-core` (FastAPI): contract + auth + audit
- `postgres` (durable truth): identities/tasks/results
- `redis` (topology placeholder queue component)
- `drone_client/WindowsDroneMVP.bat`: Windows registration/poll/result flow

## Determinism Contract

For each issued task:
1. Build canonical JSON object.
2. Serialize with stable key ordering and compact separators.
3. Compute `sha256` over canonical serialization.
4. Persist both canonical JSON and hash.
5. Require hash echo on result submit.

## Threat Model (MVP)

### Threats
- Unauthorized internet caller hits API endpoint.
- Invite code leakage/reuse.
- Token theft or replay from logs.
- Result spoofing using wrong task hash.

### Controls
- Tailscale-only network path recommended; no open public port guidance.
- Invite stored as hash and marked used on first successful registration.
- Token stored hashed and validated with expiry and revocation fields.
- Task result requires matching `drone_id`, bearer token identity, and `task_hash_sha256`.
- Audit logs include `remote_addr`, timestamps, `task_hash`, and `drone_id`.

### Residual Risk
- Token bearer model can be replayed if endpoint host is compromised.
- MVP lacks mTLS and nonce anti-replay persistence.

## Verification Procedure

1. Compose up:
```powershell
cd tools/hive_core_mvp
docker compose up -d --build
docker compose ps
```

2. Ping local:
```powershell
curl.exe http://127.0.0.1:8080/v1/ping
```

3. Ping remote via Tailscale from laptop:
```powershell
curl.exe http://<QUEEN_TAILSCALE_IP>:8080/v1/ping
```

4. Run Drone script on laptop:
```cmd
set QUEEN_URL=http://<QUEEN_TAILSCALE_IP>:8080
set INVITE_CODE=<INVITE_FROM_QUEEN_ENV>
WindowsDroneMVP.bat
```

5. Validate DB rows:
```powershell
docker compose exec -T postgres psql -U %POSTGRES_USER% -d %POSTGRES_DB% -c "select count(*) from hive_drones;"
docker compose exec -T postgres psql -U %POSTGRES_USER% -d %POSTGRES_DB% -c "select count(*) from hive_tasks;"
docker compose exec -T postgres psql -U %POSTGRES_USER% -d %POSTGRES_DB% -c "select count(*) from hive_results;"
```

Pass target for MVP smoke: `>=1` row in each table after one drone run.

## Rollback

```powershell
cd tools/hive_core_mvp
docker compose down -v
Remove-NetFirewallRule -DisplayName "HIVE MVP 8080 Tailscale"
Remove-NetFirewallRule -DisplayName "HIVE MVP 8080 Block NonVPN"
```

## Change List (Task Artifacts)

- `tools/hive_core_mvp/docker-compose.yml`
- `tools/hive_core_mvp/.env.example`
- `tools/hive_core_mvp/hive_core/main.py`
- `tools/hive_core_mvp/hive_core/Dockerfile`
- `tools/hive_core_mvp/hive_core/requirements.txt`
- `tools/hive_core_mvp/db/init.sql`
- `tools/hive_core_mvp/drone_client/WindowsDroneMVP.bat`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- `reports/analysis/TASK-0159_HIVE_MVP_PLAN.md`

## Operator Notes

- Keep `.env` local and secret.
- If invite is consumed, rotate invite code in `.env` and restart core.
- For future v1.1: mTLS, per-drone nonce cache, signed task receipts.

## L0 Verification — TASK-0160 (2026-02-17, Windows 11 host)

Status: PARTIAL (local Queen validation PASS; remote laptop over Tailscale not executed in this session).

### Environment facts
- Host OS: Windows 11 (from drone profile evidence)
- Docker: `Docker version 29.1.3`, `Docker Compose v2.40.3-desktop.1`
- Tailscale CLI on Queen host: not found (`tailscale` command unavailable at runtime)

### Commands and captured outputs

1) Compose up and process state:
```powershell
cd tools/hive_core_mvp
Copy-Item .env.example .env -Force
docker compose up -d --build
docker compose ps
```
Evidence snapshot:
- `hive-mvp-core` Up
- `hive-mvp-postgres` Up (healthy)
- `hive-mvp-redis` Up (healthy)

2) Local health:
```powershell
curl.exe http://127.0.0.1:8080/v1/ping
```
Response:
```json
{"ok":true,"ts_utc":"2026-02-17T09:08:13Z","service":"hive-core","version":"0.1.0"}
```

3) Drone flow execution (local operator run of Windows bat):
```powershell
cd tools/hive_core_mvp/drone_client
$env:QUEEN_URL='http://127.0.0.1:8080'
$env:INVITE_CODE='CHANGE_ME_INVITE_CODE'
cmd /c WindowsDroneMVP.bat
```
Terminal:
- `SUCCESS see drone_mvp_log_20260217T140831Z.txt`

Drone log excerpt:
- `Registered drone_id=9989f8e8-0923-48a5-bc54-c4b9d10190ae`
- `Received task_id=ede04091-cf34-46fe-87bb-40ad18a80834`
- `hash=87629e1a11d4d07a70d324a3f43054877a00756934e68d6d0da8f76106331bd1`
- `Result accepted=True server_ts=2026-02-17T09:08:32Z`

4) DB durable truth evidence:
```powershell
docker compose exec -T postgres psql -U hive -d hive -c "select drone_id, host_label, os, cpu_threads, gpu_vendor, created_ts from hive_drones order by created_ts desc limit 5;"
docker compose exec -T postgres psql -U hive -d hive -c "select task_id, task_type, task_hash_sha256, issued_ts, status from hive_tasks order by issued_ts desc limit 5;"
docker compose exec -T postgres psql -U hive -d hive -c "select result_id, task_id, drone_id, received_ts, status from hive_results order by received_ts desc limit 5;"
```
Observed rows:
- Drone: `9989f8e8-0923-48a5-bc54-c4b9d10190ae`, host `WIN-JTSARSVBH32`, OS `Microsoft Windows 11 Pro`, created `2026-02-17 09:08:32+00`
- Task: `ede04091-cf34-46fe-87bb-40ad18a80834`, type `HELLO_MVP`, hash `87629e1a11d4d07a70d324a3f43054877a00756934e68d6d0da8f76106331bd1`, status `COMPLETED`
- Result: `e6d00fae-66cd-4aea-bbd5-4f24ffd03a20`, status `OK`, received `2026-02-17 09:08:32+00`

5) Audit log evidence (`tools/hive_core_mvp/logs/hive-core.log`):
- `startup` event at `2026-02-17T09:07:59Z`
- `drone_registered` for drone `9989f8e8-0923-48a5-bc54-c4b9d10190ae`
- `task_issued` with task hash `87629e...31bd1`
- `task_result_received` with same hash + nonce `15a7bc85-12dc-4a95-ab46-f5168b7a1944`

### Pass criteria mapping
- All containers running: PASS
- Local ping returns ok:true: PASS
- Drone flow register/poll/result accepted: PASS
- DB contains drone/task/result rows with matching IDs/hash/time: PASS
- Remote ping over Tailscale from laptop: NOT EXECUTED in this session (Tailscale CLI absent on Queen host; no remote laptop execution attached)

### Security posture notes
- No raw public exposure commands were used.
- Validation was local-only for this run; VPN/Tailscale remote proof remains pending.

## Follow-up Attempt — TASK-0163 (2026-02-17)

- Intent: close remote-laptop-over-Tailscale proof gap from TASK-0160.
- Queen-side evidence captured in `reports/analysis/TASK-0163_BRIEF_REPORT.md`.
- Current blocker at execution time: Tailscale state on Queen = `NeedsLogin` (`tailscale status --json`), so remote laptop path could not be validated in this session.
- No fake SUCCESS recorded; status remains evidence-gated.

## Cross-reference Update — TASK-0165 (2026-02-17)

- See `reports/analysis/TASK-0165_BRIEF_REPORT.md` for post-login Tailscale L0 evidence:
  - Queen tailnet state with `100.72.39.43`
  - successful `/v1/ping` via Tailscale URL
  - successful drone flow and DB correlation over Tailscale URL
- Remaining gap for strict close of remote proof: dedicated laptop (second device) run evidence.
