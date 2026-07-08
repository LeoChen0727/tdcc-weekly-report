from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_feature_audit_detail_latest.csv"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

LATEST_CONTRACT_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_research_contract_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_research_contract_detail_latest.csv"
LATEST_STRATIFICATION_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_research_contract_stratification_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_research_contract_latest.md"

HISTORY_CONTRACT_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_research_contract.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_research_contract_detail.csv"
HISTORY_STRATIFICATION_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_research_contract_stratification.csv"

RESEARCH_ID = "volume_range_breakout_v2_research_contract"
ARTIFACT_VERSION = "volume_range_breakout_v2_research_contract_20260709"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_split_feature_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARENT_MODEL_ID = "volume_range_breakout"

ENTRY_RULE_ID = "confirmation_next_open"
CONFIRMATION_RULE_ID = "next_day_continuation_confirmed_close_only"
CONFIRMATION_RULE_ZH = (
    "訊號隔日收盤高於訊號日收盤，且收盤不低於訊號日最高價；"
    "資訊只在確認日收盤後成立，隔日開盤進場。"
)
ENTRY_RULE_ZH = "確認日收盤成立後，下一個交易日開盤進場。"

NO_STOP_EXIT_POLICY_ID = "fixed_d20_close_no_stop_reference"
NO_STOP_EXIT_RULE_ID = "fixed_20d_close"
NO_STOP_EXIT_RULE_ZH = "確認後隔日開盤進場，固定第20個交易日收盤出場；不使用停損，僅作停損比較基準。"
NO_STOP_RULE_ID = "none_no_stop_reference"
NO_STOP_RULE_ZH = "無停損，僅作 research-only 對照。"

EMA23_STOP_EXIT_POLICY_ID = "fixed_d20_close_with_23ema_close_stop"
EMA23_STOP_EXIT_RULE_ID = "ema23_close_stop_or_fixed_20d_close"
EMA23_STOP_EXIT_RULE_ZH = "確認後隔日開盤進場；若未觸發停損，固定第20個交易日收盤出場。"
EMA23_STOP_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
EMA23_STOP_RULE_ZH = "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。"

EXIT_POLICIES = [
    NO_STOP_EXIT_POLICY_ID,
    EMA23_STOP_EXIT_POLICY_ID,
]

MODEL_SPECS = {
    "momentum_continuation": {
        "model_id": "volume_range_breakout_v2_momentum_continuation",
        "model_zh": "動能放量攻擊",
        "candidate_condition_id": "prev60_breakout_momentum_continuation",
        "candidate_condition_zh": (
            "既有 volume_range_breakout 原始訊號；訊號日收盤突破前60日高點至少2%；"
            "同股同期間不重複計算；且不屬於 low_base_loose_flag=True 且 consolidated_any_flag=True 的低位盤整分群。"
        ),
    },
    "low_base_consolidated": {
        "model_id": "volume_range_breakout_v2_low_base_consolidation",
        "model_zh": "低位盤整放量突破",
        "candidate_condition_id": "prev60_breakout_low_base_consolidated",
        "candidate_condition_zh": (
            "既有 volume_range_breakout 原始訊號；訊號日收盤突破前60日高點至少2%；"
            "同股同期間不重複計算；off_60d_low_pct<=50、range_width_60_pct<=45，"
            "且 consolidation_type 為 short_consolidation 或 long_consolidation。"
        ),
    },
}

