# TASK-7640 BRIEF REPORT

## Scope
- Open the bounded `BDC Designer` hardening program after the Cockpit external case.
- Preserve the scientific reboot hierarchy while making the product line execution focus explicit.

## Changes
- Created the post-Cockpit hardening charter:
  - `docs/project/BDC_DESIGNER_POST_COCKPIT_HARDENING_PLAN.md`
- Created the bounded task chain:
  - `tasks/TASK-7640-BDC-DESIGNER-POST-COCKPIT-HARDENING-CHARTER.json`
  - `tasks/TASK-7641-BDC-DESIGNER-WINNER-ELIGIBILITY-GUARD.json`
  - `tasks/TASK-7642-BDC-DESIGNER-DOMAIN-SAFE-NORMALIZATION.json`
  - `tasks/TASK-7643-BDC-DESIGNER-OUTPUT-TRUST-SPLIT.json`
  - `tasks/TASK-7644-BDC-DESIGNER-BENCHMARK-AND-PREFLIGHT.json`
  - `tasks/TASK-7645-BDC-DESIGNER-EXTERNAL-RERUN-GATE.json`

## Verification (L0)
- Command: `Test-Path docs/project/BDC_DESIGNER_POST_COCKPIT_HARDENING_PLAN.md`
- Result: PASS
- Output summary: hardening charter file exists
- Command: `Get-Content tasks/TASK-7640-BDC-DESIGNER-POST-COCKPIT-HARDENING-CHARTER.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: task file parses as JSON
- Command: `Get-Content tasks/TASK-7645-BDC-DESIGNER-EXTERNAL-RERUN-GATE.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: last task in the chain parses as JSON

## Artifacts
- `docs/project/BDC_DESIGNER_POST_COCKPIT_HARDENING_PLAN.md` — bounded product hardening charter
- `tasks/TASK-7640-BDC-DESIGNER-POST-COCKPIT-HARDENING-CHARTER.json` — D0 task definition
- `tasks/TASK-7641-BDC-DESIGNER-WINNER-ELIGIBILITY-GUARD.json` — D1 task definition
- `tasks/TASK-7642-BDC-DESIGNER-DOMAIN-SAFE-NORMALIZATION.json` — D2 task definition
- `tasks/TASK-7643-BDC-DESIGNER-OUTPUT-TRUST-SPLIT.json` — D3 task definition
- `tasks/TASK-7644-BDC-DESIGNER-BENCHMARK-AND-PREFLIGHT.json` — D4/D5 task definition
- `tasks/TASK-7645-BDC-DESIGNER-EXTERNAL-RERUN-GATE.json` — D6 task definition

## Risks / Limitations
- This task opens the hardening program but does not yet fix the product defects.
- The Cockpit and TextAI rerun gate remains pending until D1-D6 code changes are complete.

## Rollback
- `git revert <commit>`
