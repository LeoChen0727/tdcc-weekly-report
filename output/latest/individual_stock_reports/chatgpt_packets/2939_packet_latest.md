# INDIVIDUAL STOCK CHATGPT PACKET - 2939 永邑-KY

## Metadata
- generated_at: 2026-08-02 22:27:00 Asia/Taipei
- stock_id: 2939
- stock_name: 永邑-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 311
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2939_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2939_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2939_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2939_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2939_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2939_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2939_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2939.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2939.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2939.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2939.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2939_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2939_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2939_latest.md?ref=main

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
- open: 19.5
- high: 19.5
- low: 19.1
- close: 19.1
- volume: 12000
- ma5: 19.29
- ema23_primary: 19.48
- distance_to_ema23_pct: -1.96
- ma20: 19.2
- ma60: 21.05
- ma120: 22.78
- return_5d: 0.53
- return_20d: -0.52
- volume_ratio: 0.33
- distance_to_ma20_pct_auxiliary: -0.49
- distance_to_high_60_pct: -23.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,19.05,19.05,18.95,18.95,20000,20.66,-8.3,20.65,22.95,0.85
20260703,19,19.8,19,19.7,22001,20.58,-4.3,20.59,22.85,0.92
20260706,19.3,19.5,19,19.5,18001,20.49,-4.85,20.47,22.74,0.77
20260707,19.45,19.45,18.85,19.4,30000,20.4,-4.92,20.34,22.65,1.34
20260708,19.35,19.45,19.05,19.45,15001,20.32,-4.3,20.25,22.57,0.68
20260709,19.4,19.55,19.15,19.45,29000,20.25,-3.95,20.19,22.48,1.28
20260713,19.05,19.05,18.65,18.9,15002,20.14,-6.15,20.05,22.39,0.65
20260714,18.9,19.5,18.65,18.85,27001,20.03,-5.9,19.94,22.29,1.13
20260715,18.9,19.5,18.6,18.8,12000,19.93,-5.66,19.8,22.18,0.5
20260716,18.45,18.8,18.45,18.8,6000,19.83,-5.21,19.64,22.05,0.25
20260717,18.8,19.2,18.8,19.15,7000,19.78,-3.17,19.52,21.94,0.3
20260720,18.85,19.5,18.85,19.4,11022,19.75,-1.75,19.39,21.84,0.47
20260721,19.25,19.45,18.95,19.1,34004,19.69,-3.01,19.28,21.74,1.42
20260722,19.1,19.1,18.65,19,12004,19.63,-3.23,19.23,21.64,0.54
20260723,19.05,19.05,18.75,19,14105,19.58,-2.97,19.19,21.54,0.69
20260724,18.75,19.4,18.1,18.4,44069,19.48,-5.56,19.12,21.43,2.02
20260727,18.55,20.2,18.55,20.2,186008,19.54,3.36,19.18,21.34,6.94
20260728,20.45,21.6,19.2,19.2,159012,19.51,-1.61,19.18,21.24,4.69
20260729,19.3,19.65,18.7,19.55,64000,19.52,0.17,19.2,21.15,1.76
20260730,19.5,19.5,19.1,19.1,12000,19.48,-1.96,19.2,21.05,0.33
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 76.06
- over_600_ratio: 71.85
- over_800_ratio: 62.56
- over_1000_ratio: 58.22
- over_400_change_1w: 0.1
- over_800_change_1w: 0.1
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,75.96,0.09,62.46,0.03,58.12,2.23,2,True,True
20260522,75.97,0.01,62.47,0.01,58.13,0.01,3,True,True
20260529,75.97,0,62.47,0,58.13,0,0,False,False
20260605,75.97,0,62.47,0,58.13,0,0,False,False
20260612,75.96,-0.01,62.46,-0.01,58.12,-0.01,0,False,False
20260618,75.95,-0.01,62.45,-0.01,58.11,-0.01,0,False,False
20260626,75.95,0,62.45,0,58.11,0,0,False,False
20260703,75.95,0,62.45,0,58.11,0,0,False,False
20260709,75.94,-0.01,62.44,-0.01,58.1,-0.01,0,False,False
20260717,75.95,0.01,62.45,0.01,58.11,0.01,1,True,True
20260724,75.96,0.01,62.46,0.01,58.12,0.01,2,True,True
20260731,76.06,0.1,62.56,0.1,58.22,0.1,3,True,True
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
