# ADR-0015: Applied Fairness Two-Level Governance (EXP-0700 v4)

- **Date:** 2026-03-05
- **Status:** ACCEPTED
- **Type:** R2 governance update (applied track only)
- **Related:** ADR-0013, ADR-0014, TASK-2120

## Context

Applied diagnostic v3 confirmed:
- GPU runtime stability is restored (`stability_fail_rate = 0.0`).
- GPU gate still fails by CI (`ci95_low(delta_gpu) <= 0`).
- Root cause is between-seed/protocol sensitivity, not nondeterminism (`within-seed variance = 0`, TASK-2110/TASK-2120).

Existing protocol audit (`TASK-2112`) treated `lr_scaled_with_batch` as a hard blocker. This blocks empirically stable profiles that satisfy task-level comparability and manifest traceability.

## Decision

Adopt **two-level fairness governance** for applied track reruns.

### Level 1: Hard fairness (blocking)

These checks are mandatory:
1. Dataset parity: same `dataset_root` and dataset artifact hash in manifest.
2. Architecture parity: same model family/structural params for compared runs.
3. Objective parity: same metric and direction (`delta_gpu = loss_baseline - loss_optimized`).
4. Seed policy parity: same seed list/range between compared arms.
5. Budget parity: **token/examples parity** (not LR heuristic).
6. Device integrity: no hidden fallback (`requested_device=cuda` must resolve to `cuda:*` for GPU pilot).
7. Manifest completeness: row-level run index + per-run manifest with command/flags/hashes.

### Level 2: Advisory checks (non-blocking)

These are recorded and audited but do not block runs by themselves:
- `lr_scaled_with_batch`
- AMP mode selection
- Clip/scaler tuning choices

## Pre-Registered GPU Profile Space (v4)

Baseline profile:
- `gpu_baseline_fp32_bs12_steps80_lr3e5`

Allowed optimized profiles:
- `gpu_opt_amp_bs8_steps120_lr3e5_fp32crit_clip1`
- `gpu_opt_amp_bs8_steps120_lr2e5_fp32crit_clip08`

Selection rule (if multiple profiles are evaluated):
1. Keep only profiles with `stability_fail_rate <= 0.10`.
2. Choose profile with maximal `ci95_low(delta_gpu)`.
3. Tie-break by maximal `mean_delta`.

## What Does Not Change

- ADR-0013 thresholds and PASS/FAIL logic are unchanged.
- No post-hoc threshold tuning is allowed.
- Phase 4 scientific verdict remains unchanged (`RUN COMPLETE / GATE FAIL`).

## Consequences

- Removes a methodological blocker (hard LR-scaling gate) while preserving strict reproducibility and comparability.
- Keeps fairness enforceable via hard contract fields (data/arch/objective/seeds/budget/device/manifest).

## Rollback

- `git revert <commit-hash-containing-ADR-0015>`
