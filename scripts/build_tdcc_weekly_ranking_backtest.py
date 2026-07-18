from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_tdcc_weekly_candidate_reports import (  # noqa: E402
    DELTA_WEIGHTS,
    TDCC_EFFECTIVE_INCREASE_THRESHOLD,
    TDCC_HIGH_PAIR_STREAK_BONUS_CAP,
    TDCC_HIGH_PAIR_STREAK_BONUS_STEP,
    TDCC_LOW_VOLUME_MA20_LOTS_THRESHOLD,
    TDCC_LOW_VOLUME_PENALTY,
    high_pair_streak_bonus,
    normalize_volume_ma20_lots,
    sync_bonus,
)
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    load_price_history,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    pct_return,
    position_on_or_before,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)
from research_tdcc_dataset_consumer import (  # noqa: E402
    ResearchTdccDatasetContract,
    load_research_tdcc_dataset_contract,
)


MODEL_ID = "tdcc_weekly_ranking_formula"
RANKING_MODEL_VERSION = "tdcc_weekly_ranking_formula_20260614"
HORIZONS = [5, 10, 20]
RANK_BUCKETS = [10, 20, 50]

THEME_TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"

EVENTS_CSV = HISTORY_DIR / "research" / "tdcc_weekly_ranking_backtest_events.csv"
SUMMARY_CSV = HISTORY_DIR / "research" / "tdcc_weekly_ranking_backtest.csv"
LATEST_SUMMARY_CSV = LATEST_DIR / "tdcc_weekly_ranking_backtest_latest.csv"
LATEST_SUMMARY_MD = LATEST_DIR / "tdcc_weekly_ranking_backtest_latest.md"
DOCS_SUMMARY_CSV = DOCS_LATEST_DIR / LATEST_SUMMARY_CSV.name
DOCS_SUMMARY_MD = DOCS_LATEST_DIR / LATEST_SUMMARY_MD.name

THRESHOLD_MAP = {
    "tdcc_1w_change_400": "over_400_pct",
    "tdcc_1w_change_600": "over_600_pct",
    "tdcc_1w_change_800": "over_800_pct",
    "tdcc_1w_change_1000": "over_1000_pct",
}
PRICE_CACHE: dict[str, pd.DataFrame] = {}


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def snapshot_paths(contract: ResearchTdccDatasetContract | None = None) -> list[Path]:
    contract = contract or load_research_tdcc_dataset_contract()
    return [snapshot.path for snapshot in contract.snapshots]


def load_snapshot(path: Path) -> pd.DataFrame:
    df = read_csv(path, dtype=str)
    if df.empty:
        return pd.DataFrame()
    if "code" in df.columns and "stock_id" not in df.columns:
        df["stock_id"] = df["code"]
    if "name" in df.columns and "stock_name" not in df.columns:
        df["stock_name"] = df["name"]
    for col in ["date", "stock_id", "stock_name", *THRESHOLD_MAP.values()]:
        if col not in df.columns:
            df[col] = ""
    df["signal_date"] = df["date"].map(normalize_date)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    for col in THRESHOLD_MAP.values():
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["signal_date", "stock_id"]).drop_duplicates("stock_id", keep="last")


def load_theme_context() -> dict[str, dict[str, str]]:
    df = read_csv(THEME_TAXONOMY, dtype=str).fillna("")
    if df.empty or "stock_id" not in df.columns:
        return {}
    out: dict[str, dict[str, str]] = {}
    for _, row in df.iterrows():
        stock_id = normalize_code(row.get("stock_id"))
        if not stock_id:
            continue
        theme = (
            safe_str(row.get("hot_primary_theme"))
            or safe_str(row.get("primary_theme"))
            or safe_str(row.get("basic_theme"))
            or safe_str(row.get("industry"))
        )
        effective = safe_str(row.get("effective_mainstream_label"))
        eligible = boolish(row.get("mainstream_report_eligible"))
        mainstream = effective == "mainstream" or eligible
        out[stock_id] = {
            "theme": theme,
            "theme_mainstream_status": "mainstream_latest_taxonomy" if mainstream else "non_mainstream_latest_taxonomy",
        }
    return out


