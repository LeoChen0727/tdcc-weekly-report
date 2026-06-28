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

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail_latest.csv"
SOURCE_VARIANT_EVENTS_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_events_latest.csv"
SOURCE_BASELINE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_nm_anchor_chart_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_nearest_micro_anchor_chart_review"
SOURCE_RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_nearest_micro_anchor_chart_review_20260625"
PRODUCTION_READINESS = "not_production_ready_research_only"
PRIMARY_SYMMETRY_RATIO = 1.5

CATEGORY_FOLDERS = {
    "variant_only_win": "01_v_win",
    "variant_only_loss": "02_v_loss",
    "variant_only_pending_or_no_breakout": "03_v_pending",
    "baseline_only_win": "04_b_win",
    "baseline_only_loss": "05_b_loss",
    "baseline_only_pending_or_no_breakout": "06_b_pending",
    "common_variant_win": "07_c_win",
    "common_variant_loss": "08_c_loss",
    "common_variant_pending_or_no_breakout": "09_c_pending",
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
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "comparison_status",
    "selected_event_set_id",
    "outcome_bucket",
    "category_id",
    "category_folder",
    "chart_path",
    "chart_path_absolute",
    "baseline_present",
    "variant_present",
    "baseline_left_peak_date",
    "variant_left_peak_date",
    "baseline_left_low_date",
    "variant_left_low_date",
    "baseline_neckline_date",
    "variant_neckline_date",
    "baseline_right_low_date",
    "variant_right_low_date",
    "baseline_breakout_date",
    "variant_breakout_date",
    "baseline_signal_close",
    "variant_signal_close",
    "baseline_neckline_price",
    "variant_neckline_price",
    "baseline_a_mature",
    "variant_a_mature",
    "baseline_a_return_pct",
    "variant_a_return_pct",
    "baseline_tdcc_any_age7",
    "variant_tdcc_any_age7",
    "variant_left_anchor_rule_id",
    "variant_left_anchor_rule_reason",
    "manual_review_status",
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


def bool_value(value: Any) -> bool:
    return bool_text(value) == "true"


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, digits)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def comparable_events(events: pd.DataFrame) -> pd.DataFrame:
    sample = events[
        events["symmetry_ratio"].astype(float).eq(PRIMARY_SYMMETRY_RATIO)
        & events["dedup_20d_eligible"].astype(str).str.lower().isin(["true", "1"])
    ].copy()
    sample["stock_id"] = sample["stock_id"].map(normalize_code)
    sample["signal_date"] = sample["signal_date"].map(normalize_date)
    return sample.sort_values(["stock_id", "signal_date"]).drop_duplicates(["stock_id", "signal_date"], keep="first")


def event_map(events: pd.DataFrame) -> dict[tuple[str, str], pd.Series]:
    result: dict[tuple[str, str], pd.Series] = {}
    for _, row in comparable_events(events).iterrows():
        result[(normalize_code(row.get("stock_id")), normalize_date(row.get("signal_date")))] = row
    return result


def read_sources() -> tuple[pd.DataFrame, dict[tuple[str, str], pd.Series], dict[tuple[str, str], pd.Series]]:
    detail = read_csv(SOURCE_DETAIL_CSV)
    baseline_events = read_csv(SOURCE_BASELINE_EVENTS_CSV)
    variant_events = read_csv(SOURCE_VARIANT_EVENTS_CSV)
    required_detail = {
        "stock_id",
        "stock_name",
        "signal_date",
        "comparison_status",
        "baseline_present",
        "variant_present",
        "baseline_left_peak_date",
        "variant_left_peak_date",
        "baseline_left_low_date",
        "variant_left_low_date",
        "baseline_neckline_date",
        "variant_neckline_date",
        "baseline_right_low_date",
        "variant_right_low_date",
        "baseline_breakout_date",
        "variant_breakout_date",
        "baseline_a_mature",
        "variant_a_mature",
        "baseline_a_return_pct",
        "variant_a_return_pct",
        "variant_left_anchor_rule_id",
        "variant_left_anchor_rule_reason",
    }
    required_events = {
        "stock_id",
        "signal_date",
        "symmetry_ratio",
        "dedup_20d_eligible",
        "signal_close",
        "neckline_price",
        "tdcc_any_age7",
    }
    missing_detail = sorted(required_detail - set(detail.columns))
    missing_baseline = sorted(required_events - set(baseline_events.columns))
    missing_variant = sorted((required_events | {"left_anchor_rule_id", "left_anchor_rule_reason"}) - set(variant_events.columns))
    if missing_detail:
        raise SystemExit(f"ERROR: source detail missing columns: {missing_detail}")
    if missing_baseline:
        raise SystemExit(f"ERROR: baseline events missing columns: {missing_baseline}")
    if missing_variant:
        raise SystemExit(f"ERROR: variant events missing columns: {missing_variant}")
    detail = detail.copy()
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["signal_date"] = detail["signal_date"].map(normalize_date)
    detail = detail.sort_values(["comparison_status", "signal_date", "stock_id"]).reset_index(drop=True)
    return detail, event_map(baseline_events), event_map(variant_events)


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
    for column in ["open", "high", "low", "close", "volume"]:
        if column in price.columns:
            price[column] = pd.to_numeric(price[column], errors="coerce")
    if "volume" in price.columns:
        price["volume_ma20"] = price["volume"].rolling(20, min_periods=1).mean()
    price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
    return price


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].eq(normalize_date(date))]
    if len(matches) == 0:
        return None
    return int(matches[0])


