# TASK-0162 BRIEF REPORT

## Scope
- Security hardening v1.1 for HIVE MVP API in `tools/hive_core_mvp`.
- Add stronger baseline controls for online use while keeping MVP simplicity.

## Implemented

### 1) Network exposure posture (VPN-first)
- Updated runbook with explicit operational mode matrix:
  - LAN-only: allowed
  - VPN/Tailscale: allowed/recommended
  - Managed tunnel: conditional
  - Raw public port-forward: prohibited for MVP
- File: `tools/hive_core_mvp/README_RUNBOOK.md`

### 2) Anti-abuse baseline: rate limiting
- Added in-memory IP+route rate limiting with env controls:
  - `ENABLE_RATE_LIMIT`
  - `RATE_LIMIT_WINDOW_SEC`
  - `RATE_LIMIT_MAX_REQUESTS`
  - `RATE_LIMIT_REGISTER_MAX_REQUESTS`
- Enforced on register/poll/result/revoke endpoints.
- File: `tools/hive_core_mvp/hive_core/main.py`

### 3) Token expiry and revocation mechanics
- Existing expiry check retained in token authorization path.
- Added explicit revoke endpoint:
  - `POST /v1/tokens/revoke`
  - revokes current token (or all drone tokens with `revoke_all=true`)
- Revocation events are audited.
- File: `tools/hive_core_mvp/hive_core/main.py`

### 4) Replay protection (nonce + timestamp skew)
- Added strict client-proof enforcement with feature-flag rollback:
  - `ENABLE_STRICT_CLIENT_PROOF` (default true)
  - `CLIENT_PROOF_MAX_SKEW_SEC`
  - `NONCE_TTL_SEC`
- Server validates:
  - ISO timestamp parse and skew window
  - nonce uniqueness per drone within TTL window
- Added DB table:
  - `hive_seen_nonces(drone_id, nonce_hash, seen_ts, expires_ts, unique(drone_id, nonce_hash))`
- Files:
  - `tools/hive_core_mvp/db/init.sql`
  - `tools/hive_core_mvp/hive_core/main.py`

### 5) Config surface
- Added new env fields in `.env.example`.
- File: `tools/hive_core_mvp/.env.example`

## Threat Model (MVP v1.1)

### Threats addressed
- Blind endpoint abuse / burst traffic.
- Token replay after leak.
- Client proof replay (same nonce).
- Stale delayed result injection with old timestamps.

### Controls now present
- Per-IP route rate limiting.
- Token hash storage + expiry + explicit revocation.
- Nonce replay rejection (409) and strict timestamp skew validation.
- VPN-first exposure guidance and firewall posture in runbook.

### Residual risks
- In-memory rate limit is single-instance and non-distributed.
- Nonce cache in Postgres can grow if retention is misconfigured.
- Bearer-token model still vulnerable if endpoint host is compromised.
- No mTLS/device attestation yet (out of scope).

## Verification (L0)

### Local checks executed
1. Replay rejection:
- First `/v1/tasks/result` => `200`
- Second request with same nonce => `409`

2. Revocation rejection:
- `/v1/tokens/revoke` => `200`
- subsequent `/v1/tasks/poll` with revoked token => `401`

3. Expiry rejection:
- token forced expired in DB (`expires_ts=now()-5m`)
- subsequent `/v1/tasks/poll` => `401`

4. Unauthenticated rejection:
- `/v1/tasks/poll` without Bearer token => `401`

### DB evidence snapshots
- `hive_tokens` shows revoked_ts populated for revoked token and past expires_ts for expired token case.
- `hive_seen_nonces` contains recorded nonce hash and expiry window.

### Service logs evidence
- `hive-core` logs include:
  - `409 Conflict` on replay attempt
  - `token_revoked` audit event
  - `401 Unauthorized` after revocation and after expiry

## Rollback
- Fast rollback path (feature-flag):
  - set `ENABLE_STRICT_CLIENT_PROOF=false` to return to MVP behavior for client proof checks.
- Full rollback:
```powershell
cd tools/hive_core_mvp
docker compose down -v
# restore previous commit if needed
```

## Files changed
- `tools/hive_core_mvp/hive_core/main.py`
- `tools/hive_core_mvp/db/init.sql`
- `tools/hive_core_mvp/.env.example`
- `tools/hive_core_mvp/README_RUNBOOK.md`
- `reports/analysis/TASK-0162_BRIEF_REPORT.md`
