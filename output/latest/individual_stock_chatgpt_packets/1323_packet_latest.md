# INDIVIDUAL STOCK CHATGPT PACKET - 1323 永裕

## Metadata
- generated_at: 2026-06-02 23:24:23 Asia/Taipei
- stock_id: 1323
- stock_name: 永裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 275
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1323_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1323_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1323_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1323_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1323_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1323_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1323_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1323_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1323_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1323_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1323_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1323_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1323_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1323.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1323.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1323.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1323.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1323.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1323.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1323_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1323_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1323_latest.md?ref=main

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
- entry_style: pullback_to_23ema
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
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 20.3
- high: 20.8
- low: 20.15
- close: 20.45
- volume: 216516
- ma5: 20.37
- ema23_primary: 20.16
- distance_to_ema23_pct: 1.41
- ma20: 19.84
- ma60: 20.23
- ma120: 19.68
- return_5d: 0.99
- return_20d: 3.28
- volume_ratio: 1.61
- distance_to_ma20_pct_auxiliary: 3.06
- distance_to_high_60_pct: -19.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,19.9,19.9,19.55,19.7,107505,20.68,-4.72,21.09,19.86,0.32
20260507,19.6,19.6,18.95,19.25,338616,20.56,-6.36,20.95,19.87,1.12
20260508,19.25,19.4,18.95,19.25,101173,20.45,-5.86,20.82,19.88,0.35
20260511,19.3,20,19.3,19.75,281259,20.39,-3.14,20.71,19.9,0.96
20260512,19.6,19.75,19.3,19.45,142640,20.31,-4.24,20.56,19.91,0.51
20260513,19.35,19.4,19.2,19.2,56925,20.22,-5.04,20.43,19.92,0.21
20260514,19.2,19.5,19.1,19.35,79307,20.15,-3.95,20.33,19.93,0.3
20260515,19.5,19.5,19.3,19.3,66020,20.08,-3.86,20.23,19.94,0.25
20260518,19.5,19.75,19.15,19.45,76044,20.02,-2.86,20.15,19.95,0.29
20260519,19.5,20,19.45,20,136418,20.02,-0.11,20.11,19.97,0.52
20260520,19.9,19.95,19.75,19.9,65958,20.01,-0.56,20.07,20,0.26
20260521,19.75,19.95,19.35,19.9,74682,20,-0.51,20.05,20.02,0.29
20260522,20.4,20.4,19.7,20.1,114975,20.01,0.45,19.95,20.04,0.54
20260525,20.1,20.3,20,20.15,166257,20.02,0.64,19.84,20.06,1.05
20260526,20.15,20.45,20.1,20.25,111711,20.04,1.04,19.8,20.09,0.78
20260527,20.2,20.2,19.95,20.2,79604,20.05,0.73,19.78,20.11,0.57
20260528,20.2,20.3,20,20.15,133432,20.06,0.44,19.76,20.14,0.95
20260529,20.15,20.25,20.05,20.1,47091,20.07,0.17,19.75,20.17,0.37
20260601,20.1,21,20.1,20.95,287475,20.14,4.03,19.81,20.2,2.18
20260602,20.3,20.8,20.15,20.45,216516,20.16,1.41,19.84,20.23,1.61
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 70.68
- over_600_ratio: 67.42
- over_800_ratio: 61.44
- over_1000_ratio: 61.44
- over_400_change_1w: 0.01
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 26
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,70.3,0.22,61.2,0.23,61.2,0.23,15,True,True
20260320,70.38,0.08,61.28,0.08,61.28,0.08,16,True,True
20260327,70.41,0.03,61.31,0.03,61.31,0.03,17,True,True
20260402,70.42,0.01,61.32,0.01,61.32,0.01,18,True,True
20260410,70.44,0.02,61.33,0.01,61.33,0.01,19,True,True
20260417,70.47,0.03,61.34,0.01,61.34,0.01,20,True,True
20260424,70.47,0,61.35,0.01,61.35,0.01,21,False,True
20260430,70.5,0.03,61.37,0.02,61.37,0.02,22,True,True
20260508,70.53,0.03,61.39,0.02,61.39,0.02,23,True,True
20260515,70.66,0.13,61.41,0.02,61.41,0.02,24,True,True
20260522,70.67,0.01,61.43,0.02,61.43,0.02,25,True,True
20260529,70.68,0.01,61.44,0.01,61.44,0.01,26,True,True
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
