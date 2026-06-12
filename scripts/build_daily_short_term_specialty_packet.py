from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd
from tracking_utils import main_price_date_from_freshness


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

OUT_MD = LATEST_DIR / "daily_short_term_specialty_packet_latest.md"
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

TDCC_EDGE_STATS = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.csv"
TDCC_EDGE_CANDIDATES = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
WEEKLY_SURGE_STRICT_SEARCH = LATEST_DIR / "weekly_surge_strict_parameter_search_latest.csv"
WEEKLY_SURGE_STRICT_CANDIDATES = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv"
EXPLOSIVE_VOLUME_SUMMARY = LATEST_DIR / "explosive_volume_up_backtest_latest.csv"
EXPLOSIVE_VOLUME_POSITION_SUMMARY = LATEST_DIR / "explosive_volume_up_position_backtest_latest.csv"
EXPLOSIVE_VOLUME_EVENTS = LATEST_DIR / "explosive_volume_up_events_latest.csv"
MARKET_ABNORMAL_STATUS = LATEST_DIR / "market_abnormal_status_latest.csv"


def now_text() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str)
    except Exception:
        return pd.DataFrame()


def read_main_price_date() -> str:
    return main_price_date_from_freshness()


def md_table(headers: Iterable[str], rows: Iterable[Iterable[object]]) -> list[str]:
    headers = [str(h) for h in headers]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        values = [str(v).replace("\n", " ").strip() for v in row]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def pick_columns(df: pd.DataFrame, candidates: list[str]) -> list[str]:
    return [c for c in candidates if c in df.columns]


def top_rows(df: pd.DataFrame, columns: list[str], limit: int) -> list[list[object]]:
    if df.empty or not columns:
        width = max(len(columns), 1)
        return [["資料不足 / 僅能觀察"] + [""] * (width - 1)]
    safe = df.copy()
    for col in columns:
        if col not in safe.columns:
            safe[col] = ""
    return safe[columns].head(limit).fillna("").values.tolist()


def sort_numeric(df: pd.DataFrame, column: str, ascending: bool = False) -> pd.DataFrame:
    if df.empty or column not in df.columns:
        return df
    safe = df.copy()
    safe["_sort_value"] = pd.to_numeric(safe[column], errors="coerce")
    safe = safe.sort_values("_sort_value", ascending=ascending, na_position="last")
    return safe.drop(columns=["_sort_value"])


def d1_to_d10_labels() -> list[str]:
    return [f"D+{value}" for value in range(1, 11)]


def build_tdcc_edge_section(lines: list[str]) -> None:
    stats = read_csv(TDCC_EDGE_STATS)
    candidates = read_csv(TDCC_EDGE_CANDIDATES)

    lines.append("## TDCC Overheated Short-Term Edge")
    lines.append("")
    lines.append("- section_required_in_daily_pdf: `True`")
    lines.append("- section_type: `short_term_research_stat_support`")
    lines.append("- model_effect_allowed: `False`")
    lines.append("- allowed_use: `reporting_priority_only`")
    lines.append("- rule: `D+5` and `D+10` must be shown as separate tables.")
    lines.append("- rule: close-to-close metrics and next-open metrics must not be mixed.")
    lines.append("")

    if stats.empty:
        lines.append("### D+5 Stats")
        lines.extend(md_table(["status", "note"], [["missing", TDCC_EDGE_STATS.as_posix()]]))
        lines.append("")
        lines.append("### D+10 Stats")
        lines.extend(md_table(["status", "note"], [["missing", TDCC_EDGE_STATS.as_posix()]]))
        lines.append("")
    else:
        horizon_col = "horizon" if "horizon" in stats.columns else ""
        base_cols = pick_columns(
            stats,
            [
                "rule_name",
                "condition_name",
                "mature_count",
                "win_rate_close_to_close_pct",
                "avg_close_to_close_return_pct",
                "median_close_to_close_return_pct",
                "avg_relative_return_vs_benchmark_pct",
                "win_rate_next_open_to_close_pct",
                "avg_next_open_relative_return_vs_benchmark_pct",
                "sample_status",
            ],
        )
        for horizon in ["D+5", "D+10"]:
            lines.append(f"### {horizon} Stats")
            if horizon_col:
                sub = stats[stats[horizon_col].astype(str).str.upper().eq(horizon.upper())]
            else:
                sub = stats
            sub = sort_numeric(sub, "win_rate_next_open_to_close_pct")
            lines.extend(md_table(base_cols[:9] if base_cols else ["status"], top_rows(sub, base_cols[:9], 8)))
            lines.append("")

    lines.append("### Current TDCC Edge Candidates")
    candidate_cols = pick_columns(
        candidates,
        [
            "stock_id",
            "stock_name",
            "theme",
            "theme_mainstream_status",
            "tdcc_price_phase",
            "matched_rules",
            "research_priority",
            "next_confirmation",
            "risk_note",
        ],
    )
    lines.extend(md_table(candidate_cols[:9] if candidate_cols else ["status"], top_rows(candidates, candidate_cols[:9], 20)))
    lines.append("")


