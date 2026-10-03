# INDIVIDUAL STOCK CHATGPT PACKET - 6190 萬泰科

## Metadata
- generated_at: 2026-10-03 15:47:38 Asia/Taipei
- stock_id: 6190
- stock_name: 萬泰科
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 266
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6190_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6190_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6190_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6190_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6190_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6190_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6190_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6190.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6190.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6190.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6190.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6190_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6190_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6190_latest.md?ref=main

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
- date: 20261002
- open: 71.5
- high: 71.5
- low: 70.8
- close: 70.8
- volume: 1189000
- ma5: 70.06
- ema23_primary: 68.93
- distance_to_ema23_pct: 2.71
- ma20: 68.42
- ma60: 68.89
- ma120: 73.22
- return_5d: 3.96
- return_20d: 2.46
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: 3.47
- distance_to_high_60_pct: -17.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,69.2,69.8,67,67.3,2067000,68.52,-1.77,67.72,73.17,1.22
20260904,68.4,70.3,67.5,68,2388000,68.47,-0.69,67.83,72.97,1.37
20260907,68.8,68.8,67,67.1,1331000,68.36,-1.84,67.75,72.77,0.77
20260908,67.5,67.8,66,66,867000,68.16,-3.17,67.61,72.53,0.5
20260909,66.4,69.4,66.4,69,1716000,68.23,1.13,67.62,72.36,0.98
20260910,69.2,69.4,67.9,68.1,1994000,68.22,-0.18,67.61,72.23,1.12
20260911,68,68,66.8,66.8,1040000,68.1,-1.91,67.61,72.03,0.59
20260914,66.5,67.3,65.6,66,932000,67.93,-2.84,67.56,71.75,0.52
20260915,66.4,66.9,65.7,66,599000,67.77,-2.61,67.59,71.46,0.34
20260916,66.9,69.4,66.8,68.8,2315000,67.85,1.4,67.78,71.24,1.25
20260917,69.3,69.6,68.1,68.4,3941000,67.9,0.74,67.94,71,1.97
20260918,68.8,69.8,68.5,69.4,2828000,68.02,2.02,68.1,70.77,1.36
20260921,69.6,71.8,68.6,70.2,3659000,68.2,2.93,68.36,70.58,1.66
20260922,70.6,71.2,68.8,69,2144000,68.27,1.07,68.47,70.41,0.95
20260923,69,69.1,68.1,68.1,1161000,68.26,-0.23,68.44,70.14,0.53
20260924,68.5,69.4,68.5,68.6,1013000,68.29,0.46,68.44,69.88,0.48
20260929,68.6,69.5,68.2,69.3,1026000,68.37,1.36,68.37,69.61,0.51
20260930,70.1,71.2,69.6,70.4,1946000,68.54,2.72,68.36,69.35,0.96
20261001,71.2,71.6,70.4,71.2,1537000,68.76,3.55,68.34,69.08,0.78
20261002,71.5,71.5,70.8,70.8,1189000,68.93,2.71,68.42,68.89,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 36.48
- over_600_ratio: 32.93
- over_800_ratio: 28.81
- over_1000_ratio: 27.04
- over_400_change_1w: 0.44
- over_800_change_1w: -0.26
- over_1000_change_1w: 0.74
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,36.65,-0.24,30.4,0.01,29.46,0.05,1,False,True
20260724,35.8,-0.85,29.44,-0.96,28.01,-1.45,0,False,False
20260731,36.76,0.96,30.1,0.66,28.73,0.72,1,True,True
20260807,35.96,-0.8,29.89,-0.21,28.53,-0.2,0,False,False
20260814,36.19,0.23,29.86,-0.03,28.49,-0.04,1,False,False
20260821,35.77,-0.42,29.45,-0.41,27.53,-0.96,0,False,False
20260828,36.55,0.78,29.87,0.42,27.6,0.07,1,True,True
20260904,35.27,-1.28,29.49,-0.38,27.2,-0.4,0,False,False
20260911,35.68,0.41,28.69,-0.8,26.45,-0.75,1,False,False
20260918,35.73,0.05,28.73,0.04,26.9,0.45,2,False,True
20260924,36.04,0.31,29.07,0.34,26.3,-0.6,3,False,True
20261002,36.48,0.44,28.81,-0.26,27.04,0.74,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6190 | 萬泰科 | pattern | 型態觀察 | 54.0 |  |  | base_building |  |  | stale_signal | 1.原預定買回股份總金額上限(元):1,303,686,388 2.原預定買回之期間:115/05/13~115/07/10 3.原預定買回之數量(股):2,000,000 4.原預定買回區間價格(元):60.00~110.00 5.本次實際買回期間:115/05/13~115/06/25 6.本次已買回股份數量(股):1,536,000 7.本次已買回股份總金額(元):123,190,630 8.本次平均每股買回價格(元):80.20 9.累積已持有自己公司股份數量(股):6,600,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):3.54 11.本次未執行完畢之原因: 考量後續整體資金運用之效益，故未予以執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |
| 20261002 | 6190 | 萬泰科 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 5 | A_優先追蹤 |  |  |  | stale_signal | 1.原預定買回股份總金額上限(元):1,303,686,388 2.原預定買回之期間:115/05/13~115/07/10 3.原預定買回之數量(股):2,000,000 4.原預定買回區間價格(元):60.00~110.00 5.本次實際買回期間:115/05/13~115/06/25 6.本次已買回股份數量(股):1,536,000 7.本次已買回股份總金額(元):123,190,630 8.本次平均每股買回價格(元):80.20 9.累積已持有自己公司股份數量(股):6,600,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):3.54 11.本次未執行完畢之原因: 考量後續整體資金運用之效益，故未予以執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6190 | 萬泰科 | 14 | 12 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
