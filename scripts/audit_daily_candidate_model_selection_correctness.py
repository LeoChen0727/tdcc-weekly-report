from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import pandas as pd

from build_daily_candidate_model_layer import (
    build_signals,
    build_specs,
    cond_pullback,
    cond_w_bottom_right,
)
from tracking_utils import LATEST_DIR, main_price_date_from_freshness, read_csv, resolve_candidate_signal_date, safe_str


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_latest.csv"
REPORT_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
VOLUME_WATCH = LATEST_DIR / "volume_breakout_watch_latest.csv"
TDCC_SHORT_EDGE = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
AUDIT_JSON = LATEST_DIR / "daily_candidate_model_selection_audit_latest.json"
AUDIT_MD = LATEST_DIR / "daily_candidate_model_selection_audit_latest.md"


VALID_VOLUME_TYPES = {
    "range_breakout_volume",
    "platform_volume_breakout",
    "neckline_volume_breakout",
    "strict_high_breakout",
    "strict_60d_volume_breakout",
    "true_breakout",
    "breakout",
}
VALID_VOLUME_STATUSES = {
    "selected",
    "selected_as_strict_breakout",
    "selected_but_routed_to_other_category",
    "not_selected_by_candidate_model",
}
POSITIVE_TDCC = {"strong_accumulation", "mild_accumulation", "tdcc_price_confirmed", "tdcc_leading_price"}
CONFIRMED_STAGES = {"breakout_confirmed", "platform_breakout", "neckline_breakout"}
CONFIRMED_STAGE_TEXT_MARKERS = {"已突破", "突破確認", "平台突破", "頸線突破"}


def normalize_code(value: Any) -> str:
    raw = safe_str(value).strip()
    if not raw:
        return ""
    if raw.endswith(".0"):
        raw = raw[:-2]
    return raw.zfill(4) if raw.isdigit() and len(raw) < 4 else raw


def text(row: pd.Series | dict[str, Any], *cols: str) -> str:
    for col in cols:
        if col in row:
            value = safe_str(row.get(col, "")).strip()
            if value and value.lower() not in {"nan", "none", "nat"}:
                return value
    return ""


def num(row: pd.Series | dict[str, Any], *cols: str) -> float:
    for col in cols:
        if col in row:
            value = pd.to_numeric(pd.Series([row.get(col, "")]), errors="coerce").iloc[0]
            if pd.notna(value):
                return float(value)
    return math.nan


def flag(row: pd.Series | dict[str, Any], *cols: str) -> bool:
    value = text(row, *cols).lower()
    return value in {"1", "1.0", "true", "yes", "y", "t"}


def is_true(value: Any) -> bool:
    return safe_str(value).strip().lower() in {"1", "1.0", "true", "yes", "y", "t"}


def read(path: Path) -> pd.DataFrame:
    return read_csv(path, dtype=str, keep_default_na=False)


def stock_set(df: pd.DataFrame, model_id: str | None = None) -> set[str]:
    source = df
    if model_id is not None and "model_id" in source.columns:
        source = source[source["model_id"].astype(str).eq(model_id)]
    if "stock_id" not in source.columns:
        return set()
    return {normalize_code(v) for v in source["stock_id"].astype(str) if normalize_code(v)}


def model_key_set(df: pd.DataFrame, model_ids: set[str] | None = None) -> set[tuple[str, str, str]]:
    required = {"report_bucket", "model_id", "stock_id"}
    if df.empty or not required.issubset(df.columns):
        return set()
    source = df
    if model_ids is not None:
        source = source[source["model_id"].astype(str).isin(model_ids)]
    return {
        (
            safe_str(row.get("report_bucket", "")).strip(),
            safe_str(row.get("model_id", "")).strip(),
            normalize_code(row.get("stock_id", "")),
        )
        for _, row in source.iterrows()
        if safe_str(row.get("report_bucket", "")).strip()
        and safe_str(row.get("model_id", "")).strip()
        and normalize_code(row.get("stock_id", ""))
    }


