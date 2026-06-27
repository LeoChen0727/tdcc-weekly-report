from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_quality_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_candidate_quality_audit"
SOURCE_RESEARCH_ID = "w_bottom_tdcc_abc_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_candidate_quality_audit_20260624"

SYMMETRY_RATIOS = ("1.5", "2.0")
CLOSE_ZONE_RATIO = 0.98
INVALID_UNDERCUT_RATIO = 0.97
MAX_ABSOLUTE_W_COMPLETION_DAYS = 60

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

BASE_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "stock_id",
    "stock_name",
    "signal_date",
    "signal_close",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "neckline_price",
    "right_low_value",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "signal_near_neckline_zone",
    "signal_above_neckline",
    "first_rebound_days",
    "right_rebound_days_at_signal",
    "second_arc_volume_ratio",
]

PER_RATIO_COLUMNS = [
    "sym1_5_deadline_total_days",
    "sym1_5_future_days_allowed",
    "sym1_5_price_days_observed",
    "sym1_5_window_complete",
    "sym1_5_w_shape_completed",
    "sym1_5_completion_date",
    "sym1_5_completion_days_from_signal",
    "sym1_5_completion_kind",
    "sym1_5_right_low_broken",
    "sym1_5_right_low_broken_date",
    "sym1_5_late_neckline_completion_not_w",
    "sym1_5_late_completion_date",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "sym1_5_late_volume_breakout_not_w",
    "sym1_5_post_confirmation_trigger_id",
    "sym1_5_quality_bucket",
    "sym2_0_deadline_total_days",
    "sym2_0_future_days_allowed",
    "sym2_0_price_days_observed",
    "sym2_0_window_complete",
    "sym2_0_w_shape_completed",
    "sym2_0_completion_date",
    "sym2_0_completion_days_from_signal",
    "sym2_0_completion_kind",
    "sym2_0_right_low_broken",
    "sym2_0_right_low_broken_date",
    "sym2_0_late_neckline_completion_not_w",
    "sym2_0_late_completion_date",
    "sym2_0_neckline_volume_breakout",
    "sym2_0_breakout_date",
    "sym2_0_late_volume_breakout_not_w",
    "sym2_0_post_confirmation_trigger_id",
    "sym2_0_quality_bucket",
]

TRAILING_COLUMNS = [
    "primary_review_flag",
    "approved_for_daily",
    "generated_at",
]

OUTPUT_COLUMNS = BASE_COLUMNS + PER_RATIO_COLUMNS + TRAILING_COLUMNS

QUALITY_BUCKETS = {
    "neckline_volume_breakout",
    "already_near_neckline_at_signal",
    "completed_without_volume_breakout",
    "right_low_broken_before_completion",
    "future_window_incomplete",
    "late_volume_breakout_not_w",
    "late_neckline_completion_not_w",
    "right_low_broken_after_deadline",
    "no_completion_within_symmetry",
    "price_history_missing",
    "price_date_missing",
    "invalid_price_inputs",
}


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


def safe_int(value: Any) -> int | None:
    number = safe_float(value)
    if math.isnan(number):
        return None
    return int(round(number))


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, digits)


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if not text:
        return ""
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def load_price(stock_id: str, cache: dict[str, pd.DataFrame]) -> pd.DataFrame:
    stock_id = normalize_code(stock_id)
    if stock_id in cache:
        return cache[stock_id]
    path = PRICE_DIR / f"{stock_id}.csv"
    if not path.exists():
        cache[stock_id] = pd.DataFrame()
        return cache[stock_id]
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns:
        cache[stock_id] = pd.DataFrame()
        return cache[stock_id]
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
    cache[stock_id] = price
    return price


def date_index(price: pd.DataFrame) -> dict[str, int]:
    return {normalize_date(date): idx for idx, date in enumerate(price.get("date", []))}


def completion_kind(row: pd.Series, neckline: float) -> str:
    high = safe_float(row.get("high"))
    close = safe_float(row.get("close"))
    if not math.isnan(high) and high >= neckline:
        return "high_touched_neckline"
    if not math.isnan(close) and close >= neckline * CLOSE_ZONE_RATIO:
        return "close_near_neckline"
    return ""


