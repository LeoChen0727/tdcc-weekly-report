from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, now_text, safe_str, write_csv  # noqa: E402
from update_event_catalyst_data import (  # noqa: E402
    COMPANY_THEME_COLUMNS,
    COMPANY_THEME_MAPPING,
    EVENT_CATALYST_COLUMNS,
    EVENT_CATALYST_LOG,
    QUARTERLY_CATALYST,
    QUARTERLY_CATALYST_COLUMNS,
    THEME_EVENT_CALENDAR,
    THEME_EVENT_COLUMNS,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
PACKET = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
CATALYST_SUMMARY_MD = LATEST_DIR / "catalyst_summary_latest.md"
CATALYST_SUMMARY_CSV = LATEST_DIR / "catalyst_summary_latest.csv"
CATALYST_PERFORMANCE = Path("output/history/catalyst_performance/catalyst_performance.csv")
CATALYST_NEEDS_REVIEW_CSV = LATEST_DIR / "catalyst_needs_review_latest.csv"
CATALYST_NEEDS_REVIEW_MD = LATEST_DIR / "catalyst_needs_review_latest.md"
VALIDATION_MD = LATEST_DIR / "catalyst_layer_validation_latest.md"
VALIDATION_JSON = LATEST_DIR / "catalyst_layer_validation_latest.json"

ALL_CANDIDATES_REQUIRED = {
    "theme_strength_score",
    "catalyst_strength_score",
    "catalyst_tags",
    "event_catalyst_tags",
    "fundamental_catalyst_tags",
    "price_reaction_level",
    "low_reaction_after_catalyst",
    "already_reacted_to_catalyst",
    "catalyst_overheated",
    "similar_to_shihsinko_flag",
    "event_calendar_tags",
    "event_proximity_score",
    "nearest_event_date",
    "nearest_event_type",
}

PERFORMANCE_REQUIRED = {
    "event_date",
    "stock_id",
    "event_type",
    "catalyst_strength",
    "catalyst_confidence",
    "return_d1",
    "return_d3",
    "return_d5",
    "return_d10",
    "return_d20",
    "relative_return_vs_benchmark_d5",
    "relative_return_vs_benchmark_d20",
    "mfe_d10",
    "mae_d10",
    "tdcc_status_at_event",
    "price_reaction_level",
    "success_label",
}

NEEDS_REVIEW_REQUIRED = {
    "item_id",
    "source_area",
    "requested_data",
    "current_status",
    "owner",
    "required_evidence",
    "model_effect_allowed",
    "pdf_effect_allowed",
    "next_action",
    "source_url",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for enc in ["utf-8-sig", "utf-8", "cp950"]:
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc)
        except Exception:
            continue
    return pd.DataFrame()


def check_schema(path: Path, required: list[str], errors: list[str]) -> int:
    if not path.exists():
        errors.append(f"missing data table: {path.as_posix()}")
        return 0
    df = read_csv(path)
    missing = set(required) - set(df.columns)
    if missing:
        errors.append(f"{path.as_posix()} missing columns: {sorted(missing)}")
    return len(df)


def truthy_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes", "y"])


def validate_all_candidates(errors: list[str]) -> int:
    if not ALL_CANDIDATES.exists():
        errors.append(f"missing {ALL_CANDIDATES.as_posix()}")
        return 0
    df = read_csv(ALL_CANDIDATES)
    missing = ALL_CANDIDATES_REQUIRED - set(df.columns)
    if missing:
        errors.append(f"all_candidates missing catalyst columns: {sorted(missing)}")
        return len(df)
    similar = df[truthy_series(df["similar_to_shihsinko_flag"])]
    if similar.empty:
        return len(df)
    if "is_construction_recognition" in similar.columns:
        bad = similar[truthy_series(similar["is_construction_recognition"])]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes construction recognition rows")
    if "tdcc_accumulation_signal" in similar.columns:
        bad = similar[similar["tdcc_accumulation_signal"].astype(str).str.contains("distribution_warning", case=False, na=False)]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes TDCC distribution_warning rows")
    if "already_reacted_to_catalyst" in similar.columns:
        bad = similar[truthy_series(similar["already_reacted_to_catalyst"])]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes already_reacted_to_catalyst rows")
    if "catalyst_overheated" in similar.columns:
        bad = similar[truthy_series(similar["catalyst_overheated"])]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes catalyst_overheated rows")
    return len(df)


def validate_packet(errors: list[str]) -> None:
    if not PACKET.exists():
        errors.append(f"missing {PACKET.as_posix()}")
        return
    text = PACKET.read_text(encoding="utf-8", errors="ignore")
    required_snippets = [
        "FUNDAMENTAL / EVENT CATALYST LAYER",
        "CATALYST DATA LAYER",
        "EVENT / MACRO CALENDAR LAYER",
        "catalyst_summary_raw_url",
        "catalyst_performance_raw_url",
        "catalyst_needs_review_csv_raw_url",
        "catalyst_needs_review_md_raw_url",
        "upcoming_catalyst_calendar_raw_url",
        "DATA SOURCE PRIORITY",
    ]
    for snippet in required_snippets:
        if snippet not in text:
            errors.append(f"packet missing catalyst layer snippet: {snippet}")


def validate_outputs(errors: list[str]) -> tuple[int, int]:
    if not CATALYST_SUMMARY_MD.exists():
        errors.append(f"missing {CATALYST_SUMMARY_MD.as_posix()}")
    if not CATALYST_SUMMARY_CSV.exists():
        errors.append(f"missing {CATALYST_SUMMARY_CSV.as_posix()}")
    if not CATALYST_PERFORMANCE.exists():
        errors.append(f"missing {CATALYST_PERFORMANCE.as_posix()}")
        return 0, 0
    perf = read_csv(CATALYST_PERFORMANCE)
    missing = PERFORMANCE_REQUIRED - set(perf.columns)
    if missing:
        errors.append(f"catalyst_performance missing columns: {sorted(missing)}")
    summary = read_csv(CATALYST_SUMMARY_CSV)
    return len(perf), len(summary)


def validate_needs_review(errors: list[str]) -> int:
    if not CATALYST_NEEDS_REVIEW_CSV.exists():
        errors.append(f"missing {CATALYST_NEEDS_REVIEW_CSV.as_posix()}")
        return 0
    if not CATALYST_NEEDS_REVIEW_MD.exists():
        errors.append(f"missing {CATALYST_NEEDS_REVIEW_MD.as_posix()}")
    df = read_csv(CATALYST_NEEDS_REVIEW_CSV)
    missing = NEEDS_REVIEW_REQUIRED - set(df.columns)
    if missing:
        errors.append(f"catalyst_needs_review missing columns: {sorted(missing)}")
        return len(df)
    bad_model = df[truthy_series(df["model_effect_allowed"])]
    bad_pdf = df[truthy_series(df["pdf_effect_allowed"])]
    if not bad_model.empty:
        errors.append("catalyst_needs_review contains rows allowed to affect model")
    if not bad_pdf.empty:
        errors.append("catalyst_needs_review contains rows allowed to affect PDF recommendations")
    if "company_specific_event_sources" not in set(df["item_id"].astype(str)):
        errors.append("catalyst_needs_review missing company_specific_event_sources row")
    return len(df)


def write_validation(result: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Catalyst Layer Validation",
        "",
        f"- generated_at: `{result['generated_at']}`",
        f"- status: `{result['status']}`",
        f"- schema_only: `{result['schema_only']}`",
        f"- all_candidates_rows: `{result.get('all_candidates_rows', '')}`",
        f"- catalyst_performance_rows: `{result.get('catalyst_performance_rows', '')}`",
        f"- catalyst_summary_rows: `{result.get('catalyst_summary_rows', '')}`",
        f"- catalyst_needs_review_rows: `{result.get('catalyst_needs_review_rows', '')}`",
        "",
        "## Data Tables",
        "",
        "| table | rows |",
        "|---|---:|",
    ]
    for key, rows in result.get("data_table_rows", {}).items():
        lines.append(f"| {key} | {rows} |")
    if result.get("errors"):
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {safe_str(error)}" for error in result["errors"])
    else:
        lines.extend(["", "No validation errors."])
    VALIDATION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema-only", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    data_rows = {
        "theme_event_calendar": check_schema(THEME_EVENT_CALENDAR, THEME_EVENT_COLUMNS, errors),
        "company_theme_mapping": check_schema(COMPANY_THEME_MAPPING, COMPANY_THEME_COLUMNS, errors),
        "quarterly_catalyst": check_schema(QUARTERLY_CATALYST, QUARTERLY_CATALYST_COLUMNS, errors),
        "event_catalyst_log": check_schema(EVENT_CATALYST_LOG, EVENT_CATALYST_COLUMNS, errors),
    }
    all_candidates_rows = ""
    performance_rows = ""
    summary_rows = ""
    needs_review_rows = ""
    if not args.schema_only:
        all_candidates_rows = validate_all_candidates(errors)
        performance_rows, summary_rows = validate_outputs(errors)
        needs_review_rows = validate_needs_review(errors)
        validate_packet(errors)

    result = {
        "generated_at": now_text(),
        "status": "fail" if errors else "pass",
        "schema_only": bool(args.schema_only),
        "data_table_rows": data_rows,
        "all_candidates_rows": all_candidates_rows,
        "catalyst_performance_rows": performance_rows,
        "catalyst_summary_rows": summary_rows,
        "catalyst_needs_review_rows": needs_review_rows,
        "errors": errors,
    }
    write_validation(result)
    print(f"Saved: {VALIDATION_MD}")
    print(f"Saved: {VALIDATION_JSON}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
