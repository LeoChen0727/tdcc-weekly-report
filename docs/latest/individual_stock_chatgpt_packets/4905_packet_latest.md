# INDIVIDUAL STOCK CHATGPT PACKET - 4905 台聯電

## Metadata
- generated_at: 2026-06-04 01:55:49 Asia/Taipei
- stock_id: 4905
- stock_name: 台聯電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260603
- price_rows: 266
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4905_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4905_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4905_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4905_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4905_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4905_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4905_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4905_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4905_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4905_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4905_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4905_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4905_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4905.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4905.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4905.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4905.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4905.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4905.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4905_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4905_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4905_latest.md?ref=main

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
- date: 20260603
- open: 84.5
- high: 85.5
- low: 82.2
- close: 83.9
- volume: 84000
- ma5: 82.86
- ema23_primary: 81.12
- distance_to_ema23_pct: 3.42
- ma20: 80.22
- ma60: 80.18
- ma120: 71.19
- return_5d: 6.2
- return_20d: 5.53
- volume_ratio: 2.03
- distance_to_ma20_pct_auxiliary: 4.59
- distance_to_high_60_pct: -21.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,81,81.2,79.2,79.9,31000,81.72,-2.23,83.78,74.59,0.3
20260508,79.9,82,77.4,79.7,40000,81.56,-2.28,83.56,74.9,0.39
20260511,80.2,84,80.2,80.7,38000,81.48,-0.96,83.42,75.22,0.38
20260512,81.5,81.5,78.1,80.7,28000,81.42,-0.88,83.39,75.54,0.28
20260513,80.5,80.5,79,79.5,14000,81.26,-2.17,83.51,75.84,0.14
20260514,80.8,80.8,78.1,78.6,20000,81.04,-3.01,83.2,76.12,0.21
20260515,78.3,80,78.2,78.2,20000,80.8,-3.22,82.46,76.39,0.25
20260518,78.3,80.5,78.3,79.8,11000,80.72,-1.14,81.92,76.67,0.16
20260519,81.2,81.2,77.9,77.9,23000,80.48,-3.21,81.53,76.92,0.36
20260520,77,79.6,76.7,76.7,13000,80.17,-4.33,80.99,77.12,0.21
20260521,74.1,79.7,74.1,78,25000,79.99,-2.48,80.08,77.35,0.59
20260522,78.2,80.2,78.2,79.8,79000,79.97,-0.21,79.7,77.64,2.59
20260525,80,81.7,79,80.5,80000,80.02,0.61,79.44,77.95,2.58
20260526,81,85.9,80.5,81.1,82000,80.11,1.24,79.53,78.27,2.48
20260527,82.7,82.7,79,79,80000,80.01,-1.27,79.39,78.54,2.24
20260528,80.5,80.5,77.4,77.4,78000,79.8,-3,79.25,78.77,1.99
20260529,80,81.9,78.8,80.2,80000,79.83,0.46,79.36,79.03,1.93
20260601,80.2,88.1,80.2,87.8,86,80.49,9.08,79.75,79.44,0
20260602,88.5,88.5,84.6,85,86,80.87,5.11,80,79.81,0
20260603,84.5,85.5,82.2,83.9,84000,81.12,3.42,80.22,80.18,2.03
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.61
- over_600_ratio: 76.45
- over_800_ratio: 69.95
- over_1000_ratio: 63.65
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,81.64,0.02,69.8,0.02,63.5,0.02,1,True,True
20260320,81.64,0,69.8,0,63.5,0,0,False,False
20260327,81.5,-0.14,69.84,0.04,63.54,0.04,1,False,True
20260402,81.51,0.01,69.85,0.01,63.55,0.01,2,True,True
20260410,81.51,0,69.85,0,63.55,0,0,False,False
20260417,81.56,0.05,69.9,0.05,63.6,0.05,1,True,True
20260424,81.56,0,69.9,0,63.6,0,0,False,False
20260430,81.57,0.01,69.91,0.01,63.61,0.01,1,True,True
20260508,81.58,0.01,69.92,0.01,63.62,0.01,2,True,True
20260515,81.59,0.01,69.93,0.01,63.63,0.01,3,True,True
20260522,81.61,0.02,69.95,0.02,63.65,0.02,4,True,True
20260529,81.61,0,69.95,0,63.65,0,0,False,False
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
