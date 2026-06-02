# INDIVIDUAL STOCK CHATGPT PACKET - 2027 大成鋼

## Metadata
- generated_at: 2026-06-02 23:25:07 Asia/Taipei
- stock_id: 2027
- stock_name: 大成鋼
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2027_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2027_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2027_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2027_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2027_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2027_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2027_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2027_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2027_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2027_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2027_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2027_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2027_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2027.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2027.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2027.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2027.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2027.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2027.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2027_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2027_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2027_latest.md?ref=main

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
- insufficient_tdcc_history

### chatgpt_instruction
- Open the report with action_rating_label_zh as the program-side action conclusion.
- Do not downgrade buy_now / scale_in / starter_position to wait_pullback unless current repo price, volume, or TDCC data contradicts ACTION_DECISION.
- Treat post_entry_watch_items as post-entry monitoring, not as buy-before requirements.

## Latest Price Snapshot
- date: 20260602
- open: 43.6
- high: 43.65
- low: 42.05
- close: 43.65
- volume: 33817082
- ma5: 42.54
- ema23_primary: 40.83
- distance_to_ema23_pct: 6.92
- ma20: 40.86
- ma60: 38.49
- ma120: 37.7
- return_5d: 5.56
- return_20d: 15.63
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: 6.82
- distance_to_high_60_pct: -2.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260506,38.05,38.75,37.75,38.45,31091906,37.5,2.53,37.58,37.43,1.4
20260507,38.55,39.2,38.25,39.1,30542417,37.64,3.89,37.61,37.44,1.37
20260508,39.1,39.8,38.65,39.6,33348864,37.8,4.76,37.67,37.42,1.47
20260511,40,40.45,39.5,39.95,30077425,37.98,5.19,37.78,37.44,1.34
20260512,40.2,40.25,39.4,39.7,23834355,38.12,4.14,37.85,37.46,1.05
20260513,39.05,39.05,37.6,38.1,40973530,38.12,-0.05,37.83,37.45,1.74
20260514,38.25,40.5,38.1,39.8,57508095,38.26,4.03,37.95,37.47,2.31
20260515,40.05,41.2,39.75,39.85,47747482,38.39,3.8,38.08,37.51,1.8
20260518,39.5,41,39.25,39.4,37468752,38.48,2.4,38.16,37.55,1.34
20260519,39.5,40.35,39.35,40,25955528,38.6,3.62,38.32,37.59,0.92
20260520,40.3,41.95,40.25,41.15,46970650,38.82,6.01,38.53,37.66,1.57
20260521,41.35,42.45,40.85,42.35,34914027,39.11,8.28,38.8,37.74,1.14
20260522,42.5,42.9,41.75,41.95,24351187,39.35,6.62,39.09,37.82,0.8
20260525,42.5,44.35,42.5,43.8,37622473,39.72,10.28,39.46,37.93,1.19
20260526,44.3,44.75,41.35,41.35,37127594,39.85,3.75,39.71,37.99,1.13
20260527,41.5,43.25,41.05,42.45,27210094,40.07,5.94,39.93,38.08,0.84
20260528,42.55,43.15,41.4,41.75,18913490,40.21,3.83,40.09,38.17,0.6
20260529,42.15,42.5,41.6,41.65,17386615,40.33,3.27,40.29,38.25,0.56
20260601,42.05,43.2,41.6,43.2,28077068,40.57,6.48,40.57,38.37,0.88
20260602,43.6,43.65,42.05,43.65,33817082,40.83,6.92,40.86,38.49,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 73.11
- over_600_ratio: 71.15
- over_800_ratio: 70.19
- over_1000_ratio: 69.35
- over_400_change_1w: 0.58
- over_800_change_1w: 0.62
- over_1000_change_1w: 0.54
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.94,,64.71,,63.96,,0,False,False
20260508,69.1,1.16,65.87,1.16,65.04,1.08,1,True,True
20260515,70.22,1.12,67.25,1.38,66.46,1.42,2,True,True
20260522,72.53,2.31,69.57,2.32,68.81,2.35,3,True,True
20260529,73.11,0.58,70.19,0.62,69.35,0.54,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 2027 | 大成鋼 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |
| 20260521 | 2027 | 大成鋼 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 2027 | 大成鋼 | 9 | 9 | 5 | 9 | 9 | repeated_but_no_breakout | 近 10 日上榜 9 日、近 20 日上榜 9 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260602 | 2027 | 大成鋼 | 67 | 0 | 19119860.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- ACTION_DECISION is the program-side action guidance for single-stock trading language.
- If action_rating is buy_now / scale_in / starter_position, do not rewrite it as waiting for confirmation unless current repo price, TDCC, or volume data directly contradicts it.
- entry_prerequisites are first-tranche requirements. post_entry_watch_items are post-entry monitoring checks, not buy-before blockers.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
