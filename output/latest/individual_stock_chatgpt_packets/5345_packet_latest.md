# INDIVIDUAL STOCK CHATGPT PACKET - 5345 馥鴻

## Metadata
- generated_at: 2026-05-26 21:26:03 Asia/Taipei
- stock_id: 5345
- stock_name: 馥鴻
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 122
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5345_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5345_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5345_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5345_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5345_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5345_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5345_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5345_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5345_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5345_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5345_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5345_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5345_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5345.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5345.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5345.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5345.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5345.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5345.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5345_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5345_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5345_latest.md?ref=main

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
- open: 18.8
- high: 19.5
- low: 18.25
- close: 18.95
- volume: 19000
- ma5: 19.66
- ema23_primary: 21.14
- distance_to_ema23_pct: -10.35
- ma20: 21.22
- ma60: 22.47
- ma120: 23.41
- return_5d: -8.45
- return_20d: -16.34
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: -10.7
- distance_to_high_60_pct: -21.04

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260424,22.2,22.7,22.15,22.7,6000,23.1,-1.72,23.14,23.43,0.38
20260428,22.35,22.5,21.9,22.45,37000,23.04,-2.57,23.14,23.4,2.12
20260429,22.45,22.45,22.45,22.45,1000,22.99,-2.36,23.14,23.37,0.06
20260430,21.85,22,21.5,21.9,22000,22.9,-4.37,23.1,23.31,1.29
20260504,21.9,21.95,21.3,21.95,14000,22.82,-3.82,23.02,23.25,0.83
20260505,21.95,21.95,21.6,21.6,15000,22.72,-4.93,22.94,23.21,0.94
20260506,20.95,21.2,20.8,21.2,8000,22.59,-6.17,22.82,23.15,0.51
20260507,21.15,21.75,21.15,21.75,27000,22.52,-3.43,22.74,23.1,1.68
20260508,21.75,21.75,21.75,21.75,12000,22.46,-3.16,22.66,23.05,0.74
20260511,21,21.85,21,21.85,3000,22.41,-2.49,22.57,23.01,0.2
20260512,21.85,21.95,21.85,21.95,23000,22.37,-1.88,22.5,22.97,1.65
20260513,21.15,21.9,20.95,21.9,6000,22.33,-1.93,22.41,22.94,0.44
20260514,21.15,21.3,20.95,21.25,29000,22.24,-4.46,22.3,22.9,1.94
20260515,20.75,20.75,20.7,20.7,4000,22.11,-6.39,22.16,22.85,0.27
20260518,20.7,20.7,20,20.7,21000,21.99,-5.89,22.02,22.79,1.34
20260519,21,21,21,21,1000,21.91,-4.16,21.91,22.75,0.07
20260521,20.3,21,20.2,20.2,20000,21.77,-7.21,21.77,22.7,1.3
20260522,20.2,20.2,19.4,19.4,20000,21.57,-10.07,21.6,22.63,1.35
20260525,19.95,19.95,18.75,18.75,19000,21.34,-12.12,21.41,22.55,1.31
20260526,18.8,19.5,18.25,18.95,19000,21.14,-10.35,21.22,22.47,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.56
- over_600_ratio: 79.56
- over_800_ratio: 79.56
- over_1000_ratio: 79.56
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
20260430,79.56,,79.56,,79.56,,0,False,False
20260508,79.56,0,79.56,0,79.56,0,0,False,False
20260515,79.56,0,79.56,0,79.56,0,0,False,False
20260522,79.56,0,79.56,0,79.56,0,0,False,False
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
