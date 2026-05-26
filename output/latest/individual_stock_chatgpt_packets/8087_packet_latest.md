# INDIVIDUAL STOCK CHATGPT PACKET - 8087 麗升能源

## Metadata
- generated_at: 2026-05-26 22:20:43 Asia/Taipei
- stock_id: 8087
- stock_name: 麗升能源
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8087_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8087_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8087_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8087_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8087_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8087_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8087_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8087_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8087_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8087_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8087_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8087_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8087_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8087.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8087.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8087.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8087.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8087.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8087.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8087_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8087_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8087_latest.md?ref=main

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
- open: 32.8
- high: 32.95
- low: 32.3
- close: 32.95
- volume: 33000
- ma5: 33.61
- ema23_primary: 33.78
- distance_to_ema23_pct: -2.46
- ma20: 33.57
- ma60: 34.19
- ma120: 33.21
- return_5d: -3.94
- return_20d: -2.51
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: -1.85
- distance_to_high_60_pct: -18.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,33,33.95,33,33,62000,34.3,-3.78,34.38,32.95,1.19
20260429,33.2,33.2,33.2,33.2,12000,34.2,-2.94,34.34,33,0.23
20260430,33.2,34.15,33.1,33.85,37000,34.18,-0.95,34.43,33.07,0.7
20260504,33.2,33.85,32.9,32.9,43000,34.07,-3.43,34.4,33.11,0.79
20260505,33,33.8,32.7,33.3,59000,34,-2.07,34.4,33.15,1.05
20260506,33,33.6,32.9,33.1,63000,33.93,-2.44,34.38,33.21,1.07
20260507,33,33.1,32.85,32.85,50000,33.84,-2.92,34.32,33.26,0.84
20260508,32.85,34.95,32.8,33,52000,33.77,-2.28,34.28,33.32,0.85
20260511,35.5,36.3,34,34,281000,33.79,0.63,34.33,33.4,3.98
20260512,33.7,33.7,31.25,33.2,142000,33.74,-1.6,34.18,33.47,1.91
20260513,33,33.2,32.85,33,54000,33.68,-2.01,33.96,33.54,0.86
20260514,33,36.3,33,35.35,417000,33.82,4.53,33.93,33.65,5.27
20260515,34.3,35.5,34.1,34.1,99000,33.84,0.77,33.84,33.73,1.2
20260518,37,37,34,34.25,122000,33.88,1.11,33.77,33.84,1.39
20260519,35.7,35.7,34.2,34.3,77000,33.91,1.15,33.76,33.96,0.85
20260520,34.15,34.7,34.15,34.3,39000,33.94,1.05,33.73,34.11,0.43
20260521,34.3,36.5,34.15,34.15,58000,33.96,0.56,33.69,34.22,0.63
20260522,34.2,34.2,33.2,33.85,34000,33.95,-0.3,33.68,34.27,0.37
20260525,33.9,33.9,32.6,32.8,33000,33.86,-3.12,33.62,34.26,0.36
20260526,32.8,32.95,32.3,32.95,33000,33.78,-2.46,33.57,34.19,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.12
- over_600_ratio: 49.34
- over_800_ratio: 43.88
- over_1000_ratio: 43.88
- over_400_change_1w: -0.17
- over_800_change_1w: -2.06
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.38,,46.07,,46.07,,0,False,False
20260508,58.3,-0.08,45.97,-0.1,45.97,-0.1,0,False,False
20260515,58.29,-0.01,45.94,-0.03,43.62,-2.35,0,False,False
20260522,58.12,-0.17,43.88,-2.06,43.88,0.26,1,False,True
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
