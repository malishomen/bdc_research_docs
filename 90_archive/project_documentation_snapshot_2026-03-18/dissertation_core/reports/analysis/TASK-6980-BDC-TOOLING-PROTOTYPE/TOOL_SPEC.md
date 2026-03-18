# TOOL_SPEC (TASK-6980)

## Purpose
Provide practical architecture recommendations from task descriptors using restricted BDC priors.

## Inputs
- task-family descriptor
- causal asymmetry (0..1)
- DAG depth and branching
- budget tier

## Outputs
- recommended effective role count
- equilibrium-style role weights (predictor/critic/aggregator)
- strategy mode (`standalone_bdc_prior`, `bdc_warm_start`, `bdc_pruning`, `full_hybrid_search`)
- confidence score and caution flags

## Rules
1. Use family-specific rulebook strategy as default.
2. Prefer pruning for hard-failure families under budget pressure.
3. Emit caution flags for high asymmetry/depth and known hard-failure families.
4. Fall back to full hybrid with low confidence for unknown families.
