# INDIVIDUAL STOCK CHATGPT PACKET - 1305 華夏

## Metadata
- generated_at: 2026-06-02 23:24:21 Asia/Taipei
- stock_id: 1305
- stock_name: 華夏
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1305_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1305_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1305_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1305_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1305_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1305_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1305_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1305_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1305_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1305_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1305_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1305_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1305_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1305.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1305.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1305.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1305.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1305.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1305.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1305_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1305_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1305_latest.md?ref=main

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
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
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
- open: 13.1
- high: 13.3
- low: 12.8
- close: 13.1
- volume: 4534244
- ma5: 12.59
- ema23_primary: 13.03
- distance_to_ema23_pct: 0.5
- ma20: 12.68
- ma60: 14.56
- ma120: 13.11
- return_5d: 9.17
- return_20d: -6.43
- volume_ratio: 1.16
- distance_to_ma20_pct_auxiliary: 3.31
- distance_to_high_60_pct: -34.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,13.8,13.9,13.1,13.3,6421705,14.89,-10.7,15.21,14.39,0.63
20260507,13,13.05,12.7,13,5420421,14.74,-11.78,15.06,14.39,0.57
20260508,13.2,13.25,12.7,12.75,3097176,14.57,-12.49,14.88,14.4,0.35
20260511,12.95,13.45,12.9,13.35,4155981,14.47,-7.73,14.71,14.41,0.49
20260512,13.2,13.35,12.95,13,2699996,14.35,-9.38,14.48,14.44,0.34
20260513,13.5,13.5,12.85,13,2728355,14.23,-8.67,14.25,14.46,0.37
20260514,12.75,12.8,12.5,12.65,3694618,14.1,-10.3,14.04,14.48,0.53
20260515,12.65,12.85,12.5,12.5,3002292,13.97,-10.51,13.86,14.49,0.45
20260518,12.8,13.25,12.75,12.9,4985849,13.88,-7.06,13.76,14.51,0.82
20260519,12.75,12.9,12.5,12.5,2192047,13.76,-9.19,13.64,14.52,0.38
20260520,12.5,12.6,12.2,12.45,2731010,13.65,-8.82,13.54,14.53,0.48
20260521,12.4,12.55,12.35,12.5,1854156,13.56,-7.81,13.45,14.54,0.34
20260522,12.5,12.5,12.2,12.4,3403807,13.46,-7.89,13.31,14.55,0.76
20260525,12.3,12.5,11.9,12.35,4535943,13.37,-7.62,13.19,14.56,1.06
20260526,12.4,12.5,11.9,12,3720302,13.26,-9.47,13.08,14.54,0.9
20260527,12.1,12.25,11.9,12.1,3549398,13.16,-8.05,12.97,14.54,0.85
20260528,12.15,12.65,12.05,12.6,7743103,13.11,-3.91,12.89,14.54,1.77
20260529,12.25,12.55,12.1,12.3,4061364,13.04,-5.71,12.77,14.53,0.99
20260601,12.3,12.95,12.2,12.85,3578492,13.03,-1.37,12.72,14.54,0.92
20260602,13.1,13.3,12.8,13.1,4534244,13.03,0.5,12.68,14.56,1.16
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 51.13
- over_600_ratio: 49.65
- over_800_ratio: 48.34
- over_1000_ratio: 48.18
- over_400_change_1w: -0.05
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260313,53.34,0.39,50.71,0.23,49.91,0.03,1,True,True
20260320,54.01,0.67,51.3,0.59,50.67,0.76,2,True,True
20260327,52.04,-1.97,49.75,-1.55,49.13,-1.54,0,False,False
20260402,50.66,-1.38,48.3,-1.45,47.37,-1.76,0,False,False
20260410,50.15,-0.51,47.49,-0.81,46.73,-0.64,0,False,False
20260417,50.95,0.8,48.44,0.95,47.8,1.07,1,True,True
20260424,49.81,-1.14,47.32,-1.12,47.18,-0.62,0,False,False
20260430,50.17,0.36,47.38,0.06,47.22,0.04,1,False,True
20260508,50.23,0.06,47.82,0.44,47.51,0.29,2,True,True
20260515,50.83,0.6,47.84,0.02,47.54,0.03,3,True,True
20260522,51.18,0.35,48.14,0.3,47.82,0.28,4,True,True
20260529,51.13,-0.05,48.34,0.2,48.18,0.36,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1305 | 華夏 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |
| 20260602 | 1305 | 華夏 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260602 | 1305 | 華夏 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 62.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |
| 20260521 | 1305 | 華夏 | pattern | 型態觀察 |  |  |  | 預備發動型 |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1305 | 華夏 | 9 | 9 | 5 | 9 | 9 | repeated_but_no_breakout | 近 10 日上榜 9 日、近 20 日上榜 9 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 1305 | 華夏 | 7 | 0 | 102670.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- ACTION_DECISION is the program-side action guidance for single-stock trading language.
- If action_rating is buy_now / scale_in / starter_position, do not rewrite it as waiting for confirmation unless current repo price, TDCC, or volume data directly contradicts it.
- entry_prerequisites are first-tranche requirements. post_entry_watch_items are post-entry monitoring checks, not buy-before blockers.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
