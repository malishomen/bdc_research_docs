# TASK-0151 L0 RUN BUNDLE — exp_0017 results harvest + viz pipeline evidence (file-based)

Branch: `test`

This report is **L0 evidence-only** (paths, hashes, command outputs). No training semantics or metrics logic changes were made.

## 1) Chosen Run (Most Recent Completed)

Selection rule (L0):
- newest `logs/exp_0017_comprehension_v0_cloze/run_*` with `metrics.json` OR `CRASH.json` present.

Chosen run_dir:
- `logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz`

## 2) Identity (from run artifacts)

From `logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz/RUN_STATUS.json` and `metrics_by_step.jsonl`:
- run_tag: `task0149_live_45m_viz`
- git_head_run: `4c913b3e22eaa840f7d95e9695feecd9ea99749b`
- device: `cuda`
- seed: `12345` (from `RUN_METADATA.json`)
- dataset_root: `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build` (from `RUN_METADATA.json`)

## 3) Gates (L0)

### 3.1 KC_DATA_INTEGRITY

Command (stdout captured):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root $root
```

Observed:
- `KC_DATA_INTEGRITY: PASS`
- launcher log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T171153Z_task0151_integrity_only.log`

### 3.2 Artifact Integrity (crash-safe proof)

Command:
```powershell
python tools/analysis/exp0017_artifact_integrity_check.py `
  --run_dir logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz `
  --hash
```

Observed:
- `ok: true`
- exit_code: `0`

### 3.3 Progress Policy Eval

Command (stdout captured JSON):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0149_live_45m_viz `
  --require_integrity `
  --dataset_root $root `
  --require_sanity
```

Observed:
- verdict: `PASS`
- exit_code: `0`
- launcher log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T171222Z_task0151_policy_eval_task0149.log`

## 4) Metrics (from metrics.json)

From `logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz/metrics.json`:
- final_step: `30827`
- val:
  - masked_accuracy: `0.4811008153250761`
  - masked_correct: `57060`
  - masked_total: `118603`
  - masked_loss: `3.5860769201203277`
- test:
  - masked_accuracy: `0.4637265515179913`
  - masked_correct: `57401`
  - masked_total: `123782`
  - masked_loss: `3.7288462154136153`
- baselines:
  - baseline_shuffled_val.masked_accuracy: `0.027646855475831133`
  - baseline_random_val.masked_accuracy: `0.00009274638921443809`
- verdict_kc_sanity: `PASS`

## 5) Crash-Safe Artifacts (presence + sha256)

From artifact integrity output (sha256):
- `RUN_METADATA.json`: `89da49c59aa41b4bed42ce807698ffe4fdc27a3bde4243a128d0bfbb9700595a`
- `RUN_STATUS.json`: `ad8d34305d9c6d5fd8896df6019f006c22e596001edc33741e078149d1db233b`
- `metrics_by_step.jsonl`: `35ae3881d410dfbc6d4274c3106feb6d349bdbdd56bc49819268fd68721739f9`
- `metrics.json`: `7dc5110749e12971c1cc1be191fc18c4db333f1f8df5beeca032b0485ce42985`

RUN_START line (from `metrics_by_step.jsonl` head):
```json
{"device": "cuda", "event": "RUN_START", "git_head": "4c913b3e22eaa840f7d95e9695feecd9ea99749b", "run_tag": "task0149_live_45m_viz", "step": 0, "ts_utc": "2026-02-09T16:10:52Z"}
```

## 6) Policy Sidecar (optional; written post-run; atomic)

Command (idempotent):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python tools/analysis/exp0017_write_policy_sidecar.py `
  --run_dir logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz `
  --dataset_root $root `
  --require_integrity `
  --require_sanity
```

Observed:
- created: `logs/exp_0017_comprehension_v0_cloze/run_20260209T161052Z_4c913b3_task0149_live_45m_viz/policy_eval.json`
- policy sidecar sha256: `48e05f3ec327c775aa5b18575ebc362a90e5e24bc0896278f1b4ec7f364e5bec`
- exit_code: `0`, quaternary_state: `YES`, verdict: `PASS`

## 7) Viz Pipeline Evidence (snapshots + localhost serving)

Snapshot root:
- `ui/pacman_viz/_snapshots/task0149_live_45m_viz` (gitignored runtime artifacts)

Observed (L0):
- snapshot_count: `61`
- `LATEST.json` sha256: `031d4b5bfca50f7da35ba53d74ba55e84a0afd3a939a5059edf0cd2fe4ba8c7b`
- last snapshot: `snapshot_20260209T171149Z.json`
  - sha256: `031d4b5bfca50f7da35ba53d74ba55e84a0afd3a939a5059edf0cd2fe4ba8c7b`

LATEST.json key fields:
- ts_utc: `2026-02-09T17:11:49Z`
- step: `30827`
- data_status: `complete`
- quat_source: `policy_eval`
- quat_state: `YES`

Localhost server proof (loopback-only):
- `curl http://127.0.0.1:8848/LATEST.json` => `HTTP 200`, `Cache-Control: no-store`
- `netstat` shows `127.0.0.1:8848 LISTENING`

## 8) Risks / Notes (L0)

- `RUN_METADATA.json.run_tag` is `null` for this run; run_tag is present in `RUN_STATUS.json` and `metrics_by_step.jsonl` RUN_START line.
- Policy sidecar was not present during the run; it was written post-run for viz “quat_source=policy_eval” proof.

