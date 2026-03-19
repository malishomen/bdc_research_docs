# BDC Redesign Memo

## Case
- System: Bio_Digital_Core
- Case ID: BDC_R3_SEQUENCE_MEMORY_MECHANISM

## Recommendation
- Winner prior: bounded_working_memory_candidate
- Recommended roles: orchestrator, planner, editor, guardian
- Role count: 4
- Strategy mode: direct_architecture_selection
- Confidence: high
- Prior confidence: high
- Deployability confidence: high

## Logical Redesign
- Recommended split: 4_role_logical_redesign
- Guardian mode: post_edit_validation
- Next test: 4_role_logical_redesign
- Formalize first: planner-like routing and family selection, editor path as explicit execution layer, guardian-like post-edit accept/revert/retry layer, orchestrator lifecycle and bounded iteration control
- Do not add yet: harmonizer_role

## Minimum Additional Measurements
- accepted_rewrite_rate_pct, useful_rewrite_rate_pct, semantic_pass_proxy_pct, revert_rate_pct, runtime_min, cost_usd, useful_output_rate_pct
