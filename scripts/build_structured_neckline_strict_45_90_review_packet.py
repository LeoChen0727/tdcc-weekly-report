from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import shutil

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from build_structured_neckline_dual_window_risk_penalty_audit import (
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
)
from build_structured_neckline_retest_entry_exit_grid import (
    LATEST_DETAIL_CSV as ENTRY_EXIT_DETAIL_CSV,
)
from build_structured_neckline_retest_review_packet import (
    EVENT_FAMILY_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    PRODUCTION_READINESS,
    RESEARCH_VARIANT_ID,
    draw_candles,
    mark_date,
    mark_price,
    metric_text,
    normalize_code,
    normalize_date,
    read_price,
    safe_float,
    safe_path_part,
    safe_str,
)


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_strict_45_90_review_packet"
PARAMETER_SET_ID = "structured_neckline_strict_45_90_review_packet_20260629"
TARGET_RISK_RULE_ID = "strict_45_90_non_bearish"
TARGET_SEGMENT_ID = "low_position_le60_market_bull"
TARGET_STOP_RULE_ID = "signal_low_stop"
REFERENCE_EXIT_RULE_ID = "fixed_20d_close"
MANUAL_REVIEW_STATUS = "pending_user_chart_review"

CHART_ROOT = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_review_packet"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_review_packet_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_review_summary_latest.csv"
LATEST_FLAG_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_review_flags_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_review_packet_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_review_packet.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_review_summary.csv"
HISTORY_FLAG_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_review_flags.csv"

OUTCOME_FOLDER = {
    "win": "01_win",
    "neutral": "02_neutral",
    "loss": "03_loss",
}

INDEX_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "risk_penalty_rule_id",
    "source_event_key",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "reference_price",
    "stop_level",
    "holding_days",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "exit_reason",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "context_45",
    "filter_45",
    "return_45",
    "slope20_45",
    "drawdown_45",
    "context_90",
    "filter_90",
    "return_90",
    "slope20_90",
    "drawdown_90",
    "risk_penalty_points",
    "risk_penalty_flags",
    "review_tags",
    "outcome_folder",
    "chart_window_start_date",
    "chart_window_end_date",
    "chart_path",
    "chart_path_absolute",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "summary_scope_id",
    "outcome_result",
    "sample_size",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "avg_max_close_return_pct",
    "avg_min_close_return_pct",
    "median_low_position_120_pct",
    "median_base_width_pct",
    "top_review_tags",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FLAG_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "review_flag",
    "loss_event_count",
    "success_or_neutral_event_count",
    "total_event_count",
    "loss_share_with_flag_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def to_float(value: Any) -> float:
    try:
        text = safe_str(value)
        if not text:
            return math.nan
        return float(text)
    except (TypeError, ValueError):
        return math.nan


def format_float(value: Any) -> str:
    return metric_text(to_float(value))


def bool_text(value: Any) -> str:
    return safe_str(value).strip().lower()


def event_key(row: pd.Series) -> tuple[str, str, str, str, str]:
    return (
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("signal_date")),
        normalize_date(row.get("retest_date")),
        normalize_date(row.get("retest_attack_date")),
        normalize_date(row.get("retest_entry_date")),
    )


