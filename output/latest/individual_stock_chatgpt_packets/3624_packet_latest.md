# INDIVIDUAL STOCK CHATGPT PACKET - 3624 光頡

## Metadata
- generated_at: 2026-05-30 23:42:10 Asia/Taipei
- stock_id: 3624
- stock_name: 光頡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3624_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3624_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3624_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3624_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3624_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3624_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3624_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3624_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3624_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3624_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3624_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3624_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3624_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3624.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3624.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3624.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3624.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3624.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3624.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3624_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3624_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3624_latest.md?ref=main

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
- open: 107
- high: 110
- low: 99.7
- close: 110
- volume: 106000
- ma5: 98.3
- ema23_primary: 80.25
- distance_to_ema23_pct: 37.07
- ma20: 78.22
- ma60: 60.22
- ma120: 58.45
- return_5d: 20.22
- return_20d: 116.54
- volume_ratio: 0.01
- distance_to_ma20_pct_auxiliary: 40.64
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,51.9,53.7,51.4,52.4,869000,52.15,0.48,51.96,53.42,0.41
20260505,52.1,55,52.1,54.7,1433000,52.36,4.47,52.42,53.28,0.66
20260506,55.5,56.4,53.2,54,1880000,52.5,2.86,52.84,53.14,0.84
20260507,55.1,59.4,54.1,59.4,9424000,53.07,11.92,53.42,53.11,3.51
20260508,57.8,63.4,57.5,59,10984000,53.57,10.14,53.98,53.13,3.44
20260511,60.9,63.3,57.1,63,7811000,54.35,15.91,54.65,53.23,2.25
20260512,63.1,68.3,61.5,66.3,14345000,55.35,19.79,55.36,53.41,3.55
20260513,65.2,68.3,61.4,66.6,11617000,56.29,18.32,56.05,53.6,2.61
20260514,72.9,73.2,72.6,73.2,6050000,57.7,26.87,56.96,53.86,1.34
20260515,74.1,80.5,71.4,76.2,33224000,59.24,28.63,57.97,54.24,5.64
20260518,80.7,83.8,76.3,83.8,24847000,61.28,36.74,59.31,54.77,3.59
20260519,83.4,92.1,78.9,91.2,40774000,63.78,43,61,55.4,4.67
20260520,90,100,89.9,90,59377000,65.96,36.44,62.67,56.01,5.12
20260521,91.9,95.7,89,91.5,6282000,68.09,34.38,64.46,56.65,0.53
20260522,91.7,92.8,89,91.5,91000,70.04,30.64,66.44,57.22,0.01
20260525,95,95,92,94,94000,72.04,30.49,68.63,57.74,0.01
20260526,94,94,84.6,93.5,88000,73.83,26.65,70.81,58.22,0.01
20260527,94.5,97.4,89,94,94000,75.51,24.49,72.87,58.73,0.01
20260528,95,103,95,100,100000,77.55,28.95,75.25,59.37,0.01
20260529,107,110,99.7,110,106000,80.25,37.07,78.22,60.22,0.01
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 61.9
- over_600_ratio: 59.37
- over_800_ratio: 55.75
- over_1000_ratio: 53.49
- over_400_change_1w: 0.88
- over_800_change_1w: -1.49
- over_1000_change_1w: -0.59
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.62,,45.62,,43.34,,0,False,False
20260508,49.91,1.29,47.2,1.58,43.4,0.06,1,True,True
20260515,58.62,8.71,53.17,5.97,49.22,5.82,2,True,True
20260522,61.02,2.4,57.24,4.07,54.08,4.86,3,True,True
20260529,61.9,0.88,55.75,-1.49,53.49,-0.59,4,False,False
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
