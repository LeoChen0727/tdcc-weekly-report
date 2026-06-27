from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tdcc_weekly_pdf_font_contract import validate_tdcc_weekly_pdf_font_contract  # noqa: E402


LATEST_DIR = Path("output/latest")
VALIDATION_MD = LATEST_DIR / "tdcc_weekly_candidate_report_validation_latest.md"
VALIDATION_JSON = LATEST_DIR / "tdcc_weekly_candidate_report_validation_latest.json"

WEEKLY_INCREASE_CSV = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.csv"
CONSECUTIVE_CSV = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.csv"
MODEL_CROSS_CSV = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.csv"
SECTION_MANIFEST_CSV = LATEST_DIR / "tdcc_weekly_report_section_manifest_latest.csv"
HIGHLIGHT_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_highlight_for_report_latest.csv"
FULL_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_full_for_report_latest.csv"
HIGHLIGHT_MD = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.md"
FULL_MD = LATEST_DIR / "tdcc_weekly_candidate_full_latest.md"
HIGHLIGHT_PDF = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.pdf"
FULL_PDF = LATEST_DIR / "tdcc_weekly_candidate_full_latest.pdf"
DELIVERY_HIGHLIGHT_PDF_PREFIX = "TDCC大戶籌碼週報_精華版"
DELIVERY_FULL_PDF_PREFIX = "TDCC大戶籌碼週報_完整版"
DELIVERY_PDF_DIR = LATEST_DIR / "published_reports" / "tdcc_weekly"

EFFECTIVE_INCREASE_THRESHOLD = 0.5
LOW_VOLUME_MA20_LOTS_THRESHOLD = 1000.0
LOW_VOLUME_PENALTY = 10.0
HIGH_PAIR_STREAK_BONUS_STEP = 5.0
HIGH_PAIR_STREAK_BONUS_CAP = 20.0

