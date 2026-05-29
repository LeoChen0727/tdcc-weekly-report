from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_weekly_surge_multifactor_candidates import build_latest_stock_frame
from research_weekly_surge_strict_parameter_search import build_parameter_masks, write_csv


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

GRID_CSV = LATEST_DIR / "weekly_surge_strict_parameter_search_latest.csv"
OUT_CSV = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_strict_parameter_candidates.csv"
MARKET_ABNORMAL_STATUS_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def load_candidate_rules() -> pd.DataFrame:
    if not GRID_CSV.exists():
        return pd.DataFrame()
    grid = pd.read_csv(GRID_CSV, dtype=str, keep_default_na=False)
    for col in [
        "hit_rate_pct",
        "selected_stock_days",
        "median_next_open_to_high_return_pct",
        "coverage_of_all_hits_pct",
        "avg_signal_close_to_next_open_gap_pct",
    ]:
        grid[col] = pd.to_numeric(grid.get(col), errors="coerce")
    eligible = grid[
        (grid["sample_status"] == "ok_initial_sample")
        & (
            ((grid["target_window"] == "D+5") & (grid["hit_rate_pct"] >= 35))
            | ((grid["target_window"] == "D+10") & (grid["hit_rate_pct"] >= 50))
            | ((grid["target_window"] == "D+20") & (grid["hit_rate_pct"] >= 60))
        )
    ].copy()
    return eligible


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


def metrics_for_rule(rules: pd.DataFrame, rule_name: str) -> dict[str, object]:
    out: dict[str, object] = {}
    part = rules[rules["rule_name"] == rule_name]
    for window in ["D+5", "D+10", "D+20"]:
        row = part[part["target_window"] == window]
        if row.empty:
            continue
        first = row.iloc[0]
        key = window.lower().replace("+", "")
        out[f"{key}_hit_rate_pct"] = first.get("hit_rate_pct", "")
        out[f"{key}_selected_stock_days"] = first.get("selected_stock_days", "")
        out[f"{key}_median_next_open_to_high_return_pct"] = first.get("median_next_open_to_high_return_pct", "")
        out[f"{key}_coverage_of_all_hits_pct"] = first.get("coverage_of_all_hits_pct", "")
    return out


def research_priority(row: pd.Series) -> str:
    d10 = pd.to_numeric(row.get("best_d10_hit_rate_pct"), errors="coerce")
    d5 = pd.to_numeric(row.get("best_d5_hit_rate_pct"), errors="coerce")
    if pd.notna(d10) and d10 >= 60:
        return "A_strict_research_watch"
    if pd.notna(d10) and d10 >= 50:
        return "B_strict_research_confirm"
    if pd.notna(d5) and d5 >= 35:
        return "C_strict_short_term_watch"
    return "D_background_only"


