from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repair_tdcc_weekly_history_continuity import load_continuity_report
from tdcc_stock_history_utils import (
    THRESHOLDS,
    consecutive_up_weeks,
    normalize_code,
    normalize_date,
    read_csv,
    safe_str,
    to_number,
)
from tdcc_weekly_data_readiness import load_readiness


HISTORY_DIR = Path("output/history/tdcc")
STOCK_HISTORY_DIR = Path("data/tdcc_stock_history")


def snapshot_path(date: str) -> Path:
    return HISTORY_DIR / f"tdcc_holder_ratio_{normalize_date(date)}.csv"


def load_snapshot(date: str) -> pd.DataFrame:
    frame = read_csv(snapshot_path(date), dtype=str)
    if frame.empty or "code" not in frame.columns:
        return pd.DataFrame()
    frame["code"] = frame["code"].map(normalize_code)
    return frame.drop_duplicates("code", keep="last").set_index("code")


def close_enough(left: object, right: object, tolerance: float = 0.011) -> bool:
    left_num = to_number(left)
    right_num = to_number(right)
    if math.isnan(left_num) and math.isnan(right_num):
        return True
    if math.isnan(left_num) or math.isnan(right_num):
        return False
    return abs(left_num - right_num) <= tolerance


def validate() -> list[str]:
    errors: list[str] = []
    try:
        readiness = load_readiness()
    except Exception as exc:
        return [str(exc)]
    try:
        continuity = load_continuity_report()
    except Exception as exc:
        return [str(exc)]

    signal_date = readiness["selected_official_date"]
    if continuity.get("signal_date") != signal_date:
        errors.append(
            "continuity signal_date does not match readiness: "
            f"{continuity.get('signal_date', '')} != {signal_date}"
        )
    if continuity.get("unresolved_missing_rows") != 0:
        errors.append("continuity report contains unresolved missing rows")

    official_dates = readiness["official_dates"]
    signal_index = official_dates.index(signal_date)
    if signal_index == 0:
        return errors
    current = load_snapshot(signal_date)
    if current.empty:
        errors.append(f"current official snapshot is missing: {snapshot_path(signal_date)}")
        return errors

    comparison_snapshots: dict[int, tuple[str, pd.DataFrame]] = {}
    for weeks in (1, 2, 3):
        prior_index = signal_index - weeks
        if prior_index < 0:
            continue
        prior_date = official_dates[prior_index]
        prior = load_snapshot(prior_date)
        if prior.empty:
            errors.append(f"prior official snapshot is missing: {snapshot_path(prior_date)}")
            continue
        comparison_snapshots[weeks] = (prior_date, prior)
    if any(signal_index - weeks >= 0 and weeks not in comparison_snapshots for weeks in (1, 2, 3)):
        return errors

    accepted_exceptions = {
        (normalize_date(item.get("date", "")), normalize_code(item.get("stock_id", "")))
        for item in continuity.get("confirmed_history_exceptions", [])
    }
    for stock_id in current.index:
        history_path = STOCK_HISTORY_DIR / f"{stock_id}.csv"
        history = read_csv(history_path, dtype=str)
        if history.empty or "as_of_date" not in history.columns:
            errors.append(f"per-stock TDCC history is missing for current stock {stock_id}: {history_path}")
            continue
        history["as_of_date"] = history["as_of_date"].map(normalize_date)
        history = history.sort_values("as_of_date").reset_index(drop=True)
        current_rows = history[history["as_of_date"].eq(signal_date)]
        if current_rows.empty:
            errors.append(f"per-stock TDCC history lacks signal_date={signal_date}: {stock_id}")
            continue
        current_row = current_rows.iloc[-1]
        for weeks, (prior_date, prior) in comparison_snapshots.items():
            if stock_id not in prior.index:
                if (prior_date, stock_id) not in accepted_exceptions:
                    errors.append(
                        f"stock {stock_id} is missing from prior official period {prior_date} "
                        "without explicit history-exception evidence"
                    )
                for threshold in THRESHOLDS:
                    value = to_number(current_row.get(f"over_{threshold}_change_{weeks}w"))
                    if not math.isnan(value):
                        errors.append(
                            f"stock {stock_id} has change_{weeks}w across missing official period {prior_date}"
                        )
                continue

            for threshold in THRESHOLDS:
                expected = to_number(current.loc[stock_id].get(f"over_{threshold}_pct")) - to_number(
                    prior.loc[stock_id].get(f"over_{threshold}_pct")
                )
                actual = current_row.get(f"over_{threshold}_change_{weeks}w")
                if not close_enough(actual, expected):
                    errors.append(
                        f"stock {stock_id} over_{threshold}_change_{weeks}w does not use exact official period "
                        f"{prior_date}->{signal_date}: actual={safe_str(actual)} expected={expected:.2f}"
                    )

        ratio_cols = [f"over_{threshold}_ratio" for threshold in THRESHOLDS]
        recomputed_streak = consecutive_up_weeks(
            history,
            ratio_cols,
            int(current_rows.index[-1]),
            official_dates,
        )
        actual_streak_number = to_number(current_row.get("tdcc_consecutive_up_weeks"))
        if math.isnan(actual_streak_number):
            errors.append(f"stock {stock_id} has empty tdcc_consecutive_up_weeks")
            continue
        actual_streak = int(actual_streak_number)
        if actual_streak != recomputed_streak:
            errors.append(
                f"stock {stock_id} consecutive streak crosses a missing official period or is stale: "
                f"actual={actual_streak} expected={recomputed_streak}"
            )
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("TDCC weekly history continuity validation failed:")
        for error in errors[:100]:
            print(f"- {error}")
        if len(errors) > 100:
            print(f"- ... {len(errors) - 100} more errors")
        return 1
    readiness = load_readiness()
    continuity = load_continuity_report()
    print(
        "TDCC weekly history continuity validation passed: "
        f"signal_date={readiness['selected_official_date']} "
        f"required_dates={len(continuity['required_dates'])} "
        f"unresolved_missing_rows={continuity['unresolved_missing_rows']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