def volume_ma20_lots(stock_id: str, signal_date: str) -> float:
    price = cached_price_history(stock_id)
    pos = position_on_or_before(price, signal_date)
    if pos is None or "volume_ma20" not in price.columns:
        return math.nan
    return normalize_volume_ma20_lots(price.loc[pos].get("volume_ma20"))


def cached_price_history(stock_id: Any) -> pd.DataFrame:
    code = normalize_code(stock_id)
    if not code:
        return pd.DataFrame()
    if code not in PRICE_CACHE:
        PRICE_CACHE[code] = load_price_history(code)
    return PRICE_CACHE[code]


def stock_return_after_cached(stock_id: Any, signal_date: str, horizon: int) -> tuple[float, float, float, float, int]:
    price = cached_price_history(stock_id)
    pos = position_on_or_before(price, signal_date)
    if pos is None:
        return math.nan, math.nan, math.nan, math.nan, 0
    signal_close = to_number(price.loc[pos, "close"])
    available = max(0, len(price) - pos - 1)
    if math.isnan(signal_close) or signal_close <= 0:
        return signal_close, math.nan, math.nan, math.nan, available
    close_h = math.nan
    ret = math.nan
    if pos + horizon < len(price):
        close_h = to_number(price.loc[pos + horizon, "close"])
        ret = pct_return(close_h, signal_close)
    window = price.iloc[pos + 1 : min(len(price), pos + horizon + 1)]
    mfe = pct_return(window["high"].max(), signal_close) if not window.empty and "high" in window.columns else math.nan
    mae = pct_return(window["low"].min(), signal_close) if not window.empty and "low" in window.columns else math.nan
    return close_h, ret, mfe, mae, available


def weekly_delta_rows(contract: ResearchTdccDatasetContract | None = None) -> pd.DataFrame:
    contract = contract or load_research_tdcc_dataset_contract()
    paths = snapshot_paths(contract)
    if len(paths) < 2:
        return pd.DataFrame()

    theme_context = load_theme_context()
    rows: list[dict[str, Any]] = []
    high_pair_streak_by_stock: dict[str, int] = {}
    previous = load_snapshot(paths[0])
    previous_date = contract.history_dates[0]

    for current_date, path in zip(contract.history_dates[1:], paths[1:]):
        current = load_snapshot(path)
        if current.empty or previous.empty:
            previous = current
            previous_date = current_date
            continue

        prev_keep = ["stock_id", *THRESHOLD_MAP.values()]
        merged = current.merge(
            previous[prev_keep],
            on="stock_id",
            how="left",
            suffixes=("", "_prev"),
        )
        current_streaks: dict[str, int] = {}
        for _, row in merged.iterrows():
            stock_id = safe_str(row.get("stock_id"))
            if not stock_id:
                continue
            item: dict[str, Any] = {
                "model_id": MODEL_ID,
                "ranking_model_version": RANKING_MODEL_VERSION,
                "signal_date": safe_str(row.get("signal_date")),
                "source_tdcc_dataset_id": contract.dataset_id,
                "source_tdcc_prior_date": previous_date,
                "stock_id": stock_id,
                "stock_name": safe_str(row.get("stock_name")),
            }
            for delta_col, ratio_col in THRESHOLD_MAP.items():
                cur = to_number(row.get(ratio_col))
                prev = to_number(row.get(f"{ratio_col}_prev"))
                item[delta_col] = cur - prev if not math.isnan(cur) and not math.isnan(prev) else math.nan

            item["tdcc_interval_status"] = (
                "complete_official_period"
                if all(not math.isnan(to_number(item.get(delta_col))) for delta_col in THRESHOLD_MAP)
                else "excluded_missing_snapshot_row"
            )

            change_800 = to_number(item.get("tdcc_1w_change_800"))
            change_1000 = to_number(item.get("tdcc_1w_change_1000"))
            high_pair_up = (
                not math.isnan(change_800)
                and not math.isnan(change_1000)
                and change_800 > TDCC_EFFECTIVE_INCREASE_THRESHOLD
                and change_1000 > TDCC_EFFECTIVE_INCREASE_THRESHOLD
            )
            streak = high_pair_streak_by_stock.get(stock_id, 0) + 1 if high_pair_up else 0
            current_streaks[stock_id] = streak
            item["tdcc_high_pair_effective_streak_weeks"] = streak

            theme = theme_context.get(stock_id, {})
            item["theme"] = theme.get("theme", "")
            item["theme_mainstream_status"] = theme.get("theme_mainstream_status", "unknown_latest_taxonomy")
            rows.append(item)

        high_pair_streak_by_stock = current_streaks
        previous = current
        previous_date = current_date

    return pd.DataFrame(rows)


