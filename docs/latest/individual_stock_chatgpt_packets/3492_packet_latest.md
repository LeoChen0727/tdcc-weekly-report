# INDIVIDUAL STOCK CHATGPT PACKET - 3492 長盛

## Metadata
- generated_at: 2026-05-27 21:27:08 Asia/Taipei
- stock_id: 3492
- stock_name: 長盛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3492_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3492_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3492_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3492_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3492_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3492_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3492_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3492_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3492_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3492_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3492_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3492_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3492_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3492.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3492.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3492.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3492.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3492.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3492.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3492_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3492_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3492_latest.md?ref=main

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
- date: 20260527
- open: 23.4
- high: 23.4
- low: 22.55
- close: 22.8
- volume: 23000
- ma5: 22.65
- ema23_primary: 22.73
- distance_to_ema23_pct: 0.31
- ma20: 22.57
- ma60: 23.37
- ma120: 24.58
- return_5d: 3.4
- return_20d: 0.44
- volume_ratio: 0.41
- distance_to_ma20_pct_auxiliary: 1.03
- distance_to_high_60_pct: -13.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,22.8,22.95,22.8,22.9,36000,23.5,-2.57,23.55,24.1,0.32
20260430,22.85,22.85,22.45,22.55,55000,23.42,-3.73,23.53,24.06,0.5
20260504,22.35,22.65,22.35,22.55,100000,23.35,-3.43,23.49,24.01,0.89
20260505,22.4,22.55,22.4,22.5,76000,23.28,-3.35,23.4,23.93,0.94
20260506,22.65,22.65,22.2,22.4,74000,23.21,-3.48,23.31,23.86,0.98
20260507,22.45,23.55,22.45,22.9,97000,23.18,-1.21,23.23,23.8,1.27
20260508,23.05,23.55,22.75,22.75,83000,23.15,-1.71,23.17,23.76,1.08
20260511,22.85,23,22.75,22.9,33000,23.12,-0.97,23.13,23.72,0.43
20260512,22.85,22.85,22.6,22.65,74000,23.09,-1.89,23.07,23.69,0.97
20260513,22.65,22.95,22.6,22.9,65000,23.07,-0.74,23.03,23.66,0.86
20260514,22.8,22.8,22.6,22.6,65000,23.03,-1.87,22.97,23.61,0.84
20260515,22.7,22.7,22.25,22.25,70000,22.97,-3.12,22.9,23.57,0.92
20260518,22.5,22.5,22.1,22.15,44000,22.9,-3.26,22.82,23.52,0.58
20260519,22.05,22.15,21.9,22.05,75000,22.83,-3.4,22.75,23.5,0.99
20260520,22.05,22.05,22,22.05,71000,22.76,-3.13,22.66,23.47,0.94
20260521,22.5,22.5,22.3,22.4,25000,22.73,-1.46,22.6,23.45,0.35
20260522,22.4,22.75,22.05,22.6,22000,22.72,-0.53,22.57,23.43,0.36
20260525,22.65,22.9,22.55,22.55,23000,22.71,-0.69,22.54,23.41,0.38
20260526,22.55,23.25,22.45,22.9,23000,22.72,0.78,22.56,23.39,0.39
20260527,23.4,23.4,22.55,22.8,23000,22.73,0.31,22.57,23.37,0.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.19
- over_600_ratio: 44.69
- over_800_ratio: 44.69
- over_1000_ratio: 44.69
- over_400_change_1w: 1.14
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.05,,44.69,,44.69,,0,False,False
20260508,47.05,0,44.69,0,44.69,0,0,False,False
20260515,47.05,0,44.69,0,44.69,0,0,False,False
20260522,48.19,1.14,44.69,0,44.69,0,1,False,False
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
