from __future__ import annotations

from pathlib import Path
import sys
import re

import pandas as pd


LATEST_DIR = Path("output/latest")
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
GROUP_ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"

REQUIRED_COLUMNS = [
    "generated_at",
    "main_price_date",
    "actual_stock_price_history_date",
    "stock_monitor_price_date",
    "all_candidates_date",
    "official_price_fetch_date",
    "warrant_flow_date",
    "raw_stock_monitor_price_date",
    "raw_all_candidates_date",
    "raw_official_price_fetch_date",
    "raw_warrant_flow_date",
    "report_ready",
    "report_ready_note",
    "warrant_ready",
    "warrant_ready_note",
    "daily_pdf_ready",
    "daily_pdf_ready_note",
    "stock_monitor_note",
    "all_candidates_note",
    "official_fetch_note",
    "warrant_note",
]


def bool_text(value: object) -> str:
    return str(value).strip().lower()


def is_true(value: object) -> bool:
    return bool_text(value) == "true"


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def warrant_grace_allows_publish(row: dict[str, str]) -> bool:
    return bool(
        str(row.get("warrant_source_status", "")).strip() == "warning_grace"
        and is_true(row.get("warrant_daily_publish_allowed"))
        and str(row.get("warrant_pdf_visibility", "")).strip() == "hidden_unavailable"
        and not is_true(row.get("warrant_model_effect_allowed"))
        and not is_true(row.get("warrant_pdf_effect_allowed"))
    )


RAW_THEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_ -]*$")
UNRESOLVED_THEME_VALUES = {"", "其他", "其他業", "other", "theme_unknown", "unclassified", "needs_manual_review"}


def has_cjk_text(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def unresolved_theme_value(value: object) -> bool:
    text = str(value).strip()
    if text in UNRESOLVED_THEME_VALUES:
        return True
    if text.isdigit():
        return True
    if RAW_THEME_PATTERN.fullmatch(text) and not has_cjk_text(text):
        return True
    return False


def group_rotation_theme_state() -> tuple[bool, str]:
    if not GROUP_ROTATION_CSV.exists():
        return True, "group rotation table missing; no theme rows to validate"
    try:
        df = pd.read_csv(GROUP_ROTATION_CSV, dtype=str).fillna("")
    except Exception as exc:
        return False, f"group rotation unreadable: {exc}"
    if df.empty:
        return True, "group rotation table empty; no theme rows to validate"
    required = {"theme", "theme_display_zh", "theme_resolution_status"}
    missing = sorted(required - set(df.columns))
    if missing:
        return False, f"group rotation missing theme display columns: {missing}"
    bad = df[
        df["theme_resolution_status"].astype(str).ne("resolved")
        | df["theme"].map(unresolved_theme_value)
        | df["theme_display_zh"].map(unresolved_theme_value)
    ]
    if not bad.empty:
        sample = bad[["theme", "theme_display_zh", "theme_resolution_status"]].head(5).to_dict("records")
        return False, f"group rotation has unresolved/raw theme rows: count={len(bad)} sample={sample}"
    return True, "group rotation themes resolved for PDF display"


def main() -> int:
    errors: list[str] = []

    if not DATA_FRESHNESS_CSV.exists():
        print(f"missing {DATA_FRESHNESS_CSV}")
        return 1

    try:
        df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str).fillna("")
    except Exception as exc:
        print(f"failed to read {DATA_FRESHNESS_CSV}: {exc}")
        return 1

    require(errors, len(df) == 1, "data_freshness_latest.csv must contain exactly one row")
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    require(errors, not missing, f"missing required columns: {missing}")
    if errors or df.empty:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    row = df.iloc[0].to_dict()
    main_date = str(row.get("main_price_date", "")).strip()
    all_candidates_date = str(row.get("all_candidates_date", "")).strip()
    official_date = str(row.get("official_price_fetch_date", "")).strip()
    warrant_date = str(row.get("warrant_flow_date", "")).strip()

    report_ready = is_true(row.get("report_ready"))
    warrant_ready = is_true(row.get("warrant_ready"))
    daily_pdf_ready = is_true(row.get("daily_pdf_ready"))

    expected_report_ready = bool(
        main_date
        and all_candidates_date == main_date
        and (not official_date or official_date == main_date)
    )
    warrant_ready_note = str(row.get("warrant_ready_note", ""))
    warrant_data_unavailable = "stock-level warrant data is unavailable" in warrant_ready_note
    expected_warrant_ready = bool(
        main_date
        and warrant_date
        and warrant_date == main_date
        and not warrant_data_unavailable
    )
    expected_warrant_publish_allowed = expected_warrant_ready or warrant_grace_allows_publish(row)
    group_rotation_theme_ready, group_rotation_theme_note = group_rotation_theme_state()
    expected_daily_pdf_ready = expected_report_ready and expected_warrant_publish_allowed and group_rotation_theme_ready

    require(
        errors,
        report_ready == expected_report_ready,
        f"report_ready={report_ready} expected {expected_report_ready}",
    )
    require(
        errors,
        warrant_ready == expected_warrant_ready,
        f"warrant_ready={warrant_ready} expected {expected_warrant_ready}",
    )
    require(
        errors,
        daily_pdf_ready == expected_daily_pdf_ready,
        f"daily_pdf_ready={daily_pdf_ready} expected {expected_daily_pdf_ready} ({group_rotation_theme_note})",
    )

    for col in ("report_ready_note", "warrant_ready_note", "daily_pdf_ready_note"):
        require(errors, bool(str(row.get(col, "")).strip()), f"{col} must not be empty")

    if not expected_warrant_ready:
        require(
            errors,
            "warrant_flow_date" in warrant_ready_note
            or "missing" in warrant_ready_note
            or "unavailable" in warrant_ready_note
            or "observe-only" in warrant_ready_note,
            "stale/missing/unavailable warrant state must be explicit in warrant_ready_note",
        )
        if expected_warrant_publish_allowed:
            require(
                errors,
                "warrant source unavailable within bounded grace" in str(row.get("daily_pdf_ready_note", "")),
                "bounded warrant grace must be explicit in daily_pdf_ready_note",
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "data_freshness validation passed: "
        f"main_price_date={main_date}, "
        f"report_ready={report_ready}, "
        f"warrant_ready={warrant_ready}, "
        f"daily_pdf_ready={daily_pdf_ready}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