def index_candidates(df: pd.DataFrame) -> dict[str, pd.Series]:
    result: dict[str, pd.Series] = {}
    if df.empty or "stock_id" not in df.columns:
        return result
    for _, row in df.iterrows():
        sid = normalize_code(row.get("stock_id", ""))
        if sid and sid not in result:
            result[sid] = row
    return result


def index_volume_watch(df: pd.DataFrame) -> dict[str, pd.Series]:
    """Index the strongest usable volume-watch row per stock.

    Some stocks can appear in different scopes. Prefer rows that are valid
    selected/watch breakout entries instead of whichever row appears first.
    """
    result: dict[str, pd.Series] = {}
    if df.empty or "stock_id" not in df.columns:
        return result
    priority = {
        "selected_as_strict_breakout": 0,
        "selected_but_routed_to_other_category": 1,
        "not_selected_by_candidate_model": 2,
        "selected": 3,
    }
    rows: list[tuple[int, int, pd.Series]] = []
    for idx, row in df.iterrows():
        sid = normalize_code(row.get("stock_id", ""))
        if not sid:
            continue
        status = text(row, "selection_status").lower()
        btype = text(row, "volume_breakout_type", "breakout_type").lower()
        type_ok = btype in VALID_VOLUME_TYPES
        status_score = priority.get(status, 9)
        rows.append((0 if type_ok else 1, status_score * 100000 + int(idx), row))
    for _, _, row in sorted(rows, key=lambda x: (x[0], x[1])):
        sid = normalize_code(row.get("stock_id", ""))
        if sid not in result:
            result[sid] = row
    return result


def source_candidate(row: pd.Series, candidates: pd.DataFrame, by_stock: dict[str, pd.Series]) -> pd.Series | None:
    raw_idx = text(row, "source_row_index")
    if raw_idx.isdigit():
        idx = int(raw_idx)
        if 0 <= idx < len(candidates):
            return candidates.iloc[idx]
    sid = normalize_code(row.get("stock_id", ""))
    return by_stock.get(sid)


def already_confirmed_breakout(row: pd.Series) -> bool:
    category = text(row, "category", "original_category").lower()
    breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
    stage_raw = text(row, "pattern_stage")
    stage = stage_raw.lower()
    if category in {"true_breakout", "strict_breakout"}:
        return True
    if breakout_type in VALID_VOLUME_TYPES:
        return True
    if any(marker in stage_raw for marker in CONFIRMED_STAGE_TEXT_MARKERS):
        return True
    return (
        stage in CONFIRMED_STAGES
        or flag(row, "volume_confirmed_breakout")
        or flag(row, "platform_breakout_flag")
        or flag(row, "neckline_breakout_flag")
    )


def hard_confirmed_breakout(row: pd.Series) -> bool:
    """Confirmed breakout that should end pre-breakout pattern models.

    Some upstream rows carry broad flags such as volume_confirmed_breakout while
    still being useful for overlapping pattern review.  For W-bottom validation
    we only treat explicit breakout categories, dedicated breakout types, and
    confirmed pattern stages as hard confirmation.
    """
    category = text(row, "category", "original_category").lower()
    breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
    stage_raw = text(row, "pattern_stage")
    stage = stage_raw.lower()
    return (
        category in {"true_breakout", "strict_breakout"}
        or breakout_type in VALID_VOLUME_TYPES
        or stage in CONFIRMED_STAGES
        or any(marker in stage_raw for marker in CONFIRMED_STAGE_TEXT_MARKERS)
    )


def strong_revenue(row: pd.Series) -> bool:
    yoy = num(row, "latest_revenue_yoy", "revenue_yoy_pct")
    cumulative = num(row, "cumulative_revenue_yoy", "cumulative_yoy_pct")
    return (not math.isnan(yoy) and yoy >= 30) or (not math.isnan(cumulative) and cumulative >= 20)


