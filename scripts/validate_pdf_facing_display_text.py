from __future__ import annotations

from pathlib import Path
from typing import Iterable


PDF_FACING_FILES = [
    Path("output/latest/chatgpt_daily_report_packet_latest.txt"),
    Path("output/latest/CHATGPT_DAILY_REPORT_PACKET.txt"),
    Path("output/latest/chatgpt_indicator_usage_guide_latest.md"),
    Path("output/latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt"),
    Path("output/latest/warrant_flow_latest.md"),
    Path("output/latest/CHATGPT_DAILY_REPORT_RULES.txt"),
    Path("output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md"),
    Path("output/latest/tdcc_weekly_candidate_full_for_report_latest.md"),
    Path("docs/latest/chatgpt_daily_report_packet_latest.txt"),
    Path("docs/latest/CHATGPT_DAILY_REPORT_PACKET.txt"),
    Path("docs/latest/chatgpt_indicator_usage_guide_latest.md"),
    Path("docs/latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt"),
    Path("docs/latest/warrant_flow_latest.md"),
    Path("docs/latest/CHATGPT_DAILY_REPORT_RULES.txt"),
]

PDF_FACING_PDFS = [
    Path("output/latest/mainstream_daily_recommendation_highlight_latest.pdf"),
    Path("output/latest/mainstream_full_candidate_list_latest.pdf"),
    Path("output/latest/non_mainstream_daily_recommendation_highlight_latest.pdf"),
    Path("output/latest/non_mainstream_full_candidate_list_latest.pdf"),
    Path("output/latest/warrant_market_report_latest.pdf"),
    Path("output/latest/market_risk_dashboard_latest.pdf"),
    Path("output/latest/tdcc_weekly_candidate_highlight_latest.pdf"),
    Path("output/latest/tdcc_weekly_candidate_full_latest.pdf"),
]

REQUIRED_TDCC_PDFS = [
    Path("output/latest/tdcc_weekly_candidate_highlight_latest.pdf"),
    Path("output/latest/tdcc_weekly_candidate_full_latest.pdf"),
]

RAW_TOKENS = [
    "call_strong_inflow",
    "call_inflow",
    "call_put_bullish",
    "put_strong_inflow",
    "put_inflow",
    "put_call_bearish",
    "mixed_flow",
    "call_activity_observation",
    "put_activity_observation",
    "low_float_call_spike",
    "no_signal",
    "range_rebound",
    "revenue_pullback",
    "revenue_breakout_low_response",
    "pullback_rebound",
    "short_term_specialty",
    "tdcc_short_term_edge",
    "tdcc_short_term_continuation_d5_d10",
    "insufficient_data",
    "strong_accumulation",
    "mild_accumulation",
    "distribution_warning",
    "mainstream_leader",
    "mainstream_follow_through",
    "single_name_signal",
    "non_mainstream",
    "other electronics",
    "semiconductor equipment",
    "semiconductor",
    "power discrete",
    "networking",
    "biotechnology",
    "connector/cable",
    "memory",
]

MOJIBAKE_MARKERS = [
    "�",
    "銝",
    "蝐",
    "嚗",
    "鞈",
    "憭",
    "隤",
    "撟",
    "瘥",
    "摰",
    "閫",
    "餈",
    "鈭",
    "",
    "",
]


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - validated in CI
        raise RuntimeError(f"pypdf unavailable for PDF display validation: {exc}") from exc

    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def iter_sources() -> Iterable[tuple[Path, str]]:
    for path in PDF_FACING_FILES:
        if path.exists():
            yield path, path.read_text(encoding="utf-8", errors="replace")
    for path in PDF_FACING_PDFS:
        if path.exists():
            yield path, extract_pdf_text(path)


def main() -> int:
    problems: list[str] = []
    warnings: list[str] = []

    for path in REQUIRED_TDCC_PDFS:
        if not path.exists():
            problems.append(f"{path}: missing required TDCC weekly PDF")

    for path, text in iter_sources():
        target = problems if path.suffix.lower() == ".pdf" else warnings
        for line_no, line in enumerate(text.splitlines(), start=1):
            for token in RAW_TOKENS:
                if token in line:
                    target.append(f"{path}:{line_no}: raw token `{token}`")
            for marker in MOJIBAKE_MARKERS:
                if marker in line:
                    target.append(f"{path}:{line_no}: mojibake marker `{marker}`")

    if problems:
        print("PDF-facing display text validation failed:")
        for problem in problems[:200]:
            print(problem)
        if len(problems) > 200:
            print(f"... {len(problems) - 200} more")
        return 1

    if warnings:
        print("PDF-facing display text validation warnings in non-PDF helper files:")
        for warning in warnings[:50]:
            print(warning)
        if len(warnings) > 50:
            print(f"... {len(warnings) - 50} more")

    print("PDF-facing display text validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
