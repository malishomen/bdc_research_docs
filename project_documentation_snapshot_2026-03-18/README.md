# BIO-DIGITAL CORE (BDC)

## Purpose
BIO-DIGITAL CORE (BDC) is a disciplined framework for collaborative agent-driven development. This repository serves as the canonical source for task execution logs, agent protocols, and project artifacts.

**Core Principle:** Atomic commits, comprehensive logging, and verifiable execution.

## Working Branch
Active branch is task-dependent and defined by operator/runtime policy for the current phase.
Do not assume `test` or `main` by default; always verify current branch before work:

```bash
git branch --show-current
git status --short
```

## Branch Policy
- `main`: stable checkpoint branch unless explicit release/cutover requires direct work.
- `test`/feature branches: task execution and staging by default.
- Final authority for branch selection: task contract + `AGENTS.md` + operator instruction.

## Docs
Normative (single source of truth):
- `CANON.md`
- `SEMANTICS.md`
- `SEED_POLICY.md`
- `KILL_CRITERIA.yaml`
- `REPRODUCIBILITY.md`
- `VERSIONING.md`

Project references:
- `docs/project/`

## Repo Layout
```
Bio_Digital_Core/
├── qcore/              # Core quantum/digital logic
├── memory/             # Memory and state management
├── env/                # Environment configurations
├── agent/              # Agent definitions and protocols
├── evolution/          # Evolution and optimization logs
├── experiments/        # Experimental runs and results
├── decisions/          # Decision records and rationale
├── docs/               # Documentation
├── scripts/            # Utility scripts
└── results/            # Output and results artifacts
```

## How to Contribute
1. **Atomic Commits:** One logical unit = one commit. Include reason in message.
2. **Commit Format:** Use task IDs. Example: `TASK-0001: init repo skeleton`
3. **Mandatory Logging:** Every commit must have a corresponding entry in `AGENTS_LOG.md` with:
   - Timestamp (UTC)
   - Agent/executor name
   - Task ID
   - Result status
   - Artifacts created
   - Verification commands run
4. **No Assertions Without Artifacts:** Claims require proof (code, logs, test results).
5. **Rollback Ready:** Every change must have a documented rollback path.

## Agents Log
See `AGENTS_LOG.md` for execution history. Canonical format: timestamp | agent | task_id | result | artifacts.

---

**Last updated:** 2026-02-25
**Status:** Active
