# INDIVIDUAL STOCK CHATGPT PACKET - 5306 桂盟

## Metadata
- generated_at: 2026-06-02 23:28:12 Asia/Taipei
- stock_id: 5306
- stock_name: 桂盟
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5306_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5306_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5306_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5306_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5306_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5306_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5306_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5306_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5306_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5306_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5306_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5306_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5306_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5306.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5306.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5306.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5306.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5306.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5306.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5306_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5306_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5306_latest.md?ref=main

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
- open: 84.5
- high: 85
- low: 84
- close: 84.6
- volume: 137456
- ma5: 83.44
- ema23_primary: 83.19
- distance_to_ema23_pct: 1.69
- ma20: 82.69
- ma60: 84.77
- ma120: 87.94
- return_5d: 2.05
- return_20d: 4.83
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: 2.31
- distance_to_high_60_pct: -6.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,81.5,81.9,79.8,80.3,219556,83.48,-3.81,83.2,87.72,1.25
20260507,79.8,80.4,79.1,80.3,287980,83.22,-3.51,82.97,87.51,1.62
20260508,80.3,81.1,80.2,80.9,150850,83.02,-2.56,82.83,87.32,0.89
20260511,80.9,81.5,80.3,80.8,155597,82.84,-2.46,82.67,87.16,0.91
20260512,81,83.4,81,83,570306,82.85,0.18,82.57,87.04,2.95
20260513,83.1,83.1,81.5,82.1,286732,82.79,-0.83,82.44,86.87,1.43
20260514,82.8,85.9,82.8,83.4,337399,82.84,0.68,82.38,86.72,1.6
20260515,84.7,86.4,84.5,85.1,363840,83.03,2.49,82.36,86.58,1.63
20260518,85.5,85.5,83.1,83.5,249558,83.07,0.52,82.31,86.47,1.1
20260519,83.2,84.3,82.4,82.7,161691,83.04,-0.41,82.23,86.32,0.71
20260520,82.7,82.8,81.5,82,171208,82.95,-1.15,82.08,86.17,0.74
20260521,83.3,83.8,82,83.4,206912,82.99,0.5,82.02,85.97,0.88
20260522,82.7,83.2,82.1,83.2,128359,83.01,0.23,82.01,85.8,0.57
20260525,83.2,83.5,82.3,83,177448,83.01,-0.01,82.03,85.61,0.79
20260526,83,83,82.3,82.9,131184,83,-0.12,82.07,85.43,0.61
20260527,82.4,82.6,82.1,82.3,153510,82.94,-0.77,82.14,85.25,0.74
20260528,83.2,83.2,82.2,82.6,155616,82.91,-0.37,82.19,85.08,0.73
20260529,82.6,83.9,82.6,83.4,168217,82.95,0.54,82.31,84.94,0.78
20260601,83.4,84.5,83,84.3,191725,83.06,1.49,82.5,84.86,0.88
20260602,84.5,85,84,84.6,137456,83.19,1.69,82.69,84.77,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 68.88
- over_600_ratio: 65.09
- over_800_ratio: 65.09
- over_1000_ratio: 64.4
- over_400_change_1w: 0.05
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,69.64,-0.02,66.07,0.03,65.39,0.03,2,False,True
20260320,69.55,-0.09,66.08,0.01,65.4,0.01,3,False,True
20260327,69.51,-0.04,66.04,-0.04,65.36,-0.04,0,False,False
20260402,69.49,-0.02,66.01,-0.03,65.33,-0.03,0,False,False
20260410,69.38,-0.11,65.9,-0.11,65.22,-0.11,0,False,False
20260417,69.21,-0.17,65.73,-0.17,64.29,-0.93,0,False,False
20260424,69.09,-0.12,65.01,-0.72,64.33,0.04,1,False,True
20260430,68.88,-0.21,65.02,0.01,64.34,0.01,2,False,True
20260508,69.11,0.23,65.02,0,64.34,0,3,False,False
20260515,68.78,-0.33,65.03,0.01,64.35,0.01,4,False,True
20260522,68.83,0.05,65.05,0.02,64.36,0.01,5,True,True
20260529,68.88,0.05,65.09,0.04,64.4,0.04,6,True,True
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
