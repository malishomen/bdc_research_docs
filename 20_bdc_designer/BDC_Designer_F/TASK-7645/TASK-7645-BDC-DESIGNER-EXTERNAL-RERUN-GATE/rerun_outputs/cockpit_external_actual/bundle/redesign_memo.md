# BDC Redesign Memo

## Case
- System: Cockpit
- Case ID: cockpit_runtime_audit_2026_03_20

## Recommendation
- Winner prior: normalized_event_relay
- Recommended roles: orchestrator, editor
- Role count: 2
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
- runtime_min, semantic_pass_pct