def build_weekly_surge_section(lines: list[str]) -> None:
    stats = read_csv(WEEKLY_SURGE_STRICT_SEARCH)
    candidates = read_csv(WEEKLY_SURGE_STRICT_CANDIDATES)

    lines.append("## Next-Open +10pct Touch Strict Parameter Research")
    lines.append("")
    lines.append("- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.")
    lines.append("- display_name_zh: `隔日開盤買進後 D+1 至 D+10 / D+20 盤中觸及 +10% 研究`")
    lines.append("- forbidden_label_zh: `周線急漲`")
    lines.append("- not_weekly_candle: `True`")
    lines.append("- section_required_in_daily_pdf: `True`")
    lines.append("- section_type: `short_term_research_stat_support`")
    lines.append("- entry_basis: `D+1 open`; the signal is only knowable after the signal-day close.")
    lines.append("- hit_definition: `D+1 open to D+N high reaches +10%`")
    lines.append("- close_exit_definition: `D+1 open to D+N close`; close-exit win rate uses return > 0.")
    lines.append("- intraperiod_low_definition: `D+1 open to D+N lowest low`; use this as adverse-move / pain-risk context.")
    lines.append("- required_risk_columns: `avg_loss_next_open_to_close_return_pct`, `worst_loss_next_open_to_close_return_pct`, `median_next_open_to_low_return_pct`, `worst_next_open_to_low_return_pct`, `top_stock_concentration_pct`.")
    lines.append("- win_rate_definition: keep +10% high touch-rate and close-exit win rate separate.")
    lines.append("- model_effect_allowed: `False`")
    lines.append("- allowed_use: `research_watchlist_and_reporting_priority_only`")
    lines.append("- market_abnormal_status: read `market_abnormal_status_latest.csv/md`; disposition/attention stocks must be flagged as execution-risk. Historical disposition filtering remains `disposition_history_not_backfilled` until daily snapshots or verified history are available.")
    lines.append("- rule: show a compact `D+1` to `D+10` summary, plus separate `D+5` and `D+10` tables with loss and intraperiod-low diagnostics.")
    lines.append("")

    if stats.empty:
        lines.append("### D+1 to D+10 Horizon Summary")
        lines.extend(md_table(["status", "note"], [["missing", WEEKLY_SURGE_STRICT_SEARCH.as_posix()]]))
        lines.append("")
        lines.append("### D+5 Parameter Table")
        lines.extend(md_table(["status", "note"], [["missing", WEEKLY_SURGE_STRICT_SEARCH.as_posix()]]))
        lines.append("")
        lines.append("### D+10 Parameter Table")
        lines.extend(md_table(["status", "note"], [["missing", WEEKLY_SURGE_STRICT_SEARCH.as_posix()]]))
        lines.append("")
    else:
        summary_rows = []
        for horizon in d1_to_d10_labels():
            sub = stats[stats.get("target_window", pd.Series(dtype=str)).astype(str).str.upper().eq(horizon.upper())].copy()
            if sub.empty:
                summary_rows.append([horizon, "missing", "", "", "", ""])
                continue
            for col in [
                "selected_stock_days",
                "hit_rate_pct",
                "median_next_open_to_high_return_pct",
                "win_rate_next_open_to_close_pct",
                "avg_next_open_to_close_return_pct",
                "median_next_open_to_close_return_pct",
                "median_next_open_to_low_return_pct",
                "avg_signal_close_to_next_open_gap_pct",
            ]:
                sub[col] = pd.to_numeric(sub.get(col), errors="coerce")
            sub = sub[sub["selected_stock_days"] >= 100].sort_values(["win_rate_next_open_to_close_pct", "avg_next_open_to_close_return_pct", "selected_stock_days"], ascending=[False, False, False])
            if sub.empty:
                summary_rows.append([horizon, "no sample>=100", "", "", "", ""])
                continue
            row = sub.iloc[0]
            summary_rows.append(
                [
                    horizon,
                    row.get("selected_stock_days", ""),
                    row.get("close_exit_mature_count", ""),
                    row.get("win_rate_next_open_to_close_pct", ""),
                    row.get("avg_next_open_to_close_return_pct", ""),
                    row.get("median_next_open_to_close_return_pct", ""),
                    row.get("median_next_open_to_low_return_pct", ""),
                    row.get("hit_rate_pct", ""),
                    row.get("avg_signal_close_to_next_open_gap_pct", ""),
                    row.get("rule_name", ""),
                ]
            )
        lines.append("### D+1 to D+10 Horizon Summary")
        lines.extend(md_table(["horizon", "selected", "close_mature", "close_win_rate", "avg_close_ret", "median_close_ret", "median_low_ret", "+10pct_touch_rate", "avg_gap", "best_rule"], summary_rows))
        lines.append("")
        cols = pick_columns(
            stats,
            [
                "rule_name",
                "target_window",
                "selected_stock_days",
                "win_rate_next_open_to_close_pct",
                "avg_next_open_to_close_return_pct",
                "median_next_open_to_close_return_pct",
                "avg_loss_next_open_to_close_return_pct",
                "worst_loss_next_open_to_close_return_pct",
                "hit_rate_pct",
                "median_next_open_to_high_return_pct",
                "median_next_open_to_low_return_pct",
                "worst_next_open_to_low_return_pct",
                "avg_next_open_to_high_return_pct",
                "avg_signal_close_to_next_open_gap_pct",
                "top_stock_concentration_pct",
                "sample_status",
            ],
        )
        for horizon in ["D+5", "D+10"]:
            lines.append(f"### {horizon} Parameter Table")
            if "target_window" in stats.columns:
                sub = stats[stats["target_window"].astype(str).str.upper().eq(horizon.upper())]
            else:
                sub = stats
            sub = sort_numeric(sub, "hit_rate_pct")
            lines.extend(md_table(cols[:12] if cols else ["status"], top_rows(sub, cols[:12], 12)))
            lines.append("")

    lines.append("### Current Strict Research Candidates")
    candidate_cols = pick_columns(
        candidates,
        [
            "research_priority",
            "stock_id",
            "stock_name",
            "theme",
            "matched_rules",
            "best_d5_hit_rate_pct",
            "best_d10_hit_rate_pct",
            "best_d10_rule",
            "market_abnormal_status",
            "market_abnormal_risk_level",
            "execution_risk_note",
            "research_caveat",
        ],
    )
    lines.extend(md_table(candidate_cols[:12] if candidate_cols else ["status"], top_rows(candidates, candidate_cols[:12], 25)))
    lines.append("")


