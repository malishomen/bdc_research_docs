# TASK-0178 BRIEF REPORT

## Scope
- Implement one-command Windows friend bundle creation (Option A) with:
  - fresh single-use invite
  - embedded Cloudflare Access service token file
  - `QUEEN_URL.txt`, `JOIN_CODE.txt`
  - zip hash and manifest

## Changes
- Added script:
  - `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
- Updated runbook:
  - `tools/hive_core_mvp/README_RUNBOOK.md`
- Repo hygiene guard:
  - `.gitignore` now ignores `tools/hive_core_mvp/dist/` runtime bundles (contain embedded secret/invite in Option A)

## Verification (L0)
- Command run:
  - `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/drone_client/build_friend_bundle.ps1 -HostLabel FRIEND-TEST`

- Output bundle files:
  - `tools/hive_core_mvp/dist/HIVE_FRIEND_20260218T091109Z.zip`
  - `tools/hive_core_mvp/dist/HIVE_FRIEND_20260218T091109Z.zip.sha256`
  - `tools/hive_core_mvp/dist/BUNDLE_MANIFEST_FRIEND_20260218T091109Z.json`

- ZIP content check:
  - contains `START_HIVE.bat`
  - contains `WindowsDroneOneClick.bat`
  - contains `WindowsDroneOneClick.ps1`
  - contains `README_FOR_FRIEND.txt`
  - contains `QUEEN_URL.txt`
  - contains `JOIN_CODE.txt`
  - contains `cloudflare_access.env` (Option A)

- SHA256 check:
  - `certutil -hashfile tools/hive_core_mvp/dist/HIVE_FRIEND_20260218T091109Z.zip SHA256`
  - Result: `c6fe675841ced4747c2199df69b1d9d26a09726ae54a798a288bfd1dc7a62c6c`
  - `.sha256` file matches the same hash.

- DB invite evidence (redacted invite code, hash only):
  - Query:
    - `docker compose exec -T postgres psql -U hive -d hive -c "select invite_code_hash, created_ts, used_ts from hive_invites where invite_code_hash='28c033605f6150f248684f16da44f860d14b2531dbc07f5873486fecb7e96167';"`
  - Result:
    - row exists with `created_ts=2026-02-18 09:11:10.689671+00`
    - `used_ts` is `NULL` at creation time.

## Artifacts
- `tools/hive_core_mvp/drone_client/build_friend_bundle.ps1`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- `reports/analysis/TASK-0178_BRIEF_REPORT.md`

## Risks / Limitations
- Option A intentionally embeds Access token in distributable ZIP.
- Restrict distribution to trusted volunteers and rotate Access token on leak suspicion.

## Rollback
- `git revert` TASK-0178 commits.
- Runtime bundles in `tools/hive_core_mvp/dist/` can be deleted locally.

## L0 Runtime Proof Update (Laptop friend run, 2026-02-18)
- Source log excerpt provided from laptop one-click execution.
- Observed sequence:
  - `Step 1: ping` -> `Ping ok=True`
  - `Step 2: register` -> `Registered drone_id=aed4a1f7-a805-4114-bb55-7527b5f7a355`
  - `Step 3: poll task` -> `task_id=41903b03-59b4-4638-a180-e873a9b28764`
  - `Step 4: submit result` -> `Result accepted=True`
  - `One-click flow complete.`
- Volunteer first-run capture was confirmed on laptop:
  - `Volunteer profile captured from GUI display_name=Laptop Dan`
  - profile then reused in same run (`Volunteer profile active ...`)

Conclusion:
- Option A bundle worked end-to-end on remote laptop with Cloudflare Access headers and accepted result.
