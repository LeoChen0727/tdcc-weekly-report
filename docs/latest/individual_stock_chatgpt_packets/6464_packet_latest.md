# INDIVIDUAL STOCK CHATGPT PACKET - 6464 台數科

## Metadata
- generated_at: 2026-05-26 23:02:18 Asia/Taipei
- stock_id: 6464
- stock_name: 台數科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6464_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6464_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6464_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6464_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6464_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6464.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6464.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6464.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6464.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6464_latest.md?ref=main

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
- open: 78
- high: 78
- low: 77.5
- close: 78
- volume: 11422
- ma5: 78.02
- ema23_primary: 77.15
- distance_to_ema23_pct: 1.1
- ma20: 76.92
- ma60: 76.77
- ma120: 76.96
- return_5d: 0
- return_20d: 3.04
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: 1.4
- distance_to_high_60_pct: -3.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,75.1,76.2,74.9,76,89100,76.35,-0.46,76.37,76.63,2.72
20260429,76,76,75.6,75.6,2701,76.29,-0.91,76.33,76.62,0.08
20260430,75,76.1,73,76.1,56206,76.28,-0.23,76.31,76.62,1.64
20260504,76,76.2,75.2,76.2,33323,76.27,-0.09,76.29,76.61,0.95
20260505,76.1,76.3,75.6,76.3,62525,76.27,0.04,76.31,76.62,1.68
20260506,77.1,77.1,76.1,76.4,36507,76.28,0.15,76.33,76.64,0.98
20260507,76.4,76.5,75.8,76.2,25212,76.28,-0.1,76.28,76.64,0.68
20260508,77.1,77.1,76.1,76.2,44768,76.27,-0.09,76.24,76.65,1.16
20260511,77,77,75.6,76.5,16097,76.29,0.28,76.23,76.68,0.42
20260512,76,76.5,76,76.5,21221,76.31,0.25,76.23,76.72,0.54
20260513,76.5,76.5,76.1,76.5,26502,76.32,0.23,76.22,76.77,0.68
20260514,75.4,76.9,75.4,76.5,50574,76.34,0.21,76.23,76.8,1.27
20260515,76.5,77.6,75.8,77.6,51854,76.44,1.51,76.3,76.81,1.28
20260518,77.4,77.8,76.2,77.8,66006,76.56,1.63,76.38,76.83,1.59
20260519,77.8,78,77.2,78,16612,76.68,1.73,76.46,76.83,0.4
20260520,76.8,78.1,76.8,78,239322,76.79,1.58,76.56,76.83,4.63
20260521,78,78,77.8,78,9040,76.89,1.45,76.63,76.83,0.18
20260522,77.3,78.1,77.1,78.1,36577,76.99,1.44,76.71,76.82,0.75
20260525,77.8,78.1,77.8,78,247412,77.07,1.2,76.81,76.8,4.31
20260526,78,78,77.5,78,11422,77.15,1.1,76.92,76.77,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.68
- over_600_ratio: 81.54
- over_800_ratio: 79.06
- over_1000_ratio: 77.64
- over_400_change_1w: 0
- over_800_change_1w: -0.39
- over_1000_change_1w: 0.29
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.52,,79.29,,77.22,,0,False,False
20260508,84.6,0.08,79.37,0.08,77.3,0.08,1,True,True
20260515,84.68,0.08,79.45,0.08,77.35,0.05,2,True,True
20260522,84.68,0,79.06,-0.39,77.64,0.29,3,False,True
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
