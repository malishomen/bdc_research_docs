# TASK-0174 BRIEF REPORT

## Scope
- Add Cloudflare Access Service Token support to one-click clients (Windows + macOS).
- Auto-inject `CF-Access-Client-Id` / `CF-Access-Client-Secret` for API calls to `https://queen.bdc-hive.com`.
- Keep secrets local-only and optional in bundle builders.
- Provide L0 verification helper for Access-protected ping.

## Changes
- Windows client:
  - `tools/hive_core_mvp/drone_client/START_HIVE.bat`
  - `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
  - `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.bat`
  - Added Cloudflare Access credential discovery order:
    1. env vars
    2. `tools/hive_core_mvp/secrets/cloudflare_access.env`
    3. `tools/hive_core_mvp/drone_client/cloudflare_access.env`
  - All API calls now include Access headers when credentials are present.
- macOS client:
  - `tools/hive_core_mvp/drone_client_macos/START_HIVE.command`
  - Same credential discovery logic and header injection for `curl` requests.
- Bundle builders:
  - `tools/hive_core_mvp/drone_client/build_zip.ps1`
  - `tools/hive_core_mvp/drone_client_macos/build_zip.sh`
  - Added optional include-secrets mode (`-IncludeSecrets`, `--include-secrets`), default OFF.
- Access verification helper:
  - `tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
- Secret scaffolding and ignore policy:
  - `tools/hive_core_mvp/secrets/.gitkeep`
  - `.gitignore` updated for secret env locations.
- Runbook:
  - `tools/hive_core_mvp/README_RUNBOOK.md` updated with Cloudflare Access token section.

## Verification (L0)
- Command:
  - `pwsh -NoProfile -ExecutionPolicy Bypass -File tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
- Output:
  - `URL=https://queen.bdc-hive.com/v1/ping`
  - `ACCESS_HEADERS_USED=True`
  - `ACCESS_SOURCE=repo_secrets_file`
  - `STATUS=200`
  - `CONTENT_TYPE=text/html`
  - `LOOKS_JSON=False`
  - `BODY_PREVIEW=<!DOCTYPE html> ... Sign in ・ Cloudflare Access ...`
- Result: **PARTIAL**
  - Headers are injected and request succeeds to Access edge.
  - Response is still Cloudflare Access sign-in HTML (not JSON API ping).

- Windows one-click runtime proof:
  - Log: `tools/hive_core_mvp/drone_client/drone_mvp_log_20260218T014705Z.txt`
  - Evidence lines:
    - `Cloudflare Access headers enabled for endpoint=https://queen.bdc-hive.com`
    - `Step 1: ping`
    - parse failure due non-JSON response (`property 'ok' not found`).

- macOS one-click runtime proof:
  - Log: `tools/hive_core_mvp/drone_client_macos/drone_mvp_log_20260218T014800Z.txt`
  - Evidence lines:
    - `cloudflare_access_headers=enabled endpoint=https://queen.bdc-hive.com`
    - `Step 1: ping`
    - `ERROR: ping failed code=302`

- Bundle rebuild (default, no secrets):
  - Windows sha: `d111e67ed9f3e9959d9bc79d334b901a9deb5b366e4a47dbbcf59ed9fad21502`
  - macOS sha: `3366c8b65147b4ad7cb39f5435e75483b4dcd8118f2892ea895294f9a8392e2f`
  - manifests updated:
    - `dist/BUNDLE_MANIFEST.json`
    - `dist/BUNDLE_MANIFEST_MACOS15.json`

## Artifacts
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.bat`
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
- `tools/hive_core_mvp/drone_client/build_zip.ps1`
- `tools/hive_core_mvp/drone_client_macos/START_HIVE.command`
- `tools/hive_core_mvp/drone_client_macos/build_zip.sh`
- `tools/hive_core_mvp/tools/ingress/cloudflared/verify_access_headers.ps1`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- `tools/hive_core_mvp/secrets/.gitkeep`
- `dist/BUNDLE_MANIFEST.json`
- `dist/BUNDLE_MANIFEST_MACOS15.json`
- `dist/HIVE_DRONE_ONECLICK_LAPTOP.zip.sha256`
- `dist/HIVE_DRONE_ONECLICK_MACOS15.zip.sha256`

## Risks / Limitations
- Earlier `PARTIAL` limitation (HTML login/302 and then 502 origin mismatch) has been resolved in the closure update.
- Remaining scope note: this report closes JSON ping proof for TASK-0174; full register/poll/submit over HTTPS can be tracked as follow-up evidence task.

## Rollback
- Revert client script changes and helper script via git revert.
- Remove optional secret include flags in builders if needed.

## Closure Update (2026-02-18)
- Cloudflare tunnel token was corrected in local `tools/hive_core_mvp/tools/ingress/cloudflared/.env` (local-only).
- Cloudflare tunnel route for `queen.bdc-hive.com` was corrected to `http://host.docker.internal:8080` (not `127.0.0.1` inside container namespace).
- Verification helper was hardened for PowerShell response-header/runtime variants.

### Verification (L0) after fix
- Command: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\tools\hive_core_mvp\tools\ingress\cloudflared\verify_access_headers.ps1`
- Output:
  - `STATUS=200`
  - `CONTENT_TYPE=application/json`
  - `LOOKS_JSON=True`
  - `BODY_PREVIEW={"ok":true,"ts_utc":"2026-02-18T08:25:03Z","service":"hive-core","version":"0.1.0"}`
- Additional tunnel evidence:
  - `docker logs hive-cloudflared --tail 50` shows active tunnel and config update to:
    - `service":"http://host.docker.internal:8080"`

### Final status
- **SUCCESS** for TASK-0174 goal: Cloudflare Access service-token headers now produce JSON `/v1/ping` response through `https://queen.bdc-hive.com` with real L0 evidence.
