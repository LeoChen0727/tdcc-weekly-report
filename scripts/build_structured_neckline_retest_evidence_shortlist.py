from __future__ import annotations

from dataclasses import dataclass
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
from matplotlib.patches import Rectangle

from build_breakout_family_retest_grid import MAX_RECENT_SWING_POINTS, local_min_indexes
from build_structured_neckline_retest_review_packet import (
    EVENT_FAMILY_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    PRICE_DIR,
    PRODUCTION_READINESS,
    RESEARCH_HISTORY_DIR,
    RESEARCH_LATEST_DIR,
    RESEARCH_VARIANT_ID,
    TARGET_SEGMENT_ID,
    TARGET_STOP_RULE_ID,
    index_for_date,
    metric_text,
    normalize_code,
    normalize_date,
    safe_float,
    safe_path_part,
    safe_str,
)
from build_structured_neckline_retest_review_shortlist import (
    FOCUS_EXIT_RULE_IDS,
    LATEST_INDEX_CSV as SOURCE_SHORTLIST_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    outcome_folder,
)


ROOT = Path(".")
CHART_ROOT = RESEARCH_LATEST_DIR / "structured_neckline_retest_evidence_shortlist"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_evidence_shortlist_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "structured_neckline_retest_evidence_shortlist_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_retest_evidence_shortlist.csv"

