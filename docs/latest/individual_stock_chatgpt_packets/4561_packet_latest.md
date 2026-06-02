# INDIVIDUAL STOCK CHATGPT PACKET - 4561 健椿

## Metadata
- generated_at: 2026-06-02 23:27:39 Asia/Taipei
- stock_id: 4561
- stock_name: 健椿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 275
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4561_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4561_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4561_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4561_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4561_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4561_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4561_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4561_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4561_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4561_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4561_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4561_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4561_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4561.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4561.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4561.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4561.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4561.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4561.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4561_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4561_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4561_latest.md?ref=main

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
- insufficient_tdcc_history

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 59.8
- high: 59.8
- low: 52.9
- close: 54.2
- volume: 55
- ma5: 51.7
- ema23_primary: 47.98
- distance_to_ema23_pct: 12.96
- ma20: 49.73
- ma60: 39.5
- ma120: 38.4
- return_5d: 8.4
- return_20d: 21.8
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: 8.98
- distance_to_high_60_pct: -9.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,44.3,44.35,42.65,44.2,1145000,36.75,20.28,35.95,36.93,2.04
20260507,45.2,47.5,44.3,47.25,2885000,37.62,25.59,36.67,36.91,4.12
20260508,47.85,51.9,47.7,51.4,4823000,38.77,32.57,37.63,36.97,5.15
20260511,50.2,52.5,48.45,51.6,2271000,39.84,29.52,38.61,37.09,2.17
20260512,51,51,49.3,50.2,625000,40.7,23.33,39.54,37.18,0.58
20260513,49.8,49.8,47.25,47.5,513000,41.27,15.1,40.17,37.21,0.47
20260514,47.1,49.4,47.1,48.45,397000,41.87,15.72,40.69,37.25,0.37
20260515,49.2,49.4,47.6,48.1,359000,42.39,13.48,41.22,37.34,0.34
20260518,48.1,49.85,48,49.85,474000,43.01,15.91,41.88,37.51,0.45
20260519,49.3,49.85,48,48,269000,43.43,10.54,42.52,37.62,0.25
20260520,48.5,48.8,47.45,47.7,156000,43.78,8.95,43.15,37.74,0.15
20260521,48,50,48,49.1,332000,44.22,11.02,43.88,37.88,0.31
20260522,50.2,51,49.2,51,50000,44.79,13.87,44.76,38.03,0.05
20260525,51.3,52.8,51.3,51.8,52000,45.37,14.16,45.71,38.21,0.05
20260526,51.2,52.9,47.4,50,50000,45.76,9.27,46.57,38.36,0.05
20260527,50.5,53.8,48.6,48.8,51000,46.01,6.06,47.2,38.49,0.05
20260528,48.95,50.3,46.9,47,48000,46.09,1.96,47.82,38.62,0.05
20260529,47.6,51.7,46.9,51.7,51000,46.56,11.04,48.5,38.85,0.06
20260601,53.3,56.8,53.3,56.8,56,47.41,19.79,49.25,39.21,0
20260602,59.8,59.8,52.9,54.2,55,47.98,12.96,49.73,39.5,0
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 59.05
- over_600_ratio: 57.66
- over_800_ratio: 57.66
- over_1000_ratio: 52.04
- over_400_change_1w: 1.24
- over_800_change_1w: -0.15
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.85,,57.92,,53.78,,0,False,False
20260508,58.77,-0.08,57.92,0,53.78,0,0,False,False
20260515,57.85,-0.92,57.85,-0.07,52.04,-1.74,0,False,False
20260522,57.81,-0.04,57.81,-0.04,52.04,0,0,False,False
20260529,59.05,1.24,57.66,-0.15,52.04,0,1,False,False
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