def completion_result(price: pd.DataFrame, event: pd.Series, ratio: str) -> dict[str, Any]:
    prefix = f"sym{ratio.replace('.', '_')}"
    defaults: dict[str, Any] = {
        f"{prefix}_deadline_total_days": "",
        f"{prefix}_future_days_allowed": "",
        f"{prefix}_price_days_observed": "",
        f"{prefix}_window_complete": "false",
        f"{prefix}_w_shape_completed": "false",
        f"{prefix}_completion_date": "",
        f"{prefix}_completion_days_from_signal": "",
        f"{prefix}_completion_kind": "",
        f"{prefix}_right_low_broken": "false",
        f"{prefix}_right_low_broken_date": "",
        f"{prefix}_late_neckline_completion_not_w": "false",
        f"{prefix}_late_completion_date": "",
        f"{prefix}_neckline_volume_breakout": "false",
        f"{prefix}_breakout_date": safe_str(event.get("breakout_date")),
        f"{prefix}_late_volume_breakout_not_w": bool_text(bool_value(event.get("late_breakout_not_w"))),
        f"{prefix}_post_confirmation_trigger_id": safe_str(event.get("post_confirmation_trigger_id")),
        f"{prefix}_quality_bucket": "",
    }
    if price.empty:
        defaults[f"{prefix}_quality_bucket"] = "price_history_missing"
        return defaults

    indexes = date_index(price)
    signal_date = normalize_date(event.get("signal_date"))
    right_low_date = normalize_date(event.get("right_low_date"))
    signal_idx = indexes.get(signal_date)
    right_low_idx = indexes.get(right_low_date)
    if signal_idx is None or right_low_idx is None:
        defaults[f"{prefix}_quality_bucket"] = "price_date_missing"
        return defaults

    neckline = safe_float(event.get("neckline_price"))
    right_low_value = safe_float(price.iloc[right_low_idx].get("low"))
    right_rebound_days = safe_int(event.get("right_rebound_days_at_signal"))
    deadline_total = safe_int(event.get("symmetry_deadline_total_days"))
    if math.isnan(neckline) or math.isnan(right_low_value) or right_rebound_days is None or deadline_total is None:
        defaults[f"{prefix}_quality_bucket"] = "invalid_price_inputs"
        return defaults

    future_days_allowed = max(0, deadline_total - right_rebound_days)
    deadline_idx = min(len(price) - 1, signal_idx + future_days_allowed)
    max_end_idx = min(len(price) - 1, signal_idx + MAX_ABSOLUTE_W_COMPLETION_DAYS)
    price_days_observed = max(0, min(len(price) - 1, signal_idx + future_days_allowed) - signal_idx)
    window_complete = len(price) - 1 >= signal_idx + future_days_allowed
    defaults[f"{prefix}_deadline_total_days"] = deadline_total
    defaults[f"{prefix}_future_days_allowed"] = future_days_allowed
    defaults[f"{prefix}_price_days_observed"] = price_days_observed
    defaults[f"{prefix}_window_complete"] = bool_text(window_complete)

    signal_completion = completion_kind(price.iloc[signal_idx], neckline)
    completion_idx: int | None = signal_idx if signal_completion else None
    completion_kind_value = signal_completion
    late_completion_idx: int | None = None
    invalidation_idx: int | None = None

    for idx in range(signal_idx + 1, max_end_idx + 1):
        low = safe_float(price.iloc[idx].get("low"))
        if not math.isnan(low) and low < right_low_value * INVALID_UNDERCUT_RATIO:
            invalidation_idx = idx
            break
        kind = completion_kind(price.iloc[idx], neckline)
        if not kind:
            continue
        if idx <= deadline_idx and completion_idx is None:
            completion_idx = idx
            completion_kind_value = kind
            break
        if idx > deadline_idx and late_completion_idx is None:
            late_completion_idx = idx
            break

    if completion_idx is not None:
        defaults[f"{prefix}_w_shape_completed"] = "true"
        defaults[f"{prefix}_completion_date"] = normalize_date(price.iloc[completion_idx].get("date"))
        defaults[f"{prefix}_completion_days_from_signal"] = completion_idx - signal_idx
        defaults[f"{prefix}_completion_kind"] = completion_kind_value
    if late_completion_idx is not None:
        defaults[f"{prefix}_late_neckline_completion_not_w"] = "true"
        defaults[f"{prefix}_late_completion_date"] = normalize_date(price.iloc[late_completion_idx].get("date"))
    if invalidation_idx is not None:
        defaults[f"{prefix}_right_low_broken"] = "true"
        defaults[f"{prefix}_right_low_broken_date"] = normalize_date(price.iloc[invalidation_idx].get("date"))

    breakout_date = safe_str(event.get("breakout_date"))
    late_breakout = bool_value(event.get("late_breakout_not_w"))
    if breakout_date:
        defaults[f"{prefix}_neckline_volume_breakout"] = "true"
        bucket = "neckline_volume_breakout"
    elif signal_completion:
        bucket = "already_near_neckline_at_signal"
    elif completion_idx is not None:
        bucket = "completed_without_volume_breakout"
    elif invalidation_idx is not None and invalidation_idx <= deadline_idx:
        bucket = "right_low_broken_before_completion"
    elif not window_complete:
        bucket = "future_window_incomplete"
    elif late_breakout:
        bucket = "late_volume_breakout_not_w"
    elif late_completion_idx is not None:
        bucket = "late_neckline_completion_not_w"
    elif invalidation_idx is not None:
        bucket = "right_low_broken_after_deadline"
    else:
        bucket = "no_completion_within_symmetry"
    defaults[f"{prefix}_quality_bucket"] = bucket
    return defaults


