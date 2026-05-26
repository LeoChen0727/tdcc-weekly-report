# INDIVIDUAL STOCK CHATGPT PACKET - 4556 旭然

## Metadata
- generated_at: 2026-05-26 23:54:06 Asia/Taipei
- stock_id: 4556
- stock_name: 旭然
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4556_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4556_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4556_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4556_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4556_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4556_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4556_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4556_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4556_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4556_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4556_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4556_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4556_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4556.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4556.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4556.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4556.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4556.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4556.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4556_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4556_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4556_latest.md?ref=main

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
- open: 39.3
- high: 39.9
- low: 38.6
- close: 39.8
- volume: 39000
- ma5: 39.7
- ema23_primary: 38.61
- distance_to_ema23_pct: 3.09
- ma20: 40.12
- ma60: 32.79
- ma120: 29.24
- return_5d: 3.92
- return_20d: 6.13
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -0.8
- distance_to_high_60_pct: -16.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,38.4,38.75,34.35,37,1286000,31.71,16.7,30.43,28.95,1.76
20260429,36.8,38.35,36.35,37.4,503000,32.18,16.22,30.95,29.08,0.67
20260430,37.7,37.9,35.8,35.8,523000,32.48,10.21,31.41,29.2,0.67
20260504,36.1,36.5,35.6,35.8,315000,32.76,9.28,31.84,29.32,0.4
20260505,35.8,39.35,35.8,39.35,1573000,33.31,18.14,32.47,29.52,1.82
20260506,41.3,43.25,39.6,43.25,2324000,34.14,26.7,33.29,29.79,2.37
20260507,43.45,47.55,42.55,43.35,2470000,34.9,24.2,34.11,30.01,2.24
20260508,39.2,43.3,39.1,42.3,1163000,35.52,19.09,34.86,30.22,1
20260511,42.3,46,41.5,45.55,1093000,36.36,25.29,35.76,30.51,0.9
20260512,45.3,46.8,43.95,44.25,965000,37.01,19.55,36.62,30.79,0.77
20260513,43.2,43.35,41.85,42.1,435000,37.44,12.45,37.38,31.03,0.34
20260514,44.4,44.4,42,42.15,302000,37.83,11.42,38.13,31.27,0.24
20260515,42.15,42.65,38.4,38.55,1164000,37.89,1.74,38.57,31.45,0.88
20260518,38.55,39,37.3,38.8,250000,37.97,2.2,38.87,31.64,0.2
20260519,38.8,40.45,38.2,38.3,208000,37.99,0.81,39.19,31.81,0.18
20260520,38.35,39.35,37.8,38.6,157000,38.04,1.46,39.56,31.99,0.13
20260521,38.95,40.5,38.95,39.7,231000,38.18,3.97,39.84,32.19,0.2
20260522,39.7,41.6,39.7,41.1,41000,38.43,6.96,40.02,32.41,0.04
20260525,41.1,41.1,38.5,39.3,39000,38.5,2.08,40.01,32.6,0.05
20260526,39.3,39.9,38.6,39.8,39000,38.61,3.09,40.12,32.79,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.49
- over_600_ratio: 75.49
- over_800_ratio: 75.49
- over_1000_ratio: 73.43
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
20260430,75.5,,75.5,,73.44,,0,False,False
20260508,75.49,-0.01,75.49,-0.01,73.43,-0.01,0,False,False
20260515,75.49,0,75.49,0,73.43,0,0,False,False
20260522,75.49,0,75.49,0,73.43,0,0,False,False
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
