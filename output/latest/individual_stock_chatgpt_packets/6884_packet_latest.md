# INDIVIDUAL STOCK CHATGPT PACKET - 6884 海柏特

## Metadata
- generated_at: 2026-05-26 23:02:36 Asia/Taipei
- stock_id: 6884
- stock_name: 海柏特
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 102
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6884_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6884_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6884_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6884_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6884_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6884_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6884_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6884_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6884_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6884_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6884_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6884_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6884_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6884.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6884.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6884.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6884.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6884.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6884.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6884_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6884_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6884_latest.md?ref=main

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
- open: 33.1
- high: 33.35
- low: 33.1
- close: 33.35
- volume: 33000
- ma5: 33.14
- ema23_primary: 33.87
- distance_to_ema23_pct: -1.52
- ma20: 33.98
- ma60: 34.5
- ma120: 35.52
- return_5d: -0.3
- return_20d: -5.26
- volume_ratio: 1.83
- distance_to_ma20_pct_auxiliary: -1.84
- distance_to_high_60_pct: -9.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,36.1,36.1,35.2,35.2,31000,34.86,0.96,34.66,35.15,2.33
20260429,36.05,36.05,35.05,35.45,8000,34.91,1.54,34.7,35.13,0.62
20260430,35.4,35.4,34.55,34.55,6000,34.88,-0.95,34.7,35.09,0.46
20260504,34.25,35.05,34,34.95,43000,34.89,0.18,34.7,35.06,2.9
20260505,34.3,34.8,34.3,34.7,8000,34.87,-0.49,34.72,35.03,0.54
20260506,34.3,34.65,34,34.65,8000,34.85,-0.58,34.75,35.01,0.54
20260507,34.1,34.35,34,34,15000,34.78,-2.25,34.74,34.98,1
20260508,34.5,34.6,34,34.4,13000,34.75,-1.01,34.76,34.95,0.83
20260511,34.4,34.4,33.9,33.9,17000,34.68,-2.25,34.77,34.9,1.05
20260512,33.4,34.2,33.35,33.45,14000,34.58,-3.26,34.76,34.88,0.87
20260513,34.1,34.35,34.1,34.35,3000,34.56,-0.6,34.76,34.87,0.19
20260514,33.9,33.9,33.2,33.7,23000,34.49,-2.28,34.74,34.85,1.42
20260515,33.7,33.7,33.4,33.6,8000,34.41,-2.36,34.68,34.83,0.51
20260518,33.65,33.65,33.05,33.45,20000,34.33,-2.57,34.6,34.76,1.23
20260519,33.3,33.5,33.3,33.45,7000,34.26,-2.36,34.52,34.71,0.43
20260520,33.05,33.4,33,33.1,14000,34.16,-3.11,34.41,34.67,0.86
20260521,33.15,33.4,33,33.35,23000,34.09,-2.18,34.31,34.62,1.41
20260522,33.05,33.75,32.8,32.8,33000,33.99,-3.49,34.17,34.57,2.01
20260525,33.35,33.35,33.1,33.1,33000,33.91,-2.4,34.07,34.53,1.92
20260526,33.1,33.35,33.1,33.35,33000,33.87,-1.52,33.98,34.5,1.83
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.85
- over_600_ratio: 81.85
- over_800_ratio: 78.05
- over_1000_ratio: 78.05
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
20260430,81.85,,78.05,,78.05,,0,False,False
20260508,81.85,0,78.05,0,78.05,0,0,False,False
20260515,81.85,0,78.05,0,78.05,0,0,False,False
20260522,81.85,0,78.05,0,78.05,0,0,False,False
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
