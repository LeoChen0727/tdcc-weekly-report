from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_market_sentiment_context import REQUIRED_CONTEXT_COLUMNS  # noqa: E402
from tracking_utils import HISTORY_DIR, LATEST_DIR, main_price_date_from_freshness  # noqa: E402


LATEST_CSV = LATEST_DIR / "market_sentiment_context_latest.csv"
LATEST_MD = LATEST_DIR / "market_sentiment_context_latest.md"
MARKET_RISK_DASHBOARD_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
MARKET_TIMING_PACKET_MD = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"

HISTORY_DIR_MARKET_RISK = HISTORY_DIR / "market_risk"
HISTORY_FILES = [
    HISTORY_DIR_MARKET_RISK / "market_sentiment_context_history.csv",
    HISTORY_DIR_MARKET_RISK / "vix_history.csv",
    HISTORY_DIR_MARKET_RISK / "retail_mtx_sentiment_history.csv",
    HISTORY_DIR_MARKET_RISK / "futures_options_indicators_history.csv",
]


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _packet_main_price_date(text: str) -> str:
    match = re.search(r"(?m)^-\s*main_price_date:\s*`?(\d{8})`?\s*$", text)
    return match.group(1) if match else ""


def main() -> None:
    errors: list[str] = []

    required_paths = [LATEST_CSV, LATEST_MD, MARKET_RISK_DASHBOARD_MD, MARKET_TIMING_PACKET_MD, *HISTORY_FILES]
    for path in required_paths:
        if not path.exists():
            errors.append(f"missing file: {path}")

    if LATEST_CSV.exists():
        df = pd.read_csv(LATEST_CSV, dtype=str).fillna("")
        expected_main_date = main_price_date_from_freshness()
        if len(df) != 1:
            errors.append(f"{LATEST_CSV} must have exactly 1 row, got {len(df)}")
        missing_cols = [col for col in REQUIRED_CONTEXT_COLUMNS if col not in df.columns]
        if missing_cols:
            errors.append(f"{LATEST_CSV} missing columns: {missing_cols}")
        if not df.empty:
            row = df.iloc[0].to_dict()
            if expected_main_date and row.get("date", "") != expected_main_date:
                errors.append(
                    f"{LATEST_CSV} date mismatch: expected {expected_main_date}, got {row.get('date', '')}"
                )
            sample_status = row.get("sample_status", "")
            combined = row.get("combined_sentiment_interpretation", "")
            warning = row.get("sentiment_warning_level", "")
            note = row.get("data_quality_note", "")
            retail_interp = row.get("retail_mtx_index_interpretation", "")
            vix_interp = row.get("vix_index_interpretation", "")
            if sample_status == "insufficient_history":
                if "資料不足 / 僅能觀察" not in note:
                    errors.append("insufficient_history must include 資料不足 / 僅能觀察 in data_quality_note")
                if combined != "insufficient_history_observe_only":
                    errors.append(
                        "insufficient_history must set combined_sentiment_interpretation="
                        "insufficient_history_observe_only"
                    )
                if warning != "insufficient":
                    errors.append("insufficient_history must set sentiment_warning_level=insufficient")
            if "insufficient_history" in retail_interp or "insufficient_history" in vix_interp:
                if combined != "insufficient_history_observe_only":
                    errors.append("any insufficient VIX/retail interpretation must force combined insufficient")

    latest_md = _read_text(LATEST_MD)
    if LATEST_MD.exists() and "Market Sentiment Context" not in latest_md:
        errors.append(f"{LATEST_MD} missing Market Sentiment Context heading")
    if LATEST_CSV.exists() and LATEST_MD.exists():
        df = pd.read_csv(LATEST_CSV, dtype=str).fillna("")
        if not df.empty and df.iloc[0].get("sample_status") == "insufficient_history":
            if "資料不足 / 僅能觀察" not in latest_md:
                errors.append(f"{LATEST_MD} must state 資料不足 / 僅能觀察")

    dashboard = _read_text(MARKET_RISK_DASHBOARD_MD)
    for heading in [
        "VIX Historical Context",
        "Retail MTX Historical Context",
        "Combined Sentiment Interpretation",
    ]:
        if MARKET_RISK_DASHBOARD_MD.exists() and heading not in dashboard:
            errors.append(f"{MARKET_RISK_DASHBOARD_MD} missing heading: {heading}")

    packet = _read_text(MARKET_TIMING_PACKET_MD)
    if MARKET_TIMING_PACKET_MD.exists() and "MARKET_SENTIMENT_CONTEXT" not in packet:
        errors.append(f"{MARKET_TIMING_PACKET_MD} missing MARKET_SENTIMENT_CONTEXT")
    if MARKET_TIMING_PACKET_MD.exists():
        expected_main_date = main_price_date_from_freshness()
        packet_main_date = _packet_main_price_date(packet)
        if expected_main_date and packet_main_date != expected_main_date:
            errors.append(
                f"{MARKET_TIMING_PACKET_MD} main_price_date mismatch: "
                f"expected {expected_main_date}, got {packet_main_date or 'missing'}"
            )

    if errors:
        print("Market sentiment context validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Market sentiment context validation passed.")


if __name__ == "__main__":
    main()
