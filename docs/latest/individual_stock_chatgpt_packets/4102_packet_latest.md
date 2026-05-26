# INDIVIDUAL STOCK CHATGPT PACKET - 4102 永日

## Metadata
- generated_at: 2026-05-26 23:01:29 Asia/Taipei
- stock_id: 4102
- stock_name: 永日
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4102_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4102_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4102_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4102_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4102_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4102_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4102_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4102_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4102_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4102_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4102_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4102_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4102_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4102.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4102.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4102.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4102.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4102.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4102.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4102_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4102_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4102_latest.md?ref=main

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
- open: 17.1
- high: 17.4
- low: 16.9
- close: 17.15
- volume: 17000
- ma5: 17.26
- ema23_primary: 17.74
- distance_to_ema23_pct: -3.31
- ma20: 17.61
- ma60: 18.78
- ma120: 19.5
- return_5d: -0.29
- return_20d: -8.78
- volume_ratio: 0.23
- distance_to_ma20_pct_auxiliary: -2.63
- distance_to_high_60_pct: -16.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,18.8,18.95,18.6,18.95,19000,19.14,-1.02,19.12,19.65,0.4
20260429,18.9,18.95,18.4,18.55,90000,19.1,-2.86,19.09,19.63,1.75
20260430,18.5,18.6,17.9,18.25,131000,19.02,-4.07,19.04,19.6,2.3
20260504,18.15,18.15,17.9,18,30000,18.94,-4.96,18.98,19.57,0.55
20260505,17.95,17.95,17.45,17.7,156000,18.84,-6.03,18.91,19.53,2.59
20260506,17.7,17.85,17.65,17.85,122000,18.75,-4.82,18.83,19.48,1.86
20260507,17.8,17.8,17.4,17.5,107000,18.65,-6.16,18.74,19.42,1.55
20260508,17.45,17.7,17.4,17.7,58000,18.57,-4.69,18.66,19.37,0.81
20260511,17.7,17.9,17.5,17.8,98000,18.51,-3.82,18.58,19.32,1.34
20260512,17.85,17.85,17.5,17.65,57000,18.43,-4.26,18.51,19.27,0.76
20260513,17.5,17.6,17.3,17.6,62000,18.37,-4.17,18.43,19.24,0.81
20260514,17.5,17.55,17.2,17.2,72000,18.27,-5.85,18.34,19.19,1.04
20260515,17.2,17.2,16.9,17,73000,18.16,-6.4,18.23,19.14,1.04
20260518,16.95,17.1,16.7,17,84000,18.07,-5.9,18.13,19.09,1.15
20260519,17,17.55,17,17.2,146000,17.99,-4.41,18.04,19.03,1.86
20260520,17.05,17.15,16.85,17,43000,17.91,-5.08,17.93,18.97,0.55
20260521,17,17.15,16.85,17.15,98000,17.85,-3.91,17.84,18.92,1.19
20260522,17.3,17.7,17.3,17.55,18000,17.82,-1.53,17.77,18.88,0.23
20260525,17.55,17.55,17.2,17.45,17000,17.79,-1.92,17.7,18.83,0.22
20260526,17.1,17.4,16.9,17.15,17000,17.74,-3.31,17.61,18.78,0.23
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 44.99
- over_600_ratio: 41.28
- over_800_ratio: 39.63
- over_1000_ratio: 33.25
- over_400_change_1w: -0.01
- over_800_change_1w: 0.03
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.95,,37.92,,31.24,,0,False,False
20260508,45.01,0.06,39.64,1.72,30.96,-0.28,1,False,True
20260515,45,-0.01,39.6,-0.04,33.25,2.29,2,False,True
20260522,44.99,-0.01,39.63,0.03,33.25,0,3,False,True
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
