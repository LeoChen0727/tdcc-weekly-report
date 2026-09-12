# INDIVIDUAL STOCK CHATGPT PACKET - 2609 陽明

## Metadata
- generated_at: 2026-09-12 22:16:14 Asia/Taipei
- stock_id: 2609
- stock_name: 陽明
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2609_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2609_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2609_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2609_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2609_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2609_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2609_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2609.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2609.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2609.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2609.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2609_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2609_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2609_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_volume_price_failure
- acceptable_risk_reward

### post_entry_watch_items
- next_monthly_revenue
- next_tdcc_update
- 23ema_hold_or_reclaim
- volume_price_confirmation
- prior_high_breakout_quality
- sector_benchmark_strength
- event_follow_through
- warrant_overheat_check

### downgrade_reason
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260911
- open: 57.6
- high: 60.7
- low: 57.6
- close: 59.4
- volume: 79512906
- ma5: 58.26
- ema23_primary: 57.26
- distance_to_ema23_pct: 3.74
- ma20: 58.8
- ma60: 53.58
- ma120: 52.42
- return_5d: 2.06
- return_20d: 15.12
- volume_ratio: 0.86
- distance_to_ma20_pct_auxiliary: 1.03
- distance_to_high_60_pct: -11.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,51.7,54.8,51.7,54.7,97224950,51.34,6.54,51.16,51.48,4.68
20260818,55.1,57.2,54.6,56.2,86793977,51.75,8.61,51.43,51.54,3.66
20260819,55.6,59,54.9,59,114832016,52.35,12.7,51.81,51.66,4.02
20260820,59.9,61,58.6,60.3,153031407,53.01,13.74,52.3,51.8,4.29
20260821,60.7,64.6,60.1,64,198985656,53.93,18.67,52.92,51.98,4.5
20260824,65.8,66.8,63.5,64.5,170173225,54.81,17.68,53.59,52.19,3.26
20260825,65.9,67.3,62.9,63.6,192985885,55.54,14.51,54.24,52.37,3.16
20260826,63.5,64.4,57.3,57.6,157663706,55.71,3.39,54.62,52.41,2.32
20260827,56.7,58.4,56.5,57.9,60493753,55.9,3.59,55.01,52.49,0.86
20260828,57.5,57.5,55.8,56.2,42997981,55.92,0.5,55.28,52.53,0.6
20260831,57.2,59.5,56.3,59.5,233814127,56.22,5.83,55.72,52.63,2.83
20260901,59.4,60.5,57.5,57.6,49894440,56.33,2.25,56.05,52.69,0.59
20260902,58,60,56.9,57.5,41626918,56.43,1.89,56.39,52.78,0.49
20260903,57.6,58.6,57.2,57.8,35026477,56.55,2.22,56.76,52.88,0.4
20260904,58,59.3,57.2,58.2,29297988,56.68,2.68,57.15,53.01,0.33
20260907,58.5,58.7,58,58.1,15705138,56.8,2.29,57.47,53.13,0.18
20260908,58.2,58.2,57.1,57.3,15542080,56.84,0.8,57.73,53.21,0.18
20260909,57.1,58.6,56.5,58.5,31633364,56.98,2.67,58.08,53.33,0.36
20260910,58.8,59.8,57.4,58,43320399,57.07,1.64,58.41,53.45,0.48
20260911,57.6,60.7,57.6,59.4,79512906,57.26,3.74,58.8,53.58,0.86
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 61.98
- over_600_ratio: 60.57
- over_800_ratio: 59.91
- over_1000_ratio: 59.14
- over_400_change_1w: 0.21
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,55.87,0.28,53.88,0.26,53.14,0.14,1,True,True
20260703,55.29,-0.58,53.3,-0.58,52.43,-0.71,0,False,False
20260709,55.67,0.38,53.58,0.28,52.79,0.36,1,True,True
20260717,55.55,-0.12,53.52,-0.06,52.81,0.02,2,False,True
20260724,56.39,0.84,54.31,0.79,53.48,0.67,3,True,True
20260731,57.28,0.89,55.15,0.84,54.34,0.86,4,True,True
20260807,57.37,0.09,55.17,0.02,54.31,-0.03,5,False,True
20260814,57.72,0.35,55.56,0.39,54.73,0.42,6,True,True
20260821,61.16,3.44,58.94,3.38,58.12,3.39,7,True,True
20260828,62.23,1.07,60.02,1.08,59.18,1.06,8,True,True
20260904,61.77,-0.46,59.82,-0.2,59.12,-0.06,0,False,False
20260911,61.98,0.21,59.91,0.09,59.14,0.02,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2609 | 陽明 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | continued_overheated | 1.發生變動日期:115/09/08 2.法人名稱:陽明海運股份有限公司 3.舊任者姓名:劉政得/陳飛傑 4.舊任者簡歷: 劉政得:陽明(新加坡)有限公司船舶管理部主管 陳飛傑:陽明(新加坡)有限公司業務部主管 5.新任者姓名:卓承佑/洪啟勛 6.新任者簡歷: 卓承佑:陽明(新加坡)有限公司船舶管理部主管 洪啟勛:陽明(新加坡)有限公司業務部主管 7.異動原因:法人董事改派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）: 劉政得:111/10/03至115/09/30 陳飛傑:115/05/01至115/09/30 9.新任生效日期:115/10/01 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 2609 | 陽明 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | call_inflow | continued_overheated | 1.發生變動日期:115/09/08 2.法人名稱:陽明海運股份有限公司 3.舊任者姓名:劉政得/陳飛傑 4.舊任者簡歷: 劉政得:陽明(新加坡)有限公司船舶管理部主管 陳飛傑:陽明(新加坡)有限公司業務部主管 5.新任者姓名:卓承佑/洪啟勛 6.新任者簡歷: 卓承佑:陽明(新加坡)有限公司船舶管理部主管 洪啟勛:陽明(新加坡)有限公司業務部主管 7.異動原因:法人董事改派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）: 劉政得:111/10/03至115/09/30 陳飛傑:115/05/01至115/09/30 9.新任生效日期:115/10/01 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2609 | 陽明 | 18 | 9 | 5 | 10 | 18 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2609 | 陽明 | 100 | 8 | 18783660.0 | 490830.0 | 38.27 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
