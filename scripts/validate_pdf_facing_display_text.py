from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Iterable


PDF_FACING_FILES = [
    Path("output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md"),
    Path("output/latest/tdcc_weekly_candidate_full_for_report_latest.md"),
    Path("output/latest/tdcc_weekly_increase_ranking_latest.md"),
    Path("output/latest/tdcc_consecutive_accumulation_ranking_latest.md"),
    Path("output/latest/tdcc_weekly_model_cross_summary_latest.md"),
    Path("docs/latest/tdcc_weekly_candidate_highlight_for_report_latest.md"),
    Path("docs/latest/tdcc_weekly_candidate_full_for_report_latest.md"),
    Path("docs/latest/tdcc_weekly_increase_ranking_latest.md"),
    Path("docs/latest/tdcc_consecutive_accumulation_ranking_latest.md"),
    Path("docs/latest/tdcc_weekly_model_cross_summary_latest.md"),
]

PDF_FACING_PDFS = [
    Path("output/latest/tdcc_weekly_candidate_highlight_latest.pdf"),
    Path("output/latest/tdcc_weekly_candidate_full_latest.pdf"),
]

REQUIRED_TDCC_PDFS = [
    Path("output/latest/tdcc_weekly_candidate_highlight_latest.pdf"),
    Path("output/latest/tdcc_weekly_candidate_full_latest.pdf"),
]

SOURCE_DISPLAY_FILES = [
    Path("scripts/build_tdcc_weekly_candidate_reports.py"),
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
    "core_mainstream",
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
    "\ufffd",  # Unicode replacement character, usually means decode failure.
]

PRIVATE_USE_RE = re.compile(r"[\ue000-\uf8ff]")
PANDAS_SERIES_LEAK_RE = re.compile(
    r"\bName:\s*\d+\s*,\s*dtype:\s*object\b|\bdtype:\s*object\b"
)


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - validated in CI
        raise RuntimeError(f"pypdf unavailable for PDF display validation: {exc}") from exc

    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def report_ready_signal_date() -> str:
    paths = [
        Path("output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv"),
        Path("output/latest/tdcc_weekly_candidate_full_for_report_latest.csv"),
    ]
    dates_by_path: list[set[str]] = []
    for path in paths:
        if not path.exists():
            return ""
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            dates = {row.get("signal_date", "").strip() for row in reader if row.get("signal_date", "").strip()}
        dates_by_path.append(dates)
    if len(dates_by_path) != 2 or any(len(dates) != 1 for dates in dates_by_path):
        return ""
    highlight_date = next(iter(dates_by_path[0]))
    full_date = next(iter(dates_by_path[1]))
    return highlight_date if highlight_date == full_date else ""


def tdcc_delivery_pdfs() -> list[Path]:
    signal_date = report_ready_signal_date()
    if not signal_date:
        return []
    return [
        Path(f"output/latest/TDCC大戶籌碼週報_精華版_{signal_date}.pdf"),
        Path(f"output/latest/TDCC大戶籌碼週報_完整版_{signal_date}.pdf"),
    ]


def iter_sources() -> Iterable[tuple[Path, str]]:
    for path in PDF_FACING_FILES:
        if path.exists():
            yield path, path.read_text(encoding="utf-8", errors="replace")
    for path in [*PDF_FACING_PDFS, *tdcc_delivery_pdfs()]:
        if path.exists():
            yield path, extract_pdf_text(path)


def is_machine_readable_helper_line(line: str) -> bool:
    lowered = line.lower()
    markers = [
        "raw_url:",
        "_raw_url:",
        "_path:",
        "path:",
        "http://",
        "https://",
        "chart_path",
        "chart_url",
        "file_path",
        "fields:",
    ]
    return any(marker in lowered for marker in markers)


def main() -> int:
    problems: list[str] = []
    warnings: list[str] = []

    required_pdfs = [*REQUIRED_TDCC_PDFS, *tdcc_delivery_pdfs()]
    for path in required_pdfs:
        if not path.exists():
            problems.append(f"{path}: missing required TDCC weekly PDF")

    for path in SOURCE_DISPLAY_FILES:
        if not path.exists():
            problems.append(f"{path}: missing source display file")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for marker in MOJIBAKE_MARKERS:
                if marker in line:
                    problems.append(f"{path}:{line_no}: source mojibake marker `{marker}`")
            if PRIVATE_USE_RE.search(line):
                problems.append(f"{path}:{line_no}: source private-use mojibake marker")

    for path, text in iter_sources():
        target = problems if path.suffix.lower() == ".pdf" else warnings
        for line_no, line in enumerate(text.splitlines(), start=1):
            if PANDAS_SERIES_LEAK_RE.search(line):
                problems.append(f"{path}:{line_no}: pandas Series leaked into display text")
            if path.suffix.lower() != ".pdf" and is_machine_readable_helper_line(line):
                continue
            for token in RAW_TOKENS:
                if token in line:
                    target.append(f"{path}:{line_no}: raw token `{token}`")
            for marker in MOJIBAKE_MARKERS:
                if marker in line:
                    target.append(f"{path}:{line_no}: mojibake marker `{marker}`")
            if PRIVATE_USE_RE.search(line):
                target.append(f"{path}:{line_no}: private-use mojibake marker")

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