def build_candidates(latest: pd.DataFrame, rules: pd.DataFrame) -> pd.DataFrame:
    if latest.empty or rules.empty:
        return pd.DataFrame()
    latest = attach_market_abnormal_status(latest)
    masks = build_parameter_masks(latest)
    long_rows: list[pd.DataFrame] = []
    for rule_name in sorted(rules["rule_name"].unique()):
        parts = [part.strip() for part in rule_name.split("+")]
        if not parts or any(part not in masks for part in parts):
            continue
        mask = pd.Series(True, index=latest.index)
        for part in parts:
            mask = mask & masks[part]
        picked = latest[mask].copy()
        if picked.empty:
            continue
        picked["matched_rule"] = rule_name
        for key, value in metrics_for_rule(rules, rule_name).items():
            picked[key] = value
        long_rows.append(picked)
    if not long_rows:
        return pd.DataFrame()

    long = pd.concat(long_rows, ignore_index=True)
    for col in ["d5_hit_rate_pct", "d10_hit_rate_pct", "d20_hit_rate_pct"]:
        long[col] = pd.to_numeric(long.get(col), errors="coerce")

    rows: list[dict[str, object]] = []
    for (_, _), part in long.groupby(["date", "stock_id"], sort=False):
        best_d10 = part.sort_values(["d10_hit_rate_pct", "d5_hit_rate_pct"], ascending=False).iloc[0]
        best_d5 = part.sort_values(["d5_hit_rate_pct", "d10_hit_rate_pct"], ascending=False).iloc[0]
        best_d20 = part.sort_values(["d20_hit_rate_pct", "d10_hit_rate_pct"], ascending=False).iloc[0]
        base = best_d10
        rows.append(
            {
                "date": base.get("date", ""),
                "stock_id": base.get("stock_id", ""),
                "stock_name": base.get("stock_name", ""),
                "market": base.get("market", ""),
                "close": base.get("close", ""),
                "volume": base.get("volume", ""),
                "start_5d_avg_volume_ratio_vs_prev20": round(float(base.get("start_5d_avg_volume_ratio_vs_prev20", 0)), 2),
                "start_day_volume_ratio_vs_prev20": round(float(base.get("start_day_volume_ratio_vs_prev20", 0)), 2),
                "return_5d_pct": round(float(base.get("return_5d_pct", 0)), 2) if pd.notna(base.get("return_5d_pct")) else "",
                "return_10d_pct": round(float(base.get("return_10d_pct", 0)), 2) if pd.notna(base.get("return_10d_pct")) else "",
                "return_20d_pct": round(float(base.get("return_20d_pct", 0)), 2) if pd.notna(base.get("return_20d_pct")) else "",
                "rsi14": round(float(base.get("rsi14", 0)), 2) if pd.notna(base.get("rsi14")) else "",
                "macd_hist": round(float(base.get("macd_hist", 0)), 4) if pd.notna(base.get("macd_hist")) else "",
                "tdcc_available": base.get("tdcc_available", False),
                "tdcc_all_thresholds_up": base.get("tdcc_all_thresholds_up", False),
                "tdcc_high_thresholds_up": base.get("tdcc_high_thresholds_up", False),
                "tdcc_high_up_streak": base.get("tdcc_high_up_streak", ""),
                "derived_market_regime": base.get("derived_market_regime", ""),
                "market_abnormal_status": base.get("market_abnormal_status", ""),
                "market_abnormal_risk_level": base.get("market_abnormal_risk_level", ""),
                "is_disposition": base.get("is_disposition", False),
                "is_attention": base.get("is_attention", False),
                "is_periodic_trading": base.get("is_periodic_trading", False),
                "disposition_period": base.get("disposition_period", ""),
                "execution_risk_note": base.get("execution_risk_note", ""),
                "matched_rules": "; ".join(part.sort_values("d10_hit_rate_pct", ascending=False)["matched_rule"].head(8).tolist()),
                "best_d5_rule": best_d5.get("matched_rule", ""),
                "best_d5_hit_rate_pct": best_d5.get("d5_hit_rate_pct", ""),
                "best_d10_rule": best_d10.get("matched_rule", ""),
                "best_d10_hit_rate_pct": best_d10.get("d10_hit_rate_pct", ""),
                "best_d10_selected_stock_days": best_d10.get("d10_selected_stock_days", ""),
                "best_d20_rule": best_d20.get("matched_rule", ""),
                "best_d20_hit_rate_pct": best_d20.get("d20_hit_rate_pct", ""),
                "model_effect_allowed": False,
                "core_weight_change_allowed": False,
                "research_caveat": "strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled",
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
    lines.append("# Next-Open +10pct Strict Parameter Candidates")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- use: strict research watchlist only; no latest theme label is used.")
    lines.append("- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.")
    lines.append("- display_name_zh: `隔日開盤買進後 D+1 至 D+10、D+20 盤中觸及 +10% 候選`.")
    lines.append("- not_weekly_candle: `True`.")
    lines.append("- entry_basis: D+1 open, because the signal is only known after the signal-day close.")
    lines.append("- target: next-open to D+1 / ... / D+10 / D+20 high >= 10%.")
    lines.append("- win_rate_definition: touch-rate of +10% intraperiod high after next-open entry; not close-to-close return.")
    lines.append("- caveat: research only; do not mix into daily candidate core ranking.")
    lines.append("")
    if candidates.empty:
        lines.append("_No current candidates matched strict research rules._")
        return "\n".join(lines) + "\n"

    lines.append(f"- signal_date: `{candidates['date'].astype(str).max()}`")
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
        "return_10d_pct",
        "rsi14",
        "tdcc_high_thresholds_up",
        "derived_market_regime",
        "market_abnormal_status",
        "best_d5_hit_rate_pct",
        "best_d10_hit_rate_pct",
        "best_d10_selected_stock_days",
        "best_d10_rule",
        "research_caveat",
    ]
    for priority in ["A_strict_research_watch", "B_strict_research_confirm", "C_strict_short_term_watch", "D_background_only"]:
        part = candidates[candidates["research_priority"] == priority]
        lines.append(f"## {priority}")
        lines.append("")
        lines.append(df_to_md(part[keep], limit=40))
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    latest = build_latest_stock_frame()
    rules = load_candidate_rules()
    candidates = build_candidates(latest, rules)
    write_csv(candidates, OUT_CSV)
    write_csv(candidates, HISTORY_CSV)
    OUT_MD.write_text(build_markdown(candidates), encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(candidates)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
