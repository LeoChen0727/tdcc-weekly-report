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
from matplotlib.patches import Rectangle


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_chart_review.csv"

MODEL_ID = "w_bottom_right_side"
RESEARCH_ID = "w_bottom_candidate_chart_review"
SOURCE_RESEARCH_ID = "w_bottom_candidate_quality_audit"
SOURCE_CANDIDATE_SET_ID = "grid_gap_2_20_rebound_7_12_vol_1_2"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_candidate_chart_review_20260624"

NECKLINE_GAP_MIN_PCT = 2.0
NECKLINE_GAP_MAX_PCT = 20.0
RIGHT_REBOUND_MIN_PCT = 7.0
RIGHT_REBOUND_MAX_PCT = 12.0
SECOND_ARC_VOLUME_RATIO_MIN = 1.2

CATEGORY_FOLDERS = {
    "passed_volume_breakout_confirmation": "01_passed_volume_breakout_confirmation",
    "shape_completed_but_volume_missing": "02_shape_completed_but_volume_missing",
    "candidate_selected_too_near_neckline": "03_candidate_selected_too_near_neckline",
    "right_low_failed": "04_right_low_failed",
    "completion_too_late_for_w": "05_completion_too_late_for_w",
    "did_not_complete_w": "06_did_not_complete_w",
    "other": "99_other",
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
    "model_id",
    "research_id",
    "source_research_id",
    "source_candidate_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "category_id",
    "category_folder",
    "chart_path",
    "chart_path_absolute",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_close",
    "neckline_price",
    "right_low_value",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "second_arc_volume_ratio",
    "sym1_5_quality_bucket",
    "primary_review_flag",
    "sym1_5_w_shape_completed",
    "sym1_5_completion_date",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "sym1_5_right_low_broken",
    "sym1_5_right_low_broken_date",
    "manual_review_status",
    "approved_for_daily",
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


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


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


def bool_text(value: Any) -> str:
    return "true" if safe_str(value).lower() in {"true", "1", "yes", "y"} else "false"


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, digits)


def read_source_audit() -> pd.DataFrame:
    if not SOURCE_AUDIT_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_AUDIT_CSV}")
    audit = pd.read_csv(SOURCE_AUDIT_CSV, dtype=str, keep_default_na=False)
    required = {
        "stock_id",
        "signal_date",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "signal_distance_to_neckline_pct",
        "signal_rebound_from_right_low_pct",
        "second_arc_volume_ratio",
        "primary_review_flag",
        "sym1_5_quality_bucket",
        "approved_for_daily",
    }
    missing = sorted(required - set(audit.columns))
    if missing:
        raise SystemExit(f"ERROR: source audit missing columns: {missing}")
    return audit


def filter_review_candidates(audit: pd.DataFrame) -> pd.DataFrame:
    distance = pd.to_numeric(audit["signal_distance_to_neckline_pct"], errors="coerce")
    rebound = pd.to_numeric(audit["signal_rebound_from_right_low_pct"], errors="coerce")
    volume_ratio = pd.to_numeric(audit["second_arc_volume_ratio"], errors="coerce")
    mask = (
        distance.le(-NECKLINE_GAP_MIN_PCT)
        & distance.ge(-NECKLINE_GAP_MAX_PCT)
        & rebound.ge(RIGHT_REBOUND_MIN_PCT)
        & rebound.le(RIGHT_REBOUND_MAX_PCT)
        & volume_ratio.ge(SECOND_ARC_VOLUME_RATIO_MIN)
    )
    candidates = audit[mask].copy()
    candidates["stock_id"] = candidates["stock_id"].map(normalize_code)
    candidates["signal_date"] = candidates["signal_date"].map(normalize_date)
    candidates = candidates.sort_values(["primary_review_flag", "signal_date", "stock_id"]).reset_index(drop=True)
    return candidates


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    for folder in CATEGORY_FOLDERS.values():
        (CHART_ROOT / folder).mkdir(parents=True, exist_ok=True)


def load_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns:
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "high", "low", "close", "volume", "volume_ma20"]:
        if column in price.columns:
            price[column] = pd.to_numeric(price[column], errors="coerce")
    price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
    return price


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].eq(normalize_date(date))]
    if len(matches) == 0:
        return None
    return int(matches[0])


def category_for(row: pd.Series) -> str:
    flag = safe_str(row.get("primary_review_flag"))
    return flag if flag in CATEGORY_FOLDERS else "other"


def chart_filename(row: pd.Series) -> str:
    stock_id = normalize_code(row.get("stock_id"))
    signal_date = normalize_date(row.get("signal_date"))
    category = category_for(row)
    return f"{signal_date}_{stock_id}_{category}.png"


