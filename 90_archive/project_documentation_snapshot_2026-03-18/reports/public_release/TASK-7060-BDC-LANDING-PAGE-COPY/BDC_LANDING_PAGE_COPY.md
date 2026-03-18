# BDC Designer: Better Cooperative AI Architecture Decisions

## Build Better Multi-Agent Systems Faster, Without Overclaiming
Restricted BDC v1 helps engineering teams choose role structure, role weights, and search strategy using causal task descriptors and hybrid design guidance.

## What It Does
- Recommends effective role count from task descriptors.
- Proposes equilibrium-style role-weight priors.
- Selects strategy mode (`standalone`, `warm start`, `pruning`, or `full hybrid`).
- Surfaces caution flags before expensive iteration.

## What It Does Not Do
- It does not claim universal optimization.
- It does not guarantee universal dominance across all tasks.
- It does not replace baseline measurement and validation.

## Why Hybrid Beats Naive Design
Naive architecture selection often wastes search budget and increases iteration count.
BDC-guided hybrid design uses informed priors first, then constrained refinement.

## Flagship Case Proof
Real deployment (planner-executor-checker workflow):
- Core wins vs baseline: `3/3`
- Quality improvement: `+0.1026`
- Time-to-target reduction: `11.797h`
- Search-cost change: `-25.52`

## How It Works
1. Describe task family, asymmetry, DAG depth/branching, and budget.
2. Run BDC Designer CLI for role-count, role-weight, strategy, and caution output.
3. Apply recommended mode and validate against frozen baseline.

## Who It Is For
- AI engineering leads
- workflow and systems designers
- product teams operating cooperative AI pipelines
- innovation teams validating architecture strategy quickly

## Calls To Action
- Book an Architecture Audit
- Run a Pilot Engagement
- Request a Demo Pack

## FAQ
**Is this a universal optimizer?**  
No. Restricted BDC v1 is explicitly scope-bounded.

**Can I use this without a baseline?**  
No. Baseline freeze is required for defensible comparisons.

**When should I prefer full hybrid search?**  
High-impact workflows, deeper DAGs, and higher asymmetry settings.

## Claim Safety
This page intentionally separates validated claims from non-claims and includes explicit negative boundaries.
