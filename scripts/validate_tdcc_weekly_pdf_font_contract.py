from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tdcc_weekly_pdf_font_contract import validate_tdcc_weekly_pdf_font_contract  # noqa: E402


LATEST_DIR = Path("output/latest")
HIGHLIGHT_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_highlight_for_report_latest.csv"
FULL_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_full_for_report_latest.csv"
HIGHLIGHT_PDF = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.pdf"
FULL_PDF = LATEST_DIR / "tdcc_weekly_candidate_full_latest.pdf"
DELIVERY_PDF_DIR = LATEST_DIR / "published_reports" / "tdcc_weekly"
DELIVERY_HIGHLIGHT_PDF_PREFIX = "TDCC大戶籌碼週報_精華版"
DELIVERY_FULL_PDF_PREFIX = "TDCC大戶籌碼週報_完整版"


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    return "" if text.lower() in {"nan", "none", "nat", "<na>"} else text


def read_signal_dates(path: Path) -> list[str]:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"missing report-ready CSV for TDCC font contract: {path.as_posix()}")
    frame = pd.read_csv(path, dtype=str)
    if "signal_date" not in frame.columns:
        raise RuntimeError(f"TDCC report-ready CSV missing signal_date: {path.as_posix()}")
    return sorted({safe_str(value) for value in frame["signal_date"].dropna() if safe_str(value)})


def resolve_signal_date() -> str:
    highlight_dates = read_signal_dates(HIGHLIGHT_FOR_REPORT_CSV)
    full_dates = read_signal_dates(FULL_FOR_REPORT_CSV)
    if len(highlight_dates) != 1 or len(full_dates) != 1 or highlight_dates != full_dates:
        raise RuntimeError(
            "TDCC font contract requires one consistent report-ready signal_date; "
            f"highlight={highlight_dates}, full={full_dates}"
        )
    signal_date = highlight_dates[0]
    if not re.fullmatch(r"\d{8}", signal_date):
        raise RuntimeError(f"TDCC font contract signal_date must be YYYYMMDD, got: {signal_date!r}")
    return signal_date


def delivery_pdf_path(report_kind: str, signal_date: str) -> Path:
    if report_kind == "highlight":
        return DELIVERY_PDF_DIR / f"{DELIVERY_HIGHLIGHT_PDF_PREFIX}_{signal_date}.pdf"
    if report_kind == "full":
        return DELIVERY_PDF_DIR / f"{DELIVERY_FULL_PDF_PREFIX}_{signal_date}.pdf"
    raise ValueError(f"unsupported report kind: {report_kind}")


def main() -> None:
    signal_date = resolve_signal_date()
    paths = [
        HIGHLIGHT_PDF,
        FULL_PDF,
        delivery_pdf_path("highlight", signal_date),
        delivery_pdf_path("full", signal_date),
    ]
    result = validate_tdcc_weekly_pdf_font_contract(paths)
    print(
        json.dumps(
            {
                "status": "pass",
                "signal_date": signal_date,
                "font_contract": result,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
