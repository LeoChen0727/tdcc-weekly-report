# INDIVIDUAL STOCK CHATGPT PACKET - 1584 精剛

## Metadata
- generated_at: 2026-06-02 23:24:44 Asia/Taipei
- stock_id: 1584
- stock_name: 精剛
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1584_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1584_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1584_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1584_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1584_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1584_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1584_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1584_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1584_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1584_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1584_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1584_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1584_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1584.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1584.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1584.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1584.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1584.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1584.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1584_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1584_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1584_latest.md?ref=main

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
- open: 19.85
- high: 19.95
- low: 19.65
- close: 19.85
- volume: 20
- ma5: 19.75
- ema23_primary: 20
- distance_to_ema23_pct: -0.74
- ma20: 19.87
- ma60: 21.02
- ma120: 22.09
- return_5d: 0.51
- return_20d: -1
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: -0.11
- distance_to_high_60_pct: -16.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,20.2,20.2,19.6,20,730000,20.75,-3.62,20.73,22.36,0.84
20260507,20,20.45,19.85,20.35,876000,20.72,-1.78,20.63,22.3,1.04
20260508,20.5,20.7,20.05,20.1,720000,20.67,-2.74,20.54,22.22,0.86
20260511,20.1,21.5,20.1,20.4,1873000,20.64,-1.18,20.5,22.14,2.18
20260512,20.4,20.6,19.8,20,977000,20.59,-2.87,20.44,22.05,1.11
20260513,20,20.2,19.75,20,761000,20.54,-2.64,20.39,21.98,0.87
20260514,19.95,20,19.55,19.75,856000,20.48,-3.54,20.33,21.88,0.97
20260515,19.75,19.95,19.45,19.75,775000,20.42,-3.26,20.27,21.8,0.9
20260518,19.65,19.75,19.2,19.75,376000,20.36,-2.99,20.2,21.74,0.44
20260519,19.85,19.95,19.35,19.7,736000,20.3,-2.98,20.09,21.67,0.91
20260520,19.6,19.7,19.45,19.65,596000,20.25,-2.96,19.99,21.61,0.74
20260521,19.7,19.7,19.5,19.65,539000,20.2,-2.72,19.91,21.54,0.68
20260522,19.65,19.75,19.4,19.65,20000,20.15,-2.5,19.87,21.46,0.03
20260525,19.75,20.45,19.7,20.2,20000,20.16,0.21,19.89,21.39,0.03
20260526,20.35,20.35,19.75,19.75,20000,20.12,-1.86,19.9,21.32,0.03
20260527,19.75,19.85,19.25,19.45,19000,20.07,-3.08,19.89,21.25,0.03
20260528,19.5,19.85,19.5,19.8,20000,20.05,-1.23,19.88,21.19,0.03
20260529,19.8,20.2,19.7,19.8,20000,20.03,-1.12,19.89,21.13,0.04
20260601,19.8,20.1,19.5,19.85,20,20.01,-0.8,19.88,21.08,0
20260602,19.85,19.95,19.65,19.85,20,20,-0.74,19.87,21.02,0
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 41.17
- over_600_ratio: 38.82
- over_800_ratio: 37.94
- over_1000_ratio: 36.37
- over_400_change_1w: 0.48
- over_800_change_1w: 0.12
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 26
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,40.19,0.3,36.42,0.31,34.83,1.1,15,True,True
20260320,40.22,0.03,35.88,-0.54,34.3,-0.53,16,False,False
20260327,39.9,-0.32,36.28,0.4,34.76,0.46,17,False,True
20260402,39.56,-0.34,36.41,0.13,34.83,0.07,18,False,True
20260410,40.13,0.57,36.59,0.18,35.41,0.58,19,True,True
20260417,40.13,0,36.76,0.17,35.2,-0.21,20,False,True
20260424,40.12,-0.01,36.87,0.11,35.67,0.47,21,False,True
20260430,40.15,0.03,37.22,0.35,35.67,0,22,False,True
20260508,40.65,0.5,37.59,0.37,36.03,0.36,23,True,True
20260515,40.37,-0.28,37.61,0.02,35.65,-0.38,24,False,True
20260522,40.69,0.32,37.82,0.21,36.26,0.61,25,True,True
20260529,41.17,0.48,37.94,0.12,36.37,0.11,26,True,True
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
