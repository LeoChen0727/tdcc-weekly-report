# INDIVIDUAL STOCK CHATGPT PACKET - 5609 中菲行

## Metadata
- generated_at: 2026-06-02 23:28:28 Asia/Taipei
- stock_id: 5609
- stock_name: 中菲行
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5609_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5609_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5609_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5609_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5609_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5609_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5609_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5609_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5609_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5609_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5609_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5609_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5609_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5609.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5609.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5609.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5609.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5609.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5609.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5609_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5609_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5609_latest.md?ref=main

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
- open: 81.4
- high: 81.6
- low: 81
- close: 81.5
- volume: 81
- ma5: 80.88
- ema23_primary: 80.08
- distance_to_ema23_pct: 1.77
- ma20: 80.08
- ma60: 79.34
- ma120: 79.39
- return_5d: 1.37
- return_20d: 4.49
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: 1.78
- distance_to_high_60_pct: -1.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,78.3,79,78.1,78.7,203000,78.69,0.01,78.86,78.81,1.22
20260507,79.2,79.9,78.5,79.6,293000,78.77,1.06,78.9,78.81,1.67
20260508,79.7,79.9,79.3,79.6,155000,78.84,0.97,78.92,78.83,0.86
20260511,79.6,80,79.6,79.6,154000,78.9,0.89,78.94,78.84,0.85
20260512,79.9,79.9,79.2,79.6,177000,78.96,0.81,78.98,78.87,0.95
20260513,79.5,79.5,79.3,79.3,170000,78.99,0.4,78.99,78.89,0.91
20260514,79.7,80.4,79.6,80.3,373000,79.1,1.52,79.06,78.92,1.89
20260515,80.3,80.3,79.1,79.2,307000,79.11,0.12,79.04,78.93,1.5
20260518,79,80,78.7,79.7,113000,79.16,0.69,79.02,78.96,0.56
20260519,79.4,80,79.4,79.5,76000,79.18,0.4,79.02,78.98,0.38
20260520,79.9,80.2,79.9,80,127000,79.25,0.94,79.04,79.01,0.64
20260521,80,80.9,80,80.8,253000,79.38,1.79,79.08,79.05,1.25
20260522,81,81.2,80.3,80.5,81000,79.47,1.29,79.15,79.09,0.41
20260525,80.4,80.5,79.9,80.3,80000,79.54,0.95,79.22,79.12,0.41
20260526,80.3,81.1,80.2,80.4,81000,79.61,0.99,79.33,79.16,0.44
20260527,80.4,80.9,80.2,80.2,80000,79.66,0.67,79.44,79.19,0.45
20260528,80.8,81.1,80.2,80.4,81000,79.72,0.85,79.57,79.21,0.47
20260529,83,83,80.5,81,81000,79.83,1.46,79.72,79.23,0.49
20260601,81,81.4,80.5,81.3,81,79.95,1.68,79.9,79.28,0
20260602,81.4,81.6,81,81.5,81,80.08,1.77,80.08,79.34,0
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 52.56
- over_600_ratio: 49.88
- over_800_ratio: 46.57
- over_1000_ratio: 46.57
- over_400_change_1w: 0.3
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,53.16,-0.01,46.7,-0.02,46.7,-0.02,0,False,False
20260320,53.11,-0.05,46.65,-0.05,46.65,-0.05,0,False,False
20260327,53.02,-0.09,46.58,-0.07,46.58,-0.07,0,False,False
20260402,52.94,-0.08,46.51,-0.07,46.51,-0.07,0,False,False
20260410,52.93,-0.01,46.5,-0.01,46.5,-0.01,1,False,False
20260417,52.65,-0.28,46.5,0,46.5,0,0,False,False
20260424,52.61,-0.04,46.47,-0.03,45.78,-0.72,0,False,False
20260430,52.16,-0.45,46.48,0.01,46.48,0.7,1,False,True
20260508,52.14,-0.02,46.44,-0.04,45.75,-0.73,0,False,False
20260515,52.16,0.02,46.46,0.02,46.46,0.71,1,True,True
20260522,52.26,0.1,46.55,0.09,46.55,0.09,2,True,True
20260529,52.56,0.3,46.57,0.02,46.57,0.02,3,True,True
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
