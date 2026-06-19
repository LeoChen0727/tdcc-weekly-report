# ChatGPT Indicator Usage Guide

- generated_at: `2026-06-19 17:33:27 UTC`
- main_price_date: `20260618`
- purpose: Use program-side classifications first. ChatGPT should explain and synthesize, not re-rank from memory.
- rule: If memory, PDF, or ad-hoc interpretation conflicts with program-side fields, use the structured program-side fields.

## Delivery Contract

- Repo pipeline PDFs / Markdown / packets are source artifacts, validation artifacts, or shareable reference outputs.
- `report_ready=True` means repo data and artifacts are available; it does not mean ChatGPT has completed the requested report.
- Repo artifact PDF links are not ChatGPT-side deliverable PDFs. Do not present repo artifact PDFs as completed daily recommendation reports.
- If the user asks only for pipeline/repo status, report artifact status and links.
- If the user asks to do today's report, produce six ChatGPT-side PDFs after reading repo structured data: 主流每日推薦精華 PDF, 主流完整候選清單 PDF, 非主流每日推薦精華 PDF, 非主流完整候選清單 PDF, 權證市場輔助分析 PDF, 市場風險與大盤期權背景 PDF.
- Do not replace required ChatGPT-generated PDFs with repo PDF links, and do not paste a full chat report instead of required PDFs unless the user explicitly asks for text-only output.

## Read Order
| step | source | how to use |
| --- | --- | --- |
| 1 | READ_ME_FIRST_DAILY_REPORT.txt | Confirm date/report_ready and collect raw URLs. |
| 2 | chatgpt_indicator_usage_guide_latest.md | Understand which indicator layer is authoritative for each task. |
| 3 | daily_report_model_registry_latest.csv + daily_candidate_model_summary_for_report_latest.csv | Mandatory for daily stock PDF first page; fixed official model rows plus new/repeated first names. Do not hard-code model count in the PDF layer. |
| 4 | daily_candidate_model_layer_packet_latest.md | Mandatory for daily stock reports; lists independent model signals, parameters, and group rotation. Do not hard-code model count. |
| 5 | daily_short_term_specialty_packet_latest.md | Mandatory for daily stock reports; contains standalone D+1-D+10 short-term specialty summary plus D+5/D+10 detail sections. |
| 6 | stock_theme_taxonomy_latest.csv/md + stock_theme_taxonomy_review_latest.csv/md | Use program-side market-theme taxonomy before raw industry; review file marks missing/industry-only mappings that cannot enter mainstream routing. |
| 7 | Task-specific packet/top-list CSV | Use packet/top-list fields before PDF text. |
| 7 | PDF / Markdown reports | Use as readable summaries and presentation artifacts. |
| 8 | External sources | Only supplement news/events/targets; never replace repo price or TDCC raw data. |

