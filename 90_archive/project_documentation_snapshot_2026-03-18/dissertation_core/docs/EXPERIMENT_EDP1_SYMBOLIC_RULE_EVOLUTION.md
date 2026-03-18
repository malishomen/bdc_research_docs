# EDP1 Symbolic Rule Evolution (Diversity-First)

## Goal
- Launch Evolution Demonstration Phase 1 (EDP1) as a CPU-only symbolic experiment.
- Validate evolutionary loop discipline before any neural/GPU expansion.

## Scope
- No Hive integration in this task.
- No neural training.
- Deterministic dataset generation with fixed seed.

## Design
- `Phase 0`: mutation-only (no selection) until diversity threshold is reached.
- `Phase 1`: moderate selection (elite + survivor mutation).

## Genome v1
- Interpretable rule parameters:
  - `threshold_count`
  - weights for `count_gate`, `pattern_101`, `first_bit`, `last_bit`, `pos3`, `pos7`
  - `bias`

## Fitness
- `fitness = accuracy - complexity_penalty`
- Complexity is weighted sum of absolute coefficients + threshold term.

## Metrics
- `mean_fitness`, `max_fitness`
- `diversity_index` (unique fingerprints / population)
- `lineage_persistence`
- `rule_entropy`
- `convergence = 1 - diversity_index`
- `trivial_strategy_rate`

## Kill Criteria
- Diversity collapse (`diversity_index` below threshold for N generations).
- Plateau (no `max_fitness` improvement for patience window).
- Trivial strategy dominance (`always-0`/`always-1` frequency above threshold).

## Reproducibility
- Fixed seed for RNG.
- Deterministic task dataset generation.
- No parallel randomness or nondeterministic operators.

