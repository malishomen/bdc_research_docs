# BDC Strategy Explanation Contract v2

## Purpose
This contract defines how `BDC CLI v2` chooses search mode from evidence state.

## Supported strategy modes
- `direct_architecture_selection`
- `direct_architecture_selection_with_tuning`
- `warm_start`
- `bdc_pruning`
- `full_hybrid_search`

## Decision rules
- Strong evidence winner + high-quality packet -> direct architecture selection or direct selection with tuning.
- Weak evidence + low budget -> pruning.
- Weak evidence + usable packet -> warm start.
- Contradictions or unresolved ambiguity -> warm start or full hybrid.
- No strategy decision may be based on family defaults alone.

## Hard TextAI_Auto expectation
For TextAI_Auto, strategy must be:
- `direct_architecture_selection_with_tuning`

Reason:
- strong evidence winner exists
- role inflation failed
- some implementation tuning remains useful
