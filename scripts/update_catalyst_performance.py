from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    load_market_index_history,
    load_price_history,
    market_return_after,
    normalize_code,
    normalize_date,
    now_text,
    pct_return,
    safe_str,
    to_number,
    write_csv,
)


EVENT_CATALYST_LOG = Path("data/event_catalysts/event_catalyst_log.csv")
QUARTERLY_CATALYST = Path("data/fundamental_catalysts/quarterly_catalyst.csv")
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"

OUTPUT_DIR = Path("output/history/catalyst_performance")
CATALYST_PERFORMANCE = OUTPUT_DIR / "catalyst_performance.csv"
SUMMARY_CSV = LATEST_DIR / "catalyst_summary_latest.csv"
SUMMARY_MD = LATEST_DIR / "catalyst_summary_latest.md"

HORIZONS = [1, 3, 5, 10, 20]

OUTPUT_COLUMNS = [
    "event_date",
    "stock_id",
    "stock_name",
    "event_type",
    "theme_tags",
    "catalyst_strength",
    "catalyst_confidence",
    "close_at_event",
    "return_d1",
    "return_d3",
    "return_d5",
    "return_d10",
    "return_d20",
    "relative_return_vs_twse_d5",
    "relative_return_vs_twse_d20",
    "relative_return_vs_tpex_d5",
    "relative_return_vs_tpex_d20",
    "relative_return_vs_benchmark_d5",
    "relative_return_vs_benchmark_d20",
    "mfe_d10",
    "mae_d10",
    "tdcc_status_at_event",
    "volume_reaction",
    "price_reaction_level",
    "success_label",
    "last_updated",
]


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for enc in ["utf-8-sig", "utf-8", "cp950"]:
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc)
        except Exception:
            continue
    return pd.DataFrame()


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def first_value(row: pd.Series, names: list[str]) -> str:
    for name in names:
        if name in row.index:
            value = safe_str(row.get(name, ""))
            if value:
                return value
    return ""


def latest_candidate_map() -> dict[str, dict[str, str]]:
    df = read_csv(ALL_CANDIDATES)
    if df.empty:
        return {}
    out: dict[str, dict[str, str]] = {}
    for _, row in df.iterrows():
        code = normalize_code(first_value(row, ["stock_id", "code", "ticker"]))
        if not code:
            continue
        out[code] = {
            "tdcc_status_at_event": first_value(row, ["tdcc_accumulation_signal", "tdcc_judgement", "tdcc_status"]),
            "benchmark_index": first_value(row, ["benchmark_index"]),
            "market": first_value(row, ["market"]),
        }
    return out


def collect_event_rows() -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    events = read_csv(EVENT_CATALYST_LOG)
    for _, row in events.iterrows():
        code = normalize_code(row.get("stock_id", ""))
        event_date = normalize_date(row.get("event_date", ""))
        event_type = safe_str(row.get("event_type", ""))
        if not code or not event_date or not event_type:
            continue
        rows.append(
            {
                "event_date": event_date,
                "stock_id": code,
                "stock_name": safe_str(row.get("stock_name", "")),
                "event_type": event_type,
                "theme_tags": safe_str(row.get("theme_tags", "")),
                "catalyst_strength": safe_str(row.get("catalyst_strength", "")),
                "catalyst_confidence": safe_str(row.get("catalyst_confidence", "")),
            }
        )

    quarterly = read_csv(QUARTERLY_CATALYST)
    for _, row in quarterly.iterrows():
        code = normalize_code(row.get("stock_id", ""))
        event_date = normalize_date(row.get("announcement_date", ""))
        if not code or not event_date:
            continue
        event_types: list[str] = []
        if boolish(row.get("eps_surprise_flag")):
            event_types.append("eps_surprise")
        if boolish(row.get("margin_improvement_flag")):
            event_types.append("margin_improvement")
        if boolish(row.get("profit_turnaround")):
            event_types.append("profit_turnaround")
        if boolish(row.get("earnings_acceleration_flag")):
            event_types.append("earnings_acceleration")
        if not event_types:
            event_types.append("quarterly_financial")
        rows.append(
            {
                "event_date": event_date,
                "stock_id": code,
                "stock_name": safe_str(row.get("stock_name", "")),
                "event_type": ";".join(dict.fromkeys(event_types)),
                "theme_tags": "",
                "catalyst_strength": "5" if any(x in event_types for x in ["eps_surprise", "margin_improvement", "profit_turnaround"]) else "3",
                "catalyst_confidence": "high",
            }
        )

    if not rows:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    out = pd.DataFrame(rows)
    out = out.drop_duplicates(["event_date", "stock_id", "event_type"], keep="last")
    return out.sort_values(["event_date", "stock_id", "event_type"]).reset_index(drop=True)


def base_position(price: pd.DataFrame, event_date: str) -> int | None:
    if price.empty:
        return None
    part = price[price["date"] <= normalize_date(event_date)]
    if part.empty:
        return None
    return int(part.index[-1])


