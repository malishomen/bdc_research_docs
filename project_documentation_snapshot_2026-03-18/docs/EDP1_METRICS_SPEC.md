# EDP1 Metrics Spec

## Scope
This document defines canonical metric names and aggregation semantics for EDP1 symbolic evolution outputs.

## Runtime metrics.csv (per generation)
Required columns:
- `mean_accuracy`: population mean of per-genome accuracy on the run dataset.
- `max_accuracy`: maximum per-genome accuracy in the population.
- `mean_fitness`: population mean of `fitness`.
- `max_fitness`: maximum `fitness` in the population.

Decomposition columns (if emitted):
- `mean_complexity`: population mean of genome complexity.
- `max_complexity`: maximum genome complexity.
- `mean_penalty`: population mean of `complexity_lambda * complexity`.
- `max_penalty`: maximum `complexity_lambda * complexity`.

## Fitness definition
For each genome:
- `fitness = accuracy - penalty`
- `penalty = complexity_lambda * complexity`

## Aggregation semantics (scripts/edp1/aggregate_results.py)
- `*_mean` in trajectory files means mean over seeds at generation `g`.
- `final_*` in `metrics_agg.csv` means value from last available generation in each seed run, then aggregated over seeds.
- `final_max_accuracy_mean` aggregates `final max_accuracy` values over seeds.
- `final_mean_accuracy_mean` aggregates `final mean_accuracy` values over seeds.
- `final_max_fitness_mean` aggregates `final max_fitness` values over seeds.

## Integrity rules
- Aggregator must fail if required accuracy columns are missing (`max_accuracy`, `mean_accuracy`).
- Aggregator must never substitute `mean_accuracy` in place of `max_accuracy`.
- If decomposition columns are absent in historical runs, decomposition aggregates are emitted as `NaN`/`UNVERIFIED` and must be treated as unavailable.
