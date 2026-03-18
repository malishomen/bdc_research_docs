# TASK-7572 BRIEF REPORT

## Scope
- Normalize the repository instruction file from `agents.md` to `AGENTS.md` on `test`.
- Remove the case-only filename ambiguity that breaks branch switching on Windows with `core.ignorecase=true`.

## Changes
- Renamed the tracked instruction file:
  - `agents.md` -> `AGENTS.md`
- Corrected the internal self-reference in the document:
  - `AGENTS.md`

## Verification (L0)
- Command: `git ls-files | Select-String -Pattern '^(?i)agents\\.md$'`
- Result: PASS
- Output summary: only `AGENTS.md` remains tracked in `test`.

- Command: `Get-ChildItem -Force | Where-Object { $_.Name -match '^(?i)agents\\.md$' } | Select-Object Name,Length,LastWriteTime`
- Result: PASS
- Output summary: working tree contains `AGENTS.md`.

## Artifacts
- `AGENTS.md` — canonical repository instruction file with normalized filename.

## Risks / Limitations
- `main` still contains both `AGENTS.md` and `agents.md` until the merge line is corrected.
- Branch-switch verification must still be run after this commit because the historical `main` branch is the origin of the case conflict.

## Rollback
- `git revert <TASK-7572-commit>`