CONTRACT_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "model_id",
    "model_zh",
    "candidate_condition_id",
    "candidate_condition_zh",
    "confirmation_rule_id",
    "confirmation_rule_zh",
    "entry_rule_id",
    "entry_rule_zh",
    "exit_policy_id",
    "exit_rule_id",
    "exit_rule_zh",
    "stop_rule_id",
    "stop_rule_zh",
    "base_metric_scope",
    "extra_condition_policy",
    "production_registry_change",
    "source_confirmed_sample_count",
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
    "stop_exit_count",
    "stop_exit_rate_pct",
    "invalid_return_count",
    "membership_note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "parent_model_id",
    "model_id",
    "model_zh",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "planned_exit_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "exit_policy_id",
    "exit_rule_id",
    "stop_rule_id",
    "stop_price",
    "stop_confirmed_days",
    "candidate_condition_id",
    "confirmation_rule_id",
    "entry_rule_id",
    "split_group_id",
    "same_stock_non_overlap_included",
    "breakout_over_prev60_pct",
    "volume_ratio",
    "signal_return_1d_pct",
    "range_width_20_pct",
    "range_width_60_pct",
    "off_60d_low_pct",
    "position_in_60d_range_pct",
    "consolidation_type",
    "follow_through_type",
    "limit_up_like",
    "low_base_loose_flag",
    "consolidated_any_flag",
    "hist_return_20d_pct",
    "hist_return_60d_pct",
    "hist_close",
    "hist_ma20",
    "hist_ma60",
    "hist_ma120",
    "hist_ema23",
    "dist_ema23_pct",
    "close_gt_ema23",
    "close_gt_ma20",
    "ma20_gt_ma60",
    "ma60_gt_ma120",
    "tdcc_asof_signal_date",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "return_valid",
    "invalid_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

STRATIFICATION_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "model_id",
    "model_zh",
    "exit_policy_id",
    "stratification_family",
    "stratification_id",
    "stratification_label",
    "condition_expression",
    "condition_role",
    "baseline_sample_size",
    "sample_size",
    "coverage_pct",
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
    "baseline_win_rate_pct",
    "baseline_loss_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "win_rate_delta_pct",
    "loss_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
    "decision_hint",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class StratificationSpec:
    family: str
    stratification_id: str
    label: str
    expression: str
    mask_builder: Callable[[pd.DataFrame], pd.Series]


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


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() else text


def to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def pct_round(value: float, digits: int = 4) -> float | str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return round(float(value), digits)


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


def false_text() -> str:
    return "False"


def trueish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "1.0", "yes", "y"})


def numeric(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame.get(column, pd.Series(index=frame.index, dtype=float)), errors="coerce")


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


