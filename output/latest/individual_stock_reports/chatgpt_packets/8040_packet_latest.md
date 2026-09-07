# INDIVIDUAL STOCK CHATGPT PACKET - 8040 九暘

## Metadata
- generated_at: 2026-09-06 22:18:45 Asia/Taipei
- stock_id: 8040
- stock_name: 九暘
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8040_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8040_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8040_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8040_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8040_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8040_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8040_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8040.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8040.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8040.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8040.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8040_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8040_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8040_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- no_major_tdcc_warning
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
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260904
- open: 74.7
- high: 76.5
- low: 73.7
- close: 75
- volume: 1334000
- ma5: 75.32
- ema23_primary: 74
- distance_to_ema23_pct: 1.36
- ma20: 72.94
- ma60: 83.02
- ma120: 78.95
- return_5d: 3.73
- return_20d: 2.74
- volume_ratio: 2.18
- distance_to_ma20_pct_auxiliary: 2.82
- distance_to_high_60_pct: -40.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,74.1,76.8,73.8,76,648000,77.01,-1.31,73.53,93.06,0.91
20260811,74.9,75.5,74.1,74.7,278000,76.82,-2.75,72.97,92.89,0.42
20260812,75.1,75.9,74.7,75.1,243000,76.67,-2.05,72.44,92.59,0.38
20260813,75.4,76.5,74,74.2,357000,76.47,-2.96,72.03,92.33,0.56
20260814,74.3,74.9,72.7,73,337000,76.18,-4.17,71.91,91.91,0.57
20260817,72.8,73.9,72.5,73,235000,75.91,-3.84,71.89,91.31,0.44
20260818,73.1,73.2,69,69.6,476000,75.39,-7.68,71.55,90.49,0.91
20260819,67.8,71.8,67.4,71.2,267000,75.04,-5.11,71.25,89.64,0.52
20260820,72.7,72.7,69.5,69.7,245000,74.59,-6.56,70.95,88.83,0.48
20260821,70.1,71.2,69.5,69.6,277000,74.18,-6.17,70.78,88.11,0.55
20260824,69.9,70.6,69.3,69.5,212000,73.79,-5.81,70.63,87.44,0.44
20260825,69.4,70.7,67.6,70.7,156000,73.53,-3.85,70.78,86.76,0.34
20260826,70.9,73.8,70.8,72,305000,73.4,-1.91,71.16,86.09,0.75
20260827,72.8,72.8,70.8,71.6,252000,73.25,-2.26,71.68,85.52,0.69
20260828,71.7,73.3,71.2,72.3,466000,73.17,-1.19,72,84.97,1.29
20260831,71,71,68.4,68.6,474000,72.79,-5.76,72,84.39,1.34
20260901,75.4,75.4,75.4,75.4,251000,73.01,3.27,72.27,83.94,0.72
20260902,82.9,82.9,82.9,82.9,744000,73.83,12.28,72.72,83.73,2.1
20260903,85.9,85.9,74.7,74.7,4697000,73.91,1.07,72.84,83.35,8.2
20260904,74.7,76.5,73.7,75,1334000,74,1.36,72.94,83.02,2.18
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 49.98
- over_600_ratio: 47.01
- over_800_ratio: 45.71
- over_1000_ratio: 44.68
- over_400_change_1w: -1.92
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,52.96,-0.25,46.61,-0.18,44.6,-1.16,0,False,False
20260626,51.96,-1,46.57,-0.04,44.6,0,0,False,False
20260703,51.08,-0.88,45.63,-0.94,44.6,0,0,False,False
20260709,51.09,0.01,45.63,0,44.6,0,1,False,False
20260717,51.12,0.03,45.63,0,44.6,0,2,False,False
20260724,50.7,-0.42,45.63,0,44.6,0,3,False,False
20260731,51.14,0.44,45.63,0,44.6,0,4,False,False
20260807,51.52,0.38,45.63,0,44.6,0,5,False,False
20260814,51.65,0.13,45.63,0,44.6,0,6,False,False
20260821,51.79,0.14,45.65,0.02,44.62,0.02,7,True,True
20260828,51.9,0.11,45.69,0.04,44.66,0.04,8,True,True
20260904,49.98,-1.92,45.71,0.02,44.68,0.02,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 8040 | 九暘 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | continued_2_3d | 1.發生變動日期:115/06/26 2.法人名稱:達發科技股份有限公司 3.舊任者姓名:羅瑞祥 4.舊任者簡歷: 睿瑾明新投資股份有限公司董事長 5.新任者姓名:潘建華 6.新任者簡歷: 九暘電子股份有限公司總經理 7.異動原因:法人董事改派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）:113/06/21-116/06/20 9.新任生效日期:115/06/26 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 8040 | 九暘 | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  |  | continued_2_3d | 1.發生變動日期:115/06/26 2.法人名稱:達發科技股份有限公司 3.舊任者姓名:羅瑞祥 4.舊任者簡歷: 睿瑾明新投資股份有限公司董事長 5.新任者姓名:潘建華 6.新任者簡歷: 九暘電子股份有限公司總經理 7.異動原因:法人董事改派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）:113/06/21-116/06/20 9.新任生效日期:115/06/26 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 8040 | 九暘 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | continued_2_3d | 1.發生變動日期:115/06/26 2.法人名稱:達發科技股份有限公司 3.舊任者姓名:羅瑞祥 4.舊任者簡歷: 睿瑾明新投資股份有限公司董事長 5.新任者姓名:潘建華 6.新任者簡歷: 九暘電子股份有限公司總經理 7.異動原因:法人董事改派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）:113/06/21-116/06/20 9.新任生效日期:115/06/26 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 8040 | 九暘 | 2 | 2 | 2 | 2 | 5 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