def compute_score_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in THRESHOLD_MAP:
        out[col] = pd.to_numeric(out.get(col, pd.Series(index=out.index)), errors="coerce")

    out["tdcc_four_threshold_weekly_increase_sum"] = sum(out[col].fillna(0).clip(lower=0) for col in THRESHOLD_MAP)
    out["tdcc_effective_increase_count"] = sum(
        (out[col].fillna(0) > TDCC_EFFECTIVE_INCREASE_THRESHOLD).astype(int) for col in THRESHOLD_MAP
    )
    out["tdcc_weighted_weekly_increase_score"] = sum(
        out[col].fillna(0) * DELTA_WEIGHTS[col] for col in THRESHOLD_MAP
    ).round(2)
    out["tdcc_sync_bonus"] = out["tdcc_effective_increase_count"].map(sync_bonus)
    out["tdcc_theme_bonus"] = out.get("theme_mainstream_status", "").map(
        lambda value: 5.0 if safe_str(value).startswith("mainstream") else 0.0
    )
    if "volume_ma20_lots" not in out.columns:
        out["volume_ma20_lots"] = math.nan
    out["volume_ma20_lots"] = pd.to_numeric(out["volume_ma20_lots"], errors="coerce")
    out["tdcc_low_volume_penalty"] = out["volume_ma20_lots"].map(
        lambda value: TDCC_LOW_VOLUME_PENALTY
        if not math.isnan(to_number(value)) and to_number(value) < TDCC_LOW_VOLUME_MA20_LOTS_THRESHOLD
        else 0.0
    )
    out["tdcc_high_pair_effective_streak_weeks"] = pd.to_numeric(
        out.get("tdcc_high_pair_effective_streak_weeks", pd.Series(index=out.index)),
        errors="coerce",
    ).fillna(0)
    out["tdcc_high_pair_streak_bonus"] = out["tdcc_high_pair_effective_streak_weeks"].map(high_pair_streak_bonus)
    out["tdcc_weekly_increase_score"] = (
        out["tdcc_weighted_weekly_increase_score"]
        + out["tdcc_sync_bonus"]
        + out["tdcc_theme_bonus"]
        - out["tdcc_low_volume_penalty"]
    ).round(2)
    out["tdcc_consecutive_accumulation_score"] = (
        out["tdcc_weighted_weekly_increase_score"]
        + out["tdcc_sync_bonus"]
        + out["tdcc_high_pair_streak_bonus"]
        + out["tdcc_theme_bonus"]
        - out["tdcc_low_volume_penalty"]
    ).round(2)
    return out


