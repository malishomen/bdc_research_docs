# R5 Cloze Transfer Launch Prep

## Canonical Verdict
- `READY_FOR_R5_TRANSFER_LONGRUN`

## Approved Target
- `symbolic_micro_corpus_cloze_transfer`

## What was prepared

- deterministic cloze-transfer smoke artifact:
  - `results/r5_cloze_transfer_launch_prep_smoke`
- canonical long-run manifest:
  - `scripts/analysis/r5_cloze_transfer_longrun_manifest.json`
- executable long-run runner:
  - `scripts/analysis/run_phase68_r5_transfer_launch_prep.py --stage longrun`
- `BDC Designer` launch-readiness packet:
  - `docs/experiments/BDC_R5_TRANSFER_LAUNCH_PREP_PACKET`

## Smoke result

Key measured result from `results/r5_cloze_transfer_launch_prep_smoke/scorecard.json`:
- `candidate_accuracy = 1.0`
- `no_memory_control_accuracy = 0.046875`
- `trivial_last_symbol_memory_accuracy = 0.0`
- `random_symbol_accuracy = 0.046875`
- `deterministic_replay_status = true`

This is not the full long-run result.
It is the measured launch-readiness proof that the approved FIFO mechanism survives the deterministic adjacent cloze surface.

## Canonical long-run surface

- seed count:
  - `30`
- slice count:
  - `4`
- total planned runs:
  - `120`

Slices:
1. `base_cloze_transfer`
2. `gap_extension_cloze_transfer`
3. `lexicon_extension_cloze_transfer`
4. `combined_bounded_cloze_transfer`

## Compute posture

- preferred device:
  - `cpu`
- reason:
  - this `R5` run evaluates a fixed deterministic FIFO mechanism rather than a GPU-native training loop.

## Launch command

When the project is ready to start the full run, the canonical command is:

```powershell
python scripts/analysis/run_phase68_r5_transfer_launch_prep.py --stage longrun --manifest_path scripts/analysis/r5_cloze_transfer_longrun_manifest.json --longrun_out results/r5_cloze_transfer_longrun
```

## Constraint carried forward

The run must:
- keep the same FIFO mechanism family unchanged,
- use the prepared deterministic cloze transfer surface,
- avoid reusing the older cloze evolutionary stack as proof of transfer.
