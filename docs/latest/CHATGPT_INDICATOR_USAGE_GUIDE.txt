# ChatGPT Indicator Usage Guide

- generated_at: `2026-05-28 14:56:24 台北標準時間`
- main_price_date: `20260527`
- purpose: Use program-side classifications first. ChatGPT should explain and synthesize, not re-rank from memory.
- rule: If memory, PDF, or ad-hoc interpretation conflicts with program-side fields, use the structured program-side fields.

## Delivery Contract

- Repo pipeline PDFs / Markdown / packets are source artifacts, validation artifacts, or shareable reference outputs.
- `report_ready=True` means repo data and artifacts are available; it does not mean ChatGPT has completed the requested report.
- `fixed_pdf_validation_status=pass` means repo PDF artifacts passed validation; it is not the same as a newly generated ChatGPT deliverable PDF.
- If the user asks only for pipeline/repo status, report artifact status and links.
- If the user asks to do today's report, produce four ChatGPT-side PDFs after reading repo structured data: 每日推薦分析 PDF, 完整候選清單補充 PDF, 權證市場輔助分析 PDF, 市場風險與大盤期權背景 PDF.
- Do not replace required ChatGPT-generated PDFs with repo PDF links, and do not paste a full chat report instead of required PDFs unless the user explicitly asks for text-only output.

## Read Order
| step | source | how to use |
| --- | --- | --- |
| 1 | READ_ME_FIRST_DAILY_REPORT.txt | Confirm date/report_ready and collect raw URLs. |
| 2 | chatgpt_indicator_usage_guide_latest.md | Understand which indicator layer is authoritative for each task. |
| 3 | daily_short_term_specialty_packet_latest.md | Mandatory for daily stock reports; contains standalone D+5/D+10 short-term specialty sections. |
| 4 | Task-specific packet/top-list CSV | Use packet/top-list fields before PDF text. |
| 5 | PDF / Markdown reports | Use as readable summaries and presentation artifacts. |
| 6 | External sources | Only supplement news/events/targets; never replace repo price or TDCC raw data. |