def source_volume_breakout_condition(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    if math.isnan(vol) or vol < 1.5:
        return False
    btype = text(row, "volume_breakout_type", "breakout_type").lower()
    return (
        btype in VALID_VOLUME_TYPES
        or flag(row, "platform_breakout_flag")
        or flag(row, "neckline_breakout_flag")
        or flag(row, "volume_confirmed_breakout")
    )


def active_attack(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    ret5 = num(row, "return_5d", "return_5d_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    return (
        source_volume_breakout_condition(row)
        or flag(row, "volume_confirmed_breakout")
        or (not math.isnan(vol) and vol >= 2.5)
        or (not math.isnan(ret5) and ret5 >= 8)
        or (not math.isnan(ret20) and ret20 >= 20)
    )


def audit_selected_row(
    row: pd.Series,
    source: pd.Series | None,
    volume_by_stock: dict[str, pd.Series],
    tdcc_edge_stocks: set[str],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    sid = normalize_code(row.get("stock_id", ""))
    model = text(row, "model_id")

    if not is_true(row.get("main_condition_met", "")):
        errors.append(f"{sid} {model}: main_condition_met is not true")

    if model == "volume_range_breakout":
        vrow = volume_by_stock.get(sid)
        raw_idx = text(row, "source_row_index")
        if raw_idx.isdigit() and source is not None and source_volume_breakout_condition(source):
            return errors, warnings
        if vrow is None:
            if source is not None and source_volume_breakout_condition(source):
                return errors, warnings
            errors.append(f"{sid}: selected by volume_range_breakout but missing from volume_breakout_watch")
        else:
            btype = text(vrow, "volume_breakout_type", "breakout_type").lower()
            status = text(vrow, "selection_status").lower()
            if btype not in VALID_VOLUME_TYPES:
                errors.append(f"{sid}: volume breakout type not valid for selected model: {btype}")
            if status not in VALID_VOLUME_STATUSES:
                errors.append(f"{sid}: volume selection_status not valid for selected model: {status}")
            vol = num(vrow, "volume_ratio")
            if math.isnan(vol) or vol < 1.5:
                errors.append(f"{sid}: volume breakout selected but volume_ratio < 1.5")
        return errors, warnings

    if model == "tdcc_short_term_continuation_d5_d10":
        if sid not in tdcc_edge_stocks:
            errors.append(f"{sid}: selected by TDCC short continuation but missing from TDCC edge table")
        return errors, warnings

    if source is None:
        warnings.append(f"{sid} {model}: source candidate row not found; condition could not be verified")
        return errors, warnings

    if model == "revenue_unreacted_range":
        if not strong_revenue(source):
            errors.append(f"{sid}: revenue_unreacted_range without strong revenue")
        if active_attack(source):
            errors.append(f"{sid}: revenue_unreacted_range selected despite active attack/breakout/extended move")
    elif model == "near_high_neckline_challenge":
        if already_confirmed_breakout(source):
            errors.append(f"{sid}: near_high_neckline_challenge selected after confirmed breakout")
        vol = num(source, "volume_ratio")
        if math.isnan(vol) or vol < 1.2:
            warnings.append(f"{sid}: near_high_neckline_challenge volume_ratio below review threshold")
    elif model == "platform_strengthening":
        if already_confirmed_breakout(source):
            errors.append(f"{sid}: platform_strengthening selected after confirmed breakout")
        if not (flag(source, "platform_base_flag") or not math.isnan(num(source, "platform_width_pct", "short_platform_width_pct"))):
            warnings.append(f"{sid}: platform_strengthening missing platform/base evidence")
    elif model == "w_bottom_right_side":
        if hard_confirmed_breakout(source):
            errors.append(f"{sid}: w_bottom_right_side selected after confirmed breakout")
        if not cond_w_bottom_right(source):
            errors.append(f"{sid}: w_bottom_right_side selected but price-history W geometry check failed")
    elif model == "price_pullback_23ema":
        if not cond_pullback(source):
            errors.append(f"{sid}: price_pullback_23ema selected but pullback/23EMA/support condition failed")
    elif model == "pullback_short_reclaim":
        ret20 = num(source, "return_20d", "return_20d_pct")
        if math.isnan(ret20) or ret20 < 5:
            warnings.append(f"{sid}: pullback_short_reclaim lacks prior 20d strength")
    elif model == "tdcc_stealth_accumulation":
        phase = text(source, "tdcc_price_phase").lower()
        if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
            errors.append(f"{sid}: tdcc_stealth_accumulation selected despite disallowed phase {phase}")
        if active_attack(source):
            errors.append(f"{sid}: tdcc_stealth_accumulation selected despite active attack/breakout/extended move")
        if text(source, "tdcc_status").lower() not in POSITIVE_TDCC and not phase:
            warnings.append(f"{sid}: tdcc_stealth_accumulation lacks positive TDCC status/phase")

    return errors, warnings


def audit() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, Any] = {}

    candidates = read(ALL_CANDIDATES)
    raw_signals = read(MODEL_SIGNALS)
    report_signals = read(REPORT_SIGNALS)
    volume = read(VOLUME_WATCH)
    tdcc_edge = read(TDCC_SHORT_EDGE)
    taxonomy = read(TAXONOMY)
    freshness_main_date = main_price_date_from_freshness()
    main_date, date_notes = resolve_candidate_signal_date(candidates, freshness_main_date)
    if not main_date:
        main_date = freshness_main_date

    details["main_price_date"] = freshness_main_date
    details["effective_candidate_signal_date"] = main_date
    details["date_notes"] = date_notes
    if freshness_main_date and main_date and freshness_main_date != main_date:
        warnings.append(
            f"freshness main_price_date={freshness_main_date} differs from candidate signal_date={main_date}; "
            "auditing candidate-model internal consistency against candidate signal_date"
        )
    details["all_candidates_rows"] = int(len(candidates))
    details["raw_model_signal_rows"] = int(len(raw_signals))
    details["report_model_signal_rows"] = int(len(report_signals))
    details["volume_watch_rows"] = int(len(volume))
    details["tdcc_short_edge_rows"] = int(len(tdcc_edge))
    details["taxonomy_rows"] = int(len(taxonomy))

    required_paths = {
        "all_candidates_latest.csv": candidates,
        "daily_candidate_model_signals_latest.csv": raw_signals,
        "daily_candidate_model_signals_for_report_latest.csv": report_signals,
        "stock_theme_taxonomy_latest.csv": taxonomy,
    }
    for name, df in required_paths.items():
        if df.empty:
            errors.append(f"missing_or_empty: {name}")

    for name, df in {
        "all_candidates": candidates,
        "raw_model_signals": raw_signals,
        "report_model_signals": report_signals,
        "volume_watch": volume,
        "tdcc_short_edge": tdcc_edge,
    }.items():
        if df.empty or "signal_date" not in df.columns:
            continue
        dates = sorted({safe_str(v) for v in df["signal_date"].astype(str) if safe_str(v)})
        details[f"{name}_dates"] = dates
        bad_dates = [d for d in dates if d != main_date]
        if bad_dates:
            errors.append(f"{name} signal_date mismatch: expected {main_date}, got {bad_dates}")

    if not report_signals.empty:
        dup_cols = ["report_line", "model_id", "stock_id"]
        missing_dup_cols = [c for c in dup_cols if c not in report_signals.columns]
        if missing_dup_cols:
            errors.append(f"report signal missing duplicate check columns: {missing_dup_cols}")
        else:
            dup_count = int(report_signals.duplicated(dup_cols).sum())
            details["same_report_line_model_stock_duplicates"] = dup_count
            if dup_count:
                errors.append(f"same report_line/model/stock duplicate rows: {dup_count}")

        valid_lines = {"mainstream", "non_mainstream"}
        if "report_line" in report_signals.columns:
            bad_lines = sorted(set(report_signals["report_line"].astype(str)) - valid_lines - {""})
            details["bad_report_lines"] = bad_lines
            if bad_lines:
                errors.append(f"invalid report_line values: {bad_lines}")

    if not taxonomy.empty:
        if "basic_theme" in taxonomy.columns:
            unresolved_basic = int(taxonomy["basic_theme"].astype(str).str.strip().eq("").sum())
            details["taxonomy_unresolved_basic_theme_rows"] = unresolved_basic
            if unresolved_basic:
                errors.append(f"taxonomy has blank basic_theme rows: {unresolved_basic}")
        if "report_line_memberships" in taxonomy.columns:
            blank_memberships = int(taxonomy["report_line_memberships"].astype(str).str.strip().eq("").sum())
            details["taxonomy_blank_report_line_memberships"] = blank_memberships
            if blank_memberships:
                errors.append(f"taxonomy has blank report_line_memberships rows: {blank_memberships}")

    candidate_by_stock = index_candidates(candidates)
    volume_by_stock = index_volume_watch(volume)
    tdcc_edge_stocks = stock_set(tdcc_edge)

    selected_errors: list[str] = []
    selected_warnings: list[str] = []
    for _, row in raw_signals.iterrows():
        source = source_candidate(row, candidates, candidate_by_stock)
        row_errors, row_warnings = audit_selected_row(row, source, volume_by_stock, tdcc_edge_stocks)
        selected_errors.extend(row_errors)
        selected_warnings.extend(row_warnings)

    details["selected_condition_error_count"] = len(selected_errors)
    details["selected_condition_warning_count"] = len(selected_warnings)
    errors.extend(selected_errors[:200])
    if len(selected_errors) > 200:
        errors.append(f"selected condition errors truncated: {len(selected_errors) - 200} more")
    warnings.extend(selected_warnings[:200])
    if len(selected_warnings) > 200:
        warnings.append(f"selected condition warnings truncated: {len(selected_warnings) - 200} more")

    raw_volume_stocks = stock_set(raw_signals, "volume_range_breakout")
    if not candidates.empty and not raw_signals.empty:
        specs = build_specs()
        spec_ids = {spec.model_id for spec in specs}
        expected_core = build_signals(candidates, specs, main_date)
        expected_core_keys = model_key_set(expected_core)
        actual_core_keys = model_key_set(raw_signals, spec_ids)
        missing_core = sorted(expected_core_keys - actual_core_keys)
        unexpected_core = sorted(actual_core_keys - expected_core_keys)
        details["expected_core_model_signal_rows"] = int(len(expected_core))
        details["actual_core_model_signal_rows"] = int(
            len(raw_signals[raw_signals["model_id"].astype(str).isin(spec_ids)])
        )
        details["missing_core_model_condition_hits"] = ["/".join(x) for x in missing_core[:100]]
        details["extra_core_model_rows_from_external_sources"] = ["/".join(x) for x in unexpected_core[:100]]
        if missing_core:
            errors.append(
                "core model condition hits missing from daily_candidate_model_signals_latest.csv: "
                f"{['/'.join(x) for x in missing_core[:20]]}"
            )

    expected_volume = set()
    if not volume.empty:
        for _, row in volume.iterrows():
            sid = normalize_code(row.get("stock_id", ""))
            btype = text(row, "volume_breakout_type", "breakout_type").lower()
            status = text(row, "selection_status").lower()
            if sid and btype in VALID_VOLUME_TYPES and status in VALID_VOLUME_STATUSES:
                expected_volume.add(sid)
    if not candidates.empty:
        for _, row in candidates.iterrows():
            sid = normalize_code(row.get("stock_id", ""))
            if sid and source_volume_breakout_condition(row):
                expected_volume.add(sid)
    missing_volume = sorted(expected_volume - raw_volume_stocks)
    details["expected_volume_breakout_stock_count"] = len(expected_volume)
    details["missing_volume_breakout_model_stocks"] = missing_volume[:50]
    if missing_volume:
        errors.append(f"volume breakout source rows missing from volume_range_breakout model: {missing_volume[:20]}")

    raw_tdcc_short_stocks = stock_set(raw_signals, "tdcc_short_term_continuation_d5_d10")
    missing_tdcc_short = sorted(tdcc_edge_stocks - raw_tdcc_short_stocks)
    details["expected_tdcc_short_stock_count"] = len(tdcc_edge_stocks)
    details["missing_tdcc_short_model_stocks"] = missing_tdcc_short[:50]
    if missing_tdcc_short:
        errors.append(f"TDCC short edge rows missing from tdcc_short_term_continuation_d5_d10 model: {missing_tdcc_short[:20]}")

    # Review-only false-negative tripwires for model conditions whose source
    # formulas are still being tuned. These warn instead of failing the daily
    # pipeline, so they can feed model research without blocking reports.
    if not candidates.empty:
        current_model_keys = {
            (normalize_code(row.get("stock_id", "")), text(row, "model_id"))
            for _, row in raw_signals.iterrows()
        }
        review_missing_w: list[str] = []
        review_missing_breakout: list[str] = []
        for _, row in candidates.iterrows():
            sid = normalize_code(row.get("stock_id", ""))
            if not sid:
                continue
            if cond_w_bottom_right(row) and not already_confirmed_breakout(row):
                if (sid, "w_bottom_right_side") not in current_model_keys:
                    review_missing_w.append(sid)
            vol = num(row, "volume_ratio")
            if (not math.isnan(vol) and vol >= 1.5 and already_confirmed_breakout(row)):
                if (sid, "volume_range_breakout") not in current_model_keys:
                    review_missing_breakout.append(sid)
        details["review_missing_w_bottom_candidates"] = sorted(set(review_missing_w))[:50]
        details["review_missing_breakout_candidates"] = sorted(set(review_missing_breakout))[:50]
        if review_missing_w:
            warnings.append(f"W-bottom flagged candidate rows not in W model, review formula: {sorted(set(review_missing_w))[:20]}")
        if review_missing_breakout:
            warnings.append(f"Confirmed breakout candidate rows not in volume model, review formula/source table: {sorted(set(review_missing_breakout))[:20]}")

    result = {
        "status": "pass" if not errors else "fail",
        "details": details,
        "errors": errors,
        "warnings": warnings,
    }
    return result


def write_report(result: dict[str, Any]) -> None:
    AUDIT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    details = result.get("details", {})
    lines = [
        "# Daily Candidate Model Selection Audit",
        "",
        f"- status: `{result.get('status')}`",
        f"- main_price_date: `{details.get('main_price_date', '')}`",
        f"- all_candidates_rows: `{details.get('all_candidates_rows', 0)}`",
        f"- raw_model_signal_rows: `{details.get('raw_model_signal_rows', 0)}`",
        f"- report_model_signal_rows: `{details.get('report_model_signal_rows', 0)}`",
        f"- selected_condition_error_count: `{details.get('selected_condition_error_count', 0)}`",
        f"- selected_condition_warning_count: `{details.get('selected_condition_warning_count', 0)}`",
        f"- expected_volume_breakout_stock_count: `{details.get('expected_volume_breakout_stock_count', 0)}`",
        f"- expected_tdcc_short_stock_count: `{details.get('expected_tdcc_short_stock_count', 0)}`",
        "",
        "## Errors",
        "",
    ]
    errors = result.get("errors") or []
    lines.extend([f"- {err}" for err in errors] if errors else ["- none"])
    lines.extend(["", "## Warnings", ""])
    warnings = result.get("warnings") or []
    lines.extend([f"- {warn}" for warn in warnings] if warnings else ["- none"])
    lines.extend(["", "## Review Details", ""])
    for key in [
        "missing_volume_breakout_model_stocks",
        "missing_tdcc_short_model_stocks",
        "review_missing_w_bottom_candidates",
        "review_missing_breakout_candidates",
    ]:
        lines.append(f"- {key}: `{details.get(key, [])}`")
    lines.append("")
    AUDIT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    result = audit()
    write_report(result)
    print(f"Saved: {AUDIT_JSON}")
    print(f"Saved: {AUDIT_MD}")
    if result["status"] != "pass":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
