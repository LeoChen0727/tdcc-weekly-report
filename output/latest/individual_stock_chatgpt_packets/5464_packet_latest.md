# INDIVIDUAL STOCK CHATGPT PACKET - 5464 霖宏

## Metadata
- generated_at: 2026-05-30 23:42:42 Asia/Taipei
- stock_id: 5464
- stock_name: 霖宏
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5464_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5464_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5464.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5464.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5464.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5464.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5464_latest.md?ref=main

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
- open: 77
- high: 83
- low: 75.6
- close: 83
- volume: 82000
- ma5: 74.96
- ema23_primary: 60.22
- distance_to_ema23_pct: 37.83
- ma20: 61.14
- ma60: 39.7
- ma120: 32.82
- return_5d: 16.9
- return_20d: 151.52
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 35.75
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.7,36.3,33.65,35.9,3684000,30.85,16.36,30.71,28.24,6.76
20260505,37,39.45,37,39.45,5772000,31.57,24.96,31.28,28.46,6.98
20260506,43.35,43.35,43.35,43.35,1410000,32.55,33.17,32.03,28.75,1.58
20260507,47.65,47.65,47.65,47.65,1583000,33.81,40.93,32.99,29.12,1.67
20260508,52.4,52.4,50.4,52.4,7811000,35.36,48.19,34.19,29.57,5.86
20260511,52.6,57.6,50.5,57.6,2645000,37.21,54.79,35.62,30.11,1.81
20260512,62.9,63.3,62.9,63.3,1018000,39.39,60.71,37.29,30.74,0.68
20260513,68.7,68.7,62,62,2514000,41.27,50.23,38.91,31.36,1.57
20260514,61.5,64,59,59.5,1355000,42.79,39.05,40.4,31.93,0.82
20260515,60.2,60.2,53.6,57.1,1402000,43.98,29.82,41.77,32.45,0.82
20260518,53.8,61.1,53.8,57.3,968000,45.09,27.07,43.13,32.97,0.55
20260519,57.4,62.9,55.8,62.5,834000,46.54,34.28,44.67,33.57,0.48
20260520,68,68,62.7,67.5,901000,48.29,39.78,46.42,34.26,0.51
20260521,68,72,68,71.5,718000,50.22,42.36,48.36,35.02,0.4
20260522,71.5,72,70,71,71000,51.95,36.66,50.33,35.75,0.04
20260525,71.5,75,71.5,73,73000,53.71,35.92,52.43,36.51,0.04
20260526,73,73,69.8,72.2,71000,55.25,30.68,54.49,37.26,0.04
20260527,73.1,73.1,71.1,71.1,72000,56.57,25.68,56.46,37.98,0.04
20260528,70,78.2,69,75.5,77000,58.15,29.84,58.64,38.78,0.05
20260529,77,83,75.6,83,82000,60.22,37.83,61.14,39.7,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 71.79
- over_600_ratio: 67.25
- over_800_ratio: 63.42
- over_1000_ratio: 55.61
- over_400_change_1w: 0.2
- over_800_change_1w: -0.69
- over_1000_change_1w: -0.63
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.27,,58.64,,52.07,,0,False,False
20260508,66.57,4.3,63.43,4.79,54.28,2.21,1,True,True
20260515,69.73,3.16,64.61,1.18,58.05,3.77,2,True,True
20260522,71.59,1.86,64.11,-0.5,56.24,-1.81,3,False,False
20260529,71.79,0.2,63.42,-0.69,55.61,-0.63,4,False,False
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
