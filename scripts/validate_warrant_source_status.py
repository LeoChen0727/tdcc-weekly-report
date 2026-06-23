from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_STATUS_JSON = Path("output/latest/warrant_source_status_latest.json")


def is_true(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def read_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def validate_status(status: dict[str, Any], *, allow_noncritical_grace: bool) -> list[str]:
    errors: list[str] = []
    state = str(status.get("status", "")).strip()

    if state == "ok":
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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        status = read_status(args.status)
    except Exception as exc:
        print(f"ERROR: failed to read warrant source status: {exc}")
        return 1

    errors = validate_status(status, allow_noncritical_grace=args.allow_noncritical_grace)
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