def prepare_source_detail() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        raise SystemExit("ERROR: split feature audit detail is empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: source detail must come from volume_range_breakout_v2_split_feature_audit")
    if not set(source.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain research-only approved_for_daily=False")
    if source.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique in split feature detail")

    source = source[source["same_stock_non_overlap_included"].astype(str).eq("True")].copy()
    if source.empty:
        raise SystemExit("ERROR: no same-stock non-overlap source rows")
    if set(source["split_group_id"].astype(str)) != {"momentum_continuation", "low_base_consolidated"}:
        raise SystemExit("ERROR: source must split into exactly momentum_continuation and low_base_consolidated")

    for col in [
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "range_width_20_pct",
        "range_width_60_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "hist_return_20d_pct",
        "hist_return_60d_pct",
        "hist_close",
        "hist_ma20",
        "hist_ma60",
        "hist_ma120",
        "hist_ema23",
        "dist_ema23_pct",
    ]:
        source[col] = pd.to_numeric(source.get(col, ""), errors="coerce")
    return source


def load_tdcc_events() -> pd.DataFrame:
    if not TDCC_EVENTS_CSV.exists():
        return pd.DataFrame()
    tdcc = read_csv(TDCC_EVENTS_CSV)
    if tdcc.empty:
        return tdcc
    tdcc["stock_id"] = tdcc.get("stock_id", pd.Series(dtype=str)).map(normalize_stock_id)
    tdcc["signal_date"] = tdcc.get("signal_date", pd.Series(dtype=str)).map(normalize_date)
    tdcc["tdcc_rank_num"] = pd.to_numeric(tdcc.get("tdcc_rank", ""), errors="coerce")
    tdcc = tdcc[(tdcc["stock_id"].ne("")) & (tdcc["signal_date"].ne(""))].copy()
    return tdcc.sort_values(["stock_id", "signal_date", "tdcc_rank_num"], ascending=[True, True, True])


def attach_tdcc_flags(events: pd.DataFrame, tdcc: pd.DataFrame) -> pd.DataFrame:
    out = events.copy()
    out["tdcc_asof_signal_date"] = ""
    out["tdcc_list_type"] = "no_tdcc"
    out["tdcc_rank"] = ""
    out["tdcc_weekly_increase_top20"] = "False"
    out["tdcc_any_top20"] = "False"
    if tdcc.empty:
        return out

    grouped = {stock_id: part.copy() for stock_id, part in tdcc.groupby("stock_id", dropna=False)}
    asof_dates: list[str] = []
    list_types: list[str] = []
    ranks: list[str] = []
    weekly_top20: list[str] = []
    any_top20: list[str] = []
    for _, row in out.iterrows():
        stock_id = normalize_stock_id(row.get("stock_id"))
        asof_date = normalize_date(row.get("confirmation_date")) or normalize_date(row.get("signal_date"))
        part = grouped.get(stock_id, pd.DataFrame())
        selected = pd.DataFrame()
        if not part.empty and asof_date:
            eligible = part[part["signal_date"].astype(str).le(asof_date)].copy()
            if not eligible.empty:
                latest_date = eligible["signal_date"].max()
                selected = eligible[eligible["signal_date"].eq(latest_date)].sort_values("tdcc_rank_num").head(1)
        if selected.empty:
            asof_dates.append("")
            list_types.append("no_tdcc")
            ranks.append("")
            weekly_top20.append("False")
            any_top20.append("False")
            continue
        selected_row = selected.iloc[0]
        rank = to_float(selected_row.get("tdcc_rank"))
        list_type = safe_str(selected_row.get("tdcc_list_type")) or "unknown_tdcc"
        asof_dates.append(normalize_date(selected_row.get("signal_date")))
        list_types.append(list_type)
        ranks.append(str(int(rank)) if not math.isnan(rank) else "")
        weekly_top20.append(bool_text(list_type == "weekly_increase" and not math.isnan(rank) and rank <= 20))
        any_top20.append(bool_text(not math.isnan(rank) and rank <= 20))
    out["tdcc_asof_signal_date"] = asof_dates
    out["tdcc_list_type"] = list_types
    out["tdcc_rank"] = ranks
    out["tdcc_weekly_increase_top20"] = weekly_top20
    out["tdcc_any_top20"] = any_top20
    return out


def price_for_stock(stock_id: str) -> pd.DataFrame:
    path = PRICE_HISTORY_DIR / f"{normalize_stock_id(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if price.empty or "date" not in price.columns:
        return pd.DataFrame()
    out = price.copy()
    out["date"] = out["date"].map(normalize_date)
    for col in ["open", "high", "low", "close"]:
        out[col] = pd.to_numeric(out.get(col, ""), errors="coerce")
    out = out.dropna(subset=["date", "open", "close"]).sort_values("date").reset_index(drop=True)
    out["ma20"] = out["close"].rolling(20, min_periods=20).mean()
    out["ema23"] = out["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return out


def exact_index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].astype(str).eq(normalize_date(date))].tolist()
    return int(matches[0]) if matches else None


def lower_ma_stop_price(price_row: pd.Series) -> float:
    refs = [to_float(price_row.get("ma20")), to_float(price_row.get("ema23"))]
    refs = [value for value in refs if not math.isnan(value) and value > 0]
    if not refs:
        return math.nan
    return min(refs) * 0.96


