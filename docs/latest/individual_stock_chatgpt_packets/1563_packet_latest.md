# INDIVIDUAL STOCK CHATGPT PACKET - 1563 巧新

## Metadata
- generated_at: 2026-06-04 01:54:20 Asia/Taipei
- stock_id: 1563
- stock_name: 巧新
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1563_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1563_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1563_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1563_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1563_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1563_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1563_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1563_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1563_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1563_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1563_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1563_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1563_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1563.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1563.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1563.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1563.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1563.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1563.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1563_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1563_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1563_latest.md?ref=main

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
- open: 69
- high: 69.8
- low: 67.1
- close: 67.8
- volume: 1597771
- ma5: 67.06
- ema23_primary: 53.19
- distance_to_ema23_pct: 27.46
- ma20: 51.22
- ma60: 44.74
- ma120: 44.92
- return_5d: 21.94
- return_20d: 61.24
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: 32.38
- distance_to_high_60_pct: -6.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,42.4,43.75,41.65,43.55,1870291,41.94,3.85,42.06,42.62,2.39
20260508,43.8,44.05,43,43.9,1017603,42.1,4.27,42.15,42.57,1.29
20260511,44,44,43.2,43.8,692458,42.24,3.69,42.23,42.53,0.87
20260512,43.9,44.2,43.05,44,775167,42.39,3.8,42.32,42.51,0.97
20260513,44.1,44.8,43.9,44.2,1096827,42.54,3.9,42.37,42.48,1.34
20260514,44.4,46.6,44.4,45.4,1578742,42.78,6.13,42.52,42.48,1.83
20260515,45.65,46.3,44.5,44.75,866595,42.94,4.21,42.62,42.47,0.98
20260518,44.8,45.8,44.5,45.15,497907,43.13,4.69,42.73,42.47,0.57
20260519,45.25,46.3,45.2,45.3,625952,43.31,4.6,42.91,42.48,0.72
20260520,45.3,45.4,44.65,45,480341,43.45,3.57,43.07,42.45,0.55
20260521,45.3,45.75,44.6,45.7,774136,43.64,4.73,43.16,42.45,0.95
20260522,45.7,46.1,45.1,46.05,728898,43.84,5.05,43.36,42.45,0.92
20260525,46.05,46.35,45.45,46,808204,44.02,4.5,43.59,42.46,0.99
20260526,50.6,50.6,50.6,50.6,1592814,44.57,13.54,44.08,42.58,1.84
20260527,55.6,55.6,55.6,55.6,1389402,45.49,22.24,44.83,42.77,1.53
20260528,61.1,61.1,61.1,61.1,4815581,46.79,30.59,45.81,43.07,4.31
20260529,67.2,67.2,64,66.7,14824089,48.45,37.68,47.07,43.43,8.05
20260601,65.6,72.5,60.7,69.9,7979932,50.23,39.15,48.5,43.88,3.6
20260602,70,70,64.9,69.8,4931104,51.86,34.58,49.93,44.33,2.03
20260603,69,69.8,67.1,67.8,1597771,53.19,27.46,51.22,44.74,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 44.7
- over_600_ratio: 39.46
- over_800_ratio: 35.76
- over_1000_ratio: 32.6
- over_400_change_1w: 1.92
- over_800_change_1w: 0.38
- over_1000_change_1w: 0.73
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,41.49,-0.16,33.98,0.01,31.28,0.01,15,False,True
20260320,41.71,0.22,34.01,0.03,31.31,0.03,16,True,True
20260327,41.82,0.11,34.77,0.76,31.7,0.39,17,True,True
20260402,41.91,0.09,34.96,0.19,32.26,0.56,18,False,True
20260410,41.02,-0.89,33.65,-1.31,30.88,-1.38,0,False,False
20260417,41.12,0.1,33.76,0.11,30.99,0.11,1,True,True
20260424,41.07,-0.05,33.69,-0.07,30.56,-0.43,0,False,False
20260430,41.45,0.38,34.24,0.55,30.72,0.16,1,True,True
20260508,42.02,0.57,34.44,0.2,30.16,-0.56,2,False,True
20260515,42.64,0.62,35.27,0.83,31.34,1.18,3,True,True
20260522,42.78,0.14,35.38,0.11,31.87,0.53,4,True,True
20260529,44.7,1.92,35.76,0.38,32.6,0.73,5,True,True
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260603 | 1563 | 巧新 | 1 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- ACTION_DECISION is the program-side action guidance for single-stock trading language.
- If action_rating is buy_now / scale_in / starter_position, do not rewrite it as waiting for confirmation unless current repo price, TDCC, or volume data directly contradicts it.
- entry_prerequisites are first-tranche requirements. post_entry_watch_items are post-entry monitoring checks, not buy-before blockers.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
