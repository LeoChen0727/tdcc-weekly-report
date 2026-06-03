# INDIVIDUAL STOCK CHATGPT PACKET - 1799 易威

## Metadata
- generated_at: 2026-06-04 01:54:27 Asia/Taipei
- stock_id: 1799
- stock_name: 易威
- packet_status: standard_180d_window_packet
- latest_price_date: 20260603
- price_rows: 275
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1799_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1799_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1799_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1799_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1799_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1799_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1799_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1799_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1799_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1799_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1799_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1799_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1799_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1799.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1799.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1799.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1799.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1799.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1799.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1799_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1799_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1799_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DECISION
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: current_price_ok
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
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260603
- open: 33.1
- high: 33.5
- low: 32.8
- close: 33.15
- volume: 33000
- ma5: 33.21
- ema23_primary: 35.05
- distance_to_ema23_pct: -5.41
- ma20: 34.92
- ma60: 37.17
- ma120: 35.26
- return_5d: -1.92
- return_20d: -8.43
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: -5.08
- distance_to_high_60_pct: -26.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,39.45,39.8,37.3,38.55,272000,38.75,-0.51,40.04,36.27,1.04
20260508,37.4,37.4,35.8,36,251000,38.52,-6.54,39.72,36.3,0.98
20260511,36.35,36.95,35.85,35.85,103000,38.3,-6.39,39.45,36.33,0.41
20260512,36.1,36.6,36,36.5,137000,38.15,-4.32,39.23,36.38,0.54
20260513,36.5,38.3,36.2,37.45,138000,38.09,-1.68,39.04,36.47,0.56
20260514,39,39,36.75,36.75,121000,37.98,-3.23,38.79,36.54,0.49
20260515,36.8,37.2,35.75,36.15,131000,37.83,-4.43,38.53,36.6,0.54
20260518,36.1,36.2,35.35,35.6,57000,37.64,-5.42,38.13,36.65,0.27
20260519,36,36,35.3,35.35,57000,37.45,-5.6,37.77,36.71,0.3
20260520,35.35,35.45,34.3,34.45,102000,37.2,-7.39,37.46,36.76,0.59
20260521,34.55,35.2,33.9,34.35,185000,36.96,-7.07,37.01,36.8,1.11
20260522,35,35.2,34,34.15,35000,36.73,-7.02,36.7,36.82,0.24
20260525,34.6,34.6,33.3,33.7,34000,36.48,-7.61,36.37,36.84,0.25
20260526,33.65,35,33.25,33.8,34000,36.25,-6.76,36.1,36.87,0.27
20260527,33.55,33.8,33.35,33.8,33000,36.05,-6.24,35.89,36.9,0.28
20260528,33.8,34,33,33.2,33000,35.81,-7.29,35.65,36.92,0.28
20260529,33.2,33.65,33.1,33.25,33000,35.6,-6.59,35.43,36.95,0.29
20260601,33.25,33.3,32,33.05,33,35.38,-6.6,35.24,37.01,0
20260602,32.85,34.65,32.75,33.4,34,35.22,-5.17,35.08,37.1,0
20260603,33.1,33.5,32.8,33.15,33000,35.05,-5.41,34.92,37.17,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 68.1
- over_600_ratio: 67.07
- over_800_ratio: 66.49
- over_1000_ratio: 66.49
- over_400_change_1w: 0.31
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 8
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,67.59,0.01,66.35,0.01,66.35,0.01,6,True,True
20260320,67.61,0.02,66.36,0.01,66.36,0.01,7,True,True
20260327,67.61,0,66.36,0,66.36,0,0,False,False
20260402,67.61,0,66.36,0,66.36,0,0,False,False
20260410,67.63,0.02,66.36,0,66.36,0,1,False,False
20260417,67.65,0.02,66.38,0.02,66.38,0.02,2,True,True
20260424,67.73,0.08,66.46,0.08,66.46,0.08,3,True,True
20260430,67.75,0.02,66.48,0.02,66.48,0.02,4,True,True
20260508,67.76,0.01,66.49,0.01,66.49,0.01,5,True,True
20260515,67.78,0.02,66.51,0.02,66.51,0.02,6,True,True
20260522,67.79,0.01,66.52,0.01,66.52,0.01,7,True,True
20260529,68.1,0.31,66.49,-0.03,66.49,-0.03,8,False,False
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
- ACTION_DECISION is the program-side action guidance for single-stock trading language.
- If action_rating is buy_now / scale_in / starter_position, do not rewrite it as waiting for confirmation unless current repo price, TDCC, or volume data directly contradicts it.
- entry_prerequisites are first-tranche requirements. post_entry_watch_items are post-entry monitoring checks, not buy-before blockers.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
