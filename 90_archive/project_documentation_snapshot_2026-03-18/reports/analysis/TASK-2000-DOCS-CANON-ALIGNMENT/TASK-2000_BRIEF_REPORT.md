# TASK-2000 BRIEF REPORT

## Scope
- Align documentation layer to canonical navigation centered on:
  - `docs/project/project_main_doc.md`
  - `docs/project/project_roadmap.md`
- Add explicit deprecation markers for legacy project main-doc/roadmap files.
- Introduce experiment-level documentation standard and create Phase 1 EXP-0300 document.
- Keep changes documentation-only (no runtime code or script changes).

## Changes
- Updated project index:
  - `docs/project/README.md`
- Added deprecation headers:
  - `docs/project/BDC_PROJECT_MAIN_DOC.MD`
  - `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`
  - `docs/project/BDC_ROADMAP_Paramecium_MVP_ (TRL-3).MD`
- Link hygiene and canonical references:
  - `reports/analysis/PROJECT_KNOWLEDGE_CONSOLIDATED_20260227.md`
  - `decisions/ADR-0004-hidden-rule-closure.md`
  - `reports/analysis/TASK-1400-COMPLEXITY-AUDIT/TASK-1400_BRIEF_REPORT.md`
  - `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`
  - `reports/analysis/TASK-1501-COMPLEXITY-SWEEP/TASK-1501_BRIEF_REPORT.md`
  - `reports/analysis/TASK-1502-COMPLEXITY-SWEEP-FULL/TASK-1502_BRIEF_REPORT.md`
- Added experiment docs layer:
  - `docs/experiments/README.md`
  - `docs/experiments/EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md`
- Updated master documents to include experiment docs policy:
  - `docs/project/project_main_doc.md`
  - `docs/project/project_roadmap.md`

## Verification (L0)
- Command: `git diff --name-only | rg -n "\.(py|sh|ps1)$"`
  - Result: PASS
  - Output summary: no executable files changed.
- Command: `rg -n "project_main_doc|project_roadmap" docs/project/README.md`
  - Result: PASS
  - Output summary: README explicitly marks both files as primary entry points.
- Command: `Get-Content docs/project/BDC_PROJECT_MAIN_DOC.MD -TotalCount 12; Get-Content docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md -TotalCount 12`
  - Result: PASS
  - Output summary: both legacy docs have top `[DEPRECATED]` banner with links to canonical docs.
- Command: `rg -n "TASK-1501|TASK-1502|ADR-0005|Regime|A|B|C|D|E" docs/experiments/EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md`
  - Result: PASS
  - Output summary: EXP-0300 exists and includes A..E regime table and required links.
- Command: `rg -n "docs/experiments" docs/project/project_main_doc.md docs/project/project_roadmap.md`
  - Result: PASS
  - Output summary: both master docs mention experiment documentation layer.
- Command: `rg -n "TASK-2000-DOCS-CANON-ALIGNMENT|TASK-2000" AGENTS_LOG.md WEEKLY_STATUS.md`
  - Result: PASS
  - Output summary: append-only log/status entries added.

## Artifacts
- `docs/project/README.md` - canonical project-doc index.
- `docs/project/BDC_PROJECT_MAIN_DOC.MD` - deprecated marker + forward links.
- `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md` - deprecated marker + forward links.
- `docs/experiments/README.md` - experiment-doc standard.
- `docs/experiments/EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md` - Phase 1 experiment description.
- `docs/project/project_main_doc.md` - experiment docs layer section.
- `docs/project/project_roadmap.md` - phase-completion EXP requirement.
- `reports/analysis/TASK-2000-DOCS-CANON-ALIGNMENT/TASK-2000_BRIEF_REPORT.md` - this report.

## Risks / Limitations
- This task does not alter runtime behavior or experiment outputs; it only aligns documentation and references.
- Historical docs remain in repository; users must follow deprecation banners to avoid stale guidance.

## Rollback
- `git revert <TASK-2000-commit-hash>`
