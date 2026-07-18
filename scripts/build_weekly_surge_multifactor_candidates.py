from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from research_weekly_20pct_surge_volume import PRICE_DIR, normalize_stock_id, read_price
from research_weekly_surge_multifactor_grid import (
    attach_market_context,
    attach_tdcc_context,
    build_rules,
    write_csv,
)
from research_weekly_surge_technical_grid import add_technical_features
from research_weekly_surge_theme_segments import attach_theme_labels
from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract, require_dataset_id


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

GRID_CSV = LATEST_DIR / "weekly_surge_multifactor_filter_grid_latest.csv"
OUT_CSV = LATEST_DIR / "weekly_surge_multifactor_candidates_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_multifactor_candidates_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_multifactor_candidates.csv"
MARKET_ABNORMAL_STATUS_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def build_latest_stock_frame() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(PRICE_DIR.glob("*.csv")):
        df = read_price(path)
        if len(df) < 60:
            continue
        df = df.sort_values("date").copy()
        df["volume_ma20_prev"] = df["volume"].shift(1).rolling(20, min_periods=20).mean()
        df["start_day_volume_ratio_vs_prev20"] = df["volume"] / df["volume_ma20_prev"]
        df["prev_day_volume_ratio_vs_prev20"] = df["volume"].shift(1) / df["volume"].shift(2).rolling(20, min_periods=20).mean()
        df["start_5d_avg_volume_ratio_vs_prev20"] = df["volume"].rolling(5, min_periods=5).mean() / df["volume_ma20_prev"]
        df["prev_5d_avg_volume_ratio_vs_prev20"] = df["volume"].shift(1).rolling(5, min_periods=5).mean() / df["volume_ma20_prev"]
        frames.append(df)
    if not frames:
        return pd.DataFrame()

    full = pd.concat(frames, ignore_index=True)
    full = add_technical_features(full)
    full["stock_id"] = full["stock_id"].map(normalize_stock_id)
    latest_date = full["date"].astype(str).str.replace(r"\D", "", regex=True).max()
    latest = full[full["date"].astype(str).str.replace(r"\D", "", regex=True) == latest_date].copy()
    latest = latest.dropna(subset=["start_5d_avg_volume_ratio_vs_prev20", "start_day_volume_ratio_vs_prev20"])
    latest = attach_theme_labels(latest)
    latest = attach_tdcc_context(latest)
    latest = attach_market_context(latest)
    return latest.reset_index(drop=True)


def load_grid() -> pd.DataFrame:
    if not GRID_CSV.exists():
        return pd.DataFrame()
    grid = pd.read_csv(GRID_CSV, dtype=str, keep_default_na=False)
    require_dataset_id(grid, load_research_tdcc_dataset_contract(), label=GRID_CSV.as_posix())
    for col in [
        "hit_rate_pct",
        "median_next_open_to_high_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "selected_stock_days",
        "tdcc_available_rate_pct",
    ]:
        grid[col] = pd.to_numeric(grid.get(col), errors="coerce")
    return grid


def load_market_abnormal_status() -> pd.DataFrame:
    if not MARKET_ABNORMAL_STATUS_CSV.exists():
        return pd.DataFrame(columns=["stock_id"])
    df = pd.read_csv(MARKET_ABNORMAL_STATUS_CSV, dtype=str, keep_default_na=False)
    if "stock_id" not in df.columns:
        return pd.DataFrame(columns=["stock_id"])
    keep = [
        col
        for col in [
            "stock_id",
            "market_abnormal_status",
            "market_abnormal_risk_level",
            "is_disposition",
            "is_attention",
            "is_attention_accumulation",
            "is_periodic_trading",
            "disposition_period",
            "execution_risk_note",
        ]
        if col in df.columns
    ]
    out = df[keep].copy()
    out["stock_id"] = out["stock_id"].astype(str).str.extract(r"(\d{4})", expand=False).fillna("")
    return out[out["stock_id"] != ""].drop_duplicates("stock_id", keep="last")


