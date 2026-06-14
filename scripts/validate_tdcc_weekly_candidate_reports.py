from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd


LATEST_DIR = Path("output/latest")
VALIDATION_MD = LATEST_DIR / "tdcc_weekly_candidate_report_validation_latest.md"
VALIDATION_JSON = LATEST_DIR / "tdcc_weekly_candidate_report_validation_latest.json"

WEEKLY_INCREASE_CSV = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.csv"
CONSECUTIVE_CSV = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.csv"
MODEL_CROSS_CSV = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.csv"
HIGHLIGHT_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_highlight_for_report_latest.csv"
FULL_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_full_for_report_latest.csv"
HIGHLIGHT_PDF = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.pdf"
FULL_PDF = LATEST_DIR / "tdcc_weekly_candidate_full_latest.pdf"

EFFECTIVE_INCREASE_THRESHOLD = 0.5
LOW_VOLUME_MA20_LOTS_THRESHOLD = 1000.0
LOW_VOLUME_PENALTY = 10.0
HIGH_PAIR_STREAK_BONUS_STEP = 5.0
HIGH_PAIR_STREAK_BONUS_CAP = 20.0

HIGHLIGHT_SECTION_LIMIT = 10
FULL_SECTION_LIMIT = 50
ALLOWED_MODEL_CROSS_IDS = {"tdcc_short_term_continuation_d5_d10"}
EXPECTED_SECTIONS = {
    "weekly_increase",
    "consecutive_accumulation",
    "model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10",
    "model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10",
}
DELTA_COLS = [
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
]
REQUIRED_REPORT_COLUMNS = [
    "report_kind",
    "section_id",
    "section_name_zh",
    "section_rank",
    "tdcc_list_type",
    "tdcc_rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "tdcc_score",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
    "tdcc_weighted_weekly_increase_score",
    "tdcc_effective_increase_count",
    "tdcc_sync_bonus",
    "tdcc_theme_bonus",
    "volume_ma20_lots",
    "tdcc_low_volume_penalty",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_high_pair_streak_bonus",
]
REQUIRED_RANKING_COLUMNS = [
    "rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    *DELTA_COLS,
    "tdcc_weighted_weekly_increase_score",
    "tdcc_effective_increase_count",
    "tdcc_sync_bonus",
    "tdcc_theme_bonus",
    "volume_ma20_lots",
    "tdcc_low_volume_penalty",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_high_pair_streak_bonus",
]


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    return "" if text.lower() in {"nan", "none", "nat", "<na>"} else text


def read_csv(path: Path, errors: list[str]) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 0:
        errors.append(f"missing or empty file: {path.as_posix()}")
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str)
    except Exception as exc:
        errors.append(f"failed to read CSV {path.as_posix()}: {exc}")
        return pd.DataFrame()


def require_columns(df: pd.DataFrame, columns: list[str], label: str, errors: list[str]) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        errors.append(f"{label} missing columns: {', '.join(missing)}")


