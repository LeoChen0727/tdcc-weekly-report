# INDIVIDUAL STOCK CHATGPT PACKET - 9136 巨騰-DR

## Metadata
- generated_at: 2026-05-26 23:03:01 Asia/Taipei
- stock_id: 9136
- stock_name: 巨騰-DR
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 117
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9136_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9136_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9136_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9136_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9136_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9136_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9136_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9136_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9136_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9136_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9136_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9136_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9136_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9136.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9136.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9136.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9136.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9136.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9136.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9136_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9136_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9136_latest.md?ref=main

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
- date: 20260526
- open: 11.5
- high: 11.5
- low: 10.8
- close: 10.9
- volume: 1336325
- ma5: 10.97
- ema23_primary: 10.29
- distance_to_ema23_pct: 5.91
- ma20: 10.04
- ma60: 9.08
- ma120: 8.3
- return_5d: -6.84
- return_20d: 28.84
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: 8.54
- distance_to_high_60_pct: -22.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260401,8.7,8.71,8.52,8.7,1085510,9.32,-6.68,9.55,8.48,0.27
20260402,8.88,8.88,8.61,8.7,1086271,9.27,-6.16,9.58,8.5,0.27
20260407,8.81,8.85,8.72,8.84,643156,9.23,-4.28,9.61,8.51,0.16
20260408,8.98,9.72,8.78,9.57,1460381,9.26,3.32,9.67,8.54,0.36
20260409,9.88,9.88,8.65,8.7,1865743,9.22,-5.6,9.64,8.54,0.5
20260410,8.74,8.74,8.33,8.59,1091228,9.16,-6.26,9.62,8.55,0.35
20260413,8.59,9.2,8.59,8.99,1218188,9.15,-1.74,9.6,8.57,0.44
20260414,9.08,9.45,8.95,9.24,1293564,9.16,0.91,9.6,8.59,0.48
20260415,9.3,9.62,9.25,9.45,1846259,9.18,2.93,9.61,8.61,0.71
20260416,9.8,9.98,9.46,9.46,1342413,9.2,2.78,9.61,8.64,0.52
20260417,9.73,10.35,9.73,10.15,3516047,9.28,9.34,9.63,8.67,1.36
20260420,10.6,10.85,9.95,10.7,2928783,9.4,13.81,9.66,8.71,1.12
20260421,10.9,11.6,10.8,11.05,3012861,9.54,15.84,9.67,8.76,1.21
20260422,11.3,12.15,11.15,12.15,7094025,9.76,24.53,9.73,8.82,2.79
20260519,12,14.05,11.7,11.7,8901138,9.92,17.96,9.76,8.88,3.26
20260520,11.35,12.25,11,11,4701602,10.01,9.91,9.76,8.91,1.67
20260521,11.4,11.45,10.6,10.7,1882014,10.07,6.3,9.74,8.94,0.68
20260522,10.9,11.25,10.55,10.95,1150150,10.14,7.99,9.8,8.98,0.43
20260525,11.25,11.5,11.2,11.3,1117988,10.24,10.39,9.92,9.04,0.44
20260526,11.5,11.5,10.8,10.9,1336325,10.29,5.91,10.04,9.08,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 67.19
- over_600_ratio: 61.37
- over_800_ratio: 59.87
- over_1000_ratio: 58.01
- over_400_change_1w: 2.17
- over_800_change_1w: 2.22
- over_1000_change_1w: 1.6
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.17,,57.65,,56.41,,0,False,False
20260508,65.02,-0.15,57.65,0,56.41,0,0,False,False
20260515,65.02,0,57.65,0,56.41,0,0,False,False
20260522,67.19,2.17,59.87,2.22,58.01,1.6,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 9136 | 巨騰-DR | pattern | 型態觀察 |  |  |  | 預備發動型 |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 9136 | 巨騰-DR | 4 | 4 | 4 | 4 | 4 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
