# TASK-0139 BRIEF REPORT — comprehension metric v0 (cloze) on simplified_wiki_v0: deterministic masking + GPU/CPU training harness + sanity + repro

Branch/HEAD (start): `test` @ `b3418ee8f1ec94e87597441f5c119abbfcbcb758`

## What Changed (In Git)

- Spec: `docs/spec/COMPREHENSION_V0_CLOZE.md`
- Experiment scaffold:
  - `experiments/exp_0017_comprehension_v0_cloze/SPEC.md`
  - `experiments/exp_0017_comprehension_v0_cloze/RUN_COMMANDS.md`
- Implementation:
  - `experiments/exp_0017_comprehension_v0_cloze/src/data.py` (tokenization + deterministic masking)
  - `experiments/exp_0017_comprehension_v0_cloze/src/train.py` (train+eval+baselines; RUN_METADATA)
  - `experiments/exp_0017_comprehension_v0_cloze/src/eval.py` (integrity + baselines)
- Monitoring: `reports/analysis/TASK_0139_MONITORING_COMMANDS.md`

## Environment (Training Machine)

- torch: `2.5.1+cu121`
- CUDA available: `True`
- GPU: `NVIDIA GeForce GTX 1080 Ti`

## Dataset Integrity (Kill-Criteria: KC_DATA_INTEGRITY)

External dataset root:
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Pinned docs.jsonl sha256 (from `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`):
- expected: `dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687`
- actual:   `dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687`

Result: **PASS** (training allowed).

## Runs (Outputs External-Only; Not In Git)

Run outputs are under repo `logs/` (gitignored):
- smoke1: `logs/exp_0017_comprehension_v0_cloze/run_20260208T200428Z_b3418ee_smoke1`
- repro2: `logs/exp_0017_comprehension_v0_cloze/run_20260208T200614Z_b3418ee_repro2`
- main:   `logs/exp_0017_comprehension_v0_cloze/run_20260208T200756Z_b3418ee_main`

Each run dir contains:
- `RUN_METADATA.json` (git head, seed, device, dataset root, tokenizer/masking, hyperparams)
- `metrics.json` (final val/test + baselines + sanity verdict)
- `metrics_by_step.jsonl` (periodic eval snapshots)

## Metric Results (Masked Accuracy)

Baselines on val (no learning; deterministic):
- shuffled baseline val_acc: `0.0276468555`
- random baseline val_acc: `0.0000927464`

Smoke (max_docs=2000, max_steps=200, seed=12345):
- model val_acc: `0.0570390294`
- model test_acc: `0.0564460099`
- KC_SANITY (shuffled >= model?): **PASS** (0.0276 < 0.0570)

Main (max_steps=2000, seed=12345):
- model val_acc: `0.1175855585`
- model test_acc: `0.1131182240`
- KC_SANITY: **PASS**

## Reproducibility (Kill-Criteria: KC_REPRO)

Smoke repeat (`smoke1` vs `repro2`) val accuracy drift:
- `abs(0.0570390294 - 0.0570390294) = 0.0` (<= 0.005 required)

Result: **PASS**.

## Stability (Kill-Criteria: KC_STABILITY)

- No NaN/inf loss observed in training runs.

Result: **PASS**.

## Monitoring

Commands: `reports/analysis/TASK_0139_MONITORING_COMMANDS.md`

## Explicitly Not Committed

- No dataset outputs, checkpoints, or large logs committed.

## Next Step

- Define TASK-0140+ policy: what accuracy threshold counts as "improvement" and how to extend beyond v0 (richer tokenizer, stronger model, and long-run training under governance).

