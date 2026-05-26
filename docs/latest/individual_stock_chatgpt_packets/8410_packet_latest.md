# INDIVIDUAL STOCK CHATGPT PACKET - 8410 森田

## Metadata
- generated_at: 2026-05-26 21:26:56 Asia/Taipei
- stock_id: 8410
- stock_name: 森田
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8410_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8410_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8410_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8410_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8410_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8410_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8410_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8410_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8410_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8410_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8410_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8410_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8410_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8410.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8410.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8410.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8410.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8410.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8410.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8410_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8410_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8410_latest.md?ref=main

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
- open: 35
- high: 35.35
- low: 34.4
- close: 35.05
- volume: 35000
- ma5: 34.82
- ema23_primary: 35.77
- distance_to_ema23_pct: -2
- ma20: 35.93
- ma60: 36.44
- ma120: 36.73
- return_5d: 1.15
- return_20d: -4.1
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -2.44
- distance_to_high_60_pct: -8.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,36.9,36.9,36.15,36.6,19000,36.85,-0.67,36.65,37.08,0.64
20260429,36.65,37.1,36.65,36.95,11000,36.86,0.25,36.66,37.04,0.38
20260430,36.6,36.9,36.55,36.9,32000,36.86,0.11,36.7,37.01,1.12
20260504,36.9,36.9,36.6,36.8,17000,36.86,-0.15,36.72,36.97,0.6
20260505,36.65,36.75,36.3,36.75,24000,36.85,-0.26,36.76,36.93,0.9
20260506,36.5,36.9,36.45,36.7,11000,36.83,-0.37,36.81,36.9,0.44
20260507,36.8,36.8,36.4,36.6,29000,36.81,-0.58,36.86,36.87,1.11
20260508,36.45,36.9,36.3,36.55,24000,36.79,-0.66,36.89,36.86,0.89
20260511,36.1,36.65,36.1,36.65,16000,36.78,-0.36,36.91,36.85,0.61
20260512,36.6,36.6,36.1,36.55,57000,36.76,-0.58,36.93,36.84,2.01
20260513,36.55,36.8,36.35,36.6,52000,36.75,-0.4,36.93,36.83,1.77
20260514,36.7,36.7,35.6,36.05,93000,36.69,-1.74,36.92,36.8,2.73
20260515,35.75,35.8,35.1,35.5,70000,36.59,-2.98,36.85,36.77,2.03
20260518,35,35,34.2,34.6,83000,36.42,-5.01,36.73,36.72,2.23
20260519,34.2,34.7,34,34.65,54000,36.28,-4.49,36.56,36.67,1.47
20260520,34.15,34.65,34.15,34.65,8000,36.14,-4.13,36.38,36.62,0.22
20260521,34.4,35.2,34.4,35.15,17000,36.06,-2.52,36.25,36.58,0.47
20260522,34.3,34.9,34.3,34.5,34000,35.93,-3.98,36.12,36.53,0.93
20260525,34.5,35,34.35,34.75,35000,35.83,-3.02,36,36.48,0.95
20260526,35,35.35,34.4,35.05,35000,35.77,-2,35.93,36.44,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 59.33
- over_600_ratio: 53.78
- over_800_ratio: 53.78
- over_1000_ratio: 51.12
- over_400_change_1w: -0.19
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.7,,53.78,,51.12,,0,False,False
20260508,59.69,-0.01,53.78,0,51.12,0,0,False,False
20260515,59.52,-0.17,53.78,0,51.12,0,0,False,False
20260522,59.33,-0.19,53.78,0,51.12,0,0,False,False
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
