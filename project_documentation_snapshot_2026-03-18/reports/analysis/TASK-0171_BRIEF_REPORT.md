# TASK-0171 BRIEF REPORT

## Scope
- Implement automated Postgres backups on Queen to external disk `H:\HIVE_BACKUPS`.
- Add scheduler installer for 30-minute cadence.
- Add restore verification runbook section.

## Changes
- Added `tools/hive_core_mvp/tools/backup/hive_backup.ps1`.
- Added `tools/hive_core_mvp/tools/backup/install_task_scheduler.ps1`.
- Added scheduler install evidence file writer: `reports/analysis/TASK-0171_SCHEDULER_INSTALL_EVIDENCE.md`.
- Updated `tools/hive_core_mvp/README_RUNBOOK.md` with backup/restore verification section.

## Verification (L0)
- Command: `cd tools/hive_core_mvp; pwsh -NoProfile -ExecutionPolicy Bypass -File tools/backup/hive_backup.ps1`
- Result: PASS
  - Created `H:\HIVE_BACKUPS\db\hive_db_20260218T000609Z.sql.gz`
  - Created sidecar `H:\HIVE_BACKUPS\db\hive_db_20260218T000609Z.sql.gz.json`
  - Sidecar hash `ec1a998ee3f33885acdba3a809306969e1109ebdbcee1ff157be633c3542501c`
  - `Get-FileHash` matched sidecar hash.

- Command: `cd tools/hive_core_mvp; pwsh -NoProfile -ExecutionPolicy Bypass -File tools/backup/install_task_scheduler.ps1`
- Result: PASS
  - Task created: `BDC_HIVE_DB_BACKUP_30MIN`
  - Query evidence: `schtasks /Query /TN BDC_HIVE_DB_BACKUP_30MIN /V /FO LIST`
  - Repeat interval reported: every 30 minutes.

- Rotation check:
  - Command: `pwsh ... hive_backup.ps1 -RetentionDays 0 -DryRun`
  - Result: PASS (dry-run only)
  - Evidence in `H:\HIVE_BACKUPS\backup_events.log`:
    - `dry_run_rotation_delete file=...`
    - `rotation_complete retention_days=0 deleted=1`

## Artifacts
- `tools/hive_core_mvp/tools/backup/hive_backup.ps1`
- `tools/hive_core_mvp/tools/backup/install_task_scheduler.ps1`
- `reports/analysis/TASK-0171_SCHEDULER_INSTALL_EVIDENCE.md`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- External-only evidence:
  - `H:\HIVE_BACKUPS\db\hive_db_20260218T000609Z.sql.gz`
  - `H:\HIVE_BACKUPS\db\hive_db_20260218T000609Z.sql.gz.json`
  - `H:\HIVE_BACKUPS\backup_events.log`

## Risks / Limitations
- Scheduled task is configured with SYSTEM account; execution policy is bypass mode by design.
- Restore verification commands require Docker and temporary container availability.

## Rollback
- `schtasks /Delete /TN BDC_HIVE_DB_BACKUP_30MIN /F`
- Revert task scripts via git revert if needed.
