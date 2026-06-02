# INDIVIDUAL STOCK CHATGPT PACKET - 6534 正瀚-創

## Metadata
- generated_at: 2026-06-02 23:29:15 Asia/Taipei
- stock_id: 6534
- stock_name: 正瀚-創
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 274
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6534_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6534_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6534_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6534_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6534_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6534_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6534_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6534_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6534_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6534_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6534_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6534_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6534_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6534.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6534.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6534.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6534.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6534.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6534.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6534_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6534_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6534_latest.md?ref=main

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
- open: 93.1
- high: 94.5
- low: 93.1
- close: 93.3
- volume: 73630
- ma5: 94.64
- ema23_primary: 95.27
- distance_to_ema23_pct: -2.07
- ma20: 95.75
- ma60: 92.78
- ma120: 90.37
- return_5d: -2.71
- return_20d: 0.43
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: -2.55
- distance_to_high_60_pct: -10.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,95.8,95.9,94.1,94.4,84501,94.45,-0.06,96.69,88.94,0.36
20260507,94,96.8,93.8,96.8,152588,94.65,2.27,96.81,89.13,0.67
20260508,97.8,97.8,93.5,95.8,208375,94.74,1.11,96.76,89.3,0.96
20260511,95.4,97.8,94.4,97.6,181383,94.98,2.76,96.97,89.46,0.86
20260512,97,98.5,96,97.8,160457,95.22,2.71,97.03,89.68,0.8
20260513,97,97,95,96.7,101132,95.34,1.43,96.9,89.88,0.53
20260514,96.7,96.7,93,94.2,129034,95.25,-1.1,96.51,90.03,0.74
20260515,93.8,96.9,91.7,96.9,169789,95.38,1.59,96.42,90.21,1.06
20260518,94,96.5,93.4,96.5,138901,95.48,1.07,96.27,90.41,0.9
20260519,95,95.1,93.5,93.8,52099,95.34,-1.61,96.05,90.56,0.34
20260520,95,95,93.5,94.4,66205,95.26,-0.9,95.77,90.74,0.46
20260521,95.8,97.8,94.6,96.9,166150,95.4,1.58,95.61,90.95,1.13
20260522,96.1,97,95.2,97,171815,95.53,1.54,95.52,91.15,1.26
20260525,96.5,98.4,94.2,97,283016,95.65,1.41,95.53,91.41,2.01
20260526,95.5,96,93.8,95.9,311872,95.67,0.24,95.49,91.63,2.07
20260527,94,94.9,93.3,94.9,202804,95.61,-0.74,95.44,91.87,1.36
20260528,94,96.5,93.9,96,277468,95.64,0.38,95.57,92.11,1.76
20260529,95,97.1,94.9,96,378786,95.67,0.34,95.75,92.39,2.18
20260601,96.3,96.3,93,93,213784,95.45,-2.56,95.72,92.6,1.23
20260602,93.1,94.5,93.1,93.3,73630,95.27,-2.07,95.75,92.78,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 82
- over_600_ratio: 79.43
- over_800_ratio: 76.74
- over_1000_ratio: 75.88
- over_400_change_1w: 0.6
- over_800_change_1w: 0.6
- over_1000_change_1w: 0.61
- tdcc_consecutive_up_weeks: 8
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,79.98,-0.06,73.18,-0.04,72.31,-0.04,0,False,False
20260320,79.87,-0.11,73.48,0.3,71.82,-0.49,1,False,True
20260327,80.16,0.29,73.85,0.37,72.98,1.16,2,True,True
20260402,79.84,-0.32,73.64,-0.21,71.82,-1.16,0,False,False
20260410,79.83,-0.01,73.58,-0.06,72.71,0.89,1,False,True
20260417,80.18,0.35,74,0.42,73.13,0.42,2,False,True
20260424,80.32,0.14,74.48,0.48,73.61,0.48,3,True,True
20260430,80.77,0.45,74.86,0.38,73.99,0.38,4,True,True
20260508,80.9,0.13,75.64,0.78,73.98,-0.01,5,False,True
20260515,81.2,0.3,75.94,0.3,75.07,1.09,6,True,True
20260522,81.4,0.2,76.14,0.2,75.27,0.2,7,True,True
20260529,82,0.6,76.74,0.6,75.88,0.61,8,True,True
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
