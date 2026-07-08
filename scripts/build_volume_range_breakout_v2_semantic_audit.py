from __future__ import annotations

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

SOURCE_EVENTS_CSV = ROOT / "output" / "history" / "research" / "volume_breakout_formal_operation_events.csv"
LATEST_OPERATION_SECTION_CSV = ROOT / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv"
LATEST_EVIDENCE_AUDIT_CSV = ROOT / "output" / "latest" / "daily_volume_breakout_operation_evidence_audit_latest.csv"
LEGACY_4989_SIGNAL_CSV = (
    ROOT / "output" / "history" / "daily_model_snapshots" / "daily_candidate_model_signals_for_report_20260703.csv"
)
LEGACY_4989_OPERATION_CSV = (
    ROOT / "output" / "history" / "daily_model_snapshots" / "daily_volume_breakout_operation_section_20260706.csv"
)

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_semantic_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_semantic_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_semantic_audit_20260708"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

RETURN_KEY = "return_pct"
HIGH_RETURN_Q = 0.80
LOW_RETURN_Q = 0.20

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "advisory_status",
    "model_id",
    "source_event_key",
    "duplicate_overlay_count",
    "preferred_tdcc_list_type",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "exit_date",
    "entry_date",
    "return_pct",
    "return_bucket",
    "exit_reason",
    "trigger_id",
    "selected_trigger_id",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "previous_20d_high",
    "previous_40d_high",
    "previous_60d_high",
    "previous_60d_low",
    "breakout_over_prev20_pct",
    "breakout_over_prev40_pct",
    "breakout_over_prev60_pct",
    "high_breakout_20d_met",
    "high_breakout_40d_met",
    "high_breakout_60d_met",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "off_60d_low_pct",
    "position_in_60d_range_pct",
    "anomaly_flag",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "audit_scope",
    "audit_key",
    "sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "min_return_pct",
    "max_return_pct",
    "high_return_share_pct",
    "low_return_share_pct",
    "high_minus_low_pct",
    "value_a",
    "value_b",
    "value_c",
    "status",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


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


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def num_text(value: float | int | str, digits: int = 4) -> str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return safe_str(value)
    if math.isnan(number) or math.isinf(number):
        return ""
    return f"{number:.{digits}f}"


def pct_round(value: float, digits: int = 4) -> float | str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return round(float(value), digits)


def false_text() -> str:
    return "False"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def load_events() -> pd.DataFrame:
    events = read_csv(SOURCE_EVENTS_CSV)
    events = events[
        events.get("selected_for_formal_operation", pd.Series(dtype=str)).astype(str).eq("True")
        & events.get("sample_maturity_status", pd.Series(dtype=str)).astype(str).eq("mature")
    ].copy()
    if events.empty:
        raise SystemExit("ERROR: no mature formal operation events found")
    for column in [
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "low_position_60_pct",
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "tdcc_rank",
    ]:
        if column in events.columns:
            events[column] = pd.to_numeric(events[column], errors="coerce")
    for column in ["stock_id", "signal_date", "confirmation_date", "exit_date", "entry_date"]:
        if column in events.columns:
            events[column] = events[column].map(normalize_date if column.endswith("date") else normalize_code)
    events["stock_id"] = events["stock_id"].map(normalize_code)
    return events


def event_key(row: pd.Series) -> str:
    parts = [
        row.get("stock_id", ""),
        row.get("signal_date", ""),
        row.get("confirmation_date", ""),
        row.get("selected_trigger_id", "") or row.get("trigger_id", ""),
        row.get("entry_date", ""),
        row.get("exit_date", ""),
        safe_str(row.get("entry_price", "")),
        safe_str(row.get("exit_price", "")),
    ]
    return "|".join(safe_str(part) for part in parts)


