# TASK-0145 — TASK-0144 L0 One-Pager (Inputs → Gates → Metrics → Conclusion → Risks)

Scope: L0 audit + reproducibility hardening only. No changes to exp_0017 training semantics or metrics.

## 1) Identity

- branch: `test`
- git_head_run (from run artifacts): `9708fecb84eccc9b2418a1e26820945bbc2a0cc5`
- git_head_doc (repo HEAD at time of this one-pager creation): `5217fc66c4db946920c6ef9a6d7ca9a11efe1f5c`
- run_tag: `task0144_quality_2h_io`
- run_dir (gitignored): `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io`
- dataset_root (external-only): `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Note (L0): `RUN_METADATA.json.git_head` can differ from `git_head_doc` if the report is written after the run finishes.

## 2) Inputs (L0)

From `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io/RUN_METADATA.json`:
- seed: `12345`
- device: `cuda`
- torch: `2.5.1+cu121`
- torch_cuda_available: `true`
- torch_cuda_device_name: `NVIDIA GeForce GTX 1080 Ti`
- tokenizer: `whitespace_hash` (vocab_size=8192; pad_id=0; mask_id=1)
- masking:
  - mask_rate: `0.15`
  - mask_span_max: `3`
  - mask_salt: `comprehension_v0_cloze_mask_v1`
- training (IO knobs are recorded under `training`):
  - batch_size: `32`
  - eval_every: `1000`
  - eval_max_docs: `2000`
  - max_docs: `null`
  - num_workers: `4`
  - pin_memory: `true`
  - prefetch_factor: `2`
  - persistent_workers: `true`

Dataset integrity expectation:
- Verified via integrity gate (see Gates section). Dataset file itself is external-only and not committed.

Proof snippet (L0; artifact-derived values):
- `RUN_METADATA.json.git_head`: `9708fecb84eccc9b2418a1e26820945bbc2a0cc5`
- `metrics.json.final_step`: `91001`

## 3) Gates (L0)

### 3.1 KC_DATA_INTEGRITY (dataset sha256)

Pre-run check (repro command):
```powershell
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build
```
Result (L0): `KC_DATA_INTEGRITY: PASS` (expected sha256 == actual sha256 for `docs.jsonl`).

### 3.2 Crash-safe artifacts present (P0 regression guard)

Repro command:
```powershell
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io --hash
```
Result (L0): PASS (exit code 0). Required artifacts present:
- `RUN_METADATA.json`
- `RUN_STATUS.json`
- `metrics_by_step.jsonl` (starts with `RUN_START`)
- `metrics.json` (terminal artifact)

SHA256 (from integrity tool output):
- `RUN_METADATA.json`: `050c14d81259d5457bb5cdff36cab247bda7b3ff4d805751873beb605884e053`
- `RUN_STATUS.json`: `5d62ce6228cde6b1a02c3edce6fe88d3ed92d50905c91db5a5ac482c0218d484`
- `metrics_by_step.jsonl`: `12f39ef40212021bb83a6d6d1b9b26093cf203744105d536083df1cc98e86567`
- `metrics.json`: `0354495bd2099596cb1009c3c4cc06e8e080e7a781eaa2cd6762cad77353fc3c`

### 3.3 Policy gates (progress policy evaluator)

Repro command:
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0144_quality_2h_io `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```

Result (L0):
- `exit_code=0`
- `verdict=PASS`
- `repro.skipped=true` (single-run; no replicate provided)
- `metrics_verdict_kc_sanity=PASS` (model > shuffled baseline)
- `problems=[]`

Policy-eval stdout snapshot (captured as JSON):
```json
{
  "exit_code": 0,
  "info": {
    "dataset_integrity": {
      "actual": "dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687",
      "expected": "dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687"
    },
    "policy": {
      "d_repro": 0.01,
      "improve_abs": 0.02,
      "m_sanity": 0.02,
      "ref_val_acc": 0.1175855585,
      "use_ci_improvement": false
    },
    "repro": {
      "reason": "single run (no replicate provided)",
      "skipped": true
    },
    "runs": [
      {
        "baseline_shuffled_val_acc": 0.027646855475831133,
        "git_head": "9708fecb84eccc9b2418a1e26820945bbc2a0cc5",
        "metrics_verdict_kc_sanity": "PASS",
        "run_dir": "logs\\exp_0017_comprehension_v0_cloze\\run_20260209T075959Z_9708fec_task0144_quality_2h_io",
        "seed": 12345,
        "tag": "task0144_quality_2h_io",
        "test": {
          "acc": 0.5134025948845551,
          "k": 63550,
          "n": 123782
        },
        "val": {
          "acc": 0.5346070504118783,
          "k": 63406,
          "n": 118603,
          "wilson95": [
            0.5317671708296339,
            0.5374446881935138
          ]
        }
      }
    ]
  },
  "problems": [],
  "verdict": "PASS"
}
```

## 4) Metrics (L0)

From `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io/metrics.json`:
- final_step: `91001`
- val:
  - masked_accuracy: `0.5346070504118783` (k=`63406`, n=`118603`)
  - masked_loss: `3.0943933426487025`
- test:
  - masked_accuracy: `0.5134025948845551` (k=`63550`, n=`123782`)
  - masked_loss: `3.246902529181848`
- baselines (val):
  - shuffled masked_accuracy: `0.027646855475831133`
  - random masked_accuracy: `0.00009274638921443809`
- verdict_kc_sanity: `PASS`

Completion evidence (stdout; reproduced in launcher log):
- `TIME_BUDGET_REACHED step=91000 budget_minutes=120`

## 5) Timeline (L0, sampled)

From `metrics_by_step.jsonl`:
- RUN_START:
  - ts_utc: `2026-02-09T07:59:59Z`
  - git_head: `9708fecb84eccc9b2418a1e26820945bbc2a0cc5`
  - device: `cuda`
- eval points:
  - count: `91`
  - first eval: step `1000`, val_acc `0.1149465`
  - last eval: step `91000`, val_acc `0.5346071`

Extended excerpts for plateau/noise inspection:
- `reports/analysis/TASK_0144_L0_ARTIFACT_EXCERPTS.md` (tail window + mid-run window + metadata/metrics + launcher head)

## 6) Conclusion (what is proven / not proven)

Proven (L0):
- Dataset integrity gate PASS for the pinned dataset root.
- Crash-safe artifacts are present (RUN_START + RUN_STATUS heartbeat + terminal `metrics.json`) and sha256 pinned.
- Policy-eval verdict PASS (exit 0) with sanity gate PASS and no reported problems.
- IO knobs are traceable (num_workers/pin_memory/prefetch_factor/persistent_workers recorded in RUN_METADATA).

Not proven (explicitly not done here):
- Replicate stability for 2h (KC_REPRO is skipped for single-run policy eval).

## 7) Risks + next hardening steps (no in-place tuning)

- Missing replicate for 2h: run a second 2h replicate with identical config/seed to evaluate drift and satisfy KC_REPRO at the long-run horizon.
- Heavy-eval: current eval uses `eval_max_docs=2000`; if decision is “scale to 6h”, consider a periodic heavier eval (more docs) under an explicit schedule (separate task; may affect wall time, not semantics).
- Metadata gaps: `RUN_METADATA.json` currently has no explicit `model` / `optimizer` sections (only training hyperparams + tokenizer/masking). If needed for audit, add non-semantic metadata-only fields (separate task; should not change training).