def selected_event_set(row: pd.Series) -> str:
    status = safe_str(row.get("comparison_status"))
    if status == "baseline_only":
        return "baseline"
    return "variant"


def selected_prefix(row: pd.Series) -> str:
    return selected_event_set(row)


def selected_return(row: pd.Series) -> float:
    return safe_float(row.get(f"{selected_prefix(row)}_a_return_pct"))


def selected_mature(row: pd.Series) -> bool:
    return bool_value(row.get(f"{selected_prefix(row)}_a_mature"))


def outcome_bucket(row: pd.Series) -> str:
    if not selected_mature(row):
        return "pending_or_no_breakout"
    return "win" if selected_return(row) > 0 else "loss"


def category_for(row: pd.Series) -> str:
    status = safe_str(row.get("comparison_status"))
    bucket = outcome_bucket(row)
    if status == "common":
        return f"common_variant_{bucket}"
    return f"{status}_{bucket}"


def chart_filename(row: pd.Series) -> str:
    stock_id = normalize_code(row.get("stock_id"))
    signal_date = normalize_date(row.get("signal_date"))
    folder = CATEGORY_FOLDERS[category_for(row)]
    category_code = folder.split("_", 1)[0]
    return f"{signal_date}_{stock_id}_{category_code}.png"


def row_dates(row: pd.Series) -> list[str]:
    fields = [
        "baseline_left_peak_date",
        "variant_left_peak_date",
        "baseline_left_low_date",
        "variant_left_low_date",
        "baseline_neckline_date",
        "variant_neckline_date",
        "baseline_right_low_date",
        "variant_right_low_date",
        "signal_date",
        "baseline_breakout_date",
        "variant_breakout_date",
    ]
    return [normalize_date(row.get(field)) for field in fields if normalize_date(row.get(field))]


def chart_window(price: pd.DataFrame, row: pd.Series) -> pd.DataFrame:
    indexes = [index_for_date(price, date) for date in row_dates(row)]
    indexes = [idx for idx in indexes if idx is not None]
    if not indexes:
        return price.tail(100).copy()
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
    ax.axvline(idx, color=color, linestyle=linestyle, linewidth=1.0, alpha=0.82)
    y_min, y_max = ax.get_ylim()
    ax.text(
        idx + 0.12,
        y_max - (y_max - y_min) * 0.04,
        label,
        rotation=90,
        color=color,
        fontsize=6.5,
        va="top",
        ha="left",
    )


