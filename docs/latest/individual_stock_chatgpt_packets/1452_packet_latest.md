# INDIVIDUAL STOCK CHATGPT PACKET - 1452 宏益

## Metadata
- generated_at: 2026-06-04 01:54:15 Asia/Taipei
- stock_id: 1452
- stock_name: 宏益
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1452_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1452_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1452_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1452_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1452_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1452_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1452_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1452_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1452_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1452_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1452_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1452_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1452_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1452.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1452.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1452.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1452.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1452.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1452.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1452_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1452_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1452_latest.md?ref=main

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
- open: 10.6
- high: 11
- low: 10.6
- close: 10.95
- volume: 235987
- ma5: 10.6
- ema23_primary: 10.81
- distance_to_ema23_pct: 1.28
- ma20: 10.74
- ma60: 11.24
- ma120: 11.51
- return_5d: 6.31
- return_20d: -2.67
- volume_ratio: 2.07
- distance_to_ma20_pct_auxiliary: 1.93
- distance_to_high_60_pct: -13.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,11.15,11.3,11.1,11.2,149802,11.51,-2.66,11.65,11.53,1.79
20260508,11.2,11.3,11.1,11.2,62648,11.48,-2.44,11.61,11.51,0.74
20260511,11.2,11.2,11.05,11.05,141587,11.44,-3.45,11.56,11.5,1.62
20260512,11.1,11.1,11.05,11.05,74277,11.41,-3.17,11.52,11.49,0.84
20260513,11.05,11.05,11,11,76423,11.38,-3.32,11.47,11.48,0.88
20260514,11.05,11.1,10.95,11,97100,11.35,-3.05,11.43,11.46,1.11
20260515,11.05,11.05,10.9,10.9,57783,11.31,-3.62,11.38,11.45,0.69
20260518,10.9,11,10.8,10.85,113332,11.27,-3.73,11.32,11.43,1.33
20260519,10.95,10.95,10.8,10.8,69059,11.23,-3.84,11.26,11.42,0.81
20260520,10.35,10.65,10.35,10.55,177482,11.17,-5.59,11.2,11.4,1.93
20260521,10.55,10.6,10.5,10.5,119882,11.12,-5.56,11.13,11.38,1.28
20260522,10.5,10.6,10.5,10.6,52486,11.08,-4.29,11.08,11.36,0.58
20260525,10.6,10.6,10.4,10.45,109927,11.02,-5.2,11.03,11.34,1.19
20260526,10.45,10.5,10.3,10.4,130755,10.97,-5.21,10.97,11.32,1.44
20260527,10.4,10.5,10.25,10.3,119054,10.92,-5.64,10.92,11.3,1.3
20260528,10.3,10.5,10.3,10.4,84003,10.87,-4.34,10.87,11.28,0.91
20260529,10.4,10.55,10.4,10.45,48055,10.84,-3.57,10.82,11.27,0.51
20260601,10.5,10.6,10.45,10.55,277555,10.81,-2.43,10.79,11.26,2.63
20260602,10.7,10.8,10.55,10.65,84569,10.8,-1.39,10.76,11.24,0.79
20260603,10.6,11,10.6,10.95,235987,10.81,1.28,10.74,11.24,2.07
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 48.45
- over_600_ratio: 45.63
- over_800_ratio: 41.05
- over_1000_ratio: 37.81
- over_400_change_1w: 0.12
- over_800_change_1w: 0.13
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 13
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,47.27,0.08,40.29,0.05,37.03,0.06,2,True,True
20260320,47.34,0.07,40.35,0.06,37.09,0.06,3,True,True
20260327,47.39,0.05,40.4,0.05,37.15,0.06,4,True,True
20260402,47.44,0.05,40.45,0.05,37.2,0.05,5,True,True
20260410,47.54,0.1,40.55,0.1,37.3,0.1,6,True,True
20260417,47.59,0.05,40.59,0.04,37.34,0.04,7,True,True
20260424,47.64,0.05,40.64,0.05,37.39,0.05,8,True,True
20260430,47.95,0.31,40.04,-0.6,37.47,0.08,9,False,True
20260508,48.05,0.1,40.1,0.06,37.53,0.06,10,True,True
20260515,48.19,0.14,40.83,0.73,37.64,0.11,11,True,True
20260522,48.33,0.14,40.92,0.09,37.7,0.06,12,True,True
20260529,48.45,0.12,41.05,0.13,37.81,0.11,13,True,True
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
