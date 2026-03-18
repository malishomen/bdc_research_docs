# BDC Logical Redesign Mode

## Purpose
Return current-runtime redesign guidance, not only the best historical winner.

## Output contract
Redesign mode must answer:
- what logical split to test first,
- how current runtime components map to BDC roles,
- whether guardian should remain post-edit only,
- which architecture test arm should run next.

## TextAI_Auto target behavior
For `TextAI_Auto`, redesign mode should prefer a 4-role logical redesign around:
- orchestrator
- planner
- editor
- guardian

while explicitly rejecting harmonizer-like overhead as a default next step.
