# BDC Sparse Runtime Evidence

## Purpose
- Preserve sparse current-runtime evidence from client packets without forcing false precision.
- Keep verdict-like metric text, explicit missing values, and aggregate runtime rows machine-readable.
- Prevent contradiction inflation when H5.x-style evidence is partially numeric and partially qualitative.

## Rules
- Raw metric text is preserved in `evidence_annotations.raw_metric_text`.
- Parsed numeric values are emitted only when a numeric component exists.
- Verdict-like cells such as `0% substantial accepted` are preserved as `verdict_like_numeric`.
- Explicit `missing` remains explicit and is counted in sparse-runtime support summaries.
- Aggregate rows like `H5.4_all_tested` are marked as `aggregate_runtime_variant` and are not treated as concrete per-variant coverage.

## Output Contract
- `packet.metadata.sparse_runtime_support_summary`
- `tested_variants[*].metadata.sparse_runtime_annotations`
- `variant_metrics_by_slice[*].evidence_annotations`

## TextAI_Auto Relevance
- H5.x runtime evidence mixes numeric rates, verdict-level phrases, and explicit missing values.
- BDC now preserves those signals during folder intake instead of collapsing them into incomplete numeric-only rows.
- This keeps uncertainty explicit while still allowing recommendation, redesign, and measurement-gap outputs.
