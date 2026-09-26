# INDIVIDUAL STOCK CHATGPT PACKET - 2801 彰銀

## Metadata
- generated_at: 2026-09-26 22:16:29 Asia/Taipei
- stock_id: 2801
- stock_name: 彰銀
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2801_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2801_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2801_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2801_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2801_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2801_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2801_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2801.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2801.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2801.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2801.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2801_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2801_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2801_latest.md?ref=main

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
- open: 27.8
- high: 28
- low: 27.6
- close: 27.75
- volume: 12370808
- ma5: 28.27
- ema23_primary: 27.11
- distance_to_ema23_pct: 2.37
- ma20: 27.29
- ma60: 25.09
- ma120: 23.25
- return_5d: -6.25
- return_20d: 12.35
- volume_ratio: 0.38
- distance_to_ma20_pct_auxiliary: 1.68
- distance_to_high_60_pct: -6.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,25.15,25.15,24.7,24.85,19034930,24.01,3.52,23.92,23.6,0.82
20260831,24.75,25.15,24.65,25.15,28219778,24.1,4.35,23.91,23.66,1.27
20260901,24.95,25.3,24.9,25.2,25541592,24.19,4.17,23.91,23.73,1.27
20260902,24.95,25.8,24.95,25.7,28838271,24.32,5.68,24.01,23.8,1.59
20260903,25.7,26.9,25.7,26.6,46745368,24.51,8.54,24.18,23.88,2.51
20260904,26.6,26.7,26.2,26.6,25691019,24.68,7.77,24.35,23.95,1.35
20260907,26.8,26.8,26.2,26.5,24267028,24.83,6.71,24.52,24.02,1.25
20260908,26.5,27.3,26.3,27.25,35457646,25.04,8.85,24.73,24.09,1.74
20260909,27.25,27.55,26.85,26.85,29009612,25.19,6.6,24.88,24.16,1.41
20260910,26.65,27.1,26.5,26.85,26974283,25.33,6.02,25.05,24.23,1.28
20260911,26.75,27.95,26.55,27.9,38086522,25.54,9.24,25.27,24.31,1.7
20260914,27.9,28.65,27.8,28.55,54168016,25.79,10.7,25.5,24.41,2.21
20260915,28.65,28.65,27.75,28,38455068,25.97,7.8,25.71,24.49,1.5
20260916,28.05,28.9,27.8,28.9,40587271,26.22,10.23,25.96,24.59,1.49
20260917,28.95,29.75,28.85,29.6,55925715,26.5,11.7,26.25,24.7,1.89
20260918,29.7,29.7,28.8,28.95,45992866,26.7,8.41,26.49,24.79,1.47
20260921,28.75,28.8,28.25,28.45,24240937,26.85,5.96,26.71,24.88,0.76
20260922,28.7,28.7,28.3,28.35,14996270,26.97,5.1,26.94,24.96,0.47
20260923,28.4,28.4,27.75,27.85,32124964,27.05,2.97,27.14,25.02,0.97
20260924,27.8,28,27.6,27.75,12370808,27.11,2.37,27.29,25.09,0.38
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 77.71
- over_600_ratio: 76.07
- over_800_ratio: 75.04
- over_1000_ratio: 74.11
- over_400_change_1w: -0.09
- over_800_change_1w: -0.05
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,77.43,0.08,74.62,0.12,73.72,0.12,6,True,True
20260717,77.49,0.06,74.67,0.05,73.78,0.06,7,True,True
20260724,77.63,0.14,74.86,0.19,73.96,0.18,8,True,True
20260731,77.83,0.2,75.08,0.22,74.17,0.21,9,True,True
20260807,77.55,-0.28,74.76,-0.32,73.84,-0.33,0,False,False
20260814,77.46,-0.09,74.69,-0.07,73.71,-0.13,0,False,False
20260821,77.5,0.04,74.73,0.04,73.8,0.09,1,True,True
20260828,78.18,0.68,75.48,0.75,74.51,0.71,2,True,True
20260904,77.89,-0.29,75.12,-0.36,74.17,-0.34,0,False,False
20260911,77.79,-0.1,75.02,-0.1,74.05,-0.12,0,False,False
20260918,77.8,0.01,75.09,0.07,74.11,0.06,1,True,True
20260924,77.71,-0.09,75.04,-0.05,74.11,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2801 | 彰銀 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.發生變動日期:115/08/20 2.法人名稱:財政部 3.舊任者姓名:無 4.舊任者簡歷:無 5.新任者姓名:董事陳佩君(財政部代表) 6.新任者簡歷:兆豐國際證券投資信託股份有限公司董事長 7.異動原因:財政部改派 8.原任期（例xx/xx/xx至xx/xx/xx）:115/6/19~118/6/18 9.新任生效日期:115/08/20 10.其他應敘明事項:依財政部115年8月20日台財庫字第11503716340號函辦理。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 2801 | 彰銀 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.發生變動日期:115/08/20 2.法人名稱:財政部 3.舊任者姓名:無 4.舊任者簡歷:無 5.新任者姓名:董事陳佩君(財政部代表) 6.新任者簡歷:兆豐國際證券投資信託股份有限公司董事長 7.異動原因:財政部改派 8.原任期（例xx/xx/xx至xx/xx/xx）:115/6/19~118/6/18 9.新任生效日期:115/08/20 10.其他應敘明事項:依財政部115年8月20日台財庫字第11503716340號函辦理。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2801 | 彰銀 | 2 | 2 | 2 | 6 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
