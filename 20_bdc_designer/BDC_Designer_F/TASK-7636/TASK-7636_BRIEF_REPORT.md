# TASK-7636 BRIEF REPORT

## Scope
- Review the current Cockpit `BDC_PACKET_PREP` status.
- Prepare the final corrective checklist that can turn it into an honest `BDC Designer`-ready packet in one cycle.
- Save a delivery copy for the Agent Studio case materials.

## Changes
- Created the final corrective checklist:
  - `reports/analysis/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST/BDC_PACKET_PREP_FINAL_CORRECTIVE_CHECKLIST.md`
- Created the task definition:
  - `tasks/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST.json`

## Verification (L0)
- Command: `Test-Path reports/analysis/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST/BDC_PACKET_PREP_FINAL_CORRECTIVE_CHECKLIST.md`
- Result: PASS
- Output summary: corrective checklist exists.

- Command: `Test-Path tasks/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST.json`
- Result: PASS
- Output summary: task definition exists.

- Command: `Get-Content tasks/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: task definition is valid JSON.

- Command: `Select-String -Path reports/analysis/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST/BDC_PACKET_PREP_FINAL_CORRECTIVE_CHECKLIST.md -Pattern 'Current Blockers','One-Cycle Mission','Final Readiness Gate','Final Self-Check','BDC_PACKET_READY.zip'`
- Result: PASS
- Output summary: checklist contains blockers, one-cycle mission, readiness gate, self-check, and final packaging rule.

## Artifacts
- `reports/analysis/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST/BDC_PACKET_PREP_FINAL_CORRECTIVE_CHECKLIST.md` — final pre-audit corrective checklist.
- `tasks/TASK-7636-BDC-DESIGNER-COCKPIT-FINAL-CORRECTIVE-CHECKLIST.json` — task registration.

## Risks / Limitations
- This checklist does not replace the measured packet itself; it only defines the last honest preparation cycle.
- If owner priorities remain unresolved, the packet should still remain blocked.

## Rollback
- `git revert <commit>`
