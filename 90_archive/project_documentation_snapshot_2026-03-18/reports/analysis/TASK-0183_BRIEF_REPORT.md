# TASK-0183 BRIEF REPORT

## Scope
- Implement device-bound claim auth flow and local-only stop controls for Windows drone client.

## Changes
- Server (`hive-core`):
  - Added `POST /v1/drones/claim` endpoint.
  - Added DB entities for device keys and token binding (`hive_device_keys`, `hive_tokens.pubkey_sha256`, `hive_tokens.token_mode`).
  - Added request-signature enforcement on `/v1/tasks/poll` and `/v1/tasks/result` for claim-bound tokens.
- Client (Windows):
  - `WindowsDroneOneClick.ps1` now:
    - generates/loads local device key,
    - performs claim flow (`/v1/drones/claim`) and persists local claim state,
    - signs poll/result requests and sends `X-HIVE-*` headers,
    - respects local soft-stop file before major API steps,
    - writes local PID file for stop scripts.
  - Added local-only stop launchers:
    - `STOP_HIVE_NOW.bat`
    - `STOP_HIVE_SOFT.bat`
  - Updated `START_HIVE.bat`, `README_FOR_FRIEND.txt`, bundle scripts.

## Verification (L0)
- `python -m py_compile tools/hive_core_mvp/hive_core/main.py` -> PASS
- `python -m py_compile tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1` -> N/A (PowerShell)
- `PYTHONPATH=. pytest -q tests/test_localhost_server_loopback_only.py tests/test_localhost_stop_endpoint_loopback_token.py` -> PASS (regression)

## Artifacts
- `tools/hive_core_mvp/hive_core/main.py`
- `tools/hive_core_mvp/db/init.sql`
- `tools/hive_core_mvp/drone_client/WindowsDroneOneClick.ps1`
- `tools/hive_core_mvp/drone_client/STOP_HIVE_NOW.bat`
- `tools/hive_core_mvp/drone_client/STOP_HIVE_SOFT.bat`
- `tools/hive_core_mvp/drone_client/START_HIVE.bat`
- `tools/hive_core_mvp/drone_client/build_zip.ps1`

## Risks / Limitations
- Requested algorithm was Ed25519, but current Windows PowerShell/.NET environment lacks native Ed25519 type; implemented ECDSA P-256 device signatures as pragmatic fallback (`algorithm=ECDSA_P256`).
- Full second-device invite-reuse proof remains UNVERIFIED in this session.

## Runtime Fix Follow-Up (2026-02-18)
- Added Windows runtime compatibility fixes in `WindowsDroneOneClick.ps1`:
  - PowerShell/.NET hash fallback (`ComputeHash` path),
  - CNG P-256 key/sign fallback for older environments,
  - DER-compatible signature conversion for CNG signatures,
  - claim/poll/result pubkey header consistency.
- Live e2e proof from friend Windows 11 client:
  - `Step 2: claim` -> `Claimed drone_id=c83e62a1-a7ca-40c1-9247-3f0b6e4a0ad4`
  - `Step 3: poll task` -> task received
  - `Step 4: submit result` -> `Result accepted=True server_ts=2026-02-18T17:54:46Z`
- DB correlation on Queen:
  - `hive_device_keys` includes `drone_id=c83e62a1-a7ca-40c1-9247-3f0b6e4a0ad4`, `algorithm=ECDSA_P256`.
  - `hive_tokens` includes `token_mode=device_claim` with non-null `pubkey_sha256`.

## Rollback
- Revert claim/signature code paths and keep legacy `/v1/drones/register` flow.
- Disable strict signature checks via env if needed.
