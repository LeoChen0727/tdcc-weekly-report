# INDIVIDUAL STOCK CHATGPT PACKET - 3317 尼克森

## Metadata
- generated_at: 2026-05-30 23:41:59 Asia/Taipei
- stock_id: 3317
- stock_name: 尼克森
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3317_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3317_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3317_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3317_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3317_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3317_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3317_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3317_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3317_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3317_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3317_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3317_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3317_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3317.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3317.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3317.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3317.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3317.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3317.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3317_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3317_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3317_latest.md?ref=main

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
- date: 20260529
- open: 85.9
- high: 86.8
- low: 83.1
- close: 83.8
- volume: 84000
- ma5: 83.26
- ema23_primary: 72.37
- distance_to_ema23_pct: 15.8
- ma20: 73.06
- ma60: 57.69
- ma120: 52.61
- return_5d: 10.12
- return_20d: 50.45
- volume_ratio: 0.01
- distance_to_ma20_pct_auxiliary: 14.7
- distance_to_high_60_pct: -4.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,56,59,55.8,58.9,4466000,53.34,10.43,53.29,49.81,1.35
20260505,58.4,63.4,57.9,62.2,10160000,54.08,15.02,53.88,49.98,2.72
20260506,62.8,65.9,61.5,64.9,12350000,54.98,18.05,54.62,50.2,2.87
20260507,66.6,70,66,66.9,11615000,55.97,19.52,55.41,50.47,2.43
20260508,66.2,66.5,62,62.2,5247000,56.49,10.11,56,50.68,1.07
20260511,64,68.4,62.6,68.2,10889000,57.47,18.68,56.88,51,2.01
20260512,67,69,66.7,67.9,6891000,58.34,16.39,57.7,51.35,1.21
20260513,67,68.6,64.9,68.3,4169000,59.17,15.44,58.56,51.7,0.71
20260514,69,74.9,69,74,12979000,60.4,22.51,59.73,52.12,2.01
20260515,75,76.1,71.7,75.3,13703000,61.64,22.15,60.94,52.58,1.93
20260518,74,77,72.8,75.8,6336000,62.82,20.65,61.99,53.07,0.88
20260519,75.8,77.8,75.3,76,7835000,63.92,18.9,63.09,53.54,1.08
20260520,76,80.4,72.3,72.5,12331000,64.64,12.17,64.03,53.96,1.58
20260521,73.2,75.7,73,75.7,4910000,65.56,15.47,65.07,54.42,0.63
20260522,75.5,77.7,75.5,76.1,77000,66.44,14.54,66.31,54.87,0.01
20260525,76.8,83.7,76.5,83.7,82000,67.88,23.31,67.73,55.45,0.01
20260526,84.2,87.7,81,83.7,84000,69.19,20.96,69.05,56.03,0.01
20260527,85.7,87.5,81.5,82.3,84000,70.29,17.09,70.3,56.56,0.01
20260528,82.9,86,80.7,82.8,84000,71.33,16.08,71.66,57.1,0.01
20260529,85.9,86.8,83.1,83.8,84000,72.37,15.8,73.06,57.69,0.01
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 30.72
- over_600_ratio: 26.52
- over_800_ratio: 24.83
- over_1000_ratio: 23.95
- over_400_change_1w: 2.62
- over_800_change_1w: 2
- over_1000_change_1w: 1.12
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.04,,23.71,,22.82,,0,False,False
20260508,28.18,1.14,22.82,-0.89,22.82,0,1,False,False
20260515,29.06,0.88,23.75,0.93,22.83,0.01,2,True,True
20260522,28.1,-0.96,22.83,-0.92,22.83,0,0,False,False
20260529,30.72,2.62,24.83,2,23.95,1.12,1,True,True
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
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