def load_reference_levels() -> pd.DataFrame:
    detail = read_csv(ENTRY_EXIT_DETAIL_CSV)
    required = {
        "event_family_id",
        "segment_id",
        "stop_rule_id",
        "exit_rule_id",
        "stock_id",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "reference_price",
        "stop_level",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: entry/exit source missing columns: {missing}")
    detail = detail[
        detail["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & detail["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
        & detail["stop_rule_id"].astype(str).eq(TARGET_STOP_RULE_ID)
        & detail["exit_rule_id"].astype(str).eq(REFERENCE_EXIT_RULE_ID)
    ].copy()
    if detail.empty:
        raise SystemExit("ERROR: no reference-level rows for strict 45/90 packet")
    detail["_event_key"] = detail.apply(event_key, axis=1)
    detail = detail.drop_duplicates("_event_key", keep="first")
    return detail[["_event_key", "reference_price", "stop_level"]]


def load_source_rows() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "risk_penalty_rule_id",
        "risk_penalty_candidate_accept",
        "source_event_key",
        "event_family_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "market_regime",
        "low_position_120_pct",
        "base_width_pct",
        "support_touch_count",
        "in_low_position_le60_market_bull",
        "entry_price",
        "exit_date",
        "exit_price",
        "holding_days",
        "return_pct",
        "max_close_return_pct",
        "min_close_return_pct",
        "outcome_result",
        "exit_reason",
        "context_45",
        "filter_45",
        "return_45",
        "slope20_45",
        "drawdown_45",
        "context_90",
        "filter_90",
        "return_90",
        "slope20_90",
        "drawdown_90",
        "risk_penalty_points",
        "risk_penalty_flags",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: strict 45/90 source missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source contains forbidden production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & source["risk_penalty_rule_id"].astype(str).eq(TARGET_RISK_RULE_ID)
        & source["risk_penalty_candidate_accept"].map(bool_text).eq("true")
        & source["in_low_position_le60_market_bull"].map(bool_text).eq("true")
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: strict 45/90 low-position bull source produced no rows")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    rows["_event_key"] = rows.apply(event_key, axis=1)
    if rows["_event_key"].duplicated().any():
        duplicated = rows.loc[rows["_event_key"].duplicated(), "_event_key"].head(5).tolist()
        raise SystemExit(f"ERROR: duplicate source event keys: {duplicated}")
    reference = load_reference_levels()
    rows = rows.merge(reference, on="_event_key", how="left", validate="one_to_one")
    if rows[["reference_price", "stop_level"]].eq("").any().any():
        missing = rows.loc[rows["reference_price"].astype(str).eq("") | rows["stop_level"].astype(str).eq(""), ["stock_id", "signal_date", "retest_entry_date"]]
        raise SystemExit(f"ERROR: missing reference/stop levels for rows: {missing.head(5).to_dict('records')}")
    return rows.sort_values(["outcome_result", "return_pct", "signal_date", "stock_id"]).reset_index(drop=True)


def index_for_date(price: pd.DataFrame, date: Any) -> int | None:
    date_text = normalize_date(date)
    if not date_text:
        return None
    matches = price.index[price["date"].astype(str).eq(date_text)].tolist()
    return int(matches[0]) if matches else None


def chart_window(price: pd.DataFrame, row: pd.Series) -> pd.DataFrame:
    anchors = [
        index_for_date(price, row.get("signal_date")),
        index_for_date(price, row.get("retest_date")),
        index_for_date(price, row.get("retest_attack_date")),
        index_for_date(price, row.get("retest_entry_date")),
        index_for_date(price, row.get("exit_date")),
    ]
    found = [idx for idx in anchors if idx is not None]
    if not found:
        return price.tail(140).copy().reset_index(drop=True)
    signal_idx = index_for_date(price, row.get("signal_date"))
    start_anchor = signal_idx if signal_idx is not None else min(found)
    start = max(0, start_anchor - 110)
    end = min(len(price), max(found) + 11)
    return price.iloc[start:end].copy().reset_index(drop=True)


def outcome_folder(value: Any) -> str:
    return OUTCOME_FOLDER.get(safe_str(value), f"99_{safe_path_part(value)}")


def chart_filename(row: pd.Series) -> str:
    return "_".join(
        [
            normalize_date(row.get("signal_date")),
            normalize_code(row.get("stock_id")),
            normalize_date(row.get("retest_entry_date")),
            safe_path_part(row.get("outcome_result")),
            safe_path_part(format_float(row.get("return_pct"))),
        ]
    ) + ".png"


def draw_chart(row: pd.Series, chart_path: Path) -> tuple[str, str]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        raise SystemExit(f"ERROR: missing price history for {stock_id}")
    window = chart_window(price, row)
    if window.empty:
        raise SystemExit(f"ERROR: empty chart window for {stock_id}")

    fig, (ax_price, ax_volume) = plt.subplots(
        2,
        1,
        figsize=(14.0, 8.2),
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 1.0]},
    )
    fig.patch.set_facecolor("white")
    draw_candles(ax_price, window)
    ax_price.grid(True, color="#e0e0e0", linewidth=0.6, alpha=0.75)
    ax_price.set_ylabel("price")
    ax_price.set_title(
        "Strict 45/90 structured neckline review "
        f"{stock_id} outcome={safe_str(row.get('outcome_result'))} "
        f"ret={format_float(row.get('return_pct'))}% max={format_float(row.get('max_close_return_pct'))}%"
    )
    mark_price(ax_price, row.get("reference_price"), "neckline", "#1565c0")
    mark_price(ax_price, row.get("stop_level"), "signal stop", "#6a1b9a")
    mark_price(ax_price, row.get("entry_price"), "entry", "#ef6c00", linestyle=":")
    mark_price(ax_price, row.get("exit_price"), "exit", "#424242", linestyle=":")
    mark_date(ax_price, window, row.get("signal_date"), "signal", "#1565c0")
    mark_date(ax_price, window, row.get("retest_date"), "retest", "#00838f", linestyle="--")
    mark_date(ax_price, window, row.get("retest_attack_date"), "attack", "#ef6c00")
    mark_date(ax_price, window, row.get("retest_entry_date"), "entry", "#bf360c")
    mark_date(ax_price, window, row.get("exit_date"), "exit", "#424242")

    volumes = pd.to_numeric(window.get("volume", ""), errors="coerce").fillna(0)
    colors = ["#c62828" if safe_float(item.get("close")) >= safe_float(item.get("open")) else "#2e7d32" for _, item in window.iterrows()]
    ax_volume.bar(range(len(window)), volumes, color=colors, alpha=0.55, width=0.75)
    ax_volume.set_ylabel("volume")
    tick_step = max(1, len(window) // 12)
    ticks = list(range(0, len(window), tick_step))
    ax_volume.set_xticks(ticks)
    ax_volume.set_xticklabels([safe_str(window.iloc[idx].get("date")) for idx in ticks], rotation=45, ha="right", fontsize=8)
    ax_volume.grid(True, axis="y", color="#e0e0e0", linewidth=0.6, alpha=0.75)

    fig.tight_layout()
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=130)
    plt.close(fig)
    return safe_str(window.iloc[0].get("date")), safe_str(window.iloc[-1].get("date"))


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def review_tags(row: pd.Series) -> list[str]:
    tags: list[str] = []
    ret = to_float(row.get("return_pct"))
    max_ret = to_float(row.get("max_close_return_pct"))
    min_ret = to_float(row.get("min_close_return_pct"))
    low_position = to_float(row.get("low_position_120_pct"))
    base_width = to_float(row.get("base_width_pct"))
    support_touch = to_float(row.get("support_touch_count"))
    return_45 = to_float(row.get("return_45"))
    drawdown_45 = to_float(row.get("drawdown_45"))
    return_90 = to_float(row.get("return_90"))
    drawdown_90 = to_float(row.get("drawdown_90"))
    slope90 = to_float(row.get("slope20_90"))

    if ret <= -10:
        tags.append("deep_close_loss_le_minus10pct")
    if max_ret < 5:
        tags.append("weak_follow_through_max_close_lt5pct")
    if max_ret >= 5 and ret < 5:
        tags.append("gave_back_after_plus5pct")
    if min_ret <= -10:
        tags.append("deep_adverse_close_le_minus10pct")
    if low_position >= 50:
        tags.append("near_upper_low_position_band_ge50pct")
    if base_width >= 20:
        tags.append("wide_base_over_20pct")
    if support_touch < 3:
        tags.append("thin_support_touches_lt3")
    if return_45 < 0:
        tags.append("short_window_return_negative")
    if drawdown_45 <= -15:
        tags.append("short_window_drawdown_le_minus15pct")
    if return_90 < 0:
        tags.append("long_window_return_negative")
    if drawdown_90 <= -25:
        tags.append("long_window_drawdown_le_minus25pct")
    if slope90 < 0:
        tags.append("long_window_slope_negative")
    if safe_str(row.get("context_45")) == "volatile_mixed":
        tags.append("short_context_volatile_mixed")
    if safe_str(row.get("context_90")) == "volatile_mixed":
        tags.append("long_context_volatile_mixed")
    return sorted(set(tags))


