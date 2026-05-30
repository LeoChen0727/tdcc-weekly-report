# INDIVIDUAL STOCK CHATGPT PACKET - 1423 利華

## Metadata
- generated_at: 2026-05-30 23:40:56 Asia/Taipei
- stock_id: 1423
- stock_name: 利華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1423_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1423_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1423_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1423_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1423_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1423_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1423_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1423_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1423_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1423_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1423_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1423_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1423_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1423.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1423.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1423.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1423.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1423.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1423.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1423_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1423_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1423_latest.md?ref=main

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
- open: 42.4
- high: 42.4
- low: 41.3
- close: 41.5
- volume: 62034
- ma5: 41.47
- ema23_primary: 41.06
- distance_to_ema23_pct: 1.07
- ma20: 40.94
- ma60: 40.49
- ma120: 39.4
- return_5d: 1.47
- return_20d: -0.24
- volume_ratio: 0.8
- distance_to_ma20_pct_auxiliary: 1.37
- distance_to_high_60_pct: -3.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,41.6,41.7,40.8,40.8,112023,40.93,-0.32,40.91,39.59,1.95
20260505,39.95,41.15,39.95,40.7,70897,40.91,-0.52,40.95,39.63,1.17
20260506,40.8,41.2,40.75,41.1,84809,40.93,0.42,41.01,39.68,1.35
20260507,40.85,41.7,40.85,41.05,16366,40.94,0.27,41.06,39.73,0.26
20260508,42,42,40.8,40.85,17733,40.93,-0.2,41.1,39.78,0.28
20260511,40.85,40.9,40.5,40.55,65912,40.9,-0.85,41.12,39.82,1.03
20260512,40,41.15,39.55,40.2,78157,40.84,-1.57,41.13,39.85,1.17
20260513,39.75,40.2,39.75,39.95,7938,40.77,-2,41.12,39.89,0.12
20260514,40.55,41.4,39.6,40.55,244942,40.75,-0.49,41.14,39.93,3.37
20260515,41,41.4,40.65,41.1,52340,40.78,0.79,41.16,39.98,0.75
20260518,40.8,40.8,40.75,40.8,6318,40.78,0.05,41.18,40.03,0.1
20260519,40.8,42.25,40.8,40.8,10585,40.78,0.05,41.17,40.07,0.16
20260520,40.85,41.15,40.75,40.8,37158,40.78,0.04,41.14,40.12,0.6
20260521,40.9,41.3,40.75,41.3,37498,40.83,1.16,41.09,40.17,0.65
20260522,40.8,41.8,40.75,40.9,31794,40.83,0.17,41.02,40.21,0.57
20260525,41.4,42.4,41.4,41.8,125452,40.91,2.17,41.02,40.27,2.04
20260526,41.8,42.45,40.85,40.85,419290,40.91,-0.14,40.98,40.31,5.28
20260527,41,41.8,41,41.5,43216,40.96,1.33,40.95,40.37,0.55
20260528,41,41.7,40.95,41.7,35220,41.02,1.66,40.95,40.43,0.44
20260529,42.4,42.4,41.3,41.5,62034,41.06,1.07,40.94,40.49,0.8
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.34
- over_600_ratio: 79.79
- over_800_ratio: 76.97
- over_1000_ratio: 74.25
- over_400_change_1w: 0.11
- over_800_change_1w: 0.11
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.84,,75.7,,73.92,,0,False,False
20260508,80.95,0.11,76.59,0.89,73.92,0,1,False,True
20260515,81.13,0.18,76.25,-0.34,74.47,0.55,2,False,True
20260522,81.23,0.1,76.86,0.61,74.27,-0.2,3,False,True
20260529,81.34,0.11,76.97,0.11,74.25,-0.02,4,False,True
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
