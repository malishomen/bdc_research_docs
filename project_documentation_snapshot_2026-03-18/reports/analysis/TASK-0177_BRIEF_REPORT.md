# TASK-0177 BRIEF REPORT

## Scope
- Persist volunteer identity fields and per-drone contribution counters.
- Add volunteer aggregate table/counters.
- Add read-only stats APIs (`/v1/stats/drones`, `/v1/stats/summary`).

## Changes
- DB schema updates:
  - `tools/hive_core_mvp/db/init.sql`
    - Added drone columns: `volunteer_name`, `volunteer_email_hash`, `volunteer_key`, `tasks_completed`, `tasks_failed`, `total_compute_seconds`, `total_result_bytes`.
    - Added table `hive_volunteers` with aggregate counters.
- API updates:
  - `tools/hive_core_mvp/hive_core/main.py`
    - Runtime schema migration guard (`ALTER ... IF NOT EXISTS`).
    - `/v1/drones/register` now accepts optional `volunteer` object and stores name/email hash.
    - `/v1/tasks/result` updates counters for drones + volunteers using L0-derivable metrics:
      - task outcome, walltime (`received_ts - issued_ts`), result payload bytes.
    - Added `GET /v1/stats/drones` (admin bearer token required).
    - Added `GET /v1/stats/summary` (no PII).
- Docs updates:
  - `tools/hive_core_mvp/README_RUNBOOK.md` (stats usage and DB queries).

## Verification (L0)
- Created fresh invite and ran one full client flow:
  - Command: `powershell -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
  - Result: `SUCCESS`, `accepted=True`, drone `12498629-3765-4690-aea8-2433f5adc604`.

- Public summary endpoint:
  - Command: `curl.exe -sS http://127.0.0.1:8080/v1/stats/summary`
  - Result includes non-zero counters:
    - `"tasks_completed_total":1`
    - `"total_compute_seconds":0.136`
    - `"total_result_bytes":242`

- Admin drones endpoint:
  - Command: `curl.exe -sS -H "Authorization: Bearer CHANGE_ME_STATS_ADMIN_TOKEN" http://127.0.0.1:8080/v1/stats/drones`
  - Result includes latest drone with `volunteer_name="Volunteer Test"` and counters.

- DB proof (drone counters):
  - Query output includes:
    - `tasks_completed=1`
    - `tasks_failed=0`
    - `total_compute_seconds=0.136`
    - `total_result_bytes=242`

- DB proof (volunteer aggregate):
  - `hive_volunteers` row for hashed email key with matching counters and `drones_count=1`.

## Artifacts
- `tools/hive_core_mvp/hive_core/main.py`
- `tools/hive_core_mvp/db/init.sql`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- `reports/analysis/TASK-0177_BRIEF_REPORT.md`

## Risks / Limitations
- Existing historical drones without volunteer profile remain with null volunteer fields.
- Admin stats endpoint currently uses a static bearer secret from env (`STATS_ADMIN_TOKEN`).

## Rollback
- Revert schema/code commits.
- For full schema rollback on live DB, apply explicit ALTER/DROP plan (destructive rollback only with backup).
