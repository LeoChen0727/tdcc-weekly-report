# INDIVIDUAL STOCK CHATGPT PACKET - 1734 杏輝

## Metadata
- generated_at: 2026-06-04 01:54:25 Asia/Taipei
- stock_id: 1734
- stock_name: 杏輝
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1734_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1734_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1734_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1734_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1734_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1734_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1734_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1734_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1734_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1734_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1734_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1734_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1734_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1734.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1734.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1734.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1734.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1734.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1734.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1734_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1734_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1734_latest.md?ref=main

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
- open: 31.3
- high: 31.3
- low: 30.8
- close: 30.9
- volume: 478264
- ma5: 30.92
- ema23_primary: 30.91
- distance_to_ema23_pct: -0.03
- ma20: 30.73
- ma60: 31.17
- ma120: 30.93
- return_5d: 0.98
- return_20d: 0
- volume_ratio: 1.15
- distance_to_ma20_pct_auxiliary: 0.57
- distance_to_high_60_pct: -4.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,31,31,30.65,30.75,377267,31.5,-2.38,31.71,31.17,1.13
20260508,30.7,30.9,30.55,30.65,314170,31.43,-2.48,31.67,31.16,0.92
20260511,30.65,30.75,30.45,30.55,490115,31.36,-2.57,31.62,31.15,1.39
20260512,30.55,30.95,30.45,30.95,593339,31.32,-1.19,31.58,31.15,1.6
20260513,30.85,30.85,29.8,30.8,481223,31.28,-1.53,31.54,31.16,1.27
20260514,30.55,30.8,30.55,30.65,258641,31.23,-1.85,31.47,31.15,0.71
20260515,30.65,30.7,30.5,30.6,263237,31.17,-1.84,31.39,31.15,0.75
20260518,30.6,30.6,30.4,30.6,285151,31.13,-1.69,31.32,31.15,0.84
20260519,30.45,31,30.45,30.55,345384,31.08,-1.7,31.23,31.15,1.01
20260520,30.6,30.7,30.4,30.65,328319,31.04,-1.27,31.17,31.15,0.97
20260521,30.65,30.85,30.55,30.8,340240,31.02,-0.72,31.09,31.15,1.04
20260522,30.8,30.85,30.55,30.75,285102,31,-0.81,31.04,31.15,0.9
20260525,30.75,30.75,30.4,30.5,561438,30.96,-1.48,30.98,31.15,1.67
20260526,30.5,30.6,30.4,30.5,360235,30.92,-1.36,30.91,31.14,1.07
20260527,30.5,30.65,30.35,30.6,324207,30.89,-0.95,30.86,31.14,0.93
20260528,30.55,30.85,30.55,30.7,435065,30.88,-0.57,30.8,31.14,1.2
20260529,30.75,30.85,30.6,30.7,542183,30.86,-0.53,30.76,31.15,1.44
20260601,30.65,31,30.5,31,681469,30.87,0.41,30.73,31.16,1.71
20260602,31.1,31.3,30.85,31.3,563116,30.91,1.26,30.73,31.17,1.34
20260603,31.3,31.3,30.8,30.9,478264,30.91,-0.03,30.73,31.17,1.15
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 46.88
- over_600_ratio: 43.37
- over_800_ratio: 40.83
- over_1000_ratio: 38.97
- over_400_change_1w: 0.51
- over_800_change_1w: 0.26
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 21
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,45.06,0.06,37.68,0.05,36.27,0.05,10,True,True
20260320,45.32,0.26,37.87,0.19,36.46,0.19,11,True,True
20260327,45.46,0.14,38.01,0.14,36.6,0.14,12,True,True
20260402,45.51,0.05,38.49,0.48,36.62,0.02,13,False,True
20260410,45.5,-0.01,38.51,0.02,36.63,0.01,14,False,True
20260417,46.09,0.59,38.63,0.12,36.71,0.08,15,True,True
20260424,46.48,0.39,39.16,0.53,36.8,0.09,16,True,True
20260430,46.6,0.12,39.25,0.09,36.85,0.05,17,True,True
20260508,46.46,-0.14,39.77,0.52,37.51,0.66,18,False,True
20260515,46.21,-0.25,40.16,0.39,38.3,0.79,19,False,True
20260522,46.37,0.16,40.57,0.41,38.7,0.4,20,True,True
20260529,46.88,0.51,40.83,0.26,38.97,0.27,21,True,True
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
