from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/volume_breakout")

REQUIRED_FILES = [
    LATEST_DIR / "volume_breakout_watch_latest.csv",
    LATEST_DIR / "volume_breakout_watch_latest.md",
    LATEST_DIR / "volume_breakout_backtest_latest.csv",
    LATEST_DIR / "volume_breakout_backtest_latest.md",
    LATEST_DIR / "volume_breakout_chatgpt_packet_latest.md",
    HISTORY_DIR / "volume_breakout_event_log.csv",
]

WATCH_REQUIRED_COLUMNS = [
    "signal_date",
    "stock_id",
    "stock_name",
    "volume_breakout_type",
    "volume_breakout_priority",
    "selection_status",
    "risk_flags",
    "next_volume_breakout_confirmation",
]

BACKTEST_REQUIRED_COLUMNS = [
    "group_name",
    "group_value",
    "sample_count",
    "mature_d5_count",
    "avg_return_d5",
    "win_rate_d5",
    "sample_status",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def line_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(text.splitlines())


def check_multiline_markdown(path: Path) -> None:
    if line_count(path) <= 5:
        fail(f"{path} is suspiciously short or single-line")


def check_csv(path: Path, required_columns: list[str], allow_empty: bool = False) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        fail(f"{path} missing columns: {missing}")
    if not allow_empty and df.empty:
        fail(f"{path} has no rows")
    return df


def main() -> int:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"missing required file: {path}")
        if path.suffix.lower() == ".md":
            check_multiline_markdown(path)

    watch = check_csv(LATEST_DIR / "volume_breakout_watch_latest.csv", WATCH_REQUIRED_COLUMNS, allow_empty=True)
    backtest = check_csv(LATEST_DIR / "volume_breakout_backtest_latest.csv", BACKTEST_REQUIRED_COLUMNS, allow_empty=False)
    events = check_csv(HISTORY_DIR / "volume_breakout_event_log.csv", ["event_date", "stock_id", "volume_breakout_type", "mature_d5"], allow_empty=False)

    if not watch.empty:
        valid_priorities = {"A_valid_breakout_watch", "B_confirm_needed", "C_watch_only", "D_risk_downgrade"}
        bad = sorted(set(watch["volume_breakout_priority"]) - valid_priorities)
        if bad:
            fail(f"invalid volume_breakout_priority values: {bad}")

    if "sample_status" in backtest.columns:
        bad_status = sorted(set(backtest["sample_status"]) - {"ok", "insufficient_sample", "pending_only", "data_missing", ""})
        if bad_status:
            fail(f"invalid sample_status values: {bad_status}")

    print(f"Volume breakout validation passed: watch_rows={len(watch)}, backtest_rows={len(backtest)}, event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
