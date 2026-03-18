# TASK-0123 BRIEF REPORT — fix RUN_METADATA KC1 traceability (H/T + label) + regression test

HEAD (start): `c44d2b3883643a1c4e2a8bd9c59aa04d2f565876`

## What Was Wrong

In TASK-0122 evidence, both V2 and V3 runs wrote `kc1_variant: KC1_TTT_V2` in `RUN_METADATA.md`, even when the effective parameters differed (`--kc1_t 0.075` vs `--kc1_t 0.0725`). This breaks L0 traceability for KC1 gate variants.

## What Changed

- Updated metadata fields in `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`:
  - Added `kc1_variant_label` computed from effective `(kc1_h,kc1_t)`:
    - `(5, 0.075)` => `KC1_TTT_V2`
    - `(5, 0.0725)` => `KC1_TTT_V3`
    - else => `KC1_TTT_CUSTOM`
  - Ensured `RUN_METADATA.md` records:
    - `kc1_h`, `kc1_t`, `kc1_variant_label`
    - `kc1_variant` now reflects the computed label (instead of a hardcoded value).

## How Verified

1. Unit regression test (no evolution runs):
   - `tests/test_exp0015_run_metadata_traceability.py`
   - `pytest -q` => PASS
2. Smoke metadata check (local-only, not committed):
   - Ran `runner.py` twice with seeds=1, gen=1 and different `--kc1_t` values.
   - Observed `RUN_METADATA.md` differs:
     - `kc1_variant_label: KC1_TTT_V2` with `kc1_t: 0.075`
     - `kc1_variant_label: KC1_TTT_V3` with `kc1_t: 0.0725`

## Rollback

- Revert the commit that modifies `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py` and removes `tests/test_exp0015_run_metadata_traceability.py`.
- No experiment semantics or thresholds were changed; rollback is metadata-only.

