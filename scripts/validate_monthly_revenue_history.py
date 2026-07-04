from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_monthly_revenue_history import (  # noqa: E402
    DOCS_LATEST_CSV,
    DOCS_LATEST_MD,
    HISTORY_CSV,
    HISTORY_ID,
    HISTORY_VERSION,
    LATEST_CSV,
    LATEST_MD,
    OUTPUT_COLUMNS,
    SOURCE_STATUS_JSON,
)


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_POINT_IN_TIME_STATUS = {"ready_official_source_table_date"}
VALID_MARKETS = {"listed", "otc"}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_mirror(errors: list[str]) -> None:
    for left, right in [(HISTORY_CSV, LATEST_CSV), (LATEST_CSV, DOCS_LATEST_CSV), (LATEST_MD, DOCS_LATEST_MD)]:
        if not left.exists():
            errors.append(f"missing monthly revenue artifact: {left.as_posix()}")
            continue
        if not right.exists():
            errors.append(f"missing monthly revenue mirror: {right.as_posix()}")
            continue
        if left.read_bytes() != right.read_bytes():
            errors.append(f"monthly revenue mirror differs: {right.as_posix()}")


def validate_source_status(errors: list[str]) -> None:
    if not SOURCE_STATUS_JSON.exists():
        errors.append(f"missing source status json: {SOURCE_STATUS_JSON.as_posix()}")
        return
    try:
        data = json.loads(SOURCE_STATUS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"source status json is not valid JSON: {exc}")
        return
    if not isinstance(data, list) or not data:
        errors.append("source status json must contain a non-empty list")
        return
    markets = {str(item.get("market", "")) for item in data if isinstance(item, dict)}
    missing = VALID_MARKETS - markets
    if missing:
        errors.append(f"source status missing markets: {sorted(missing)}")
    for item in data:
        if not isinstance(item, dict):
            errors.append("source status row must be an object")
            continue
        if str(item.get("status", "")) != "ok":
            errors.append(f"source status is not ok for {item.get('market')}: {item.get('status')}")
        if int(item.get("standardized_rows") or 0) <= 0:
            errors.append(f"source status has no standardized rows for {item.get('market')}")


def validate_history(
    history: pd.DataFrame,
    require_source_files: bool = True,
    require_all_markets: bool = True,
) -> list[str]:
    errors: list[str] = []
    missing = set(OUTPUT_COLUMNS) - set(history.columns)
    if missing:
        errors.append(f"monthly revenue history missing columns: {sorted(missing)}")
        return errors
    if history.empty:
        errors.append("monthly revenue history is empty")
        return errors

    if set(history["history_id"].astype(str)) != {HISTORY_ID}:
        errors.append("monthly revenue history has unexpected history_id values")
    if set(history["history_version"].astype(str)) != {HISTORY_VERSION}:
        errors.append("monthly revenue history has unexpected history_version values")

    markets = set(history["market"].astype(str))
    if markets - VALID_MARKETS:
        errors.append(f"monthly revenue history has unexpected markets: {sorted(markets - VALID_MARKETS)}")
    if require_all_markets and not VALID_MARKETS <= markets:
        errors.append(f"monthly revenue history must include listed and otc markets, got {sorted(markets)}")

    duplicated = history.duplicated(["market", "stock_id", "revenue_period"], keep=False)
    if duplicated.any():
        errors.append("monthly revenue history must be unique by market + stock_id + revenue_period")

    blank_key = history[
        history["market"].astype(str).eq("")
        | history["stock_id"].astype(str).eq("")
        | history["revenue_period"].astype(str).eq("")
        | history["source_table_date"].astype(str).eq("")
    ]
    if not blank_key.empty:
        errors.append("monthly revenue history has blank market, stock_id, revenue_period, or source_table_date")

    bad_stock_ids = history[~history["stock_id"].astype(str).str.fullmatch(r"\d{4,6}")]
    if not bad_stock_ids.empty:
        errors.append("monthly revenue history stock_id must be 4 to 6 digits")

    bad_periods = history[~history["revenue_period"].astype(str).str.fullmatch(r"20\d{4}")]
    if not bad_periods.empty:
        errors.append("monthly revenue history revenue_period must be YYYYMM")

    bad_dates = history[~history["source_table_date"].astype(str).str.fullmatch(r"20\d{6}")]
    if not bad_dates.empty:
        errors.append("monthly revenue history source_table_date must be YYYYMMDD")

    future_period = history[history["revenue_period"].astype(str).str[:6] > history["source_table_date"].astype(str).str[:6]]
    if not future_period.empty:
        errors.append("monthly revenue history revenue_period must not be after source_table_date month")

    statuses = set(history["point_in_time_status"].astype(str))
    if statuses - ALLOWED_POINT_IN_TIME_STATUS:
        errors.append(f"unexpected point_in_time_status values: {sorted(statuses - ALLOWED_POINT_IN_TIME_STATUS)}")

    if not history["research_join_allowed"].astype(str).eq("True").all():
        errors.append("monthly revenue history rows must be research_join_allowed=True")

    formal_allowed = history[history["allowed_for_formal_historical_model_use"].astype(str).eq("True")]
    if not formal_allowed.empty:
        errors.append("monthly revenue history must not claim formal model-use approval before coverage audit")

    no_blocker = history[history["formal_use_blocker"].astype(str).eq("")]
    if not no_blocker.empty:
        errors.append("monthly revenue history rows must carry formal_use_blocker")

    numeric_cols = [
        "monthly_revenue",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
    ]
    for col in numeric_cols:
        values = pd.to_numeric(history[col], errors="coerce")
        if values.notna().sum() == 0:
            errors.append(f"monthly revenue history numeric column has no numeric values: {col}")

    if require_source_files:
        missing_source = []
        for source_file in sorted(set(history["source_file"].astype(str))):
            if not source_file:
                missing_source.append(source_file)
                continue
            if not (ROOT / source_file).exists():
                missing_source.append(source_file)
        if missing_source:
            errors.append(f"monthly revenue history source_file missing: {missing_source[:5]}")

    return errors


def main() -> int:
    errors: list[str] = []
    validate_mirror(errors)
    validate_source_status(errors)
    try:
        history = read_csv(HISTORY_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing monthly revenue history: {exc}")
        history = pd.DataFrame()
    if not history.empty:
        errors.extend(validate_history(history))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_monthly_revenue_history_rows={len(history)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
