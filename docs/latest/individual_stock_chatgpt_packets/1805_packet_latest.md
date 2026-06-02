# INDIVIDUAL STOCK CHATGPT PACKET - 1805 寶徠

## Metadata
- generated_at: 2026-06-02 23:25:00 Asia/Taipei
- stock_id: 1805
- stock_name: 寶徠
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1805_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1805_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1805_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1805_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1805_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1805_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1805_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1805_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1805_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1805_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1805_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1805_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1805_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1805.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1805.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1805.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1805.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1805.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1805.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1805_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1805_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1805_latest.md?ref=main

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
- open: 10
- high: 10.05
- low: 9.97
- close: 10.05
- volume: 93981
- ma5: 10.07
- ema23_primary: 10.26
- distance_to_ema23_pct: -2.05
- ma20: 10.24
- ma60: 10.57
- ma120: 11.16
- return_5d: 0.5
- return_20d: -6.51
- volume_ratio: 0.7
- distance_to_ma20_pct_auxiliary: -1.82
- distance_to_high_60_pct: -17.28

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,10.75,10.75,10.6,10.75,98545,10.77,-0.16,10.78,11.05,0.99
20260507,10.75,10.9,10.65,10.75,209985,10.77,-0.15,10.78,11.03,2
20260508,10.8,10.9,10.7,10.75,99728,10.76,-0.14,10.77,11.01,0.93
20260511,10.6,10.6,10.1,10.3,267651,10.73,-3.97,10.75,10.98,2.28
20260512,10.3,10.35,10.2,10.35,74104,10.69,-3.22,10.72,10.95,0.63
20260513,10.35,10.6,10.2,10.3,120050,10.66,-3.39,10.69,10.93,1.04
20260514,10.25,10.35,10.2,10.25,144565,10.63,-3.55,10.65,10.9,1.22
20260515,10.25,10.25,10.1,10.15,115269,10.59,-4.13,10.61,10.87,0.94
20260518,10.2,10.25,10.15,10.15,118051,10.55,-3.8,10.57,10.84,0.94
20260519,10.2,10.3,10.15,10.2,110053,10.52,-3.06,10.54,10.81,0.86
20260520,10.4,10.4,10.1,10.25,183648,10.5,-2.37,10.51,10.79,1.41
20260521,10.2,10.2,10.05,10.1,141776,10.47,-3.5,10.48,10.76,1.09
20260522,10.05,10.1,9.7,10.1,234707,10.44,-3.22,10.46,10.73,1.71
20260525,10.1,10.15,10,10,126547,10.4,-3.84,10.43,10.7,0.9
20260526,9.83,10.1,9.82,10,102012,10.37,-3.53,10.4,10.68,0.72
20260527,10.3,10.3,9.89,9.98,164268,10.33,-3.42,10.37,10.65,1.13
20260528,10,10.2,9.92,10.1,100279,10.31,-2.08,10.33,10.62,0.71
20260529,10.15,10.15,10.05,10.15,53941,10.3,-1.46,10.3,10.6,0.39
20260601,10.05,10.05,9.98,10.05,143314,10.28,-2.23,10.27,10.58,1.04
20260602,10,10.05,9.97,10.05,93981,10.26,-2.05,10.24,10.57,0.7
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 78.14
- over_600_ratio: 73.91
- over_800_ratio: 72.33
- over_1000_ratio: 69.6
- over_400_change_1w: -0.52
- over_800_change_1w: 0.67
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,77.28,0.14,71.08,0.03,69.01,0.03,2,True,True
20260320,77.33,0.05,71.12,0.04,69.05,0.04,3,True,True
20260327,77.14,-0.19,70.63,-0.49,68.56,-0.49,0,False,False
20260402,76.9,-0.24,70.68,0.05,68.61,0.05,1,False,True
20260410,76.98,0.08,70.75,0.07,68.67,0.06,2,True,True
20260417,77.08,0.1,70.86,0.11,68.76,0.09,3,True,True
20260424,77.8,0.72,70.92,0.06,68.82,0.06,4,True,True
20260430,77.95,0.15,71.06,0.14,68.96,0.14,5,True,True
20260508,78.15,0.2,71.25,0.19,69.15,0.19,6,True,True
20260515,78.38,0.23,71.46,0.21,69.36,0.21,7,True,True
20260522,78.66,0.28,71.66,0.2,69.56,0.2,8,True,True
20260529,78.14,-0.52,72.33,0.67,69.6,0.04,9,False,True
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
