from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

OUT_MD = LATEST_DIR / "chatgpt_indicator_usage_guide_latest.md"
OUT_TXT = LATEST_DIR / "CHATGPT_INDICATOR_USAGE_GUIDE.txt"
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
DOCS_TXT = DOCS_LATEST_DIR / OUT_TXT.name

RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"


def now_text() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    else:
        rel = path.as_posix()
    return f"{PAGES_PREFIX}/{rel}"


def read_csv(path: str | Path, max_rows: int | None = None) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(p, dtype=str, nrows=max_rows)
    except Exception:
        return pd.DataFrame()


def count_values(df: pd.DataFrame, column: str, limit: int = 12) -> str:
    if df.empty or column not in df.columns:
        return "missing"
    values = (
        df[column]
        .fillna("")
        .astype(str)
        .str.strip()
        .replace({"nan": ""})
    )
    counts = values[values != ""].value_counts().head(limit)
    if counts.empty:
        return "empty"
    return "; ".join(f"{k}={v}" for k, v in counts.items())


def rows(path: str | Path) -> int:
    df = read_csv(path)
    return 0 if df.empty else len(df)


def md_table(headers: Iterable[str], rows_: Iterable[Iterable[str]]) -> list[str]:
    headers = list(headers)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows_:
        values = [str(v).replace("\n", " ").strip() for v in row]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def file_status(path: str | Path) -> str:
    p = Path(path)
    if not p.exists():
        return "missing"
    if p.suffix.lower() == ".csv":
        df = read_csv(p, max_rows=5)
        if df.empty:
            return "exists_but_unreadable_or_empty"
        return "ready"
    text = p.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return "empty"
    if len(text.splitlines()) <= 1:
        return "suspicious_single_line"
    return "ready"