def add_volume_context(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    values: list[float] = []
    for _, row in out.iterrows():
        values.append(volume_ma20_lots(safe_str(row.get("stock_id")), safe_str(row.get("signal_date"))))
    out["volume_ma20_lots"] = values
    return out


def rank_weekly_models(scored: pd.DataFrame) -> pd.DataFrame:
    events: list[pd.DataFrame] = []
    for signal_date, group in scored.groupby("signal_date", dropna=False):
        weekly = group[group["tdcc_effective_increase_count"] >= 1].copy()
        if not weekly.empty:
            weekly = weekly.sort_values(
                [
                    "tdcc_weekly_increase_score",
                    "tdcc_weighted_weekly_increase_score",
                    "tdcc_1w_change_1000",
                    "tdcc_1w_change_800",
                ],
                ascending=[False, False, False, False],
            ).head(max(RANK_BUCKETS))
            weekly["tdcc_list_type"] = "weekly_increase"
            weekly["tdcc_rank"] = range(1, len(weekly) + 1)
            weekly["tdcc_ranking_score"] = weekly["tdcc_weekly_increase_score"]
            events.append(weekly)

        consecutive = group[group["tdcc_high_pair_effective_streak_weeks"] >= 2].copy()
        if not consecutive.empty:
            consecutive = consecutive.sort_values(
                [
                    "tdcc_consecutive_accumulation_score",
                    "tdcc_high_pair_effective_streak_weeks",
                    "tdcc_weighted_weekly_increase_score",
                ],
                ascending=[False, False, False],
            ).head(max(RANK_BUCKETS))
            consecutive["tdcc_list_type"] = "consecutive_accumulation"
            consecutive["tdcc_rank"] = range(1, len(consecutive) + 1)
            consecutive["tdcc_ranking_score"] = consecutive["tdcc_consecutive_accumulation_score"]
            events.append(consecutive)

    if not events:
        return pd.DataFrame()
    return pd.concat(events, ignore_index=True, sort=False)


def add_return_columns(events: pd.DataFrame) -> pd.DataFrame:
    out = events.copy()
    for horizon in HORIZONS:
        close_values: list[float] = []
        returns: list[float] = []
        mfe_values: list[float] = []
        mae_values: list[float] = []
        available_values: list[int] = []
        for _, row in out.iterrows():
            close_h, ret, mfe, mae, available = stock_return_after_cached(
                row.get("stock_id"),
                safe_str(row.get("signal_date")),
                horizon,
            )
            close_values.append(close_h)
            returns.append(ret)
            mfe_values.append(mfe)
            mae_values.append(mae)
            available_values.append(available)
        out[f"d{horizon}_close"] = close_values
        out[f"d{horizon}_return_pct"] = returns
        out[f"d{horizon}_mfe_pct"] = mfe_values
        out[f"d{horizon}_mae_pct"] = mae_values
        out[f"d{horizon}_mature"] = [available >= horizon for available in available_values]
    out["approved_for_daily"] = False
    out["theme_context_note"] = "theme bonus uses latest taxonomy context; research only"
    out["generated_at"] = now_text()
    return out


def profit_factor(returns: pd.Series) -> float:
    values = pd.to_numeric(returns, errors="coerce").dropna()
    gains = values[values > 0].sum()
    losses = values[values < 0].sum()
    if losses == 0:
        return math.nan if gains == 0 else 999.0
    return round(gains / abs(losses), 4)


def confidence_status(count: int) -> str:
    if count >= 120:
        return "high"
    if count >= 50:
        return "medium"
    return "low"


def summarize(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if events.empty:
        return pd.DataFrame()
    dates = sorted(events["signal_date"].dropna().astype(str).unique())
    cutoff = dates[int(len(dates) * 0.7)] if len(dates) >= 4 else (dates[-1] if dates else "")

    for list_type in sorted(events["tdcc_list_type"].dropna().unique()):
        base = events[events["tdcc_list_type"].eq(list_type)].copy()
        for bucket in RANK_BUCKETS:
            bucket_part = base[pd.to_numeric(base["tdcc_rank"], errors="coerce") <= bucket].copy()
            for horizon in HORIZONS:
                ret_col = f"d{horizon}_return_pct"
                mfe_col = f"d{horizon}_mfe_pct"
                mae_col = f"d{horizon}_mae_pct"
                mature_col = f"d{horizon}_mature"
                part = bucket_part[bucket_part[mature_col].astype(bool)].copy()
                returns = pd.to_numeric(part[ret_col], errors="coerce").dropna()
                if returns.empty:
                    continue
                oos = part[part["signal_date"].astype(str) >= cutoff].copy() if cutoff else part.iloc[0:0].copy()
                oos_returns = pd.to_numeric(oos[ret_col], errors="coerce").dropna()
                oos_win = round((oos_returns > 0).mean() * 100, 2) if len(oos_returns) else math.nan
                oos_avg = round(oos_returns.mean(), 4) if len(oos_returns) else math.nan
                rows.append(
                    {
                        "model_id": MODEL_ID,
                        "ranking_model_version": RANKING_MODEL_VERSION,
                        "tdcc_list_type": list_type,
                        "rank_bucket": f"top_{bucket}",
                        "horizon": f"D+{horizon}",
                        "event_count": int(len(returns)),
                        "unique_stocks": int(part["stock_id"].nunique()),
                        "signal_weeks": int(part["signal_date"].nunique()),
                        "win_rate": round((returns > 0).mean() * 100, 2),
                        "avg_return": round(returns.mean(), 4),
                        "median_return": round(returns.median(), 4),
                        "avg_mfe": round(pd.to_numeric(part[mfe_col], errors="coerce").mean(), 4),
                        "avg_mae": round(pd.to_numeric(part[mae_col], errors="coerce").mean(), 4),
                        "max_drawdown": round(pd.to_numeric(part[mae_col], errors="coerce").min(), 4),
                        "profit_factor": profit_factor(returns),
                        "avg_rank": round(pd.to_numeric(part["tdcc_rank"], errors="coerce").mean(), 2),
                        "avg_tdcc_score": round(pd.to_numeric(part["tdcc_ranking_score"], errors="coerce").mean(), 4),
                        "out_of_sample_start_date": cutoff,
                        "out_of_sample_size": int(len(oos_returns)),
                        "out_of_sample_win_rate": oos_win,
                        "out_of_sample_avg_return": oos_avg,
                        "out_of_sample_pass": bool(len(oos_returns) >= 20 and oos_avg > 0 and oos_win >= 50),
                        "confidence_status": confidence_status(int(len(returns))),
                        "approved_for_daily": False,
                        "risk_notes_zh": "research only; ranking is not promoted to production buy order",
                        "theme_context_note": "theme bonus uses latest taxonomy context",
                        "generated_at": now_text(),
                        "data_start_date": min(dates) if dates else "",
                        "data_end_date": max(dates) if dates else "",
                    }
                )
    return pd.DataFrame(rows)


def build_markdown(summary: pd.DataFrame, events: pd.DataFrame) -> str:
    lines: list[str] = [
        "# TDCC Weekly Ranking Formula Backtest",
        "",
        f"- model_id: `{MODEL_ID}`",
        f"- ranking_model_version: `{RANKING_MODEL_VERSION}`",
        f"- source_tdcc_dataset_id: `{safe_str(events.iloc[0].get('source_tdcc_dataset_id')) if not events.empty else ''}`",
        f"- generated_at: `{now_text()}`",
        f"- event_rows: `{len(events)}`",
        "- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.",
        "- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.",
        "",
        "## Top Summary",
        "",
    ]
    if summary.empty:
        lines.append("No matured ranking events.")
        return "\n".join(lines)
    top = summary.sort_values(["avg_return", "win_rate"], ascending=[False, False]).head(20)
    cols = [
        "tdcc_list_type",
        "rank_bucket",
        "horizon",
        "event_count",
        "win_rate",
        "avg_return",
        "median_return",
        "out_of_sample_size",
        "out_of_sample_pass",
        "confidence_status",
    ]
    lines.append(markdown_table(top, cols, limit=20))
    lines.extend(
        [
            "",
            "## Promotion Guardrail",
            "",
            "- `approved_for_daily` is always `False`.",
            "- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.",
        ]
    )
    return "\n".join(lines)


def build() -> tuple[pd.DataFrame, pd.DataFrame]:
    contract = load_research_tdcc_dataset_contract()
    deltas = weekly_delta_rows(contract)
    if deltas.empty:
        return pd.DataFrame(), pd.DataFrame()
    prelim = compute_score_columns(deltas)
    candidate_mask = (prelim["tdcc_effective_increase_count"] >= 1) | (
        prelim["tdcc_high_pair_effective_streak_weeks"] >= 2
    )
    candidates = add_volume_context(prelim[candidate_mask].copy())
    scored = compute_score_columns(candidates)
    events = add_return_columns(rank_weekly_models(scored))
    summary = summarize(events)
    if not summary.empty:
        summary["source_tdcc_dataset_id"] = contract.dataset_id
    return events, summary


def main() -> int:
    events, summary = build()
    if events.empty or summary.empty:
        raise RuntimeError("No TDCC weekly ranking backtest events were produced")

    write_csv(events, EVENTS_CSV)
    write_csv(summary, SUMMARY_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, DOCS_SUMMARY_CSV)
    markdown = build_markdown(summary, events)
    LATEST_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_SUMMARY_MD.write_text(markdown, encoding="utf-8")
    DOCS_SUMMARY_MD.write_text(markdown, encoding="utf-8")

    print(f"Saved: {EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_SUMMARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
