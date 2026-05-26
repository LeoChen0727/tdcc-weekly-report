# INDIVIDUAL STOCK CHATGPT PACKET - 6205 詮欣

## Metadata
- generated_at: 2026-05-26 23:02:10 Asia/Taipei
- stock_id: 6205
- stock_name: 詮欣
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6205_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6205_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6205_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6205_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6205_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6205_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6205_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6205_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6205_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6205_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6205_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6205_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6205_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6205.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6205.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6205.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6205.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6205.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6205.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6205_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6205_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6205_latest.md?ref=main

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
- open: 86.5
- high: 86.5
- low: 81.6
- close: 83
- volume: 2959434
- ma5: 80.82
- ema23_primary: 80.09
- distance_to_ema23_pct: 3.63
- ma20: 84.33
- ma60: 68.54
- ma120: 58.66
- return_5d: 12.47
- return_20d: 5.33
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: -1.58
- distance_to_high_60_pct: -20.57

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,79.4,84.8,77.2,83.4,5088034,69.99,19.16,67.5,58.36,1.07
20260429,83.4,91.7,82.7,91.7,17534864,71.8,27.71,69.36,58.92,3.13
20260430,91.7,99.6,84.8,86.5,25282851,73.03,18.45,71.15,59.4,3.72
20260504,86.1,95,83.8,94.5,11444091,74.82,26.31,73.19,60.04,1.56
20260505,93.2,103,92.7,98.2,17694339,76.76,27.92,75.52,60.75,2.16
20260506,103,104.5,91.7,94.1,15877388,78.21,20.32,77.63,61.4,1.78
20260507,94.1,94.1,88.6,90.7,7825379,79.25,14.45,79.44,61.98,0.84
20260508,90.7,91.2,84.3,84.9,4844701,79.72,6.5,80.83,62.51,0.51
20260511,83.2,87.5,81,86.1,3335931,80.25,7.29,82.3,63.1,0.35
20260512,86.2,87.6,83.7,85.9,2463930,80.72,6.41,83.47,63.68,0.26
20260513,85.1,86,79,80.4,3270874,80.7,-0.37,84.07,64.17,0.35
20260514,81.2,83.5,78.6,79.3,2156279,80.58,-1.59,84.58,64.62,0.23
20260515,81.3,82,75.8,76.8,2030499,80.26,-4.32,85.02,65.07,0.22
20260518,75.4,77.1,72.5,76.2,1699918,79.93,-4.66,85.08,65.52,0.19
20260519,76.2,77.5,72.9,73.8,1687856,79.42,-7.07,84.72,65.94,0.2
20260520,73.8,74.9,72.2,72.5,1173296,78.84,-8.04,83.89,66.33,0.15
20260521,74.5,79.5,73.2,77.2,2854127,78.7,-1.91,83.39,66.81,0.39
20260522,77.8,84.9,77.2,84.9,4617635,79.22,7.17,83.7,67.39,0.64
20260525,85.5,88.5,83.2,86.5,6668759,79.83,8.36,84.12,67.98,0.92
20260526,86.5,86.5,81.6,83,2959434,80.09,3.63,84.33,68.54,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.22
- over_600_ratio: 44.13
- over_800_ratio: 41.73
- over_1000_ratio: 40.71
- over_400_change_1w: -0.99
- over_800_change_1w: 0.98
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.1,,46.38,,44.04,,0,False,False
20260508,48.56,-6.54,40.74,-5.64,40.74,-3.3,0,False,False
20260515,48.21,-0.35,40.75,0.01,40.75,0.01,1,False,True
20260522,47.22,-0.99,41.73,0.98,40.71,-0.04,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6205 | 詮欣 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6205 | 詮欣 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
