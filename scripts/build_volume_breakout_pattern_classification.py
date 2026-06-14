from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

DETAIL_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
OUT_SUMMARY_CSV = LATEST_DIR / "volume_breakout_pattern_classification_latest.csv"
OUT_SUMMARY_MD = LATEST_DIR / "volume_breakout_pattern_classification_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification_events.csv"

MODEL_ID = "volume_range_breakout"

SUMMARY_COLUMNS = [
    "model_id",
    "classification_id",
    "classification_name_zh",
    "pattern_id",
    "event_count",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
]

EVENT_COLUMNS = [
    "model_id",
    "event_date",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "classification_id",
    "classification_name_zh",
    "pattern_tags",
    "volume_ratio",
    "signal_return_1d_pct",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "limit_up_like",
    "out_of_sample",
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
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def safe_float(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if text in {"", "-"}:
        return default
    try:
        return float(text)
    except Exception:
        return default


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"1", "1.0", "true", "yes", "y", "t"}


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")


def pct_round(value: Any) -> float | str:
    num = safe_float(value)
    return round(num, 4) if not math.isnan(num) else ""


def classify_event(row: pd.Series) -> dict[str, str]:
    volume_ratio = safe_float(row.get("volume_ratio"))
    width40 = safe_float(row.get("range_width_40_pct"))
    low_pos60 = safe_float(row.get("low_position_60_pct"))
    limit_up_like = bool_value(row.get("limit_up_like"))

    tags: list[str] = []
    if limit_up_like:
        tags.append("limit_up_like")
    if not math.isnan(volume_ratio):
        if volume_ratio < 2:
            tags.append("volume_ratio_lt_2")
        elif volume_ratio >= 3:
            tags.append("volume_ratio_ge_3")
        else:
            tags.append("volume_ratio_2_3")
    if not math.isnan(width40):
        tags.append("long_base" if width40 <= 25 else "wide_base")
    if not math.isnan(low_pos60):
        if low_pos60 <= 60:
            tags.append("low_position_60")
        elif low_pos60 >= 80:
            tags.append("high_position_60")
        else:
            tags.append("middle_position_60")

    if limit_up_like and not math.isnan(volume_ratio) and volume_ratio < 2:
        classification_id = "locked_limit_up_breakout"
        name = "鎖量漲停突破"
    elif limit_up_like:
        classification_id = "limit_up_like_breakout"
        name = "類漲停放量突破"
    elif not math.isnan(width40) and not math.isnan(low_pos60) and width40 <= 25 and low_pos60 <= 60:
        classification_id = "long_base_low_position"
        name = "長盤整低位階突破"
    elif not math.isnan(low_pos60) and low_pos60 <= 60:
        classification_id = "low_position_breakout"
        name = "低位階突破"
    elif not math.isnan(low_pos60) and low_pos60 >= 80:
        classification_id = "high_position_breakout"
        name = "高位階突破"
    elif not math.isnan(width40) and width40 > 25:
        classification_id = "wide_range_breakout"
        name = "寬區間突破"
    else:
        classification_id = "standard_breakout"
        name = "一般突破"

    return {
        "classification_id": classification_id,
        "classification_name_zh": name,
        "pattern_tags": "|".join(dict.fromkeys(tags)),
    }


def unique_current_events(detail: pd.DataFrame) -> pd.DataFrame:
    current = detail[
        detail["model_id"].astype(str).eq(MODEL_ID)
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
        & detail["model_hit_status"].astype(str).eq("current_model_hit")
    ].copy()
    if current.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS)

    event_cols = [
        "model_id",
        "event_date",
        "stock_id",
        "stock_name",
        "market",
        "market_regime",
        "volume_ratio",
        "signal_return_1d_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "low_position_60_pct",
        "limit_up_like",
        "out_of_sample",
    ]
    events = current[event_cols].drop_duplicates(["event_date", "stock_id"], keep="first").copy()
    classes = events.apply(classify_event, axis=1, result_type="expand")
    events = pd.concat([events, classes], axis=1)
    return events[EVENT_COLUMNS].sort_values(["event_date", "stock_id"]).reset_index(drop=True)


