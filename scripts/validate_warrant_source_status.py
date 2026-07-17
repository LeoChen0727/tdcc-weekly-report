from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_STATUS_JSON = Path("output/latest/warrant_source_status_latest.json")
DEFAULT_FRESHNESS_CSV = Path("output/latest/data_freshness_latest.csv")


def is_true(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def read_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def normalize_date(value: object) -> str:
    normalized = re.sub(r"[^0-9]", "", str(value or ""))
    return normalized if len(normalized) == 8 else ""


def expected_main_price_date(path: Path) -> str:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        row = next(csv.DictReader(handle), None)
    if row is None:
        raise ValueError(f"{path} is empty")
    value = normalize_date(row.get("main_price_date", ""))
    if not value:
        raise ValueError(f"{path} has no valid main_price_date")
    return value


def validate_status(
    status: dict[str, Any],
    *,
    allow_noncritical_grace: bool,
    require_formal_current: bool = False,
    expected_date: str = "",
) -> list[str]:
    errors: list[str] = []
    state = str(status.get("status", "")).strip()

    if state == "ok":
        if not require_formal_current:
            return errors
        required_true_fields = (
            "daily_publish_allowed",
            "model_effect_allowed",
            "pdf_effect_allowed",
        )
        for field in required_true_fields:
            if not is_true(status.get(field, "")):
                errors.append(f"formal current warrant status must set {field}=true")
        if str(status.get("warrant_pdf_visibility", "")).strip() != "visible":
            errors.append("formal current warrant status must set warrant_pdf_visibility=visible")

        date_fields = ("requested_date", "target_date", "data_date")
        dates = {field: normalize_date(status.get(field, "")) for field in date_fields}
        for field, value in dates.items():
            if not value:
                errors.append(f"formal current warrant status has invalid or missing {field}")
        valid_dates = {value for value in dates.values() if value}
        if len(valid_dates) > 1:
            errors.append(
                "formal current warrant status dates must match: "
                + ",".join(f"{field}={dates[field] or '<missing>'}" for field in date_fields)
            )
        normalized_expected = normalize_date(expected_date)
        if not normalized_expected:
            errors.append("formal current warrant validation requires a valid expected main price date")
        else:
            for field, value in dates.items():
                if value and value != normalized_expected:
                    errors.append(
                        f"formal current warrant {field} must equal main_price_date "
                        f"{normalized_expected}; observed={value}"
                    )
        return errors

    if state == "warning_grace" and allow_noncritical_grace:
        if not is_true(status.get("daily_publish_allowed", "")):
            errors.append("warning_grace status must set daily_publish_allowed=true")
        if str(status.get("warrant_pdf_visibility", "")).strip() != "hidden_unavailable":
            errors.append("warning_grace status must set warrant_pdf_visibility=hidden_unavailable")
        if is_true(status.get("model_effect_allowed", "")):
            errors.append("warning_grace status must not allow warrant model effect")
        if is_true(status.get("pdf_effect_allowed", "")):
            errors.append("warning_grace status must not allow formal warrant PDF effect")
        return errors

    if state == "warning_grace":
        errors.append("warrant source is unavailable and grace was not enabled")
    elif state == "failed":
        errors.append(
            "warrant source unavailable grace expired "
            f"(consecutive_unavailable_trading_days={status.get('consecutive_unavailable_trading_days', '')}, "
            f"hard_fail_after_days={status.get('hard_fail_after_days', '')})"
        )
    else:
        errors.append(f"unknown warrant source status: {state or '<missing>'}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate official warrant source availability and bounded daily-production grace."
    )
    parser.add_argument("--status", type=Path, default=DEFAULT_STATUS_JSON)
    parser.add_argument("--allow-noncritical-grace", action="store_true")
    parser.add_argument("--require-formal-current", action="store_true")
    parser.add_argument("--freshness", type=Path, default=DEFAULT_FRESHNESS_CSV)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        status = read_status(args.status)
    except Exception as exc:
        print(f"ERROR: failed to read warrant source status: {exc}")
        return 1

    expected_date = ""
    if args.require_formal_current:
        try:
            expected_date = expected_main_price_date(args.freshness)
        except Exception as exc:
            print(f"ERROR: failed to read expected main price date: {exc}")
            return 1

    errors = validate_status(
        status,
        allow_noncritical_grace=args.allow_noncritical_grace,
        require_formal_current=args.require_formal_current,
        expected_date=expected_date,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    state = str(status.get("status", "")).strip()
    if state == "warning_grace":
        print(
            "WARNING: current-date warrant source is unavailable; "
            "daily production may continue without warrant model/PDF effect during the bounded grace window."
        )
    else:
        print(f"warrant source status validation passed: {state}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
