# Comprehension v0 Progress Policy — Thresholds + CI + Repro Gates (exp_0017)

## Scope

This policy governs **how to declare success/failure** for `exp_0017_comprehension_v0_cloze` runs on the pinned `simplified_wiki_v0` dataset.

Non-negotiables:
- dataset/build chain unchanged (use pinned `full_build`)
- cloze task unchanged (masking/tokenization/metric as defined in `docs/spec/COMPREHENSION_V0_CLOZE.md`)
- CPU-authoritative PASS/FAIL decision; GPU is compute-only

## Inputs Required For Any Decision

1. Dataset integrity gate:
   - `docs.jsonl` sha256 must match `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json full_build.outputs.docs.jsonl.sha256`.
2. Run metadata:
   - git HEAD, seed, device, tokenizer, masking parameters recorded in `RUN_METADATA.json`.
3. Metrics:
   - `metrics.json` must include `val.masked_accuracy`, `val.masked_total`, `val.masked_correct`
   - same for `test`
   - baselines: `baseline_shuffled_val.*` and `baseline_random_val.*`

If any required field is missing => ERROR (no verdict).

## Primary Metric

- `val_acc = val.masked_accuracy`
- `test_acc = test.masked_accuracy`

## Baseline Sanity (KC_SANITY)

Compute shuffled baseline on val:
- `shuf_val_acc = baseline_shuffled_val.masked_accuracy`

Hard gate:
- require `val_acc >= shuf_val_acc + M_sanity`

Pinned:
- `M_sanity = 0.02` absolute

Rationale: requires a non-trivial margin above an in-distribution "shuffle" baseline.

## Improvement vs Reference (KC_IMPROVEMENT)

Reference: TASK-0139 main run (as recorded in `reports/analysis/TASK_0139_BRIEF_REPORT.md`):
- `ref_val_acc = 0.1175855585`
- `ref_test_acc = 0.1131182240`

Define success as meeting at least one:
1. Absolute improvement threshold:
   - `val_acc - ref_val_acc >= 0.02`
2. CI-separated improvement:
   - Wilson 95% CI for accuracy on masked positions shows **lower bound** of new run > **upper bound** of reference.

Pinned:
- CI method: Wilson score interval (95%)

## Reproducibility (KC_REPRO)

Two governed replicates (`run1`, `run2`) with identical config and seed must satisfy:
- `abs(run1.val_acc - run2.val_acc) <= D_repro`

Pinned:
- `D_repro = 0.01` absolute

Rationale: allows small nondeterminism from hardware/runtime while still catching drift.

## Stability (KC_STABILITY)

Hard gate:
- training must not diverge: no NaN/inf loss observed; process exits cleanly.

## Final Verdict

PASS iff all are true:
- KC_DATA_INTEGRITY PASS
- KC_SANITY PASS (for each run)
- KC_REPRO PASS (between the two runs)
- KC_STABILITY PASS (for each run)
- KC_IMPROVEMENT PASS (for each run, versus reference)

Otherwise FAIL (or ERROR if missing data).

