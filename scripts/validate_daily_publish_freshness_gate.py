from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd


DEFAULT_CURRENT = Path("output/latest/data_freshness_latest.csv")


def normalize_date(value: object) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    digits = re.sub(r"[^0-9]", "", str(value).strip())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def is_true(value: object) -> bool:
    return str(value).strip().lower() == "true"


def warrant_grace_allows_publish(row: dict[str, str]) -> bool:
    return bool(
        str(row.get("warrant_source_status", "")).strip() == "warning_grace"
        and is_true(row.get("warrant_daily_publish_allowed", ""))
        and str(row.get("warrant_pdf_visibility", "")).strip() == "hidden_unavailable"
        and not is_true(row.get("warrant_model_effect_allowed", ""))
        and not is_true(row.get("warrant_pdf_effect_allowed", ""))
    )


def read_one_row(path: Path) -> dict[str, str]:
    df = pd.read_csv(path, dtype=str).fillna("")
    if len(df) != 1:
        raise ValueError(f"{path} must contain exactly one row, got {len(df)}")
    return {str(k): str(v) for k, v in df.iloc[0].to_dict().items()}


def require_current_ready(row: dict[str, str]) -> list[str]:
    errors: list[str] = []

    main_date = normalize_date(row.get("main_price_date", ""))
    market_session_date = normalize_date(row.get("market_session_date", ""))
    expected_main_price_date = normalize_date(row.get("expected_main_price_date", ""))
    market_session_status = str(row.get("market_session_status", "")).strip()
    actual_history_date = normalize_date(row.get("actual_stock_price_history_date", ""))
    raw_official_date = normalize_date(row.get("raw_official_price_fetch_date", ""))

    if not main_date:
        errors.append("main_price_date is missing")
    if market_session_status != "open_confirmed":
        errors.append(
            "market_session_status must be open_confirmed before publishing daily artifacts: "
            f"{market_session_status or '<missing>'}"
        )
    if not expected_main_price_date:
        errors.append("expected_main_price_date is missing")
    elif main_date and main_date != expected_main_price_date:
        errors.append(
            f"main_price_date={main_date} does not match "
            f"expected_main_price_date={expected_main_price_date}"
        )
    if not market_session_date:
        errors.append("market_session_date is missing")
    elif expected_main_price_date and market_session_date != expected_main_price_date:
        errors.append(
            f"market_session_date={market_session_date} does not match "
            f"expected_main_price_date={expected_main_price_date}"
        )
    if not actual_history_date:
        errors.append("actual_stock_price_history_date is missing")
    if raw_official_date and actual_history_date and raw_official_date > actual_history_date:
        errors.append(
            "raw_official_price_fetch_date is newer than committed usable stock history "
            f"(raw_official_price_fetch_date={raw_official_date}, "
            f"actual_stock_price_history_date={actual_history_date})"
        )

    if not is_true(row.get("report_ready", "")):
        errors.append(f"report_ready must be True before publishing daily artifacts: {row.get('report_ready_note', '')}")
    if not is_true(row.get("warrant_ready", "")) and not warrant_grace_allows_publish(row):
        errors.append(
            "warrant_ready must be True before publishing daily artifacts unless bounded "
            f"warrant_unavailable grace hides warrant model/PDF effects: {row.get('warrant_ready_note', '')}"
        )
    if not is_true(row.get("daily_pdf_ready", "")):
        errors.append(
            "daily_pdf_ready must be True before publishing daily artifacts: "
            f"{row.get('daily_pdf_ready_note', '')}"
        )

    return errors


def require_no_baseline_regression(current: dict[str, str], baseline: dict[str, str]) -> list[str]:
    errors: list[str] = []

    current_main = normalize_date(current.get("main_price_date", ""))
    baseline_main = normalize_date(baseline.get("main_price_date", ""))
    if current_main and baseline_main and current_main < baseline_main:
        errors.append(f"main_price_date regressed from {baseline_main} to {current_main}")

    for field in ("report_ready", "daily_pdf_ready"):
        if is_true(baseline.get(field, "")) and not is_true(current.get(field, "")):
            errors.append(f"{field} regressed from True to {current.get(field, '')}")
    if is_true(baseline.get("warrant_ready", "")) and not is_true(current.get("warrant_ready", "")):
        if not warrant_grace_allows_publish(current):
            errors.append(f"warrant_ready regressed from True to {current.get('warrant_ready', '')}")

    baseline_history = normalize_date(baseline.get("actual_stock_price_history_date", ""))
    current_history = normalize_date(current.get("actual_stock_price_history_date", ""))
    if current_history and baseline_history and current_history < baseline_history:
        errors.append(
            "actual_stock_price_history_date regressed "
            f"from {baseline_history} to {current_history}"
        )

    return errors


def validate_daily_publish_freshness(
    current_path: Path,
    baseline_path: Path | None,
) -> list[str]:
    current = read_one_row(current_path)
    errors = require_current_ready(current)

    if baseline_path is not None and baseline_path.exists():
        baseline = read_one_row(baseline_path)
        errors.extend(require_no_baseline_regression(current, baseline))
    elif baseline_path is not None:
        errors.append(f"baseline freshness file is missing: {baseline_path}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Block daily_full_pipeline from publishing stale or regressed latest artifacts."
    )
    parser.add_argument("--current", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--baseline", type=Path, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.current.exists():
        print(f"ERROR: current freshness file is missing: {args.current}")
        return 1

    try:
        errors = validate_daily_publish_freshness(args.current, args.baseline)
    except Exception as exc:
        print(f"ERROR: daily publish freshness gate failed to read inputs: {exc}")
        return 1

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"daily publish freshness gate passed: {args.current}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
