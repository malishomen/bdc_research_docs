# TASK-0165 BRIEF REPORT

## Goal
Close remote-proof gap by validating Tailscale login on Queen, remote path reachability, drone flow over Tailscale URL, and DB correlation.

## Result
- PARTIAL (strict evidence standard).
- Tailscale VPN path is now proven from Queen side and via Tailscale URL.
- Full *second-device/laptop* execution evidence is still missing in this session.

## L0 Evidence

### Queen Tailscale state
Commands:
```powershell
& 'C:\Program Files\Tailscale\tailscale.exe' status
& 'C:\Program Files\Tailscale\tailscale.exe' ip -4
```
Output:
- `100.72.39.43  win-jtsarsvbh32 ...`
- IPv4: `100.72.39.43`

### Queen service health
Commands:
```powershell
docker compose -f tools/hive_core_mvp/docker-compose.yml --env-file tools/hive_core_mvp/.env ps
curl.exe http://127.0.0.1:8080/v1/ping
```
Output:
- `hive-mvp-core` Up
- `/v1/ping` -> `ok:true`

### Tailscale-path ping
Command:
```powershell
curl.exe http://100.72.39.43:8080/v1/ping
```
Output:
```json
{"ok":true,"ts_utc":"2026-02-17T09:53:55Z","service":"hive-core","version":"0.1.0"}
```

### Drone flow over Tailscale URL
Commands:
```powershell
$env:QUEEN_URL='http://100.72.39.43:8080'
$env:INVITE_CODE='CHANGE_ME_INVITE_CODE'
cmd /c WindowsDroneMVP.bat
```
Logs:
- first run failed (`invite already used`) at `drone_mvp_log_20260217T145406Z.txt`
- invite reset (DB) and rerun succeeded at `drone_mvp_log_20260217T145422Z.txt`

Success excerpt:
- `Registered drone_id=80620faf-fe86-4c16-be36-376c941c7974`
- `Received task_id=957b00e4-d416-48dd-ad29-ec013910524c`
- `hash=3217c1ea3e472d297cbd807f607ab38e3dd6218ca6b1df20f9074100dbfade5f`
- `Result accepted=True server_ts=2026-02-17T09:54:24Z`

### DB correlation
Queries:
```powershell
docker compose -f tools/hive_core_mvp/docker-compose.yml --env-file tools/hive_core_mvp/.env exec -T postgres psql -U hive -d hive -c "select drone_id, host_label, os, cpu_threads, gpu_vendor, created_ts from hive_drones order by created_ts desc limit 10;"
docker compose -f tools/hive_core_mvp/docker-compose.yml --env-file tools/hive_core_mvp/.env exec -T postgres psql -U hive -d hive -c "select task_id, task_type, task_hash_sha256, issued_ts, status from hive_tasks order by issued_ts desc limit 10;"
docker compose -f tools/hive_core_mvp/docker-compose.yml --env-file tools/hive_core_mvp/.env exec -T postgres psql -U hive -d hive -c "select result_id, task_id, drone_id, received_ts, status from hive_results order by received_ts desc limit 10;"
```
Observed chain:
- Drone: `80620faf-fe86-4c16-be36-376c941c7974`
- Task: `957b00e4-d416-48dd-ad29-ec013910524c`
- Hash: `3217c1ea3e472d297cbd807f607ab38e3dd6218ca6b1df20f9074100dbfade5f`
- Result: `49d422a9-3e7e-446c-9ff0-588c295c0b69` status `OK`
- Times are aligned around `2026-02-17T09:54:23Z` to `09:54:24Z`

## Why still PARTIAL
- Required proof says laptop as second machine.
- Current successful `.bat` run is from Queen host (host_label `WIN-JTSARSVBH32`).

## Minimal final step to graduate to SUCCESS
Run once on laptop and provide excerpt:
```cmd
set QUEEN_URL=http://100.72.39.43:8080
set INVITE_CODE=CHANGE_ME_INVITE_CODE
cd tools\hive_core_mvp\drone_client
WindowsDroneMVP.bat
```
Then append laptop log + DB row correlation.
