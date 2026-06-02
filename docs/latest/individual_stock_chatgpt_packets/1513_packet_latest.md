# INDIVIDUAL STOCK CHATGPT PACKET - 1513 中興電

## Metadata
- generated_at: 2026-06-02 23:24:37 Asia/Taipei
- stock_id: 1513
- stock_name: 中興電
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1513_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1513_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1513_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1513_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1513_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1513_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1513_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1513_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1513_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1513_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1513_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1513_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1513_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1513.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1513.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1513.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1513.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1513.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1513.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1513_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1513_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1513_latest.md?ref=main

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
- price_structure_not_broken
- revenue_not_deteriorating
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
- tdcc_distribution_warning

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 169.5
- high: 170
- low: 165
- close: 168
- volume: 8754578
- ma5: 167.5
- ema23_primary: 159.14
- distance_to_ema23_pct: 5.57
- ma20: 158.22
- ma60: 154.66
- ma120: 156.42
- return_5d: 1.82
- return_20d: 9.09
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: 6.18
- distance_to_high_60_pct: -5.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,157,158,154,155.5,10727471,152.43,2.02,151.82,157.53,2.03
20260507,157,158,155.5,156.5,5840853,152.77,2.44,152.25,157.05,1.08
20260508,157,163.5,157,158,17757265,153.2,3.13,152.65,156.72,2.88
20260511,159.5,159.5,156,158.5,7010322,153.64,3.16,153.05,156.55,1.09
20260512,159.5,159.5,156,157,4903477,153.92,2,153.32,156.44,0.75
20260513,157,157,154.5,155.5,4179311,154.05,0.94,153.53,156.22,0.64
20260514,156.5,157,153,153,4842134,153.97,-0.63,153.65,155.93,0.73
20260515,154,155.5,150,150,6052430,153.64,-2.37,153.4,155.68,0.91
20260518,149,149,146.5,148.5,3926981,153.21,-3.07,153.18,155.52,0.6
20260519,149,152,149,150,4396655,152.94,-1.92,153,155.3,0.68
20260520,150,150.5,147.5,148.5,4375774,152.57,-2.67,152.65,155.06,0.68
20260521,150,154.5,150,154.5,5712027,152.73,1.16,152.6,154.91,0.87
20260522,155,157,153.5,156.5,6295032,153.05,2.26,152.85,154.72,0.97
20260525,158,160,155.5,160,12479266,153.62,4.15,153.38,154.58,1.83
20260526,166,172,164,165,33962679,154.57,6.75,154.12,154.49,4.12
20260527,168.5,175.5,166.5,169,30847651,155.78,8.49,155.12,154.38,3.21
20260528,170,177,165,165.5,30884625,156.59,5.69,155.97,154.28,2.82
20260529,168.5,169.5,165,166.5,12795546,157.41,5.77,156.88,154.3,1.12
20260601,167.5,171,166.5,168.5,9845209,158.34,6.42,157.53,154.53,0.89
20260602,169.5,170,165,168,8754578,159.14,5.57,158.22,154.66,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 41.74
- over_600_ratio: 40.26
- over_800_ratio: 38.54
- over_1000_ratio: 37.49
- over_400_change_1w: -0.27
- over_800_change_1w: 0.11
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.94,,40.31,,38.87,,0,False,False
20260508,43.17,-0.77,39.83,-0.48,38.2,-0.67,0,False,False
20260515,42.4,-0.77,38.97,-0.86,37.71,-0.49,0,False,False
20260522,42.01,-0.39,38.43,-0.54,37.54,-0.17,0,False,False
20260529,41.74,-0.27,38.54,0.11,37.49,-0.05,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1513 | 中興電 | pattern | 型態觀察 | 51.0 |  |  | base_building |  | no_signal | stale_signal | calendar event: ex_dividend on 20260709; status=confirmed; proximity=within_60d |
| 20260521 | 1513 | 中興電 | pattern | 型態觀察 |  |  |  | 預備發動型 |  | no_signal | stale_signal | calendar event: ex_dividend on 20260709; status=confirmed; proximity=within_60d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1513 | 中興電 | 9 | 9 | 5 | 9 | 9 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1513 | 中興電 | 92 | 2 | 9530030.0 | 880.0 | 10829.58 | no_signal | 0 |  |

## Interpretation Guardrails
- ACTION_DECISION is the program-side action guidance for single-stock trading language.
- If action_rating is buy_now / scale_in / starter_position, do not rewrite it as waiting for confirmation unless current repo price, TDCC, or volume data directly contradicts it.
- entry_prerequisites are first-tranche requirements. post_entry_watch_items are post-entry monitoring checks, not buy-before blockers.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
