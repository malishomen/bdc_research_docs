# ADR-0014: Applied GPU Recovery Protocol (Numeric Hardening + Contract V3)

- **Date:** 2026-03-04
- **Status:** ACCEPTED
- **Type:** R2 governance update (applied track only)
- **Supersedes:** none
- **Related:** ADR-0013, TASK-2100..2103

## Context

Applied track diagnostic run (`TASK-2004`, `N=10`) failed on GPU pilot:
- `stability_fail_rate = 0.6`
- dominant crash signature: `softmax probabilities must sum to ~1` (AMP path).

Phase 4 scientific verdict remains unchanged (`RUN COMPLETE / GATE FAIL`) and is out of scope for this ADR.

## Decision

Adopt a controlled GPU recovery package before diagnostic rerun:

1. **Numeric hardening (TASK-2101)**
   - Replace fragile softmax assertion with dtype-aware audit in default path.
   - Add `--strict_numeric_asserts` for legacy strict checks (debug-only).
   - Enforce finite-value guards for logits/probabilities/sums.

2. **Run contract v3 observability (TASK-2102)**
   - Row-level run-index contract with required fields:
     `seed/pilot/variant/return_code/requested_device/resolved_device/fallback_detected/error_signature/manifest_path`.
   - Validator in `replay_from_manifest.py --run_index ...`.

3. **GPU profile calibration selection (TASK-2103)**
   - Selected profile: `opt_amp_bs8` (`--use_amp`, `--batch_size 8`, `--steps 80`, strict asserts OFF).
   - Selection rule is fixed:
     1) keep `stability_fail_rate <= 0.10`;
     2) maximize `mean_delta`.

## What Does NOT Change

- ADR-0013 gate criteria and thresholds are unchanged.
- No post-hoc threshold tuning is allowed.
- Applied track remains parallel and does not rewrite Phase 4 scientific verdict.

## Stop-Rules for TASK-2105 Diagnostic Rerun (N=10)

Immediately stop and do not run gate N=30 if any condition holds:

1. run-index contract validation fails (`run-index-v3` invalid/incomplete).
2. `gpu.verdict_pass == False`.
3. `cpu.verdict_pass == False`.
4. `gpu.stats.stability_fail_rate > 0.10`.
5. Manifest/schema drift or missing mandatory artifacts in rerun output.

## Consequences

- If both pilots pass diagnostic rerun under unchanged ADR-0013 rules, proceed to TASK-2106 (gate N=30).
- Otherwise publish formal applied failure/closure for this iteration (no forced gate execution).

## Rollback

- Revert affected commits from TASK-2101..2103 and return to ADR-0013 baseline applied state.