def profit_factor(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    if nums.empty:
        return ""
    gains = nums[nums > 0].sum()
    losses = nums[nums < 0].sum()
    if losses == 0:
        return round(float("inf"), 4) if gains > 0 else ""
    return round(float(gains / abs(losses)), 4)


def win_rate(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    if nums.empty:
        return ""
    return round(float((nums > 0).mean() * 100.0), 2)


def confidence_status(sample: int) -> str:
    if sample >= 500:
        return "high"
    if sample >= 100:
        return "medium"
    return "low"


def summarize(detail: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    if detail.empty or events.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)

    current = detail[
        detail["model_id"].astype(str).eq(MODEL_ID)
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
        & detail["model_hit_status"].astype(str).eq("current_model_hit")
    ].copy()
    joined = current.merge(
        events[["event_date", "stock_id", "classification_id", "classification_name_zh"]],
        on=["event_date", "stock_id"],
        how="inner",
    )
    generated_at = now_text()
    data_start = safe_str(events["event_date"].min())
    data_end = safe_str(events["event_date"].max())
    rows: list[dict[str, Any]] = []
    for (classification_id, pattern_id), part in joined.groupby(["classification_id", "pattern_id"], dropna=False):
        returns = pd.to_numeric(part["return_pct"], errors="coerce").dropna()
        mae = pd.to_numeric(part.get("mae_pct", pd.Series(dtype=float)), errors="coerce")
        mfe = pd.to_numeric(part.get("mfe_pct", pd.Series(dtype=float)), errors="coerce")
        holding = pd.to_numeric(part.get("holding_days", pd.Series(dtype=float)), errors="coerce")
        oos = part[part["out_of_sample"].map(bool_value)].copy()
        oos_returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
        sample = int(len(returns))
        oos_avg = round(float(oos_returns.mean()), 4) if not oos_returns.empty else ""
        oos_win = win_rate(oos_returns)
        oos_pass = bool(len(oos_returns) >= 30 and safe_float(oos_avg) > 0 and safe_float(oos_win) >= 50)
        class_name = safe_str(part["classification_name_zh"].iloc[0])
        risk_note = "research classification only; approved_for_daily remains False"
        if classification_id == "locked_limit_up_breakout":
            risk_note = "鎖量漲停突破已納入現行模型，但仍需獨立觀察隔日可成交性與開板風險。"
        rows.append(
            {
                "model_id": MODEL_ID,
                "classification_id": safe_str(classification_id),
                "classification_name_zh": class_name,
                "pattern_id": safe_str(pattern_id),
                "event_count": sample,
                "unique_stocks": int(part["stock_id"].nunique()),
                "win_rate": win_rate(returns),
                "avg_return": round(float(returns.mean()), 4) if not returns.empty else "",
                "median_return": round(float(returns.median()), 4) if not returns.empty else "",
                "max_drawdown": round(float(mae.min()), 4) if not mae.dropna().empty else "",
                "avg_mfe": round(float(mfe.mean()), 4) if not mfe.dropna().empty else "",
                "avg_mae": round(float(mae.mean()), 4) if not mae.dropna().empty else "",
                "avg_holding_days": round(float(holding.mean()), 2) if not holding.dropna().empty else "",
                "profit_factor": profit_factor(returns),
                "out_of_sample_size": int(len(oos_returns)),
                "out_of_sample_win_rate": oos_win,
                "out_of_sample_avg_return": oos_avg,
                "confidence_status": confidence_status(sample),
                "out_of_sample_pass": oos_pass,
                "approved_for_daily": False,
                "risk_notes_zh": risk_note,
                "generated_at": generated_at,
                "data_start_date": data_start,
                "data_end_date": data_end,
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    out["_confidence_order"] = out["confidence_status"].map({"high": 0, "medium": 1, "low": 2}).fillna(9)
    out["_avg"] = pd.to_numeric(out["avg_return"], errors="coerce").fillna(-999)
    out = out.sort_values(["classification_id", "_confidence_order", "_avg", "event_count"], ascending=[True, True, False, False])
    return out.drop(columns=["_confidence_order", "_avg"])[SUMMARY_COLUMNS].reset_index(drop=True)


def markdown_table(df: pd.DataFrame, cols: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        vals = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:120] for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, events: pd.DataFrame) -> None:
    counts = (
        events.groupby(["classification_id", "classification_name_zh"], dropna=False)
        .size()
        .reset_index(name="event_count")
        .sort_values("event_count", ascending=False)
    )
    best = summary.copy()
    if not best.empty:
        best["_avg"] = pd.to_numeric(best["avg_return"], errors="coerce").fillna(-999)
        best = best.sort_values(["classification_id", "_avg", "event_count"], ascending=[True, False, False])
        best = best.groupby("classification_id", as_index=False).head(3).drop(columns=["_avg"])
    lines = [
        "# Volume Breakout Pattern Classification",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- unique_event_rows: `{len(events)}`",
        f"- summary_rows: `{len(summary)}`",
        "- scope: current model hits only; research classification, not production promotion.",
        "- approved_for_daily: always `False` in this artifact.",
        "",
        "## Classification Counts",
        "",
        *markdown_table(counts, ["classification_id", "classification_name_zh", "event_count"], 30),
        "",
        "## Best Operation Patterns By Classification",
        "",
        *markdown_table(
            best,
            [
                "classification_id",
                "pattern_id",
                "event_count",
                "win_rate",
                "avg_return",
                "median_return",
                "out_of_sample_size",
                "out_of_sample_avg_return",
                "confidence_status",
                "out_of_sample_pass",
            ],
            80,
        ),
        "",
    ]
    OUT_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    if not DETAIL_CSV.exists():
        raise FileNotFoundError(f"missing historical operation detail: {DETAIL_CSV}")
    detail = pd.read_csv(DETAIL_CSV, dtype=str, keep_default_na=False)
    events = unique_current_events(detail)
    summary = summarize(detail, events)
    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(summary, OUT_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, events)
    print(f"Saved: {OUT_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