def chart_window(price: pd.DataFrame, row: pd.Series) -> pd.DataFrame:
    date_candidates = [
        row.get("left_peak_date"),
        row.get("left_low_date"),
        row.get("neckline_date"),
        row.get("right_low_date"),
        row.get("signal_date"),
        row.get("sym1_5_completion_date"),
        row.get("sym1_5_breakout_date"),
        row.get("sym1_5_right_low_broken_date"),
    ]
    indexes = [index_for_date(price, date) for date in date_candidates if normalize_date(date)]
    indexes = [idx for idx in indexes if idx is not None]
    if not indexes:
        return price.tail(90).copy()
    start = max(0, min(indexes) - 8)
    end = min(len(price), max(indexes) + 24)
    return price.iloc[start:end].reset_index(drop=True)


def draw_candles(ax: Any, window: pd.DataFrame) -> None:
    for idx, row in window.iterrows():
        open_price = safe_float(row.get("open"))
        high = safe_float(row.get("high"))
        low = safe_float(row.get("low"))
        close = safe_float(row.get("close"))
        if any(math.isnan(value) for value in [open_price, high, low, close]):
            continue
        color = "#c62828" if close >= open_price else "#2e7d32"
        ax.vlines(idx, low, high, color=color, linewidth=1.0, alpha=0.85)
        bottom = min(open_price, close)
        height = abs(close - open_price)
        if height == 0:
            ax.hlines(close, idx - 0.32, idx + 0.32, color=color, linewidth=1.2)
        else:
            ax.add_patch(Rectangle((idx - 0.28, bottom), 0.56, height, facecolor=color, edgecolor=color, alpha=0.72))


def mark_date(ax: Any, window: pd.DataFrame, date: str, label: str, color: str, linestyle: str = "-") -> None:
    date = normalize_date(date)
    if not date:
        return
    matches = window.index[window["date"].eq(date)]
    if len(matches) == 0:
        return
    idx = int(matches[0])
    ax.axvline(idx, color=color, linestyle=linestyle, linewidth=1.1, alpha=0.82)
    y_min, y_max = ax.get_ylim()
    ax.text(
        idx + 0.15,
        y_max - (y_max - y_min) * 0.04,
        label,
        rotation=90,
        color=color,
        fontsize=7,
        va="top",
        ha="left",
    )


def draw_chart(row: pd.Series, chart_path: Path) -> None:
    stock_id = normalize_code(row.get("stock_id"))
    price = load_price(stock_id)
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
    neckline = safe_float(row.get("neckline_price"))
    right_low = safe_float(row.get("right_low_value"))
    if not math.isnan(neckline):
        ax_price.axhline(neckline, color="#f57c00", linestyle="--", linewidth=1.1, label="neckline")
    if not math.isnan(right_low):
        ax_price.axhline(right_low, color="#6a1b9a", linestyle=":", linewidth=1.0, label="right low")

    mark_date(ax_price, window, row.get("left_peak_date"), "left peak", "#616161")
    mark_date(ax_price, window, row.get("left_low_date"), "low 1", "#1565c0")
    mark_date(ax_price, window, row.get("neckline_date"), "neckline", "#f57c00")
    mark_date(ax_price, window, row.get("right_low_date"), "low 2", "#6a1b9a")
    mark_date(ax_price, window, row.get("signal_date"), "signal", "#d32f2f", "-")
    mark_date(ax_price, window, row.get("sym1_5_completion_date"), "complete", "#00897b", "--")
    mark_date(ax_price, window, row.get("sym1_5_breakout_date"), "volume breakout", "#1b5e20", "-")
    mark_date(ax_price, window, row.get("sym1_5_right_low_broken_date"), "right low broken", "#212121", "--")

    dates = window["date"].tolist()
    tick_step = max(1, len(dates) // 10)
    ticks = list(range(0, len(dates), tick_step))
    if ticks[-1] != len(dates) - 1:
        ticks.append(len(dates) - 1)
    ax_volume.set_xticks(ticks)
    ax_volume.set_xticklabels([dates[idx] for idx in ticks], rotation=35, ha="right", fontsize=8)

    volume_colors = ["#c62828" if safe_float(row.get("close")) >= safe_float(row.get("open")) else "#2e7d32" for _, row in window.iterrows()]
    ax_volume.bar(range(len(window)), window["volume"].fillna(0), color=volume_colors, alpha=0.45, width=0.65)
    if "volume_ma20" in window.columns:
        ax_volume.plot(range(len(window)), window["volume_ma20"], color="#424242", linewidth=1.0, alpha=0.75, label="volume ma20")
    mark_date(ax_volume, window, row.get("signal_date"), "signal", "#d32f2f")

    distance = safe_float(row.get("signal_distance_to_neckline_pct"))
    rebound = safe_float(row.get("signal_rebound_from_right_low_pct"))
    volume_ratio = safe_float(row.get("second_arc_volume_ratio"))
    title = (
        f"{stock_id} signal={normalize_date(row.get('signal_date'))} "
        f"category={category_for(row)} | gap={pct_round(abs(distance))}% "
        f"rebound={pct_round(rebound)}% vol2/1={pct_round(volume_ratio)}"
    )
    ax_price.set_title(title, fontsize=11)
    ax_price.set_ylabel("price")
    ax_volume.set_ylabel("volume")
    ax_price.grid(True, linestyle=":", alpha=0.28)
    ax_volume.grid(True, linestyle=":", alpha=0.2)
    ax_price.legend(loc="upper left", fontsize=8)
    ax_volume.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=130)
    plt.close(fig)


