# INDIVIDUAL STOCK CHATGPT PACKET - 7709 榮田

## Metadata
- generated_at: 2026-05-30 23:43:42 Asia/Taipei
- stock_id: 7709
- stock_name: 榮田
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 266
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7709_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7709_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7709_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7709_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7709_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7709_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7709_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7709_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7709_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7709_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7709_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7709_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7709_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7709.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7709.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7709.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7709.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7709.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7709.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7709_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7709_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7709_latest.md?ref=main

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
- open: 110.5
- high: 110.5
- low: 110.5
- close: 110.5
- volume: 110000
- ma5: 97.12
- ema23_primary: 87.09
- distance_to_ema23_pct: 26.88
- ma20: 87.19
- ma60: 72.64
- ma120: 59.1
- return_5d: 21.96
- return_20d: 59.68
- volume_ratio: 0.16
- distance_to_ma20_pct_auxiliary: 26.73
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,76.1,76.1,76.1,76.1,133000,70.99,7.19,73.32,64.15,0.2
20260505,83.7,83.7,82.8,83.7,553000,72.05,16.16,74.09,64.72,0.92
20260506,88,89.2,79,80.3,1469000,72.74,10.39,74.74,65.19,2.31
20260507,83.7,88.3,81.8,88.3,1118000,74.04,19.27,75.45,65.78,1.77
20260508,88.3,96.5,84.2,84.2,1878000,74.88,12.44,75.96,66.22,2.9
20260511,88.6,88.6,81.9,82.8,612000,75.54,9.61,76.47,66.55,0.95
20260512,84.6,84.6,80.7,82,348000,76.08,7.78,76.86,66.94,0.57
20260513,81.5,81.5,78.3,78.9,283000,76.32,3.39,76.98,67.28,0.48
20260514,81.3,81.3,76.5,77.4,310000,76.41,1.3,76.89,67.51,0.55
20260515,78,79,76.1,76.2,258000,76.39,-0.25,77,67.61,0.48
20260518,76,83.8,72.8,83.8,676000,77.01,8.82,77.55,67.83,1.22
20260519,91,92.1,90.2,92.1,468000,78.26,17.68,78.3,68.23,0.84
20260520,101,101,88.8,89,2764000,79.16,12.43,78.86,68.63,4.12
20260521,97.8,97.9,92.8,92.9,1953000,80.3,15.68,79.53,69.19,2.68
20260522,92,94.8,89.1,90.6,92000,81.16,11.63,80.4,69.66,0.13
20260525,92,93.1,90.6,91.1,92000,81.99,11.11,81.43,70.12,0.13
20260526,91.3,93.7,90.3,91.7,92000,82.8,10.75,82.53,70.61,0.14
20260527,93.3,93.3,90.8,91.8,91000,83.55,9.87,83.56,71.11,0.14
20260528,94.5,100.5,94.5,100.5,99000,84.96,18.29,85.13,71.77,0.15
20260529,110.5,110.5,110.5,110.5,110000,87.09,26.88,87.19,72.64,0.16
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 80.75
- over_600_ratio: 79.48
- over_800_ratio: 77.44
- over_1000_ratio: 77.44
- over_400_change_1w: 1.27
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.49,,77.45,,77.45,,0,False,False
20260508,79.48,-0.01,77.44,-0.01,77.44,-0.01,0,False,False
20260515,79.48,0,77.44,0,77.44,0,0,False,False
20260522,79.48,0,77.44,0,77.44,0,0,False,False
20260529,80.75,1.27,77.44,0,77.44,0,1,False,False
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
