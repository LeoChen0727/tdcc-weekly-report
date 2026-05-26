# INDIVIDUAL STOCK CHATGPT PACKET - 6582 申豐

## Metadata
- generated_at: 2026-05-26 21:26:29 Asia/Taipei
- stock_id: 6582
- stock_name: 申豐
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6582_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6582_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6582_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6582_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6582_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6582_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6582_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6582_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6582_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6582_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6582_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6582_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6582_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6582.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6582.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6582.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6582.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6582.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6582.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6582_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6582_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6582_latest.md?ref=main

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
- open: 30.6
- high: 30.7
- low: 30.3
- close: 30.5
- volume: 58614
- ma5: 30.67
- ema23_primary: 31.03
- distance_to_ema23_pct: -1.7
- ma20: 30.85
- ma60: 31.85
- ma120: 32.35
- return_5d: 0
- return_20d: -1.77
- volume_ratio: 0.91
- distance_to_ma20_pct_auxiliary: -1.14
- distance_to_high_60_pct: -16.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,32.9,32.9,30.95,31.3,72847,32.16,-2.66,32.63,32.39,0.38
20260429,31.3,31.65,31.15,31.2,32733,32.08,-2.73,32.42,32.39,0.26
20260430,31.3,31.3,30.25,30.85,44204,31.97,-3.52,32.25,32.38,0.43
20260504,30.85,31.1,30.85,30.9,37921,31.88,-3.09,32.11,32.37,0.41
20260505,30.9,30.95,30.8,30.8,42109,31.79,-3.13,31.95,32.35,0.53
20260506,31.2,31.3,30.4,30.4,58897,31.68,-4.03,31.8,32.27,0.76
20260507,31.2,31.2,30.75,30.9,74211,31.61,-2.26,31.7,32.23,1.01
20260508,31,31.8,31,31.7,85942,31.62,0.25,31.66,32.21,1.2
20260511,31.85,32.45,31.1,31.45,116847,31.61,-0.49,31.59,32.18,1.57
20260512,31.4,31.45,31,31,65410,31.56,-1.76,31.52,32.16,0.89
20260513,31.1,31.1,30.65,30.8,41088,31.49,-2.2,31.41,32.13,0.57
20260514,29.8,31.05,29.8,30.75,187370,31.43,-2.17,31.32,32.11,2.42
20260515,30.85,31.05,30.45,30.65,78867,31.37,-2.28,31.2,32.07,1
20260518,30.55,30.6,30.3,30.5,32339,31.29,-2.54,31.11,32.05,0.44
20260519,30.5,30.6,30.35,30.5,68998,31.23,-2.33,31.05,32.03,0.96
20260520,30.5,30.6,30.5,30.6,42990,31.18,-1.85,31,32.01,0.62
20260521,31.05,31.05,30.65,30.8,30939,31.14,-1.1,30.95,31.98,0.45
20260522,30.85,30.85,30.7,30.85,61189,31.12,-0.87,30.91,31.94,0.93
20260525,30.9,30.9,30.45,30.6,60517,31.08,-1.53,30.88,31.9,0.92
20260526,30.6,30.7,30.3,30.5,58614,31.03,-1.7,30.85,31.85,0.91
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.28
- over_600_ratio: 74.28
- over_800_ratio: 73.66
- over_1000_ratio: 71.21
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
20260430,74.28,,73.66,,71.21,,0,False,False
20260508,74.28,0,73.66,0,71.21,0,0,False,False
20260515,74.28,0,73.66,0,71.21,0,0,False,False
20260522,74.28,0,73.66,0,71.21,0,0,False,False
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
