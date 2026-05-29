# INDIVIDUAL STOCK CHATGPT PACKET - 3707 漢磊

## Metadata
- generated_at: 2026-05-29 19:32:44 Asia/Taipei
- stock_id: 3707
- stock_name: 漢磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3707_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3707_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3707_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3707_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3707_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3707_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3707_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3707_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3707_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3707_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3707_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3707_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3707_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3707.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3707.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3707.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3707.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3707.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3707.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3707_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3707_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3707_latest.md?ref=main

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
- open: 91.4
- high: 93.1
- low: 87.2
- close: 89.3
- volume: 89000
- ma5: 86.86
- ema23_primary: 76.91
- distance_to_ema23_pct: 16.12
- ma20: 78.53
- ma60: 63.45
- ma120: 59.08
- return_5d: 6.95
- return_20d: 34.89
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: 13.71
- distance_to_high_60_pct: -7.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,67.2,72.8,65.6,68.7,52700000,58.32,17.8,56.43,56.76,4.72
20260505,69.7,75.5,69.6,75.5,29436000,59.75,26.35,57.79,56.92,2.35
20260506,77.6,80.3,72.6,73.1,65819000,60.86,20.1,58.99,57.04,4.18
20260507,73.2,80,71.4,74.7,43956000,62.02,20.45,60.2,57.21,2.46
20260508,73.3,75.8,68.7,73.2,26115000,62.95,16.28,61.35,57.42,1.37
20260511,74,76.4,71.5,74.9,25790000,63.95,17.13,62.56,57.67,1.28
20260512,74.7,78.4,72.7,77.2,22730000,65.05,18.68,63.87,57.99,1.07
20260513,75.5,76.3,72.1,72.8,17437000,65.7,10.81,64.69,58.26,0.8
20260514,74.3,80,74.3,80,37627000,66.89,19.6,65.97,58.64,1.64
20260515,85,87.5,79.2,80.4,50558000,68.01,18.21,67.25,59.06,2
20260518,78,78.5,73.4,76.8,20664000,68.75,11.72,68.28,59.47,0.8
20260519,75.5,77.2,71.4,72.7,14687000,69.08,5.25,69.02,59.79,0.56
20260520,73,74.8,71.4,72.8,9458000,69.39,4.92,69.7,60.1,0.36
20260521,76,80,75.6,80,18148000,70.27,13.85,70.56,60.56,0.69
20260522,81,85.8,80.5,83.5,83000,71.37,16.99,71.84,61.05,0
20260525,85.7,88.4,84.7,85.7,87000,72.57,18.1,73.34,61.54,0
20260526,89.8,93.4,81.7,82.9,85000,73.43,12.9,74.67,61.99,0
20260527,85,90.5,82.4,89.3,88000,74.75,19.46,76.03,62.46,0
20260528,88.6,96.9,86.2,87.1,91000,75.78,14.94,77.38,62.92,0
20260529,91.4,93.1,87.2,89.3,89000,76.91,16.12,78.53,63.45,0
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 53.17
- over_600_ratio: 52.45
- over_800_ratio: 51.37
- over_1000_ratio: 50.72
- over_400_change_1w: 0.5
- over_800_change_1w: 0.21
- over_1000_change_1w: 0.68
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.3,,44.99,,43.85,,0,False,False
20260508,48.13,0.83,46.13,1.14,45.43,1.58,1,True,True
20260515,52.67,4.54,51.16,5.03,50.04,4.61,2,True,True
20260522,53.17,0.5,51.37,0.21,50.72,0.68,3,True,True
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
