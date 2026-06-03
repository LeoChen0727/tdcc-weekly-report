# INDIVIDUAL STOCK CHATGPT PACKET - 2414 精技

## Metadata
- generated_at: 2026-06-04 01:54:44 Asia/Taipei
- stock_id: 2414
- stock_name: 精技
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2414_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2414_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2414_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2414_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2414_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2414_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2414_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2414_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2414_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2414_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2414_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2414_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2414_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2414.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2414.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2414.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2414.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2414.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2414.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2414_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2414_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2414_latest.md?ref=main

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
- open: 52.3
- high: 52.4
- low: 51.8
- close: 52.2
- volume: 323048
- ma5: 51.34
- ema23_primary: 49.41
- distance_to_ema23_pct: 5.64
- ma20: 49.65
- ma60: 46.1
- ma120: 43.64
- return_5d: 1.95
- return_20d: 8.75
- volume_ratio: 0.84
- distance_to_ma20_pct_auxiliary: 5.13
- distance_to_high_60_pct: -0.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,49.3,49.3,47.65,48.3,814043,45.56,6.01,45.67,43.5,2.64
20260508,48.25,49.9,48.2,48.9,548027,45.84,6.68,45.96,43.63,1.67
20260511,48,49.15,47.3,47.9,447408,46.01,4.11,46.12,43.75,1.39
20260512,48.15,48.15,47.1,47.65,368204,46.15,3.26,46.27,43.87,1.16
20260513,47.3,48.2,47.25,48.2,246658,46.32,4.06,46.44,44,0.77
20260514,48.2,49.25,48.2,48.7,433333,46.52,4.69,46.62,44.13,1.33
20260515,49.2,49.6,48.25,48.3,505867,46.67,3.5,46.76,44.26,1.53
20260518,48.3,49.3,47.7,49.1,308306,46.87,4.76,46.95,44.4,0.92
20260519,49.05,49.05,48,48,260990,46.96,2.21,47.08,44.52,0.77
20260520,47.9,49.35,47.5,49.3,404071,47.16,4.54,47.28,44.65,1.15
20260521,50,50.4,49.6,50.1,452783,47.4,5.69,47.46,44.78,1.3
20260522,50.1,50.5,49.7,50.2,315650,47.64,5.38,47.67,44.92,0.91
20260525,50.5,51.5,49.9,50,430033,47.83,4.53,47.87,45.04,1.19
20260526,50.1,50.7,50.1,50.5,318827,48.06,5.09,48.13,45.17,0.86
20260527,50.5,51.3,50.5,51.2,320065,48.32,5.97,48.41,45.31,0.85
20260528,51.2,51.3,50.2,50.4,319430,48.49,3.94,48.64,45.44,0.82
20260529,50.5,51.5,50.5,50.8,229988,48.68,4.35,48.9,45.59,0.58
20260601,50.8,51.9,50.8,51.5,360862,48.92,5.28,49.16,45.76,0.9
20260602,52.4,52.4,51.4,51.8,268849,49.16,5.37,49.44,45.93,0.66
20260603,52.3,52.4,51.8,52.2,323048,49.41,5.64,49.65,46.1,0.84
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 58.76
- over_600_ratio: 53.85
- over_800_ratio: 50.86
- over_1000_ratio: 48.53
- over_400_change_1w: 0.04
- over_800_change_1w: 0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,57.94,0.06,49.43,-0.57,47.62,-0.06,1,False,False
20260320,58.09,0.15,50.03,0.6,47.61,-0.01,2,False,True
20260327,58.17,0.08,50.12,0.09,48.31,0.7,3,True,True
20260402,58.27,0.1,50.16,0.04,48.35,0.04,4,True,True
20260410,58.29,0.02,50.17,0.01,48.36,0.01,5,True,True
20260417,58.25,-0.04,50.2,0.03,48.39,0.03,6,False,True
20260424,58.3,0.05,50.19,-0.01,48.38,-0.01,7,False,False
20260430,58.3,0,50.71,0.52,48.37,-0.01,8,False,True
20260508,58.27,-0.03,50.69,-0.02,48.37,0,0,False,False
20260515,58.33,0.06,50.72,0.03,48.4,0.03,1,False,True
20260522,58.72,0.39,50.85,0.13,48.53,0.13,2,True,True
20260529,58.76,0.04,50.86,0.01,48.53,0,3,False,True
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