def build_guide() -> str:
    daily_decision = read_csv(LATEST_DIR / "daily_candidate_decision_latest.csv")
    repeat = read_csv(LATEST_DIR / "candidate_repeat_appearance_latest.csv")
    tdcc_strength = read_csv(LATEST_DIR / "tdcc_strength_ranking_top_latest.csv")
    tdcc_abm = read_csv(LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv")
    tdcc_risk = read_csv(LATEST_DIR / "tdcc_top_risk_list_latest.csv")
    tdcc_overheated_edge = read_csv(LATEST_DIR / "tdcc_overheated_short_term_edge_latest.csv")
    tdcc_overheated_edge_candidates = read_csv(LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv")
    warrant = read_csv(LATEST_DIR / "warrant_flow_by_stock_latest.csv")
    market = read_csv(LATEST_DIR / "market_regime_latest.csv")
    market_timing = read_csv(LATEST_DIR / "market_timing_backtest_latest.csv")
    surge = read_csv(LATEST_DIR / "surge_precondition_candidates_latest.csv")
    performance = read_csv(LATEST_DIR / "daily_signal_performance_summary_latest.csv")
    individual_index = read_csv(LATEST_DIR / "individual_stock_available_raw_data_index_slim.csv")
    catalyst_needs_review = read_csv(LATEST_DIR / "catalyst_needs_review_latest.csv")
    chip = read_csv(LATEST_DIR / "chip_flow_positive_streak_latest.csv")
    volume_breakout = read_csv(LATEST_DIR / "volume_breakout_watch_latest.csv")
    volume_attack_theme = read_csv(LATEST_DIR / "volume_attack_theme_layer_latest.csv")
    volume_attack_stocks = read_csv(LATEST_DIR / "volume_attack_theme_stocks_latest.csv")
    daily_theme_status_history = read_csv(LATEST_DIR / "daily_theme_status_history_latest.csv")
    weekly_surge_theme_segment = read_csv(LATEST_DIR / "weekly_surge_theme_segment_next_open_latest.csv")
    weekly_surge_technical_grid = read_csv(LATEST_DIR / "weekly_surge_technical_filter_grid_latest.csv")
    weekly_surge_multifactor_grid = read_csv(LATEST_DIR / "weekly_surge_multifactor_filter_grid_latest.csv")
    weekly_surge_multifactor_candidates = read_csv(LATEST_DIR / "weekly_surge_multifactor_candidates_latest.csv")
    weekly_surge_strict_search = read_csv(LATEST_DIR / "weekly_surge_strict_parameter_search_latest.csv")
    weekly_surge_strict_candidates = read_csv(LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv")
    short_term_specialty_packet = LATEST_DIR / "daily_short_term_specialty_packet_latest.md"
    non_revenue_momentum = read_csv(LATEST_DIR / "non_revenue_momentum_watch_latest.csv")

    main_price_date = ""
    readme = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("main_price_date="):
                main_price_date = line.split("=", 1)[1].strip()
                break

    lines: list[str] = []
    lines.append("# ChatGPT Indicator Usage Guide")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{main_price_date}`")
    lines.append("- purpose: Use program-side classifications first. ChatGPT should explain and synthesize, not re-rank from memory.")
    lines.append("- rule: If memory, PDF, or ad-hoc interpretation conflicts with program-side fields, use the structured program-side fields.")
    lines.append("")

    lines.append("## Delivery Contract")
    lines.append("")
    lines.append("- Repo pipeline PDFs / Markdown / packets are source artifacts, validation artifacts, or shareable reference outputs.")
    lines.append("- `report_ready=True` means repo data and artifacts are available; it does not mean ChatGPT has completed the requested report.")
    lines.append("- `fixed_pdf_validation_status=pass` means repo PDF artifacts passed validation; it is not the same as a newly generated ChatGPT deliverable PDF.")
    lines.append("- If the user asks only for pipeline/repo status, report artifact status and links.")
    lines.append("- If the user asks to do today's report, produce four ChatGPT-side PDFs after reading repo structured data: 每日推薦分析 PDF, 完整候選清單補充 PDF, 權證市場輔助分析 PDF, 市場風險與大盤期權背景 PDF.")
    lines.append("- Do not replace required ChatGPT-generated PDFs with repo PDF links, and do not paste a full chat report instead of required PDFs unless the user explicitly asks for text-only output.")
    lines.append("")

    lines.append("## Read Order")
    lines.extend(
        md_table(
            ["step", "source", "how to use"],
            [
                ["1", "READ_ME_FIRST_DAILY_REPORT.txt", "Confirm date/report_ready and collect raw URLs."],
                ["2", "chatgpt_indicator_usage_guide_latest.md", "Understand which indicator layer is authoritative for each task."],
                ["3", "daily_short_term_specialty_packet_latest.md", "Mandatory for daily stock reports; contains standalone D+5/D+10 short-term specialty sections."],
                ["4", "Task-specific packet/top-list CSV", "Use packet/top-list fields before PDF text."],
                ["5", "PDF / Markdown reports", "Use as readable summaries and presentation artifacts."],
                ["6", "External sources", "Only supplement news/events/targets; never replace repo price or TDCC raw data."],
            ],
        )
    )
    lines.append("")

    lines.append("## Program-Side Classification Coverage")
    coverage_rows = [
        [
            "Daily short-term specialty packet",
            "output/latest/daily_short_term_specialty_packet_latest.md",
            "Usage Contract, TDCC Overheated Short-Term Edge, Weekly Surge Strict Parameter Research, D+5/D+10 tables",
            file_status(short_term_specialty_packet),
            "Mandatory daily-report specialty packet. Read it even when the six fixed categories are already available.",
        ],
        [
            "Daily candidate decision",
            "output/latest/daily_candidate_decision_latest.csv",
            "decision_priority, decision_score, pattern_mapped_category, downgrade_flags, risk_tags, why_selected, why_downgraded, next_confirmation",
            count_values(daily_decision, "decision_priority"),
            "Primary source for daily candidate ranking and downgrade.",
        ],
        [
            "Repeat appearance",
            "output/latest/candidate_repeat_appearance_latest.csv",
            "repeat_appear_label, consecutive_appear_days_any_category, appear_count_5d/10d/20d",
            count_values(repeat, "repeat_appear_label"),
            "Use as persistence/staleness signal, never as a standalone upgrade.",
        ],
        [
            "TDCC strength",
            "output/latest/tdcc_strength_ranking_top_latest.csv",
            "tdcc_strength_score, tdcc_price_phase, risk_bucket, theme_mainstream_status",
            count_values(tdcc_strength, "risk_bucket"),
            "Strength list only. It is not the pre-move list.",
        ],
        [
            "TDCC pre-move / ABM",
            "output/latest/tdcc_pre_move_abm_top_latest.csv",
            "tracking_priority, accumulation_label, tdcc_price_phase, setup_type, trigger_to_watch",
            count_values(tdcc_abm, "tracking_priority"),
            "Use for hidden accumulation candidates, subject to mature-sample caveats.",
        ],
        [
            "TDCC risk list",
            "output/latest/tdcc_top_risk_list_latest.csv",
            "risk_group, tdcc_price_phase, risk_bucket",
            count_values(tdcc_risk, "risk_bucket"),
            "Use to avoid mislabeling late/overheated/divergent names as accumulation.",
        ],
        [
            "TDCC overheated short-term edge",
            "output/latest/tdcc_overheated_short_term_edge_latest.csv",
            "horizon, mature_count, win_rate_close_to_close_pct, avg_relative_return_vs_benchmark_pct, win_rate_next_open_to_close_pct, avg_next_open_relative_return_vs_benchmark_pct",
            f"stats_rows={len(tdcc_overheated_edge)} / current_candidates={len(tdcc_overheated_edge_candidates)}",
            "Standalone D+5/D+10 reporting-only specialty. Do not mix into the six-category ranking or core weights.",
        ],
        [
            "Non-revenue momentum watch",
            "output/latest/non_revenue_momentum_watch_latest.csv",
            "non_revenue_momentum_type, revenue_confirmation_status, theme_final_status, theme_volume_attack_status, volume_breakout_type, next_confirmation",
            f"rows={len(non_revenue_momentum)} / {count_values(non_revenue_momentum, 'non_revenue_momentum_type')}",
            "Specialty overlay for stocks moving on price/theme/fund flow before revenue/EPS confirmation. It is not a seventh core category.",
        ],
        [
            "Warrant flow",
            "output/latest/warrant_flow_by_stock_latest.csv",
            "warrant_flow_signal, warrant_flow_score, warrant_flow_warning",
            count_values(warrant, "warrant_flow_signal"),
            "Auxiliary only. Do not make warrant-only conclusions.",
        ],
        [
            "Market regime / futures options",
            "output/latest/market_regime_latest.csv",
            "market_regime, risk_level, vix_state, put_call_state, foreign_futures_state, retail_mtx_state",
            f"{count_values(market, 'market_regime')} / {count_values(market, 'risk_level')}",
            "Background for exposure, index futures, and chasing-risk interpretation.",
        ],
        [
            "Market timing backtest",
            "output/latest/market_timing_backtest_latest.csv",
            "event_name, sample_status, best_horizon, mature counts",
            count_values(market_timing, "sample_status", limit=5),
            "Use only mature_dN samples. If sample_status is insufficient, say it is observation only.",
        ],
        [
            "Surge precondition model",
            "output/latest/surge_precondition_candidates_latest.csv",
            "surge_precondition_score, surge_watch_label, reason_summary, risk_flags",
            count_values(surge, "surge_watch_label"),
            "Independent research layer; not the daily recommendation model.",
        ],
        [
            "Signal performance",
            "output/latest/daily_signal_performance_summary_latest.csv",
            "category/TDCC/warrant/sector/revenue/catalyst groups with D+N and relative benchmark returns",
            count_values(performance, "category"),
            "Use for review/backtest, not for one-day parameter changes.",
        ],
        [
            "Volume breakout watch",
            "output/latest/volume_breakout_watch_latest.csv",
            "volume_breakout_type, volume_watch_scope, volume_breakout_priority, selection_status, not_selected_reason, risk_flags, next_volume_breakout_confirmation",
            f"{count_values(volume_breakout, 'volume_breakout_priority')} / {count_values(volume_breakout, 'volume_breakout_type')}",
            "Use when asked about 帶量突破 / 放量突破 / 放量攻擊. Strict breakout is only one subset.",
        ],
        [
            "Volume attack theme layer",
            "output/latest/volume_attack_theme_layer_latest.csv",
            "theme_final_status, theme_volume_attack_status, leader_stock, range/strict/watch counts, interpretation",
            f"{count_values(volume_attack_theme, 'theme_volume_attack_status')} / stocks={len(volume_attack_stocks)}",
            "Authoritative mainstream/non-mainstream split for volume-attack sections. Do not show only the theme name.",
        ],
        [
            "Daily theme status history",
            "output/history/daily_signals/daily_theme_status_history.csv",
            "signal_date, stock_id, theme_final_status, theme_status_group, theme_volume_attack_status, candidate_source_type",
            f"{count_values(daily_theme_status_history, 'theme_status_group')} / rows={len(daily_theme_status_history)}",
            "Use for no-lookahead mainstream/non-mainstream backtests; do not use today's theme label for older signal dates.",
        ],
        [
            "Weekly surge theme segment research",
            "output/latest/weekly_surge_theme_segment_next_open_latest.csv",
            "label_type, target_window, theme_status_group, filter_metric, threshold, hit_rate_pct, sample_status",
            f"{count_values(weekly_surge_theme_segment, 'sample_status')} / rows={len(weekly_surge_theme_segment)}",
            "Research only. `provisional_latest_label_only` is exploratory; require strict history before treating as verified.",
        ],
        [
            "Weekly surge technical filter grid",
            "output/latest/weekly_surge_technical_filter_grid_latest.csv",
            "rule_family, rule_name, target_window, hit_rate_pct, median_next_open_to_high_return_pct, sample_status",
            f"{count_values(weekly_surge_technical_grid, 'sample_status')} / rows={len(weekly_surge_technical_grid)}",
            "Parameter discovery only. Use to discuss candidate filters; do not change core weights until strict-history validation matures.",
        ],
        [
            "Weekly surge multifactor filter grid",
            "output/latest/weekly_surge_multifactor_filter_grid_latest.csv",
            "rule_family, rule_name, source_type, target_window, hit_rate_pct, tdcc_available_rate_pct, sample_status",
            f"{count_values(weekly_surge_multifactor_grid, 'sample_status')} / rows={len(weekly_surge_multifactor_grid)}",
            "Parameter discovery across volume, technicals, TDCC as-of data, and market regime. Small-sample high-hit rows are watchlist hypotheses only.",
        ],
        [
            "Weekly surge multifactor current candidates",
            "output/latest/weekly_surge_multifactor_candidates_latest.csv",
            "research_priority, stock_id, matched_rules, best_d5_hit_rate_pct, best_d10_hit_rate_pct, research_caveat",
            f"{count_values(weekly_surge_multifactor_candidates, 'research_priority')} / rows={len(weekly_surge_multifactor_candidates)}",
            "Current research watchlist for the weekly-surge hypotheses. Use as a separate research section only; do not mix into core candidate ranking.",
        ],
        [
            "Weekly surge strict parameter search",
            "output/latest/weekly_surge_strict_parameter_search_latest.csv",
            "rule_name, target_window, entry_basis, target_return_pct, selected_stock_days, hit_rate_pct, median_next_open_to_high_return_pct, sample_status",
            f"{count_values(weekly_surge_strict_search, 'sample_status')} / rows={len(weekly_surge_strict_search)}",
            "No latest-theme labels are used. Entry is D+1 open; hit means next-open to D+N high reaches +10%. Research only.",
        ],
        [
            "Weekly surge strict parameter current candidates",
            "output/latest/weekly_surge_strict_parameter_candidates_latest.csv",
            "research_priority, stock_id, matched_rules, best_d5_hit_rate_pct, best_d10_hit_rate_pct, best_d10_rule, research_caveat",
            f"{count_values(weekly_surge_strict_candidates, 'research_priority')} / rows={len(weekly_surge_strict_candidates)}",
            "Current strict research watchlist using no latest-theme label. Keep as a standalone D+5/D+10 research table, not core ranking.",
        ],
        [
            "Individual stock raw availability",
            "output/latest/individual_stock_available_raw_data_index_slim.csv",
            "data_quality_status, report_status, price/TDCC row counts",
            count_values(individual_index, "data_quality_status"),
            "Check before single-stock analysis.",
        ],
        [
            "Catalyst layer",
            "output/latest/fundamental_catalyst_layer_latest.md",
            "catalyst_quality, catalyst_tags, price_reaction_level, needs_eps_confirmation",
            f"needs_review_rows={len(catalyst_needs_review)}",
            "Currently source-limited; do not upgrade without confirmed source rows.",
        ],
        [
            "Chip-flow positive streak",
            "output/latest/chip_flow_positive_streak_latest.csv",
            "positive_streak_days and category if source data exists",
            f"rows={len(chip)}",
            "If empty/unavailable, do not mention as active signal.",
        ],
    ]
    lines.extend(md_table(["layer", "file", "classification fields", "current buckets", "ChatGPT use"], coverage_rows))
    lines.append("")

    lines.append("## Task-Specific Rules")
    lines.append("")
    lines.append("### Daily candidate report")
    lines.append("- Start from `daily_candidate_decision_chatgpt_packet_latest.md` or `daily_candidate_decision_latest.csv`.")
    lines.append("- Also read `daily_short_term_specialty_packet_latest.md`; it is the mandatory source for standalone D+5/D+10 short-term specialty sections.")
    lines.append("- Use `decision_priority` as the primary reporting priority: `A_priority_watch`, `B_confirm_needed`, `C_watch_only`, `D_risk_downgrade`.")
    lines.append("- Use `why_selected`, `why_downgraded`, and `next_confirmation` directly. Do not invent a different reason when these fields exist.")
    lines.append("- `must_not_overstate=True` means do not call the stock a top pick, even if the chart looks attractive.")
    lines.append("- For volume breakout questions, read `volume_breakout_chatgpt_packet_latest.md`, `volume_attack_theme_layer_latest.md/csv`, `volume_attack_theme_stocks_latest.md/csv`, and then `volume_breakout_watch_latest.csv` for detail fields.")
    lines.append("- Every volume-attack / early-theme table must include explicit `theme_final_status`, `theme_structural_status`, `theme_mainstream_label`, and `theme_volume_attack_status`; never show only a generic theme name.")
    lines.append("- `theme_final_status` is daily flow/breadth. `theme_structural_status=core_mainstream_theme` is required before a stock can enter the mainstream capital line.")
    lines.append("- Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are non-mainstream rotation even when daily flow is strong.")
    lines.append("- For any mainstream/non-mainstream backtest, use `daily_theme_status_history.csv` by `signal_date + stock_id`. Do not join today's `theme_final_status` backward onto historical signals.")
    lines.append("- `theme_volume_attack_status=confirmed_volume_theme` or `early_mainstream_candidate` can be shown in the volume-attack theme line; `single_stock_volume_attack`, `non_mainstream_volume_watch`, `weak_or_non_mainstream_volume_watch`, `overheated_volume_theme`, and `failed_volume_theme` must not be mixed into the mainstream-funding front section.")
    lines.append("- If `tdcc_overheated_short_term_edge_latest.md/csv` exists, include its standalone D+5 and D+10 tables as a TDCC overheated short-term edge specialty; use it for reporting priority only, not core model weights.")
    lines.append("- If `non_revenue_momentum_watch_latest.md/csv` exists, include a standalone `非營收驅動強勢股 / 題材資金先行` section. Do not merge it into the six fixed categories.")
    lines.append("- Do not confuse the fixed category `回檔後短線轉強` with the short-term specialty layer; they are different sections.")
    lines.append("")

    lines.append("### TDCC / ABM report")
    lines.append("- Use `tdcc_chatgpt_tracking_packet_latest.md`, then `tdcc_strength_ranking_top_latest.csv`, `tdcc_pre_move_abm_top_latest.csv`, and `tdcc_top_risk_list_latest.csv`.")
    lines.append("- Strength ranking and pre-move ranking are separate. `strong_but_late`, `strong_but_overheated`, and `strong_but_divergent` are risk groups.")
    lines.append("- `A_prime_watch` is only a tracking priority. It is not a buy instruction.")
    lines.append("- Check mature sample counts before drawing performance conclusions.")
    lines.append("- For overheated TDCC short-term setups, use `tdcc_overheated_short_term_edge_latest.md/csv` and the candidates CSV. The close-to-close and next-open metrics must remain separate.")
    lines.append("")

    lines.append("### Market / index timing report")
    lines.append("- Use `market_timing_chatgpt_packet_latest.md`, `market_regime_latest.csv`, and market timing backtest files.")
    lines.append("- If `sample_status` is `insufficient_sample` or `pending_only`, say it is a hypothesis/observation, not a proven timing signal.")
    lines.append("- Use `market_regime` and `risk_level` to adjust how aggressively daily candidates should be discussed.")
    lines.append("")

    lines.append("### Warrant report")
    lines.append("- Use `warrant_flow_by_stock_latest.csv` and `warrant_market_report_latest.md`.")
    lines.append("- Warrant signals are auxiliary: `call_inflow`, `call_strong_inflow`, `call_put_bullish`, `mixed_flow`, `no_signal`.")
    lines.append("- If turnover is not ready, only discuss coverage/direction structure, not money-flow heat.")
    lines.append("")

    lines.append("### Catalyst / event report")
    lines.append("- Use `fundamental_catalyst_layer_latest.md`, `catalyst_needs_review_latest.csv`, and event calendar files.")
    lines.append("- `needs_eps_confirmation` means do not upgrade to a confirmed catalyst.")
    lines.append("- Company/theme mapping alone is background, not a confirmed event catalyst.")
    lines.append("")

    lines.append("### Single stock analysis")
    lines.append("- First check `individual_stock_available_raw_data_index_slim.csv` and the stock-specific packet if available.")
    lines.append("- Price history must come from `data/stock_price_history/{stock_id}.csv` or the stock packet; TDCC must come from `data/tdcc_stock_history/{stock_id}.csv` or the stock packet.")
    lines.append("- If price raw data is unavailable, do not produce a standard raw-data technical report.")
    lines.append("- If TDCC history is under 8 weeks, mark `insufficient_tdcc_history` and do not force a full TDCC backtest conclusion.")
    lines.append("")

    lines.append("## Conflict Handling")
    lines.append("- Program-side classifications win over ChatGPT memory.")
    lines.append("- Latest `main_price_date` wins over old report memory.")
    lines.append("- Raw structured files and packets win over PDF prose.")
    lines.append("- Validation/status fields win over optimistic wording.")
    lines.append("- Empty or unavailable source tables must be disclosed and ignored for ranking.")
    lines.append("")

    lines.append("## Current Data Quality Snapshot")
    quality_rows = [
        ["daily_candidate_decision_latest.csv", file_status(LATEST_DIR / "daily_candidate_decision_latest.csv"), str(len(daily_decision))],
        ["tdcc_chatgpt_tracking_packet_latest.md", file_status(LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"), "-"],
        ["market_timing_chatgpt_packet_latest.md", file_status(LATEST_DIR / "market_timing_chatgpt_packet_latest.md"), "-"],
        ["surge_model_chatgpt_packet_latest.md", file_status(LATEST_DIR / "surge_model_chatgpt_packet_latest.md"), "-"],
        ["warrant_flow_by_stock_latest.csv", file_status(LATEST_DIR / "warrant_flow_by_stock_latest.csv"), str(len(warrant))],
        ["chip_flow_positive_streak_latest.csv", file_status(LATEST_DIR / "chip_flow_positive_streak_latest.csv"), str(len(chip))],
        ["catalyst_needs_review_latest.csv", file_status(LATEST_DIR / "catalyst_needs_review_latest.csv"), str(len(catalyst_needs_review))],
    ]
    lines.extend(md_table(["file", "status", "rows"], quality_rows))
    lines.append("")

    lines.append("## Copy-Paste Summary For ChatGPT")
    lines.append("Use program-side indicator classifications first. Start from READ_ME_FIRST, then this indicator usage guide, then the task-specific packet/top-list. Do not re-rank from memory. For daily candidates, use `decision_priority`, `decision_score`, `why_selected`, `why_downgraded`, and `next_confirmation`. For TDCC, keep Strength Ranking separate from ABM Pre-Move Ranking and respect risk buckets. For market timing, use sample_status and mature counts before making any timing statement. For single stocks, verify raw price/TDCC availability before producing a standard raw-data report.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    text = build_guide()
    for path in [OUT_MD, OUT_TXT, DOCS_MD, DOCS_TXT]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"Saved: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
