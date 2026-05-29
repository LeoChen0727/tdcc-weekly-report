# INDIVIDUAL STOCK CHATGPT PACKET - 8342 益張

## Metadata
- generated_at: 2026-05-29 19:33:59 Asia/Taipei
- stock_id: 8342
- stock_name: 益張
- packet_status: standard_rawdata_packet
- latest_price_date: 20260529
- price_rows: 101
- latest_tdcc_date: 20260522
- tdcc_rows: 26
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8342_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8342_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8342_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8342_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8342_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8342_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8342_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8342_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8342_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8342_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8342_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8342_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8342_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8342.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8342.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8342.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8342.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8342.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8342.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8342_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8342_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8342_latest.md?ref=main

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
- open: 88.8
- high: 89.5
- low: 88.8
- close: 89.5
- volume: 89000
- ma5: 90.92
- ema23_primary: 90.16
- distance_to_ema23_pct: -0.74
- ma20: 90.31
- ma60: 87.92
- ma120: 86.52
- return_5d: -0.89
- return_20d: -4.28
- volume_ratio: 3.39
- distance_to_ma20_pct_auxiliary: -0.89
- distance_to_high_60_pct: -5.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260417,94,94,92.8,92.8,4000,89.26,3.97,88.54,86.4,0.53
20260421,91,93.9,91,91,3000,89.4,1.79,88.92,86.49,0.4
20260422,94.1,94.1,89.6,89.6,4000,89.42,0.2,89.19,86.55,0.53
20260423,91.9,91.9,91.9,91.9,1000,89.62,2.54,89.59,86.66,0.13
20260427,90,90,90,90,4000,89.66,0.38,89.81,86.74,0.55
20260428,88.1,88.1,88.1,88.1,3000,89.53,-1.59,89.94,86.79,0.43
20260506,87.1,90,87,87.6,4000,89.37,-1.98,90.03,86.82,0.58
20260511,89.9,90,88,88,5000,89.25,-1.4,90.14,86.85,0.74
20260512,89.9,93,89.9,90.1,14000,89.32,0.87,90.25,86.95,1.94
20260513,91.9,92,88.9,90.3,10000,89.4,1,90.36,87.06,1.32
20260514,91.8,91.8,88.8,88.8,7000,89.35,-0.62,90.38,87.12,0.9
20260515,91,91.1,89.8,89.8,4000,89.39,0.46,90.45,87.2,0.51
20260519,91.3,91.3,91.2,91.2,2000,89.54,1.85,90.66,87.29,0.26
20260520,92,92,92,92,1000,89.75,2.51,90.83,87.39,0.14
20260521,92.3,92.4,89.2,90.3,6000,89.79,0.56,90.94,87.46,0.81
20260522,91.8,92,91.8,92,92000,89.98,2.25,90.86,87.56,8.44
20260525,90.4,90.4,90.4,90.4,90000,90.01,0.43,90.67,87.65,6.59
20260526,91.4,91.5,91.4,91.5,91000,90.14,1.51,90.6,87.75,5.13
20260528,91.1,91.2,91.1,91.2,91000,90.22,1.08,90.5,87.86,4.15
20260529,88.8,89.5,88.8,89.5,89000,90.16,-0.74,90.31,87.92,3.39
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.73
- over_600_ratio: 68.37
- over_800_ratio: 68.37
- over_1000_ratio: 65.44
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260306,72.46,0,68.1,0,65.17,0,0,False,False
20260313,72.46,0,68.1,0,65.17,0,0,False,False
20260320,72.46,0,68.1,0,65.17,0,0,False,False
20260327,72.54,0.08,68.18,0.08,65.25,0.08,1,True,True
20260402,72.58,0.04,68.22,0.04,65.29,0.04,2,True,True
20260410,72.6,0.02,68.24,0.02,65.31,0.02,3,True,True
20260417,72.67,0.07,68.31,0.07,65.38,0.07,4,True,True
20260424,72.68,0.01,68.32,0.01,65.39,0.01,5,True,True
20260430,72.68,0,68.32,0,65.39,0,0,False,False
20260508,72.68,0,68.32,0,65.39,0,0,False,False
20260515,72.71,0.03,68.35,0.03,65.42,0.03,1,True,True
20260522,72.73,0.02,68.37,0.02,65.44,0.02,2,True,True
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
