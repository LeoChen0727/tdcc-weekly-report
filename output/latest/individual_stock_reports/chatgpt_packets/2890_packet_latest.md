# INDIVIDUAL STOCK CHATGPT PACKET - 2890 永豐金

## Metadata
- generated_at: 2026-09-26 22:16:31 Asia/Taipei
- stock_id: 2890
- stock_name: 永豐金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2890_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2890_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2890.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2890.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2890.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2890.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2890_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2890_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2890_latest.md?ref=main

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
- date: 20260924
- open: 44.55
- high: 45.4
- low: 44.55
- close: 45.15
- volume: 10439331
- ma5: 45.31
- ema23_primary: 43.48
- distance_to_ema23_pct: 3.85
- ma20: 43.65
- ma60: 40.98
- ma120: 36.95
- return_5d: -1.74
- return_20d: 14.74
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: 3.44
- distance_to_high_60_pct: -2.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,39.7,39.9,39.4,39.8,19928878,39.39,1.03,39.46,38.71,0.91
20260831,39.65,41.1,39.6,41.1,62967549,39.53,3.96,39.52,38.84,2.67
20260901,40.8,42,40.75,41.5,27422506,39.7,4.54,39.61,38.99,1.17
20260902,41.5,42.3,40.95,42.15,31205716,39.9,5.63,39.74,39.16,1.3
20260903,42.5,43.15,42.2,42.6,26398081,40.13,6.16,39.94,39.3,1.08
20260904,42.65,43.1,42.35,42.85,19136125,40.35,6.18,40.13,39.46,0.77
20260907,43.25,43.25,42.15,42.6,20513376,40.54,5.08,40.31,39.62,0.81
20260908,42.35,43.5,42.15,43.45,30010862,40.78,6.54,40.53,39.77,1.16
20260909,43.5,44.1,42.85,43.2,28031635,40.99,5.4,40.7,39.91,1.07
20260910,42.6,43.5,42.55,42.9,22672446,41.15,4.27,40.85,40.03,0.86
20260911,42.8,44.1,42.6,43.7,32601711,41.36,5.66,41.01,40.16,1.25
20260914,43.7,45.1,43.4,44.8,31277251,41.64,7.58,41.27,40.24,1.24
20260915,44.8,45.2,44.1,44.55,26932735,41.89,6.36,41.52,40.32,1.08
20260916,44.75,45.3,43.95,45.3,39272275,42.17,7.42,41.81,40.41,1.52
20260917,45.5,46.3,44.8,45.95,36030980,42.49,8.15,42.14,40.52,1.34
20260918,46.05,46.05,44.8,45.25,52002471,42.72,5.93,42.42,40.61,1.8
20260921,45.2,46.15,44.75,45.7,18347361,42.97,6.37,42.76,40.72,0.63
20260922,46.35,46.35,45.25,45.4,13630029,43.17,5.17,43.06,40.81,0.48
20260923,45.7,45.7,44.65,45.05,20244857,43.32,3.98,43.36,40.9,0.7
20260924,44.55,45.4,44.55,45.15,10439331,43.48,3.85,43.65,40.98,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 81.25
- over_600_ratio: 79.96
- over_800_ratio: 78.92
- over_1000_ratio: 78.12
- over_400_change_1w: -0.02
- over_800_change_1w: 0
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,80.89,0.08,78.56,0.1,77.67,0.08,6,True,True
20260717,80.81,-0.08,78.48,-0.08,77.57,-0.1,0,False,False
20260724,80.75,-0.06,78.42,-0.06,77.54,-0.03,0,False,False
20260731,80.88,0.13,78.55,0.13,77.67,0.13,1,True,True
20260807,80.93,0.05,78.59,0.04,77.69,0.02,2,True,True
20260814,80.92,-0.01,78.59,0,77.7,0.01,3,False,True
20260821,81.3,0.38,78.98,0.39,78.11,0.41,4,True,True
20260828,80.94,-0.36,78.59,-0.39,77.77,-0.34,0,False,False
20260904,81.1,0.16,78.77,0.18,77.96,0.19,1,True,True
20260911,81.14,0.04,78.8,0.03,78.01,0.05,2,True,True
20260918,81.27,0.13,78.92,0.12,78.13,0.12,3,True,True
20260924,81.25,-0.02,78.92,0,78.12,-0.01,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2890 | 永豐金 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | no_signal | stale_signal | 1.股東常會日期:115/09/15 2.重要決議事項一、盈餘分配或盈虧撥補:通過2025年度盈餘分配案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表: 通過2025年度財務報告暨會計師查核報告書。 5.重要決議事項四、董監事選舉:不適用。 6.重要決議事項五、其他事項: (一)通過2025年度董事酬金案。 (二)通過2026年4月1日董事委任案。 (三)通過2026年度會計師委任案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 2890 | 永豐金 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | stale_signal | 1.股東常會日期:115/09/15 2.重要決議事項一、盈餘分配或盈虧撥補:通過2025年度盈餘分配案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表: 通過2025年度財務報告暨會計師查核報告書。 5.重要決議事項四、董監事選舉:不適用。 6.重要決議事項五、其他事項: (一)通過2025年度董事酬金案。 (二)通過2026年4月1日董事委任案。 (三)通過2026年度會計師委任案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2890 | 永豐金 | 40 | 5 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2890 | 永豐金 | 23 | 0 | 707110.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
