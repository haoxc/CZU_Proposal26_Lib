#!/usr/bin/env python3
from __future__ import annotations

import html
import sys
from pathlib import Path


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def wrap_lines(text: str, width: int) -> list[str]:
    if not text:
        return [""]
    chunks = []
    current = ""
    for ch in text:
        current += ch
        if len(current) >= width:
            chunks.append(current)
            current = ""
    if current:
        chunks.append(current)
    return chunks


def bullet_block(x: int, y: int, items: list[str], color: str) -> str:
    lines = []
    cy = y
    for item in items:
        wrapped = wrap_lines(item, 26)
        lines.append(
            f'<circle cx="{x}" cy="{cy - 5}" r="4" fill="{color}" />'
        )
        for idx, line in enumerate(wrapped):
            tx = x + 14
            ty = cy + idx * 22
            lines.append(
                f'<text x="{tx}" y="{ty}" font-size="16" fill="#17324d">{esc(line)}</text>'
            )
        cy += max(32, len(wrapped) * 22 + 10)
    return "\n".join(lines)


def bar_row(x: int, y: int, label: str, score: int) -> str:
    width = 260
    fill = round(width * max(0, min(score, 100)) / 100)
    color = "#1976d2" if score >= 80 else "#f59e0b" if score >= 65 else "#d14343"
    return f"""
    <text x="{x}" y="{y}" font-size="16" fill="#17324d">{esc(label)}</text>
    <rect x="{x+120}" y="{y-14}" rx="8" ry="8" width="{width}" height="14" fill="#dbe7f3" />
    <rect x="{x+120}" y="{y-14}" rx="8" ry="8" width="{fill}" height="14" fill="{color}" />
    <text x="{x+392}" y="{y}" text-anchor="end" font-size="15" fill="#17324d">{score}</text>
    """


def main() -> int:
    if len(sys.argv) != 11:
        print(
            "Usage: generate_svg_report.py OUTPUT TITLE PROJECT SCORE BARS STRENGTHS RISKS ACTIONS GATES SOURCES DATE",
            file=sys.stderr,
        )
        return 1

    output, title, project, score, bars, strengths, risks, actions, gates, sources, date = sys.argv[1:]
    score = int(score)
    bar_pairs = []
    for part in bars.split("|"):
        label, val = part.split(":")
        bar_pairs.append((label, int(val)))

    strengths_list = [s for s in strengths.split("|") if s]
    risks_list = [s for s in risks.split("|") if s]
    actions_list = [s for s in actions.split("|") if s]
    gates_list = [s for s in gates.split("|") if s]
    sources_list = [s for s in sources.split("|") if s]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1180" viewBox="0 0 1400 1180">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#f4f8fc"/>
    <stop offset="100%" stop-color="#e8f0f8"/>
  </linearGradient>
  <linearGradient id="hero" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#143b63"/>
    <stop offset="100%" stop-color="#2563a6"/>
  </linearGradient>
</defs>
<rect width="1400" height="1180" fill="url(#bg)" />
<rect x="48" y="36" width="1304" height="164" rx="28" fill="url(#hero)" />
<text x="88" y="95" font-size="18" fill="#d9e9fb">Application Review Audit</text>
<text x="88" y="136" font-size="34" font-weight="700" fill="#ffffff">{esc(title)}</text>
<text x="88" y="172" font-size="19" fill="#d9e9fb">{esc(project)}</text>
<rect x="1110" y="70" width="180" height="96" rx="22" fill="#ffffff" opacity="0.14" />
<text x="1200" y="107" text-anchor="middle" font-size="16" fill="#d9e9fb">综合评分</text>
<text x="1200" y="147" text-anchor="middle" font-size="40" font-weight="700" fill="#ffffff">{score}</text>

<rect x="48" y="228" width="620" height="360" rx="24" fill="#ffffff" />
<text x="84" y="272" font-size="24" font-weight="700" fill="#17324d">维度评分</text>
"""
    y = 320
    for label, val in bar_pairs:
        svg += bar_row(84, y, label, val)
        y += 42

    svg += f"""
<rect x="700" y="228" width="652" height="360" rx="24" fill="#ffffff" />
<text x="736" y="272" font-size="24" font-weight="700" fill="#17324d">江苏专项门槛检查</text>
<rect x="736" y="295" width="560" height="2" fill="#dbe7f3" />
{bullet_block(750, 336, gates_list, "#1976d2")}

<rect x="48" y="616" width="412" height="408" rx="24" fill="#ffffff" />
<text x="84" y="660" font-size="24" font-weight="700" fill="#17324d">主要优势</text>
{bullet_block(96, 706, strengths_list, "#1f9d55")}

<rect x="494" y="616" width="412" height="408" rx="24" fill="#ffffff" />
<text x="530" y="660" font-size="24" font-weight="700" fill="#17324d">主要风险</text>
{bullet_block(542, 706, risks_list, "#d14343")}

<rect x="940" y="616" width="412" height="408" rx="24" fill="#ffffff" />
<text x="976" y="660" font-size="24" font-weight="700" fill="#17324d">优先改进动作</text>
{bullet_block(988, 706, actions_list, "#f59e0b")}

<rect x="48" y="1052" width="1304" height="86" rx="22" fill="#12314e" />
<text x="84" y="1086" font-size="16" fill="#d9e9fb">方法来源：{esc('；'.join(sources_list[:3]))}</text>
<text x="84" y="1114" font-size="15" fill="#b8d0e8">生成日期：{esc(date)}  ·  适用场景：江苏省高校图工委教改课题 / 高校教改申请书审计</text>
</svg>
"""

    Path(output).write_text(svg, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
