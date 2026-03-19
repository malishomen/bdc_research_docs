# BDC Redesign Memo

## Case
- System: Cockpit
- Case ID: cockpit_runtime_audit_2026_03_20

## Recommendation
- Winner prior: resume_flow
- Recommended roles: N/A
- Role count: 1
- Strategy mode: full_hybrid_search
- Confidence: medium
- Prior confidence: high
- Deployability confidence: medium

## Logical Redesign
- Recommended split: 3_role_logical_redesign
- Guardian mode: post_edit_validation
- Next test: 3_role_logical_redesign
- Formalize first: planner-like routing and family selection, editor path as explicit execution layer, guardian-like post-edit accept/revert/retry layer, orchestrator lifecycle and bounded iteration control
- Do not add yet: harmonizer_role

## Minimum Additional Measurements
- accepted_rewrite_rate_pct, useful_rewrite_rate_pct, semantic_pass_proxy_pct, revert_rate_pct, runtime_min, cost_usd, useful_output_rate_pct
