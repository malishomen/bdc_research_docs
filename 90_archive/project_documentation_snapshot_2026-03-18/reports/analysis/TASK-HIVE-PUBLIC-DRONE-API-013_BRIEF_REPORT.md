# TASK-HIVE-PUBLIC-DRONE-API-013 BRIEF REPORT

## Scope
- Перевести drone plane на публичный `viz.bdc-hive.com` без Cloudflare Access секретов в клиентском архиве.
- Сохранить `queen.bdc-hive.com` за Access.
- Не допустить утечку секретов в `dist` bundle.

## Changes
- `tools/hive_core_mvp/hive_core/main.py`
  - Добавлен публичный drone API alias:
    - `POST /v1/drone/register`
    - `POST /v1/drone/poll`
    - `POST /v1/drone/submit`
  - Добавлен guard для public drone plane (allowlist public-paths + `/dist/*`).
  - Для подписи poll/result используется фактический `request.url.path` (совместимо с новым и legacy путями).
  - В `request_host()` добавлена поддержка `X-Forwarded-Host` и `X-Original-Host`.
  - Admin bundle generation переведен на `QUEEN_URL=https://viz.bdc-hive.com` без embedding `cloudflare_access.env`.
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
  - Убрана блокировка по отсутствию `cloudflare_access.env`.
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
  - Удалена логика Access headers и чтения `cloudflare_access.env`.
  - Основной путь: `/v1/drone/register|poll|submit`.
  - Добавлен fallback на legacy endpoint'ы при `404`.
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.bat`
  - Удалены устаревшие подсказки про обязательный Access env.
- `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
  - Default `QueenUrl` изменен на `https://viz.bdc-hive.com`.

## Verification (L0)
- Команда: `curl.exe -i https://viz.bdc-hive.com/v1/ping`
- Результат: `200 OK`, JSON `{"ok":true,...}` -> PASS

- Команда: `curl.exe -i https://queen.bdc-hive.com/v1/ping`
- Результат: `403 Forbidden` (Cloudflare Access page) -> PASS

- Команда: `curl.exe -i https://viz.bdc-hive.com/admin`
- Результат: `401 {"detail":"Missing Bearer token"}` -> PASS (owner token required)

- Команда: `curl.exe -i -X POST https://viz.bdc-hive.com/v1/control/stop -H "Content-Type: application/json" --data-binary "{\"mode\":\"emergency\"}"`
- Результат: `401 {"detail":"Missing Bearer token"}` -> PASS (owner token required)

- Команда: `curl.exe -s https://viz.bdc-hive.com/dist/LATEST.json`
- Результат: latest bundle `HIVE_FRIEND_20260219T045449Z.zip` с SHA256 `e7a31a5b541e340d9389941ae2698c1c35f7a33b99b962c5d1181bef5cf1cd96` -> PASS

- Команда: `Get-FileHash -Algorithm SHA256 .tmp_task013_a\\HIVE_FRIEND_20260219T045449Z.zip`
- Результат: `e7a31a5b541e340d9389941ae2698c1c35f7a33b99b962c5d1181bef5cf1cd96` -> PASS

- Команда: `rg -n "CF_ACCESS_CLIENT_ID|CF_ACCESS_CLIENT_SECRET|CLOUDFLARED_TUNNEL_TOKEN|cloudflare_access\\.env" .tmp_task013_a\\unz`
- Результат: exit code `1` (совпадений нет) -> PASS

- Команда: `Get-Content .tmp_task013_a\\unz\\QUEEN_URL.txt`
- Результат: `https://viz.bdc-hive.com` -> PASS

- Команда: локальный запуск one-click без Access secrets (`START_HIVE.bat`, test bundle)
- Результат: `register -> poll -> submit`, `accepted=True` в `drone_mvp_log_20260219T050109Z.txt` -> PASS

## Artifacts
- `tools/hive_core_mvp/hive_core/main.py`
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.bat`
- `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
- `reports/analysis/TASK-HIVE-PUBLIC-DRONE-API-013_BRIEF_REPORT.md`

## Risks / Limitations
- Публичный hostname `viz.bdc-hive.com` приводит к достижимости owner routes на уровне URL, но они остаются защищены owner bearer token и не исполняются без авторизации (401).
- Для более жесткого разделения плоскостей рекомендуется отдельный backend/порт для public drone API или отдельный service policy на уровне ingress.

## Rollback
- Вернуть клиент на legacy endpoint'ы `/v1/drones/claim`, `/v1/tasks/poll`, `/v1/tasks/result`.
- Вернуть обязательную Access header логику в `START_HIVE.bat`/`WindowsDroneOneClick.ps1` (если потребуется).
- Пересобрать friend bundle и обновить `dist/LATEST.json`.