## Program-Side Classification Coverage
| layer | file | classification fields | current buckets | ChatGPT use |
| --- | --- | --- | --- | --- |
| Daily short-term specialty packet | output/latest/daily_short_term_specialty_packet_latest.md | Usage Contract, TDCC Overheated Short-Term Edge, Weekly Surge Strict Parameter Research, D+5/D+10 tables | ready | Mandatory daily-report specialty packet. Read it even when the six fixed categories are already available. |
| Daily candidate decision | output/latest/daily_candidate_decision_latest.csv | decision_priority, decision_score, pattern_mapped_category, downgrade_flags, risk_tags, why_selected, why_downgraded, next_confirmation | D_risk_downgrade=342; C_watch_only=240; B_confirm_needed=43; A_priority_watch=25 | Primary source for daily candidate ranking and downgrade. |
| Repeat appearance | output/latest/candidate_repeat_appearance_latest.csv | repeat_appear_label, consecutive_appear_days_any_category, appear_count_5d/10d/20d | stale_signal=182; repeated_but_no_breakout=122; continued_2_3d=64; continued_overheated=52; first_seen=21; continued_many_days=14 | Use as persistence/staleness signal, never as a standalone upgrade. |
| TDCC strength | output/latest/tdcc_strength_ranking_top_latest.csv | tdcc_strength_score, tdcc_price_phase, risk_bucket, theme_mainstream_status | strong_but_pre_move=23; strong_but_divergent=23; insufficient_data=2; strong_but_late=1; strong_but_overheated=1 | Strength list only. It is not the pre-move list. |
| TDCC pre-move / ABM | output/latest/tdcc_pre_move_abm_top_latest.csv | tracking_priority, accumulation_label, tdcc_price_phase, setup_type, trigger_to_watch | C_weak_or_discounted=23; B_confirm_needed=22; A_prime_watch=5 | Use for hidden accumulation candidates, subject to mature-sample caveats. |
| TDCC risk list | output/latest/tdcc_top_risk_list_latest.csv | risk_group, tdcc_price_phase, risk_bucket | strong_but_late=20; strong_but_overheated=20; strong_but_divergent=20 | Use to avoid mislabeling late/overheated/divergent names as accumulation. |
| TDCC overheated short-term edge | output/latest/tdcc_overheated_short_term_edge_latest.csv | horizon, mature_count, win_rate_close_to_close_pct, avg_relative_return_vs_benchmark_pct, win_rate_next_open_to_close_pct, avg_next_open_relative_return_vs_benchmark_pct | stats_rows=6 / current_candidates=75 | Standalone D+5/D+10 reporting-only specialty. Do not mix into the six-category ranking or core weights. |
| Warrant flow | output/latest/warrant_flow_by_stock_latest.csv | warrant_flow_signal, warrant_flow_score, warrant_flow_warning | no_signal=308; call_inflow=62; call_strong_inflow=39; call_put_bullish=29; mixed_flow=10; put_inflow=8 | Auxiliary only. Do not make warrant-only conclusions. |
| Market regime / futures options | output/latest/market_regime_latest.csv | market_regime, risk_level, vix_state, put_call_state, foreign_futures_state, retail_mtx_state | strong_bull=1 / high_risk=1 | Background for exposure, index futures, and chasing-risk interpretation. |
| Market timing backtest | output/latest/market_timing_backtest_latest.csv | event_name, sample_status, best_horizon, mature counts | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample=16; D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok=7; D+1:pending_only;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only=2; D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok=2; D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only=1 | Use only mature_dN samples. If sample_status is insufficient, say it is observation only. |
| Surge precondition model | output/latest/surge_precondition_candidates_latest.csv | surge_precondition_score, surge_watch_label, reason_summary, risk_flags | A_surge_watch=71; B_confirm_needed=26; C_too_hot=3 | Independent research layer; not the daily recommendation model. |
| Signal performance | output/latest/daily_signal_performance_summary_latest.csv | category/TDCC/warrant/sector/revenue/catalyst groups with D+N and relative benchmark returns | pattern=2; pullback_rebound=2; range_rebound=2; revenue_breakout_low_response=2; revenue_pullback=2; true_breakout=2 | Use for review/backtest, not for one-day parameter changes. |
| Volume breakout watch | output/latest/volume_breakout_watch_latest.csv | volume_breakout_type, volume_watch_scope, volume_breakout_priority, selection_status, not_selected_reason, risk_flags, next_volume_breakout_confirmation | D_risk_downgrade=130; B_confirm_needed=33; C_watch_only=23; A_valid_breakout_watch=10 / volume_expansion_watch=62; loose_platform_volume_watch=33; neckline_volume_breakout=27; strict_60d_volume_breakout=25; right_side_volume_attack=17; loose_ma_reclaim_volume_watch=14; platform_volume_breakout=8; abnormal_volume_up=5; loose_right_side_volume_watch=5 | Use when asked about 帶量突破 / 放量突破 / 放量攻擊. Strict breakout is only one subset. |
| Volume attack theme layer | output/latest/volume_attack_theme_layer_latest.csv | theme_final_status, theme_volume_attack_status, leader_stock, range/strict/watch counts, interpretation | overheated_volume_theme=13; watch_volume_theme=8; single_stock_volume_attack=2; confirmed_volume_theme=1; theme_status_missing=1 / stocks=196 | Authoritative mainstream/non-mainstream split for volume-attack sections. Do not show only the theme name. |
| Daily theme status history | output/history/daily_signals/daily_theme_status_history.csv | signal_date, stock_id, theme_final_status, theme_status_group, theme_volume_attack_status, candidate_source_type | mainstream_overheated=240; mainstream_supported=211; non_mainstream=94 / rows=545 | Use for no-lookahead mainstream/non-mainstream backtests; do not use today's theme label for older signal dates. |
| Weekly surge theme segment research | output/latest/weekly_surge_theme_segment_next_open_latest.csv | label_type, target_window, theme_status_group, filter_metric, threshold, hit_rate_pct, sample_status | provisional_latest_label_only=180 / rows=180 | Research only. `provisional_latest_label_only` is exploratory; require strict history before treating as verified. |
| Weekly surge technical filter grid | output/latest/weekly_surge_technical_filter_grid_latest.csv | rule_family, rule_name, target_window, hit_rate_pct, median_next_open_to_high_return_pct, sample_status | provisional_latest_label_only=75; insufficient_sample=6 / rows=81 | Parameter discovery only. Use to discuss candidate filters; do not change core weights until strict-history validation matures. |
| Weekly surge multifactor filter grid | output/latest/weekly_surge_multifactor_filter_grid_latest.csv | rule_family, rule_name, source_type, target_window, hit_rate_pct, tdcc_available_rate_pct, sample_status | insufficient_sample=27; provisional_latest_theme_label=21; ok_initial_sample=15 / rows=63 | Parameter discovery across volume, technicals, TDCC as-of data, and market regime. Small-sample high-hit rows are watchlist hypotheses only. |
| Weekly surge multifactor current candidates | output/latest/weekly_surge_multifactor_candidates_latest.csv | research_priority, stock_id, matched_rules, best_d5_hit_rate_pct, best_d10_hit_rate_pct, research_caveat | D_background_only=90; C_short_term_watch=29; A_research_watch=15; B_research_confirm=8 / rows=142 | Current research watchlist for the weekly-surge hypotheses. Use as a separate research section only; do not mix into core candidate ranking. |
| Weekly surge strict parameter search | output/latest/weekly_surge_strict_parameter_search_latest.csv | rule_name, target_window, entry_basis, target_return_pct, selected_stock_days, hit_rate_pct, median_next_open_to_high_return_pct, sample_status | ok_initial_sample=5355; insufficient_sample=1644 / rows=6999 | No latest-theme labels are used. Entry is D+1 open; hit means next-open to D+N high reaches +10%. Research only. |
| Weekly surge strict parameter current candidates | output/latest/weekly_surge_strict_parameter_candidates_latest.csv | research_priority, stock_id, matched_rules, best_d5_hit_rate_pct, best_d10_hit_rate_pct, best_d10_rule, research_caveat | B_strict_research_confirm=88; A_strict_research_watch=13; D_background_only=7; C_strict_short_term_watch=2 / rows=110 | Current strict research watchlist using no latest-theme label. Keep as a standalone D+5/D+10 research table, not core ranking. |
| Individual stock raw availability | output/latest/individual_stock_available_raw_data_index_slim.csv | data_quality_status, report_status, price/TDCC row counts | partial=2044; ok=81; insufficient_data=25 | Check before single-stock analysis. |
| Catalyst layer | output/latest/fundamental_catalyst_layer_latest.md | catalyst_quality, catalyst_tags, price_reaction_level, needs_eps_confirmation | needs_review_rows=4 | Currently source-limited; do not upgrade without confirmed source rows. |
| Chip-flow positive streak | output/latest/chip_flow_positive_streak_latest.csv | positive_streak_days and category if source data exists | rows=0 | If empty/unavailable, do not mention as active signal. |