def base_metrics(price: pd.DataFrame, event: pd.Series) -> dict[str, Any]:
    stock_id = normalize_code(event.get("stock_id"))
    signal_close = safe_float(event.get("signal_close"))
    neckline = safe_float(event.get("neckline_price"))
    right_low_value = math.nan
    if not price.empty:
        indexes = date_index(price)
        right_idx = indexes.get(normalize_date(event.get("right_low_date")))
        if right_idx is not None:
            right_low_value = safe_float(price.iloc[right_idx].get("low"))
        signal_idx = indexes.get(normalize_date(event.get("signal_date")))
        if signal_idx is not None and math.isnan(signal_close):
            signal_close = safe_float(price.iloc[signal_idx].get("close"))

    distance = (signal_close / neckline - 1.0) * 100.0 if signal_close > 0 and neckline > 0 else math.nan
    rebound = (signal_close / right_low_value - 1.0) * 100.0 if signal_close > 0 and right_low_value > 0 else math.nan
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "sample_mode": "dedup_approx_20_trading_days",
        "stock_id": stock_id,
        "stock_name": safe_str(event.get("stock_name")),
        "signal_date": normalize_date(event.get("signal_date")),
        "signal_close": pct_round(signal_close),
        "left_peak_date": normalize_date(event.get("left_peak_date")),
        "left_low_date": normalize_date(event.get("left_low_date")),
        "neckline_date": normalize_date(event.get("neckline_date")),
        "right_low_date": normalize_date(event.get("right_low_date")),
        "neckline_price": pct_round(neckline),
        "right_low_value": pct_round(right_low_value),
        "signal_distance_to_neckline_pct": pct_round(distance),
        "signal_rebound_from_right_low_pct": pct_round(rebound),
        "signal_near_neckline_zone": bool_text(not math.isnan(distance) and distance >= -2.0),
        "signal_above_neckline": bool_text(not math.isnan(distance) and distance >= 0.0),
        "first_rebound_days": safe_str(event.get("first_rebound_days")),
        "right_rebound_days_at_signal": safe_str(event.get("right_rebound_days_at_signal")),
        "second_arc_volume_ratio": safe_str(event.get("second_arc_volume_ratio")),
    }


def build_rows(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    events = events.copy()
    events["stock_id"] = events["stock_id"].map(normalize_code)
    events["signal_date"] = events["signal_date"].map(normalize_date)
    events["symmetry_ratio"] = events["symmetry_ratio"].map(safe_str)
    dedup = events["dedup_20d_eligible"].map(bool_value)
    base = events[events["symmetry_ratio"].eq("1.5") & dedup].copy()
    base = base.sort_values(["signal_date", "stock_id"]).reset_index(drop=True)

    ratio_lookup: dict[tuple[str, str, str], pd.Series] = {}
    for _, row in events[dedup].iterrows():
        key = (normalize_code(row.get("stock_id")), normalize_date(row.get("signal_date")), safe_str(row.get("symmetry_ratio")))
        ratio_lookup[key] = row

    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    for _, event in base.iterrows():
        stock_id = normalize_code(event.get("stock_id"))
        signal_date = normalize_date(event.get("signal_date"))
        price = load_price(stock_id, price_cache)
        row = base_metrics(price, event)
        for ratio in SYMMETRY_RATIOS:
            ratio_event = ratio_lookup.get((stock_id, signal_date, ratio), event)
            row.update(completion_result(price, ratio_event, ratio))
        strict_bucket = safe_str(row.get("sym1_5_quality_bucket"))
        if strict_bucket == "neckline_volume_breakout":
            review_flag = "passed_volume_breakout_confirmation"
        elif strict_bucket == "already_near_neckline_at_signal":
            review_flag = "candidate_selected_too_near_neckline"
        elif strict_bucket == "completed_without_volume_breakout":
            review_flag = "shape_completed_but_volume_missing"
        elif strict_bucket in {"right_low_broken_before_completion", "right_low_broken_after_deadline"}:
            review_flag = "right_low_failed"
        elif strict_bucket.startswith("late_"):
            review_flag = "completion_too_late_for_w"
        else:
            review_flag = "did_not_complete_w"
        row["primary_review_flag"] = review_flag
        row["approved_for_daily"] = "false"
        row["generated_at"] = generated_at
        rows.append(row)

    audit = pd.DataFrame(rows)
    for col in OUTPUT_COLUMNS:
        if col not in audit.columns:
            audit[col] = ""
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in audit: {forbidden}")
    invalid_buckets = sorted(
        (set(audit["sym1_5_quality_bucket"].astype(str)) | set(audit["sym2_0_quality_bucket"].astype(str)))
        - QUALITY_BUCKETS
    )
    if invalid_buckets:
        raise SystemExit(f"ERROR: invalid quality buckets: {invalid_buckets}")
    return audit[OUTPUT_COLUMNS]


def markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(col)) for col in columns) + " |")
    return lines


