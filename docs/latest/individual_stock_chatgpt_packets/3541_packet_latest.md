# INDIVIDUAL STOCK CHATGPT PACKET - 3541 西柏

## Metadata
- generated_at: 2026-05-26 23:01:21 Asia/Taipei
- stock_id: 3541
- stock_name: 西柏
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3541_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3541_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3541_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3541_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3541_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3541_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3541_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3541_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3541_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3541_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3541_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3541_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3541_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3541.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3541.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3541.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3541.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3541.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3541.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3541_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3541_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3541_latest.md?ref=main

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
- open: 22.3
- high: 22.5
- low: 22.3
- close: 22.35
- volume: 22000
- ma5: 22.68
- ema23_primary: 23.08
- distance_to_ema23_pct: -3.18
- ma20: 23.05
- ma60: 23.65
- ma120: 24.23
- return_5d: -1.97
- return_20d: -5.7
- volume_ratio: 0.33
- distance_to_ma20_pct_auxiliary: -3.04
- distance_to_high_60_pct: -13.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,23.65,23.65,23.55,23.6,92000,23.94,-1.42,23.95,24.61,1.77
20260429,23.6,23.6,23.5,23.5,71000,23.9,-1.69,23.93,24.57,1.31
20260430,23.5,23.5,23.35,23.45,77000,23.87,-1.74,23.9,24.54,1.37
20260504,23.5,23.5,23.4,23.45,80000,23.83,-1.6,23.86,24.49,1.37
20260505,23.35,23.4,23.3,23.4,50000,23.8,-1.66,23.82,24.45,0.84
20260506,23.4,23.4,23.25,23.3,103000,23.75,-1.91,23.78,24.41,1.63
20260507,23.3,23.35,23.1,23.15,153000,23.7,-2.34,23.73,24.36,2.22
20260508,23.05,23.15,23,23.15,112000,23.66,-2.15,23.68,24.31,1.57
20260511,23,23.3,22.9,23.05,117000,23.61,-2.36,23.63,24.26,1.54
20260512,23.05,23.3,22.85,23.2,52000,23.57,-1.58,23.59,24.21,0.68
20260513,22.9,23.3,22.8,23,18000,23.53,-2.23,23.55,24.16,0.24
20260514,23,23,22.8,23,65000,23.48,-2.05,23.51,24.11,0.87
20260515,22.8,22.9,22.8,22.8,84000,23.42,-2.67,23.46,24.05,1.09
20260518,22.8,22.8,22.55,22.75,52000,23.37,-2.65,23.39,23.99,0.66
20260519,22.6,22.8,22.6,22.8,11000,23.32,-2.24,23.34,23.93,0.14
20260520,22.9,23,22.9,22.95,60000,23.29,-1.46,23.29,23.88,0.8
20260521,23,23,22.7,22.9,57000,23.26,-1.54,23.23,23.82,0.79
20260522,22.9,22.9,22.8,22.9,23000,23.23,-1.41,23.19,23.77,0.33
20260525,22.5,22.55,22.3,22.3,22000,23.15,-3.67,23.12,23.71,0.32
20260526,22.3,22.5,22.3,22.35,22000,23.08,-3.18,23.05,23.65,0.33
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.94
- over_600_ratio: 33.32
- over_800_ratio: 28.54
- over_1000_ratio: 24
- over_400_change_1w: 0.25
- over_800_change_1w: 0.25
- over_1000_change_1w: 0.25
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.97,,27.57,,21.3,,0,False,False
20260508,34.4,0.43,28,0.43,23.46,2.16,1,True,True
20260515,34.69,0.29,28.29,0.29,23.75,0.29,2,True,True
20260522,34.94,0.25,28.54,0.25,24,0.25,3,True,True
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
