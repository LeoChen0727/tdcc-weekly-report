# INDIVIDUAL STOCK CHATGPT PACKET - 9946 三發地產

## Metadata
- generated_at: 2026-06-04 01:57:29 Asia/Taipei
- stock_id: 9946
- stock_name: 三發地產
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9946_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9946_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9946_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9946_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9946_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9946_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9946_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9946_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9946_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9946_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9946_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9946_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9946_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9946.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9946.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9946.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9946.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9946.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9946.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9946_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9946_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9946_latest.md?ref=main

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
- open: 16.55
- high: 16.9
- low: 16.45
- close: 16.9
- volume: 584000
- ma5: 16.56
- ema23_primary: 16.56
- distance_to_ema23_pct: 2.04
- ma20: 16.57
- ma60: 16.97
- ma120: 17.42
- return_5d: 4.32
- return_20d: 7.99
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: 1.96
- distance_to_high_60_pct: -10.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,15.65,15.85,15.5,15.85,578349,16.43,-3.53,16.43,17.02,1.22
20260508,15.95,16.15,15.85,16.15,500888,16.41,-1.57,16.39,17,1.04
20260511,16.2,16.7,16.2,16.6,617559,16.42,1.08,16.36,17,1.26
20260512,16.65,16.7,16.4,16.7,718538,16.45,1.54,16.34,17,1.4
20260513,17,17,16.4,16.75,1505844,16.47,1.69,16.32,17,2.69
20260514,16.9,17.15,16.75,17,1298140,16.52,2.93,16.32,17,2.18
20260515,17.15,17.15,16.65,16.8,929593,16.54,1.58,16.3,17,1.51
20260518,16.7,17.15,16.55,16.8,936185,16.56,1.44,16.3,17.01,1.47
20260519,16.95,17.1,16.7,16.7,389866,16.57,0.77,16.31,17.01,0.63
20260520,16.7,16.8,16.55,16.8,393668,16.59,1.26,16.32,17.02,0.62
20260521,16.8,16.9,16.75,16.8,380742,16.61,1.15,16.32,17.02,0.61
20260522,16.8,16.85,16.7,16.8,485554,16.62,1.05,16.35,17.02,0.81
20260525,16.8,16.9,16.4,16.4,718925,16.61,-1.24,16.36,17.01,1.16
20260526,16.4,16.45,16.2,16.35,307518,16.58,-1.42,16.37,17.01,0.51
20260527,16.35,16.35,16.1,16.2,500512,16.55,-2.13,16.38,17,0.82
20260528,16.2,16.45,16.15,16.35,313533,16.54,-1.12,16.39,16.99,0.51
20260529,16.3,16.45,16.25,16.45,303429,16.53,-0.48,16.42,16.99,0.5
20260601,16.45,16.55,16.2,16.55,555667,16.53,0.12,16.47,16.99,0.91
20260602,16.55,16.55,16.35,16.55,326585,16.53,0.11,16.51,16.98,0.54
20260603,16.55,16.9,16.45,16.9,584000,16.56,2.04,16.57,16.97,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.19
- over_600_ratio: 78.58
- over_800_ratio: 78.2
- over_1000_ratio: 77.07
- over_400_change_1w: 0.07
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,80.92,-0.06,77.55,-0.25,76.69,0,4,False,False
20260320,81.02,0.1,77.55,0,76.69,0,5,False,False
20260327,81.04,0.02,77.55,0,76.69,0,6,False,False
20260402,81.12,0.08,77.84,0.29,76.69,0,7,False,True
20260410,81.15,0.03,77.83,-0.01,76.69,0,8,False,False
20260417,81.01,-0.14,77.83,0,76.69,0,0,False,False
20260424,81.08,0.07,77.56,-0.27,76.69,0,1,False,False
20260430,81.09,0.01,77.82,0.26,76.69,0,2,False,True
20260508,81.23,0.14,77.83,0.01,76.69,0,3,False,True
20260515,81.03,-0.2,77.95,0.12,76.82,0.13,4,False,True
20260522,81.12,0.09,78.11,0.16,76.98,0.16,5,False,True
20260529,81.19,0.07,78.2,0.09,77.07,0.09,6,True,True
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
