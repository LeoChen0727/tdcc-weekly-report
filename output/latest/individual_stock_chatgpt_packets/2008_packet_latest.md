# INDIVIDUAL STOCK CHATGPT PACKET - 2008 高興昌

## Metadata
- generated_at: 2026-05-28 19:31:43 Asia/Taipei
- stock_id: 2008
- stock_name: 高興昌
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2008_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2008_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2008_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2008_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2008_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2008_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2008_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2008_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2008_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2008_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2008_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2008_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2008_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2008.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2008.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2008.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2008.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2008.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2008.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2008_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2008_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2008_latest.md?ref=main

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
- date: 20260528
- open: 28.5
- high: 28.95
- low: 28.15
- close: 28.25
- volume: 20274
- ma5: 27.89
- ema23_primary: 27.78
- distance_to_ema23_pct: 1.69
- ma20: 27.75
- ma60: 27.84
- ma120: 28.59
- return_5d: 1.44
- return_20d: 0.89
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: 1.82
- distance_to_high_60_pct: -5.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,27.55,27.95,27.5,27.5,32095,27.67,-0.63,27.5,28.4,0.18
20260504,27.55,27.6,27.5,27.5,58993,27.66,-0.58,27.52,28.38,0.32
20260505,27.85,27.9,27.5,27.5,9802,27.65,-0.53,27.54,28.35,0.05
20260506,27.6,28.55,27.55,28,17020,27.68,1.17,27.59,28.33,0.09
20260507,27.6,28,27.6,27.65,17199,27.67,-0.09,27.57,28.3,0.09
20260508,28.25,28.25,27.15,28.15,57202,27.71,1.57,27.57,28.27,0.31
20260511,27.5,28.1,27.5,27.9,13780,27.73,0.62,27.57,28.24,0.07
20260512,27.55,27.55,27.5,27.5,30004,27.71,-0.76,27.57,28.21,0.16
20260513,27.5,27.75,27.5,27.7,8191,27.71,-0.03,27.59,28.18,0.05
20260514,27.5,27.95,27.5,27.5,37655,27.69,-0.69,27.61,28.14,0.21
20260515,27.5,27.55,27.5,27.5,18581,27.68,-0.64,27.61,28.11,0.1
20260518,27.5,27.55,27.5,27.55,13403,27.67,-0.42,27.62,28.09,0.07
20260519,28.15,28.15,27.5,27.75,15779,27.67,0.28,27.66,28.07,0.54
20260520,27.5,27.9,27.5,27.9,18446,27.69,0.75,27.7,28.04,0.68
20260521,27.5,27.85,27.5,27.85,30547,27.7,0.52,27.7,28.01,1.2
20260522,27.5,27.85,27.5,27.55,15108,27.69,-0.51,27.7,27.97,0.61
20260525,27.55,27.75,27.5,27.75,20927,27.7,0.19,27.7,27.93,0.85
20260526,27.75,27.8,27.75,27.75,24279,27.7,0.18,27.7,27.9,0.95
20260527,28,28.3,27.75,28.15,26469,27.74,1.48,27.73,27.87,1.04
20260528,28.5,28.95,28.15,28.25,20274,27.78,1.69,27.75,27.84,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 92.33
- over_600_ratio: 91.23
- over_800_ratio: 91.23
- over_1000_ratio: 90.71
- over_400_change_1w: 0.04
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,92.19,,91.08,,90.56,,0,False,False
20260508,92.25,0.06,91.14,0.06,90.62,0.06,1,True,True
20260515,92.29,0.04,91.19,0.05,90.67,0.05,2,True,True
20260522,92.33,0.04,91.23,0.04,90.71,0.04,3,True,True
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