def build_packet(generated_at: str) -> pd.DataFrame:
    audit = read_source_audit()
    candidates = filter_review_candidates(audit)
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for _, source_row in candidates.iterrows():
        category = category_for(source_row)
        folder = CATEGORY_FOLDERS[category]
        chart_path = CHART_ROOT / folder / chart_filename(source_row)
        draw_chart(source_row, chart_path)
        row = {
            "model_id": MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_candidate_set_id": SOURCE_CANDIDATE_SET_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "stock_id": normalize_code(source_row.get("stock_id")),
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": normalize_date(source_row.get("signal_date")),
            "category_id": category,
            "category_folder": folder,
            "chart_path": chart_path.as_posix(),
            "chart_path_absolute": str(chart_path.resolve()),
            "left_peak_date": normalize_date(source_row.get("left_peak_date")),
            "left_low_date": normalize_date(source_row.get("left_low_date")),
            "neckline_date": normalize_date(source_row.get("neckline_date")),
            "right_low_date": normalize_date(source_row.get("right_low_date")),
            "signal_close": source_row.get("signal_close", ""),
            "neckline_price": source_row.get("neckline_price", ""),
            "right_low_value": source_row.get("right_low_value", ""),
            "signal_distance_to_neckline_pct": source_row.get("signal_distance_to_neckline_pct", ""),
            "signal_rebound_from_right_low_pct": source_row.get("signal_rebound_from_right_low_pct", ""),
            "second_arc_volume_ratio": source_row.get("second_arc_volume_ratio", ""),
            "sym1_5_quality_bucket": source_row.get("sym1_5_quality_bucket", ""),
            "primary_review_flag": source_row.get("primary_review_flag", ""),
            "sym1_5_w_shape_completed": bool_text(source_row.get("sym1_5_w_shape_completed", "")),
            "sym1_5_completion_date": normalize_date(source_row.get("sym1_5_completion_date")),
            "sym1_5_neckline_volume_breakout": bool_text(source_row.get("sym1_5_neckline_volume_breakout", "")),
            "sym1_5_breakout_date": normalize_date(source_row.get("sym1_5_breakout_date")),
            "sym1_5_right_low_broken": bool_text(source_row.get("sym1_5_right_low_broken", "")),
            "sym1_5_right_low_broken_date": normalize_date(source_row.get("sym1_5_right_low_broken_date")),
            "manual_review_status": "pending_user_shape_review",
            "approved_for_daily": "false",
            "generated_at": generated_at,
        }
        rows.append(row)
    index = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in chart review index: {forbidden}")
    return index[OUTPUT_COLUMNS]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(data: pd.DataFrame | list[dict[str, Any]], columns: list[str], limit: int = 30) -> list[str]:
    df = data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    if df.empty:
        return ["_No rows._"]
    rows = df.head(limit).to_dict("records")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(col)) for col in columns) + " |")
    return lines


def write_markdown(index: pd.DataFrame, generated_at: str) -> None:
    category_counts = (
        index.groupby(["category_id", "category_folder"], dropna=False)
        .size()
        .reset_index(name="chart_count")
        .sort_values(["category_folder"])
    )
    sample = index[
        [
            "stock_id",
            "signal_date",
            "category_id",
            "signal_distance_to_neckline_pct",
            "signal_rebound_from_right_low_pct",
            "second_arc_volume_ratio",
            "chart_path",
        ]
    ]
    lines = [
        "# W-Bottom Candidate Chart Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_candidate_set_id: `{SOURCE_CANDIDATE_SET_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, or baseline.",
        "",
        "## Candidate Filter",
        "",
        "| rule | value |",
        "| --- | ---: |",
        f"| neckline gap min pct | {NECKLINE_GAP_MIN_PCT} |",
        f"| neckline gap max pct | {NECKLINE_GAP_MAX_PCT} |",
        f"| right rebound min pct | {RIGHT_REBOUND_MIN_PCT} |",
        f"| right rebound max pct | {RIGHT_REBOUND_MAX_PCT} |",
        f"| second arc volume ratio min | {SECOND_ARC_VOLUME_RATIO_MIN} |",
        "",
        "## Folder Counts",
        "",
        *markdown_table(category_counts.to_dict("records"), ["category_id", "category_folder", "chart_count"], limit=20),
        "",
        "## Review Index Sample",
        "",
        *markdown_table(sample, list(sample.columns), limit=30),
        "",
        "## Reading Notes",
        "",
        "- Start with `01_passed_volume_breakout_confirmation` to see the cleanest successful examples.",
        "- Use `02_shape_completed_but_volume_missing` to judge whether volume confirmation is too strict or correctly filtering weak W completions.",
        "- Use `04_right_low_failed` to inspect which shapes should be rejected earlier.",
        "- This packet is for manual shape review only and is not a production model change.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_packet(generated_at)
    if index.empty:
        raise SystemExit("ERROR: W-bottom chart review packet produced no rows")
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
