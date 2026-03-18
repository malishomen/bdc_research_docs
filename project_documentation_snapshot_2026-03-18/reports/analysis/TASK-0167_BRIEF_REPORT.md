# TASK-0167 BRIEF REPORT

- Task: `TASK-0167`
- Date (UTC): `2026-02-17`
- Branch: `hive`
- Status: `PARTIAL`

## Objective

Implement a true one-click Windows launcher for non-IT users:
- single entrypoint `START_HIVE.bat`
- no manual terminal commands
- optional auto-install/check of Tailscale
- run full drone flow and produce L0 log

## Changes

1. Added `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- Single double-click entrypoint.
- Reads operator-provided `config.ini`.
- Auto-generates `hive_join.conf` for existing one-click client.
- Verifies PowerShell.
- Verifies Tailscale, offers install via `winget install -e --id Tailscale.Tailscale`.
- If Tailscale login is required, triggers login flow and waits for ready state.
- Calls `WindowsDroneOneClick.bat`.
- Shows explicit final `SUCCESS`/`FAIL` banner and pause.

2. Added `tools/hive_core_mvp/drone_client/config.ini`
- Safe operator template only (no real secret).

3. Added `tools/hive_core_mvp/drone_client/README_FOR_FRIEND.txt`
- Single instruction for non-IT users.

4. Updated `tools/hive_core_mvp/README_RUNBOOK.md`
- Added/updated one-click friend flow around `START_HIVE.bat`.

## Verification (L0)

## Case 2: Tailscale already installed and logged in

Command:
```powershell
$env:HIVE_NO_PAUSE='1'; cmd /c tools\hive_core_mvp\drone_client\START_HIVE.bat
```

Observed output excerpt:
```text
[2/4] Checking Tailscale...
Tailscale connected. Local VPN IP: 100.72.39.43
[3/4] Running HIVE drone flow...
SUCCESS
drone_id=33cfb695-2e36-425a-8ed7-03d35cbf8e4e
task_id=f2d658f4-07c3-436a-a373-04d2b00a635a
task_hash=2876e4fcfc84df1c30ab58d56271be9ace31ce7f44c2ceed58265c5325370ba2
accepted=True
```

Log evidence:
- `tools/hive_core_mvp/drone_client/drone_mvp_log_20260217T103944Z.txt`

## Case 3: Invite already used

Command:
```powershell
$env:HIVE_NO_PAUSE='1'; cmd /c tools\hive_core_mvp\drone_client\START_HIVE.bat
```

Observed output excerpt:
```text
FAILURE: Invite already used or expired. Ask for a new invite file.
See log: drone_mvp_log_20260217T103952Z.txt
```

Log evidence:
- `tools/hive_core_mvp/drone_client/drone_mvp_log_20260217T103952Z.txt`

## DB Correlation After Success Run

Commands:
```powershell
cd tools/hive_core_mvp
docker compose exec -T postgres psql -U hive -d hive -c "select drone_id,host_label,created_ts from hive_drones order by created_ts desc limit 3;"
docker compose exec -T postgres psql -U hive -d hive -c "select task_id,task_hash_sha256,issued_ts,status from hive_tasks order by issued_ts desc limit 3;"
docker compose exec -T postgres psql -U hive -d hive -c "select result_id,task_id,drone_id,received_ts,status from hive_results order by received_ts desc limit 3;"
```

Observed latest linked chain:
- drone_id: `33cfb695-2e36-425a-8ed7-03d35cbf8e4e`
- task_id: `f2d658f4-07c3-436a-a373-04d2b00a635a`
- task_hash: `2876e4fcfc84df1c30ab58d56271be9ace31ce7f44c2ceed58265c5325370ba2`
- result_id: `2d321ed7-b8d9-46c9-a23e-51797c08cd26`
- timestamps aligned with launcher log (`2026-02-17T10:39:45Z` window)

## Verification Gap

- Fresh-machine Case 1 (no Tailscale installed) was not executed in this host session.
- Installation/login path is implemented and documented, but not validated on a clean VM in this task run.

## Outcome

- One-click launcher workflow is implemented and operational for installed/logged-in Tailscale path.
- Used-invite failure path is explicit and user-friendly.
- L0 logs and DB evidence captured for successful one-click run.
