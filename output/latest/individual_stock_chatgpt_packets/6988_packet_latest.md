# INDIVIDUAL STOCK CHATGPT PACKET - 6988 威力暘-創

## Metadata
- generated_at: 2026-06-02 23:29:59 Asia/Taipei
- stock_id: 6988
- stock_name: 威力暘-創
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 263
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6988_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6988_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6988_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6988_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6988_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6988_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6988_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6988_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6988_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6988_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6988_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6988_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6988_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6988.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6988.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6988.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6988.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6988.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6988.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6988_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6988_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6988_latest.md?ref=main

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
- insufficient_tdcc_history

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 15.4
- high: 15.4
- low: 15.05
- close: 15.2
- volume: 33020
- ma5: 15.85
- ema23_primary: 15.73
- distance_to_ema23_pct: -3.37
- ma20: 15.89
- ma60: 14.91
- ma120: 15.44
- return_5d: -8.16
- return_20d: 6.29
- volume_ratio: 0.35
- distance_to_ma20_pct_auxiliary: -4.33
- distance_to_high_60_pct: -16.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,15.1,15.1,14.3,14.4,51003,14.34,0.4,14.4,15.63,1.2
20260507,14.7,14.7,14.15,14.15,34000,14.33,-1.23,14.37,15.54,0.8
20260508,14.2,15.1,14.2,14.5,114320,14.34,1.11,14.35,15.46,2.46
20260511,15,15.25,14.5,14.9,92000,14.39,3.56,14.35,15.39,1.84
20260512,15,15.6,15,15.1,90431,14.45,4.52,14.37,15.32,1.69
20260513,15.5,16,15.25,15.25,143200,14.51,5.07,14.38,15.24,2.42
20260514,15,16.1,15,15.55,89060,14.6,6.51,14.41,15.17,1.43
20260515,16,17.1,15.5,17.1,135077,14.81,15.47,14.54,15.12,2
20260518,16.3,18.15,16.3,17.2,114399,15.01,14.61,14.65,15.06,1.57
20260519,17.25,17.5,16.7,16.85,100017,15.16,11.14,14.76,15.02,1.35
20260520,17.2,17.4,16.75,16.9,80000,15.31,10.41,14.87,14.99,1.04
20260521,16.95,17.2,16.3,16.7,127839,15.42,8.28,14.97,14.96,1.59
20260522,16.95,17.4,16.7,16.7,93271,15.53,7.54,15.1,14.94,1.11
20260525,16.7,17.45,16.65,16.65,135145,15.62,6.58,15.23,14.91,1.52
20260526,16.65,17,16.5,16.55,49000,15.7,5.42,15.38,14.89,0.56
20260527,17.3,17.3,16.45,16.45,123070,15.76,4.36,15.51,14.87,1.39
20260528,17,17.75,16.4,16.45,102537,15.82,3.99,15.65,14.87,1.11
20260529,16.45,16.45,15.55,15.8,85036,15.82,-0.11,15.77,14.88,0.9
20260601,15.75,16.1,15.3,15.35,77314,15.78,-2.72,15.84,14.89,0.8
20260602,15.4,15.4,15.05,15.2,33020,15.73,-3.37,15.89,14.91,0.35
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 78.82
- over_600_ratio: 76.88
- over_800_ratio: 69.99
- over_1000_ratio: 66.18
- over_400_change_1w: -0.61
- over_800_change_1w: 0.51
- over_1000_change_1w: 0.51
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.83,,68.33,,64.52,,0,False,False
20260508,78.89,0.06,68.49,0.16,64.68,0.16,1,True,True
20260515,79.16,0.27,68.98,0.49,65.17,0.49,2,False,True
20260522,79.43,0.27,69.48,0.5,65.67,0.5,3,True,True
20260529,78.82,-0.61,69.99,0.51,66.18,0.51,4,False,True
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
