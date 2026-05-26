from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, main_price_date_from_freshness, read_csv, safe_str  # noqa: E402


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
THEME_LEADERSHIP_MD = LATEST_DIR / "daily_theme_leadership_latest.md"
TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
TWO_LINE_VIEW_MD = LATEST_DIR / "daily_candidate_two_line_view_latest.md"
VALIDATION_JSON = LATEST_DIR / "daily_theme_leadership_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_theme_leadership_validation_latest.md"


REQUIRED_THEME_COLUMNS = [
    "theme_name",
    "theme_candidate_count",
    "theme_A_candidate_count",
    "theme_B_candidate_count",
    "theme_strict_breakout_count",
    "theme_true_breakout_count",
    "theme_volume_breakout_count",
    "theme_near_high_count",
    "theme_tdcc_strong_count",
    "theme_tdcc_mild_count",
    "theme_tdcc_distribution_warning_count",
    "theme_warrant_bullish_count",
    "theme_warrant_bearish_count",
    "theme_overheated_count",
    "theme_leader_stock_id",
    "theme_leader_stock_name",
    "theme_leader_confirmed",
    "theme_breadth_score",
    "theme_strength_score",
    "theme_risk_score",
    "theme_final_status",
]

REQUIRED_CANDIDATE_COLUMNS = [
    "theme_name",
    "theme_final_status",
    "candidate_source_type",
    "candidate_line",
    "candidate_line_group",
    "two_line_overlap_flag",
    "theme_leadership_note",
]

VALID_THEME_STATUSES = {
    "mainstream_leader",
    "mainstream_follow_through",
    "emerging_theme",
    "single_name_signal",
    "weak_theme",
    "mainstream_overheated",
}

VALID_SOURCE_TYPES = {
    "mainstream_theme_candidate",
    "individual_quality_candidate",
    "latent_watch_candidate",
    "event_driven_candidate",
    "risk_downgraded_candidate",
}


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8", errors="replace").count("\n") + 1


def add_missing_column_errors(df: pd.DataFrame, required: list[str], label: str, errors: list[str]) -> None:
    missing = [col for col in required if col not in df.columns]
    if missing:
        errors.append(f"{label}: missing_columns={missing}")


def validate() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    main_date = main_price_date_from_freshness()

    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    theme = read_csv(THEME_LEADERSHIP_CSV, dtype=str, keep_default_na=False)
    two_line = read_csv(TWO_LINE_VIEW_CSV, dtype=str, keep_default_na=False)

    if candidates.empty:
        errors.append(f"missing_or_empty: {ALL_CANDIDATES}")
    else:
        add_missing_column_errors(candidates, REQUIRED_CANDIDATE_COLUMNS, "all_candidates", errors)
        if "category" in candidates.columns:
            categories = {safe_str(x) for x in candidates["category"].tolist() if safe_str(x)}
            forbidden = {"mainstream_leader", "mainstream_follow_through", "emerging_theme", "single_name_signal"}
            if categories.intersection(forbidden):
                errors.append("theme statuses must not be inserted as seventh daily candidate categories")
        if "theme_final_status" in candidates.columns:
            invalid_status = sorted({safe_str(x) for x in candidates["theme_final_status"].tolist() if safe_str(x) and safe_str(x) not in VALID_THEME_STATUSES})
            if invalid_status:
                errors.append(f"all_candidates: invalid_theme_final_status={invalid_status}")
        if "candidate_source_type" in candidates.columns:
            invalid_source = sorted({safe_str(x) for x in candidates["candidate_source_type"].tolist() if safe_str(x) and safe_str(x) not in VALID_SOURCE_TYPES})
            if invalid_source:
                errors.append(f"all_candidates: invalid_candidate_source_type={invalid_source}")

        if {"stock_id", "candidate_line_group"}.issubset(candidates.columns):
            lianqiang = candidates[candidates["stock_id"].astype(str).str.zfill(4).eq("2347")]
            if not lianqiang.empty:
                bad = lianqiang[lianqiang["candidate_line_group"].isin(["mainstream_leader_stock", "mainstream_follow_through_stock"])]
                if not bad.empty:
                    errors.append("2347 stale/non-confirmed rows must not be placed in mainstream fund line")
                if not lianqiang["candidate_line_group"].isin(["individual_revenue_low_response_watch", "individual_tdcc_latent_watch", "individual_pattern_watch", "risk"]).any():
                    warnings.append("2347 exists but was not found in an expected individual/latent/risk line group")

    if theme.empty:
        errors.append(f"missing_or_empty: {THEME_LEADERSHIP_CSV}")
    else:
        add_missing_column_errors(theme, REQUIRED_THEME_COLUMNS, "theme_leadership", errors)
        if "theme_final_status" in theme.columns:
            invalid_status = sorted({safe_str(x) for x in theme["theme_final_status"].tolist() if safe_str(x) and safe_str(x) not in VALID_THEME_STATUSES})
            if invalid_status:
                errors.append(f"theme_leadership: invalid_theme_final_status={invalid_status}")

    if two_line.empty:
        errors.append(f"missing_or_empty: {TWO_LINE_VIEW_CSV}")
    else:
        add_missing_column_errors(two_line, REQUIRED_CANDIDATE_COLUMNS, "two_line_view", errors)
        if "two_line_overlap_flag" in two_line.columns and not two_line["two_line_overlap_flag"].astype(str).isin(["True", "False", ""]).all():
            errors.append("two_line_view: two_line_overlap_flag must be True/False")

    for path in [THEME_LEADERSHIP_MD, TWO_LINE_VIEW_MD]:
        if not path.exists():
            errors.append(f"missing_file: {path}")
        elif line_count(path) <= 10:
            errors.append(f"suspicious_markdown_too_short: {path}")

    result = {
        "status": "pass" if not errors else "fail",
        "main_price_date": main_date,
        "theme_rows": 0 if theme.empty else int(len(theme)),
        "two_line_rows": 0 if two_line.empty else int(len(two_line)),
        "all_candidate_rows": 0 if candidates.empty else int(len(candidates)),
        "errors": errors,
        "warnings": warnings,
    }
    return result


def write_report(result: dict[str, Any]) -> None:
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Daily Theme Leadership Layer Validation",
        "",
        f"- status: `{result['status']}`",
        f"- main_price_date: `{result['main_price_date']}`",
        f"- theme_rows: `{result['theme_rows']}`",
        f"- two_line_rows: `{result['two_line_rows']}`",
        f"- all_candidate_rows: `{result['all_candidate_rows']}`",
        "",
        "## Errors",
        "",
    ]
    errors = result.get("errors") or []
    lines.extend([f"- {err}" for err in errors] if errors else ["- none"])
    lines.extend(["", "## Warnings", ""])
    warnings = result.get("warnings") or []
    lines.extend([f"- {warn}" for warn in warnings] if warnings else ["- none"])
    lines.append("")
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result = validate()
    write_report(result)
    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    if result["errors"]:
        for error in result["errors"]:
            print(f"ERROR: {error}")
        return 1
    print("Daily theme leadership layer validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