## Program-Side Classification Coverage
| layer | file | classification fields | current buckets | ChatGPT use |
| --- | --- | --- | --- | --- |
| Independent daily candidate models | output/latest/daily_candidate_model_layer_packet_latest.md | daily_candidate_model_parameters, daily_report_model_registry, daily_candidate_model_summary_for_report, daily_candidate_model_signals, model_rank, report_bucket, selection_semantics | models=16 / registry=10 / fixed_summary=20 / raw_signals=574 / report_signals=574 / packet=ready | Main condition met means selected into that model. Score/risk ranks inside the model. Use model_signals_for_report for model sections and daily_candidate_model_summary_for_report for fixed first-page new/repeated representatives. |
| Daily candidate fixed model summary | output/latest/daily_candidate_model_summary_for_report_latest.csv | report_line, model_id, model_registry_order, new_stock_display, new_rank_label, repeated_stock_display, repeated_rank_label | rows=20 / mainstream=10; non_mainstream=10 | First-page curated PDF contract. Render every registry model applicable to the report line; show no candidate when no new/repeated stock exists. Do not let models disappear from the first page. |
| Daily candidate front-page unique representatives | output/latest/daily_candidate_frontpage_unique_latest.csv | frontpage_unique_rank, report_bucket, stock_id, primary_model_id, model_hit_count, model_hits | rows=237 / mainstream=162; non_mainstream=75 | Legacy first-page unique table. Prefer daily_candidate_model_summary_for_report_latest.csv for fixed per-model new/repeated summaries. |
| Daily candidate same-model repeat | output/latest/daily_candidate_same_model_repeat_latest.csv | same_model_consecutive_days, same_model_appear_count_5d, same_model_appear_count_10d, same_model_repeat_status | rows=245 / mainstream=151; non_mainstream=94 | Persistence table only. Same-stock same-model repeat is not a score penalty or veto; curated/front-page tables may prefer new_model_signal and list repeated names separately. |
| Group fund rotation | output/latest/daily_candidate_group_rotation_latest.csv | theme, stock_count, volume_expansion_3x_count, volume_expansion_ratio, leader_1/2/3 | rows=10 | Theme-flow section only. It is not an individual stock buy model. |
| Daily model parameter research | output/latest/daily_model_parameter_research_latest.csv | model_id, parameter_set_id, entry_basis, selected_stock_days, best_horizon_by_avg_return, best_d1_to_d10_close_win_rate_pct, sample_status | rows=82 / details=902 / ok_first_pass=82 | Research/backtest layer only. Entry is next trading day open; D+1-D+10 close/high endpoints are in the horizon detail table. Use to tune future parameters, not as PDF-side veto logic. |
| Daily model parameter recommendations | output/latest/daily_model_parameter_recommendations_latest.csv | model_id, parameter_set_id, recommended_usage, recommended_close_exit_horizon, best_close_win_rate_pct, model_revision_note | rows=82 / intraday_target_watch=61; research_only=12; pdf_secondary_watch=5; promote_to_pdf_core=3; score_component_only=1 | Program-side conversion from backtest to reporting usage. Use this for whether a parameter is core, secondary, intraday-target only, or research-only. |
| Daily short-term specialty packet | output/latest/daily_short_term_specialty_packet_latest.md | Usage Contract, TDCC Overheated Short-Term Edge, Next-Open +10pct Touch Strict Parameter Research, D+5/D+10 tables | ready | Mandatory daily-report specialty packet. Read it even when the six fixed categories are already available. |
| Daily candidate model signals for report | output/latest/daily_candidate_model_signals_for_report_latest.csv | model_id, model_name_zh, model_score, model_rank, display_rank, score_components, risk_penalty_tags, risk_tags, next_confirmation | price_pullback_23ema=240; revenue_unreacted_range=125; pullback_short_reclaim=105; hot_theme_pullback=54; volume_range_breakout=22; tdcc_short_term_continuation_d5_d10=18; near_high_neckline_challenge=6; w_bottom_right_side=4 | Primary source for daily PDF/packet model rows, scores, ranks, risks, and next confirmations. |
| Repeat appearance | output/latest/candidate_repeat_appearance_latest.csv | repeat_appear_label, consecutive_appear_days_any_category, appear_count_5d/10d/20d | stale_signal=262; first_seen=143; repeated_but_no_breakout=77; continued_overheated=41; continued_2_3d=17; continued_many_days=7 | Use as persistence/staleness signal, never as a standalone upgrade. |
| TDCC strength | output/latest/tdcc_strength_ranking_top_latest.csv | tdcc_strength_score, tdcc_price_phase, risk_bucket, theme_mainstream_status | insufficient_data=22; strong_but_pre_move=9; strong_but_late=9; strong_but_divergent=6; strong_confirmed=2; strong_but_overheated=2 | Strength list only. It is not the pre-move list. |
| TDCC pre-move / ABM | output/latest/tdcc_pre_move_abm_top_latest.csv | tracking_priority, accumulation_label, tdcc_price_phase, setup_type, trigger_to_watch | C_weak_or_discounted=19; B_confirm_needed=8; A_prime_watch=4 | Use for hidden accumulation candidates, subject to mature-sample caveats. |
| TDCC risk list | output/latest/tdcc_top_risk_list_latest.csv | risk_group, tdcc_price_phase, risk_bucket | strong_but_late=20; strong_but_overheated=20; strong_but_divergent=20 | Use to avoid mislabeling late/overheated/divergent names as accumulation. |
| TDCC overheated short-term edge | output/latest/tdcc_overheated_short_term_edge_latest.csv | horizon, mature_count, win_rate_close_to_close_pct, avg_relative_return_vs_benchmark_pct, win_rate_next_open_to_close_pct, avg_next_open_relative_return_vs_benchmark_pct | stats_rows=6 / current_candidates=25 | Core D+5/D+10 continuation model when active in the program-side registry. Separate research-stat tables are supporting evidence and must not override model ranking. |
| Non-revenue momentum watch | output/latest/non_revenue_momentum_watch_latest.csv | non_revenue_momentum_type, revenue_confirmation_status, theme_final_status, theme_volume_attack_status, volume_breakout_type, next_confirmation | rows=88 / D_overheated_or_failed_risk=70; C_hot_money_watch=14; A_fund_flow_confirmed_revenue_unconfirmed=4 | Specialty overlay for stocks moving on price/theme/fund flow before revenue/EPS confirmation. It is not a seventh core category. |
| MSCI Taiwan rebalance event tag | output/latest/msci_taiwan_rebalance_backtest_latest.csv | msci_index_segment, action, effective_date, entry_date, ret_d5_return, ret_d10_return, ret_d15_return, ret_d20_return, sample_status | addition=59; deletion=59 / ok=70; pending_no_next_trade=34; price_history_starts_after_event=14 | Event tag and research layer only. Entry is first trading day after effective date open; exits are D+5/D+10/D+15/D+20 close. Do not treat MSCI addition/deletion as a standalone buy/sell signal. |
| Warrant flow | output/latest/warrant_flow_by_stock_latest.csv | warrant_flow_signal, warrant_flow_score, warrant_flow_warning | 無明確權證訊號=303; 認購流入=87; 認購強流入=33; 認購/認售結構偏多=24; 多空混合=3; 認售流入=1 | Auxiliary only. Do not make warrant-only conclusions. |
| Market regime / futures options | output/latest/market_regime_latest.csv | market_regime, risk_level, vix_state, put_call_state, foreign_futures_state, retail_mtx_state | strong_bull=1 / elevated_risk=1 | Background for exposure, index futures, and chasing-risk interpretation. |
| Market timing backtest | output/latest/market_timing_backtest_latest.csv | event_name, sample_status, best_horizon, mature counts | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample=16; D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok=7; D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok=2; D+1:insufficient_sample;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only=1; D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:insufficient_sample=1 | Use only mature_dN samples. If sample_status is insufficient, say it is observation only. |
| Surge precondition model | output/latest/surge_precondition_candidates_latest.csv | surge_precondition_score, surge_watch_label, reason_summary, risk_flags | A_surge_watch=100 | Independent research layer; not the daily recommendation model. |
| Signal performance | output/latest/daily_signal_performance_summary_latest.csv | category/TDCC/warrant/sector/revenue/catalyst groups with D+N and relative benchmark returns | 回檔後短線轉強=3; 營收爆發但股價尚未反應=3; pattern=3; 營收成長股價回檔=3; 嚴格突破=3; 區間內轉強 / 挑戰前高觀察=3 | Use for review/backtest, not for one-day parameter changes. |
| Volume breakout watch | output/latest/volume_breakout_watch_latest.csv | volume_breakout_type, volume_watch_scope, volume_breakout_priority, selection_status, not_selected_reason, risk_flags, next_volume_breakout_confirmation | A_bottom_volume_attack=22 / bottom_volume_attack=22 | Use when asked about 放量攻擊 / 放量突破. The core condition is prior-20-day-high breakout with large volume; strict 60-day breakout is a separate concept. |
| Stock theme taxonomy | output/latest/stock_theme_taxonomy_latest.csv | primary_theme, secondary_themes, structural_theme_bucket, theme_structural_status, theme_mainstream_label, concept_tags | rows=2372 / non_mainstream_theme=896; semiconductor_general_theme=185; electronic_component_general_theme=166; optoelectronics_general_theme=110; robotics_precision_motion_theme=92; computer_peripheral_general_theme=91; other_electronics_general_theme=84; networking_general_theme=75; information_service_general_theme=45; digital_cloud_general_theme=39; electronics_channel_general_theme=35; power_grid_theme=22 | Authoritative program-side theme/concept mapping. Use before raw industry; e.g. robotics, low-earth-orbit satellite, glass fiber/CCL can cross exchange industries. |
| Stock theme taxonomy review | output/latest/stock_theme_taxonomy_review_latest.csv | taxonomy_review_status, review_priority, effective_primary_theme, effective_structural_theme_bucket | Use this to find stocks with signals but missing market-theme mapping. | Rows marked industry_core_needs_market_theme are not eligible for the mainstream attack list until mapped to an explicit core structural_theme_bucket. |
| Volume attack theme layer | output/latest/volume_attack_theme_layer_latest.csv | market_theme_group, theme_group_source, structural_theme_bucket, theme_final_status, theme_volume_attack_status, theme_spread_decision, leader_stock_id, second_stock_id, third_stock_id, range/strict/watch counts, interpretation | overheated_volume_theme=8; single_stock_volume_attack=1; non_mainstream_volume_watch=1 / stocks=22 | Authoritative volume-attack theme spread table. Leader/second/third are program fields; do not invent runner-up stocks from memory. |
| Daily theme status history | output/history/daily_signals/daily_theme_status_history.csv | signal_date, stock_id, theme_final_status, theme_status_group, theme_volume_attack_status, candidate_source_type | mainstream_overheated=431; mainstream_supported=112; non_mainstream=5 / rows=548 | Use for no-lookahead mainstream/non-mainstream backtests; do not use today's theme label for older signal dates. |
| Five-day 20pct high-low event theme segment research | output/latest/weekly_surge_theme_segment_next_open_latest.csv | label_type, target_window, theme_status_group, filter_metric, threshold, hit_rate_pct, sample_status | provisional_latest_label_only=638; ok=407; insufficient_history=88; insufficient_sample=22 / rows=1155 | Research only. The legacy file prefix `weekly_surge` means rolling five-trading-day high-low event research, not weekly candlesticks. `provisional_latest_label_only` is exploratory; require strict history before treating as verified. |
| Next-open +10pct technical filter grid | output/latest/weekly_surge_technical_filter_grid_latest.csv | rule_family, rule_name, target_window, hit_rate_pct, median_next_open_to_high_return_pct, sample_status | provisional_latest_label_only=286; insufficient_sample=11 / rows=297 | Parameter discovery only. Entry is D+1 open and hit means D+1 open to D+N high touches +10%; do not change core weights until strict-history validation matures. |
| Next-open +10pct multifactor filter grid | output/latest/weekly_surge_multifactor_filter_grid_latest.csv | rule_family, rule_name, source_type, target_window, hit_rate_pct, tdcc_available_rate_pct, sample_status | provisional_latest_theme_label=143; ok_initial_sample=55; insufficient_sample=33 / rows=231 | Parameter discovery across volume, technicals, TDCC as-of data, and market regime. Entry is D+1 open; small-sample high-touch rows are watchlist hypotheses only. |
| Next-open +10pct multifactor current candidates | output/latest/weekly_surge_multifactor_candidates_latest.csv | research_priority, stock_id, matched_rules, best_d5_touch_rate_pct, best_d10_touch_rate_pct, research_caveat | D_background_only=91; A_research_watch=30; C_short_term_watch=25; B_research_confirm=21 / rows=167 | Current research watchlist for next-open +10pct touch hypotheses. Use as a separate research section only; do not mix into core candidate ranking. |
| Next-open +10pct strict parameter search | output/latest/weekly_surge_strict_parameter_search_latest.csv | rule_name, target_window, entry_basis, target_return_pct, selected_stock_days, hit_rate_pct, median_next_open_to_high_return_pct, sample_status | ok_initial_sample=21285; insufficient_sample=5654 / rows=26939 | No latest-theme labels are used. Entry is D+1 open; hit means next-open to D+N high touches +10%. This is not weekly candlestick analysis. Research only. |
| Next-open +10pct strict parameter current candidates | output/latest/weekly_surge_strict_parameter_candidates_latest.csv | research_priority, stock_id, matched_rules, best_d5_touch_rate_pct, best_d10_touch_rate_pct, best_d10_rule, research_caveat | B_strict_research_confirm=43; A_strict_research_watch=23; D_background_only=13; C_strict_short_term_watch=11 / rows=90 | Current strict research watchlist using no latest-theme label. Keep as a standalone D+5/D+10 research table, not core ranking. |
| Individual stock raw availability | output/latest/individual_stock_available_raw_data_index_slim.csv | data_quality_status, report_status, price/TDCC row counts | partial=2290; ok=83; insufficient_data=24 | Check before single-stock analysis. |
| Catalyst layer | output/latest/fundamental_catalyst_layer_latest.md | catalyst_quality, catalyst_tags, price_reaction_level, needs_eps_confirmation | needs_review_rows=2 | Currently source-limited; do not upgrade without confirmed source rows. |

