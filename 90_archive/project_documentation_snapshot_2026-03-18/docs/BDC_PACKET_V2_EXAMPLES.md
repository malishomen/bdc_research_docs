# BDC Packet V2 Examples

## Purpose
This document freezes the initial `BDC_PACKET_V2` examples used by `TASK-7450`.

## Example 1: Descriptor adapter packet
Source: `descriptor_v1_to_packet_v2`

Use when:
- only v1-style descriptor inputs are available
- no empirical architecture variants exist yet

Expected packet quality:
- `Q1` or `Q2`

Characteristics:
- no tested variants
- inferred candidate roles
- explicit limits and open questions
- suitable for later validator downgrade, not for overconfident recommendation

## Example 2: TextAI_Auto evidence-guided packet
Source: `legacy_packet_to_v2`

Use when:
- a real project packet already contains tested variants and measured outcomes
- the goal is to preserve architecture evidence without flattening it into toy descriptors

Expected packet quality:
- `Q4`

Required preserved facts:
- all tested variants A-E remain present
- variant-level metrics remain attached
- role inflation evidence remains visible
- harmonizer remains representable as a candidate role

## Required fields summary
- `case_id`
- `system_name`
- `task_type`
- `workflow_summary`
- `primary_objective`
- `functional_decomposition`
- `hard_constraints`
- `soft_constraints`
- `candidate_roles`
- `tested_variants`
- `quality_targets`
- `risk_map`

## Source-label rule
Every packet must carry `source_labels` so later layers can distinguish:
- `user_provided`
- `inferred`
- `unknown`

## Quality-level rule
- `Q0`: invalid or unusable
- `Q1`: prior-only packet with minimal structure
- `Q2`: usable structure but weak evidence
- `Q3`: evidence-guided packet with tested variants
- `Q4`: high-quality packet with tested variants and stable metrics
