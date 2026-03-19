# TASK-7638 BRIEF REPORT

## Scope
- Convert the negative `TASK-7637` findings into an exact native-intake contract-fix plan for the Cockpit packet.
- Prepare a matching start prompt so the partner can execute one bounded remap cycle without reopening measurement or architecture scope.

## Changes
- Created the native contract-fix document:
  - `reports/analysis/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX/BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md`
- Created the matching Gemini start prompt:
  - `reports/analysis/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX/GEMINI_START_PROMPT_FOR_NATIVE_CONTRACT_FIX.md`
- Saved delivery copies for Agent Studio:
  - `D:/projects/Bio_Digital_Core/Designer/Agent_Studio/OUT/BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md`
  - `D:/projects/Bio_Digital_Core/Designer/Agent_Studio/OUT/GEMINI_START_PROMPT_FOR_NATIVE_CONTRACT_FIX.md`
- Created the task definition:
  - `tasks/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX.json`

## Verification (L0)
- Command: `Test-Path D:/projects/Bio_Digital_Core/Designer/Agent_Studio/OUT/BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md`
- Result: PASS
- Output summary: delivery contract-fix document exists.

- Command: `Test-Path D:/projects/Bio_Digital_Core/Designer/Agent_Studio/OUT/GEMINI_START_PROMPT_FOR_NATIVE_CONTRACT_FIX.md`
- Result: PASS
- Output summary: delivery start prompt exists.

- Command: `Get-Content tasks/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX.json | ConvertFrom-Json | Out-Null`
- Result: PASS
- Output summary: task definition is valid JSON.

- Command: `Select-String -Path reports/analysis/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX/BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md -Pattern 'Required Final Folder Shape','Exact Source -> Target Remap','Unified variant comparison','Current runtime role mapping','Current slice metrics','Final Packaging Rule'`
- Result: PASS
- Output summary: contract-fix document contains exact target files, remap instructions, CSV targets, and final packaging rule.

## Artifacts
- `reports/analysis/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX/BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md` — exact native contract-fix plan.
- `reports/analysis/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX/GEMINI_START_PROMPT_FOR_NATIVE_CONTRACT_FIX.md` — start prompt for executing the remap cycle.
- `tasks/TASK-7638-BDC-DESIGNER-COCKPIT-NATIVE-CONTRACT-FIX.json` — task registration.

## Risks / Limitations
- This package does not itself make the partner packet native; it defines the exact remap needed.
- If the partner leaves required files under non-native names, the next BDC run will fail for the same reason.
- Local/unversioned runtime truth remains governance-weak but is still preferable to invented hashes.

## Rollback
- `git revert <commit>`
