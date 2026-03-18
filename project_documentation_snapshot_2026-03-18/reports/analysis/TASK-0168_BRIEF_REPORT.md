# TASK-0168 BRIEF REPORT

- Task: `TASK-0168`
- Date (UTC): `2026-02-17`
- Branch: `hive`
- Status: `SUCCESS`

## What Was Implemented

1. Added bundle build script:
- `tools/hive_core_mvp/drone_client/build_zip.ps1`

2. Added tracked dist scaffold:
- `dist/.gitkeep`

3. Updated ignore policy for bundle outputs:
- `.gitignore`
  - ignore staging folder: `dist/HIVE_DRONE_ONECLICK_LAPTOP/`
  - ignore zip binary: `dist/*.zip`
  - keep tracked L0 text artifacts: `dist/BUNDLE_MANIFEST.json`, `dist/*.zip.sha256`

4. Updated runbook with USB distribution steps:
- `tools/hive_core_mvp/README_RUNBOOK.md`

## Build Command

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/drone_client/build_zip.ps1
```

## Verification Evidence (L0)

Generated files in `dist/`:
- `HIVE_DRONE_ONECLICK_LAPTOP.zip`
- `HIVE_DRONE_ONECLICK_LAPTOP.zip.sha256`
- `BUNDLE_MANIFEST.json`

`certutil` SHA256 output:
- `8b194154471500c4760bc6b7611e031fb2bbd92150b09e198dd3926d06b342d3`

`.sha256` file content:
- `8b194154471500c4760bc6b7611e031fb2bbd92150b09e198dd3926d06b342d3 *HIVE_DRONE_ONECLICK_LAPTOP.zip`

SHA values matched.

Bundle entries (zip listing):
- `config.ini` (safe template, `HOST_LABEL=LAPTOP-TEST`)
- `README_FOR_FRIEND.txt`
- `START_HIVE.bat`
- `WindowsDroneOneClick.bat`
- `WindowsDroneOneClick.ps1`

## Secret-Safety Checks

- `hive_join.conf` is not included in the ZIP.
- `.env` is not included in the ZIP.
- no token files are included in the ZIP.
- `INVITE_CODE` in bundled `config.ini` is placeholder only.

## Notes

- ZIP binary is generated for distribution and kept untracked by policy.
- L0 traceability artifacts are tracked as text:
  - `dist/BUNDLE_MANIFEST.json`
  - `dist/HIVE_DRONE_ONECLICK_LAPTOP.zip.sha256`
