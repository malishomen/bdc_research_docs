# EXP-0803: R2 Controlled Task Environment Implementation Package

## Status
- Date: 2026-03-19
- Status: ACTIVE IMPLEMENTATION PACKAGE
- Depends on:
  - `docs/experiments/EXP-0802_R2_CONTROLLED_TASK_ENVIRONMENT.md`
  - `docs/experiments/BDC_R2_CONTROLLED_TASK_ENVIRONMENT_PREEXPERIMENT_GATE.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`

## Purpose

This package converts the `R2` environment-selection phase into an executable bounded task chain.

It does not pick the environment by intuition.
It defines how the project must compare environment candidates before any downstream implementation work starts.

## Bounded implementation objective

Implement a disciplined `R2` comparison chain that can:
- define candidate environment families,
- define deterministic generation and baseline contracts,
- compare candidates on a shared gate surface,
- and emit one of two outcomes:
  - `APPROVE_R2_ENVIRONMENT`
  - `REMAIN_IN_R2`

## Execution scope

The implementation package is restricted to three gates.

### Gate 1 - Candidate environment matrix
Define and serialize the candidate families, their scientific purpose, and their exclusion boundaries.

### Gate 2 - Baseline and measurement harness
Define the baseline contract, metric definitions, trivial-strategy exposure, and failure registry for every candidate.

### Gate 3 - R2 decision packet
Produce a bounded environment-approval packet that chooses either:
- `APPROVE_R2_ENVIRONMENT`
- `REMAIN_IN_R2`

## Required implementation sequence

1. `TASK-7603` - candidate environment matrix
2. `TASK-7604` - baseline and measurement harness contract
3. `TASK-7605` - R2 gate audit and environment approval packet

## Required candidate family set

At minimum, compare:
1. `controlled_sequence_memory`
2. `controlled_uncertainty_abstention`
3. `micro_corpus_cloze`

Additional families are allowed only if they remain bounded and interpretable.

## Required outputs

### Code / structured artifacts
- candidate matrix JSON or equivalent
- baseline harness spec
- deterministic environment-generation contract
- gate packet

### Governance artifacts
- task brief reports
- append-only log entries
- environment comparison memo

## R2 metrics contract

Every candidate must report, at minimum:
- `environment_id`
- `deterministic_generation_status`
- `baseline_count`
- `trivial_strategy_detectable`
- `mechanism_pressure`
- `causal_interpretability_status`
- `excluded_false_directions`
- `approval_recommendation`

## R2 Definition of Done

The package is complete only if:
1. the candidate family matrix exists,
2. every candidate has explicit baselines,
3. the final gate packet chooses either approval or remain-in-phase,
4. no organism-level scope expansion occurred.

## Acceptance criteria for progression beyond R2

`R2` may authorize downstream implementation only if at least one candidate environment:
- is deterministic,
- is more meaningful than `hidden_rule`,
- remains causally interpretable,
- supports bounded mechanism pressure,
- and has explicit baselines and stop-rules.

## Failure conditions

The package fails if:
- candidate environments cannot be compared on a shared bounded surface,
- baselines are underspecified,
- causal interpretability is not demonstrated,
- or the package drifts into downstream organism work.