## Task-Specific Rules

### Daily candidate report
- Start from `daily_candidate_model_layer_packet_latest.md`, `daily_candidate_model_parameters_latest.md/csv`, and `daily_candidate_model_signals_for_report_latest.md/csv` for report/PDF sections. Raw research rows remain in `daily_candidate_model_signals_latest.md/csv`.
- For PDF model sections, use `daily_candidate_model_signals_for_report_latest.csv/md`. It has one row per report line + displayed model + stock, with merged source columns when the same stock hit the same model through multiple source categories.
- For the first page of curated PDFs, use `daily_report_model_registry_latest.csv/md` plus `daily_candidate_model_summary_for_report_latest.csv/md`. Render every official model row for that report line, split new signals and repeated/cumulative signals, and show `今日無候選` when a model has no candidate.
- `daily_candidate_frontpage_unique_latest.csv/md` is legacy/secondary. Do not use it for the fixed first-page per-model new/repeated summary.
- If a stock appears in the same model across multiple days, do not subtract score for that fact. Use `daily_candidate_same_model_repeat_latest.csv/md` as a separate repeated-signal table; front-page summaries can prioritize `new_model_signal` rows and place repeated same-model rows in a separate section.
- A model main condition being met means the stock enters that model. Do not add a second ChatGPT-side action gate after selection; use risk fields only as score/rank/annotation unless the program-side model marks a hard exclusion.
- Do not hard-code the number of models. Render the model rows present in `daily_candidate_model_parameters_latest.csv` and the matching candidates in `daily_candidate_model_signals_for_report_latest.csv`.
- Mainstream/non-mainstream is a report split and comparison group only. It must not cap score, veto a signal, or remove a stock from a model list.
- Use `model_score`, `model_rank`, `score_components`, `risk_penalty_tags`, and `report_bucket` for per-model ranking. Curated PDFs should show top rows per model/bucket; full PDFs should keep the complete model list.
- Use `daily_model_parameter_research_latest.csv` and `daily_model_parameter_research_horizon_detail_latest.csv` only as model-parameter evidence. The backtest entry basis is signal-date next open; close-return and high-return endpoints are separate for D+1 through D+10.
- Use `daily_model_parameter_recommendations_latest.csv` as the program-side interpretation of the research table: `promote_to_pdf_core`, `pdf_secondary_watch`, `score_component_only`, `intraday_target_watch`, or `research_only`. Do not let the PDF layer invent these statuses.
- Do not promote research-only rules to a PDF core section until the program-side model parameter file explicitly promotes them.
- If the model layer is missing, explicitly mark model-layer data unavailable instead of reconstructing a trading-action layer.
- Also read `daily_short_term_specialty_packet_latest.md`; it is the mandatory source for standalone D+1-D+10 short-term specialty summary plus D+5/D+10 detail sections.
- Use `model_score`, `model_rank`, `display_rank`, `score_components`, `risk_penalty_tags`, `risk_tags`, and `next_confirmation` directly. Do not invent a different reason when these fields exist.
- `must_not_overstate=True` means do not call the stock a top pick, even if the chart looks attractive.
- For volume breakout questions, read `volume_breakout_chatgpt_packet_latest.md`, `volume_attack_theme_layer_latest.md/csv`, `volume_attack_theme_stocks_latest.md/csv`, and then `volume_breakout_watch_latest.csv` for detail fields.
- Every volume-attack / early-theme table must include explicit `theme_final_status`, `theme_structural_status`, `theme_mainstream_label`, and `theme_volume_attack_status`; never show only a generic theme name.
- For 族群出量 / volume spread tables, use only `theme_spread_decision`, `leader_stock_id`, `second_stock_id`, and `third_stock_id` from `volume_attack_theme_layer_latest.csv`; never infer 龍頭/老二/老三 manually.
- For mainstream/non-mainstream grouping, read `stock_theme_taxonomy_latest.csv/md` and `stock_theme_taxonomy_review_latest.csv/md`. A stock needs an explicit core `structural_theme_bucket` to enter the mainstream capital line; official industry alone is not enough.
- Market theme is not the same as official industry: 上銀/大銀微系統 are robotics/precision motion; 華通/啟碁 can be low-earth-orbit satellite; 南亞/台玻 can be glass fiber/CCL.
- `theme_final_status` is daily flow/breadth. `theme_structural_status=core_mainstream_theme` is required before a stock can enter the mainstream capital line.
- Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are non-mainstream rotation even when daily flow is strong.
- Mainstream/non-mainstream is a display section and comparison group, not a score penalty or buy veto. Use `theme_group`, `display_section`, and `section_rank`; do not downgrade solely because a stock is non-mainstream.
- For any mainstream/non-mainstream backtest, use `daily_theme_status_history.csv` by `signal_date + stock_id`. Do not join today's `theme_final_status` backward onto historical signals.
- `theme_volume_attack_status=confirmed_volume_theme` or `early_mainstream_candidate` can be shown in the volume-attack theme line; `single_stock_volume_attack`, `non_mainstream_volume_watch`, `weak_or_non_mainstream_volume_watch`, `overheated_volume_theme`, and `failed_volume_theme` must not be mixed into the mainstream-funding front section.
- If `tdcc_overheated_short_term_edge_latest.md/csv` exists, include its D+5 and D+10 research-stat tables as supporting evidence. Do not use those research tables to override the core `TDCC短線延續模型 D+5/D+10` ranking.
- If `non_revenue_momentum_watch_latest.md/csv` exists, include a standalone `非營收驅動強勢股 / 題材資金先行` section. Do not merge it into the six fixed categories.
- `A_theme_first_momentum_revenue_not_primary` / `B_theme_first_watch_revenue_not_primary` are for core themes where monthly revenue is not the first screening layer. Use order/spec upgrade, theme breadth, price-volume, TDCC, and warrant confirmation instead of forcing a revenue interpretation.
- Do not confuse the fixed category `回檔後短線轉強` with the short-term specialty layer; they are different sections.

