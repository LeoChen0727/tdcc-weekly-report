# INDIVIDUAL STOCK CHATGPT PACKET - 2498 宏達電

## Metadata
- generated_at: 2026-05-28 19:32:00 Asia/Taipei
- stock_id: 2498
- stock_name: 宏達電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2498_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2498_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2498_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2498_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2498_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2498.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2498.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2498.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2498.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2498_latest.md?ref=main

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

## Latest Price Snapshot
- date: 20260528
- open: 45
- high: 45.5
- low: 43.8
- close: 43.9
- volume: 9042819
- ma5: 45.1
- ema23_primary: 43.29
- distance_to_ema23_pct: 1.41
- ma20: 42.97
- ma60: 41.62
- ma120: 44.63
- return_5d: -3.41
- return_20d: 10.3
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: 2.16
- distance_to_high_60_pct: -8.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,39.85,40.9,39.85,40.15,6917634,40.57,-1.03,40.3,42.3,1.07
20260504,40.6,41.45,40.4,41.1,6734932,40.61,1.2,40.35,42.21,1.02
20260505,41.3,41.45,40.75,41,4660647,40.65,0.87,40.43,42.1,0.7
20260506,41.55,41.55,40,40.1,8182552,40.6,-1.23,40.48,41.99,1.19
20260507,40.1,40.85,39.6,40.45,7053001,40.59,-0.34,40.46,41.9,1.03
20260508,40.9,41.25,39.3,39.35,12845816,40.48,-2.8,40.42,41.79,1.76
20260511,39.45,40.25,38.65,40.25,8626307,40.47,-0.53,40.45,41.72,1.15
20260512,40.35,41.3,39.35,41.3,12069492,40.53,1.89,40.52,41.68,1.55
20260513,41,41.25,39.8,40.1,8146362,40.5,-0.98,40.51,41.61,1.04
20260514,40.3,44.1,39.4,44.1,21497834,40.8,8.09,40.66,41.58,2.57
20260515,46.35,46.9,44.75,45.3,71302266,41.17,10.02,40.86,41.59,6.16
20260518,45.6,46.95,44.1,44.2,43881556,41.43,6.7,41.01,41.57,3.24
20260519,44.05,46.3,43.75,45.65,26249966,41.78,9.27,41.27,41.59,1.8
20260520,45.85,47.7,45.3,45.45,30019647,42.08,8,41.48,41.6,1.91
20260521,45.85,46.2,45.35,45.45,15833029,42.36,7.28,41.66,41.62,0.99
20260522,46,46.7,45.65,46.4,15829848,42.7,8.66,41.98,41.64,0.98
20260525,47.2,47.8,46.2,46.2,21032552,42.99,7.46,42.29,41.66,1.26
20260526,46.5,46.95,44.35,44.35,15432709,43.11,2.89,42.52,41.64,0.9
20260527,44.55,45.8,44,44.65,13857095,43.23,3.27,42.77,41.63,0.78
20260528,45,45.5,43.8,43.9,9042819,43.29,1.41,42.97,41.62,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.48
- over_600_ratio: 37.27
- over_800_ratio: 35.43
- over_1000_ratio: 34.18
- over_400_change_1w: -1.22
- over_800_change_1w: -1.53
- over_1000_change_1w: -1.41
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.17,,36.2,,35.18,,0,False,False
20260508,40.51,0.34,36.59,0.39,35.45,0.27,1,True,True
20260515,40.7,0.19,36.96,0.37,35.59,0.14,2,True,True
20260522,39.48,-1.22,35.43,-1.53,34.18,-1.41,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2498 | 宏達電 | pattern | 型態觀察 | 51.0 |  |  | base_building |  | no_signal | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 2498 | 宏達電 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | no_signal | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2498 | 宏達電 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2498 | 宏達電 | 93 | 10 | 6071670.0 | 21400.0 | 283.72 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