## Task-Specific Rules

### Daily candidate report
- Start from `daily_candidate_decision_chatgpt_packet_latest.md` or `daily_candidate_decision_latest.csv`.
- Also read `daily_short_term_specialty_packet_latest.md`; it is the mandatory source for standalone D+5/D+10 short-term specialty sections.
- Use `decision_priority` as the primary reporting priority: `A_priority_watch`, `B_confirm_needed`, `C_watch_only`, `D_risk_downgrade`.
- Use `why_selected`, `why_downgraded`, and `next_confirmation` directly. Do not invent a different reason when these fields exist.
- `must_not_overstate=True` means do not call the stock a top pick, even if the chart looks attractive.
- For volume breakout questions, read `volume_breakout_chatgpt_packet_latest.md`, `volume_attack_theme_layer_latest.md/csv`, `volume_attack_theme_stocks_latest.md/csv`, and then `volume_breakout_watch_latest.csv` for detail fields.
- Every volume-attack / early-theme table must include explicit `theme_final_status` and `theme_volume_attack_status`; never show only a generic theme name.
- For any mainstream/non-mainstream backtest, use `daily_theme_status_history.csv` by `signal_date + stock_id`. Do not join today's `theme_final_status` backward onto historical signals.
- `theme_volume_attack_status=confirmed_volume_theme` or `early_mainstream_candidate` can be shown in the volume-attack theme line; `single_stock_volume_attack`, `non_mainstream_volume_watch`, `weak_or_non_mainstream_volume_watch`, `overheated_volume_theme`, and `failed_volume_theme` must not be mixed into the mainstream-funding front section.
- If `tdcc_overheated_short_term_edge_latest.md/csv` exists, include its standalone D+5 and D+10 tables as a TDCC overheated short-term edge specialty; use it for reporting priority only, not core model weights.
- Do not confuse the fixed category `回檔後短線轉強` with the short-term specialty layer; they are different sections.