def count_rows(audit: pd.DataFrame, column: str) -> list[dict[str, Any]]:
    counter = Counter(audit[column].astype(str))
    return [{"bucket": bucket, "count": count} for bucket, count in counter.most_common()]


def rate(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return f"{numerator / denominator * 100.0:.2f}%"


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    total = len(audit)
    strict_completed = int(audit["sym1_5_w_shape_completed"].astype(str).eq("true").sum())
    strict_breakout = int(audit["sym1_5_neckline_volume_breakout"].astype(str).eq("true").sum())
    strict_near = int(audit["sym1_5_quality_bucket"].astype(str).eq("already_near_neckline_at_signal").sum())
    loose_completed = int(audit["sym2_0_w_shape_completed"].astype(str).eq("true").sum())
    loose_breakout = int(audit["sym2_0_neckline_volume_breakout"].astype(str).eq("true").sum())
    lines: list[str] = [
        "# W-Bottom Candidate Quality Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{total}` dedup candidates",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this artifact does not update production model conditions, scoring, ranking, or baseline.",
        "- TDCC handling: TDCC is intentionally not used as a W observation-stage quality gate in this audit.",
        "",
        "## Headline Counts",
        "",
        "| metric | strict_symmetry_1_5 | loose_symmetry_2_0 |",
        "| --- | ---: | ---: |",
        f"| W shape completed or already near neckline | {strict_completed} ({rate(strict_completed, total)}) | {loose_completed} ({rate(loose_completed, total)}) |",
        f"| Neckline volume breakout confirmed | {strict_breakout} ({rate(strict_breakout, total)}) | {loose_breakout} ({rate(loose_breakout, total)}) |",
        f"| Already near neckline at signal, without later volume breakout | {strict_near} ({rate(strict_near, total)}) | - |",
        "",
        "## Strict Symmetry 1.5 Quality Buckets",
        "",
        *markdown_table(count_rows(audit, "sym1_5_quality_bucket"), ["bucket", "count"]),
        "",
        "## Loose Symmetry 2.0 Quality Buckets",
        "",
        *markdown_table(count_rows(audit, "sym2_0_quality_bucket"), ["bucket", "count"]),
        "",
        "## Primary Review Flags",
        "",
        *markdown_table(count_rows(audit, "primary_review_flag"), ["bucket", "count"]),
        "",
        "## Candidate Examples Needing Review",
        "",
    ]
    review_sample = audit[
        audit["primary_review_flag"].isin(
            [
                "candidate_selected_too_near_neckline",
                "did_not_complete_w",
                "right_low_failed",
                "completion_too_late_for_w",
            ]
        )
    ].head(30)
    sample_rows = review_sample[
        [
            "stock_id",
            "signal_date",
            "signal_distance_to_neckline_pct",
            "signal_rebound_from_right_low_pct",
            "sym1_5_quality_bucket",
            "primary_review_flag",
        ]
    ].to_dict("records")
    lines.extend(markdown_table(sample_rows, list(sample_rows[0].keys()) if sample_rows else []))
    lines.extend(
        [
            "",
            "## Reading Notes",
            "",
            "- `already_near_neckline_at_signal` means the candidate was already in the neckline completion zone on the signal date, so it may be too late for a right-side early-entry model.",
            "- `completed_without_volume_breakout` means price reached the neckline zone within the symmetry window, but did not satisfy the volume-breakout confirmation rule.",
            "- `late_*_not_w` means the move happened after the symmetry window, so it is treated as a later breakout rather than a clean W-bottom completion.",
        ]
    )
    LATEST_AUDIT_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = read_csv(SOURCE_EVENTS_CSV)
    audit = build_rows(events, generated_at)
    if audit.empty:
        raise SystemExit("ERROR: W-bottom candidate quality audit produced no rows")
    write_csv(audit, LATEST_AUDIT_CSV)
    write_csv(audit, HISTORY_AUDIT_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_AUDIT_MD}")
    print(f"Saved: {HISTORY_AUDIT_CSV} rows={len(audit)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