def build_index(generated_at: str) -> pd.DataFrame:
    source = load_source_rows()
    clean_chart_root()
    rows: list[dict[str, str]] = []
    for _, item in source.iterrows():
        folder = CHART_ROOT / outcome_folder(item.get("outcome_result"))
        chart_path = folder / chart_filename(item)
        window_start, window_end = draw_chart(item, chart_path)
        tags = review_tags(item)
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
                "source_event_key": safe_str(item.get("source_event_key")),
                "event_family_id": EVENT_FAMILY_ID,
                "segment_id": TARGET_SEGMENT_ID,
                "stock_id": normalize_code(item.get("stock_id")),
                "stock_name": safe_str(item.get("stock_name")),
                "signal_date": normalize_date(item.get("signal_date")),
                "retest_date": normalize_date(item.get("retest_date")),
                "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                "exit_date": normalize_date(item.get("exit_date")),
                "entry_price": format_float(item.get("entry_price")),
                "exit_price": format_float(item.get("exit_price")),
                "reference_price": format_float(item.get("reference_price")),
                "stop_level": format_float(item.get("stop_level")),
                "holding_days": safe_str(item.get("holding_days")),
                "return_pct": format_float(item.get("return_pct")),
                "max_close_return_pct": format_float(item.get("max_close_return_pct")),
                "min_close_return_pct": format_float(item.get("min_close_return_pct")),
                "outcome_result": safe_str(item.get("outcome_result")),
                "exit_reason": safe_str(item.get("exit_reason")),
                "market_regime": safe_str(item.get("market_regime")),
                "low_position_120_pct": format_float(item.get("low_position_120_pct")),
                "base_width_pct": format_float(item.get("base_width_pct")),
                "support_touch_count": safe_str(item.get("support_touch_count")),
                "context_45": safe_str(item.get("context_45")),
                "filter_45": safe_str(item.get("filter_45")),
                "return_45": format_float(item.get("return_45")),
                "slope20_45": format_float(item.get("slope20_45")),
                "drawdown_45": format_float(item.get("drawdown_45")),
                "context_90": safe_str(item.get("context_90")),
                "filter_90": safe_str(item.get("filter_90")),
                "return_90": format_float(item.get("return_90")),
                "slope20_90": format_float(item.get("slope20_90")),
                "drawdown_90": format_float(item.get("drawdown_90")),
                "risk_penalty_points": safe_str(item.get("risk_penalty_points")),
                "risk_penalty_flags": safe_str(item.get("risk_penalty_flags")),
                "review_tags": ";".join(tags),
                "outcome_folder": outcome_folder(item.get("outcome_result")),
                "chart_window_start_date": window_start,
                "chart_window_end_date": window_end,
                "chart_path": chart_path.relative_to(ROOT).as_posix(),
                "chart_path_absolute": str(chart_path.resolve()),
                "manual_review_status": MANUAL_REVIEW_STATUS,
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    index = pd.DataFrame(rows)
    for column in INDEX_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: output contains forbidden production fields: {forbidden}")
    return index[INDEX_COLUMNS]


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def numeric_summary(group: pd.DataFrame, column: str, stat: str) -> str:
    values = pd.to_numeric(group[column], errors="coerce").dropna()
    if values.empty:
        return ""
    if stat == "avg":
        return metric_text(float(values.mean()))
    return metric_text(float(values.median()))