def simulate_exit_policy(row: pd.Series, exit_policy_id: str, price_cache: dict[str, pd.DataFrame]) -> dict[str, Any]:
    stock_id = normalize_stock_id(row.get("stock_id"))
    price = price_cache.setdefault(stock_id, price_for_stock(stock_id))
    if price.empty:
        return {"return_valid": "False", "invalid_reason": "missing_price_history"}

    entry_idx = exact_index_for_date(price, row.get("entry_date"))
    if entry_idx is None:
        return {"return_valid": "False", "invalid_reason": "missing_entry_date"}
    planned_exit_idx = entry_idx + 19
    if planned_exit_idx >= len(price):
        return {"return_valid": "False", "invalid_reason": "insufficient_20d_forward_price"}

    entry_price = to_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"return_valid": "False", "invalid_reason": "missing_entry_open"}

    planned_exit = price.iloc[planned_exit_idx]
    exit_idx = planned_exit_idx
    exit_price = to_float(planned_exit.get("close"))
    exit_reason = "fixed_20d_close"
    stop_price = math.nan
    stop_days = 0
    if exit_policy_id == EMA23_STOP_EXIT_POLICY_ID:
        for idx in range(entry_idx, planned_exit_idx):
            current = price.iloc[idx]
            close = to_float(current.get("close"))
            stop_price = lower_ma_stop_price(current)
            if not math.isnan(stop_price) and not math.isnan(close) and close <= stop_price:
                stop_days += 1
            else:
                stop_days = 0
            if stop_days >= 4:
                exit_idx = idx + 1
                exit_price = to_float(price.iloc[exit_idx].get("open"))
                exit_reason = EMA23_STOP_RULE_ID
                break

    if math.isnan(exit_price) or exit_price <= 0:
        return {"return_valid": "False", "invalid_reason": "missing_exit_price"}
    return_pct = (exit_price / entry_price - 1.0) * 100.0
    return {
        "planned_exit_date": safe_str(price.iloc[planned_exit_idx].get("date")),
        "exit_date": safe_str(price.iloc[exit_idx].get("date")),
        "entry_price": pct_round(entry_price),
        "exit_price": pct_round(exit_price),
        "return_pct": pct_round(return_pct),
        "return_outcome": "win" if return_pct > 0 else "loss" if return_pct < 0 else "neutral",
        "exit_reason": exit_reason,
        "stop_price": pct_round(stop_price),
        "stop_confirmed_days": stop_days,
        "return_valid": "True",
        "invalid_reason": "",
    }


