# BDC LLM Adapter Prompt Contracts

## Boundary
The adapter may:
- interpret raw case text
- draft packet fields
- assign source labels
- ask clarification questions

The adapter may not:
- set final recommended architecture
- set final strategy mode
- set final confidence score

## Determinism rule
CI uses deterministic mocked adapter logic. No network LLM calls are required for baseline validation.
