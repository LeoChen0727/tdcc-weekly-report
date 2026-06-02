# INDIVIDUAL STOCK CHATGPT PACKET - 1443 立益物流

## Metadata
- generated_at: 2026-06-02 23:24:30 Asia/Taipei
- stock_id: 1443
- stock_name: 立益物流
- packet_status: standard_180d_window_packet
- latest_price_date: 20260602
- price_rows: 268
- latest_tdcc_date: 20260529
- tdcc_rows: 27
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1443_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1443_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1443_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1443_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1443_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1443_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1443_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1443_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1443_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1443_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1443_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1443_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1443_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1443.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1443.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1443.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1443.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1443.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1443.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1443_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1443_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1443_latest.md?ref=main

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
- open: 25.4
- high: 25.4
- low: 24.6
- close: 25.2
- volume: 30392
- ma5: 25.15
- ema23_primary: 25.25
- distance_to_ema23_pct: -0.22
- ma20: 25.96
- ma60: 24.4
- ma120: 25.75
- return_5d: -0.98
- return_20d: 12.5
- volume_ratio: 0.92
- distance_to_ma20_pct_auxiliary: -2.95
- distance_to_high_60_pct: -9.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,22.95,23.95,22.4,23.8,69740,22.96,3.68,22.94,24.71,1.56
20260507,23.85,25.75,23.85,25.75,128943,23.19,11.05,23.03,24.68,2.58
20260508,26.7,26.9,26.35,26.8,40110,23.49,14.09,23.19,24.67,0.78
20260511,27.4,27.6,26.9,27.6,30731,23.83,15.81,23.43,24.68,0.61
20260512,27.7,27.7,27.05,27.1,19703,24.1,12.43,23.63,24.68,0.39
20260513,26.75,26.95,26.25,26.8,28004,24.33,10.16,23.81,24.68,0.55
20260514,26.8,27.1,26.35,26.35,46387,24.5,7.56,23.94,24.66,0.94
20260515,26.95,26.95,26.1,26.2,27460,24.64,6.33,24.03,24.64,0.59
20260518,27.15,27.15,25.85,26.3,21191,24.78,6.14,24.15,24.63,0.49
20260519,26.15,26.5,26.05,26.5,29023,24.92,6.33,24.27,24.63,0.65
20260520,26.15,26.45,26.05,26.45,19347,25.05,5.59,24.4,24.63,0.43
20260521,26.25,26.5,26.25,26.45,17114,25.17,5.1,24.54,24.63,0.38
20260522,26.4,26.6,26.1,26.1,11100,25.24,3.39,24.72,24.62,0.26
20260525,26.5,26.5,25.4,25.9,13982,25.3,2.38,24.92,24.58,0.34
20260526,25.9,25.9,24.7,25.45,23168,25.31,0.55,25.1,24.55,0.55
20260527,25.35,25.35,24.5,25.1,31001,25.29,-0.76,25.28,24.5,0.76
20260528,26.25,26.35,24.9,25.2,31001,25.29,-0.34,25.48,24.48,0.84
20260529,25.05,25.5,25.05,25.15,21281,25.27,-0.49,25.67,24.45,0.58
20260601,25.15,25.2,24.8,25.1,17575,25.26,-0.63,25.82,24.42,0.5
20260602,25.4,25.4,24.6,25.2,30392,25.25,-0.22,25.96,24.4,0.92
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 89.73
- over_600_ratio: 85.35
- over_800_ratio: 84.32
- over_1000_ratio: 81.79
- over_400_change_1w: 0.04
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 20
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,89.28,0.07,82.88,0.05,81.57,0.05,9,True,True
20260320,89.31,0.03,82.9,0.02,81.59,0.02,10,True,True
20260327,89.32,0.01,82.91,0.01,81.6,0.01,11,True,True
20260402,89.38,0.06,83.54,0.63,81.63,0.03,12,True,True
20260410,89.5,0.12,83.54,0,81.63,0,13,False,False
20260417,89.51,0.01,83.56,0.02,81.65,0.02,14,True,True
20260424,89.52,0.01,84.16,0.6,81.65,0,15,False,True
20260430,89.58,0.06,84.2,0.04,81.69,0.04,16,True,True
20260508,89.58,0,84.22,0.02,81.71,0.02,17,False,True
20260515,89.65,0.07,84.27,0.05,81.75,0.04,18,True,True
20260522,89.69,0.04,84.29,0.02,81.77,0.02,19,True,True
20260529,89.73,0.04,84.32,0.03,81.79,0.02,20,True,True
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