def infer_benchmark(price: pd.DataFrame, candidate: dict[str, str]) -> str:
    explicit = safe_str(candidate.get("benchmark_index", "")).upper()
    if explicit in {"TWSE", "TPEX"}:
        return explicit
    market = safe_str(candidate.get("market", "")).upper()
    if "TPEX" in market or "OTC" in market:
        return "TPEX"
    if "TWSE" in market:
        return "TWSE"
    if not price.empty and "market" in price.columns:
        latest_market = safe_str(price["market"].dropna().astype(str).iloc[-1] if len(price) else "").upper()
        if "TPEX" in latest_market or "OTC" in latest_market:
            return "TPEX"
        if "TWSE" in latest_market:
            return "TWSE"
    return "unknown"


def price_level(ret5: float, ret20: float, volume_reaction: str) -> str:
    if (not math.isnan(ret5) and ret5 > 20) or (not math.isnan(ret20) and ret20 > 30):
        return "overheated"
    if (not math.isnan(ret5) and ret5 > 12) or (not math.isnan(ret20) and ret20 > 20):
        return "priced_in"
    if (not math.isnan(ret5) and ret5 > 3) or (not math.isnan(ret20) and ret20 > 5):
        return "mild"
    return "none"


def success_label(row: dict[str, Any]) -> str:
    available = int(to_number(row.get("_available_days"), 0))
    if available < 5:
        return "pending"
    ret10 = to_number(row.get("return_d10"))
    rel10 = to_number(row.get("relative_return_vs_benchmark_d20"))
    if math.isnan(rel10):
        rel10 = to_number(row.get("relative_return_vs_benchmark_d5"))
    mfe10 = to_number(row.get("mfe_d10"))
    mae10 = to_number(row.get("mae_d10"))
    if not math.isnan(ret10) and not math.isnan(rel10) and ret10 > 0 and rel10 > 0:
        return "effective"
    if not math.isnan(mfe10) and mfe10 >= 5 and (math.isnan(ret10) or ret10 <= 0):
        return "tradable_then_faded"
    if not math.isnan(ret10) and ret10 < 0 and not math.isnan(mae10) and mae10 <= -5:
        return "failed"
    return "mixed_or_pending"


def compute_event(row: pd.Series, index_df: pd.DataFrame, candidate_map: dict[str, dict[str, str]]) -> dict[str, Any]:
    code = normalize_code(row.get("stock_id", ""))
    event_date = normalize_date(row.get("event_date", ""))
    price = load_price_history(code)
    pos = base_position(price, event_date)
    candidate = candidate_map.get(code, {})
    out = {col: "" for col in OUTPUT_COLUMNS}
    out.update(
        {
            "event_date": event_date,
            "stock_id": code,
            "stock_name": safe_str(row.get("stock_name", "")),
            "event_type": safe_str(row.get("event_type", "")),
            "theme_tags": safe_str(row.get("theme_tags", "")),
            "catalyst_strength": safe_str(row.get("catalyst_strength", "")),
            "catalyst_confidence": safe_str(row.get("catalyst_confidence", "")),
            "tdcc_status_at_event": safe_str(candidate.get("tdcc_status_at_event", "")),
            "last_updated": now_text(),
            "_available_days": 0,
        }
    )
    if pos is None:
        out["success_label"] = "missing_price_history"
        return out

    signal_close = to_number(price.loc[pos, "close"])
    out["close_at_event"] = signal_close
    out["_available_days"] = max(0, len(price) - pos - 1)
    benchmark = infer_benchmark(price, candidate)
    max_volume_ratio = math.nan

    for horizon in HORIZONS:
        target = pos + horizon
        if target < len(price):
            close_h = to_number(price.loc[target, "close"])
            out[f"return_d{horizon}"] = pct_return(close_h, signal_close)
        window = price.iloc[pos + 1 : min(len(price), pos + horizon + 1)]
        if horizon == 10 and not window.empty:
            out["mfe_d10"] = pct_return(window["high"].max(), signal_close) if "high" in window.columns else ""
            out["mae_d10"] = pct_return(window["low"].min(), signal_close) if "low" in window.columns else ""
        if not window.empty and "volume_ratio" in window.columns:
            ratio = pd.to_numeric(window["volume_ratio"], errors="coerce").max()
            if not math.isnan(ratio):
                max_volume_ratio = max(max_volume_ratio if not math.isnan(max_volume_ratio) else ratio, ratio)

    for index_code, prefix in [("TWSE", "twse"), ("TPEX", "tpex")]:
        for horizon in [5, 20]:
            _, idx_ret = market_return_after(index_df, index_code, event_date, horizon)
            stock_ret = to_number(out.get(f"return_d{horizon}"))
            out[f"relative_return_vs_{prefix}_d{horizon}"] = "" if math.isnan(stock_ret) or math.isnan(idx_ret) else stock_ret - idx_ret
    for horizon in [5, 20]:
        if benchmark == "TWSE":
            out[f"relative_return_vs_benchmark_d{horizon}"] = out.get(f"relative_return_vs_twse_d{horizon}", "")
        elif benchmark == "TPEX":
            out[f"relative_return_vs_benchmark_d{horizon}"] = out.get(f"relative_return_vs_tpex_d{horizon}", "")
        else:
            out[f"relative_return_vs_benchmark_d{horizon}"] = ""

    if math.isnan(max_volume_ratio):
        out["volume_reaction"] = "missing"
    elif max_volume_ratio >= 3:
        out["volume_reaction"] = "explosive"
    elif max_volume_ratio >= 1.2:
        out["volume_reaction"] = "healthy"
    else:
        out["volume_reaction"] = "quiet"

    out["price_reaction_level"] = price_level(to_number(out.get("return_d5")), to_number(out.get("return_d20")), out["volume_reaction"])
    out["success_label"] = success_label(out)
    out.pop("_available_days", None)
    return out


