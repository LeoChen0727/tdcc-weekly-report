from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import re
import shutil

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

from build_structured_neckline_retest_entry_exit_grid import (
    EVENT_FAMILY_ID,
    EXIT_RULE_IDS,
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    PRICE_DIR,
    PRODUCTION_READINESS,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    normalize_code,
    normalize_date,
    safe_float,
    safe_str,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

CHART_ROOT = RESEARCH_LATEST_DIR / "structured_neckline_retest_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "structured_neckline_retest_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_retest_review.csv"

RESEARCH_ID = "structured_neckline_retest_review_packet"
PARAMETER_SET_ID = "structured_neckline_retest_review_packet_20260627"
TARGET_SEGMENT_ID = "low_position_le60_market_bull"
TARGET_STOP_RULE_ID = "signal_low_stop"
MANUAL_REVIEW_STATUS = "pending_user_chart_review"

OUTCOME_FOLDER = {
    "win": "01_win",
    "neutral": "02_neutral",
    "loss": "03_loss",
    "incomplete": "04_incomplete",
}

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

OUTPUT_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_family_id",
    "segment_id",
    "stop_rule_id",
    "exit_rule_id",
    "outcome_rule_id",
    "outcome_result",
    "outcome_folder",
    "chart_path",
    "chart_path_absolute",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "exit_date",
    "exit_reason",
    "reference_price",
    "stop_level",
    "entry_price",
    "exit_price",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "tdcc_fresh",
    "tdcc_supportive",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "exit_rule_id",
    "sample_size",
    "unique_stock_count",
    "max_rows_single_stock",
    "max_single_stock_row_share_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "max_return_pct",
    "top5_positive_return_sum_share_pct",
    "avg_return_ex_top5_positive_pct",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def metric_text(value: float, digits: int = 4) -> str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def safe_path_part(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", safe_str(value))
    return text.strip("_") or "unknown"


def read_source_detail() -> pd.DataFrame:
    if not SOURCE_DETAIL_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_DETAIL_CSV}")
    detail = pd.read_csv(SOURCE_DETAIL_CSV, dtype=str, keep_default_na=False)
    required = set(OUTPUT_COLUMNS) - {"research_id", "source_research_id", "source_parameter_set_id", "parameter_set_id", "chart_path", "chart_path_absolute", "outcome_folder", "manual_review_status"}
    required |= {"event_family_id", "segment_id", "stop_rule_id", "exit_rule_id", "outcome_result", "approved_for_daily", "production_readiness"}
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: source detail missing columns: {missing}")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source detail contains production fields: {forbidden}")
    rows = detail[
        detail["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & detail["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
        & detail["stop_rule_id"].astype(str).eq(TARGET_STOP_RULE_ID)
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no rows for target structured-neckline review packet")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    for column in ["reference_price", "stop_level", "entry_price", "exit_price", "return_pct", "mfe_pct", "mae_pct", "low_position_120_pct", "base_width_pct"]:
        rows[column] = pd.to_numeric(rows.get(column, ""), errors="coerce")
    return rows.sort_values(["exit_rule_id", "outcome_result", "signal_date", "stock_id"]).reset_index(drop=True)


def read_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns:
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
    for column in ["open", "high", "low", "close", "volume"]:
        price[column] = pd.to_numeric(price.get(column, ""), errors="coerce")
    return price


def index_for_date(price: pd.DataFrame, date: Any) -> int | None:
    date_text = normalize_date(date)
    if not date_text:
        return None
    matches = price.index[price["date"].astype(str).eq(date_text)].tolist()
    return int(matches[0]) if matches else None


def chart_window(price: pd.DataFrame, row: pd.Series) -> pd.DataFrame:
    indexes = [
        index_for_date(price, row.get("signal_date")),
        index_for_date(price, row.get("retest_date")),
        index_for_date(price, row.get("retest_attack_date")),
        index_for_date(price, row.get("retest_entry_date")),
        index_for_date(price, row.get("exit_date")),
    ]
    found = [idx for idx in indexes if idx is not None]
    if not found:
        return price.tail(90).copy().reset_index(drop=True)
    start = max(0, min(found) - 30)
    end = min(len(price), max(found) + 16)
    return price.iloc[start:end].copy().reset_index(drop=True)


def draw_candles(ax: Any, window: pd.DataFrame) -> None:
    for idx, item in window.iterrows():
        open_price = safe_float(item.get("open"))
        high = safe_float(item.get("high"))
        low = safe_float(item.get("low"))
        close = safe_float(item.get("close"))
        if any(math.isnan(value) for value in [open_price, high, low, close]):
            continue
        color = "#c62828" if close >= open_price else "#2e7d32"
        ax.vlines(idx, low, high, color=color, linewidth=1.0, alpha=0.88)
        bottom = min(open_price, close)
        height = abs(close - open_price)
        if height == 0:
            ax.hlines(close, idx - 0.32, idx + 0.32, color=color, linewidth=1.2)
        else:
            ax.add_patch(Rectangle((idx - 0.28, bottom), 0.56, height, facecolor=color, edgecolor=color, alpha=0.72))


def mark_date(ax: Any, window: pd.DataFrame, date: Any, label: str, color: str, linestyle: str = "-") -> None:
    idx = index_for_date(window, date)
    if idx is None:
        return
    ax.axvline(idx, color=color, linestyle=linestyle, linewidth=1.1, alpha=0.82)
    y_min, y_max = ax.get_ylim()
    ax.text(idx + 0.15, y_max - (y_max - y_min) * 0.04, label, rotation=90, color=color, fontsize=7, va="top", ha="left")


def mark_price(ax: Any, value: Any, label: str, color: str, linestyle: str = "--") -> None:
    price = safe_float(value)
    if math.isnan(price) or price <= 0:
        return
    ax.axhline(price, color=color, linestyle=linestyle, linewidth=1.0, alpha=0.76)
    x_min, x_max = ax.get_xlim()
    ax.text(x_min + (x_max - x_min) * 0.01, price, f"{label} {price:.2f}", color=color, fontsize=7, va="bottom", ha="left")


def draw_chart(row: pd.Series, chart_path: Path) -> None:
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
        figsize=(13.5, 8.0),
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 1.0]},
    )
    fig.patch.set_facecolor("white")
    draw_candles(ax_price, window)
    ax_price.grid(True, color="#e0e0e0", linewidth=0.6, alpha=0.75)
    ax_price.set_ylabel("price")
    ax_price.set_title(
        "Structured neckline retest review "
        f"{stock_id} exit={safe_str(row.get('exit_rule_id'))} outcome={safe_str(row.get('outcome_result'))} "
        f"ret={metric_text(safe_float(row.get('return_pct')))}%"
    )
    mark_price(ax_price, row.get("reference_price"), "neckline", "#1565c0")
    mark_price(ax_price, row.get("stop_level"), "stop", "#6a1b9a")
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
    tick_step = max(1, len(window) // 10)
    ticks = list(range(0, len(window), tick_step))
    ax_volume.set_xticks(ticks)
    ax_volume.set_xticklabels([safe_str(window.iloc[idx].get("date")) for idx in ticks], rotation=45, ha="right", fontsize=8)
    ax_volume.grid(True, axis="y", color="#e0e0e0", linewidth=0.6, alpha=0.75)

    fig.tight_layout()
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=130)
    plt.close(fig)