def enrich_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_version = safe_str(source["artifact_version"].iloc[0])
    source = attach_tdcc_flags(source, load_tdcc_events())
    source["close_gt_ema23"] = (
        pd.to_numeric(source["hist_close"], errors="coerce") > pd.to_numeric(source["hist_ema23"], errors="coerce")
    ).fillna(False).map(bool_text)
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        split_group_id = safe_str(row.get("split_group_id"))
        spec = MODEL_SPECS[split_group_id]
        for exit_policy_id in EXIT_POLICIES:
            simulated = simulate_exit_policy(row, exit_policy_id, price_cache)
            if exit_policy_id == NO_STOP_EXIT_POLICY_ID:
                exit_rule_id = NO_STOP_EXIT_RULE_ID
                stop_rule_id = NO_STOP_RULE_ID
            else:
                exit_rule_id = EMA23_STOP_EXIT_RULE_ID
                stop_rule_id = EMA23_STOP_RULE_ID
            detail_row = {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_artifact_version": source_version,
                "advisory_status": ADVISORY_STATUS,
                "parent_model_id": PARENT_MODEL_ID,
                "model_id": spec["model_id"],
                "model_zh": spec["model_zh"],
                "source_event_key": safe_str(row.get("source_event_key")),
                "stock_id": normalize_stock_id(row.get("stock_id")),
                "stock_name": safe_str(row.get("stock_name")),
                "signal_date": normalize_date(row.get("signal_date")),
                "confirmation_date": normalize_date(row.get("confirmation_date")),
                "entry_date": normalize_date(row.get("entry_date")),
                "exit_policy_id": exit_policy_id,
                "exit_rule_id": exit_rule_id,
                "stop_rule_id": stop_rule_id,
                "candidate_condition_id": spec["candidate_condition_id"],
                "confirmation_rule_id": CONFIRMATION_RULE_ID,
                "entry_rule_id": ENTRY_RULE_ID,
                "split_group_id": split_group_id,
                "same_stock_non_overlap_included": safe_str(row.get("same_stock_non_overlap_included")),
                "breakout_over_prev60_pct": pct_round(to_float(row.get("breakout_over_prev60_pct"))),
                "volume_ratio": pct_round(to_float(row.get("volume_ratio"))),
                "signal_return_1d_pct": pct_round(to_float(row.get("signal_return_1d_pct"))),
                "range_width_20_pct": pct_round(to_float(row.get("range_width_20_pct"))),
                "range_width_60_pct": pct_round(to_float(row.get("range_width_60_pct"))),
                "off_60d_low_pct": pct_round(to_float(row.get("off_60d_low_pct"))),
                "position_in_60d_range_pct": pct_round(to_float(row.get("position_in_60d_range_pct"))),
                "consolidation_type": safe_str(row.get("consolidation_type")),
                "follow_through_type": safe_str(row.get("follow_through_type")),
                "limit_up_like": safe_str(row.get("limit_up_like")),
                "low_base_loose_flag": safe_str(row.get("low_base_loose_flag")),
                "consolidated_any_flag": safe_str(row.get("consolidated_any_flag")),
                "hist_return_20d_pct": pct_round(to_float(row.get("hist_return_20d_pct"))),
                "hist_return_60d_pct": pct_round(to_float(row.get("hist_return_60d_pct"))),
                "hist_close": pct_round(to_float(row.get("hist_close"))),
                "hist_ma20": pct_round(to_float(row.get("hist_ma20"))),
                "hist_ma60": pct_round(to_float(row.get("hist_ma60"))),
                "hist_ma120": pct_round(to_float(row.get("hist_ma120"))),
                "hist_ema23": pct_round(to_float(row.get("hist_ema23"))),
                "dist_ema23_pct": pct_round(to_float(row.get("dist_ema23_pct"))),
                "close_gt_ema23": safe_str(row.get("close_gt_ema23")),
                "close_gt_ma20": safe_str(row.get("close_gt_ma20")),
                "ma20_gt_ma60": safe_str(row.get("ma20_gt_ma60")),
                "ma60_gt_ma120": safe_str(row.get("ma60_gt_ma120")),
                "tdcc_asof_signal_date": safe_str(row.get("tdcc_asof_signal_date")),
                "tdcc_list_type": safe_str(row.get("tdcc_list_type")),
                "tdcc_rank": safe_str(row.get("tdcc_rank")),
                "tdcc_weekly_increase_top20": safe_str(row.get("tdcc_weekly_increase_top20")),
                "tdcc_any_top20": safe_str(row.get("tdcc_any_top20")),
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
            detail_row.update(simulated)
            rows.append(detail_row)
    return pd.DataFrame(rows)


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    valid = part[part["return_valid"].astype(str).eq("True")].copy()
    returns = pd.to_numeric(valid.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
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
        }
    outcomes = valid["return_outcome"].astype(str)
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
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
    }


def exit_policy_text(exit_policy_id: str) -> dict[str, str]:
    if exit_policy_id == NO_STOP_EXIT_POLICY_ID:
        return {
            "exit_rule_id": NO_STOP_EXIT_RULE_ID,
            "exit_rule_zh": NO_STOP_EXIT_RULE_ZH,
            "stop_rule_id": NO_STOP_RULE_ID,
            "stop_rule_zh": NO_STOP_RULE_ZH,
        }
    return {
        "exit_rule_id": EMA23_STOP_EXIT_RULE_ID,
        "exit_rule_zh": EMA23_STOP_EXIT_RULE_ZH,
        "stop_rule_id": EMA23_STOP_RULE_ID,
        "stop_rule_zh": EMA23_STOP_RULE_ZH,
    }


