# TASK-7634 BRIEF REPORT

## Scope
- Prepare a start prompt for the client's Gemini coder agent.
- Make the prompt explicitly reference `BDC_DESIGNER_RESPONSE_TO_COCKPIT.md`.
- Define concrete actions and expected packet-prep outputs.

## Changes
- Created the versioned Gemini start prompt:
  - `reports/analysis/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT/GEMINI_START_PROMPT_FOR_BDC_PACKET_PREP.md`
- Created the task definition:
  - `tasks/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT.json`

## Verification (L0)
- Command: `Test-Path reports/analysis/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT/GEMINI_START_PROMPT_FOR_BDC_PACKET_PREP.md`
- Result: PASS
- Output summary: versioned prompt exists.

- Command: `Test-Path tasks/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT.json`
- Result: PASS
- Output summary: task definition exists.

- Command: `Get-Content tasks/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: task definition is valid JSON.

- Command: `Select-String -Path reports/analysis/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT/GEMINI_START_PROMPT_FOR_BDC_PACKET_PREP.md -Pattern 'BDC_PACKET_PREP','02_RUNTIME_TRUTH.json','05_SLICE_METRICS.csv','Do not','packet_ready = yes/no'`
- Result: PASS
- Output summary: prompt contains explicit actions, output files, restrictions, and final response contract.

## Artifacts
- `reports/analysis/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT/GEMINI_START_PROMPT_FOR_BDC_PACKET_PREP.md` — start prompt for Gemini.
- `tasks/TASK-7634-BDC-DESIGNER-GEMINI-START-PROMPT.json` — task registration.

## Risks / Limitations
- The prompt is intentionally strict and packet-oriented; it is not a coding-spec prompt for feature implementation.
- It assumes the Gemini agent has access to the Cockpit project workspace and can inspect code, logs, and tests.

## Rollback
- `git revert <commit>`
