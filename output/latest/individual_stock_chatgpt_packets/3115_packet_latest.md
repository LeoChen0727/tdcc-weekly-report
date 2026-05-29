# INDIVIDUAL STOCK CHATGPT PACKET - 3115 富榮綱

## Metadata
- generated_at: 2026-05-29 19:32:26 Asia/Taipei
- stock_id: 3115
- stock_name: 富榮綱
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3115_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3115_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3115_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3115_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3115_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3115_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3115_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3115_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3115_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3115_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3115_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3115_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3115_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3115.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3115.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3115.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3115.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3115.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3115.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3115_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3115_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3115_latest.md?ref=main

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
- open: 7.75
- high: 8.29
- low: 7.75
- close: 8.29
- volume: 8000
- ma5: 7.99
- ema23_primary: 8.91
- distance_to_ema23_pct: -6.94
- ma20: 9.01
- ma60: 9.57
- ma120: 10.01
- return_5d: 1.72
- return_20d: -17.1
- volume_ratio: 0.35
- distance_to_ma20_pct_auxiliary: -8.01
- distance_to_high_60_pct: -25.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,9.62,9.62,9.44,9.5,47000,9.93,-4.28,9.84,9.98,1.46
20260505,9.5,10,9.45,9.76,41000,9.91,-1.53,9.85,9.97,1.23
20260506,9.76,9.76,9.76,9.76,2000,9.9,-1.4,9.86,9.96,0.06
20260507,9.7,9.87,9.51,9.75,8000,9.89,-1.38,9.88,9.95,0.24
20260508,9.7,9.7,9.66,9.66,7000,9.87,-2.1,9.89,9.94,0.21
20260511,9.66,9.89,9.66,9.87,28000,9.87,0.02,9.91,9.93,0.82
20260512,9.99,9.99,9.33,9.59,19000,9.84,-2.59,9.91,9.92,0.55
20260513,9.36,9.65,9.36,9.59,4000,9.82,-2.38,9.9,9.9,0.12
20260514,9.4,9.68,9.4,9.4,9000,9.79,-3.97,9.89,9.88,0.27
20260515,9.33,9.38,9.25,9.37,30000,9.75,-3.93,9.88,9.86,1.05
20260518,9.37,9.37,9.37,9.37,2000,9.72,-3.61,9.88,9.85,0.09
20260519,9.2,9.2,8.5,9.2,125000,9.68,-4.94,9.87,9.83,4.34
20260520,8.59,8.81,8.59,8.68,37000,9.59,-9.53,9.78,9.8,1.36
20260521,8.84,8.84,8.41,8.63,44000,9.51,-9.29,9.66,9.78,1.83
20260522,8.7,8.7,8.15,8.15,8000,9.4,-13.3,9.56,9.75,0.37
20260525,8.15,8.17,7.9,7.94,8000,9.28,-14.43,9.44,9.71,0.36
20260526,8,8,7.8,7.92,8000,9.17,-13.59,9.32,9.68,0.36
20260527,7.75,7.92,7.6,7.8,8000,9.05,-13.83,9.2,9.64,0.36
20260528,7.55,8.1,7.55,8,8000,8.96,-10.76,9.1,9.6,0.36
20260529,7.75,8.29,7.75,8.29,8000,8.91,-6.94,9.01,9.57,0.35
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.25
- over_600_ratio: 86.25
- over_800_ratio: 85.38
- over_1000_ratio: 85.38
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,86.25,,85.38,,85.38,,0,False,False
20260508,86.25,0,85.38,0,85.38,0,0,False,False
20260515,86.25,0,85.38,0,85.38,0,0,False,False
20260522,86.25,0,85.38,0,85.38,0,0,False,False
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
