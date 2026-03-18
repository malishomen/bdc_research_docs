# TASK-0155 L0 REVIEW BUNDLE — end-to-end verification (TASK-0154 durability cadence + dual STOP + live viz) via orchestrator

Mode: **L0-first** (artifact-derived facts only: paths, contents, sha256, timestamps, curl/netstat outputs, tool exit codes).

Repo root:
- `D:\projects\Bio_Digital_Core\Bio_digital_core`

Branch/HEAD (code):
- `test` @ `e6c2bd581270e57f9a48274ceae3585734b7081b`

Dataset root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Integrity gate (pre-check):
- `python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root <DATASET_ROOT>` => `KC_DATA_INTEGRITY: PASS`

## Port Auto-Select (R0)

### R0 (initial) — **FAIL** (port selection bug)

run_tag:
- `task0155_r0_port_busy_smoke`

Port selection file (L0):
- `logs/exp_0017_comprehension_v0_cloze/_launchers/PORT_SELECTION_task0155_r0_port_busy_smoke.json`
```json
{
  "chosen_port": 8848,
  "port_auto": true,
  "port_preferred": 8848
}
```

Observed failure (L0):
- Server bind failed with `WinError 10048` because `127.0.0.1:8848` was intentionally occupied; this indicates the port availability probe incorrectly treated the port as “free”.

Fix applied (in code; see commit for TASK-0155):
- `tools/launchers/exp0017_live_run.py`: port availability probe now uses `SO_EXCLUSIVEADDRUSE` when available to avoid false positives on Windows.

### R0b (re-run after fix) — **PASS**

run_tag:
- `task0155_r0b_port_busy_smoke`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T215430Z_e6c2bd5_task0155_r0b_port_busy_smoke`

Port selection file (L0):
- `logs/exp_0017_comprehension_v0_cloze/_launchers/PORT_SELECTION_task0155_r0b_port_busy_smoke.json`
```json
{
  "port_preferred": 8848,
  "chosen_port": 8849,
  "port_auto": true,
  "port_scan_max": 200
}
```

Crash-safe artifacts (presence + sha256; L0):
- `RUN_METADATA.json`: `ed8a38a814858edbc01e10ccfc72431d0780be37627f3bee829272cd8019287a`
- `RUN_STATUS.json`: `bef6afd3fb69302e82b88723c6d2c311875fccda97d9493a14fc8d45f29957b7`
- `metrics_by_step.jsonl`: `1ef298fad76b235bbcd9ca9cefaabc251b8486ca4a78fb8c2d777f0ac291a4a0`
- `metrics.json`: `7f83bc3fbe2c160552ef729208aaf46e7b81ecacf746685e267b5d549e134226`
- `policy_eval.json`: `42ee4bb3f8f4bb84411967c11e0e08adeaf441e1bc675c0ea8251050f1da5c26`

Integrity tool:
- `python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash` => `ok=true`, exit `0`

metrics_by_step markers (L0):
- first line: `event=RUN_START`
- last line: `event=RUN_END`, `reason=TIME_BUDGET_REACHED`

Localhost serving proof (read-only re-serve snapshots; L0):
- Started `localhost_server.py` on `127.0.0.1:8901` with root `ui/pacman_viz/_snapshots/task0155_r0b_port_busy_smoke`.
- `curl -D - http://127.0.0.1:8901/viewer.html` => `HTTP/1.0 200 OK`, `Cache-Control: no-store`
- `curl -D - http://127.0.0.1:8901/LATEST.json` => `HTTP/1.0 200 OK`, `Cache-Control: no-store`
- `netstat`: `TCP 127.0.0.1:8901 ... LISTENING`

## Live Run (R1) — 10m no STOP

run_tag:
- `task0155_r1_live_10m_no_stop`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T215746Z_e6c2bd5_task0155_r1_live_10m_no_stop`

Port selection (L0):
- `logs/exp_0017_comprehension_v0_cloze/_launchers/PORT_SELECTION_task0155_r1_live_10m_no_stop.json`:
  - `port_preferred=8848`, `chosen_port=8848`, `port_auto=true`

Crash-safe artifacts sha256 (L0):
- `RUN_METADATA.json`: `0ae30da9d12d6381dbd45fd9a010561d41ef3854a6d960c522cb82707508d167`
- `RUN_STATUS.json`: `db279cfbb87c9d74ba3a46b318a624fc9688de47afa038f6ca3e43c2e3f40732`
- `metrics_by_step.jsonl`: `054bce40dab396c93693d8ba7661d0f320c84f8f1bab3304c7f8161fde8ebff8`
- `metrics.json`: `13824c43c1b4c2d6abd10d7dcdd2c300006704ba2387fa06ac21b2365446848c`
- `policy_eval.json`: `3422d5a36fd3eb9d89cd0327c90abdb6b06abc3f473e9743d1af8f228b3885ad`

Integrity tool:
- `ok=true`, exit `0`

metrics_by_step markers (L0):
- first line: `event=RUN_START`
- last line: `event=RUN_END`, `reason=TIME_BUDGET_REACHED`, `state=COMPLETED`

Policy eval (L0):
- exit `0`, `verdict=PASS`

Snapshots (L0):
- `ui/pacman_viz/_snapshots/task0155_r1_live_10m_no_stop`
- strict snapshot count: `10`
- `LATEST.json` sha256: `f82415059f4944e8937d9cde0f37b7cdeee0eec5f829a3b1408d164094a25c93` (matches last snapshot)

Localhost serving proof (read-only re-serve snapshots; L0):
- `127.0.0.1:8902` => `HTTP 200` and `Cache-Control: no-store` for `/viewer.html` and `/LATEST.json`; `netstat` shows loopback LISTENING.

## Emergency STOP (R2) — 10m budget, STOP at ~2m

run_tag:
- `task0155_r2_live_10m_stop_emergency`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T220858Z_e6c2bd5_task0155_r2_live_10m_stop_emergency`