def build_performance() -> pd.DataFrame:
    events = collect_event_rows()
    if events.empty:
        empty = pd.DataFrame(columns=OUTPUT_COLUMNS)
        write_csv(empty, CATALYST_PERFORMANCE)
        return empty
    index_df = load_market_index_history(update_if_missing=True)
    candidate_map = latest_candidate_map()
    rows = [compute_event(row, index_df, candidate_map) for _, row in events.iterrows()]
    out = pd.DataFrame(rows)
    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out = out[OUTPUT_COLUMNS]
    out = out.drop_duplicates(["event_date", "stock_id", "event_type"], keep="last")
    out = out.sort_values(["event_date", "stock_id", "event_type"]).reset_index(drop=True)
    write_csv(out, CATALYST_PERFORMANCE)
    return out


def metric_mean(part: pd.DataFrame, col: str) -> str:
    if part.empty or col not in part.columns:
        return ""
    nums = pd.to_numeric(part[col], errors="coerce").dropna()
    if nums.empty:
        return ""
    return f"{nums.mean():.2f}"


def build_summary(perf: pd.DataFrame) -> pd.DataFrame:
    if perf.empty:
        return pd.DataFrame(
            columns=[
                "dimension",
                "bucket",
                "sample_size",
                "avg_return_d5",
                "avg_return_d10",
                "avg_return_d20",
                "avg_relative_return_vs_benchmark_d5",
                "avg_relative_return_vs_benchmark_d20",
                "effective_count",
                "pending_count",
                "last_updated",
            ]
        )
    rows: list[dict[str, str]] = []
    for dimension in ["event_type", "catalyst_confidence", "price_reaction_level", "success_label"]:
        if dimension not in perf.columns:
            continue
        for bucket, part in perf.groupby(dimension, dropna=False):
            bucket_text = safe_str(bucket) or "blank"
            rows.append(
                {
                    "dimension": dimension,
                    "bucket": bucket_text,
                    "sample_size": str(len(part)),
                    "avg_return_d5": metric_mean(part, "return_d5"),
                    "avg_return_d10": metric_mean(part, "return_d10"),
                    "avg_return_d20": metric_mean(part, "return_d20"),
                    "avg_relative_return_vs_benchmark_d5": metric_mean(part, "relative_return_vs_benchmark_d5"),
                    "avg_relative_return_vs_benchmark_d20": metric_mean(part, "relative_return_vs_benchmark_d20"),
                    "effective_count": str(int(part.get("success_label", pd.Series(dtype=str)).astype(str).eq("effective").sum())),
                    "pending_count": str(int(part.get("success_label", pd.Series(dtype=str)).astype(str).eq("pending").sum())),
                    "last_updated": now_text(),
                }
            )
    return pd.DataFrame(rows)


def write_summary_md(summary: pd.DataFrame, perf: pd.DataFrame) -> None:
    lines = [
        "# Catalyst Performance Summary",
        "",
        f"- generated_at: `{now_text()}`",
        f"- catalyst_event_rows: `{len(perf)}`",
        "- note: Empty event rows mean no confirmed catalyst records have been loaded yet. The model does not fabricate news or announcements.",
        "",
    ]
    if summary.empty:
        lines.append("No catalyst performance rows are available yet.")
    else:
        lines.extend(["| dimension | bucket | sample_size | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d20 | effective_count | pending_count |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"])
        for _, row in summary.iterrows():
            lines.append(
                "| "
                + " | ".join(
                    safe_str(row.get(col, ""))
                    for col in [
                        "dimension",
                        "bucket",
                        "sample_size",
                        "avg_return_d5",
                        "avg_return_d10",
                        "avg_return_d20",
                        "avg_relative_return_vs_benchmark_d20",
                        "effective_count",
                        "pending_count",
                    ]
                )
                + " |"
            )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    perf = build_performance()
    summary = build_summary(perf)
    write_csv(summary, SUMMARY_CSV)
    write_summary_md(summary, perf)
    print(f"Saved: {CATALYST_PERFORMANCE}, rows={len(perf)}")
    print(f"Saved: {SUMMARY_CSV}, rows={len(summary)}")
    print(f"Saved: {SUMMARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