### TDCC / ABM report
- Use `tdcc_chatgpt_tracking_packet_latest.md`, then `tdcc_strength_ranking_top_latest.csv`, `tdcc_pre_move_abm_top_latest.csv`, and `tdcc_top_risk_list_latest.csv`.
- Strength ranking and pre-move ranking are separate. `strong_but_late`, `strong_but_overheated`, and `strong_but_divergent` are risk groups.
- `A_prime_watch` is only a tracking priority. It is not a buy instruction.
- Check mature sample counts before drawing performance conclusions.
- For overheated TDCC short-term setups, use `tdcc_overheated_short_term_edge_latest.md/csv` and the candidates CSV. The close-to-close and next-open metrics must remain separate.

### Market / index timing report
- Use `market_timing_chatgpt_packet_latest.md` for daily market context.
- Use `market_timing_backtest_chatgpt_packet_latest.md`, `market_timing_backtest_latest.csv`, and regime effectiveness files only for backtest/model tracking tasks.
- If `sample_status` is `insufficient_sample` or `pending_only`, say it is a hypothesis/observation, not a proven timing signal.
- Use `market_regime` and `risk_level` to adjust how aggressively daily candidates should be discussed.

### Warrant report
- Use `warrant_flow_by_stock_latest.csv` and `warrant_market_report_latest.md`.
- Warrant signals are auxiliary: 認購流入、認購強流入、認購/認售結構偏多、多空混合、無明確權證訊號。
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
| daily_candidate_model_signals_for_report_latest.csv | ready | 574 |
| tdcc_chatgpt_tracking_packet_latest.md | ready | - |
| market_timing_chatgpt_packet_latest.md | ready | - |
| market_timing_backtest_chatgpt_packet_latest.md | missing | - |
| surge_model_chatgpt_packet_latest.md | ready | - |
| warrant_flow_by_stock_latest.csv | ready | 451 |
| catalyst_needs_review_latest.csv | ready | 2 |

## Copy-Paste Summary For ChatGPT
Use program-side indicator classifications first. Start from READ_ME_FIRST, then this indicator usage guide, then the task-specific packet/top-list. Do not re-rank from memory. For daily candidates, use `model_id`, `model_name_zh`, `model_score`, `model_rank`, `display_rank`, `score_components`, `risk_penalty_tags`, `risk_tags`, and `next_confirmation`. For TDCC, keep Strength Ranking separate from ABM Pre-Move Ranking and respect risk buckets. For market timing, use sample_status and mature counts before making any timing statement. For single stocks, verify raw price/TDCC availability before producing a standard raw-data report.

