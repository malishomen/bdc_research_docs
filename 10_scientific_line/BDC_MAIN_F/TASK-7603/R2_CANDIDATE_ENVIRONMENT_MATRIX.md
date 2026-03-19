# R2 Candidate Environment Matrix

## Purpose

This document defines the bounded candidate comparison surface for `R2`.

It does not approve an environment.
It defines how candidate environments should be read before baseline/measurement harness work begins.

## Comparison dimensions

1. `determinism`
2. `causal_interpretability`
3. `mechanism_pressure`
4. `baseline_readiness`
5. `trivial_strategy_exposure`
6. `distance_from_hidden_rule`
7. `scope_safety`

## Candidates

### 1. Controlled Sequence Memory
- Primary pressure: memory
- Strength:
  - strongest deterministic control
  - easiest causal inspection
  - cleanest baseline design
- Risk:
  - may stay too toy-like if sequence design is too weak
- Current interpretation:
  - best conservative starting candidate

### 2. Controlled Uncertainty Abstention
- Primary pressure: uncertainty handling
- Strength:
  - strongest alignment with quaternary/abstention line
  - explicit abstain-vs-error tradeoff possible
- Risk:
  - ambiguity construction can become too design-heavy if not formalized tightly
- Current interpretation:
  - strongest direct uncertainty candidate

### 3. Micro-Corpus Cloze
- Primary pressure: bounded language context
- Strength:
  - richest bridge beyond `hidden_rule`
  - closest to future information-task relevance
- Risk:
  - easiest candidate to let drift into premature language complexity
- Current interpretation:
  - richest but riskiest candidate

## Current matrix conclusion

At the matrix-only stage:
- `controlled_sequence_memory` is the safest conservative starting point
- `controlled_uncertainty_abstention` is the strongest uncertainty-aligned candidate
- `micro_corpus_cloze` is the most ambitious candidate and therefore needs the strictest baseline discipline

## What this matrix does not do

It does not:
- choose the final canonical R2 environment,
- authorize implementation-first work,
- override the later `APPROVE_R2_ENVIRONMENT` vs `REMAIN_IN_R2` gate.
