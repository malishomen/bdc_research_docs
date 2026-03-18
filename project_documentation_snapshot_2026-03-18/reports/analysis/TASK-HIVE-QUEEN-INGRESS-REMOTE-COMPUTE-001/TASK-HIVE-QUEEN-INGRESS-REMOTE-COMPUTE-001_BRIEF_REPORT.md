# TASK-HIVE-QUEEN-INGRESS-REMOTE-COMPUTE-001 BRIEF REPORT

## Scope
- Promote `bdc-queen` (`bdc@192.168.1.100`) as remote compute island for future experiments.
- Perform L0 ingress/domain audit and document current/public-access behavior.
- Fix SSH ingress runtime mismatch in cloudflared deployment (bridge-localhost issue).
- Add reusable remote-ops scripts and protocol docs.
- No secrets committed; no `results/` artifacts staged.

## Changes
- Added ingress/domain doc:
  - `docs/HIVE_INGRESS_AND_DOMAINS.md`
- Added remote compute protocol doc:
  - `docs/REMOTE_COMPUTE_PROTOCOL.md`
- Added ops scripts:
  - `scripts/ops/queen_healthcheck.ps1`
  - `scripts/ops/queen_healthcheck.sh`
  - `scripts/ops/queen_run_experiment.ps1`
- Added tracked cloudflared compose template (no token values):
  - `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
- Remote runtime change on queen (outside git, operational):
  - `/home/bdc/bdc/Bio_digital_core/tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
  - switched to `network_mode: host` + `extra_hosts: hive-core:127.0.0.1`.

## Verification (L0)
- DNS/Cloudflare resolution:
  - `nslookup queen.bdc-hive.com`
  - `nslookup viz.bdc-hive.com`
  - Result: PASS (Cloudflare anycast IPs).
- viz endpoint method behavior:
  - `curl -D - https://viz.bdc-hive.com/dist/LATEST.json -o NUL` -> `200`
  - `curl -I https://viz.bdc-hive.com/dist/LATEST.json` -> `405`, `allow: GET`
  - Result: PASS.
- Access protection:
  - `curl -I https://queen.bdc-hive.com/` -> `403` + `Cf-Access-Domain/Cf-Access-Aud`
  - Result: PASS.
- cloudflared L0 logs (queen):
  - `docker logs --tail ... hive-cloudflared`
  - Observed reconnect/TLS churn and previous SSH origin failure evidence:
    - historical: `dial tcp [::1]:22: connect: connection refused` for `ssh://localhost:22`.
  - After host-network fix: no new `connection refused` entries observed in tail.
- SSH domain attempt:
  - `ssh bdc@ssh.bdc-hive.com` -> timeout (raw SSH path, no origin-refused evidence in tunnel logs after fix).
  - Result: PARTIAL (transport/access path not fully validated end-to-end in this environment; regression from origin-refused not observed).
- Ops scripts:
  - `pwsh -File scripts/ops/queen_healthcheck.ps1` -> PASS (host/resource/docker snapshot output).
  - `bash scripts/ops/queen_healthcheck.sh` -> PARTIAL in this host (`Permission denied (publickey)` in current bash key context).
  - `pwsh -File scripts/ops/queen_run_experiment.ps1 ...` smoke:
    - commit `e8152d6`
    - command: `python3 -m evolution.edp1_symbolic.run_generations --out_dir results/remote_smoke_task_hive_queen_001 --genome_version v1 --seed 1337 --generations 5 --population 20`
    - out root: `results/remote_smoke_task_hive_queen_001`
    - Result: PASS; pulled compact artifact locally:
      - `results/remote_compact/queen_run_20260227T183139Z/summary.json`

## Artifacts
- `docs/HIVE_INGRESS_AND_DOMAINS.md`
- `docs/REMOTE_COMPUTE_PROTOCOL.md`
- `scripts/ops/queen_healthcheck.ps1`
- `scripts/ops/queen_healthcheck.sh`
- `scripts/ops/queen_run_experiment.ps1`
- `tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml`
- `reports/analysis/TASK-HIVE-QUEEN-INGRESS-REMOTE-COMPUTE-001/TASK-HIVE-QUEEN-INGRESS-REMOTE-COMPUTE-001_BRIEF_REPORT.md`

## Risks / Limitations
- SSH via public domain remains environment-dependent (Access client flow / raw SSH path); current validation confirms removal of prior origin-localhost refusal pattern but not full interactive SSH success.
- `queen_healthcheck.sh` was not fully validated in this Windows/bash keychain context; PowerShell variant is validated.
- cloudflared still experiences periodic edge reconnect noise; service remains operational but should be monitored.

## Rollback
- Repo rollback:
  - `git revert <TASK-HIVE-QUEEN-INGRESS-REMOTE-COMPUTE-001-commit>`
- Queen runtime rollback:
  - restore backup compose on queen:
    - `/home/bdc/bdc/Bio_digital_core/tools/hive_core_mvp/tools/ingress/cloudflared/docker-compose.yml.bak_20260227T1825Z`
  - then `docker compose up -d cloudflared`