def maybe_hline(ax: Any, value: Any, color: str, linestyle: str, label: str) -> None:
    number = safe_float(value)
    if not math.isnan(number):
        ax.axhline(number, color=color, linestyle=linestyle, linewidth=1.0, alpha=0.78, label=label)


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
        figsize=(14.0, 8.4),
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 1.0]},
    )
    fig.patch.set_facecolor("white")
    draw_candles(ax_price, window)

    baseline_present = bool_value(row.get("baseline_present"))
    variant_present = bool_value(row.get("variant_present"))
    if baseline_present:
        maybe_hline(ax_price, row.get("baseline_neckline_price"), "#f57c00", "--", "baseline neckline")
        mark_date(ax_price, window, row.get("baseline_left_peak_date"), "B left peak", "#757575", "--")
        mark_date(ax_price, window, row.get("baseline_left_low_date"), "B low 1", "#1976d2", "--")
        mark_date(ax_price, window, row.get("baseline_neckline_date"), "B neckline", "#f57c00", "--")
        mark_date(ax_price, window, row.get("baseline_right_low_date"), "B low 2", "#7b1fa2", "--")
        mark_date(ax_price, window, row.get("baseline_breakout_date"), "B breakout", "#2e7d32", "--")
    if variant_present:
        maybe_hline(ax_price, row.get("variant_neckline_price"), "#ef6c00", "-", "variant neckline")
        mark_date(ax_price, window, row.get("variant_left_peak_date"), "V left peak", "#424242", "-")
        mark_date(ax_price, window, row.get("variant_left_low_date"), "V low 1", "#0d47a1", "-")
        mark_date(ax_price, window, row.get("variant_neckline_date"), "V neckline", "#ef6c00", "-")
        mark_date(ax_price, window, row.get("variant_right_low_date"), "V low 2", "#4a148c", "-")
        mark_date(ax_price, window, row.get("variant_breakout_date"), "V breakout", "#1b5e20", "-")
    mark_date(ax_price, window, row.get("signal_date"), "signal", "#d32f2f", "-")

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

    status = safe_str(row.get("comparison_status"))
    selected = selected_event_set(row)
    title = (
        f"{stock_id} signal={normalize_date(row.get('signal_date'))} "
        f"{status}/{outcome_bucket(row)} selected={selected} "
        f"ret={pct_round(selected_return(row))}%"
    )
    ax_price.set_title(title, fontsize=11)
    ax_price.set_ylabel("price")
    ax_volume.set_ylabel("volume")
    ax_price.grid(True, linestyle=":", alpha=0.28)
    ax_volume.grid(True, linestyle=":", alpha=0.2)
    ax_price.legend(loc="upper left", fontsize=7)
    ax_volume.legend(loc="upper left", fontsize=7)
    fig.tight_layout()
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=130)
    plt.close(fig)


def enrich_row(source_row: pd.Series, baseline_row: pd.Series | None, variant_row: pd.Series | None) -> pd.Series:
    row = source_row.copy()
    row["baseline_signal_close"] = "" if baseline_row is None else safe_str(baseline_row.get("signal_close"))
    row["variant_signal_close"] = "" if variant_row is None else safe_str(variant_row.get("signal_close"))
    row["baseline_neckline_price"] = "" if baseline_row is None else safe_str(baseline_row.get("neckline_price"))
    row["variant_neckline_price"] = "" if variant_row is None else safe_str(variant_row.get("neckline_price"))
    row["baseline_tdcc_any_age7"] = "" if baseline_row is None else bool_text(baseline_row.get("tdcc_any_age7"))
    row["variant_tdcc_any_age7"] = "" if variant_row is None else bool_text(variant_row.get("tdcc_any_age7"))
    if variant_row is not None:
        row["variant_left_anchor_rule_id"] = safe_str(variant_row.get("left_anchor_rule_id"))
        row["variant_left_anchor_rule_reason"] = safe_str(variant_row.get("left_anchor_rule_reason"))
    return row


