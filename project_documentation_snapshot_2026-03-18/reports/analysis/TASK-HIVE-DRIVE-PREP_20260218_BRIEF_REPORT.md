# HIVE Backup Drive Prep Brief Report

## Scope
- Prepare external backup disk `H:` (label `HIVE`) for stable migration to laptop Queen.
- Do not delete existing backups.
- Add anti-incident safeguards and verification tooling.

## Changes
### Actions performed (L0)
1. Baseline disk check:
   - `Get-Volume -DriveLetter H`
   - Result: NTFS, label `HIVE`, health `Healthy`, free ~931 GB.
2. Existing backup inventory:
   - `H:\HIVE_BACKUPS\db` contains `.sql.gz` + `.json` pairs.
3. Added prep script:
   - `tools/hive_core_mvp/tools/backup/prepare_backup_drive.ps1`
4. Executed prep script:
   - Created/verified structure:
     - `H:\HIVE_BACKUPS\db`
     - `H:\HIVE_BACKUPS\logs`
     - `H:\HIVE_BACKUPS\manifests`
     - `H:\HIVE_BACKUPS\quarantine`
     - `H:\HIVE_BACKUPS\restore_scratch`
     - `H:\HIVE_BACKUPS\ops`
   - Generated:
     - `H:\HIVE_BACKUPS\ops\DISK_POLICY.json`
     - `H:\HIVE_BACKUPS\ops\DISK_STATE.json`
     - `H:\HIVE_BACKUPS\ops\README_BACKUP_DISK.txt`
     - `H:\HIVE_BACKUPS\manifests\backup_inventory_20260218T203218Z.json`
5. Sidecar hash integrity check:
   - Latest backup hash == sidecar hash (`match=True`).
6. Scheduler check:
   - Task `BDC_HIVE_DB_BACKUP_30MIN` exists and enabled.
7. Manual backup check:
   - Created `hive_db_20260218T203249Z.sql.gz` + sidecar.
8. Added ongoing health script:
   - `tools/hive_core_mvp/tools/backup/verify_backup_drive_health.ps1`
   - Result: `backup_age_ok=true`, `sidecar_hash_ok=true`.
9. Added incident playbook:
   - `tools/hive_core_mvp/tools/backup/HIVE_BACKUP_DRIVE_INCIDENT_PLAYBOOK.md`

## Verification (L0)
### Commands
- `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/tools/backup/prepare_backup_drive.ps1`
- `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/tools/backup/verify_backup_drive_health.ps1`
- `cd tools/hive_core_mvp; pwsh -NoProfile -ExecutionPolicy Bypass -File tools\backup\hive_backup.ps1`
- `schtasks /Query /TN BDC_HIVE_DB_BACKUP_30MIN /V /FO LIST`

## Artifacts
- `tools/hive_core_mvp/tools/backup/prepare_backup_drive.ps1`
- `tools/hive_core_mvp/tools/backup/verify_backup_drive_health.ps1`
- `tools/hive_core_mvp/tools/backup/HIVE_BACKUP_DRIVE_INCIDENT_PLAYBOOK.md`
- `H:\HIVE_BACKUPS\ops\DISK_POLICY.json`
- `H:\HIVE_BACKUPS\ops\DISK_STATE.json`
- `H:\HIVE_BACKUPS\manifests\backup_inventory_20260218T203218Z.json`

## Result
- Current disk `H:` is prepared for migration use with safety structure, inventory manifesting, integrity checks, and incident response baseline.

## Risks / limitations
- Drive letter may change on laptop Linux migration context; Linux mount must be pinned by UUID/label (`/mnt/HIVE`).
- Current Windows scheduler uses host-local script path; after cutover, Linux timer must replace it.

## Rollback
- Non-destructive changes only.
- Remove added ops/manifests folders if needed; existing backups remain intact.
