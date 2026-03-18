## ADR-0003: Append-only AGENTS_LOG and WEEKLY_STATUS

Date: 2026-01-24

## Context
`AGENTS_LOG.md` and `WEEKLY_STATUS.md` were updated frequently in both `main` and `test` (and feature branches). Mutable blocks at the head and tail—"Log Created / Last Updated", "SESSION CLOSE", "Неделя отчёта", phase closure blocks—caused repeated merge conflicts when both branches touched the same lines.

## Decision

### AGENTS_LOG.md
- **Append-only:** New entries are added only as new rows at the end of the table. The header and existing rows are not edited.
- **No in-body metadata:** "Log Created", "Last Updated", "Current Date", "Current User" are removed. Use `git log` or the latest table row for recency.
- **Entry Template** is placed at the very end of the file (after the table), fixed. It is not moved or interleaved with rows.
- **SESSION CLOSE** is replaced by a single static line: *"(Current status: see latest table row and WEEKLY_STATUS.md.)"* — no per-session fields to overwrite.
- A **Convention** line at the top states the append-only rule.

### WEEKLY_STATUS.md
- **Append-only:** New content is added only as new `##` sections at the end. Existing `##` sections are not rewritten or removed.
- **Fixed header:** The mutable "Неделя отчёта" block (tasks, branches, risks, agent comments) is removed. The header is a short fixed text plus the Convention.
- **No Phase Closure block at EOF:** Phase closure is written as a subsection inside the phase’s `##` section, not as a separate trailing block.
- A **Convention** line states the append-only rule.

### Merge conflicts
If a conflict still occurs: resolve by keeping both sides’ appends (union of new table rows or new `##` sections). Do not discard one branch’s appended content.

## Consequences
- Fewer merge conflicts, as both branches usually only append and rarely modify the same line.
- Current status is derived from the latest row (AGENTS_LOG) or the latest `##` section (WEEKLY_STATUS), not from a dedicated "head" block.
- CANON §8 (weekly status report) is satisfied by the append-only `##` structure; the exact format is defined here and in the file headers.
