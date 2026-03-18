# CODEX PERSONAL OPERATIONS NOTE (BDC)

Status: personal working note for Codex only.  
Last updated: 2026-03-07

## 1) What this repo is now
- BDC is no longer just a research sandbox around cooperative coevolution.
- The validated core is now a restricted theory and product stack:
  - causal equilibrium law
  - architecture priors from task causal structure
  - effective role-count reasoning
  - hybrid search guidance
  - BDC Designer CLI as the operator-facing tool
- The project has moved from internal theory validation into productization, pilot operations, proof extraction, and vertical go-to-market.

## 2) Ground rules to remember first
- Primary working branch: `test`
- `main` is protected unless user explicitly says `merge main now`
- Treat `agents.md` + Canon stack as authority, not this file
- `results/` artifacts are usually runtime outputs and should not be committed
- `AGENTS_LOG.md` and `WEEKLY_STATUS.md` are append-only

## 3) First 5 minutes of every new session
1. `git branch --show-current`
2. `git status --short`
3. `git log --oneline -n 15`
4. Read tail of:
   - `AGENTS_LOG.md`
   - `WEEKLY_STATUS.md`
5. Re-open the latest finished package reports, then identify the next package boundary before writing code.

## 4) Source-of-truth priority
1. `CANON.md`
2. `SEMANTICS.md`, `SEED_POLICY.md`, `KILL_CRITERIA.yaml`, `REPRODUCIBILITY.md`, `VERSIONING.md`
3. ADRs in `decisions/` and `docs/adr/`
4. Policies in `docs/`
5. Project docs / roadmap
6. Logs, reports, runtime outputs

If a task conflicts with levels 1-2, stop and escalate.

## 5) Project state snapshot as of 2026-03-07
- The old `TASK-1400B` era note is obsolete.
- The research core has already gone through:
  - equilibrium/causal architecture validation
  - negative result on universal transition-law recovery
  - restricted-theory consolidation
  - OOD validation
  - reproduction/manuscript/review packaging
  - CLI/tooling/productization
  - real-task validation, casebook, onboarding, release candidate
  - pilot/commercial pipeline design
  - proof/inbound/vertical GTM packaging

## 6) Validated core to remember
- Restricted BDC is the current scientific claim boundary.
- Supported:
  - equilibrium role weights track causal contribution structure
  - architecture priors can be derived from task causal structure
  - BDC is useful as a prior / hybrid design bias
- Not supported:
  - no portable universal transition law
  - no strong regime-local rescue sufficient to restore a transferable transition law
  - no hidden-state rescue strong enough to overturn that negative result
  - no claim that standalone BDC is a universal optimizer

## 7) Product/commercial state to remember
- Tool: `BDC Designer CLI`
- Positioning: restricted architecture-prior and hybrid-design system
- Sales motion already built:
  - release package
  - demo pack
  - sales offer pack
  - landing-page copy
  - outreach pack
  - pilot program
  - telemetry / feedback loop
  - commercial pilot kit
  - proof asset system
  - inbound authority loop

## 8) Where execution actually stopped
- Latest completed package before this note:
  - `PHASE-34-VERTICAL-EXECUTION-AND-WINNER-SELECTION`
- Completed tasks:
  - `TASK-7390` sales vertical outreach/pilot batch
  - `TASK-7400` real-estate vertical outreach/pilot batch
  - `TASK-7410` vertical comparative conversion review
  - `TASK-7420` retainer and expansion offer design
  - `TASK-7430` vertical winner decision
- Real stop point:
  - winner wedge for next 90 days = `sales_automation`
  - rationale: stronger revenue, faster paid cycle, lower execution friction, stronger proof

## 9) Files to reopen first when resuming
- Winner decision:
  - `results/vertical_winner/winner_decision_matrix.csv`
  - `results/vertical_winner/90_day_focus_plan.json`
  - `reports/analysis/TASK-7430-VERTICAL-WINNER-DECISION/TASK-7430_BRIEF_REPORT.md`
- Vertical comparison:
  - `results/vertical_comparison/vertical_review_summary.json`
  - `reports/analysis/TASK-7410-VERTICAL-COMPARATIVE-CONVERSION-REVIEW/TASK-7410_BRIEF_REPORT.md`
- Sales wedge packaging:
  - `reports/public_release/TASK-7340-SALES-AUTOMATION-VERTICAL-PACK/BDC_SALES_AUTOMATION_VERTICAL_PACK.md`
  - `reports/public_release/TASK-7360-VERTICAL-DEMO-ASSET-BATCH/BDC_VERTICAL_DEMOS.md`
  - `results/vertical_pricing/offer_tiers.csv`
  - `docs/BDC_VERTICAL_GTM_PLAYBOOK.md`
  - `docs/BDC_RETAINER_AND_EXPANSION_PLAYBOOK.md`

## 10) Immediate next-step heuristic
- If user asks "where did we stop?" -> answer: phase 34 finished, sales automation selected as primary wedge.
- If user asks for next work without a spec -> assume the next package should build on the sales wedge, GTM execution, pilot conversion, or product hardening rather than going back into abstract theory.
- If user asks for merge to `main` -> only do it after verifying `test` is clean and pushed.

## 11) Session close checklist
1. Re-run key verification commands for any claim made.
2. Ensure only intended files are staged.
3. Update append-only logs if the work is task-level and persistent.
4. Commit atomically.
5. Push `test`.
6. If user explicitly requests release/merge, merge `test -> main`, push `main`, then return to `test`.
