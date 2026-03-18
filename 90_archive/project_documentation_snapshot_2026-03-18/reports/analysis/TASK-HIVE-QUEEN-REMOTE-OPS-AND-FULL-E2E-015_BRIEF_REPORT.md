# TASK-HIVE-QUEEN-REMOTE-OPS-AND-FULL-E2E-015 BRIEF REPORT

## Scope
- Завершить remote ops readiness Queen и подтвердить внешний full e2e через `viz.bdc-hive.com`.
- Сборка friend bundle должна выполняться на Queen (production DB invites).
- Без остановки `hive-core` стека.

## Changes
### What Was Done
- Подтвержден runtime на Queen (`bdc-queen`) через SSH:
  - `hive-core` up (`127.0.0.1:8080`)
  - `postgres` healthy (`5432/tcp`, без `0.0.0.0`)
  - `redis` healthy (`6379/tcp`, без `0.0.0.0`)
- Подтвержден cloudflared ingress и актуальная конфигурация:
  - `queen.bdc-hive.com -> http://hive-core:8080`
  - `viz.bdc-hive.com -> http://hive-core:8080`
  - `ssh.bdc-hive.com -> ssh://localhost:22` (version=5 в cloudflared logs)
- На Queen выполнена production bundle сборка (через remote fallback build, так как `pwsh` на Ubuntu отсутствует):
  - ZIP: `HIVE_FRIEND_20260219T061218Z.zip`
  - SHA256: `1fa17923d7322e6a39a62d4065c05cfe2471ac4aa72a4873497ec63c9b1c84a9`
  - Invite создан в production DB.
- Проверен внешний download/manifest:
  - `https://viz.bdc-hive.com/dist/LATEST.json` указывает на этот ZIP и тот же SHA.
- Выполнен e2e run из скачанного production ZIP:
  - claim -> poll -> submit -> `accepted=True`
  - локальный snapshot обновлен (`_snapshots/LATEST.json`, `snapshot_*.json`)

## Verification (L0)
- `curl -s https://viz.bdc-hive.com/dist/LATEST.json` -> PASS (200 JSON, корректный latest bundle + sha256)
- `ssh ... "docker compose ps"` на Queen -> PASS (все core сервисы stable)
- `ssh ... "docker stats --no-stream"` -> PASS (ресурсы низкие, без перегрузки)
- `ssh ... "cat /proc/loadavg"` -> PASS (`0.08 0.04 0.01 ...`)
- `ssh ... "systemctl --user status bdc-hive-backup.timer/service"` -> PASS (timer active, last service `0/SUCCESS`)
- Secret scan распакованного production ZIP:
  - `rg -n "CF_ACCESS_CLIENT_ID|CF_ACCESS_CLIENT_SECRET|CLOUDFLARED_TUNNEL_TOKEN|cloudflare_access\.env|CF-Access-Client-Id|CF-Access-Client-Secret" .tmp_task015_prod_bundle2/unz`
  - Result: no matches (PASS)
- External drone log proof:
  - `.tmp_task015_prod_bundle2/unz/drone_mvp_log_20260219T061755Z.txt`
  - ключевые строки:
    - `Step 2: claim`
    - `Claimed drone_id=... auth_mode=device_claim`
    - `Step 3: poll task`
    - `Received task_id=...`
    - `Step 4: submit result`
    - `Result accepted=True ...`

## SSH Remote Access Status
- `ssh.bdc-hive.com` route присутствует в tunnel config, DNS резолвится.
- Прямая проверка `ssh bdc@ssh.bdc-hive.com` из текущей среды вернула timeout.
- Статус SSH-части: `PARTIAL` (требуется финальная проверка owner-side Access/SSH client path с внешнего оператора).

## Artifacts
- `reports/analysis/TASK-HIVE-QUEEN-REMOTE-OPS-AND-FULL-E2E-015_BRIEF_REPORT.md`
- `.tmp_task015_prod_bundle2/unz/drone_mvp_log_20260219T061755Z.txt`
- `.tmp_task015_prod_bundle2/unz/_snapshots/LATEST.json`

## Final Status
- `PARTIAL`:
  - Full external drone e2e via production bundle: PASS
  - Queen runtime/backup/ingress stability: PASS
  - Remote SSH via `ssh.bdc-hive.com`: pending final owner-side verification