def attach_market_abnormal_status(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.copy()
    out["stock_id"] = out["stock_id"].astype(str).str.extract(r"(\d{4})", expand=False).fillna(out["stock_id"].astype(str))
    abnormal = load_market_abnormal_status()
    if abnormal.empty:
        out["market_abnormal_status"] = "not_checked"
        out["market_abnormal_risk_level"] = "history_not_backfilled"
        out["is_disposition"] = False
        out["is_attention"] = False
        out["is_attention_accumulation"] = False
        out["is_periodic_trading"] = False
        out["disposition_period"] = ""
        out["execution_risk_note"] = "處置/注意歷史尚未回補；短線回測暫未分層。"
        return out
    out = out.merge(abnormal, on="stock_id", how="left")
    out["market_abnormal_status"] = out["market_abnormal_status"].fillna("normal")
    out["market_abnormal_risk_level"] = out["market_abnormal_risk_level"].fillna("A_normal")
    for col in ["is_disposition", "is_attention", "is_attention_accumulation", "is_periodic_trading"]:
        out[col] = out[col].fillna(False).astype(str).str.lower().isin(["true", "1", "yes"])
    out["disposition_period"] = out["disposition_period"].fillna("")
    out["execution_risk_note"] = out["execution_risk_note"].fillna("")
    return out


def compact_rule_metrics(grid: pd.DataFrame, rule_name: str) -> dict[str, object]:
    part = grid[grid["rule_name"] == rule_name]
    out: dict[str, object] = {}
    for window in ["D+5", "D+10", "D+20"]:
        row = part[part["target_window"] == window]
        if row.empty:
            continue
        first = row.iloc[0]
        key = window.lower().replace("+", "")
        out[f"{key}_hit_rate_pct"] = first.get("hit_rate_pct", "")
        out[f"{key}_median_next_open_to_high_return_pct"] = first.get("median_next_open_to_high_return_pct", "")
        out[f"{key}_selected_stock_days"] = first.get("selected_stock_days", "")
        out[f"{key}_sample_status"] = first.get("sample_status", "")
    return out


def research_priority(row: pd.Series) -> str:
    d10 = pd.to_numeric(row.get("best_d10_hit_rate_pct"), errors="coerce")
    d5 = pd.to_numeric(row.get("best_d5_hit_rate_pct"), errors="coerce")
    status = str(row.get("best_d10_sample_status", ""))
    if pd.notna(d10) and d10 >= 45 and status != "insufficient_sample":
        return "A_research_watch"
    if pd.notna(d10) and d10 >= 40:
        return "B_research_confirm"
    if pd.notna(d5) and d5 >= 25:
        return "C_short_term_watch"
    return "D_background_only"


def build_candidates(latest: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    if latest.empty or grid.empty:
        return pd.DataFrame()
    latest = attach_market_abnormal_status(latest)
    rule_rows: list[pd.DataFrame] = []
    for rule_name, mask, family, source_type in build_rules(latest):
        picked = latest[mask].copy()
        if picked.empty:
            continue
        metrics = compact_rule_metrics(grid, rule_name)
        picked["matched_rule"] = rule_name
        picked["rule_family"] = family
        picked["source_type"] = source_type
        for key, value in metrics.items():
            picked[key] = value
        rule_rows.append(picked)
    if not rule_rows:
        return pd.DataFrame()

    long = pd.concat(rule_rows, ignore_index=True)
    for col in ["d5_hit_rate_pct", "d10_hit_rate_pct", "d20_hit_rate_pct"]:
        long[col] = pd.to_numeric(long.get(col), errors="coerce")

    rows: list[dict[str, object]] = []
    group_cols = ["date", "stock_id"]
    for (_, _), part in long.groupby(group_cols, sort=False):
        best_d10 = part.sort_values(["d10_hit_rate_pct", "d5_hit_rate_pct"], ascending=False).iloc[0]
        best_d5 = part.sort_values(["d5_hit_rate_pct", "d10_hit_rate_pct"], ascending=False).iloc[0]
        best_d20 = part.sort_values(["d20_hit_rate_pct", "d10_hit_rate_pct"], ascending=False).iloc[0]
        base = best_d10
        matched_rules = "; ".join(part.sort_values("d10_hit_rate_pct", ascending=False)["matched_rule"].head(6).tolist())
        latest_theme_status = str(base.get("latest_theme_status_group", ""))
        source_type = str(base.get("source_type", ""))
        caveat_parts = ["research_only", "entry_basis_D+1_open", "target_next_open_to_high_10pct"]
        if "latest_theme" in source_type or latest_theme_status not in {"", "unlabeled"}:
            caveat_parts.append("latest_theme_label_provisional")
        if str(base.get("best_d10_sample_status", "")) == "insufficient_sample":
            caveat_parts.append("insufficient_sample")

        rows.append(
            {
                "date": base.get("date", ""),
                "source_tdcc_dataset_id": base.get("source_tdcc_dataset_id", ""),
                "stock_id": base.get("stock_id", ""),
                "stock_name": base.get("stock_name", ""),
                "market": base.get("market", ""),
                "close": base.get("close", ""),
                "volume": base.get("volume", ""),
                "start_day_volume_ratio_vs_prev20": round(float(base.get("start_day_volume_ratio_vs_prev20", 0)), 2),
                "start_5d_avg_volume_ratio_vs_prev20": round(float(base.get("start_5d_avg_volume_ratio_vs_prev20", 0)), 2),
                "return_5d_pct": round(float(base.get("return_5d_pct", 0)), 2) if pd.notna(base.get("return_5d_pct")) else "",
                "return_10d_pct": round(float(base.get("return_10d_pct", 0)), 2) if pd.notna(base.get("return_10d_pct")) else "",
                "return_20d_pct": round(float(base.get("return_20d_pct", 0)), 2) if pd.notna(base.get("return_20d_pct")) else "",
                "rsi14": round(float(base.get("rsi14", 0)), 2) if pd.notna(base.get("rsi14")) else "",
                "macd_hist": round(float(base.get("macd_hist", 0)), 4) if pd.notna(base.get("macd_hist")) else "",
                "bb_width_pct_rank_120d": round(float(base.get("bb_width_pct_rank_120d", 0)), 2) if pd.notna(base.get("bb_width_pct_rank_120d")) else "",
                "latest_theme_status_group": base.get("latest_theme_status_group", ""),
                "latest_theme_final_status": base.get("latest_theme_final_status", ""),
                "latest_theme_volume_attack_status": base.get("latest_theme_volume_attack_status", ""),
                "tdcc_available": base.get("tdcc_available", False),
                "tdcc_all_thresholds_up": base.get("tdcc_all_thresholds_up", False),
                "tdcc_high_thresholds_up": base.get("tdcc_high_thresholds_up", False),
                "tdcc_high_up_streak": base.get("tdcc_high_up_streak", ""),
                "tdcc_high_change_sum": round(float(base.get("tdcc_high_change_sum", 0)), 4),
                "derived_market_regime": base.get("derived_market_regime", ""),
                "market_abnormal_status": base.get("market_abnormal_status", ""),
                "market_abnormal_risk_level": base.get("market_abnormal_risk_level", ""),
                "is_disposition": base.get("is_disposition", False),
                "is_attention": base.get("is_attention", False),
                "is_periodic_trading": base.get("is_periodic_trading", False),
                "disposition_period": base.get("disposition_period", ""),
                "execution_risk_note": base.get("execution_risk_note", ""),
                "matched_rules": matched_rules,
                "best_d5_rule": best_d5.get("matched_rule", ""),
                "best_d5_hit_rate_pct": best_d5.get("d5_hit_rate_pct", ""),
                "best_d5_sample_status": best_d5.get("d5_sample_status", ""),
                "best_d10_rule": best_d10.get("matched_rule", ""),
                "best_d10_hit_rate_pct": best_d10.get("d10_hit_rate_pct", ""),
                "best_d10_sample_status": best_d10.get("d10_sample_status", ""),
                "best_d20_rule": best_d20.get("matched_rule", ""),
                "best_d20_hit_rate_pct": best_d20.get("d20_hit_rate_pct", ""),
                "best_d20_sample_status": best_d20.get("d20_sample_status", ""),
                "model_effect_allowed": False,
                "core_weight_change_allowed": False,
                "research_caveat": "; ".join(caveat_parts),
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["research_priority"] = out.apply(research_priority, axis=1)
    return out.sort_values(
        ["research_priority", "best_d10_hit_rate_pct", "best_d5_hit_rate_pct", "start_5d_avg_volume_ratio_vs_prev20"],
        ascending=[True, False, False, False],
    ).reset_index(drop=True)


def df_to_md(df: pd.DataFrame, limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    return df.head(limit).to_markdown(index=False)


def build_markdown(candidates: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Next-Open +10pct Multifactor Candidates")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    dataset_ids = sorted({str(value) for value in candidates.get("source_tdcc_dataset_id", []) if str(value)})
    lines.append(f"- source_tdcc_dataset_id: `{dataset_ids[0] if len(dataset_ids) == 1 else 'missing_or_mixed'}`")
    lines.append("- use: research watchlist only; do not mix into daily candidate core ranking.")
    lines.append("- entry_basis: D+1 open.")
    lines.append("- target: next-open to D+1 / ... / D+10 / D+20 high >= 10%.")
    lines.append("- caveat: latest theme labels are provisional until strict daily theme history accumulates.")
    lines.append("")
    if candidates.empty:
        lines.append("_No current candidates matched the research rules._")
        return "\n".join(lines) + "\n"

    date = candidates["date"].astype(str).max()
    lines.append(f"- signal_date: `{date}`")
    lines.append(f"- matched_stocks: `{len(candidates)}`")
    lines.append(f"- priority_counts: `{'; '.join(f'{k}={v}' for k, v in candidates['research_priority'].value_counts().items())}`")
    lines.append("")

    keep = [
        "research_priority",
        "stock_id",
        "stock_name",
        "market",
        "close",
        "start_5d_avg_volume_ratio_vs_prev20",
        "latest_theme_status_group",
        "tdcc_all_thresholds_up",
        "derived_market_regime",
        "market_abnormal_status",
        "best_d5_hit_rate_pct",
        "best_d10_hit_rate_pct",
        "best_d10_sample_status",
        "best_d10_rule",
        "research_caveat",
    ]
    for priority in ["A_research_watch", "B_research_confirm", "C_short_term_watch", "D_background_only"]:
        part = candidates[candidates["research_priority"] == priority]
        lines.append(f"## {priority}")
        lines.append("")
        lines.append(df_to_md(part[keep], limit=40))
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    contract = load_research_tdcc_dataset_contract()
    latest = build_latest_stock_frame()
    grid = load_grid()
    candidates = build_candidates(latest, grid)
    if candidates.empty:
        candidates["source_tdcc_dataset_id"] = pd.Series(dtype=str)
    else:
        require_dataset_id(candidates, contract, label=OUT_CSV.as_posix())
    write_csv(candidates, OUT_CSV)
    write_csv(candidates, HISTORY_CSV)
    OUT_MD.write_text(build_markdown(candidates), encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(candidates)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
