# BDC Evidence-Status Weighting

## Purpose
Separate best-prior confidence from deployability confidence when packets mix current runtime evidence with historical architecture evidence.

## Current rule
- `measured` evidence receives full weight.
- `measured_from_historical_report` remains strong but discounted.
- `inferred` and `missing` evidence remain weaker.

## Product effect
BDC must be able to say both:
- which prior is strongest;
- how ready that prior is for current-runtime deployment.

## TextAI_Auto target behavior
For `TextAI_Auto`, BDC should preserve `D` as the best architecture prior while downgrading immediate deployability confidence because the winner is historical and the current runtime is still stage-based.
