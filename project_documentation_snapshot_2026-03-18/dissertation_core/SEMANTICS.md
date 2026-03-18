## Semantics (S and conflict_flag)

This is the single source of truth for value semantics.

## Value set
S = {T, F, MY, MN}

Definitions:
- T: confirmed true (sufficient evidence).
- F: confirmed false.
- MY: directed uncertainty toward "Yes" (evidence exists but insufficient).
- MN: directed uncertainty toward "No" (evidence exists but insufficient).

## conflict_flag
conflict_flag is a separate meta-bit returned by qcore alongside S:
- conflict_flag = 1 when contradictory evidence is detected.
- conflict_flag MUST NOT be silently collapsed into T/F.

Every qcore step returns:
- value in S
- conflict_flag in {0,1}

