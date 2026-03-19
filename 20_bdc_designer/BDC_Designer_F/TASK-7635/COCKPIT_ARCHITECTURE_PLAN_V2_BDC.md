# Cockpit Architecture Plan v2 (BDC Corrective Version)

## Purpose

This is the corrected `v2` architecture plan for `Cockpit` after review against:
- the current `COCKPIT-TZ-v3` shape,
- the runtime clarification provided by the partner,
- and the current official Claude Agent SDK / Claude Code documentation.

This document is intentionally pragmatic.

It is **not** a product pitch.
It is **not** a speculative enterprise roadmap.
It is the shortest honest path from the current Cockpit to a stronger execution architecture.

## Executive Verdict

The earlier upgrade direction was broadly correct on one central point:
- Cockpit should move away from raw `claude` subprocess control as its long-term execution core.

But the earlier plan was too loose in four places:
1. it treated the session layer too casually;
2. it over-promised checkpointing as a universal undo system;
3. it pulled `Agent Teams` / multi-agent scope too early;
4. it described “one client per project” where the correct unit is a **session**, not a project.

## What Should Be Accepted From the Earlier Plan

The following direction is correct and should be kept:

1. move the backend execution layer toward the official Python Agent SDK;
2. replace brittle stdout-string parsing as the long-term primary contract;
3. make tool approvals first-class in the UI;
4. add bounded file checkpointing and rewind;
5. support MCP after the core runtime contract is stable.

## What Must Be Corrected

### Correction 1: Session is the primary runtime unit

Do **not** build the new backend around “one persistent client per project”.

That model is too weak for:
- multiple tabs,
- multiple sessions in one project,
- restart/resume,
- future multi-user operation,
- clear ownership of history.

The correct unit is:
- **one managed SDK session per Cockpit session**

Project remains a container for:
- `cwd`
- defaults
- policies
- model preferences

But conversation continuity belongs to the session.