def build_explosive_volume_section(lines: list[str]) -> None:
    summary = read_csv(EXPLOSIVE_VOLUME_SUMMARY)
    position_summary = read_csv(EXPLOSIVE_VOLUME_POSITION_SUMMARY)
    events = read_csv(EXPLOSIVE_VOLUME_EVENTS)

    lines.append("## Explosive Volume Up Research")
    lines.append("")
    lines.append("- section_required_in_daily_pdf: `True`")
    lines.append("- section_type: `short_term_research_stat_support`")
    lines.append("- signal_definition: signal day volume divided by previous 20 trading day average volume, with signal day close-to-close return >= threshold.")
    lines.append("- entry_basis: `D+1 open`")
    lines.append("- close_win_rate: D+1 open to D+N close return > 0.")
    lines.append("- high_hit_rate: after D+1 open entry, highest high during the holding window reaches +10% or +20%; this is performance labeling, not intraday signal entry.")
    lines.append("- strict_candle_quality: red candle, real body >= 40% of intraday range, upper shadow <= 25%, close location >= 75%.")
    lines.append("- relaxed_candle_quality: red candle, real body >= 25% of intraday range, upper shadow <= 35%, close location >= 65%.")
    lines.append("- model_effect_allowed: `False`")
    lines.append("- allowed_use: `research_watchlist_and_reporting_priority_only`")
    lines.append("- rule: volume alone is not a core buy signal; combine with theme/mainstream status, TDCC phase, market regime, and technical position.")
    lines.append("- position_rule: split bottom/low-zone volume reversal, low-to-mid reclaim, near-high attack, and high-zone extension before interpreting win rate.")
    lines.append("")

    if summary.empty:
        lines.append("### D+10 / D+20 Parameter Tables")
        lines.extend(md_table(["status", "note"], [["missing", EXPLOSIVE_VOLUME_SUMMARY.as_posix()]]))
        lines.append("")
        return

    cols = pick_columns(
        summary,
        [
            "rule_name",
            "horizon",
            "selected_stock_days",
            "mature_count",
            "close_win_rate_pct",
            "avg_close_return_pct",
            "median_close_return_pct",
            "hit_rate_high_ge_10pct",
            "hit_rate_high_ge_20pct",
            "sample_status",
        ],
    )
    for horizon in ["D+5", "D+10", "D+20"]:
        lines.append(f"### {horizon} Explosive Volume Table")
        sub = summary[summary["horizon"].astype(str).str.upper().eq(horizon)]
        sub = sort_numeric(sub, "hit_rate_high_ge_10pct")
        lines.extend(md_table(cols[:10] if cols else ["status"], top_rows(sub, cols[:10], 15)))
        lines.append("")

    if not position_summary.empty:
        position_cols = pick_columns(
            position_summary,
            [
                "signal_quality_bucket",
                "price_position_bucket",
                "market_theme_group",
                "theme_group_source",
                "theme_structural_status",
                "structural_theme_bucket",
                "theme_mainstream_label",
                "theme_status_group",
                "horizon",
                "volume_ratio_threshold",
                "min_signal_return_pct",
                "mature_count",
                "close_win_rate_pct",
                "avg_close_return_pct",
                "median_close_return_pct",
                "hit_rate_high_ge_10pct",
                "hit_rate_high_ge_20pct",
                "avg_mfe_pct",
                "avg_mae_pct",
                "sample_status",
            ],
        )
        for horizon in ["D+5", "D+10", "D+20"]:
            lines.append(f"### {horizon} Explosive Volume By Price Position")
            sub = position_summary[position_summary["horizon"].astype(str).str.upper().eq(horizon)]
            sub = sort_numeric(sub, "close_win_rate_pct")
            lines.extend(md_table(position_cols[:13] if position_cols else ["status"], top_rows(sub, position_cols[:13], 20)))
            lines.append("")
    else:
        lines.append("### Explosive Volume By Price Position")
        lines.extend(md_table(["status", "note"], [["missing", EXPLOSIVE_VOLUME_POSITION_SUMMARY.as_posix()]]))
        lines.append("")

    lines.append("### Latest Explosive Volume Events")
    event_cols = pick_columns(
        events,
        [
            "date",
            "stock_id",
            "stock_name",
            "industry",
            "market",
            "close",
            "volume_ratio_vs_prev20",
            "signal_return_1d_pct",
            "signal_quality_bucket",
            "price_position_bucket",
            "market_theme_group",
            "theme_group_source",
            "theme_structural_status",
            "structural_theme_bucket",
            "theme_mainstream_label",
            "next_open_to_d10_max_high_return_pct",
            "next_open_to_d20_max_high_return_pct",
        ],
    )
    if event_cols:
        safe = events.copy()
        safe["date_sort"] = safe["date"].astype(str)
        safe = safe.sort_values(["date_sort", "volume_ratio_vs_prev20"], ascending=[False, False])
        lines.extend(md_table(event_cols, top_rows(safe, event_cols, 20)))
    else:
        lines.extend(md_table(["status"], [["missing_columns"]]))
    lines.append("")