def build_packet(generated_at: str) -> pd.DataFrame:
    detail, baseline_by_key, variant_by_key = read_sources()
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for _, source_row in detail.iterrows():
        key = (normalize_code(source_row.get("stock_id")), normalize_date(source_row.get("signal_date")))
        baseline_row = baseline_by_key.get(key)
        variant_row = variant_by_key.get(key)
        chart_row = enrich_row(source_row, baseline_row, variant_row)
        category = category_for(chart_row)
        folder = CATEGORY_FOLDERS[category]
        chart_path = CHART_ROOT / folder / chart_filename(chart_row)
        draw_chart(chart_row, chart_path)
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "overlay_model_id": OVERLAY_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "stock_id": key[0],
            "stock_name": safe_str(chart_row.get("stock_name")),
            "signal_date": key[1],
            "comparison_status": safe_str(chart_row.get("comparison_status")),
            "selected_event_set_id": selected_event_set(chart_row),
            "outcome_bucket": outcome_bucket(chart_row),
            "category_id": category,
            "category_folder": folder,
            "chart_path": chart_path.as_posix(),
            "chart_path_absolute": str(chart_path.resolve()),
            "baseline_present": bool_text(chart_row.get("baseline_present")),
            "variant_present": bool_text(chart_row.get("variant_present")),
            "baseline_left_peak_date": normalize_date(chart_row.get("baseline_left_peak_date")),
            "variant_left_peak_date": normalize_date(chart_row.get("variant_left_peak_date")),
            "baseline_left_low_date": normalize_date(chart_row.get("baseline_left_low_date")),
            "variant_left_low_date": normalize_date(chart_row.get("variant_left_low_date")),
            "baseline_neckline_date": normalize_date(chart_row.get("baseline_neckline_date")),
            "variant_neckline_date": normalize_date(chart_row.get("variant_neckline_date")),
            "baseline_right_low_date": normalize_date(chart_row.get("baseline_right_low_date")),
            "variant_right_low_date": normalize_date(chart_row.get("variant_right_low_date")),
            "baseline_breakout_date": normalize_date(chart_row.get("baseline_breakout_date")),
            "variant_breakout_date": normalize_date(chart_row.get("variant_breakout_date")),
            "baseline_signal_close": safe_str(chart_row.get("baseline_signal_close")),
            "variant_signal_close": safe_str(chart_row.get("variant_signal_close")),
            "baseline_neckline_price": safe_str(chart_row.get("baseline_neckline_price")),
            "variant_neckline_price": safe_str(chart_row.get("variant_neckline_price")),
            "baseline_a_mature": bool_text(chart_row.get("baseline_a_mature")),
            "variant_a_mature": bool_text(chart_row.get("variant_a_mature")),
            "baseline_a_return_pct": safe_str(chart_row.get("baseline_a_return_pct")),
            "variant_a_return_pct": safe_str(chart_row.get("variant_a_return_pct")),
            "baseline_tdcc_any_age7": safe_str(chart_row.get("baseline_tdcc_any_age7")),
            "variant_tdcc_any_age7": safe_str(chart_row.get("variant_tdcc_any_age7")),
            "variant_left_anchor_rule_id": safe_str(chart_row.get("variant_left_anchor_rule_id")),
            "variant_left_anchor_rule_reason": safe_str(chart_row.get("variant_left_anchor_rule_reason")),
            "manual_review_status": "pending_user_shape_review",
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
    folder_counts = (
        index.groupby(["comparison_status", "outcome_bucket", "category_folder"], dropna=False)
        .size()
        .reset_index(name="chart_count")
        .sort_values(["category_folder"])
    )
    comparison_counts = (
        index.groupby(["comparison_status"], dropna=False)
        .size()
        .reset_index(name="chart_count")
        .sort_values(["comparison_status"])
    )
    sample = index[
        [
            "stock_id",
            "stock_name",
            "signal_date",
            "comparison_status",
            "outcome_bucket",
            "baseline_left_peak_date",
            "variant_left_peak_date",
            "baseline_a_return_pct",
            "variant_a_return_pct",
            "chart_path",
        ]
    ]
    lines = [
        "# W-Bottom Nearest-Micro Anchor Chart Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, daily PDF logic, or baselines.",
        "",
        "## Comparison Counts",
        "",
        *markdown_table(comparison_counts, ["comparison_status", "chart_count"], limit=10),
        "",
        "## Folder Counts",
        "",
        *markdown_table(folder_counts, ["comparison_status", "outcome_bucket", "category_folder", "chart_count"], limit=20),
        "",
        "## Review Index Sample",
        "",
        *markdown_table(sample, list(sample.columns), limit=40),
        "",
        "## Reading Notes",
        "",
        "- Start with `01_variant_only_win` and `02_variant_only_loss` to judge whether the new nearest-micro anchor is admitting better W shapes or just changing the sample.",
        "- Use `04_baseline_only_win` to find possible false removals: old-detector winners that nearest-micro excludes.",
        "- Use `07_common_variant_win` and `08_common_variant_loss` to compare anchor placement when both detectors keep the same signal date.",
        "- Baseline markers are dashed and prefixed `B`; variant markers are solid and prefixed `V`.",
        "- This is a manual shape-review packet only and is not a production model change.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_packet(generated_at)
    if index.empty:
        raise SystemExit("ERROR: W-bottom nearest-micro chart review packet produced no rows")
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
