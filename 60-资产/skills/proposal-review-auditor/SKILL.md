---
name: proposal-review-auditor
description: Audit, score, and rewrite Chinese project applications or teaching-reform proposals, especially Jiangsu higher-education library proposals. Use when the user wants an application reviewed, scored, stress-tested against evaluator criteria, improved for funding odds, or turned into an expert-style audit report or SVG scorecard.
---

# Proposal Review Auditor

Use this skill for `申请书审计`, `申报书评审`, `课题申请评估`, `教改项目申报把关`, `立项概率判断`, `评审报告`, or similar requests.

This skill is optimized for:

- Chinese project applications
- Higher-education teaching-reform proposals
- Library innovation / education-reform proposals
- Jiangsu higher-education library committee applications

## What This Skill Does

This skill helps Codex act like a rigorous reviewer rather than a copy-editor.

Core outputs:

- an audit memo with findings first
- a scored rubric
- a Jiangsu-specific compliance check
- revision advice ordered by impact
- when requested, a polished SVG review report

## Review Workflow

### 1. Extract the application structure

Read the current proposal and identify:

- title
- applicant and team information
- problem statement
- objectives
- implementation path
- research methods
- expected outcomes
- budget / support conditions
- recommendation or endorsement text

If the proposal is incomplete, do not hide that. Score the missing parts as risk, not as neutral.

### 2. Run Jiangsu gate checks first

Before qualitative scoring, check whether the proposal clears hard constraints.

For Jiangsu higher-education library teaching-reform proposals, check:

- topic fits the current year notice
- applicant eligibility is plausible
- no obvious duplicate topic claim
- category choice is realistic (`重点` vs `一般`)
- matching funds are explicitly committed
- implementation path is complete
- outputs and推广价值 are stated
- school/library recommendation path is plausible

If any hard gate is missing, mark it as `gate risk`.

Read:

- [references/jiangsu-library-rules.md](references/jiangsu-library-rules.md)

### 3. Score with the weighted rubric

Use the rubric in:

- [references/review-framework.md](references/review-framework.md)

Default scoring dimensions:

- policy / topic alignment
- problem clarity and educational value
- innovation and distinctiveness
- implementation feasibility
- research basis and team readiness
- expected outcomes and transfer value
- compliance and application hygiene

When the proposal is for Jiangsu higher-education library teaching reform, prefer the Jiangsu weighting in the reference file.

### 4. Write findings before praise

Order findings by impact:

- P1: likely to block recommendation or funding
- P2: weakens competitiveness materially
- P3: polish issues or secondary inconsistencies

Do not open with encouragement. Start with the real risk profile.

### 5. Recommend revision moves

Give changes that materially improve the score:

- title repositioning
- scope narrowing
- evidence strengthening
- budget / support clarification
- output redesign
- language cleanup

Prefer “change this paragraph into this function” over vague advice.

### 6. Generate SVG review report when asked

If the user asks for SVG output, use:

- [scripts/generate_svg_report.py](scripts/generate_svg_report.py)

Inputs to prepare before running:

- report title
- project title
- overall score
- dimension labels and scores
- 3 strengths
- 3 risks
- 3 recommended actions
- Jiangsu gate summary

The script expects UTF-8 plain-text arguments and writes a standalone SVG.

## Writing Standard

Use the workspace Claude-style writing standard if present.

In this workspace, align with:

- professional
- calm
- human
- explicit judgment
- low jargon inflation

## Do Not Do

- do not treat incomplete information as “basically okay”
- do not bury hard constraints under style suggestions
- do not score high feasibility when the proposal lacks real implementation support
- do not convert a teaching-reform proposal into a pure technical proposal

## Quick Output Template

Use this compact structure unless the user asks otherwise:

1. Overall judgment
2. Gate risks
3. Weighted scores
4. Key findings
5. Revision priorities
6. Optional SVG artifact