Official basis:
- sessions persist conversation history and are the proper mechanism for continue/resume/fork:
  - [Work with sessions](https://platform.claude.com/docs/en/agent-sdk/sessions)

### Correction 2: Checkpointing is bounded, not universal

Checkpointing is useful, but it must not be sold or implemented as a full “time machine”.

What it can do:
- revert file changes made through `Write`, `Edit`, and `NotebookEdit`

What it does **not** guarantee:
- rollback of arbitrary bash side effects
- rollback of external system mutations
- rollback of git/network/database effects

So the UI action should be framed as:
- `Undo Claude file edits`

Not:
- `Undo everything`

Official basis:
- [File checkpointing](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)

### Correction 3: Agent Teams are not core roadmap material yet

Do not make `Agent Teams` part of the core Cockpit upgrade plan.

Right now the disciplined path is:
1. fix session truth;
2. fix permission truth;
3. fix checkpoint truth;
4. stabilize MCP and runtime observability;
5. only then discuss subagents or broader orchestration surfaces.

If you open multi-agent scope before the single-session runtime is stable, you will magnify:
- state ambiguity,
- event routing complexity,
- permission ambiguity,
- persistence complexity,
- UI confusion.

Current official surface is much clearer around:
- sessions,
- user input / approvals,
- permissions,
- checkpointing,
- MCP,
- subagents.

That is enough for the next stage.

Official basis:
- [Subagents in the SDK](https://platform.claude.com/docs/en/agent-sdk/subagents)
- no need to make “agent teams” a platform commitment before the core Cockpit runtime is proven

### Correction 4: Permissions in Python have an implementation caveat

The permission path is real and should be used.

But in Python, `can_use_tool` is not just a flip-the-switch callback.
It requires:
- streaming mode
- and a `PreToolUse` hook to keep the stream alive

So the permissions redesign is correct,
but the implementation plan must explicitly budget for this detail.

Official basis:
- [Handle approvals and user input](https://platform.claude.com/docs/en/agent-sdk/user-input)
- [Configure permissions](https://platform.claude.com/docs/en/agent-sdk/permissions)

## Corrected Target Architecture

```text
Browser UI
  -> WebSocket transport
  -> Cockpit session manager
  -> SDK-backed execution session
  -> Claude Agent SDK session
  -> Tool approvals / checkpoint / MCP / resume
  -> event relay
  -> UI store rendering
```

### Core rule

Frontend shell remains largely intact:
- React
- Zustand
- WebSocket
- Task panel
- stream rendering

The primary rewrite target is the **backend execution contract**, not the UI shell.

## Corrected Phased Plan

## Phase A — Freeze Current Truth

Goal:
- document the current subprocess-based behavior exactly

Required outputs:
- current session lifecycle
- current follow-up behavior
- current event mapping
- current permission limitations
- current persistence limitations

Why:
- you need a clean baseline before migration

## Phase B — Introduce Session-Centric SDK Backend

Goal:
- replace raw execution core with a session-managed Python SDK layer

Implementation rule:
- one Cockpit session maps to one managed SDK session

Session record should minimally track:
- `session_id`
- `project_id`
- `cwd`
- `model`
- `created_at`
- `last_activity_at`
- `status`
- `resume_mode`
- `sdk_session_id`
- `last_checkpoint_id`

Core behaviors:
- create session
- continue same session
- resume specific session
- optionally fork later

Official basis:
- [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop)
- [Work with sessions](https://platform.claude.com/docs/en/agent-sdk/sessions)
- [Python SDK reference](https://platform.claude.com/docs/en/agent-sdk/python)

## Phase C — Replace Brittle Event Contract

Goal:
- move from raw stdout-string dependency toward SDK message objects

You should still normalize events into your own WS protocol.

Do **not** pipe SDK objects directly to frontend with no internal contract.

Backend should define a stable Cockpit event surface such as:
- `session_created`
- `stream_text`
- `tool_use`
- `tool_result`
- `permission_required`
- `session_status`
- `session_ended`

But the backend source should now come from typed SDK messages:
- `SystemMessage`
- `AssistantMessage`
- `UserMessage`
- `ResultMessage`

Official basis:
- [How the agent loop works](https://platform.claude.com/docs/en/agent-sdk/agent-loop)

## Phase D — First-Class Interactive Permissions

Goal:
- make runtime approvals a core user-facing interaction

Flow:
1. SDK requests approval
2. backend emits `permission_required`
3. UI modal shows:
   - tool
   - command or file action
   - description
   - affected target
4. user chooses allow/deny
5. backend returns permission result to SDK

Important:
- design this as a runtime contract, not as decorative UI

Official basis:
- [Handle approvals and user input](https://platform.claude.com/docs/en/agent-sdk/user-input)
- [Configure permissions](https://platform.claude.com/docs/en/agent-sdk/permissions)

## Phase E — Bounded Checkpointing

Goal:
- give the operator safe rollback for SDK-mediated file edits

UI wording should be explicit:
- `Undo Claude file edits`

Not:
- `Undo session`
- `Undo all actions`

Store:
- checkpoint ID
- time
- affected files
- tool origin

Official basis:
- [File checkpointing](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)

## Phase F — MCP Integration After Core Stability

Goal:
- add controlled external tool expansion only after core session/permission model is stable

MCP should be treated as:
- extension surface
- not phase-one necessity

Why:
- otherwise you expand the blast radius before proving the core runtime

Initial MCP design should include:
- explicit server registry
- per-project enablement
- permission rules
- audit trail of MCP tool use

Official basis:
- [Connect to external tools with MCP](https://platform.claude.com/docs/en/agent-sdk/mcp)

## Phase G — Defer Subagents / Multi-Agent Scope

Goal:
- explicitly **not** expand scope too early

Subagents may become relevant later.
They are not the correct first migration step.

You should not open:
- multi-agent orchestration canvas,
- team-kanban abstractions,
- leader/worker routing,
- or “enterprise agent teams”

until the following are already measured:
- stable session continuity
- approval correctness
- checkpoint correctness
- reconnect correctness
- persistence correctness

## What the Correct Next Build Order Looks Like

1. freeze and measure current subprocess behavior
2. implement session-centric SDK layer
3. normalize SDK messages into stable Cockpit WS events
4. implement interactive approvals
5. implement bounded checkpoint rewind
6. verify reconnect/persistence semantics
7. add MCP carefully
8. only then discuss subagents or broader orchestration

## What Should Not Be Done Now

- do not rewrite the frontend shell first
- do not introduce agent teams now
- do not promise universal undo
- do not keep “new process per follow-up” as an acceptable long-term model
- do not bind conversation truth to project identity
- do not widen scope before measuring the core SDK migration

## Minimum Measured Success Criteria For the Upgrade

The migration should not be called successful until these are measured:

1. follow-up retains correct session context
2. permission requests round-trip through UI correctly
3. checkpoint rewind correctly restores SDK-mediated file edits
4. session can resume after process or UI interruption
5. event ordering remains stable in the Cockpit WS layer
6. no hidden downgrade in task completion rate versus current subprocess path

## Final BDC Position

The earlier plan was directionally right:
- move toward the official SDK

But the corrected BDC version is stricter:
- session-centric, not project-centric
- permissions as runtime truth, not just UX sugar
- checkpointing as bounded file rewind, not magic undo
- MCP later, not first
- no early multi-agent expansion

## One-Line Decision

**Cockpit should migrate from subprocess-driven single-shot control to a session-centric Python Agent SDK backend, while explicitly deferring multi-agent scope until session, permission, checkpoint, and persistence truth are measured.**