def build_packet() -> str:
    lines: list[str] = []
    lines.append("# DAILY SHORT-TERM SPECIALTY PACKET")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{read_main_price_date()}`")
    lines.append("- purpose: Force daily reports to include short-term research-stat support sections without removing active D+5/D+10 core model rows.")
    lines.append(f"- market_abnormal_status_path: `{MARKET_ABNORMAL_STATUS.as_posix()}`")
    lines.append("")
    lines.append("## Usage Contract")
    lines.append("- This packet is mandatory for daily stock candidate analysis.")
    lines.append("- `回檔後短線轉強` and `TDCC短線延續模型 D+5/D+10` are separate model concepts.")
    lines.append("- The daily PDF must include a standalone short-term research-stat support section if this packet exists.")
    lines.append("- The section must include D+5 and D+10 tables separately.")
    lines.append("- These research-stat tables are supporting evidence only. Do not override core TDCC, ABM, or daily candidate model weights.")
    lines.append("- If data is missing, write `資料不足 / 僅能觀察`; do not silently omit the section.")
    lines.append("")
    build_tdcc_edge_section(lines)
    build_weekly_surge_section(lines)
    build_explosive_volume_section(lines)
    lines.append("## PDF Placement")
    lines.append("- Place after the three-line candidate split and before or near category interpretation.")
    lines.append("- Do not use this packet to replace the active core model ranking table.")
    lines.append("- If current candidates overlap with core candidate rows, show the overlap as supporting evidence, not as a second buy/sell gate.")
    lines.append("")
    lines.append("## Data Quality Notes")
    lines.append("- Short-term samples are not full-cycle regime proof yet.")
    lines.append("- Current use is suitable for tracking priority and discussion, not formal weight tuning.")
    lines.append("- More bear-market and range-market samples are still required.")
    lines.append("")
    return normalize_packet_text("\n".join(lines) + "\n")


def normalize_packet_text(text: str) -> str:
    normalized: list[str] = []
    for line in text.splitlines():
        if line.startswith("- display_name_zh:"):
            line = "- display_name_zh: `短線急漲 D+1 到 D+10 / D+20 次日開盤進場 +10% 觸及研究`"
        elif line.startswith("- forbidden_label_zh:"):
            line = "- forbidden_label_zh: `週線急漲`"
        elif "is one of the six fixed categories" in line:
            line = "- `回檔後短線轉強` is one of the fixed candidate categories; it is not the whole short-term specialty layer."
        elif "If data is missing, write" in line:
            line = "- If data is missing, write `資料不足 / 僅能觀察`; do not silently omit the section."
        normalized.append(line)
    return "\n".join(normalized) + "\n"


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    text = build_packet()
    for path in [OUT_MD, DOCS_MD]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"Saved: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
