# EXP-0801: Selection Physics Reboot Implementation Package

## Status
- Date: 2026-03-18
- Status: ACTIVE IMPLEMENTATION PACKAGE
- Depends on:
  - `docs/experiments/EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md`
  - `docs/project/BDC_RESEARCH_REBOOT_PLAN.md`
  - `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`
  - `docs/BDC_QCORE_BELNAP_ALIGNMENT.md`
  - `docs/BDC_SELECTION_DIVERSITY_POLICY_NOTE.md`
  - `docs/BDC_MEMORY_ERROR_MODEL.md`
  - `docs/BDC_MEMORY_ADDRESSABILITY_NOTE.md`

## Purpose

This package converts `Phase R1 - Selection Physics Rebuild` from a planning artifact into an executable implementation chain.

It does not claim that the reboot is already validated.

It defines the exact bounded work that must be implemented before `Phase R1` can produce a scientific pass/fail verdict.

## Why a new implementation package is required

`EXP-0800` defined the scientific question and the minimum regime families, but it intentionally stopped before code-level task decomposition.

At this point the project has:
- historical evidence of the failure of legacy complexity physics,
- an existing `edp1_symbolic` execution stack,
- and new reboot-line notes on semantics, diversity, and memory discipline.

The missing layer is the execution contract that says:
- what code changes are allowed,
- what outputs must be produced,
- what counts as a valid `Phase R1` sweep,
- and what must be true before the reboot is allowed to move to `R2`.

## Bounded implementation objective

Implement a selection-physics test harness on top of the existing `evolution/edp1_symbolic` stack that can compare:
- legacy control,
- bounded non-linear resource regimes,
- and diagnostic floor/ceiling controls,

without reopening the old line as a product claim or introducing organism-level inflation.

## Execution scope

The implementation package is restricted to four execution gates.

### Gate 1 - Regime abstraction
Add an explicit selection-physics abstraction layer that can represent:
- legacy linear penalty control,
- energy-budget regime,
- maintenance-cost regime,
- resource-allocation regime,
- bounded hybrid regime,
- and explicit diagnostic controls.

This gate is about code structure and metric compatibility, not about claiming a winner.

### Gate 2 - Multi-regime sweep runner
Build a bounded sweep runner that can execute the same task/environment across regime families and seeds under a reproducible manifest.

Minimum contract:
- deterministic seed list,
- explicit run manifest,
- per-run summary artifact,
- aggregated summary artifact,
- no silent dropping of failed regimes.

### Gate 3 - Feasibility and collapse audit
Add a gate evaluator that computes whether a regime is acceptable for reboot continuation.

Minimum required outputs:
- feasibility flag for architectural growth,
- required accuracy to beat legacy baseline,
- collapse rate,
- trivial strategy rate,
- diversity retention indicators,
- runtime pass rate,
- bounded interpretation verdict.

### Gate 4 - R1 decision packet
Produce a final `Phase R1` decision packet that says one of two things:
- `PASS_TO_R2`
- `REMAIN_IN_R1`

No softer rhetorical verdicts are allowed.

## Required implementation sequence

Execution order is strict.

1. `TASK-7591` - regime abstraction layer
2. `TASK-7592` - multi-regime sweep runner and manifest discipline
3. `TASK-7593` - R1 aggregation, gate audit, and decision packet

`TASK-7593` may start only after `TASK-7591` and `TASK-7592` are complete.

## Canonical regime family set for R1

The implementation package must cover at least these regime identifiers.

1. `legacy_linear_control`
2. `energy_budget`
3. `maintenance_cost`
4. `resource_allocation`
5. `bounded_hybrid`
6. `no_penalty_diagnostic`

The package may include additional diagnostics only if they are labeled as diagnostics and do not replace the required family set.

## Existing stack that must be reused

The reboot must reuse the current symbolic execution stack where possible:
- `evolution/edp1_symbolic/evaluate.py`
- `evolution/edp1_symbolic/select.py`
- `evolution/edp1_symbolic/run_generations.py`
- `evolution/edp1_symbolic/tests/test_complexity_regime.py`

This avoids fake novelty and forces the reboot to remain comparable to the historical line.

## What must not happen in implementation

The following are prohibited in this package:
- new organism-level modules,
- new "cell" abstractions,
- narrative claims of biological realism,
- replacing `edp1_symbolic` with an entirely different runtime,
- dropping legacy control from reports,
- redefining success after seeing results.

## Required artifacts

The full R1 execution chain must eventually produce the following artifacts.

### Code artifacts
- selection-physics abstraction module(s)
- reproducible sweep runner script(s)
- aggregation / gate-audit script(s)
- regression tests

### Results artifacts
- run manifest
- per-regime aggregate summary
- final R1 gate summary
- explicit pass/fail packet

### Governance artifacts
- task brief reports
- append-only log entries
- an experiment report under `reports/analysis/`

## R1 metrics contract

Every implemented regime must report, at minimum:
- `regime_id`
- `seed`
- `genome_version`
- `population`
- `generations`
- `feasible_growth`
- `required_accuracy_to_beat_legacy`
- `final_max_fitness`
- `final_max_accuracy`
- `final_mean_complexity_or_load`
- `collapse_status`
- `collapse_reason`
- `trivial_strategy_rate`
- `diversity_index_final`
- `functional_diversity_final`
- `runtime_pass`

## R1 Definition of Done

The implementation package is complete only if:

1. the regime family abstraction exists in code,
2. the sweep runner can execute the required family set reproducibly,
3. the aggregation logic computes the required gate metrics,
4. the final packet yields an explicit `PASS_TO_R2` or `REMAIN_IN_R1`,
5. no forbidden scope expansion occurred.

## Acceptance criteria for progression to R2

`Phase R1` may authorize `R2` only if at least one non-legacy regime:
- is mathematically feasible for architectural growth,
- avoids immediate empirical collapse under bounded multi-seed testing,
- preserves non-zero pressure on complexity/resource use,
- and does not win only by removing all constraints.

If no regime satisfies those conditions, the only valid verdict is `REMAIN_IN_R1`.

## Failure conditions

The package is considered failed if any of the following occur:
- the runner cannot compare regimes on a shared manifest,
- reports omit the legacy control,
- aggregation cannot distinguish collapse from non-collapse,
- a regime is declared acceptable without explicit feasibility evidence,
- the implementation drifts into organism assembly work.

## Immediate next step after this package

The next correct action after this package is not free-form coding.

It is to execute the task chain in order:
- `TASK-7591`
- `TASK-7592`
- `TASK-7593`

Only then can the project claim that `Phase R1` is under active execution rather than still being discussed.
