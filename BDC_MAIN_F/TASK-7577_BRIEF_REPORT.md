# TASK-7577 BRIEF REPORT

## Scope
- Create the first scientific package of the rebooted BDC research line: Phase R1 selection-physics rebuild.

## Changes
- Created:
  - `docs/experiments/EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md`
  - `tasks/TASK-7577-BDC-SELECTION-PHYSICS-REBOOT-PACKAGE.json`

## Verification (L0)
- Command: `Test-Path docs/experiments/EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md`
- Result: PASS
- Output summary: experiment package document exists.

- Command: `Select-String -Path docs/experiments/EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md -Pattern '## Protocol|## Results|## Impact on Roadmap'`
- Result: PASS
- Output summary: required experiment sections are present.

## Artifacts
- `docs/experiments/EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md` — first reboot experiment package.
- `tasks/TASK-7577-BDC-SELECTION-PHYSICS-REBOOT-PACKAGE.json` — canonical task specification for Phase R1 packaging.

## Risks / Limitations
- This package defines the experiment but does not execute it.
- A future implementation package is still required to run the regimes and produce artifacts.

## Rollback
- `git revert <TASK-7577-commit>`
