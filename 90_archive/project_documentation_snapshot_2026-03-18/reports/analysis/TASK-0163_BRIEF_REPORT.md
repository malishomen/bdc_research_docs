# TASK-0163 BRIEF REPORT

## Goal
Close missing remote-laptop validation for HIVE MVP over internet via Tailscale and capture full L0 evidence.

## Result
- PARTIAL.
- Queen-side preparation and checks completed.
- Remote laptop step could not be completed because Queen Tailscale CLI remained in `NeedsLogin` state during this session.

## L0 Evidence (captured)

### 1) Tailscale install and runtime state (Queen)
Commands:
```powershell
winget search tailscale
winget install --id Tailscale.Tailscale --silent --accept-package-agreements --accept-source-agreements
& 'C:\Program Files\Tailscale\tailscale.exe' version
& 'C:\Program Files\Tailscale\tailscale.exe' status --json
```

Observed:
- Installed version: `1.94.2`
- Service: `Tailscale` running (Automatic)
- Status JSON: `BackendState="NeedsLogin"`, `TailscaleIPs=null`, `AuthURL` present, `Health` includes `You are logged out`.

### 2) Queen service health
Commands:
```powershell
docker compose -f tools/hive_core_mvp/docker-compose.yml ps
curl.exe http://127.0.0.1:8080/v1/ping
```

Observed:
- `hive-mvp-core` Up
- Local ping response: `{"ok":true,...,"service":"hive-core","version":"0.1.0"}`

### 3) Remote path attempt using provided Queen Tailscale IP
Command:
```powershell
curl.exe http://100.72.39.43:8080/v1/ping
```

Observed:
- Failed connect (`curl: (28) ... Could not connect to server`) while Queen is in `NeedsLogin` state.

## Why not SUCCESS
Required pass criteria not satisfied in this session:
- Remote ping over Tailscale from second device (laptop) not captured.
- Laptop-run `WindowsDroneMVP.bat` against Queen Tailscale URL not captured.
- Correlated DB rows for remote laptop run therefore unavailable.

## Next action to close TASK-0163
After Queen shows authenticated Tailscale state (`tailscale status` shows assigned `100.x` IP), run on laptop:
```cmd
set QUEEN_URL=http://<QUEEN_TAILSCALE_IP>:8080
set INVITE_CODE=<QUEEN_INVITE_CODE>
cd tools\hive_core_mvp\drone_client
WindowsDroneMVP.bat
```
Then collect DB evidence with the existing SQL queries and append to this report.

## Evidence Update — TASK-0165 (2026-02-17)

New L0 facts captured after user Tailscale login:
- Queen Tailscale state active with IPv4 `100.72.39.43` (`tailscale status`, `tailscale ip -4`).
- Tailscale-path ping works: `curl http://100.72.39.43:8080/v1/ping` => `ok:true`.
- Drone flow over Tailscale URL succeeded after invite reset:
  - drone `80620faf-fe86-4c16-be36-376c941c7974`
  - task `957b00e4-d416-48dd-ad29-ec013910524c`
  - hash `3217c1ea3e472d297cbd807f607ab38e3dd6218ca6b1df20f9074100dbfade5f`
  - result accepted `OK`
- DB and audit-log correlation captured in `reports/analysis/TASK-0165_BRIEF_REPORT.md`.

Status impact:
- Remote path is operational.
- `TASK-0163` remains strict-PARTIAL until a second-device (laptop) run log is captured.
