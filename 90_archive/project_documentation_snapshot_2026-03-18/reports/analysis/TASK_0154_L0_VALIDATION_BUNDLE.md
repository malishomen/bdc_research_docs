# TASK-0154 L0 VALIDATION BUNDLE — exp_0017 durability cadence + dual STOP + live stack

This document is **L0-only**: paths, commands, exit codes, sha256, and short artifact excerpts.

Repo root:
- `D:\projects\Bio_Digital_Core\Bio_digital_core`

Dataset root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Runbook:
- `reports/analysis/TASK_0154_MONITORING_COMMANDS.md`

## V1 — 5m (no STOP)

run_tag:
- `task0154_v1_5m_no_stop`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T195939Z_83303a9_task0154_v1_5m_no_stop`

Gates:
- `exp0017_artifact_integrity_check.py` exit: `0` (`ok=true`)
- `exp0017_progress_policy_eval.py` exit: `0` (`verdict=PASS`)

SHA256 bundle:
- `RUN_METADATA.json`: `d0d94015f6860ba0295988e40ddcf1a21433673d366682e8f47fd5934ba77f8b`
- `RUN_STATUS.json`: `921cf28b0976b2d5471362f2abbfd74b971032ba3528b8aae165f2814717dea6`
- `metrics_by_step.jsonl`: `58fa4a6728f3e56ed52849a1bbef650e5fa4d47788ba81a6d1af8ca9e5a403da`
- `metrics.json`: `b3af0ba2e192909f5ac3b5a3264c5d807b6b6f3580e840dfb5ebdbf6092f0f8d`
- `policy_eval.json`: `3e3ced4b3f1daf62a1e92916731ae34ad1990604ab7118584f0058a219121954`

Snapshots:
- `ui/pacman_viz/_snapshots/task0154_v1_5m_no_stop`
- `snapshot_*.json` count (strict): `5`
- `LATEST.json` sha256: `5c28f47ab87cb9a7bced436b3eed796d6c1cb195b622358f2149763af8b577e5` (matches last snapshot)

Localhost evidence:
- Server launcher log (L0 bind + args):
  - `logs/exp_0017_comprehension_v0_cloze/_launchers/localhost_server_task0154_v1_5m_no_stop.log`:
    - `CMD=... localhost_server.py ... --port 8851 --bind 127.0.0.1`
- HTTP header behavior (Cache-Control: no-store) + loopback enforcement is verified by unit tests (see TASK-0154 `pytest -q` gate), not by runtime curl in this bundle.

Policy eval stdout snapshot (JSON):
```json
{
  "exit_code": 0,
  "verdict": "PASS",
  "problems": [],
  "info": {
    "dataset_integrity": {
      "actual": "dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687",
      "expected": "dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687"
    },
    "runs": [
      {
        "tag": "task0154_v1_5m_no_stop",
        "git_head": "83303a95bbb1f03ef3b033d0b22933c226185b18",
        "seed": 12345,
        "val": { "acc": 0.15206192086203554, "k": 18035, "n": 118603 },
        "test": { "acc": 0.14655604207396875, "k": 18141, "n": 123782 }
      }
    ]
  }
}
```

## V2 — 5m (EMERGENCY STOP @ ~2m)

run_tag:
- `task0154_v2d_5m_emergency_stop`

stop mode:
- `emergency`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T203422Z_83303a9_task0154_v2d_5m_emergency_stop`

STOP evidence (L0):
- `<run_dir>/STOP_REQUEST.json` head:
  - `mode=emergency`, `reason=EMERGENCY_STOP`, `requested_by=viewer`, `ts_utc=2026-02-09T20:35:48Z`
- `<run_dir>/STOPPED.json`:
  - `reason=EMERGENCY_STOP`, `step=899`, `ts_utc=2026-02-09T20:35:51Z`
- `metrics_by_step.jsonl` last line:
  - `{"event":"RUN_END","state":"STOPPED","reason":"EMERGENCY_STOP","step":899,...}`

Gates:
- integrity exit: `0` (`ok=true`)
- policy eval exit: `1` (`verdict=ERROR`, reason: `missing metrics.json` in emergency stop)

