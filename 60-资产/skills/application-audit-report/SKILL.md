---
name: application-audit-report
description: Turn a reviewed Chinese application or proposal into a polished audit report, especially for teaching-reform and Jiangsu library applications. Use when the user wants an expert-style audit memo, a visual scorecard, an SVG review sheet, or a concise strengths-risks-actions report after review.
---

# Application Audit Report

Use this skill after a proposal has been reviewed or when the user explicitly asks for:

- 审计报告
- 评审意见稿
- 评分卡
- SVG 报告
- 专家意见摘要

## What This Skill Produces

- concise audit memo
- strengths / risks / actions summary
- reviewer-facing scorecard
- SVG report when needed

## Workflow

### 1. Start from judgment, not decoration

Before writing the report, make sure you know:

- overall verdict
- gate risks
- weighted scores
- top 3 strengths
- top 3 weaknesses
- top 3 revision actions

If these are not available yet, tell the user and switch to `$proposal-review-auditor` first.

### 2. Use a reviewer structure

Default section order:

1. overall judgment
2. gate risks
3. weighted score summary
4. strengths
5. risks
6. revision priorities

### 3. Keep the tone expert and controlled

The report should read like:

- a serious reviewer
- not a marketing deck
- not a generic AI checklist

### 4. Generate SVG when asked

Use:

- [../proposal-review-auditor/scripts/generate_svg_report.py](../proposal-review-auditor/scripts/generate_svg_report.py)

Prepare the same structured inputs the script expects.

## Special Rule for Jiangsu Library Applications

If the target is a Jiangsu higher-education library teaching-reform proposal, ensure the report explicitly comments on:

- topic alignment with annual notice
- matching funds
- recommendation readiness
- project category realism
- evidence of research basis

## Output Standard

Prefer short expert paragraphs over bloated prose.

For SVG reports:

- keep layout clean
- avoid loud colors
- make the score immediately readable
- surface the actual risks, not decorative slogans
