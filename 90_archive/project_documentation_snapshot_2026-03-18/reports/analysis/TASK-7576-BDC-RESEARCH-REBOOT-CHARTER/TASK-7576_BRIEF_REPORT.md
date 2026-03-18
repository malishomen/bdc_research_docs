# TASK-7576 BRIEF REPORT

## Scope
- Create the formal reboot charter for the renewed BDC scientific line.

## Changes
- Created:
  - `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`
  - `tasks/TASK-7576-BDC-RESEARCH-REBOOT-CHARTER.json`

## Verification (L0)
- Command: `Test-Path docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`
- Result: PASS
- Output summary: charter document exists.

- Command: `Select-String -Path docs/project/BDC_RESEARCH_REBOOT_CHARTER.md -Pattern 'Selection Physics Rebuild|BDC Designer|hidden_rule'`
- Result: PASS
- Output summary: charter contains the required separation and first-gate anchors.

## Artifacts
- `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md` — formal charter for the rebooted BDC scientific line.
- `tasks/TASK-7576-BDC-RESEARCH-REBOOT-CHARTER.json` — canonical task specification for the charter layer.

## Risks / Limitations
- This charter authorizes the reboot framing but does not itself run or validate any scientific package.

## Rollback
- `git revert <TASK-7576-commit>`

