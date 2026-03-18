# BDC CLI v2 Migration Guide

## v1 to v2
- v1: descriptor-only
- v2: packet-first, evidence-aware, strategy-aware, confidence-aware

## Safe migration path
1. Keep v1 for descriptor-only fallback.
2. Use v2 for real packet or legacy-case inputs.
3. Compare v1 vs v2 on benchmark cases before retiring v1 in any workflow.