SHA256 bundle:
- `RUN_METADATA.json`: `06ec6925eb951fc7ea8b4377b30e59e060152619e144039ff667c584277acbe2`
- `RUN_STATUS.json`: `db3e5a4f60184d6acf1716338c0fc5c71bf45197a4ffb42135b2bbf9ca81ad4d`
- `metrics_by_step.jsonl`: `ddba033ef7184f53ee164fcc6dc483d02e6efb7dd5b408fd90ad9bb8ff20a411`
- `STOPPED.json`: `bbd4dc661abce21bbb1f671a7c1e6362067b00438ed25c39cbcba447fa1f302d`
- `STOP_REQUEST.json`: `dde49a63e94f49b1c418071d47c8b8da0ab01b8c45d38af94c595b0bfd49e660`
- `policy_eval.json`: `d00cf290b5f387f42136f3c110dc9e38118dd6532eabe2811b0e7a703f50b73e`

Snapshots:
- `ui/pacman_viz/_snapshots/task0154_v2d_5m_emergency_stop`
- `snapshot_*.json` count (strict): `2`
- `LATEST.json` sha256: `02e13acdf28a5243a5cfefa1f1f14aa0afcd4ca99f4c6c095b941eea3be23c11` (matches last snapshot)

Localhost evidence (L0):
- `logs/exp_0017_comprehension_v0_cloze/_launchers/localhost_server_task0154_v2d_5m_emergency_stop.log` contains:
  - `BIND_OK host=127.0.0.1 port=8857 ... control_stop=on`
  - `127.0.0.1 - "POST /control/stop_emergency HTTP/1.1" 200 -`

Policy eval stdout snapshot (JSON):
```json
{
  "verdict": "ERROR",
  "problems": [
    "failed to load run tag=task0154_v2d_5m_emergency_stop: FileNotFoundError: missing metrics.json: logs\\\\exp_0017_comprehension_v0_cloze\\\\run_20260209T203422Z_83303a9_task0154_v2d_5m_emergency_stop\\\\metrics.json"
  ],
  "info": {
    "runs": []
  }
}
```

## V3 — 5m (GRACEFUL STOP @ ~2m; eval_every=200)

run_tag:
- `task0154_v3d_5m_graceful_stop`

stop mode:
- `graceful`

run_dir:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\logs\exp_0017_comprehension_v0_cloze\run_20260209T203615Z_83303a9_task0154_v3d_5m_graceful_stop`

STOP evidence (L0):
- `<run_dir>/STOP_REQUEST.json` head:
  - `mode=graceful`, `reason=GRACEFUL_STOP`, `requested_by=viewer`, `ts_utc=2026-02-09T20:37:42Z`
- terminal artifact: `metrics.json` present
- `metrics_by_step.jsonl` last line:
  - `{"event":"RUN_END","state":"COMPLETED","reason":"MAX_STEPS_REACHED","step":800,...}`

Gates:
- integrity exit: `0` (`ok=true`)
- policy eval exit: `2` (`verdict=FAIL`, `KC_IMPROVEMENT: FAIL`)

SHA256 bundle:
- `RUN_METADATA.json`: `e444bca7560d0590092d19cbafe9bf0f1865aeac3e6db7c0f1e281ac669ee4ce`
- `RUN_STATUS.json`: `6357fd879405af9e5f68758aa3a8ef466af6f98e2737ffbe2109f45c10220bce`
- `metrics_by_step.jsonl`: `f4cc45b4c6377e76b0a9b938da5fbf6d83e92236f2fa42b973428794aba919d0`
- `metrics.json`: `d2b85eb9a1e4886b6d5a4357dcf328185b4a883f232ed1b3bc81668bc14a1a3f`
- `STOP_REQUEST.json`: `f8f2876d287cce9b9f6d3b6b13973f4648743b1294d70d1f7887e90021469981`
- `policy_eval.json`: `c8f7290e516a263c561fd5ce83bf371a9b161704a258381475d7a0f652f78946`

Snapshots:
- `ui/pacman_viz/_snapshots/task0154_v3d_5m_graceful_stop`
- `snapshot_*.json` count (strict): `3`
- `LATEST.json` sha256: `8d32e62e259a653c62adc7f7c7551260decdb82d46125d4016976a496da27b1e` (matches last snapshot)

Localhost evidence (L0):
- `logs/exp_0017_comprehension_v0_cloze/_launchers/localhost_server_task0154_v3d_5m_graceful_stop.log` contains:
  - `BIND_OK host=127.0.0.1 port=8858 ... control_stop=on`
  - `127.0.0.1 - "POST /control/stop_graceful HTTP/1.1" 200 -`

Policy eval stdout snapshot (JSON):
```json
{
  "exit_code": 2,
  "verdict": "FAIL",
  "problems": [
    "KC_IMPROVEMENT: FAIL tag=task0154_v3d_5m_graceful_stop val_acc=0.107864 ref=0.117586 delta=-0.009722 need>=0.020 ci_required=False"
  ]
}
```
