# INDIVIDUAL STOCK CHATGPT PACKET - 1737 臺鹽

## Metadata
- generated_at: 2026-06-04 01:54:26 Asia/Taipei
- stock_id: 1737
- stock_name: 臺鹽
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1737_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1737_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1737_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1737_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1737_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1737_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1737_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1737_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1737_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1737_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1737_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1737_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1737_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1737.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1737.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1737.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1737.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1737.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1737.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1737_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1737_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1737_latest.md?ref=main

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
- open: 31.6
- high: 31.75
- low: 31.55
- close: 31.55
- volume: 313027
- ma5: 31.55
- ema23_primary: 31.58
- distance_to_ema23_pct: -0.08
- ma20: 31.52
- ma60: 31.69
- ma120: 31.65
- return_5d: 0
- return_20d: -0.32
- volume_ratio: 2.2
- distance_to_ma20_pct_auxiliary: 0.1
- distance_to_high_60_pct: -2.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,31.55,31.7,31.5,31.55,105555,31.77,-0.7,31.88,31.72,1
20260508,31.65,31.8,31.5,31.55,77611,31.75,-0.64,31.86,31.71,0.72
20260511,31.55,31.65,31.55,31.55,119629,31.74,-0.59,31.84,31.71,1.08
20260512,31.55,31.65,31.45,31.45,142283,31.71,-0.83,31.81,31.71,1.27
20260513,31.45,31.6,31.45,31.5,76921,31.7,-0.62,31.77,31.71,0.7
20260514,31.5,31.65,31.45,31.5,140638,31.68,-0.56,31.74,31.71,1.25
20260515,31.5,31.65,31.4,31.45,166399,31.66,-0.66,31.7,31.71,1.44
20260518,31.45,31.5,31.35,31.4,66134,31.64,-0.75,31.66,31.71,0.57
20260519,31.4,31.6,31.4,31.55,54757,31.63,-0.26,31.63,31.71,0.49
20260520,31.6,31.6,31.4,31.5,49987,31.62,-0.38,31.6,31.71,0.45
20260521,31.5,31.6,31.45,31.5,86512,31.61,-0.35,31.57,31.71,0.8
20260522,31.55,31.6,31.5,31.55,103383,31.6,-0.17,31.57,31.71,1.01
20260525,31.55,31.6,31.45,31.5,220550,31.6,-0.3,31.56,31.7,2.03
20260526,31.5,31.7,31.5,31.55,179214,31.59,-0.13,31.56,31.7,1.65
20260527,31.5,31.6,31.5,31.55,104438,31.59,-0.12,31.55,31.7,0.94
20260528,31.6,31.6,31.4,31.45,320341,31.58,-0.4,31.54,31.69,2.58
20260529,31.45,31.7,31.4,31.55,165962,31.57,-0.08,31.52,31.69,1.28
20260601,31.55,31.65,31.45,31.6,170201,31.58,0.07,31.52,31.69,1.33
20260602,31.6,31.75,31.55,31.6,179696,31.58,0.07,31.52,31.69,1.37
20260603,31.6,31.75,31.55,31.55,313027,31.58,-0.08,31.52,31.69,2.2
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 63.53
- over_600_ratio: 61.38
- over_800_ratio: 59.26
- over_1000_ratio: 58.83
- over_400_change_1w: 0.26
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.2
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,63.38,0.09,58.95,0.09,58.1,0.09,9,True,True
20260320,63.41,0.03,59,0.05,58.15,0.05,10,True,True
20260327,63.32,-0.09,59.12,0.12,58.27,0.12,11,False,True
20260402,63.31,-0.01,59.12,0,58.27,0,0,False,False
20260410,63.54,0.23,59.14,0.02,58.29,0.02,1,True,True
20260417,63.54,0,59.15,0.01,58.3,0.01,2,False,True
20260424,63.51,-0.03,59.15,0,58.3,0,0,False,False
20260430,63.5,-0.01,59.18,0.03,58.33,0.03,1,False,True
20260508,63.35,-0.15,58.83,-0.35,58.4,0.07,2,False,True
20260515,63.21,-0.14,59.01,0.18,58.58,0.18,3,False,True
20260522,63.27,0.06,59.06,0.05,58.63,0.05,4,True,True
20260529,63.53,0.26,59.26,0.2,58.83,0.2,5,True,True
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