def dedupe_events(events: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    events = events.copy()
    events["source_event_key"] = events.apply(event_key, axis=1)
    dup_counts = events.groupby("source_event_key", dropna=False).size().rename("duplicate_overlay_count")
    events = events.merge(dup_counts, left_on="source_event_key", right_index=True, how="left")
    events["_preferred"] = events["tdcc_list_type"].astype(str).eq("no_tdcc").astype(int)
    dedup = (
        events.sort_values(["source_event_key", "_preferred"], ascending=[True, False])
        .drop_duplicates("source_event_key", keep="first")
        .drop(columns=["_preferred"])
        .reset_index(drop=True)
    )
    dedup["preferred_tdcc_list_type"] = dedup.get("tdcc_list_type", "")
    return dedup, events


def load_price_cache(stock_ids: pd.Series) -> dict[str, pd.DataFrame]:
    cache: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(set(stock_ids.astype(str))):
        path = PRICE_DIR / f"{stock_id}.csv"
        if not path.exists():
            cache[stock_id] = pd.DataFrame()
            continue
        price = pd.read_csv(path, dtype=str, keep_default_na=False)
        if price.empty or "date" not in price.columns:
            cache[stock_id] = pd.DataFrame()
            continue
        price = price.copy()
        price["date"] = price["date"].map(normalize_date)
        price = price[price["date"] != ""].sort_values("date").reset_index(drop=True)
        for col in ["open", "high", "low", "close", "volume"]:
            price[col] = pd.to_numeric(price.get(col, ""), errors="coerce")
        high = price["high"]
        low = price["low"]
        close = price["close"]
        for window in [20, 40, 60]:
            price[f"previous_{window}d_high"] = high.shift(1).rolling(window, min_periods=window).max()
            price[f"previous_{window}d_low"] = low.shift(1).rolling(window, min_periods=window).min()
            price[f"range_width_{window}_pct_calc"] = (
                (price[f"previous_{window}d_high"] - price[f"previous_{window}d_low"])
                / price[f"previous_{window}d_low"].replace(0, pd.NA)
                * 100.0
            )
        price["off_60d_low_pct_calc"] = (close / price["previous_60d_low"].replace(0, pd.NA) - 1.0) * 100.0
        price["position_in_60d_range_pct_calc"] = (
            (close - price["previous_60d_low"])
            / (price["previous_60d_high"] - price["previous_60d_low"]).replace(0, pd.NA)
            * 100.0
        )
        cache[stock_id] = price
    return cache


def enrich_with_high_windows(dedup: pd.DataFrame) -> pd.DataFrame:
    cache = load_price_cache(dedup["stock_id"])
    enriched_rows: list[dict[str, Any]] = []
    for _, row in dedup.iterrows():
        out = row.to_dict()
        stock_id = safe_str(row.get("stock_id"))
        signal_date = safe_str(row.get("signal_date"))
        price = cache.get(stock_id, pd.DataFrame())
        price_row = pd.DataFrame()
        if not price.empty:
            price_row = price[price["date"].astype(str).eq(signal_date)]
        if not price_row.empty:
            p = price_row.iloc[0]
            close = float(p.get("close")) if not pd.isna(p.get("close")) else math.nan
            for window in [20, 40, 60]:
                prev_high = float(p.get(f"previous_{window}d_high")) if not pd.isna(p.get(f"previous_{window}d_high")) else math.nan
                out[f"previous_{window}d_high"] = pct_round(prev_high)
                breakout = (close / prev_high - 1.0) * 100.0 if prev_high and not math.isnan(prev_high) else math.nan
                out[f"breakout_over_prev{window}_pct"] = pct_round(breakout)
                out[f"high_breakout_{window}d_met"] = "True" if not math.isnan(breakout) and breakout >= 2.0 else "False"
                calc_width = p.get(f"range_width_{window}_pct_calc")
                if window in [40, 60] and (f"range_width_{window}_pct" not in out or pd.isna(out.get(f"range_width_{window}_pct"))):
                    out[f"range_width_{window}_pct"] = pct_round(float(calc_width)) if not pd.isna(calc_width) else ""
            low60 = float(p.get("previous_60d_low")) if not pd.isna(p.get("previous_60d_low")) else math.nan
            out["previous_60d_low"] = pct_round(low60)
            out["off_60d_low_pct"] = pct_round(float(p.get("off_60d_low_pct_calc"))) if not pd.isna(p.get("off_60d_low_pct_calc")) else ""
            out["position_in_60d_range_pct"] = (
                pct_round(float(p.get("position_in_60d_range_pct_calc")))
                if not pd.isna(p.get("position_in_60d_range_pct_calc"))
                else ""
            )
        else:
            for window in [20, 40, 60]:
                out[f"previous_{window}d_high"] = ""
                out[f"breakout_over_prev{window}_pct"] = ""
                out[f"high_breakout_{window}d_met"] = "False"
            out["previous_60d_low"] = ""
            out["off_60d_low_pct"] = ""
            out["position_in_60d_range_pct"] = ""
        enriched_rows.append(out)
    out_df = pd.DataFrame(enriched_rows)
    for col in ["return_pct", "low_position_60_pct", "range_width_20_pct", "volume_ratio", "signal_return_1d_pct"]:
        out_df[col] = pd.to_numeric(out_df.get(col, ""), errors="coerce")
    return out_df


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get(RETURN_KEY, pd.Series(dtype=float)), errors="coerce").dropna()
    sample_size = int(len(returns))
    if sample_size == 0:
        return {
            "sample_size": 0,
            "win_count": 0,
            "neutral_count": 0,
            "loss_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "loss_rate_pct": "",
            "avg_return_pct": "",
            "median_return_pct": "",
            "p10_return_pct": "",
            "p90_return_pct": "",
            "min_return_pct": "",
            "max_return_pct": "",
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
    return {
        "sample_size": sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100.0, 2),
        "loss_rate_pct": pct_round(loss_count / sample_size * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
    }


def summary_base(row_type: str, scope: str, key: str, generated_at: str, note: str = "") -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "audit_scope": scope,
        "audit_key": key,
        "sample_size": "",
        "win_count": "",
        "neutral_count": "",
        "loss_count": "",
        "win_rate_pct": "",
        "neutral_rate_pct": "",
        "loss_rate_pct": "",
        "avg_return_pct": "",
        "median_return_pct": "",
        "p10_return_pct": "",
        "p90_return_pct": "",
        "min_return_pct": "",
        "max_return_pct": "",
        "high_return_share_pct": "",
        "low_return_share_pct": "",
        "high_minus_low_pct": "",
        "value_a": "",
        "value_b": "",
        "value_c": "",
        "status": "",
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def metric_row(row_type: str, scope: str, key: str, part: pd.DataFrame, generated_at: str, note: str = "") -> dict[str, Any]:
    row = summary_base(row_type, scope, key, generated_at, note)
    row.update(return_metrics(part))
    return row


def add_feature_share_rows(rows: list[dict[str, Any]], detail: pd.DataFrame, generated_at: str) -> None:
    returns = pd.to_numeric(detail[RETURN_KEY], errors="coerce")
    low_cut = float(returns.quantile(LOW_RETURN_Q))
    high_cut = float(returns.quantile(HIGH_RETURN_Q))
    low = detail[returns <= low_cut].copy()
    high = detail[returns >= high_cut].copy()
    features = [
        "price_position_type",
        "consolidation_type",
        "classification_id",
        "attack_method",
        "risk_type",
        "trigger_id",
        "candle_quality",
        "follow_through_type",
        "limit_up_like",
    ]
    for feature in features:
        values = sorted(set(detail.get(feature, pd.Series(dtype=str)).fillna("").astype(str)))
        for value in values:
            overall_share = detail[feature].fillna("").astype(str).eq(value).mean() * 100.0
            high_share = high[feature].fillna("").astype(str).eq(value).mean() * 100.0
            low_share = low[feature].fillna("").astype(str).eq(value).mean() * 100.0
            if max(overall_share, high_share, low_share) < 5.0:
                continue
            row = summary_base(
                "high_low_feature_share",
                feature,
                value or "(blank)",
                generated_at,
                "feature share compares top and bottom return quintiles; not a standalone gate",
            )
            row["sample_size"] = len(detail)
            row["high_return_share_pct"] = pct_round(high_share, 2)
            row["low_return_share_pct"] = pct_round(low_share, 2)
            row["high_minus_low_pct"] = pct_round(high_share - low_share, 2)
            row["value_a"] = f"overall_share_pct={num_text(overall_share, 2)}"
            row["value_b"] = f"high_cutoff_pct={num_text(high_cut, 4)}"
            row["value_c"] = f"low_cutoff_pct={num_text(low_cut, 4)}"
            rows.append(row)


def add_numeric_comparison_rows(rows: list[dict[str, Any]], detail: pd.DataFrame, generated_at: str) -> None:
    returns = pd.to_numeric(detail[RETURN_KEY], errors="coerce")
    low_cut = float(returns.quantile(LOW_RETURN_Q))
    high_cut = float(returns.quantile(HIGH_RETURN_Q))
    low = detail[returns <= low_cut].copy()
    high = detail[returns >= high_cut].copy()
    for feature in [
        "low_position_60_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
    ]:
        all_values = pd.to_numeric(detail.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        high_values = pd.to_numeric(high.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        low_values = pd.to_numeric(low.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        row = summary_base(
            "high_low_numeric_median",
            feature,
            "top20_vs_bottom20",
            generated_at,
            "numeric median comparison only; use with sample counts and anomaly checks",
        )
        row["sample_size"] = int(len(all_values))
        row["value_a"] = f"overall_median={num_text(all_values.median())}" if len(all_values) else ""
        row["value_b"] = f"high_median={num_text(high_values.median())};high_n={len(high_values)}" if len(high_values) else ""
        row["value_c"] = f"low_median={num_text(low_values.median())};low_n={len(low_values)}" if len(low_values) else ""
        rows.append(row)


def add_high_breakout_rows(rows: list[dict[str, Any]], detail: pd.DataFrame, generated_at: str) -> None:
    for window in [20, 40, 60]:
        flag = f"high_breakout_{window}d_met"
        part = detail[detail[flag].astype(str).eq("True")]
        row = metric_row(
            "high_window_threshold_metrics",
            "close_ge_previous_high_plus_2pct",
            f"previous_{window}d_high",
            part,
            generated_at,
            "tests stricter previous-high window on the same deduped formal operation events",
        )
        row["value_a"] = f"window_days={window}"
        row["value_b"] = f"baseline_event_count={len(detail)}"
        row["value_c"] = f"coverage_pct={num_text(len(part) / len(detail) * 100.0 if len(detail) else math.nan, 2)}"
        rows.append(row)


def add_subset_rows(rows: list[dict[str, Any]], detail: pd.DataFrame, generated_at: str) -> None:
    subsets: dict[str, pd.Series] = {
        "all_dedup": pd.Series(True, index=detail.index),
        "low_position_60_le_60": pd.to_numeric(detail["low_position_60_pct"], errors="coerce").le(60),
        "low_position_60_le_80": pd.to_numeric(detail["low_position_60_pct"], errors="coerce").le(80),
        "high_position_60_gt_80": pd.to_numeric(detail["low_position_60_pct"], errors="coerce").gt(80),
        "consolidated_any": detail["consolidation_type"].isin(["short_consolidation", "long_consolidation"]),
        "long_consolidation": detail["consolidation_type"].eq("long_consolidation"),
        "short_consolidation": detail["consolidation_type"].eq("short_consolidation"),
        "non_consolidation": detail["consolidation_type"].eq("non_consolidation"),
        "locked_limit_up": detail["limit_up_like"].astype(str).eq("True"),
        "not_locked_limit_up": detail["limit_up_like"].astype(str).eq("False"),
        "low_position_60_le_80_and_consolidated": pd.to_numeric(detail["low_position_60_pct"], errors="coerce").le(80)
        & detail["consolidation_type"].isin(["short_consolidation", "long_consolidation"]),
        "high_position_60_gt_80_non_consolidation": pd.to_numeric(detail["low_position_60_pct"], errors="coerce").gt(80)
        & detail["consolidation_type"].eq("non_consolidation"),
        "volume_attack_not_locked": detail["attack_method"].eq("volume_attack"),
    }
    for key, mask in subsets.items():
        part = detail[mask.fillna(False)]
        rows.append(
            metric_row(
                "semantic_subset_metrics",
                "provisional_semantic_slice",
                key,
                part,
                generated_at,
                "audit slice only; not a production gate",
            )
        )


def add_anomaly_rows(rows: list[dict[str, Any]], detail: pd.DataFrame, generated_at: str) -> None:
    returns = pd.to_numeric(detail[RETURN_KEY], errors="coerce").dropna()
    lower = float(returns.quantile(0.01))
    upper = float(returns.quantile(0.99))
    trimmed = detail[pd.to_numeric(detail[RETURN_KEY], errors="coerce").between(lower, upper)]
    row = metric_row(
        "anomaly_check",
        "trim_return_tail",
        "trim_1pct_each_tail",
        trimmed,
        generated_at,
        "first-pass numeric anomaly check; extremes require manual data quality review before promotion",
    )
    row["value_a"] = f"lower_cutoff={num_text(lower)}"
    row["value_b"] = f"upper_cutoff={num_text(upper)}"
    row["value_c"] = f"removed_rows={len(detail) - len(trimmed)}"
    rows.append(row)
    for key, part in [
        ("top_10_returns", detail.nlargest(10, RETURN_KEY)),
        ("bottom_10_returns", detail.nsmallest(10, RETURN_KEY)),
    ]:
        r = summary_base(
            "anomaly_extreme_list",
            "return_extremes",
            key,
            generated_at,
            "extreme return list stored in detail; inspect before using averages as evidence",
        )
        r["sample_size"] = len(part)
        r["value_a"] = "|".join(part["source_event_key"].astype(str).head(10))
        rows.append(r)


def locked_limit_up_shape_from_snapshot(row: pd.Series) -> bool:
    try:
        open_price = float(row.get("signal_open") or row.get("open") or row.get("signal_open", "nan"))
        high = float(row.get("signal_high") or row.get("high") or "nan")
        low = float(row.get("signal_low") or row.get("low") or "nan")
        close = float(row.get("signal_close") or row.get("close") or "nan")
    except ValueError:
        open_price = high = low = close = math.nan
    daily_return = pd.to_numeric(pd.Series([row.get("signal_return_1d_pct", "")]), errors="coerce").iloc[0]
    if any(math.isnan(value) for value in [open_price, high, low, close, daily_return]):
        return False
    prev_close = close / (1.0 + daily_return / 100.0) if daily_return > -99.0 else math.nan
    range_pct = (high - low) / prev_close * 100.0 if prev_close and not math.isnan(prev_close) else math.nan
    return (
        daily_return >= 9.0
        and close >= high * 0.995
        and open_price >= close * 0.995
        and (high == low or (not math.isnan(range_pct) and range_pct <= 1.0))
    )


def add_4989_guard_row(rows: list[dict[str, Any]], generated_at: str) -> None:
    row = summary_base(
        "evidence_matching_guard",
        "4989_20260703",
        "legacy_locked_limit_up_mismatch",
        generated_at,
        "guard requires evidence confluence to match the source signal classification before buy ranking",
    )
    source_locked = ""
    source_score_components = ""
    if LEGACY_4989_SIGNAL_CSV.exists():
        signal = pd.read_csv(LEGACY_4989_SIGNAL_CSV, dtype=str, keep_default_na=False)
        signal = signal[(signal.get("stock_id", "").astype(str).eq("4989")) & (signal.get("model_id", "").astype(str).eq(MODEL_ID))]
        if not signal.empty:
            s = signal.iloc[0]
            source_score_components = safe_str(s.get("score_components", ""))
            source_locked = str(locked_limit_up_shape_from_snapshot(s))
            if not source_locked:
                source_locked = "False"
    legacy_confluence = ""
    legacy_buyable = ""
    if LEGACY_4989_OPERATION_CSV.exists():
        legacy = pd.read_csv(LEGACY_4989_OPERATION_CSV, dtype=str, keep_default_na=False)
        legacy = legacy[legacy.get("stock_id", "").astype(str).eq("4989")]
        if not legacy.empty:
            legacy_confluence = "|".join(sorted(set(legacy.get("evidence_confluence_id", pd.Series(dtype=str)).astype(str))))
            legacy_buyable = "|".join(sorted(set(legacy.get("buy_rank_eligible", pd.Series(dtype=str)).astype(str))))
    current_included = "False"
    if LATEST_OPERATION_SECTION_CSV.exists():
        current = pd.read_csv(LATEST_OPERATION_SECTION_CSV, dtype=str, keep_default_na=False)
        current_rows = current[
            current.get("stock_id", "").astype(str).eq("4989")
            & current.get("row_type", "").astype(str).eq("data")
            & current.get("pdf_section", "").astype(str).isin(["confirmed_operation", "active_operation"])
        ]
        current_included = "True" if not current_rows.empty else "False"
    current_audit_states = ""
    if LATEST_EVIDENCE_AUDIT_CSV.exists():
        audit = pd.read_csv(LATEST_EVIDENCE_AUDIT_CSV, dtype=str, keep_default_na=False)
        audit_4989 = audit[audit.get("stock_id", "").astype(str).eq("4989")]
        if not audit_4989.empty:
            current_audit_states = "|".join(
                sorted(set(audit_4989.get("operation_lifecycle_state", pd.Series(dtype=str)).astype(str)))
            )
    row["status"] = "guard_required"
    row["value_a"] = f"source_locked_limit_up_met={source_locked};source_contains_bottom_volume_attack={'bottom_volume_attack' in source_score_components}"
    row["value_b"] = f"legacy_evidence_confluence_id={legacy_confluence};legacy_buy_rank_eligible={legacy_buyable}"
    row["value_c"] = f"current_included_in_confirmed_or_active={current_included};current_audit_states={current_audit_states}"
    rows.append(row)


def build_detail(dedup: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    detail = enrich_with_high_windows(dedup)
    returns = pd.to_numeric(detail[RETURN_KEY], errors="coerce")
    low_cut = float(returns.quantile(LOW_RETURN_Q))
    high_cut = float(returns.quantile(HIGH_RETURN_Q))
    anomaly_low = float(returns.quantile(0.01))
    anomaly_high = float(returns.quantile(0.99))
    detail["return_bucket"] = "middle_60pct"
    detail.loc[returns <= low_cut, "return_bucket"] = "bottom_20pct"
    detail.loc[returns >= high_cut, "return_bucket"] = "top_20pct"
    detail["anomaly_flag"] = "none"
    detail.loc[returns < anomaly_low, "anomaly_flag"] = "bottom_1pct_return"
    detail.loc[returns > anomaly_high, "anomaly_flag"] = "top_1pct_return"
    detail["research_id"] = RESEARCH_ID
    detail["artifact_version"] = ARTIFACT_VERSION
    detail["advisory_status"] = ADVISORY_STATUS
    detail["model_id"] = MODEL_ID
    detail["approved_for_daily"] = false_text()
    detail["production_readiness"] = PRODUCTION_READINESS
    detail["generated_at"] = generated_at
    for col in ["trigger_id", "selected_trigger_id"]:
        if col not in detail.columns:
            detail[col] = ""
    return detail


def build_summary(detail: pd.DataFrame, raw_events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    profile = summary_base(
        "dataset_profile",
        "dedupe",
        "raw_vs_dedup",
        generated_at,
        "dedupe key is stock/signal/confirmation/trigger/entry/exit/entry_price/exit_price; prefer no_tdcc overlay",
    )
    profile["sample_size"] = len(detail)
    profile["value_a"] = f"raw_rows={len(raw_events)}"
    profile["value_b"] = f"dedup_rows={len(detail)}"
    profile["value_c"] = f"duplicate_extra_rows={len(raw_events) - len(detail)}"
    rows.append(profile)
    rows.append(metric_row("dataset_profile", "overall", "all_dedup_mature_formal_operations", detail, generated_at))
    add_anomaly_rows(rows, detail, generated_at)
    add_high_breakout_rows(rows, detail, generated_at)
    add_subset_rows(rows, detail, generated_at)
    add_feature_share_rows(rows, detail, generated_at)
    add_numeric_comparison_rows(rows, detail, generated_at)
    add_4989_guard_row(rows, generated_at)
    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    overall = summary[(summary["row_type"].eq("dataset_profile")) & (summary["audit_key"].eq("all_dedup_mature_formal_operations"))]
    high_windows = summary[summary["row_type"].eq("high_window_threshold_metrics")]
    subsets = summary[summary["row_type"].eq("semantic_subset_metrics")]
    guard = summary[summary["row_type"].eq("evidence_matching_guard")]
    lines = [
        "# Volume Range Breakout V2 Semantic Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This is not a production recommendation and does not change `stock_model_contract_registry.csv`.",
        "- Audit goal: compare current `volume_range_breakout` semantics against bottom/base volume attack intent before any v2 promotion.",
        "- Dedupe rule: one underlying trade per stock/signal/confirmation/trigger/entry/exit/entry_price/exit_price, preferring the `no_tdcc` overlay for base semantic analysis.",
        "- Previous-high test: compare current 20-day breakout against stricter 40-day and 60-day previous-high gates on the same deduped formal operation events.",
        "- Guardrail: evidence confluence used for buy ranking must match the source signal classification; the 4989 20260703 legacy locked-limit-up mismatch is recorded as a guard case.",
        "",
        "## Overall",
        "",
        *md_table(
            overall,
            [
                "audit_key",
                "sample_size",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "min_return_pct",
                "max_return_pct",
            ],
        ),
        "",
        "## 20/40/60 Previous High",
        "",
        *md_table(
            high_windows,
            [
                "audit_key",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "value_c",
            ],
        ),
        "",
        "## Semantic Slices",
        "",
        *md_table(
            subsets,
            [
                "audit_key",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
            ],
            limit=30,
        ),
        "",
        "## 4989 Evidence Matching Guard",
        "",
        *md_table(guard, ["audit_key", "status", "value_a", "value_b", "value_c"], limit=10),
        "",
        "## Extreme Return Rows",
        "",
        "- Extreme rows are marked in the detail artifact with `anomaly_flag`.",
        "- These rows must be reviewed before average return is used as promotion evidence.",
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV.as_posix()}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV.as_posix()}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    dedup, raw_events = dedupe_events(load_events())
    detail = build_detail(dedup, generated_at)
    summary = build_summary(detail, raw_events, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_markdown(summary, detail, LATEST_MD)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