def to_number(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def score_sync_bonus(count: pd.Series) -> pd.Series:
    return count.map({4: 15.0, 3: 10.0, 2: 5.0}).fillna(0.0)


def score_high_pair_streak_bonus(streak: pd.Series) -> pd.Series:
    bonus = (streak - 1) * HIGH_PAIR_STREAK_BONUS_STEP
    return bonus.where(streak >= 2, 0.0).clip(upper=HIGH_PAIR_STREAK_BONUS_CAP)


def check_close(
    df: pd.DataFrame,
    expected: pd.Series,
    actual_col: str,
    label: str,
    errors: list[str],
    tolerance: float = 0.01,
) -> None:
    actual = to_number(df[actual_col]).fillna(0).round(2)
    mismatch = (expected.round(2) - actual).abs() > tolerance
    if mismatch.any():
        examples = []
        for _, row in df[mismatch].head(8).iterrows():
            examples.append(f"{safe_str(row.get('stock_id'))}:{safe_str(row.get(actual_col))}")
        errors.append(f"{label} has {int(mismatch.sum())} score mismatches: {', '.join(examples)}")


def validate_score_formulas(df: pd.DataFrame, label: str, errors: list[str]) -> None:
    if df.empty:
        return
    require_columns(df, REQUIRED_RANKING_COLUMNS, label, errors)
    if any(col not in df.columns for col in REQUIRED_RANKING_COLUMNS):
        return

    change_400 = to_number(df["tdcc_1w_change_400"]).fillna(0)
    change_600 = to_number(df["tdcc_1w_change_600"]).fillna(0)
    change_800 = to_number(df["tdcc_1w_change_800"]).fillna(0)
    change_1000 = to_number(df["tdcc_1w_change_1000"]).fillna(0)
    weighted = (change_1000 * 4 + change_800 * 3 + change_600 * 2 + change_400).round(2)
    effective_count = sum((to_number(df[col]).fillna(0) > EFFECTIVE_INCREASE_THRESHOLD).astype(int) for col in DELTA_COLS)
    sync_bonus = score_sync_bonus(effective_count)
    theme_bonus = to_number(df["tdcc_theme_bonus"]).fillna(0)
    low_volume_penalty = to_number(df["tdcc_low_volume_penalty"]).fillna(0)
    high_pair_streak = to_number(df["tdcc_high_pair_effective_streak_weeks"]).fillna(0)
    high_pair_bonus = score_high_pair_streak_bonus(high_pair_streak)

    check_close(df, weighted, "tdcc_weighted_weekly_increase_score", f"{label} weighted base score", errors)
    actual_effective_count = to_number(df["tdcc_effective_increase_count"]).fillna(0).astype(int)
    mismatch_count = effective_count.astype(int) != actual_effective_count
    if mismatch_count.any():
        examples = ", ".join(safe_str(row.get("stock_id")) for _, row in df[mismatch_count].head(8).iterrows())
        errors.append(f"{label} effective increase count has {int(mismatch_count.sum())} mismatches: {examples}")
    check_close(df, sync_bonus, "tdcc_sync_bonus", f"{label} sync bonus", errors)
    check_close(df, high_pair_bonus, "tdcc_high_pair_streak_bonus", f"{label} high-pair streak bonus", errors)

    volume_lots = to_number(df["volume_ma20_lots"])
    expected_low_volume_penalty = volume_lots.map(
        lambda x: LOW_VOLUME_PENALTY if not math.isnan(x) and x < LOW_VOLUME_MA20_LOTS_THRESHOLD else 0.0
    )
    check_close(df, expected_low_volume_penalty, "tdcc_low_volume_penalty", f"{label} low-volume penalty", errors)

    weekly = (weighted + sync_bonus + theme_bonus - low_volume_penalty).round(2)
    consecutive = (weighted + sync_bonus + high_pair_bonus + theme_bonus - low_volume_penalty).round(2)
    check_close(df, weekly, "tdcc_weekly_increase_score", f"{label} weekly score", errors)
    check_close(df, consecutive, "tdcc_consecutive_accumulation_score", f"{label} consecutive score", errors)


def sorted_signal_dates(df: pd.DataFrame) -> list[str]:
    if df.empty or "signal_date" not in df.columns:
        return []
    return sorted({safe_str(value) for value in df["signal_date"].dropna() if safe_str(value)})


def validate_section_ranks(report: pd.DataFrame, label: str, errors: list[str]) -> None:
    if report.empty or "section_id" not in report.columns:
        return
    for section_id, group in report.groupby("section_id", dropna=False):
        ranks = to_number(group["section_rank"]).dropna().astype(int).tolist()
        expected = list(range(1, len(ranks) + 1))
        if ranks != expected:
            errors.append(f"{label} section {section_id} ranks are not sequential 1..N")


def validate_report(
    report: pd.DataFrame,
    label: str,
    report_kind: str,
    section_limit: int,
    expected_signal_date: str,
    weekly: pd.DataFrame,
    consecutive: pd.DataFrame,
    errors: list[str],
    warnings: list[str],
) -> None:
    if report.empty:
        errors.append(f"{label} is empty")
        return
    require_columns(report, REQUIRED_REPORT_COLUMNS, label, errors)
    if any(col not in report.columns for col in REQUIRED_REPORT_COLUMNS):
        return

    bad_kind = sorted(set(report["report_kind"].dropna().map(safe_str)) - {report_kind})
    if bad_kind:
        errors.append(f"{label} has invalid report_kind values: {bad_kind}")
    signal_dates = sorted_signal_dates(report)
    if signal_dates != [expected_signal_date]:
        errors.append(f"{label} signal_date must be exactly {expected_signal_date}, got {signal_dates}")

    sections = set(report["section_id"].dropna().map(safe_str))
    missing_sections = sorted(EXPECTED_SECTIONS - sections)
    extra_sections = sorted(sections - EXPECTED_SECTIONS)
    if missing_sections:
        errors.append(f"{label} missing required sections: {', '.join(missing_sections)}")
    if extra_sections:
        errors.append(f"{label} has unexpected sections: {', '.join(extra_sections)}")

    counts = report.groupby("section_id", dropna=False).size()
    too_large = counts[counts > section_limit]
    if not too_large.empty:
        detail = ", ".join(f"{section}={count}" for section, count in too_large.items())
        errors.append(f"{label} section counts exceed {section_limit}: {detail}")
    validate_section_ranks(report, label, errors)

    ranking_sections = {
        "weekly_increase": weekly,
        "consecutive_accumulation": consecutive,
    }
    for section_id, ranking in ranking_sections.items():
        rows = report[report["section_id"].map(safe_str) == section_id]
        expected_ids = ranking.head(section_limit)["stock_id"].map(safe_str).tolist()
        actual_ids = rows.sort_values("section_rank", key=lambda s: to_number(s).fillna(999999))["stock_id"].map(safe_str).tolist()
        if actual_ids != expected_ids:
            errors.append(f"{label} {section_id} stock order does not match source ranking top {section_limit}")

    weekly_rows = report[report["section_id"].map(safe_str) == "weekly_increase"]
    weekly_effective = to_number(weekly_rows["tdcc_effective_increase_count"]).fillna(0)
    if (weekly_effective < 1).any():
        errors.append(f"{label} weekly_increase contains rows with no effective increase")

    consecutive_rows = report[report["section_id"].map(safe_str) == "consecutive_accumulation"]
    consecutive_streak = to_number(consecutive_rows["tdcc_high_pair_effective_streak_weeks"]).fillna(0)
    if (consecutive_streak < 2).any():
        bad = consecutive_rows[consecutive_streak < 2]
        examples = ", ".join(f"{safe_str(row.get('stock_id'))}:{safe_str(row.get('tdcc_high_pair_effective_streak_weeks'))}" for _, row in bad.head(8).iterrows())
        errors.append(f"{label} consecutive_accumulation contains rows below 2-week 800/1000 effective streak: {examples}")

    model_rows = report[report["section_id"].map(safe_str).str.startswith("model_cross_")]
    bad_models = sorted(set(model_rows["model_id"].dropna().map(safe_str)) - ALLOWED_MODEL_CROSS_IDS)
    if bad_models:
        errors.append(f"{label} has unsupported model cross ids: {', '.join(bad_models)}")

    for section_id in EXPECTED_SECTIONS:
        if section_id in sections and counts.get(section_id, 0) == 0:
            warnings.append(f"{label} section {section_id} has no rows")


def validate_pdfs(errors: list[str]) -> None:
    for path in [HIGHLIGHT_PDF, FULL_PDF]:
        if not path.exists() or path.stat().st_size < 10_000:
            errors.append(f"missing or too-small TDCC PDF: {path.as_posix()}")


def write_validation(result: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# TDCC Weekly Candidate Report Validation",
        "",
        f"- status: {result['status']}",
        f"- signal_date: {result.get('signal_date', '')}",
        f"- error_count: {len(result['errors'])}",
        f"- warning_count: {len(result['warnings'])}",
        "",
        "## Report Row Counts",
        "",
    ]
    counts = result.get("row_counts", {})
    if counts:
        for name, count in counts.items():
            lines.append(f"- {name}: {count}")
    else:
        lines.append("- none")
    lines.extend(["", "## Errors", ""])
    lines.extend([f"- {item}" for item in result["errors"]] or ["- none"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in result["warnings"]] or ["- none"])
    VALIDATION_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    weekly = read_csv(WEEKLY_INCREASE_CSV, errors)
    consecutive = read_csv(CONSECUTIVE_CSV, errors)
    model_cross = read_csv(MODEL_CROSS_CSV, errors)
    highlight = read_csv(HIGHLIGHT_FOR_REPORT_CSV, errors)
    full = read_csv(FULL_FOR_REPORT_CSV, errors)

    validate_score_formulas(weekly, "weekly increase ranking", errors)
    validate_score_formulas(consecutive, "consecutive accumulation ranking", errors)

    consecutive_streak = to_number(consecutive.get("tdcc_high_pair_effective_streak_weeks", pd.Series(dtype=str))).fillna(0)
    if not consecutive.empty and (consecutive_streak < 2).any():
        errors.append("consecutive accumulation source ranking contains rows below 2-week 800/1000 effective streak")

    signal_date_sets = {
        "weekly": sorted_signal_dates(weekly),
        "consecutive": sorted_signal_dates(consecutive),
        "highlight": sorted_signal_dates(highlight),
        "full": sorted_signal_dates(full),
    }
    unique_dates = {tuple(value) for value in signal_date_sets.values()}
    signal_date = ""
    if len(unique_dates) == 1:
        only = next(iter(unique_dates))
        if len(only) == 1:
            signal_date = only[0]
    if not signal_date:
        errors.append(f"weekly candidate outputs must share exactly one signal_date, got {signal_date_sets}")

    if not model_cross.empty:
        require_columns(model_cross, ["tdcc_list_type", "tdcc_rank", "stock_id", "model_id"], "model cross summary", errors)
        bad_models = sorted(set(model_cross.get("model_id", pd.Series(dtype=str)).dropna().map(safe_str)) - ALLOWED_MODEL_CROSS_IDS)
        if bad_models:
            errors.append(f"model cross summary has unsupported model ids: {', '.join(bad_models)}")

    if signal_date:
        validate_report(highlight, "highlight report-ready CSV", "highlight", HIGHLIGHT_SECTION_LIMIT, signal_date, weekly, consecutive, errors, warnings)
        validate_report(full, "full report-ready CSV", "full", FULL_SECTION_LIMIT, signal_date, weekly, consecutive, errors, warnings)
    validate_pdfs(errors)

    row_counts = {
        "weekly_increase": int(len(weekly)),
        "consecutive_accumulation": int(len(consecutive)),
        "model_cross": int(len(model_cross)),
        "highlight_report": int(len(highlight)),
        "full_report": int(len(full)),
    }
    result: dict[str, Any] = {
        "status": "pass" if not errors else "fail",
        "signal_date": signal_date,
        "row_counts": row_counts,
        "errors": errors,
        "warnings": warnings,
    }
    write_validation(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
