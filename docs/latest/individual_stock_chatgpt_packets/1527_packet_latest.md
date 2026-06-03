# INDIVIDUAL STOCK CHATGPT PACKET - 1527 鑽全

## Metadata
- generated_at: 2026-06-04 01:54:18 Asia/Taipei
- stock_id: 1527
- stock_name: 鑽全
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1527_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1527_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1527_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1527_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1527_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1527_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1527_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1527_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1527_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1527_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1527_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1527_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1527_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1527.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1527.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1527.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1527.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1527.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1527.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1527_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1527_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1527_latest.md?ref=main

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
- open: 33.45
- high: 33.45
- low: 33
- close: 33.3
- volume: 403334
- ma5: 33.2
- ema23_primary: 32.83
- distance_to_ema23_pct: 1.43
- ma20: 32.7
- ma60: 32.62
- ma120: 33.26
- return_5d: 1.83
- return_20d: 1.99
- volume_ratio: 1.19
- distance_to_ma20_pct_auxiliary: 1.83
- distance_to_high_60_pct: -1.19

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260507,32.55,32.65,32.35,32.45,176629,32.65,-0.61,32.68,33.01,0.84
20260508,32.45,32.55,32.1,32.4,339718,32.63,-0.7,32.68,32.97,1.57
20260511,32.4,32.55,32.25,32.4,303732,32.61,-0.64,32.67,32.94,1.35
20260512,32.6,32.6,32.25,32.4,303720,32.59,-0.59,32.66,32.91,1.3
20260513,32.5,32.6,32.2,32.55,438491,32.59,-0.11,32.63,32.89,1.85
20260514,32.35,32.6,32.35,32.5,227209,32.58,-0.25,32.61,32.86,0.95
20260515,32.5,32.9,32.05,32.05,426703,32.54,-1.49,32.57,32.82,1.7
20260518,32.05,32.3,31.8,32.25,204748,32.51,-0.81,32.53,32.79,0.8
20260519,32.3,32.55,32.3,32.45,124517,32.51,-0.17,32.49,32.76,0.52
20260520,32.45,32.55,32.4,32.55,151906,32.51,0.12,32.47,32.73,0.63
20260521,32.6,33.05,32.6,32.9,331014,32.54,1.1,32.48,32.71,1.33
20260522,32.75,33,32.45,32.95,422994,32.58,1.15,32.51,32.69,1.65
20260525,32.95,32.95,32.55,32.55,383611,32.57,-0.08,32.52,32.66,1.44
20260526,32.55,33,32.55,32.95,270639,32.61,1.06,32.54,32.64,1.01
20260527,33,33.55,32.4,32.7,820658,32.61,0.26,32.55,32.62,2.73
20260528,32.7,33.35,32.5,32.75,361126,32.63,0.38,32.56,32.61,1.17
20260529,32.85,33.3,32.8,33,338609,32.66,1.05,32.59,32.6,1.06
20260601,33,33.7,32.65,33.5,448905,32.73,2.36,32.63,32.62,1.36
20260602,33.5,33.7,33.1,33.45,273600,32.79,2.02,32.67,32.62,0.84
20260603,33.45,33.45,33,33.3,403334,32.83,1.43,32.7,32.62,1.19
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 31.34
- over_600_ratio: 29.64
- over_800_ratio: 27.71
- over_1000_ratio: 27.12
- over_400_change_1w: 0.45
- over_800_change_1w: 0.08
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,30.52,0.5,26.72,0.47,23.59,-0.7,4,False,True
20260320,30.21,-0.31,25.57,-1.15,23.02,-0.57,0,False,False
20260327,30.68,0.47,25.79,0.22,23.84,0.82,1,True,True
20260402,30.47,-0.21,25.83,0.04,23.88,0.04,2,False,True
20260410,30.48,0.01,25.91,0.08,23.96,0.08,3,False,True
20260417,29.65,-0.83,26.38,0.47,25.79,1.83,4,False,True
20260424,29.62,-0.03,26.38,0,25.79,0,5,False,False
20260430,30.12,0.5,26.61,0.23,26.02,0.23,6,True,True
20260508,30.23,0.11,26.97,0.36,26.38,0.36,7,True,True
20260515,30.82,0.59,27.53,0.56,26.94,0.56,8,True,True
20260522,30.89,0.07,27.63,0.1,27.04,0.1,9,True,True
20260529,31.34,0.45,27.71,0.08,27.12,0.08,10,True,True
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
