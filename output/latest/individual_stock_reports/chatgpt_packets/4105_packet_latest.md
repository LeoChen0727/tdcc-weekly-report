# INDIVIDUAL STOCK CHATGPT PACKET - 4105 東洋

## Metadata
- generated_at: 2026-08-02 22:27:28 Asia/Taipei
- stock_id: 4105
- stock_name: 東洋
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4105_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4105_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4105_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4105_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4105_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4105_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4105_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4105.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4105.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4105.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4105.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4105_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4105_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4105_latest.md?ref=main

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
- model_category_display_zh: 單一個股分析
- score_interpretation_zh: 目前缺少完整分數資料，需以價格、TDCC 與風險條件輔助判斷。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260730
- open: 75.8
- high: 76.3
- low: 75.2
- close: 75.4
- volume: 451000
- ma5: 76.26
- ema23_primary: 76.66
- distance_to_ema23_pct: -1.64
- ma20: 77.38
- ma60: 75.43
- ma120: 77.22
- return_5d: -1.05
- return_20d: -2.84
- volume_ratio: 0.48
- distance_to_ma20_pct_auxiliary: -2.55
- distance_to_high_60_pct: -5.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,77,77.6,76.1,76.4,1121000,74.84,2.08,74.67,74.25,1.3
20260703,76.6,78.9,76.6,77.9,1207000,75.1,3.73,74.84,74.32,1.31
20260706,78,79.2,77.7,78.2,688000,75.35,3.78,74.97,74.39,0.72
20260707,78.8,78.8,77.6,77.9,853000,75.57,3.09,75.14,74.44,0.91
20260708,77.5,78.4,76.5,77.2,1163000,75.7,1.98,75.3,74.49,1.23
20260709,77.2,77.8,76.7,77.3,738000,75.84,1.93,75.43,74.54,0.8
20260713,77.9,78.6,77.3,78.4,893000,76.05,3.09,75.63,74.61,0.96
20260714,78.4,78.4,77.2,77.6,700000,76.18,1.87,75.81,74.67,0.76
20260715,77.9,79,77.9,78.4,1255000,76.36,2.67,76.02,74.73,1.32
20260716,78.4,79.5,78.3,78.7,1015000,76.56,2.8,76.27,74.81,1.05
20260717,78.1,78.7,77.3,77.8,1229000,76.66,1.48,76.47,74.88,1.23
20260720,77.8,78.2,77.4,78.1,729000,76.78,1.72,76.7,74.96,0.74
20260721,78.3,79.5,78.3,79.1,1115000,76.98,2.76,76.97,75.08,1.12
20260722,78.9,78.9,76.2,77,2161000,76.98,0.03,77.13,75.16,2.01
20260723,76.7,76.9,75.8,76.2,1214000,76.91,-0.93,77.21,75.23,1.11
20260724,76.2,77.2,76.1,77,571000,76.92,0.1,77.33,75.29,0.52
20260727,77.1,77.3,76.4,76.8,355000,76.91,-0.14,77.44,75.34,0.33
20260728,76.5,77.3,76.2,76.4,610000,76.87,-0.61,77.48,75.38,0.57
20260729,76.6,76.6,75,75.7,737000,76.77,-1.39,77.48,75.41,0.71
20260730,75.8,76.3,75.2,75.4,451000,76.66,-1.64,77.38,75.43,0.48
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 48.85
- over_600_ratio: 45.46
- over_800_ratio: 42.61
- over_1000_ratio: 39.4
- over_400_change_1w: 0
- over_800_change_1w: -0.42
- over_1000_change_1w: -0.1
- tdcc_consecutive_up_weeks: 13
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,48.55,0.74,41.2,0.23,38.34,0.59,2,True,True
20260522,48.47,-0.08,41.23,0.03,38.37,0.03,3,False,True
20260529,48.19,-0.28,41.39,0.16,37.83,-0.54,4,False,True
20260605,47.67,-0.52,41.4,0.01,38.2,0.37,5,False,True
20260612,47.61,-0.06,41.37,-0.03,37.85,-0.35,6,False,False
20260618,46.71,-0.9,41.18,-0.19,38.34,0.49,7,False,True
20260626,47.08,0.37,41.44,0.26,37.92,-0.42,8,False,True
20260703,48,0.92,41.87,0.43,38.7,0.78,9,True,True
20260709,48.92,0.92,42.87,1,39.04,0.34,10,True,True
20260717,48.98,0.06,42.08,-0.79,38.82,-0.22,11,False,False
20260724,48.85,-0.13,43.03,0.95,39.5,0.68,12,False,True
20260731,48.85,0,42.61,-0.42,39.4,-0.1,13,False,False
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| status |
| --- |
| no rows |

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
