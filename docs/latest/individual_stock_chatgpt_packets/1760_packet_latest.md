# INDIVIDUAL STOCK CHATGPT PACKET - 1760 寶齡富錦

## Metadata
- generated_at: 2026-06-02 23:24:57 Asia/Taipei
- stock_id: 1760
- stock_name: 寶齡富錦
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1760_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1760_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1760_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1760_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1760_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1760_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1760_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1760_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1760_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1760_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1760_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1760_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1760_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1760.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1760.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1760.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1760.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1760.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1760.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1760_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1760_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1760_latest.md?ref=main

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
- open: 60.9
- high: 60.9
- low: 60
- close: 60.4
- volume: 254952
- ma5: 60.32
- ema23_primary: 61.91
- distance_to_ema23_pct: -2.44
- ma20: 61.88
- ma60: 62.95
- ma120: 63.55
- return_5d: -0.33
- return_20d: -9.45
- volume_ratio: 1.21
- distance_to_ma20_pct_auxiliary: -2.38
- distance_to_high_60_pct: -20.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,66.8,67.1,65.1,65.2,264891,65.06,0.22,65.08,63.3,0.6
20260507,65.7,65.9,65.1,65.9,140182,65.13,1.19,65.16,63.28,0.31
20260508,66.7,66.7,64.1,64.4,250090,65.07,-1.03,65.17,63.23,0.55
20260511,64.6,64.6,63.6,63.8,296445,64.96,-1.79,65.16,63.21,0.64
20260512,63.8,63.8,62.5,62.6,293563,64.76,-3.34,65.09,63.19,0.63
20260513,62.3,63,62.2,62.2,162270,64.55,-3.64,65.04,63.18,0.35
20260514,63,63,61.8,61.8,161460,64.32,-3.92,64.94,63.15,0.35
20260515,61.8,62.2,61,61.2,276881,64.06,-4.47,64.75,63.12,0.59
20260518,61.2,61.3,60.4,61.3,101161,63.83,-3.97,64.59,63.11,0.22
20260519,61.9,63,61.3,61.3,212942,63.62,-3.65,64.41,63.1,0.47
20260520,62,62,61,61,84025,63.4,-3.79,64.22,63.08,0.19
20260521,61.9,62.2,61.6,61.8,96338,63.27,-2.32,64.08,63.09,0.21
20260522,62.8,62.8,61.1,61.8,153407,63.15,-2.13,63.95,63.06,0.34
20260525,62.5,62.5,60.8,61,275791,62.97,-3.12,63.84,63.03,0.61
20260526,61.5,61.5,60.6,60.6,186369,62.77,-3.46,63.69,62.99,0.41
20260527,61.1,61.2,60.5,60.5,185434,62.58,-3.33,63.23,62.95,0.43
20260528,60.1,60.7,59.3,59.7,393690,62.34,-4.24,62.79,62.92,1.42
20260529,59.9,61,59.9,60.3,211584,62.17,-3.01,62.4,62.92,0.89
20260601,60.9,61,59.8,60.7,205355,62.05,-2.17,62.19,62.95,0.95
20260602,60.9,60.9,60,60.4,254952,61.91,-2.44,61.88,62.95,1.21
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 42.54
- over_600_ratio: 37.56
- over_800_ratio: 35.85
- over_1000_ratio: 33.8
- over_400_change_1w: -0.59
- over_800_change_1w: -0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,41.8,-0.05,34.48,-0.05,32.43,-0.01,0,False,False
20260320,41.86,0.06,34.5,0.02,32.43,0,1,False,True
20260327,41.99,0.13,34.49,-0.01,32.41,-0.02,2,False,False
20260402,42.15,0.16,34.56,0.07,32.41,0,3,False,True
20260410,42.11,-0.04,34.47,-0.09,32.4,-0.01,0,False,False
20260417,42.23,0.12,34.53,0.06,32.39,-0.01,1,False,True
20260424,42.8,0.57,35.56,1.03,32.39,0,2,False,True
20260430,42.86,0.06,34.69,-0.87,33.58,1.19,3,False,True
20260508,42.93,0.07,34.76,0.07,33.65,0.07,4,True,True
20260515,42.94,0.01,34.83,0.07,33.72,0.07,5,True,True
20260522,43.13,0.19,35.91,1.08,33.74,0.02,6,True,True
20260529,42.54,-0.59,35.85,-0.06,33.8,0.06,7,False,True
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
