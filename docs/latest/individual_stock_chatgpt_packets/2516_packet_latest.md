# INDIVIDUAL STOCK CHATGPT PACKET - 2516 新建

## Metadata
- generated_at: 2026-05-26 22:18:40 Asia/Taipei
- stock_id: 2516
- stock_name: 新建
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2516_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2516_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2516_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2516_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2516_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2516_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2516_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2516_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2516_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2516_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2516_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2516_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2516_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2516.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2516.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2516.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2516.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2516.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2516.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2516_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2516_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2516_latest.md?ref=main

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
- open: 11.95
- high: 13.05
- low: 11.8
- close: 12.85
- volume: 560295
- ma5: 12.38
- ema23_primary: 12.89
- distance_to_ema23_pct: -0.32
- ma20: 12.99
- ma60: 13.55
- ma120: 14.15
- return_5d: 3.21
- return_20d: 1.98
- volume_ratio: 1.78
- distance_to_ma20_pct_auxiliary: -1.1
- distance_to_high_60_pct: -16.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.8,13.6,12.8,13.5,557630,13.47,0.21,13.42,14.06,1.81
20260429,13.5,13.75,13.5,13.75,321947,13.49,1.89,13.41,14.05,1.01
20260430,13.75,13.75,13.6,13.65,206918,13.51,1.06,13.42,14.03,0.65
20260504,13.65,14.6,13.65,13.9,1174780,13.54,2.66,13.44,14.02,3.24
20260505,13.9,13.95,13.4,13.45,293797,13.53,-0.61,13.45,14,0.82
20260506,14.1,14.1,13.45,13.6,171504,13.54,0.46,13.47,13.99,0.48
20260507,13.6,13.65,13.3,13.3,261983,13.52,-1.61,13.46,13.96,0.73
20260508,13.75,13.75,13.2,13.2,320953,13.49,-2.16,13.44,13.94,0.87
20260511,13.2,13.2,13.05,13.05,242298,13.46,-3.01,13.41,13.92,0.66
20260512,13.05,13.15,12.9,12.95,216389,13.41,-3.45,13.37,13.89,0.58
20260513,12.95,13.05,12.9,13,269003,13.38,-2.83,13.32,13.87,0.72
20260514,13,13.15,12.75,12.75,293078,13.33,-4.32,13.26,13.84,0.8
20260515,12.8,12.95,12.75,12.75,155326,13.28,-3.98,13.21,13.81,0.43
20260518,12.75,12.75,12.6,12.65,79978,13.23,-4.35,13.16,13.78,0.23
20260519,12.65,12.7,12.45,12.45,113576,13.16,-5.4,13.12,13.74,0.34
20260520,12.5,12.5,12.2,12.3,213618,13.09,-6.03,13.09,13.7,0.65
20260521,12.3,12.4,12.3,12.35,149526,13.03,-5.2,13.05,13.67,0.46
20260522,12.35,12.35,12.2,12.35,93250,12.97,-4.79,13.02,13.63,0.33
20260525,12.35,12.35,11.9,12.05,602103,12.89,-6.55,12.98,13.58,2
20260526,11.95,13.05,11.8,12.85,560295,12.89,-0.32,12.99,13.55,1.78
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.66
- over_600_ratio: 68.76
- over_800_ratio: 67.23
- over_1000_ratio: 62.05
- over_400_change_1w: -0.1
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.48
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.61,,66.39,,61.29,,0,False,False
20260508,70.56,-0.05,67.18,0.79,61.3,0.01,1,False,True
20260515,70.76,0.2,67.14,-0.04,61.57,0.27,2,False,True
20260522,70.66,-0.1,67.23,0.09,62.05,0.48,3,False,True
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
