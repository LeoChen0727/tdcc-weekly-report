# INDIVIDUAL STOCK CHATGPT PACKET - 6680 鑫創電子

## Metadata
- generated_at: 2026-06-02 23:29:30 Asia/Taipei
- stock_id: 6680
- stock_name: 鑫創電子
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 264
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6680_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6680_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6680_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6680_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6680_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6680_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6680_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6680_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6680_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6680_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6680_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6680_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6680_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6680.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6680.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6680.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6680.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6680.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6680.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6680_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6680_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6680_latest.md?ref=main

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
- open: 56.2
- high: 56.2
- low: 56.2
- close: 56.2
- volume: 56
- ma5: 57.56
- ema23_primary: 55.97
- distance_to_ema23_pct: 0.4
- ma20: 55.36
- ma60: 56.82
- ma120: 61.12
- return_5d: -2.43
- return_20d: 6.64
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: 1.52
- distance_to_high_60_pct: -16.12

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,53,53,53,53,8000,55.48,-4.47,55.22,60.41,0.82
20260505,52,54.4,52,54.4,26000,55.39,-1.79,55.15,60.13,2.42
20260506,55.3,55.3,53.6,54.5,19000,55.32,-1.47,54.98,59.83,1.63
20260507,54.1,54.2,54.1,54.1,8000,55.21,-2.02,54.82,59.55,0.69
20260508,53.2,54,53.2,54,2000,55.11,-2.02,54.74,59.32,0.18
20260511,54.1,54.1,53.1,54,14000,55.02,-1.85,54.69,59.07,1.23
20260512,53.8,54.1,53.8,54.1,4000,54.94,-1.54,54.67,58.83,0.38
20260513,54.2,56.5,54.2,56.5,10000,55.07,2.59,54.75,58.65,0.96
20260514,55.1,55.1,54,54.4,10000,55.02,-1.12,54.65,58.47,0.97
20260515,54.4,54.4,53.2,53.2,3000,54.87,-3.04,54.51,58.23,0.29
20260519,53.5,53.5,53.2,53.2,4000,54.73,-2.79,54.38,58.03,0.39
20260520,53.2,53.9,51.7,53.5,11000,54.62,-2.06,54.3,57.81,1.05
20260522,54.5,55.9,54.5,55.9,55000,54.73,2.14,54.3,57.66,4.4
20260525,56.5,58,56.5,57,57000,54.92,3.79,54.26,57.55,3.99
20260526,57,57.6,55.6,57.6,57000,55.14,4.46,54.27,57.43,3.37
20260527,57.9,57.9,57.9,57.9,58000,55.37,4.56,54.44,57.32,3.04
20260528,57.9,57.9,57.9,57.9,58000,55.58,4.17,54.69,57.21,2.76
20260529,56,58.8,56,58,58000,55.78,3.97,54.94,57.09,2.44
20260601,56.4,58.3,56.4,57.8,57,55.95,3.3,55.19,56.96,0
20260602,56.2,56.2,56.2,56.2,56,55.97,0.4,55.36,56.82,0
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 72.63
- over_600_ratio: 70.66
- over_800_ratio: 67.8
- over_1000_ratio: 64.36
- over_400_change_1w: -0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,72.47,0.01,67.66,0.01,64.21,0.01,1,True,True
20260320,72.41,-0.06,67.61,-0.05,64.17,-0.04,0,False,False
20260327,72.47,0.06,67.65,0.04,64.21,0.04,1,True,True
20260402,72.53,0.06,67.73,0.08,64.29,0.08,2,True,True
20260410,72.54,0.01,67.74,0.01,64.3,0.01,3,True,True
20260417,72.62,0.08,67.77,0.03,64.33,0.03,4,True,True
20260424,72.62,0,67.77,0,64.33,0,0,False,False
20260430,72.64,0.02,67.78,0.01,64.34,0.01,1,True,True
20260508,72.64,0,67.78,0,64.34,0,0,False,False
20260515,72.63,-0.01,67.79,0.01,64.35,0.01,1,False,True
20260522,72.64,0.01,67.8,0.01,64.36,0.01,2,True,True
20260529,72.63,-0.01,67.8,0,64.36,0,0,False,False
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