def build_contract(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_version = safe_str(detail["source_artifact_version"].iloc[0])
    rows: list[dict[str, Any]] = []
    for split_group_id, spec in MODEL_SPECS.items():
        model_detail = detail[detail["model_id"].astype(str).eq(spec["model_id"])]
        contract_row = {
            "research_id": RESEARCH_ID,
            "artifact_version": ARTIFACT_VERSION,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_artifact_version": source_version,
            "advisory_status": ADVISORY_STATUS,
            "row_type": "model_contract",
            "parent_model_id": PARENT_MODEL_ID,
            "model_id": spec["model_id"],
            "model_zh": spec["model_zh"],
            "candidate_condition_id": spec["candidate_condition_id"],
            "candidate_condition_zh": spec["candidate_condition_zh"],
            "confirmation_rule_id": CONFIRMATION_RULE_ID,
            "confirmation_rule_zh": CONFIRMATION_RULE_ZH,
            "entry_rule_id": ENTRY_RULE_ID,
            "entry_rule_zh": ENTRY_RULE_ZH,
            "base_metric_scope": "confirmed_same_stock_non_overlap_only",
            "extra_condition_policy": "stratification_only_no_hidden_gate",
            "production_registry_change": "False",
            "source_confirmed_sample_count": model_detail["source_event_key"].nunique(),
            "membership_note": f"split_group_id={split_group_id}; mutually exclusive v2 research split",
            "approved_for_daily": false_text(),
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        rows.append(contract_row)
        for exit_policy_id in EXIT_POLICIES:
            part = model_detail[model_detail["exit_policy_id"].astype(str).eq(exit_policy_id)]
            valid = part[part["return_valid"].astype(str).eq("True")]
            row = dict(contract_row)
            row["row_type"] = "base_performance"
            row["exit_policy_id"] = exit_policy_id
            row.update(exit_policy_text(exit_policy_id))
            row.update(return_metrics(part))
            row["stop_exit_count"] = int(valid["exit_reason"].astype(str).eq(EMA23_STOP_RULE_ID).sum())
            row["stop_exit_rate_pct"] = pct_round(row["stop_exit_count"] / int(row["sample_size"]) * 100.0, 2) if int(row["sample_size"]) else ""
            row["invalid_return_count"] = int(part["return_valid"].astype(str).ne("True").sum())
            row["membership_note"] = "base performance uses confirmed samples only; TDCC/technical rows are not gates"
            rows.append(row)
    return pd.DataFrame(rows)


def stratification_specs() -> list[StratificationSpec]:
    return [
        StratificationSpec("tdcc", "tdcc_weekly_increase_top20", "TDCC weekly_increase rank <=20", "tdcc_list_type == weekly_increase AND tdcc_rank <= 20", lambda d: trueish(d["tdcc_weekly_increase_top20"])),
        StratificationSpec("tdcc", "tdcc_any_top20", "TDCC any list rank <=20", "tdcc_rank <= 20", lambda d: trueish(d["tdcc_any_top20"])),
        StratificationSpec("technical_23ema", "tech_close_gt_ema23", "signal close > EMA23", "hist_close > hist_ema23", lambda d: trueish(d["close_gt_ema23"])),
        StratificationSpec("technical_23ema", "tech_dist_ema23_0_to_15", "0% <= distance to EMA23 <= 15%", "0 <= dist_ema23_pct <= 15", lambda d: numeric(d, "dist_ema23_pct").between(0, 15, inclusive="both")),
        StratificationSpec("technical_23ema", "tech_ret20_0_to_25", "20d return 0% to 25%", "0 <= hist_return_20d_pct <= 25", lambda d: numeric(d, "hist_return_20d_pct").between(0, 25, inclusive="both")),
        StratificationSpec("technical_23ema", "tech_close_gt_ma20", "signal close > MA20", "close_gt_ma20 == True", lambda d: trueish(d["close_gt_ma20"])),
        StratificationSpec("technical_ma", "tech_ma20_gt_ma60", "MA20 > MA60", "ma20_gt_ma60 == True", lambda d: trueish(d["ma20_gt_ma60"])),
        StratificationSpec("technical_ma", "tech_ma60_gt_ma120", "MA60 > MA120", "ma60_gt_ma120 == True", lambda d: trueish(d["ma60_gt_ma120"])),
        StratificationSpec("signal_quality", "signal_volume_ratio_2_to_6", "volume ratio 2..6", "2 <= volume_ratio <= 6", lambda d: numeric(d, "volume_ratio").between(2, 6, inclusive="both")),
        StratificationSpec("signal_quality", "signal_volume_ratio_gt6", "volume ratio >6", "volume_ratio > 6", lambda d: numeric(d, "volume_ratio").gt(6)),
        StratificationSpec("signal_shape", "signal_non_consolidation", "non-consolidation label", "consolidation_type == non_consolidation", lambda d: d["consolidation_type"].astype(str).eq("non_consolidation")),
    ]


def add_delta(row: dict[str, Any], baseline: dict[str, Any]) -> None:
    for source, target in [
        ("win_rate_pct", "win_rate_delta_pct"),
        ("loss_rate_pct", "loss_rate_delta_pct"),
        ("avg_return_pct", "avg_return_delta_pct"),
        ("median_return_pct", "median_return_delta_pct"),
    ]:
        try:
            row[target] = pct_round(float(row.get(source) or 0.0) - float(baseline.get(source) or 0.0))
        except (TypeError, ValueError):
            row[target] = ""
    row["baseline_win_rate_pct"] = baseline.get("win_rate_pct", "")
    row["baseline_loss_rate_pct"] = baseline.get("loss_rate_pct", "")
    row["baseline_avg_return_pct"] = baseline.get("avg_return_pct", "")
    row["baseline_median_return_pct"] = baseline.get("median_return_pct", "")


def decision_hint(row: dict[str, Any]) -> str:
    sample_size = int(row.get("sample_size") or 0)
    if sample_size < 30:
        return "thin_sample_do_not_use_as_gate"
    try:
        win_delta = float(row.get("win_rate_delta_pct") or 0.0)
        avg_delta = float(row.get("avg_return_delta_pct") or 0.0)
        median_delta = float(row.get("median_return_delta_pct") or 0.0)
    except (TypeError, ValueError):
        return "research_only_review_required"
    if win_delta >= 5.0 and avg_delta >= 1.0 and median_delta >= 0:
        return "positive_stratification_candidate_not_gate"
    if win_delta <= -5.0 or avg_delta <= -1.0:
        return "risk_stratification_candidate_not_gate"
    return "mixed_or_weak_stratification_not_gate"


def build_stratification(detail: pd.DataFrame, contract: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_version = safe_str(detail["source_artifact_version"].iloc[0])
    rows: list[dict[str, Any]] = []
    specs = stratification_specs()
    for model_id, model_detail in detail.groupby("model_id", dropna=False):
        model_zh = safe_str(model_detail["model_zh"].iloc[0])
        for exit_policy_id, exit_detail in model_detail.groupby("exit_policy_id", dropna=False):
            baseline_row = contract[
                contract["row_type"].astype(str).eq("base_performance")
                & contract["model_id"].astype(str).eq(safe_str(model_id))
                & contract["exit_policy_id"].astype(str).eq(safe_str(exit_policy_id))
            ].iloc[0].to_dict()
            baseline_sample = int(baseline_row.get("sample_size") or 0)
            for spec in specs:
                mask = spec.mask_builder(exit_detail).fillna(False)
                selected = exit_detail[mask].copy()
                row = {
                    "research_id": RESEARCH_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "source_research_id": SOURCE_RESEARCH_ID,
                    "source_artifact_version": source_version,
                    "advisory_status": ADVISORY_STATUS,
                    "row_type": "stratification",
                    "parent_model_id": PARENT_MODEL_ID,
                    "model_id": safe_str(model_id),
                    "model_zh": model_zh,
                    "exit_policy_id": safe_str(exit_policy_id),
                    "stratification_family": spec.family,
                    "stratification_id": spec.stratification_id,
                    "stratification_label": spec.label,
                    "condition_expression": spec.expression,
                    "condition_role": "stratification_only_not_candidate_or_confirmation_gate",
                    "baseline_sample_size": baseline_sample,
                    "coverage_pct": "",
                    "approved_for_daily": false_text(),
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
                row.update(return_metrics(selected))
                row["coverage_pct"] = pct_round(int(row["sample_size"]) / baseline_sample * 100.0, 2) if baseline_sample else ""
                add_delta(row, baseline_row)
                row["decision_hint"] = decision_hint(row)
                rows.append(row)
    return pd.DataFrame(rows)


def md_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df[columns].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[col]) for col in columns) + " |")
    return lines


def write_markdown(contract: pd.DataFrame, stratification: pd.DataFrame, path: Path) -> None:
    contracts = contract[contract["row_type"].eq("model_contract")]
    base = contract[contract["row_type"].eq("base_performance")]
    tdcc = stratification[stratification["stratification_family"].eq("tdcc")]
    tech = stratification[stratification["stratification_family"].str.startswith("technical")]
    lines = [
        "# Volume Range Breakout V2 Research Contract",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- status: research-only; does not change `stock_model_contract_registry.csv`, production ranking, operation adapter, or PDF behavior.",
        "- Base metrics use confirmed same-stock non-overlap samples only.",
        "- TDCC top20 and 23EMA-like technical conditions are stratification-only rows, not hidden gates.",
        "- The two v2 model ids are mutually exclusive by split_group_id; their union equals the current raw v2 confirmed non-overlap sample.",
        "",
        "## Model Contracts",
        "",
        *md_table(
            contracts,
            [
                "model_id",
                "model_zh",
                "candidate_condition_id",
                "confirmation_rule_id",
                "entry_rule_id",
                "base_metric_scope",
                "extra_condition_policy",
            ],
            limit=10,
        ),
        "",
        "## Base Performance",
        "",
        *md_table(
            base,
            [
                "model_id",
                "exit_policy_id",
                "sample_size",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "stop_exit_count",
                "invalid_return_count",
            ],
            limit=20,
        ),
        "",
        "## TDCC Stratification",
        "",
        *md_table(
            tdcc,
            [
                "model_id",
                "exit_policy_id",
                "stratification_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            limit=20,
        ),
        "",
        "## 23EMA / Technical Stratification",
        "",
        *md_table(
            tech,
            [
                "model_id",
                "exit_policy_id",
                "stratification_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            limit=28,
        ),
        "",
        "## Outputs",
        "",
        f"- contract_csv: `{LATEST_CONTRACT_CSV.as_posix()}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV.as_posix()}`",
        f"- stratification_csv: `{LATEST_STRATIFICATION_CSV.as_posix()}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    source = prepare_source_detail()
    detail = enrich_detail(source, generated_at)
    contract = build_contract(detail, generated_at)
    stratification = build_stratification(detail, contract, generated_at)

    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(contract, LATEST_CONTRACT_CSV, CONTRACT_COLUMNS)
    write_csv(contract, HISTORY_CONTRACT_CSV, CONTRACT_COLUMNS)
    write_csv(stratification, LATEST_STRATIFICATION_CSV, STRATIFICATION_COLUMNS)
    write_csv(stratification, HISTORY_STRATIFICATION_CSV, STRATIFICATION_COLUMNS)
    write_markdown(contract, stratification, LATEST_MD)
    print(f"Saved: {LATEST_CONTRACT_CSV} rows={len(contract)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_STRATIFICATION_CSV} rows={len(stratification)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
