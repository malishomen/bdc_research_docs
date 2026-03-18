# GITHUB SETTINGS REPORT (UTC 2026-01-07)

## Summary (status)
- Repo private: UNVERIFIED (gh repo view returned 404)
- Default branch = test: UNVERIFIED (gh repo view returned 404; local origin/HEAD points to origin/test)
- Auto-delete head branches: UNVERIFIED (UI-only)
- Merge methods: UNVERIFIED (UI-only)
- Dependabot alerts / dependency graph / security updates: UNVERIFIED (UI-only)

## Evidence (commands + output)
```
gh auth status --hostname github.com
github.com
  ✓ Logged in to github.com account malishomen (GITHUB_TOKEN)
  - Active account: true
  - Git operations protocol: https
  - Token: github_pat_11AULPP4I0noxI7vFB3DrO_***********************************************************

  ✓ Logged in to github.com account malishomen (keyring)
  - Active account: false
  - Git operations protocol: https
  - Token: gho_************************************
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'


gh repo view malishomen/Bio_Digital_Core --json nameWithOwner,isPrivate,defaultBranchRef,visibility
GraphQL: Could not resolve to a Repository with the name 'malishomen/Bio_Digital_Core'. (repository)


gh repo view --json nameWithOwner,isPrivate,defaultBranchRef,visibility
GraphQL: Could not resolve to a Repository with the name 'malishomen/Bio_Digital_Core'. (repository)


git branch -a -vv
* test                7af01b9 [origin/test] TASK-0005: repository audit report
  remotes/origin/HEAD -> origin/test
  remotes/origin/main f760329 Create agents.log.md compatibility alias file
  remotes/origin/test 7af01b9 TASK-0005: repository audit report
```

## Manual UI checklist (required due to API 404)
Settings -> General:
- Default branch = test

Settings -> Pull Requests:
- Automatically delete head branches = ON
- Allow squash merging = ON
- Allow merge commits = OFF
- Allow rebase merging = (record actual state)

Settings -> Security / Code security and analysis:
- Dependency graph = (record actual state)
- Dependabot alerts = (record actual state)
- Dependabot security updates = (record actual state)

## Notes
- No rulesets or branch protection changes were made (per constraints).
- API/gh access to the repo appears blocked or misconfigured (404). Verification and settings changes must be confirmed via GitHub UI using an account with access.