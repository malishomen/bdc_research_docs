# R2 Baseline And Measurement Harness

## Purpose

This document defines the minimum honest measurement contract for `R2` candidate environments.

Without this layer, `R2` would collapse back into narrative environment selection.

## Global rules

1. Every candidate must have deterministic generation proof.
2. Every candidate must have at least 3 explicit baselines.
3. Every candidate must expose trivial strategies explicitly.
4. Every candidate must have named failure modes.
5. No candidate may proceed with undefined metrics.

## Candidate harness requirements

### 1. Controlled Sequence Memory
- Primary metric:
  - `sequence_recall_accuracy`
- Required baselines:
  - `random_symbol_predictor`
  - `always_repeat_last_symbol`
  - `majority_symbol_predictor`
- Key failure risks:
  - sequence shortcut solution
  - memory not actually needed
  - dataset generation drift

### 2. Controlled Uncertainty Abstention
- Primary metric:
  - `utility_weighted_abstention_score`
- Required baselines:
  - `always_decide_no_abstain`
  - `always_abstain`
  - `simple_threshold_heuristic`
- Key failure risks:
  - ambiguity marker leakage
  - abstention reward hacking
  - non-causal ambiguity construction

### 3. Micro-Corpus Cloze
- Primary metric:
  - `bounded_cloze_accuracy`
- Required baselines:
  - `random_token_baseline`
  - `most_frequent_token_baseline`
  - `local_context_frequency_heuristic`
- Key failure risks:
  - lexical shortcut dominance
  - unstable masking rule
  - premature language-complexity drift

## Shared readiness rule

`TASK-7605` is allowed only if:
- all candidates have explicit deterministic generation proof,
- all candidates have at least three named baselines,
- all candidates expose at least three trivial/failure modes,
- and none rely on undefined metrics.

## Current interpretation

At this stage:
- `controlled_sequence_memory` remains the cleanest candidate to measure honestly,
- `controlled_uncertainty_abstention` remains the strongest quaternary-aligned candidate,
- `micro_corpus_cloze` remains the most promising but highest-risk candidate from a metric-discipline standpoint.
