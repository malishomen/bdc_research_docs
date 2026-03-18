# TASK-7578 BRIEF REPORT

## Scope
- Define the documentation-first execution package for the next bounded `BDC Designer` line.
- Cover only planning artifacts for:
  - calibration
  - selective prediction
  - generalized risk
  - evidence-state semantics

## Changes
- Created the master import plan:
  - `docs/project/BDC_DESIGNER_CONFIDENCE_EVIDENCE_IMPORT_PLAN.md`
- Created strict ordered task packets:
  - `tasks/TASK-7578-BDC-DESIGNER-CONFIDENCE-EVIDENCE-IMPORT-PLAN.json`
  - `tasks/TASK-7579-BDC-DESIGNER-CALIBRATION-LAYER.json`
  - `tasks/TASK-7580-BDC-DESIGNER-SELECTIVE-PREDICTION-CONTRACT.json`
  - `tasks/TASK-7581-BDC-DESIGNER-GENERALIZED-RISK-EVALUATION.json`
  - `tasks/TASK-7582-BDC-DESIGNER-EVIDENCE-STATE-SEMANTICS.json`
- Updated project continuity references:
  - `docs/project/project_main_doc.md`
  - `docs/project/project_roadmap.md`

## Verification (L0)
- Command: `Test-Path docs/project/BDC_DESIGNER_CONFIDENCE_EVIDENCE_IMPORT_PLAN.md`
- Result: PASS
- Output summary: plan document exists

- Command: `Get-Content tasks/TASK-7578-BDC-DESIGNER-CONFIDENCE-EVIDENCE-IMPORT-PLAN.json, tasks/TASK-7579-BDC-DESIGNER-CALIBRATION-LAYER.json, tasks/TASK-7580-BDC-DESIGNER-SELECTIVE-PREDICTION-CONTRACT.json, tasks/TASK-7581-BDC-DESIGNER-GENERALIZED-RISK-EVALUATION.json, tasks/TASK-7582-BDC-DESIGNER-EVIDENCE-STATE-SEMANTICS.json | Out-String | ConvertFrom-Json`
- Result: NOT USED
- Output summary: PowerShell cannot parse concatenated JSON objects in a single stream, so per-file parse was used instead

- Command: `Get-Content tasks/TASK-7578-BDC-DESIGNER-CONFIDENCE-EVIDENCE-IMPORT-PLAN.json | ConvertFrom-Json | Out-Null; Get-Content tasks/TASK-7579-BDC-DESIGNER-CALIBRATION-LAYER.json | ConvertFrom-Json | Out-Null; Get-Content tasks/TASK-7580-BDC-DESIGNER-SELECTIVE-PREDICTION-CONTRACT.json | ConvertFrom-Json | Out-Null; Get-Content tasks/TASK-7581-BDC-DESIGNER-GENERALIZED-RISK-EVALUATION.json | ConvertFrom-Json | Out-Null; Get-Content tasks/TASK-7582-BDC-DESIGNER-EVIDENCE-STATE-SEMANTICS.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: all five task packets parse as valid JSON

- Command: `Select-String -Path docs/project/project_main_doc.md, docs/project/project_roadmap.md -Pattern 'BDC_DESIGNER_CONFIDENCE_EVIDENCE_IMPORT_PLAN.md'`
- Result: PASS
- Output summary: both project docs now reference the new import plan

## Artifacts
- `docs/project/BDC_DESIGNER_CONFIDENCE_EVIDENCE_IMPORT_PLAN.md` — master plan and package-level DoD
- `tasks/TASK-7578-BDC-DESIGNER-CONFIDENCE-EVIDENCE-IMPORT-PLAN.json` — documentation gate task
- `tasks/TASK-7579-BDC-DESIGNER-CALIBRATION-LAYER.json` — calibration implementation task
- `tasks/TASK-7580-BDC-DESIGNER-SELECTIVE-PREDICTION-CONTRACT.json` — selective-prediction task
- `tasks/TASK-7581-BDC-DESIGNER-GENERALIZED-RISK-EVALUATION.json` — generalized-risk task
- `tasks/TASK-7582-BDC-DESIGNER-EVIDENCE-STATE-SEMANTICS.json` — evidence-state semantics task
- `docs/project/project_main_doc.md` — continuity reference updated
- `docs/project/project_roadmap.md` — continuity reference updated

## Risks / Limitations
- This task intentionally does not change code.
- The plan assumes implementation will proceed in strict order `7579 -> 7580 -> 7581 -> 7582`.
- External-source import reasoning is reflected through planning references, not embedded source excerpts.

## Rollback
- `git revert <commit>`
