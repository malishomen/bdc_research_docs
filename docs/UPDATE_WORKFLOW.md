# Update Workflow

## Purpose
This repository is a research mirror. Source of truth for working materials remains:
- `D:\projects\Bio_Digital_Core\Temp\research`
- `D:\projects\Bio_Digital_Core\Bio_digital_core`

## Standard Update Procedure
1. Run:
   `powershell -ExecutionPolicy Bypass -File .\scripts\refresh_from_temp_research.ps1`
2. Review:
   `git status --short`
3. Commit:
   `git add -A`
   `git commit -m "Refresh research mirror"`
4. Push:
   `git push origin main`

## What the Script Updates
- `10_scientific_line/BDC_MAIN_F`
- `20_bdc_designer/BDC_Designer_F`
- `30_external_sources/external`
- `90_archive/internal`
- `90_archive/temp_works`
- `90_archive/project_documentation_snapshot_*`
- `00_indexes/*.md` summary files
- `40_dissertation/Dissertation/*` dissertation-support drafts

## Review Rule
Do not push blind refreshes. Always inspect `git status` and spot-check changed files before commit.
