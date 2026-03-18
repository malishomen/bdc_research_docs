# HIVE Ingress And Domains

Last verified: 2026-02-27 (UTC)

## L0 Inventory

| Hostname | Origin service | Access policy | Healthcheck method | Expected status |
|---|---|---|---|---|
| `viz.bdc-hive.com` | `http://hive-core:8080` (tunnel ingress), effective from cloudflared host-network via `hive-core -> 127.0.0.1` | Public (no Access challenge on `/dist/LATEST.json`) | `GET https://viz.bdc-hive.com/dist/LATEST.json` | `200 OK` |
| `queen.bdc-hive.com` | `http://hive-core:8080` | Cloudflare Access protected | `curl -I https://queen.bdc-hive.com/` | `403` + `Cf-Access-*` headers |
| `ssh.bdc-hive.com` | `ssh://localhost:22` (from tunnel config) | Access-controlled SSH path | `ssh bdc@ssh.bdc-hive.com` (raw TCP test) + tunnel logs | Direct raw SSH may timeout; tunnel logs must not show `origin connect refused` |

## L0 Observations (No-Change Audit)

- DNS resolution:
  - `queen.bdc-hive.com` and `viz.bdc-hive.com` resolve to Cloudflare IP ranges (`188.114.96.3`, `188.114.97.3`, IPv6 anycast).
- HTTP behavior:
  - `GET https://viz.bdc-hive.com/dist/LATEST.json` -> `200 OK`.
  - `HEAD https://viz.bdc-hive.com/dist/LATEST.json` -> `405 Method Not Allowed` (`allow: GET`).
  - `curl -I https://queen.bdc-hive.com/` -> `403 Forbidden` with `Cf-Access-Domain` and `Cf-Access-Aud`.
- cloudflared logs showed periodic reconnects and TLS handshake noise (edge connectivity churn), with eventual re-registration of tunnel connections.

## What Was Broken

Historical broken path confirmed in logs:

- `destAddr=ssh://localhost:22` with:
  - `dial tcp [::1]:22: connect: connection refused`

Why:
- `hive-cloudflared` ran in bridge network (`hive_mvp_net`), so `localhost` referred to container namespace, not host `sshd`.
- SSH ingress target `ssh://localhost:22` therefore failed.

## Fix Applied

- Switched cloudflared runtime to host networking on queen.
- Added host mapping for HTTP ingress name resolution:
  - `extra_hosts: hive-core:127.0.0.1`
- Kept tunnel token out of git; only compose template with `${CLOUDFLARED_TUNNEL_TOKEN}` is stored in repo.

Runtime compose template is tracked at:

- `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`

## Healthcheck Practice Update

- Do not use `HEAD` for `viz ... /dist/LATEST.json`; service explicitly answers `405`.
- Canonical check:
  - `GET https://viz.bdc-hive.com/dist/LATEST.json` expecting `200`.
