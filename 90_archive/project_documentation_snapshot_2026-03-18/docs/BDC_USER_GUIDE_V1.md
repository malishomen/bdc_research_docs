# BDC User Guide v1

## What BDC Designer Is
BDC Designer CLI is a restricted architecture-prior and strategy-selection assistant for cooperative AI workflow design.

## What It Does and Does Not Do
It provides role-count, role-weight, strategy mode, confidence, and caution guidance from task descriptors.
It does **not** claim universal optimization or universal transition-law guarantees.

## When to Use
- You have clear workflow descriptors and architecture choices materially affect cost/quality.
- You need a fast prior before running heavier hybrid refinement.

## When Not to Use
- You have no measurable baseline.
- You need universal guarantees across unknown task classes.
- You cannot tolerate explicit caution flags or scope limits.

## Required Inputs
- task family descriptor
- causal asymmetry metric
- DAG depth and branching
- budget tier (`low`, `medium`, `high`)

## CLI Usage Patterns
Use single-case mode for fast recommendation and batch JSON mode for repeatable scenario sweeps.

### Command Examples
- `python tools/bdc_designer_cli.py --task_family predictor_dominant --causal_asymmetry 0.75 --dag_depth 3 --dag_branching 2 --budget_tier medium --pretty`
- `python tools/bdc_designer_cli.py --input_json examples/bdc_designer_cli_examples.json --pretty`
- `python tools/bdc_designer_cli.py --task_family planner_augmented --causal_asymmetry 0.58 --dag_depth 6 --dag_branching 4 --budget_tier high --out_json results/tmp_bdc_designer_single.json`
- `python scripts/analysis/run_phase26_bdc_designer_cli.py --cli_script tools/bdc_designer_cli.py --examples_json examples/bdc_designer_cli_examples.json --prototype_csv results/bdc_tool_prototype/tool_decision_examples.csv --out_root results/bdc_designer_cli`

## Input JSON Schema
Each object must include:
`task_family`, `causal_asymmetry`, `dag_depth`, `dag_branching`, `budget_tier`.

## How to Read Outputs
`recommendation.effective_role_count` gives target role count.
`recommendation.role_weights` gives equilibrium-style prior weights.
`recommendation.strategy_mode` defines next design mode.
`caution_flags` highlights risk factors requiring operator judgment.

## Strategy Modes Explained
- `standalone_bdc_prior`: direct prior recommendation without search.
- `bdc_warm_start`: prior as initialization for downstream process.
- `bdc_pruning`: constrained search under tighter budget/risk.
- `full_hybrid_search`: recommended robust mode for higher-impact cases.

## Caution Flags Explained
- `hard_failure_family`: family historically unstable under naive setup.
- `high_causal_asymmetry`: high imbalance in causal contribution.
- `deep_dag`: deeper workflow graph, higher coordination risk.
- `invalid_strategy_mode`: protective flag for invalid strategy outputs.

## Worked Examples
At least three practical scenarios:
- `s1`: family=`predictor_dominant`, asymmetry=`0.75`, depth=`3`, branching=`2`, budget=`medium`
- `s2`: family=`critic_dominant`, asymmetry=`0.7`, depth=`4`, branching=`2`, budget=`medium`
- `s3`: family=`aggregator_dominant`, asymmetry=`0.65`, depth=`5`, branching=`3`, budget=`high`

## Flagship Case Walkthrough
Reference case: planner-executor-checker deployment with BDC-guided hybrid refinement.
Excerpt:
# Flagship Case Study: Real Deployment with Restricted BDC v1

## Executive Summary
This case demonstrates end-to-end deployment design using Restricted BDC v1 from task descriptors to architecture recommendation, hybrid refinement, and outcome comparison. The selected case (`planner-executor-checker`) shows measurable gains over baseline on quality, delivery speed, and search efficiency.

## 1) Case Selection
Candidate workflows were scored on four fixed criteria:
- descriptor clarity,
- measurable baseline availability,
- architecture sensitivity,
- public-safe documentation feasibility.

Selected case: `case_02` (`planner-executor-checker workflow`) with selection score `0.963`.

## 2) Baseline Freeze (D1)
Baseline architecture: existing intuitive workflow without BDC guidance.

Frozen baseline metrics:
- Implementation time: `52.0h`
- Time-to-target: `36.0h`
- Final quality: `0.701`

## Common Mistakes
- Treating confidence as certainty instead of conditional guidance.
- Ignoring caution flags in high-impact workflows.
- Using unknown families without follow-up validation.
- Claiming universal behavior from restricted outputs.

## Limitations and Scope
Restricted BDC v1 claims are bounded. Negative results (including no portable transition-law claim) are explicit.
Scope statement excerpt:
# Restricted BDC v1: Public Scope Statement

## What This Release Claims
Restricted BDC v1 is a bounded framework for causal-equilibrium architecture priors and hybrid cooperative design guidance.
- equilibrium law for role-weight priors
- causal architecture synthesis by task geometry
- hybrid engineering utility of BDC priors

## Explicit Negative Results (Included by Design)
This release explicitly includes negative findings (4 frozen negative claims).
- no portable universal transition law
- no sufficient standalone regime meta-law
- no sufficient hidden-state rescue for portability
- no standalone engineering dominance

## What This Release Does Not Claim
- It does not claim a universal

## FAQ
- **Is BDC Designer a universal optimizer?**
  - No. It is a restricted architecture-prior and hybrid design guidance tool.
- **Can I ignore caution flags?**
  - No. Caution flags indicate elevated design risk and should trigger review.
- **What if my task family is unknown?**
  - Use the recommendation as low-confidence prior and run additional validation.
- **What is the default robust mode?**
  - Typically full hybrid search for higher-impact workflows.
- **How many worked examples are provided?**
  - At least three CLI-ready worked examples plus a flagship case walkthrough.
