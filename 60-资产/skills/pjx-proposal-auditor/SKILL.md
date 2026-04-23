---
name: pjx-proposal-auditor
description: Audit proposal-management workspaces for grants, applications,申报项目, and课题申报库. Use when the user wants to review or improve directory structure, dashboard MOCs, naming rules, change ledgers, proposal workflow boundaries, or target-drift control in an application/project repository.
---

# PJX Proposal Auditor

Use this skill for proposal-type workspaces whose main job is:

- 课题申报
- 项目申请
- 申请书写作与管理
- 申报材料推进
- 审计申报项目目录
- 建立申请类项目管理库

This skill is not for general software delivery repos. It is for repositories whose core object is an `application workflow`, not a product codebase.

## What This Skill Owns

This skill audits and refactors proposal-management workspaces around five things:

1. top-level directory model
2. work-directory module boundaries
3. dashboard-style MOCs
4. naming rules and lifecycle naming
5. change ledger and target-drift control

Read these references before proposing structural changes:

- [references/directory-model.md](references/directory-model.md)
- [references/naming-and-lifecycle.md](references/naming-and-lifecycle.md)
- [references/dashboard-and-ledger.md](references/dashboard-and-ledger.md)

## Core Audit Lens

For proposal workspaces, the main failure mode is not only “messy folders”.

The real failure modes are:

- proposal text, evidence, and governance mixed together
- many files, but no visible current priority
- repeated rewrites without change traceability
- goal drift: scope expands while hard requirements remain unresolved
- MOCs become file dumps instead of decision-driving dashboards

## Default Directory Model

Use the model in the reference file as the default unless the project already has a confirmed local standard.

At a high level, proposal workspaces should separate:

- entry and navigation
- rules
- management
- governance
- active proposal work
- assets
- archive
- attachments
- settings

The recommended active work area is a single work directory with internal modules, rather than many top-level work folders.

## Default Work Modules

Inside the main work directory, the standard modules are:

- proposal submission
- solution design
- implementation reserve
- benchmark research
- evaluation and argumentation

Do not flatten these as parallel top-level directories unless the local standard explicitly chooses that model.

## MOC Rule

For this skill, MOCs must be goal-oriented.

That means:

- do not start with file inventories
- start with current goal, status, bottleneck, and next move
- use links only as support, not as the main content

This is a **default hard rule** for proposal-management workspaces unless the user explicitly asks for another organization model.

The top work MOC should usually behave like a proposal dashboard:

- overall goal
- current judgment
- topic/task list with status
- current phase
- current priority
- next most valuable push
- completion criteria
- change ledger entry point
- related working documents

The underlying organizing principles that should be preserved even when the exact page layout changes are:

- goal-driven structure
- topic/task list
- visible status
- current priority
- completion criteria
- change ledger

Do not regress from a goal-driving dashboard back to a document-list MOC unless the user explicitly requests that tradeoff.

## Visualization Default

When this skill helps design an SVG or other visual progress board for a proposal workspace, use a goal-driving dashboard chart by default.

Default visual emphasis:

- main path
- current stage
- topic/task status
- bottleneck
- next action

Do not default to a pure gantt, a pure file map, or a decorative flowchart unless the user explicitly asks for that chart type.

## Review Gate Rule

For this skill, proposal workspaces should use mandatory review gates at critical milestones.

This is a project-level audit rule, not an optional suggestion.

At each critical milestone, require:

- one review assessment report
- constructive improvement advice
- quantified multi-dimensional scoring
- a radar chart or equivalent score visualization

Minimum recommended gates:

1. after topic and narrative convergence
2. before phase-1 scope freeze
3. when the submission draft reaches review-ready state
4. before final submission packaging
5. before post-award implementation kickoff

Recommended default dimensions:

- goal alignment
- teaching-reform value
- innovation and distinctiveness
- feasibility and path completeness
- research basis and team readiness
- resource/security/support conditions
- compliance and submission completeness

Gate rule:

- if major `P1` risks remain open, the gate is not passed
- if there is no review report and no quantitative visualization, the gate is not considered complete
- the SVG should explicitly show the related report name so the chart keeps its audit context when viewed alone
- store gate reviews under the evaluation/argumentation area rather than mixing them into the submission draft

## Naming Rule

Use the project rule if it exists. Otherwise apply this default:

- stable baseline files do not need dates by default
- one-time process files should include `yy.MMdd`
- folder notes are an explicit exception and may match the folder name exactly
- draft files should expose lifecycle state such as `草案`, `填报稿`, `审计意见`, `要点摘录`
- avoid vague names such as `方案.md`, `材料.md`, `最终版.md`

Important:

- if a file is a temporary analysis, audit memo, snapshot, or review report, treat it as a process file and date it
- if a file is the current maintained rule, ledger, or active baseline, do not force a date just because it is recent

## Change Ledger Rule

Proposal workspaces need a dedicated change ledger.

Its purpose is:

- explain why important changes happened
- make later audits possible
- identify target drift early

The change ledger should record:

- title changes
- scope changes
- major narrative changes
- category changes
- funding-commitment changes
- directory restructures
- major technical-path changes

When a change affects multiple documents or may create goal drift, log it before rewriting the body files.

## Target Drift Checks

Flag drift when you see patterns like:

- new work keeps appearing but the main hard requirements remain unresolved
- implementation details expand while the proposal still lacks applicant/funding/evidence basics
- titles keep changing without improving recommendation probability
- evaluation risks are still open but the repo starts building delivery details too early

## Output Format

Use this structure by default:

```markdown
**结论**
One short paragraph with the main judgment.

**Findings**
- [P1/P2/P3] Title
  - Evidence
  - Why it matters
  - Fix

**建议调整**
| 当前 | 建议 | 原因 |
| --- | --- | --- |

**验证重点**
- ...
```

For implementation requests, do not stop at findings. Update the local rule files and governance records when the change alters the project standard.

## Guardrails

- Do not rename folder notes as ordinary files if the workspace uses Obsidian folder-note behavior.
- Do not treat management pages and governance records as the same object.
- Do not let the work MOC become a file dump.
- Do not replace a goal-driven dashboard with a document inventory page unless the user explicitly requests it.
- Do not push implementation detail ahead of unresolved application hard gates.
- Do not invent additional proposal modules unless the current project genuinely needs them.
