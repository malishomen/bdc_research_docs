# TASK-HIVE-FRIEND-FULL-RUNTIME-014 BRIEF REPORT

## Scope
- Собран self-contained friend bundle с full runtime:
  - drone runtime
  - local readonly viz runtime
  - auto-open browser на `http://127.0.0.1:8848/viewer.html`
- Удален авто-стоп в drone runtime (бесконечный цикл), остановка только вручную.
- Сохранена обратная совместимость `START_HIVE.bat` (один цикл по умолчанию через `HIVE_MAX_CYCLES=1`).

## Changes
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
  - добавлен бесконечный loop (`poll -> submit`) без auto-stop;
  - soft-stop (`stop_soft.request`) обрабатывается как graceful success;
  - добавлена запись local snapshots в `./_snapshots` (`LATEST.json`, `snapshot_*.json`, `DRONE_RUNTIME_STATUS.json`).
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
  - для backward compatibility: если не задано, `HIVE_MAX_CYCLES=1`.
- `tools/hive_core_mvp/drone_client/START_FULL_RUNTIME.bat` (new)
  - стартует `run_viz_readonly.ps1` + `WindowsDroneOneClick.ps1`, затем открывает browser.
- `tools/hive_core_mvp/drone_client/run_viz_readonly.ps1` (new)
  - проверка свободного порта 8848;
  - bootstrap `LATEST.json` при первом старте;
  - запуск `localhost_server.py` в `--read_only`.
- `tools/hive_core_mvp/drone_client/README_RUNTIME.txt` (new)
- `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
  - bundle включает:
    - `START_FULL_RUNTIME.bat`
    - `run_viz_readonly.ps1`
    - `README_RUNTIME.txt`
    - `viewer.html`
    - `localhost_server.py`
    - `./_snapshots/LATEST.json` bootstrap

## Verification (L0)
- Build:
  - `pwsh -NoProfile -ExecutionPolicy Bypass -File drone_client/build_friend_bundle.ps1 -HostLabel FRIEND-FULL-014`
  - Result ZIP: `tools/hive_core_mvp/dist/HIVE_FRIEND_20260219T055242Z.zip`

- SHA:
  - Actual: `f44895777fead55a9f111d1628f13274fe72620d93895904a5f6d9d0eada933c`
  - Sidecar matches: `tools/hive_core_mvp/dist/HIVE_FRIEND_20260219T055242Z.zip.sha256`

- Secret scan (unzipped bundle):
  - `rg -n "CF_ACCESS_CLIENT_ID|CF_ACCESS_CLIENT_SECRET|CLOUDFLARED_TUNNEL_TOKEN|cloudflare_access\.env|\.env" .tmp_task014_bundle3`
  - Result: no matches (PASS)

- Viz runtime dry-run:
  - `pwsh -File .tmp_task014_bundle3/run_viz_readonly.ps1 -Port 8848`
  - `curl -i http://127.0.0.1:8848/viewer.html` => 200
  - `curl -i http://127.0.0.1:8848/LATEST.json` => 200 JSON

- Drone e2e (local stack, test-limited 1 cycle):
  - `QUEEN_URL.txt` set to `http://127.0.0.1:8080` for local L0 test
  - `START_HIVE.bat` run (default one cycle)
  - Result: `SUCCESS`, `cycles=1`, `tasks_completed=1`
  - Log: `.tmp_task014_bundle3/drone_mvp_log_20260219T055353Z.txt`
  - Snapshot updated:
    - `.tmp_task014_bundle3/_snapshots/LATEST.json`
    - `.tmp_task014_bundle3/_snapshots/snapshot_20260219T055357Z.json`

## External Viz Note
- External run against `https://viz.bdc-hive.com` with locally-generated invite returned claim `403`.
- Root cause: invite was created in local DB (builder executed locally), while `viz` points to production Queen DB.
- For external PASS, bundle must be built on Queen (or invite inserted into Queen DB).

## Artifacts
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- `tools/hive_core_mvp/drone_client/START_FULL_RUNTIME.bat`
- `tools/hive_core_mvp/drone_client/run_viz_readonly.ps1`
- `tools/hive_core_mvp/drone_client/README_RUNTIME.txt`
- `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
- `reports/analysis/TASK-HIVE-FRIEND-FULL-RUNTIME-014_BRIEF_REPORT.md`

## Status
- `PARTIAL`:
  - local full-runtime path verified end-to-end;
  - external `viz` e2e requires running bundle build on Queen production DB.
