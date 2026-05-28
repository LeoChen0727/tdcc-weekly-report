# INDIVIDUAL STOCK CHATGPT PACKET - 1504 東元

## Metadata
- generated_at: 2026-05-28 19:31:33 Asia/Taipei
- stock_id: 1504
- stock_name: 東元
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1504_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1504_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1504_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1504_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1504_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1504_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1504_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1504_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1504_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1504_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1504_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1504_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1504_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1504.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1504.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1504.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1504.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1504.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1504.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1504_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1504_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1504_latest.md?ref=main

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
- open: 71.8
- high: 73.9
- low: 70.8
- close: 70.9
- volume: 21294048
- ma5: 71.66
- ema23_primary: 69.43
- distance_to_ema23_pct: 2.12
- ma20: 70.42
- ma60: 66.88
- ma120: 75.86
- return_5d: -0.28
- return_20d: 13.99
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: 0.69
- distance_to_high_60_pct: -12.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,65.5,65.8,62.2,62.4,24879960,63.02,-0.99,61.47,70.58,2.62
20260504,63.2,68.6,62.8,68.6,20779655,63.49,8.05,61.78,70.24,2.03
20260505,70.3,71.9,68,68.5,55282925,63.91,7.19,62.17,69.93,4.32
20260506,68.2,69.3,67.1,67.3,21955194,64.19,4.85,62.6,69.62,1.64
20260507,67.9,74,67.9,74,43629834,65.01,13.84,63.28,69.4,2.88
20260508,74.6,74.7,70.5,72.8,40799820,65.66,10.88,63.95,69.2,2.45
20260511,73.6,73.8,71.7,72.6,14702877,66.23,9.61,64.59,69.05,0.86
20260512,73.1,73.8,71.6,72.5,12274433,66.76,8.6,65.2,68.94,0.71
20260513,71.5,73.7,71,73.2,14470026,67.29,8.78,65.78,68.8,0.83
20260514,74.1,76.4,72,72.4,20939726,67.72,6.91,66.28,68.62,1.17
20260515,72.7,73.7,69.1,69.4,18945422,67.86,2.27,66.59,68.45,1.03
20260518,68.8,68.8,66.4,68.3,9629016,67.9,0.6,66.86,68.26,0.52
20260519,68.7,68.9,67.6,67.9,7140992,67.9,0.01,67.17,68.05,0.39
20260520,68,69.3,67.3,69,7836158,67.99,1.49,67.44,67.88,0.43
20260521,69.6,71.5,69.6,71.1,9713043,68.25,4.18,67.83,67.74,0.53
20260522,71.5,72.9,71,72.1,16736712,68.57,5.15,68.36,67.57,0.9
20260525,73.3,73.3,71.6,72,12898044,68.85,4.57,68.92,67.41,0.68
20260526,72.9,74.5,72.5,72.5,19404441,69.16,4.83,69.49,67.24,0.99
20260527,73,74.9,70.8,70.8,24989267,69.3,2.17,69.98,67.04,1.23
20260528,71.8,73.9,70.8,70.9,21294048,69.43,2.12,70.42,66.88,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 73.5
- over_600_ratio: 72.04
- over_800_ratio: 71.04
- over_1000_ratio: 70.2
- over_400_change_1w: -0.05
- over_800_change_1w: 0.13
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.34,,71.97,,70.98,,0,False,False
20260508,73.97,-0.37,71.53,-0.44,70.69,-0.29,0,False,False
20260515,73.55,-0.42,70.91,-0.62,70.11,-0.58,0,False,False
20260522,73.5,-0.05,71.04,0.13,70.2,0.09,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1504 | 東元 | pattern | 型態觀察 | 54.0 |  |  | pullback_right_side |  | call_inflow | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 1504 | 東元 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | call_inflow | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1504 | 東元 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1504 | 東元 | 88 | 4 | 9688690.0 | 0.0 |  | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