### TDCC / ABM report
- Use `tdcc_chatgpt_tracking_packet_latest.md`, then `tdcc_strength_ranking_top_latest.csv`, `tdcc_pre_move_abm_top_latest.csv`, and `tdcc_top_risk_list_latest.csv`.
- Strength ranking and pre-move ranking are separate. `strong_but_late`, `strong_but_overheated`, and `strong_but_divergent` are risk groups.
- `A_prime_watch` is only a tracking priority. It is not a buy instruction.
- Check mature sample counts before drawing performance conclusions.
- For overheated TDCC short-term setups, use `tdcc_overheated_short_term_edge_latest.md/csv` and the candidates CSV. The close-to-close and next-open metrics must remain separate.

### Market / index timing report
- Use `market_timing_chatgpt_packet_latest.md`, `market_regime_latest.csv`, and market timing backtest files.
- If `sample_status` is `insufficient_sample` or `pending_only`, say it is a hypothesis/observation, not a proven timing signal.
- Use `market_regime` and `risk_level` to adjust how aggressively daily candidates should be discussed.

### Warrant report
- Use `warrant_flow_by_stock_latest.csv` and `warrant_market_report_latest.md`.
- Warrant signals are auxiliary: `call_inflow`, `call_strong_inflow`, `call_put_bullish`, `mixed_flow`, `no_signal`.
- If turnover is not ready, only discuss coverage/direction structure, not money-flow heat.

### Catalyst / event report
- Use `fundamental_catalyst_layer_latest.md`, `catalyst_needs_review_latest.csv`, and event calendar files.
- `needs_eps_confirmation` means do not upgrade to a confirmed catalyst.
- Company/theme mapping alone is background, not a confirmed event catalyst.

### Single stock analysis
- First check `individual_stock_available_raw_data_index_slim.csv` and the stock-specific packet if available.
- Price history must come from `data/stock_price_history/{stock_id}.csv` or the stock packet; TDCC must come from `data/tdcc_stock_history/{stock_id}.csv` or the stock packet.
- If price raw data is unavailable, do not produce a standard raw-data technical report.
- If TDCC history is under 8 weeks, mark `insufficient_tdcc_history` and do not force a full TDCC backtest conclusion.

## Conflict Handling
- Program-side classifications win over ChatGPT memory.
- Latest `main_price_date` wins over old report memory.
- Raw structured files and packets win over PDF prose.
- Validation/status fields win over optimistic wording.
- Empty or unavailable source tables must be disclosed and ignored for ranking.

## Current Data Quality Snapshot
| file | status | rows |
| --- | --- | --- |
| daily_candidate_decision_latest.csv | ready | 650 |
| tdcc_chatgpt_tracking_packet_latest.md | ready | - |
| market_timing_chatgpt_packet_latest.md | ready | - |
| surge_model_chatgpt_packet_latest.md | ready | - |
| warrant_flow_by_stock_latest.csv | ready | 456 |
| chip_flow_positive_streak_latest.csv | exists_but_unreadable_or_empty | 0 |
| catalyst_needs_review_latest.csv | ready | 4 |

## Copy-Paste Summary For ChatGPT
Use program-side indicator classifications first. Start from READ_ME_FIRST, then this indicator usage guide, then the task-specific packet/top-list. Do not re-rank from memory. For daily candidates, use `decision_priority`, `decision_score`, `why_selected`, `why_downgraded`, and `next_confirmation`. For TDCC, keep Strength Ranking separate from ABM Pre-Move Ranking and respect risk buckets. For market timing, use sample_status and mature counts before making any timing statement. For single stocks, verify raw price/TDCC availability before producing a standard raw-data report.

