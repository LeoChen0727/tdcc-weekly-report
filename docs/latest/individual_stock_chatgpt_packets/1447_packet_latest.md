# INDIVIDUAL STOCK CHATGPT PACKET - 1447 力鵬

## Metadata
- generated_at: 2026-06-02 23:24:31 Asia/Taipei
- stock_id: 1447
- stock_name: 力鵬
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1447_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1447_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1447_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1447_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1447_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1447_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1447_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1447_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1447_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1447_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1447_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1447_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1447_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1447.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1447.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1447.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1447.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1447.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1447.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1447_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1447_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1447_latest.md?ref=main

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
- action_rating: starter_position
- action_rating_label_zh: 可小量試單
- confidence_level: medium
- thesis_state: unclear
- entry_style: current_price_ok
- position_sizing: starter_1_4

### management_plan
- buy_first_tranche_now
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- none

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 6.35
- high: 6.58
- low: 6.2
- close: 6.34
- volume: 2525084
- ma5: 6.02
- ema23_primary: 5.65
- distance_to_ema23_pct: 12.3
- ma20: 5.55
- ma60: 5.34
- ma120: 5.4
- return_5d: 15.06
- return_20d: 27.31
- volume_ratio: 0.9
- distance_to_ma20_pct_auxiliary: 14.17
- distance_to_high_60_pct: -3.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,5,5,4.95,4.96,930755,5.12,-3.17,5.13,5.31,0.77
20260507,4.96,5,4.93,4.98,750124,5.11,-2.55,5.13,5.3,0.63
20260508,4.99,4.99,4.95,4.95,525995,5.1,-2.89,5.12,5.29,0.46
20260511,4.98,5.04,4.95,4.96,779720,5.09,-2.47,5.12,5.28,0.69
20260512,4.96,5,4.91,4.93,1029517,5.07,-2.81,5.1,5.27,0.95
20260513,4.99,5,4.9,4.9,907275,5.06,-3.13,5.08,5.26,0.86
20260514,4.92,5.38,4.92,5.22,6341870,5.07,2.92,5.08,5.25,4.87
20260515,5.22,5.35,5.06,5.34,4142613,5.09,4.83,5.07,5.25,2.91
20260518,5.33,5.87,5.3,5.76,8256907,5.15,11.85,5.1,5.26,4.65
20260519,5.61,5.81,5.36,5.8,4452091,5.2,11.46,5.12,5.27,2.27
20260520,5.78,5.97,5.62,5.89,3037960,5.26,11.96,5.15,5.27,1.47
20260521,5.89,5.97,5.81,5.9,2553009,5.31,11.02,5.19,5.28,1.19
20260522,5.9,6.05,5.74,6,2293485,5.37,11.7,5.23,5.29,1.05
20260525,5.98,5.98,5.75,5.85,1867164,5.41,8.11,5.28,5.3,0.85
20260526,5.85,5.86,5.45,5.51,3511949,5.42,1.67,5.3,5.3,1.52
20260527,5.39,5.54,5.36,5.5,2262795,5.43,1.36,5.32,5.3,0.96
20260528,5.53,5.8,5.53,5.73,2018226,5.45,5.11,5.36,5.3,0.84
20260529,5.8,6.3,5.75,6.21,4778674,5.51,12.61,5.42,5.31,1.84
20260601,6.21,6.46,6.12,6.33,3419255,5.58,13.39,5.49,5.33,1.26
20260602,6.35,6.58,6.2,6.34,2525084,5.65,12.3,5.55,5.34,0.9
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 71.5
- over_600_ratio: 69.63
- over_800_ratio: 68.12
- over_1000_ratio: 66.83
- over_400_change_1w: 0.27
- over_800_change_1w: 0.14
- over_1000_change_1w: 0.14
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,70.53,-0.11,67.14,0.08,65.77,-0.03,4,False,True
20260320,70.57,0.04,67.05,-0.09,65.77,0,5,False,False
20260327,70.12,-0.45,66.63,-0.42,65.44,-0.33,0,False,False
20260402,70.07,-0.05,66.58,-0.05,65.5,0.06,1,False,True
20260410,70.09,0.02,66.54,-0.04,65.35,-0.15,2,False,False
20260417,70.18,0.09,66.75,0.21,65.47,0.12,3,True,True
20260424,70.14,-0.04,66.64,-0.11,65.36,-0.11,0,False,False
20260430,69.98,-0.16,66.51,-0.13,65.23,-0.13,0,False,False
20260508,70.06,0.08,66.53,0.02,65.04,-0.19,1,False,True
20260515,70.31,0.25,66.84,0.31,65.45,0.41,2,True,True
20260522,71.23,0.92,67.98,1.14,66.69,1.24,3,True,True
20260529,71.5,0.27,68.12,0.14,66.83,0.14,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 1447 | 力鵬 | pattern | 型態觀察 |  |  |  | 預備發動型 |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1447 | 力鵬 | 9 | 9 | 5 | 9 | 9 | repeated_but_no_breakout | 近 10 日上榜 9 日、近 20 日上榜 9 日，尚未突破，需分辨醞釀或鈍化。 |

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