STOP evidence (L0):
- `STOP_REQUEST.json` sha256: `2128cd1e7dc1796eb42e60389c4ea2b13511aa91cb9251b13b5692c478eb448b`
- `STOPPED.json` sha256: `bb6bb45ce3618f8841e9c6d78d406e56411455b6d803b4378820bcf18c4aac41`
- `metrics_by_step.jsonl` last line is `event=RUN_END`, `state=STOPPED`, `reason=EMERGENCY_STOP` (see tool output in harvesting logs)

Crash-safe artifacts sha256 (L0):
- `RUN_METADATA.json`: `180254a143d501b70ff24143aa9739d51a4f5b37c0281b893c56e155032f3327`
- `RUN_STATUS.json`: `078290039105cb5465e39c0e4ccb4d71ee441a747246a8142a571e396c8f0aca`
- `metrics_by_step.jsonl`: `408259d403b0019de581114d0dc88fe6ffa5e239861bc6e30c09c47e7c984153`
- `STOPPED.json`: `bb6bb45ce3618f8841e9c6d78d406e56411455b6d803b4378820bcf18c4aac41`
- `policy_eval.json`: `bd70481152f30ecff1293a34baa48a6f5fa972c6e37cde635c5828b891a4885d`

Integrity tool:
- `ok=true`, exit `0` (accepts `STOPPED.json`)

Policy eval (L0):
- exit `1`, `verdict=ERROR` due to `missing metrics.json` (expected under emergency stop, since training may stop without writing `metrics.json`)

Snapshots (L0):
- strict snapshot count: `3`
- `LATEST.json` sha256: `6ab40d7b48b881b49a912327d6a5d91755cd4de86bfeca414da813249e921d40` (matches last snapshot)

Localhost serving proof (read-only re-serve snapshots; L0):
- `127.0.0.1:8903` => `HTTP 200` and `Cache-Control: no-store` for `/viewer.html` and `/LATEST.json`; `netstat` shows loopback LISTENING.

## Graceful STOP (R3) — 10m budget, STOP at ~2m

run_tag:
- `task0155_r3_live_10m_stop_graceful`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T221137Z_e6c2bd5_task0155_r3_live_10m_stop_graceful`

STOP evidence (L0):
- `STOP_REQUEST.json` sha256: `fb8da3e99b6f03de036feb78efa93b87531d555184c8f5be1f199b337d30070c`
- terminal artifact: `metrics.json` present (sha256 below)
- `metrics_by_step.jsonl` last line is `event=RUN_END` (here: `reason=MAX_STEPS_REACHED`, because graceful stop waits for safe boundary and the run was configured to stop at `max_steps=2000` on this short rehearsal)

Crash-safe artifacts sha256 (L0):
- `RUN_METADATA.json`: `ee16bfc7f8db124f115b07500be68fbdb890a084ff3816ff6fc15d40b66f3bae`
- `RUN_STATUS.json`: `8e68561ab84c2544cc42df865c1299a759bfd08ffc13c31d7de302fb2947ae5c`
- `metrics_by_step.jsonl`: `7cebec828cd14713eb1c2af5864fe2d850e9739b9a4a3eed5308b1f6bc6cbc4a`
- `metrics.json`: `43089cab11546166941ba961ad250698c2bc1f1b50d431dbee4b8cbedf576d7a`
- `policy_eval.json`: `23f25a2d2146932506e86d0ffa8b670f90faaf1650792b5eab1776f4c8ac3112`

Integrity tool:
- `ok=true`, exit `0`

Policy eval (L0):
- exit `2`, `verdict=FAIL` (`KC_IMPROVEMENT: FAIL`, delta=0 vs reference threshold)

Snapshots (L0):
- strict snapshot count: `5`
- `LATEST.json` sha256: `d3d6c0847784641d208487edd545f6c0725eeefad8cb9924f35bfaf1596d6514` (matches last snapshot)

Localhost serving proof (read-only re-serve snapshots; L0):
- `127.0.0.1:8904` => `HTTP 200` and `Cache-Control: no-store` for `/viewer.html` and `/LATEST.json`; `netstat` shows loopback LISTENING.

## Notes (L0-only)

- `policy_eval.json` during runs can show `exit_code=1` (`MAYBE_NO`) while `metrics.json` is not yet present; final policy write after training exit updates `policy_eval.json` (observable by its `LastWriteTimeUtc` / sha256).
- Snapshot daemon is time-budgeted separately; `LATEST.json` may reflect a “running” snapshot near the end even if training completed afterwards. This is a property of the snapshot cadence and stop timing, not an inferred state.

