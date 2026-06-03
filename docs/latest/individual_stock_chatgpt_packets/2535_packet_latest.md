# INDIVIDUAL STOCK CHATGPT PACKET - 2535 達欣工

## Metadata
- generated_at: 2026-06-04 01:54:51 Asia/Taipei
- stock_id: 2535
- stock_name: 達欣工
- packet_status: standard_180d_window_packet
- latest_price_date: 20260603
- price_rows: 276
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2535_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2535_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2535_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2535_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2535_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2535_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2535_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2535_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2535_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2535_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2535_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2535_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2535_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2535.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2535.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2535.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2535.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2535.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2535.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2535_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2535_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2535_latest.md?ref=main

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
- open: 81.3
- high: 82.5
- low: 80.7
- close: 80.8
- volume: 286781
- ma5: 80.86
- ema23_primary: 76.95
- distance_to_ema23_pct: 5.01
- ma20: 76.64
- ma60: 73.66
- ma120: 70.18
- return_5d: 3.59
- return_20d: 9.93
- volume_ratio: 0.36
- distance_to_ma20_pct_auxiliary: 5.43
- distance_to_high_60_pct: -2.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,73.7,75.3,73.2,75.1,479565,72.88,3.05,72.33,71.84,0.56
20260508,75.1,75.3,74.2,74.2,241844,72.99,1.66,72.63,71.91,0.32
20260511,72.7,76,71.3,74.4,1794894,73.11,1.77,72.86,72,2.18
20260512,73.5,76.1,72.9,74.8,955215,73.25,2.12,73.07,72.11,1.13
20260513,74.7,76.7,74.5,75,2569122,73.39,2.19,73.31,72.22,2.71
20260514,75.1,77,75,75.1,920448,73.54,2.13,73.49,72.32,0.95
20260515,75.2,75.8,74,75.1,523566,73.67,1.95,73.72,72.43,0.54
20260518,74.6,74.7,73,73.1,531978,73.62,-0.7,73.87,72.5,0.54
20260519,73.3,73.8,72.1,73,383224,73.57,-0.77,74.05,72.55,0.39
20260520,74.3,74.7,72.6,74.6,564165,73.65,1.29,74.25,72.62,0.57
20260521,74.6,76,74.6,75.9,805960,73.84,2.79,74.54,72.7,0.8
20260522,75.9,77.6,75.9,77.5,916429,74.15,4.52,74.64,72.79,1.05
20260525,78.5,78.7,76.3,76.7,602145,74.36,3.15,74.64,72.83,0.74
20260526,76.7,77.3,75.5,75.9,329759,74.49,1.9,74.64,72.86,0.43
20260527,76.3,78.8,75.8,78,1469377,74.78,4.31,74.78,72.94,1.79
20260528,78.1,81,78.1,79.5,885579,75.17,5.76,74.97,73.03,1.1
20260529,80.2,80.5,79.6,80.3,378566,75.6,6.22,75.39,73.16,0.48
20260601,81,83,79.9,82.4,628114,76.17,8.18,75.84,73.36,0.8
20260602,82.4,82.8,80,81.3,504708,76.59,6.14,76.27,73.51,0.63
20260603,81.3,82.5,80.7,80.8,286781,76.95,5.01,76.64,73.66,0.36
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 61.06
- over_600_ratio: 57.01
- over_800_ratio: 55.49
- over_1000_ratio: 54.8
- over_400_change_1w: 0.47
- over_800_change_1w: 0.36
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,59.98,-0.22,55.36,0.04,54.04,0.37,4,False,True
20260320,59.94,-0.04,54.94,-0.42,53.93,-0.11,0,False,False
20260327,59.94,0,54.52,-0.42,53.51,-0.42,0,False,False
20260402,59.6,-0.34,53.88,-0.64,53.19,-0.32,1,False,False
20260410,59.51,-0.09,53.67,-0.21,52.98,-0.21,0,False,False
20260417,59.74,0.23,53.79,0.12,53.1,0.12,1,True,True
20260424,60.4,0.66,54.14,0.35,53.1,0,2,False,True
20260430,60.7,0.3,54.53,0.39,53.84,0.74,3,True,True
20260508,60.85,0.15,54.7,0.17,53.71,-0.13,4,False,True
20260515,60.69,-0.16,54.85,0.15,54.16,0.45,5,False,True
20260522,60.59,-0.1,55.13,0.28,54.44,0.28,6,False,True
20260529,61.06,0.47,55.49,0.36,54.8,0.36,7,True,True
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
