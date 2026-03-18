# BDC R1 Full Sweep Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_R1_FULL_SWEEP`
- Scientific phase: `R1 - Selection Physics Rebuild`
- Date: `2026-03-19`
- Owner: `BDC / CODEX`

## Hypothesis
- Primary hypothesis:
  - At least one bounded non-legacy selection regime can remain mathematically feasible for architectural growth, avoid immediate collapse, preserve non-zero selective pressure, and therefore justify progression from `R1` to `R2`.
- Secondary hypothesis:
  - The legacy control remains a valid comparator, but should not remain the only structurally feasible regime if the reboot is to continue honestly.
- Out-of-scope hypotheses:
  - organism assembly,
  - cell-level composition,
  - SuperCell claims,
  - environment design for `R2`,
  - product claims about digital life.

## Decision Gate
- What decision must this cycle support?
  - Whether canonical `Phase R1` should return `PASS_TO_R2` or `REMAIN_IN_R1`.
- What decision is explicitly not being made?
  - It does not decide any organism-level claim, biological realism claim, or `R2` design beyond permission to enter `R2`.

## Evidence State
- Measured evidence:
  - Historical `TASK-1400B` evidence showed the old complexity regime could make non-legacy architectural growth mathematically impossible.
  - `TASK-7591` implemented explicit bounded regime families on top of the legacy symbolic stack.
  - `TASK-7592` established a reproducible manifest-driven sweep runner.
  - `TASK-7593` established a bounded aggregate gate audit that yields only `PASS_TO_R2` or `REMAIN_IN_R1`.
- Historical prior evidence:
  - Legacy complexity physics previously punished complexity so strongly that `v2*` growth could not honestly beat the `v1` baseline under the old regime.
- Inferred evidence:
  - Bounded non-linear regimes should be the first honest place to look before reopening any richer scientific line.
- Missing evidence:
  - Full canonical multi-seed `R1` sweep across all six required regime families.
  - Multi-seed collapse/feasibility behavior under the exact manifest, not just a smoke run.
- Contradicted evidence:
  - No contradiction has yet invalidated the reboot package itself, but the old line already contradicted the sufficiency of the legacy penalty physics.

## False Directions To Exclude
- Do not treat the smoke run as a scientific verdict for full `R1`.
- Do not tune thresholds post-hoc after seeing a subset of `R1` results.
- Do not expand scope into organism assembly, cell abstractions, or `R2` environment work before the formal `R1` gate verdict exists.

## Minimal Execution Scope
- Smallest valid cycle:
  - Run the canonical manifest exactly as declared and aggregate into the bounded two-way gate packet.
- Allowed implementation surface:
  - Existing `edp1_symbolic` runtime, canonical manifest, canonical runner, canonical aggregator, and append-only reporting.
- Forbidden scope expansion:
  - changing regime families,
  - changing seed policy,
  - changing gate semantics,
  - changing pass/fail criteria after execution starts.

## Required Measurements
- Required metric 1:
  - `required_accuracy_to_beat_legacy` and resulting `feasible_growth`
- Required metric 2:
  - `collapse_rate` and `runtime_pass_rate`
- Required metric 3:
  - `trivial_strategy_rate`, `mean_penalty`, `diversity_index_final`, and `functional_diversity_final`

## Verdict Contract
- PASS means:
  - At least one non-legacy regime is feasible for growth, avoids immediate empirical collapse under bounded multi-seed testing, preserves non-zero selective pressure, and does not win only by removing all constraints.
- FAIL means:
  - The execution toolchain or artifact contract breaks such that the cycle cannot produce a valid bounded gate packet.
- REMAIN_IN_PHASE means:
  - The toolchain ran correctly, but no non-legacy regime met the bounded progression conditions required to justify `R2`.

## BDC Designer Output Attached
- Evidence-state summary:
  - Experimental synthetic packet run over the `R1` smoke outputs.
- Measurement-gap note:
  - Full multi-seed evidence remains missing until the canonical long run is executed.
- Narrowing memo:
  - This document.
- Decision-gate memo:
  - Final aggregate packet from `scripts/edp1/aggregate_selection_physics_reboot.py`.

## Canonical Attachments
- Manifest:
  - `scripts/edp1/selection_physics_manifest.json`
- Runner:
  - `scripts/edp1/run_selection_physics_reboot_sweep.py`
- Aggregator:
  - `scripts/edp1/aggregate_selection_physics_reboot.py`
- Implementation package:
  - `docs/experiments/EXP-0801_SELECTION_PHYSICS_REBOOT_IMPLEMENTATION_PACKAGE.md`
- Launch prep:
  - `scripts/edp1/run_selection_physics_reboot_parallel.ps1`
  - `reports/analysis/TASK-7594-BDC-SELECTION-PHYSICS-R1-LAUNCH-PREP/PROCESS_SNAPSHOT_2026-03-18.md`

## Integrity Note
The smoke run used for artifact validation is a tooling and preservation check only.

It is permitted to validate:
- artifact creation,
- manifest discipline,
- run indexing,
- aggregate packet generation,
- and experimental `BDC Designer` intake compatibility.

It is not permitted to claim:
- that `R1` has scientifically passed,
- that `R2` is authorized,
- or that the reboot hypothesis has already been validated.