def exit_folder(exit_rule_id: Any) -> str:
    mapping = {
        "fixed_10d_close": "e01_fixed_10d_close",
        "fixed_20d_close": "e02_fixed_20d_close",
        "tp10_intraday_or_fixed_20d_close": "e03_tp10_intraday_or_fixed_20d",
        "tp10_close_or_neutral_after_5pct_close_20d": "e04_tp10_close_5pct_neutral",
    }
    return mapping.get(safe_str(exit_rule_id), f"e99_{safe_path_part(exit_rule_id)}")


def outcome_folder(outcome: Any) -> str:
    return OUTCOME_FOLDER.get(safe_str(outcome), f"99_{safe_path_part(outcome)}")


def chart_filename(row: pd.Series) -> str:
    parts = [
        normalize_date(row.get("signal_date")),
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("retest_entry_date")),
        safe_path_part(row.get("outcome_result")),
        safe_path_part(metric_text(safe_float(row.get("return_pct")))),
    ]
    return "_".join(parts) + ".png"


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def build_packet(generated_at: str) -> pd.DataFrame:
    source = read_source_detail()
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for _, item in source.iterrows():
        folder = CHART_ROOT / exit_folder(item.get("exit_rule_id")) / outcome_folder(item.get("outcome_result"))
        chart_path = folder / chart_filename(item)
        draw_chart(item, chart_path)
        row = {
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "event_family_id": EVENT_FAMILY_ID,
            "segment_id": TARGET_SEGMENT_ID,
            "stop_rule_id": TARGET_STOP_RULE_ID,
            "exit_rule_id": safe_str(item.get("exit_rule_id")),
            "outcome_rule_id": safe_str(item.get("outcome_rule_id")),
            "outcome_result": safe_str(item.get("outcome_result")),
            "outcome_folder": outcome_folder(item.get("outcome_result")),
            "chart_path": chart_path.as_posix(),
            "chart_path_absolute": str(chart_path.resolve()),
            "stock_id": normalize_code(item.get("stock_id")),
            "stock_name": safe_str(item.get("stock_name")),
            "signal_date": normalize_date(item.get("signal_date")),
            "retest_date": normalize_date(item.get("retest_date")),
            "retest_attack_date": normalize_date(item.get("retest_attack_date")),
            "retest_entry_date": normalize_date(item.get("retest_entry_date")),
            "exit_date": normalize_date(item.get("exit_date")),
            "exit_reason": safe_str(item.get("exit_reason")),
            "reference_price": metric_text(safe_float(item.get("reference_price"))),
            "stop_level": metric_text(safe_float(item.get("stop_level"))),
            "entry_price": metric_text(safe_float(item.get("entry_price"))),
            "exit_price": metric_text(safe_float(item.get("exit_price"))),
            "holding_days": safe_str(item.get("holding_days")),
            "return_pct": metric_text(safe_float(item.get("return_pct"))),
            "mfe_pct": metric_text(safe_float(item.get("mfe_pct"))),
            "mae_pct": metric_text(safe_float(item.get("mae_pct"))),
            "market_regime": safe_str(item.get("market_regime")),
            "low_position_120_pct": metric_text(safe_float(item.get("low_position_120_pct"))),
            "base_width_pct": metric_text(safe_float(item.get("base_width_pct"))),
            "support_touch_count": safe_str(item.get("support_touch_count")),
            "tdcc_fresh": safe_str(item.get("tdcc_fresh")).lower(),
            "tdcc_supportive": safe_str(item.get("tdcc_supportive")).lower(),
            "manual_review_status": MANUAL_REVIEW_STATUS,
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        rows.append(row)
    index = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in packet: {forbidden}")
    return index[OUTPUT_COLUMNS]


def summary_for(group: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(group["return_pct"], errors="coerce").dropna()
    positives = returns[returns > 0].sort_values(ascending=False)
    positive_sum = float(positives.sum()) if len(positives) else math.nan
    top5_sum = float(positives.head(5).sum()) if len(positives) else math.nan
    returns_ex_top5 = returns.drop(index=positives.head(5).index, errors="ignore")
    outcome = group["outcome_result"].astype(str)
    wins = int(outcome.eq("win").sum())
    neutral = int(outcome.eq("neutral").sum())
    losses = int(outcome.eq("loss").sum())
    incomplete = int(outcome.eq("incomplete").sum())
    evaluated = wins + neutral + losses
    mature = wins + losses
    stock_counts = group.groupby("stock_id", dropna=False).size().sort_values(ascending=False)
    max_rows = int(stock_counts.iloc[0]) if len(stock_counts) else 0
    return {
        "exit_rule_id": safe_str(group["exit_rule_id"].iloc[0]),
        "sample_size": str(len(group)),
        "unique_stock_count": str(int(group["stock_id"].nunique())),
        "max_rows_single_stock": str(max_rows),
        "max_single_stock_row_share_pct": metric_text(max_rows / len(group) * 100.0 if len(group) else math.nan),
        "win_count": str(wins),
        "neutral_count": str(neutral),
        "loss_count": str(losses),
        "incomplete_count": str(incomplete),
        "pure_win_rate_pct": metric_text(wins / mature * 100.0 if mature else math.nan),
        "neutral_inclusive_success_rate_pct": metric_text((wins + neutral) / evaluated * 100.0 if evaluated else math.nan),
        "positive_return_rate_pct": metric_text((returns > 0).sum() / len(returns) * 100.0 if len(returns) else math.nan),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "max_return_pct": metric_text(float(returns.max()) if len(returns) else math.nan),
        "top5_positive_return_sum_share_pct": metric_text(top5_sum / positive_sum * 100.0 if positive_sum and positive_sum > 0 else math.nan),
        "avg_return_ex_top5_positive_pct": metric_text(float(returns_ex_top5.mean()) if len(returns_ex_top5) else math.nan),
    }


def build_summary(index: pd.DataFrame) -> pd.DataFrame:
    rows = [summary_for(group) for _, group in index.groupby("exit_rule_id", sort=False)]
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    return summary[SUMMARY_COLUMNS]


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


def write_markdown(index: pd.DataFrame, generated_at: str) -> None:
    summary = build_summary(index)
    review_sample = index[
        [
            "exit_rule_id",
            "outcome_result",
            "stock_id",
            "stock_name",
            "signal_date",
            "retest_entry_date",
            "exit_date",
            "return_pct",
            "mfe_pct",
            "mae_pct",
            "chart_path",
        ]
    ].copy()
    review_sample["_return_num"] = pd.to_numeric(review_sample["return_pct"], errors="coerce")
    review_sample = review_sample.sort_values(["exit_rule_id", "outcome_result", "_return_num"], ascending=[True, True, False]).drop(columns=["_return_num"])
    lines = [
        "# Structured Neckline Retest Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        f"- segment_id: `{TARGET_SEGMENT_ID}`",
        f"- stop_rule_id: `{TARGET_STOP_RULE_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Why This Packet Exists",
        "",
        "This packet isolates the low-position plus bull-market structured-neckline retest entries using `signal_low_stop`. The goal is manual chart review of wins, neutrals, and losses, and a concentration check to see whether the apparent return improvement is driven by only a few outsized winners.",
        "",
        "## Exit Rule Summary",
        "",
        *markdown_table(summary, SUMMARY_COLUMNS, limit=20),
        "",
        "## Review Index",
        "",
        *markdown_table(review_sample, list(review_sample.columns), limit=120),
        "",
        "## Reading Notes",
        "",
        "- Review folders by `exit_rule_id` first, then compare win/neutral/loss charts side by side.",
        "- `top5_positive_return_sum_share_pct` is an outlier concentration check, not a trading rule.",
        "- `avg_return_ex_top5_positive_pct` removes the top five positive-return rows for that exit rule to show whether average return is still supported after excluding the biggest winners.",
        "- This is research-only evidence and does not promote structured-neckline logic to production.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_packet(generated_at)
    if index.empty:
        raise SystemExit("ERROR: structured neckline retest review packet produced no rows")
    write_csv(index, LATEST_INDEX_CSV)
    write_csv(index, HISTORY_INDEX_CSV)
    write_markdown(index, generated_at)
    print(f"Saved: {LATEST_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {LATEST_INDEX_MD}")
    print(f"Saved chart root: {CHART_ROOT}")
    print(f"Saved: {HISTORY_INDEX_CSV} rows={len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