ALLOWED_MODEL_CROSS_IDS = {"tdcc_short_term_continuation_d5_d10"}
DELTA_COLS = [
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
]
MANIFEST_COLUMNS = [
    "section_order",
    "section_id",
    "section_title_zh",
    "table_contract",
    "include_in_highlight",
    "highlight_limit",
    "include_in_full",
    "full_limit",
    "required",
    "enabled",
    "notes_zh",
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


def manifest_bool(value: Any, default: bool) -> bool:
    text = safe_str(value).strip().lower()
    if not text:
        return default
    return text in {"1", "true", "yes", "y", "on", "是", "啟用"}


def is_model_cross_section(row: pd.Series) -> bool:
    section_id = safe_str(row.get("section_id"))
    table_contract = safe_str(row.get("table_contract"))
    return table_contract == "model_cross" or section_id.startswith("model_cross_")


def section_allows_empty(row: pd.Series) -> bool:
    return is_model_cross_section(row)


def manifest_limit(value: Any, default: int) -> int:
    number = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(number) or number <= 0:
        return default
    return int(number)


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


def ensure_manifest_columns(manifest: pd.DataFrame, errors: list[str]) -> pd.DataFrame:
    require_columns(manifest, MANIFEST_COLUMNS, "section manifest", errors)
    out = manifest.copy()
    for column in MANIFEST_COLUMNS:
        if column not in out.columns:
            out[column] = ""
    return out[MANIFEST_COLUMNS]


def ordered_manifest(manifest: pd.DataFrame) -> pd.DataFrame:
    return manifest.sort_values(
        by=["section_order", "section_id"],
        key=lambda series: pd.to_numeric(series, errors="coerce").fillna(999999)
        if series.name == "section_order"
        else series,
    ).reset_index(drop=True)


def sections_for_report(manifest: pd.DataFrame, report_kind: str) -> pd.DataFrame:
    include_col = "include_in_highlight" if report_kind == "highlight" else "include_in_full"
    if manifest.empty or include_col not in manifest.columns:
        return pd.DataFrame(columns=MANIFEST_COLUMNS)
    filtered = manifest[
        manifest["enabled"].map(lambda value: manifest_bool(value, True))
        & manifest[include_col].map(lambda value: manifest_bool(value, True))
    ].copy()
    return ordered_manifest(filtered)


def section_limit(row: pd.Series, report_kind: str) -> int:
    return manifest_limit(row.get("highlight_limit" if report_kind == "highlight" else "full_limit"), 10 if report_kind == "highlight" else 50)


def validate_manifest(manifest: pd.DataFrame, errors: list[str]) -> None:
    if manifest.empty:
        errors.append("section manifest is empty")
        return
    ids = manifest["section_id"].map(safe_str)
    blank = ids == ""
    if blank.any():
        errors.append("section manifest has blank section_id")
    duplicated = sorted(ids[ids.duplicated() & ~blank].unique())
    if duplicated:
        errors.append(f"section manifest has duplicate section_id values: {', '.join(duplicated)}")
    bad_contracts = sorted(set(manifest["table_contract"].map(safe_str)) - {"tdcc_ranking", "model_cross"})
    if bad_contracts:
        errors.append(f"section manifest has unsupported table_contract values: {', '.join(bad_contracts)}")
    for report_kind in ["highlight", "full"]:
        sections = sections_for_report(manifest, report_kind)
        titles = sections["section_title_zh"].map(safe_str)
        duplicated_titles = sorted(titles[titles.duplicated() & (titles != "")].unique())
        if duplicated_titles:
            errors.append(f"{report_kind} manifest has duplicate section titles that could merge tables: {', '.join(duplicated_titles)}")


def section_rank_values(group: pd.DataFrame) -> list[int]:
    return to_number(group["section_rank"]).dropna().astype(int).tolist()


def validate_report(
    report: pd.DataFrame,
    label: str,
    report_kind: str,
    expected_signal_date: str,
    weekly: pd.DataFrame,
    consecutive: pd.DataFrame,
    manifest: pd.DataFrame,
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

    manifest_sections = sections_for_report(manifest, report_kind)
    expected_section_ids = [safe_str(value) for value in manifest_sections["section_id"] if safe_str(value)]
    report_section_ids = sorted({safe_str(value) for value in report["section_id"].dropna() if safe_str(value)})
    unexpected = sorted(set(report_section_ids) - set(expected_section_ids))
    if unexpected:
        errors.append(f"{label} has sections not enabled for {report_kind}: {', '.join(unexpected)}")

    section_name_map = report.groupby("section_name_zh", dropna=False)["section_id"].nunique()
    merged_titles = section_name_map[section_name_map > 1]
    if not merged_titles.empty:
        errors.append(
            f"{label} appears to merge multiple section_id values under one table title: "
            + ", ".join(safe_str(value) for value in merged_titles.index)
        )

    for _, section_row in manifest_sections.iterrows():
        section_id = safe_str(section_row.get("section_id"))
        if not section_id:
            continue
        rows = report[report["section_id"].map(safe_str) == section_id].copy()
        limit = section_limit(section_row, report_kind)
        required = manifest_bool(section_row.get("required"), True)
        if rows.empty:
            if required and not section_allows_empty(section_row):
                errors.append(f"{label} required section is empty or missing: {section_id}")
            else:
                warnings.append(f"{label} section has no rows and will render an explicit empty state: {section_id}")
            continue
        if len(rows) > limit:
            errors.append(f"{label} section {section_id} has {len(rows)} rows above manifest limit {limit}")
        ranks = section_rank_values(rows)
        expected_ranks = list(range(1, len(ranks) + 1))
        if ranks != expected_ranks:
            errors.append(f"{label} section {section_id} ranks are not sequential 1..N")

    source_rankings = {
        "weekly_increase": weekly,
        "consecutive_accumulation": consecutive,
    }
    for section_id, ranking in source_rankings.items():
        section_manifest = manifest_sections[manifest_sections["section_id"].map(safe_str) == section_id]
        if section_manifest.empty or ranking.empty:
            continue
        limit = section_limit(section_manifest.iloc[0], report_kind)
        rows = report[report["section_id"].map(safe_str) == section_id]
        expected_ids = ranking.head(limit)["stock_id"].map(safe_str).tolist()
        actual_ids = rows.sort_values("section_rank", key=lambda s: to_number(s).fillna(999999))["stock_id"].map(safe_str).tolist()
        if actual_ids != expected_ids:
            errors.append(f"{label} {section_id} stock order does not match source ranking top {limit}")

    weekly_rows = report[report["section_id"].map(safe_str) == "weekly_increase"]
    if not weekly_rows.empty:
        weekly_effective = to_number(weekly_rows["tdcc_effective_increase_count"]).fillna(0)
        if (weekly_effective < 1).any():
            errors.append(f"{label} weekly_increase contains rows with no effective increase")

    consecutive_rows = report[report["section_id"].map(safe_str) == "consecutive_accumulation"]
    if not consecutive_rows.empty:
        consecutive_streak = to_number(consecutive_rows["tdcc_high_pair_effective_streak_weeks"]).fillna(0)
        if (consecutive_streak < 2).any():
            bad = consecutive_rows[consecutive_streak < 2]
            examples = ", ".join(
                f"{safe_str(row.get('stock_id'))}:{safe_str(row.get('tdcc_high_pair_effective_streak_weeks'))}"
                for _, row in bad.head(8).iterrows()
            )
            errors.append(f"{label} consecutive_accumulation contains rows below 2-week 800/1000 effective streak: {examples}")

    model_rows = report[report["section_id"].map(safe_str).str.startswith("model_cross_")]
    bad_models = sorted(set(model_rows["model_id"].dropna().map(safe_str)) - ALLOWED_MODEL_CROSS_IDS)
    if bad_models:
        errors.append(f"{label} has unsupported model cross ids: {', '.join(bad_models)}")
    for section_id, rows in model_rows.groupby(model_rows["section_id"].map(safe_str), dropna=False):
        actual = rows.sort_values("section_rank", key=lambda s: to_number(s).fillna(999999))
        expected = rows.assign(
            _model_score=to_number(rows.get("model_score", pd.Series(index=rows.index))).fillna(float("-inf")),
            _display_rank=to_number(rows.get("model_rank", pd.Series(index=rows.index))).fillna(999999),
            _tdcc_rank=to_number(rows.get("tdcc_rank", pd.Series(index=rows.index))).fillna(999999),
        ).sort_values(
            ["_model_score", "_display_rank", "_tdcc_rank"],
            ascending=[False, True, True],
        )
        actual_ids = actual["stock_id"].map(safe_str).tolist()
        expected_ids = expected["stock_id"].map(safe_str).tolist()
        if actual_ids != expected_ids:
            errors.append(
                f"{label} model cross section {section_id} is not sorted by model_score desc, "
                "model rank asc, then TDCC rank asc"
            )


def read_text_artifact(path: Path, errors: list[str]) -> str:
    if not path.exists() or path.stat().st_size <= 0:
        errors.append(f"missing or empty artifact: {path.as_posix()}")
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        errors.append(f"failed to read artifact {path.as_posix()}: {exc}")
        return ""


def read_pdf_text(path: Path, errors: list[str]) -> str:
    if not path.exists() or path.stat().st_size < 10_000:
        errors.append(f"missing or too-small TDCC PDF: {path.as_posix()}")
        return ""
    try:
        from pypdf import PdfReader
    except Exception as exc:
        errors.append(f"pypdf unavailable for PDF validation: {exc}")
        return ""
    try:
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:
        errors.append(f"failed to extract PDF text from {path.as_posix()}: {exc}")
        return ""


def delivery_pdf_path(report_kind: str, signal_date: str) -> Path:
    date = safe_str(signal_date)
    if not re.fullmatch(r"\d{8}", date):
        raise RuntimeError(f"TDCC delivery PDF signal_date must be YYYYMMDD, got: {signal_date!r}")
    if report_kind == "highlight":
        return DELIVERY_PDF_DIR / f"{DELIVERY_HIGHLIGHT_PDF_PREFIX}_{date}.pdf"
    if report_kind == "full":
        return DELIVERY_PDF_DIR / f"{DELIVERY_FULL_PDF_PREFIX}_{date}.pdf"
    raise ValueError(f"unsupported TDCC delivery report kind: {report_kind}")


def read_pdf_page_count_and_text(path: Path, errors: list[str]) -> tuple[int, str]:
    if not path.exists() or path.stat().st_size < 10_000:
        errors.append(f"missing or too-small TDCC PDF: {path.as_posix()}")
        return 0, ""
    try:
        from pypdf import PdfReader
    except Exception as exc:
        errors.append(f"pypdf unavailable for PDF validation: {exc}")
        return 0, ""
    try:
        reader = PdfReader(str(path))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        if not text.strip():
            errors.append(f"TDCC PDF has no extractable text: {path.as_posix()}")
        return len(reader.pages), text
    except Exception as exc:
        errors.append(f"failed to open or extract PDF text from {path.as_posix()}: {exc}")
        return 0, ""


def tdcc_data_dates_from_text(text: str) -> list[str]:
    return sorted(set(re.findall(r"TDCC data date:\s*([0-9]{8})", text)))


def markdown_section_titles(text: str) -> list[str]:
    return [line[3:].strip() for line in text.splitlines() if line.startswith("## ")]


def validate_artifact(
    text: str,
    label: str,
    report_kind: str,
    expected_signal_date: str,
    manifest: pd.DataFrame,
    errors: list[str],
) -> None:
    dates = tdcc_data_dates_from_text(text)
    if dates != [expected_signal_date]:
        errors.append(f"{label} TDCC data date must be {expected_signal_date}, got {dates}")
    expected_titles = [safe_str(value) for value in sections_for_report(manifest, report_kind)["section_title_zh"] if safe_str(value)]
    for title in expected_titles:
        if title not in text:
            errors.append(f"{label} missing independent section title: {title}")


def validate_markdown_artifact(
    path: Path,
    label: str,
    report_kind: str,
    expected_signal_date: str,
    manifest: pd.DataFrame,
    errors: list[str],
) -> None:
    text = read_text_artifact(path, errors)
    if not text:
        return
    validate_artifact(text, label, report_kind, expected_signal_date, manifest, errors)
    headings = markdown_section_titles(text)
    expected_titles = [safe_str(value) for value in sections_for_report(manifest, report_kind)["section_title_zh"] if safe_str(value)]
    missing = [title for title in expected_titles if title not in headings]
    if missing:
        errors.append(f"{label} missing Markdown H2 sections: {', '.join(missing)}")


def validate_pdf_artifact(
    path: Path,
    label: str,
    report_kind: str,
    expected_signal_date: str,
    manifest: pd.DataFrame,
    errors: list[str],
) -> None:
    text = read_pdf_text(path, errors)
    if not text:
        return
    validate_artifact(text, label, report_kind, expected_signal_date, manifest, errors)


def validate_delivery_pdf_artifact(
    canonical_path: Path,
    delivery_path: Path,
    label: str,
    report_kind: str,
    expected_signal_date: str,
    manifest: pd.DataFrame,
    errors: list[str],
) -> None:
    canonical_pages, canonical_text = read_pdf_page_count_and_text(canonical_path, errors)
    delivery_pages, delivery_text = read_pdf_page_count_and_text(delivery_path, errors)
    if canonical_pages and delivery_pages and canonical_pages != delivery_pages:
        errors.append(
            f"{label} page count must match canonical PDF: "
            f"{delivery_path.as_posix()}={delivery_pages}, {canonical_path.as_posix()}={canonical_pages}"
        )
    if delivery_text:
        validate_artifact(delivery_text, label, report_kind, expected_signal_date, manifest, errors)
    if canonical_text and delivery_text and canonical_text.strip() != delivery_text.strip():
        errors.append(f"{label} extractable text must match canonical PDF")


def validate_no_root_delivery_pdfs(errors: list[str]) -> None:
    stale = [
        *LATEST_DIR.glob(f"{DELIVERY_HIGHLIGHT_PDF_PREFIX}_*.pdf"),
        *LATEST_DIR.glob(f"{DELIVERY_FULL_PDF_PREFIX}_*.pdf"),
    ]
    if stale:
        paths = ", ".join(path.as_posix() for path in sorted(stale))
        errors.append(f"TDCC Chinese delivery PDFs must not remain in output/latest root: {paths}")


def validate_signal_dates(highlight: pd.DataFrame, full: pd.DataFrame, errors: list[str]) -> str:
    highlight_dates = sorted_signal_dates(highlight)
    full_dates = sorted_signal_dates(full)
    signal_date = ""
    if len(highlight_dates) != 1:
        errors.append(f"highlight report-ready CSV must contain exactly one signal_date, got {highlight_dates}")
    if len(full_dates) != 1:
        errors.append(f"full report-ready CSV must contain exactly one signal_date, got {full_dates}")
    if len(highlight_dates) == 1 and len(full_dates) == 1:
        if highlight_dates[0] != full_dates[0]:
            errors.append(f"highlight/full signal_date mismatch: highlight={highlight_dates}, full={full_dates}")
        else:
            signal_date = highlight_dates[0]
    return signal_date


def report_section_counts(report: pd.DataFrame, manifest: pd.DataFrame, report_kind: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    actual_counts: dict[str, int] = {}
    if "section_id" in report.columns:
        actual_counts = {
            safe_str(section_id): int(count)
            for section_id, count in report.groupby("section_id", dropna=False).size().to_dict().items()
        }
    for _, section_row in sections_for_report(manifest, report_kind).iterrows():
        section_id = safe_str(section_row.get("section_id"))
        if section_id:
            counts[section_id] = int(actual_counts.get(section_id, 0))
    for section_id, count in actual_counts.items():
        if section_id and section_id not in counts:
            counts[section_id] = int(count)
    return counts


def write_validation(result: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# TDCC Weekly Candidate Report Validation",
        "",
        f"- status: {result['status']}",
        f"- signal_date: {result.get('signal_date', '')}",
        f"- date_source: {result.get('date_contract', {}).get('date_source', '')}",
        f"- error_count: {len(result['errors'])}",
        f"- warning_count: {len(result['warnings'])}",
        "",
        "## Date Contract",
        "",
    ]
    date_contract = result.get("date_contract", {})
    if date_contract:
        for key, value in date_contract.items():
            lines.append(f"- {key}: `{value}`")
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## Manifest Sections",
        "",
    ])
    manifest_sections = result.get("manifest_sections", [])
    if manifest_sections:
        for section in manifest_sections:
            lines.append(
                f"- {section['section_order']}. `{section['section_id']}` "
                f"({section['table_contract']}): highlight={section['highlight_limit']}, full={section['full_limit']}"
            )
    else:
        lines.append("- none")
    lines.extend(["", "## Report Row Counts", ""])
    counts = result.get("row_counts", {})
    if counts:
        for name, count in counts.items():
            lines.append(f"- {name}: {count}")
    else:
        lines.append("- none")
    lines.extend(["", "## Section Row Counts", ""])
    section_counts = result.get("section_counts", {})
    if section_counts:
        for report_kind, counts_by_section in section_counts.items():
            lines.append(f"### {report_kind}")
            for section_id, count in counts_by_section.items():
                lines.append(f"- `{section_id}`: {count}")
    else:
        lines.append("- none")
    lines.extend(["", "## Font Contract", ""])
    font_contract = result.get("font_contract", {})
    if font_contract:
        for path, fonts in font_contract.items():
            lines.append(f"- `{path}`: `{fonts}`")
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
    manifest = ensure_manifest_columns(read_csv(SECTION_MANIFEST_CSV, errors), errors)
    manifest = ordered_manifest(manifest) if not manifest.empty else manifest
    highlight = read_csv(HIGHLIGHT_FOR_REPORT_CSV, errors)
    full = read_csv(FULL_FOR_REPORT_CSV, errors)

    validate_manifest(manifest, errors)
    validate_score_formulas(weekly, "weekly increase ranking", errors)
    validate_score_formulas(consecutive, "consecutive accumulation ranking", errors)

    consecutive_streak = to_number(consecutive.get("tdcc_high_pair_effective_streak_weeks", pd.Series(dtype=str))).fillna(0)
    if not consecutive.empty and (consecutive_streak < 2).any():
        errors.append("consecutive accumulation source ranking contains rows below 2-week 800/1000 effective streak")

    signal_date = validate_signal_dates(highlight, full, errors)
    validate_no_root_delivery_pdfs(errors)

    source_date_sets = {
        "weekly": sorted_signal_dates(weekly),
        "consecutive": sorted_signal_dates(consecutive),
    }
    if signal_date:
        for label, dates in source_date_sets.items():
            if dates and dates != [signal_date]:
                errors.append(f"{label} source signal_date must be {signal_date}, got {dates}")

    if not model_cross.empty:
        require_columns(model_cross, ["tdcc_list_type", "tdcc_rank", "stock_id", "model_id"], "model cross summary", errors)
        bad_models = sorted(set(model_cross.get("model_id", pd.Series(dtype=str)).dropna().map(safe_str)) - ALLOWED_MODEL_CROSS_IDS)
        if bad_models:
            errors.append(f"model cross summary has unsupported model ids: {', '.join(bad_models)}")

    if signal_date and not manifest.empty:
        validate_report(highlight, "highlight report-ready CSV", "highlight", signal_date, weekly, consecutive, manifest, errors, warnings)
        validate_report(full, "full report-ready CSV", "full", signal_date, weekly, consecutive, manifest, errors, warnings)
        validate_markdown_artifact(HIGHLIGHT_MD, "highlight Markdown", "highlight", signal_date, manifest, errors)
        validate_markdown_artifact(FULL_MD, "full Markdown", "full", signal_date, manifest, errors)
        validate_pdf_artifact(HIGHLIGHT_PDF, "highlight PDF", "highlight", signal_date, manifest, errors)
        validate_pdf_artifact(FULL_PDF, "full PDF", "full", signal_date, manifest, errors)
        validate_delivery_pdf_artifact(
            HIGHLIGHT_PDF,
            delivery_pdf_path("highlight", signal_date),
            "highlight delivery PDF",
            "highlight",
            signal_date,
            manifest,
            errors,
        )
        validate_delivery_pdf_artifact(
            FULL_PDF,
            delivery_pdf_path("full", signal_date),
            "full delivery PDF",
            "full",
            signal_date,
            manifest,
            errors,
        )
        try:
            font_contract = validate_tdcc_weekly_pdf_font_contract(
                [
                    HIGHLIGHT_PDF,
                    FULL_PDF,
                    delivery_pdf_path("highlight", signal_date),
                    delivery_pdf_path("full", signal_date),
                ]
            )
        except RuntimeError as exc:
            errors.append(str(exc))
            font_contract = {}
    else:
        font_contract = {}
        for path in [HIGHLIGHT_PDF, FULL_PDF]:
            if not path.exists() or path.stat().st_size < 10_000:
                errors.append(f"missing or too-small TDCC PDF: {path.as_posix()}")

    row_counts = {
        "weekly_increase": int(len(weekly)),
        "consecutive_accumulation": int(len(consecutive)),
        "model_cross": int(len(model_cross)),
        "highlight_report": int(len(highlight)),
        "full_report": int(len(full)),
        "manifest_sections": int(len(manifest)),
    }
    section_counts = {
        "highlight": report_section_counts(highlight, manifest, "highlight"),
        "full": report_section_counts(full, manifest, "full"),
    }
    manifest_sections = [
        {
            "section_order": safe_str(row.get("section_order")),
            "section_id": safe_str(row.get("section_id")),
            "section_title_zh": safe_str(row.get("section_title_zh")),
            "table_contract": safe_str(row.get("table_contract")),
            "highlight_limit": section_limit(row, "highlight"),
            "full_limit": section_limit(row, "full"),
            "required": manifest_bool(row.get("required"), True),
            "enabled": manifest_bool(row.get("enabled"), True),
        }
        for _, row in manifest.iterrows()
    ]
    date_contract = {
        "date_source": "report_ready_csv_signal_date",
        "report_date": signal_date,
        "highlight_report_ready_signal_dates": sorted_signal_dates(highlight),
        "full_report_ready_signal_dates": sorted_signal_dates(full),
        "weekly_source_signal_dates": source_date_sets["weekly"],
        "consecutive_source_signal_dates": source_date_sets["consecutive"],
    }
    result: dict[str, Any] = {
        "status": "pass" if not errors else "fail",
        "signal_date": signal_date,
        "date_contract": date_contract,
        "row_counts": row_counts,
        "section_counts": section_counts,
        "manifest_sections": manifest_sections,
        "font_contract": font_contract,
        "errors": errors,
        "warnings": warnings,
    }
    write_validation(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