RESEARCH_ID = "structured_neckline_retest_evidence_shortlist"
PARAMETER_SET_ID = "structured_neckline_retest_evidence_shortlist_20260628"
MANUAL_REVIEW_STATUS = "pending_user_chart_review"

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
    "selection_reasons",
    "evidence_status",
    "evidence_chart_path",
    "evidence_chart_path_absolute",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "exit_date",
    "reference_price",
    "reconstructed_neckline_price",
    "neckline_anchor_date",
    "neckline_anchor_high",
    "left_support_date",
    "left_support_low",
    "right_support_date",
    "right_support_low",
    "support_price",
    "support_gap_pct",
    "support_touch_count",
    "support_touch_dates",
    "detection_window_start",
    "detection_window_end",
    "visible_context_start",
    "visible_context_end",
    "visual_pre_signal_sessions",
    "visual_pre_signal_return_pct",
    "visual_pre_signal_range_pct",
    "visual_pre_signal_context",
    "base_age_sessions",
    "support_pair_span_sessions",
    "neckline_anchor_age_sessions",
    "base_width_pct",
    "low_position_120_pct",
    "entry_price",
    "exit_price",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class NecklineEvidence:
    evidence_status: str
    detection_start_idx: int
    detection_end_idx: int
    left_idx: int
    right_idx: int
    neckline_idx: int
    neckline_price: float
    support_price: float
    support_gap_pct: float
    support_touch_indexes: tuple[int, ...]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_source() -> pd.DataFrame:
    if not SOURCE_SHORTLIST_CSV.exists():
        raise SystemExit(f"ERROR: missing source shortlist: {SOURCE_SHORTLIST_CSV}")
    source = pd.read_csv(SOURCE_SHORTLIST_CSV, dtype=str, keep_default_na=False)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stop_rule_id",
        "exit_rule_id",
        "outcome_rule_id",
        "outcome_result",
        "selection_reasons",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "exit_date",
        "reference_price",
        "entry_price",
        "exit_price",
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "low_position_120_pct",
        "base_width_pct",
        "support_touch_count",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source shortlist missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source shortlist contains production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & source["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
        & source["stop_rule_id"].astype(str).eq(TARGET_STOP_RULE_ID)
        & source["exit_rule_id"].astype(str).isin(FOCUS_EXIT_RULE_IDS)
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no rows available for evidence shortlist")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
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


def reconstruct_neckline_evidence(price: pd.DataFrame, signal_date: Any) -> NecklineEvidence | None:
    signal_idx = index_for_date(price, signal_date)
    if signal_idx is None or signal_idx < 90:
        return None
    start = max(0, signal_idx - 90)
    window = price.iloc[start:signal_idx].reset_index(drop=True)
    if len(window) < 70:
        return None
    highs = pd.to_numeric(window["high"], errors="coerce").tolist()
    lows = pd.to_numeric(window["low"], errors="coerce").tolist()
    troughs = [item for item in local_min_indexes(lows) if item <= len(window) - 5]
    troughs = troughs[-MAX_RECENT_SWING_POINTS:]
    if len(troughs) < 2:
        return None

    best: tuple[float, int, int, int, float, int, float, float, tuple[int, ...]] | None = None
    for left_pos, left in enumerate(troughs):
        for right in troughs[left_pos + 1 :]:
            separation = right - left
            if separation < 8 or separation > 80:
                continue
            if len(window) - 1 - right > 55:
                continue
            left_low = lows[left]
            right_low = lows[right]
            if left_low <= 0 or right_low <= 0 or math.isnan(left_low) or math.isnan(right_low):
                continue
            support_gap = abs(right_low / left_low - 1.0) * 100.0
            if support_gap > 9.0:
                continue
            support = (left_low + right_low) / 2.0
            high_segment = highs[left + 1 :]
            valid_highs = [(offset + left + 1, value) for offset, value in enumerate(high_segment) if not math.isnan(value)]
            if len(valid_highs) < 5:
                continue
            neckline_idx_local, neckline = max(valid_highs, key=lambda item: (item[1], -item[0]))
            if neckline <= support:
                continue
            depth = (neckline / support - 1.0) * 100.0
            if depth < 6.0:
                continue
            support_touch_indexes = tuple(
                trough
                for trough in troughs
                if left <= trough <= len(window) - 1 and abs(lows[trough] / support - 1.0) * 100.0 <= 6.0
            )
            touches = len(support_touch_indexes)
            score = depth + touches * 3.0 - support_gap
            if best is None or score > best[0]:
                best = (score, left, right, neckline_idx_local, neckline, touches, support, support_gap, support_touch_indexes)

    if best is None:
        return None
    _, left, right, neckline_idx_local, neckline, _, support, support_gap, support_touch_indexes = best
    return NecklineEvidence(
        evidence_status="reconstructed_from_signal_90d_window",
        detection_start_idx=start,
        detection_end_idx=signal_idx - 1,
        left_idx=start + left,
        right_idx=start + right,
        neckline_idx=start + neckline_idx_local,
        neckline_price=neckline,
        support_price=support,
        support_gap_pct=support_gap,
        support_touch_indexes=tuple(start + item for item in support_touch_indexes),
    )


def chart_index_bounds(price: pd.DataFrame, row: pd.Series, evidence: NecklineEvidence) -> tuple[int, int]:
    indexes = [
        evidence.detection_start_idx,
        evidence.detection_end_idx,
        evidence.left_idx,
        evidence.right_idx,
        evidence.neckline_idx,
        index_for_date(price, row.get("signal_date")),
        index_for_date(price, row.get("retest_date")),
        index_for_date(price, row.get("retest_attack_date")),
        index_for_date(price, row.get("retest_entry_date")),
        index_for_date(price, row.get("exit_date")),
    ]
    found = [idx for idx in indexes if idx is not None]
    start = max(0, min(found) - 5)
    end = min(len(price), max(found) + 16)
    return start, end


def chart_window(price: pd.DataFrame, row: pd.Series, evidence: NecklineEvidence) -> pd.DataFrame:
    start, end = chart_index_bounds(price, row, evidence)
    return price.iloc[start:end].copy().reset_index(drop=True)


def return_and_range(price: pd.DataFrame, start_idx: int, end_idx: int) -> tuple[float, float]:
    if start_idx < 0 or end_idx < 0 or start_idx >= len(price) or end_idx >= len(price) or end_idx <= start_idx:
        return math.nan, math.nan
    start_close = safe_float(price.iloc[start_idx].get("close"))
    end_close = safe_float(price.iloc[end_idx].get("close"))
    frame = price.iloc[start_idx : end_idx + 1]
    highest = pd.to_numeric(frame.get("high", ""), errors="coerce").max()
    lowest = pd.to_numeric(frame.get("low", ""), errors="coerce").min()
    return_pct = (end_close / start_close - 1.0) * 100.0 if start_close > 0 and not math.isnan(end_close) else math.nan
    range_pct = (highest / lowest - 1.0) * 100.0 if lowest > 0 and not math.isnan(highest) else math.nan
    return return_pct, range_pct


def classify_visual_context(return_pct: float, range_pct: float) -> str:
    if math.isnan(return_pct) or math.isnan(range_pct):
        return "unknown"
    if return_pct <= -12.0:
        return "bearish"
    if abs(return_pct) <= 8.0 and range_pct <= 35.0:
        return "sideways_or_consolidation"
    if return_pct >= 12.0:
        return "bullish"
    return "mixed"


def local_index(window: pd.DataFrame, price: pd.DataFrame, absolute_idx: int) -> int | None:
    date_text = normalize_date(price.iloc[absolute_idx].get("date")) if 0 <= absolute_idx < len(price) else ""
    return index_for_date(window, date_text)


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
    ax.axvline(idx, color=color, linestyle=linestyle, linewidth=1.05, alpha=0.82)
    y_min, y_max = ax.get_ylim()
    ax.text(idx + 0.15, y_max - (y_max - y_min) * 0.04, label, rotation=90, color=color, fontsize=7, va="top", ha="left")


def mark_price(ax: Any, value: Any, label: str, color: str, linestyle: str = "--") -> None:
    price = safe_float(value)
    if math.isnan(price) or price <= 0:
        return
    ax.axhline(price, color=color, linestyle=linestyle, linewidth=1.05, alpha=0.78)
    x_min, x_max = ax.get_xlim()
    ax.text(x_min + (x_max - x_min) * 0.01, price, f"{label} {price:.2f}", color=color, fontsize=7, va="bottom", ha="left")


def mark_absolute_point(
    ax: Any,
    window: pd.DataFrame,
    price: pd.DataFrame,
    absolute_idx: int,
    y_value: float,
    label: str,
    color: str,
    marker: str,
) -> None:
    idx = local_index(window, price, absolute_idx)
    if idx is None or math.isnan(y_value):
        return
    ax.scatter([idx], [y_value], color=color, s=58, marker=marker, zorder=5)
    ax.text(idx + 0.25, y_value, label, color=color, fontsize=7, va="center", ha="left")


def mark_detection_window(ax: Any, window: pd.DataFrame, price: pd.DataFrame, evidence: NecklineEvidence) -> None:
    start_idx = local_index(window, price, evidence.detection_start_idx)
    end_idx = local_index(window, price, evidence.detection_end_idx)
    if start_idx is None or end_idx is None:
        return
    ax.axvspan(start_idx - 0.5, end_idx + 0.5, color="#e3f2fd", alpha=0.28, zorder=0)
    y_min, y_max = ax.get_ylim()
    ax.text(start_idx + 0.5, y_min + (y_max - y_min) * 0.03, "90d reference window", color="#1565c0", fontsize=7, va="bottom")


def draw_evidence_chart(row: pd.Series, chart_path: Path) -> dict[str, str]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        raise SystemExit(f"ERROR: missing price history for {stock_id}")
    evidence = reconstruct_neckline_evidence(price, row.get("signal_date"))
    if evidence is None:
        raise SystemExit(f"ERROR: unable to reconstruct neckline evidence for {stock_id} {row.get('signal_date')}")
    window = chart_window(price, row, evidence)
    if window.empty:
        raise SystemExit(f"ERROR: empty evidence chart window for {stock_id}")

    fig, (ax_price, ax_volume) = plt.subplots(
        2,
        1,
        figsize=(15.0, 8.8),
        sharex=True,
        gridspec_kw={"height_ratios": [3.4, 1.0]},
    )
    fig.patch.set_facecolor("white")
    draw_candles(ax_price, window)
    ax_price.grid(True, color="#e0e0e0", linewidth=0.6, alpha=0.75)
    ax_price.set_ylabel("price")
    ax_price.set_title(
        "Structured neckline evidence "
        f"{stock_id} exit={safe_str(row.get('exit_rule_id'))} outcome={safe_str(row.get('outcome_result'))} "
        f"ret={metric_text(safe_float(row.get('return_pct')))}%"
    )
    mark_detection_window(ax_price, window, price, evidence)
    mark_price(ax_price, evidence.neckline_price, "neckline", "#1565c0")
    mark_price(ax_price, evidence.support_price, "support avg", "#6a1b9a", linestyle=":")
    mark_price(ax_price, row.get("stop_level"), "stop", "#ad1457", linestyle=":")
    mark_price(ax_price, row.get("entry_price"), "entry", "#ef6c00", linestyle=":")
    mark_price(ax_price, row.get("exit_price"), "exit", "#424242", linestyle=":")

    left_low = safe_float(price.iloc[evidence.left_idx].get("low"))
    right_low = safe_float(price.iloc[evidence.right_idx].get("low"))
    neckline_high = safe_float(price.iloc[evidence.neckline_idx].get("high"))
    mark_absolute_point(ax_price, window, price, evidence.left_idx, left_low, "left support low", "#6a1b9a", "v")
    mark_absolute_point(ax_price, window, price, evidence.right_idx, right_low, "right support low", "#6a1b9a", "v")
    mark_absolute_point(ax_price, window, price, evidence.neckline_idx, neckline_high, "neckline high anchor", "#1565c0", "^")
    for touch_idx in evidence.support_touch_indexes:
        touch_low = safe_float(price.iloc[touch_idx].get("low"))
        mark_absolute_point(ax_price, window, price, touch_idx, touch_low, "touch", "#8e24aa", "o")

    mark_date(ax_price, window, row.get("signal_date"), "signal", "#1565c0")
    mark_date(ax_price, window, row.get("retest_date"), "retest", "#00838f", linestyle="--")
    mark_date(ax_price, window, row.get("retest_attack_date"), "attack", "#ef6c00")
    mark_date(ax_price, window, row.get("retest_entry_date"), "entry", "#bf360c")
    mark_date(ax_price, window, row.get("exit_date"), "exit", "#424242")

    evidence_text = (
        "neckline = max high after left support low before signal; "
        f"support_gap={metric_text(evidence.support_gap_pct)}%; "
        f"touches={len(evidence.support_touch_indexes)}; "
        f"base_width={metric_text(safe_float(row.get('base_width_pct')))}%"
    )
    ax_price.text(
        0.01,
        0.98,
        evidence_text,
        transform=ax_price.transAxes,
        fontsize=8,
        va="top",
        ha="left",
        bbox={"facecolor": "white", "edgecolor": "#bdbdbd", "alpha": 0.82},
    )

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

    support_touch_dates = [normalize_date(price.iloc[idx].get("date")) for idx in evidence.support_touch_indexes]
    signal_idx = index_for_date(price, row.get("signal_date"))
    chart_start_idx, _ = chart_index_bounds(price, row, evidence)
    visible_end_idx = (signal_idx - 1) if signal_idx is not None and signal_idx > 0 else evidence.detection_end_idx
    visual_return, visual_range = return_and_range(price, chart_start_idx, visible_end_idx)
    return {
        "evidence_status": evidence.evidence_status,
        "reconstructed_neckline_price": metric_text(evidence.neckline_price),
        "neckline_anchor_date": normalize_date(price.iloc[evidence.neckline_idx].get("date")),
        "neckline_anchor_high": metric_text(neckline_high),
        "left_support_date": normalize_date(price.iloc[evidence.left_idx].get("date")),
        "left_support_low": metric_text(left_low),
        "right_support_date": normalize_date(price.iloc[evidence.right_idx].get("date")),
        "right_support_low": metric_text(right_low),
        "support_price": metric_text(evidence.support_price),
        "support_gap_pct": metric_text(evidence.support_gap_pct),
        "support_touch_dates": ";".join(support_touch_dates),
        "detection_window_start": normalize_date(price.iloc[evidence.detection_start_idx].get("date")),
        "detection_window_end": normalize_date(price.iloc[evidence.detection_end_idx].get("date")),
        "visible_context_start": normalize_date(price.iloc[chart_start_idx].get("date")),
        "visible_context_end": normalize_date(price.iloc[visible_end_idx].get("date")),
        "visual_pre_signal_sessions": str(visible_end_idx - chart_start_idx + 1),
        "visual_pre_signal_return_pct": metric_text(visual_return),
        "visual_pre_signal_range_pct": metric_text(visual_range),
        "visual_pre_signal_context": classify_visual_context(visual_return, visual_range),
        "base_age_sessions": str(signal_idx - evidence.left_idx) if signal_idx is not None else "",
        "support_pair_span_sessions": str(evidence.right_idx - evidence.left_idx),
        "neckline_anchor_age_sessions": str(signal_idx - evidence.neckline_idx) if signal_idx is not None else "",
    }


def exit_folder(exit_rule_id: Any) -> str:
    mapping = {
        "tp10_intraday_or_fixed_20d_close": "e03_tp10_intraday_or_fixed_20d",
        "tp10_close_or_neutral_after_5pct_close_20d": "e04_tp10_close_5pct_neutral",
    }
    return mapping.get(safe_str(exit_rule_id), f"e99_{safe_path_part(exit_rule_id)}")


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
        raise SystemExit(f"ERROR: refused to clear evidence chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def build_evidence_shortlist(generated_at: str) -> pd.DataFrame:
    source = read_source()
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for _, item in source.iterrows():
        folder = CHART_ROOT / exit_folder(item.get("exit_rule_id")) / outcome_folder(item.get("outcome_result"))
        chart_path = folder / chart_filename(item)
        evidence_fields = draw_evidence_chart(item, chart_path)
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
            "selection_reasons": safe_str(item.get("selection_reasons")),
            "evidence_chart_path": chart_path.as_posix(),
            "evidence_chart_path_absolute": str(chart_path.resolve()),
            "stock_id": normalize_code(item.get("stock_id")),
            "stock_name": safe_str(item.get("stock_name")),
            "signal_date": normalize_date(item.get("signal_date")),
            "retest_date": normalize_date(item.get("retest_date")),
            "retest_attack_date": normalize_date(item.get("retest_attack_date")),
            "retest_entry_date": normalize_date(item.get("retest_entry_date")),
            "exit_date": normalize_date(item.get("exit_date")),
            "reference_price": metric_text(safe_float(item.get("reference_price"))),
            "support_touch_count": safe_str(item.get("support_touch_count")),
            "base_width_pct": metric_text(safe_float(item.get("base_width_pct"))),
            "low_position_120_pct": metric_text(safe_float(item.get("low_position_120_pct"))),
            "entry_price": metric_text(safe_float(item.get("entry_price"))),
            "exit_price": metric_text(safe_float(item.get("exit_price"))),
            "return_pct": metric_text(safe_float(item.get("return_pct"))),
            "mfe_pct": metric_text(safe_float(item.get("mfe_pct"))),
            "mae_pct": metric_text(safe_float(item.get("mae_pct"))),
            "manual_review_status": MANUAL_REVIEW_STATUS,
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
            **evidence_fields,
        }
        rows.append(row)
    index = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in evidence shortlist: {forbidden}")
    return index[OUTPUT_COLUMNS]


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
    summary = (
        index.groupby(["exit_rule_id", "outcome_result"], dropna=False)
        .agg(
            rows=("stock_id", "size"),
            unique_stocks=("stock_id", "nunique"),
            avg_support_gap_pct=("support_gap_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
            avg_base_width_pct=("base_width_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
            avg_visual_pre_signal_return_pct=("visual_pre_signal_return_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
            avg_base_age_sessions=("base_age_sessions", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
        )
        .reset_index()
    )
    visual_context_summary = (
        index.groupby(["outcome_result", "visual_pre_signal_context"], dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
    )
    review_index = index[
        [
            "exit_rule_id",
            "outcome_result",
            "stock_id",
            "stock_name",
            "signal_date",
            "reference_price",
            "neckline_anchor_date",
            "left_support_date",
            "right_support_date",
            "support_gap_pct",
            "visible_context_start",
            "visible_context_end",
            "visual_pre_signal_context",
            "base_age_sessions",
            "evidence_chart_path",
        ]
    ].copy()
    lines = [
        "# Structured Neckline Retest Evidence Shortlist",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this evidence packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Why This Exists",
        "",
        "The previous shortlist charts only drew a horizontal neckline. This packet redraws the same rows with the 90-session reference window, left/right support lows, support average line, support touches, and the high anchor that produced the reconstructed horizontal neckline.",
        "",
        "## Evidence Rule",
        "",
        "- The structured-neckline proxy first finds two recent local support lows within 9% of each other.",
        "- It then sets the horizontal neckline to the maximum high after the left support low and before the signal date.",
        "- The signal date must close above that neckline after the volume-confirmed event has been detected upstream.",
        "- `visual_pre_signal_context` uses the same chart span that the manual reviewer saw: from the evidence chart's left edge to the trading day before the signal date.",
        "",
        "## Summary",
        "",
        *markdown_table(summary, list(summary.columns), limit=20),
        "",
        "## Visual Pre-Signal Context Summary",
        "",
        *markdown_table(visual_context_summary, list(visual_context_summary.columns), limit=40),
        "",
        "## Review Index",
        "",
        *markdown_table(review_index, list(review_index.columns), limit=120),
        "",
        "## Boundary Notes",
        "",
        "- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "- This is chart-evidence clarification only. It does not change the model event selection, exit rules, scoring, ranking, or production contract.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_evidence_shortlist(generated_at)
    write_csv(index, LATEST_INDEX_CSV)
    write_csv(index, HISTORY_INDEX_CSV)
    write_markdown(index, generated_at)
    png_count = len(list(CHART_ROOT.rglob("*.png")))
    print(f"Saved: {LATEST_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {LATEST_INDEX_MD}")
    print(f"Saved chart root: {CHART_ROOT} charts={png_count}")
    print(f"Saved: {HISTORY_INDEX_CSV} rows={len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
