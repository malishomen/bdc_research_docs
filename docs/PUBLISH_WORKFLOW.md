# Publish Workflow

## Repository
- GitHub: `https://github.com/malishomen/bdc_research_docs`
- Local root: `D:\projects\Bio_Digital_Core\bdc_research_docs`

## One-step Refresh + Commit + Push
Run from repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\refresh_commit_push.ps1
```

Optional custom message:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\refresh_commit_push.ps1 -CommitMessage "Refresh research mirror after BDC update"
```

## What It Does
1. Refreshes from `D:\projects\Bio_Digital_Core\Temp\research`
2. Shows `git status --short`
3. Stages all changes
4. Commits only if changes exist
5. Pushes to `origin/main`

## Review Rule
If the refresh contains unexpected deletions or layout changes, stop and inspect before pushing.
