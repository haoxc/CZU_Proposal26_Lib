# Dashboard And Ledger

## Work MOC As Dashboard

The top work MOC should act like a proposal dashboard, not a file list.

This is the default rule, not a soft suggestion. Only relax it when the user explicitly asks for a different organization model.

Recommended sections:

1. overall goal
2. current judgment
3. topic/task list with status
4. current phase
5. current priority
6. most valuable next push
7. completion criteria
8. change ledger entry
9. related working documents

The key idea is simple:

- users should see what to push next, not what files exist

## Required Organizing Principles

Even when wording changes, the work MOC should preserve these principles:

- goal-driven structure
- topic/task list
- visible status
- current priority
- completion criteria
- change ledger

If one of these disappears, the page is drifting back toward a passive archive rather than an active proposal dashboard.

## Default Visualization Pattern

When generating an SVG or similar visual progress board for the work area, prefer a dashboard-style proposal path view by default.

Recommended information architecture:

1. overall goal
2. main path
3. current stage
4. topic/task cards with status
5. current bottleneck
6. next action
7. completion criteria

Recommended default chart form:

- main path route map
- current status summary
- topic/task cards

Avoid defaulting to:

- pure gantt charts
- pure file maps
- decorative process diagrams without status visibility

Only use a different chart type when the user explicitly requests it.

## Review Gates

Proposal dashboards should not only show progress. They should also expose review gates.

Recommended rule:

- every critical milestone needs a review checkpoint
- each checkpoint produces a written review report
- each checkpoint includes constructive improvements, not just findings
- each checkpoint includes quantified scoring and a radar chart or equivalent visual

Recommended minimum gate points:

1. topic/narrative convergence
2. scope freeze before major drafting lock
3. review-ready submission draft
4. final submission readiness
5. implementation kickoff readiness

Recommended default dimensions:

- goal alignment
- reform value
- innovation
- feasibility
- basis/team readiness
- support conditions
- compliance completeness

Interpretation rule:

- a gate is not passed if major `P1` issues are still open
- a gate is not complete if the report has no scoring visualization
- the visualization should visibly show the related report name or report title

## Change Ledger

Proposal repos need a change ledger to prevent silent drift.

Recommended fields:

| Field | Meaning |
| --- | --- |
| change id | unique id |
| date | decision date |
| object | what changed |
| type | add / adjust / merge / delete / refactor |
| content | what changed |
| trigger | why it changed |
| impact | what is affected |
| effect on goal | strengthen / neutral / drift risk |
| back-sync needed | yes / no |
| status | confirmed / executed / pending validation / retired |

## Drift Warnings

Treat these as warning signs:

- more and more documents, but hard facts still missing
- implementation expands before recommendation readiness
- narrative keeps shifting without better scoring odds
- governance changes are not logged

## Audit Expectation

When auditing a proposal workspace:

- check whether the dashboard actually drives work
- check whether major changes are ledgered
- check whether current priority matches the real bottleneck
