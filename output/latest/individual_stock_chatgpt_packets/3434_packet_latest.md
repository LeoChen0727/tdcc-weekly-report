# INDIVIDUAL STOCK CHATGPT PACKET - 3434 哲固

## Metadata
- generated_at: 2026-06-04 01:55:21 Asia/Taipei
- stock_id: 3434
- stock_name: 哲固
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3434_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3434_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3434_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3434_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3434_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3434_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3434_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3434_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3434_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3434_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3434_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3434_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3434_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3434.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3434.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3434.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3434.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3434.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3434.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3434_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3434_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3434_latest.md?ref=main

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
- thesis_state: high_level_consolidation
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
- price_too_extended

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260603
- open: 34.6
- high: 36.45
- low: 33.5
- close: 35.9
- volume: 36000
- ma5: 31.6
- ema23_primary: 29.98
- distance_to_ema23_pct: 19.76
- ma20: 29.37
- ma60: 29.3
- ma120: 30.28
- return_5d: 23.79
- return_20d: 23.16
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: 22.22
- distance_to_high_60_pct: -1.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,29.05,29.15,29,29.05,37000,29.55,-1.68,29.83,29.61,0.23
20260508,29.45,29.45,28.65,28.65,104000,29.47,-2.79,29.85,29.51,0.65
20260511,28.55,28.8,28.55,28.65,55000,29.4,-2.56,29.87,29.45,0.34
20260512,28.6,28.9,28.5,28.65,68000,29.34,-2.35,29.85,29.41,0.44
20260513,28.65,28.65,28.3,28.4,71000,29.26,-2.95,29.8,29.37,0.46
20260514,28.4,28.65,28.2,28.4,71000,29.19,-2.71,29.62,29.33,0.56
20260515,28.4,29.05,28.35,28.35,88000,29.12,-2.64,29.49,29.29,0.81
20260518,28,28.5,27.65,28.15,75000,29.04,-3.06,29.35,29.26,0.68
20260519,28.9,28.9,28,28,68000,28.95,-3.29,29.2,29.22,0.72
20260520,27.85,28.25,27.85,28.25,61000,28.89,-2.23,29.04,29.2,0.68
20260521,28.35,28.7,28.35,28.5,36000,28.86,-1.25,28.86,29.18,0.45
20260522,28.5,29,28.5,29,29000,28.87,0.44,28.79,29.17,0.42
20260525,29,29.5,28.8,29.2,29000,28.9,1.04,28.77,29.16,0.45
20260526,29.5,31,29.2,29.2,30000,28.93,0.95,28.77,29.15,0.5
20260527,29.2,29.2,28.8,29,29000,28.93,0.24,28.76,29.13,0.48
20260528,29,29.8,28.95,29.35,29000,28.97,1.32,28.77,29.11,0.49
20260529,29.5,29.55,29.15,29.45,29000,29.01,1.53,28.8,29.11,0.49
20260601,29.45,30.45,29.45,30.15,30,29.1,3.6,28.85,29.13,0
20260602,30,33.15,30,33.15,33,29.44,12.6,29.04,29.2,0
20260603,34.6,36.45,33.5,35.9,36000,29.98,19.76,29.37,29.3,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 44.25
- over_600_ratio: 40.39
- over_800_ratio: 32.41
- over_1000_ratio: 30.15
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 26
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,42.44,0.3,29.42,0.36,27.16,0.36,15,True,True
20260320,42.61,0.17,29.45,0.03,27.19,0.03,16,True,True
20260327,43,0.39,29.89,0.44,27.63,0.44,17,True,True
20260402,43.35,0.35,30.22,0.33,27.96,0.33,18,True,True
20260410,43.65,0.3,30.55,0.33,28.29,0.33,19,True,True
20260417,44.83,1.18,31.79,1.24,29.53,1.24,20,True,True
20260424,44.88,0.05,31.82,0.03,29.56,0.03,21,True,True
20260430,44.87,-0.01,31.83,0.01,29.57,0.01,22,False,True
20260508,43.76,-1.11,31.92,0.09,29.66,0.09,23,False,True
20260515,44.09,0.33,32.25,0.33,29.99,0.33,24,True,True
20260522,44.23,0.14,32.39,0.14,30.13,0.14,25,True,True
20260529,44.25,0.02,32.41,0.02,30.15,0.02,26,True,True
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
