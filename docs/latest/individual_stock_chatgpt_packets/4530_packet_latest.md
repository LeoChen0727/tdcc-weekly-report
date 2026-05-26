# INDIVIDUAL STOCK CHATGPT PACKET - 4530 宏易

## Metadata
- generated_at: 2026-05-26 22:19:29 Asia/Taipei
- stock_id: 4530
- stock_name: 宏易
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 124
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4530_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4530_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4530_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4530_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4530_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4530_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4530_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4530_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4530_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4530_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4530_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4530_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4530_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4530.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4530.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4530.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4530.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4530.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4530.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4530_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4530_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4530_latest.md?ref=main

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
- open: 24.5
- high: 25.5
- low: 24.3
- close: 25.5
- volume: 25000
- ma5: 25.39
- ema23_primary: 26.08
- distance_to_ema23_pct: -2.21
- ma20: 25.73
- ma60: 27.68
- ma120: 24.06
- return_5d: 0.79
- return_20d: -7.94
- volume_ratio: 1.05
- distance_to_ma20_pct_auxiliary: -0.91
- distance_to_high_60_pct: -19.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,27.1,28,27,27.5,20000,28.26,-2.7,28.23,28.76,0.96
20260428,27.8,27.8,27.3,27.3,17000,28.18,-3.14,28.19,28.74,0.89
20260429,27.1,27.6,27.1,27.6,2000,28.14,-1.9,28.16,28.74,0.11
20260430,24.85,25.6,24.85,24.85,205000,27.86,-10.81,28,28.65,7.44
20260504,25.65,25.7,24.9,25.1,30000,27.63,-9.16,27.8,28.58,1.04
20260505,24.9,25,24.5,24.6,26000,27.38,-10.15,27.57,28.49,0.91
20260506,25.4,25.4,25.4,25.4,1000,27.21,-6.66,27.42,28.42,0.04
20260507,25.35,25.4,25.35,25.4,5000,27.06,-6.14,27.29,28.35,0.19
20260508,25,25.45,24.5,25.45,6000,26.93,-5.49,27.15,28.27,0.25
20260511,26.4,26.4,25.45,25.45,6000,26.81,-5.06,27.03,28.2,0.25
20260512,26.2,26.25,25.1,26.25,20000,26.76,-1.9,26.93,28.14,0.84
20260513,26.2,26.25,26,26,14000,26.7,-2.61,26.82,28.08,0.58
20260514,26.05,26.95,25.35,25.35,7000,26.58,-4.64,26.67,28.02,0.3
20260515,25.3,26.2,25.3,26.2,7000,26.55,-1.32,26.55,27.99,0.3
20260518,25.9,26.2,24.3,25.3,28000,26.45,-4.34,26.41,27.94,1.15
20260520,25.2,25.2,25.2,25.2,1000,26.34,-4.34,26.26,27.9,0.04
20260521,25.25,25.25,25.15,25.2,7000,26.25,-3.99,26.1,27.84,0.32
20260522,25.2,25.95,25.2,25.95,26000,26.22,-1.04,25.98,27.79,1.17
20260525,25.5,26,25.1,25.1,25000,26.13,-3.94,25.84,27.72,1.08
20260526,24.5,25.5,24.3,25.5,25000,26.08,-2.21,25.73,27.68,1.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.94
- over_600_ratio: 68.75
- over_800_ratio: 66.73
- over_1000_ratio: 64.46
- over_400_change_1w: 0.08
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,73.1,,66.73,,64.46,,0,False,False
20260508,72.85,-0.25,66.73,0,64.46,0,0,False,False
20260515,72.86,0.01,66.73,0,64.46,0,1,False,False
20260522,72.94,0.08,66.73,0,64.46,0,2,False,False
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