def top_tags(group: pd.DataFrame) -> str:
    counts: dict[str, int] = {}
    for value in group["review_tags"].astype(str):
        for tag in [item for item in value.split(";") if item]:
            counts[tag] = counts.get(tag, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:6]
    return ";".join(f"{tag}:{count}" for tag, count in ranked)


def summary_row(scope: str, outcome: str, group: pd.DataFrame, generated_at: str) -> dict[str, str]:
    outcomes = group["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    mature = win + loss
    evaluated = win + neutral + loss
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "summary_scope_id": scope,
        "outcome_result": outcome,
        "sample_size": str(len(group)),
        "unique_stock_count": str(int(group["stock_id"].nunique())) if not group.empty else "0",
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "pure_win_rate_pct": pct_text(win, mature),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, evaluated),
        "avg_return_pct": numeric_summary(group, "return_pct", "avg"),
        "median_return_pct": numeric_summary(group, "return_pct", "median"),
        "avg_max_close_return_pct": numeric_summary(group, "max_close_return_pct", "avg"),
        "avg_min_close_return_pct": numeric_summary(group, "min_close_return_pct", "avg"),
        "median_low_position_120_pct": numeric_summary(group, "low_position_120_pct", "median"),
        "median_base_width_pct": numeric_summary(group, "base_width_pct", "median"),
        "top_review_tags": top_tags(group),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(index: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [summary_row("overall", "all", index, generated_at)]
    for outcome, group in index.groupby("outcome_result", sort=True):
        rows.append(summary_row("by_outcome", safe_str(outcome), group, generated_at))
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    return summary[SUMMARY_COLUMNS]


def build_flags(index: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    all_flags = sorted(
        {
            flag
            for value in index["review_tags"].astype(str)
            for flag in value.split(";")
            if flag
        }
    )
    rows: list[dict[str, str]] = []
    for flag in all_flags:
        has_flag = index["review_tags"].astype(str).str.split(";").apply(lambda parts: flag in parts)
        loss_count = int((has_flag & index["outcome_result"].eq("loss")).sum())
        success_count = int((has_flag & index["outcome_result"].isin(["win", "neutral"])).sum())
        total = loss_count + success_count
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "review_flag": flag,
                "loss_event_count": str(loss_count),
                "success_or_neutral_event_count": str(success_count),
                "total_event_count": str(total),
                "loss_share_with_flag_pct": metric_text(loss_count / total * 100.0 if total else math.nan),
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    flags = pd.DataFrame(rows).sort_values(
        ["loss_event_count", "loss_share_with_flag_pct", "review_flag"],
        ascending=[False, False, True],
    )
    for column in FLAG_COLUMNS:
        if column not in flags.columns:
            flags[column] = ""
    return flags[FLAG_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def write_markdown(index: pd.DataFrame, summary: pd.DataFrame, flags: pd.DataFrame, generated_at: str) -> None:
    review = index[
        [
            "outcome_result",
            "stock_id",
            "stock_name",
            "signal_date",
            "retest_entry_date",
            "exit_date",
            "return_pct",
            "max_close_return_pct",
            "min_close_return_pct",
            "context_45",
            "context_90",
            "review_tags",
            "chart_path",
        ]
    ].copy()
    review["_outcome_order"] = review["outcome_result"].map({"win": 1, "neutral": 2, "loss": 3}).fillna(9)
    review["_return_num"] = pd.to_numeric(review["return_pct"], errors="coerce")
    review = review.sort_values(["_outcome_order", "_return_num"], ascending=[True, False]).drop(columns=["_outcome_order", "_return_num"])
    loss_review = review[review["outcome_result"].eq("loss")].copy()
    loss_flags = flags[pd.to_numeric(flags["loss_event_count"], errors="coerce").fillna(0).gt(0)].copy()
    lines = [
        "# Structured Neckline Strict 45/90 Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        f"- risk_penalty_rule_id: `{TARGET_RISK_RULE_ID}`",
        f"- segment_id: `{TARGET_SEGMENT_ID}`",
        f"- chart_root: `{CHART_ROOT.relative_to(ROOT).as_posix()}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Why This Packet Exists",
        "",
        "This packet isolates the strict 45/90 non-bearish structured-neckline retest rows in the low-position bull segment. It keeps the full 48-row set visible, then tags the 10 loss rows so the next research step can focus on failure patterns instead of changing production rules.",
        "",
        "## Summary",
        "",
        *markdown_table(summary, SUMMARY_COLUMNS, limit=20),
        "",
        "## Loss Review Flags",
        "",
        *markdown_table(loss_flags, FLAG_COLUMNS, limit=40),
        "",
        "## Loss Rows",
        "",
        *markdown_table(loss_review, list(loss_review.columns), limit=40),
        "",
        "## Full Review Index",
        "",
        *markdown_table(review, list(review.columns), limit=80),
        "",
        "## Reading Notes",
        "",
        "- Review `01_win`, `02_neutral`, and `03_loss` side by side before treating any tag as a rule.",
        "- `review_tags` are diagnostic labels, not production filters.",
        "- The chart window starts roughly 110 trading sessions before `signal_date` so the pre-breakout context is visible.",
        "- This is research-only evidence and does not promote structured-neckline logic to production.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_index(generated_at)
    if index.empty:
        raise SystemExit("ERROR: strict 45/90 review packet produced no rows")
    summary = build_summary(index, generated_at)
    flags = build_flags(index, generated_at)
    write_csv(index, LATEST_INDEX_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(flags, LATEST_FLAG_CSV)
    write_csv(index, HISTORY_INDEX_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(flags, HISTORY_FLAG_CSV)
    write_markdown(index, summary, flags, generated_at)
    print(f"Saved: {LATEST_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_FLAG_CSV} rows={len(flags)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved chart root: {CHART_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
