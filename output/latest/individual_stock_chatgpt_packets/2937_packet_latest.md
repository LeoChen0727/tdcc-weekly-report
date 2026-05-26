# INDIVIDUAL STOCK CHATGPT PACKET - 2937 集雅社

## Metadata
- generated_at: 2026-05-26 23:53:34 Asia/Taipei
- stock_id: 2937
- stock_name: 集雅社
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 117
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2937_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2937_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2937_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2937_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2937_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2937_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2937_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2937_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2937_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2937_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2937_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2937_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2937_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2937.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2937.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2937.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2937.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2937.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2937.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2937_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2937_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2937_latest.md?ref=main

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
- open: 47.5
- high: 47.75
- low: 47.15
- close: 47.75
- volume: 47000
- ma5: 47.13
- ema23_primary: 45.59
- distance_to_ema23_pct: 4.74
- ma20: 44.98
- ma60: 45.2
- ma120: 44.52
- return_5d: 3.35
- return_20d: 6.82
- volume_ratio: 3.69
- distance_to_ma20_pct_auxiliary: 6.16
- distance_to_high_60_pct: -3.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260423,44.2,44.45,43.85,44.45,4000,45.14,-1.54,45.4,44.87,0.42
20260424,43.9,43.9,43.8,43.8,6000,45.03,-2.74,45.16,44.87,0.62
20260427,43.8,43.8,43.8,43.8,1000,44.93,-2.51,44.93,44.87,0.11
20260429,42.45,43.05,42.45,43.05,5000,44.77,-3.85,44.66,44.85,0.58
20260430,43.4,43.75,43.4,43.75,2000,44.69,-2.1,44.41,44.85,0.31
20260504,43.75,43.75,43.75,43.75,2000,44.61,-1.93,44.31,44.85,0.38
20260505,43.75,43.75,43.75,43.75,2000,44.54,-1.77,44.3,44.84,0.4
20260506,43.95,43.95,43.5,43.5,4000,44.45,-2.14,44.27,44.84,0.87
20260507,41.65,43.5,41.65,43.5,12000,44.37,-1.97,44.27,44.84,2.5
20260508,43,43.5,42.95,43.5,11000,44.3,-1.8,44.27,44.83,2.12
20260511,43,44.4,43,44.4,15000,44.31,0.21,44.31,44.83,2.56
20260512,44.4,45.2,44.4,45,7000,44.37,1.43,44.34,44.85,1.18
20260513,45.05,45.65,45.05,45.6,15000,44.47,2.54,44.37,44.87,2.4
20260514,45.6,45.85,45.6,45.85,6000,44.58,2.84,44.4,44.9,0.94
20260515,45.8,46.2,44.3,46.2,17000,44.72,3.31,44.45,44.94,2.46
20260518,46.2,46.45,46.2,46.45,4000,44.86,3.54,44.51,44.98,0.6
20260519,46.4,46.45,46.4,46.45,9000,44.99,3.23,44.56,45.02,1.32
20260521,46.5,49.7,46.5,47.5,38000,45.2,5.08,44.68,45.08,4.58
20260522,47.5,47.55,47.5,47.5,48000,45.4,4.64,44.83,45.14,4.59
20260526,47.5,47.75,47.15,47.75,47000,45.59,4.74,44.98,45.2,3.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.52
- over_600_ratio: 81.25
- over_800_ratio: 77.86
- over_1000_ratio: 71.57
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.46,,77.88,,71.57,,0,False,False
20260508,84.48,0.02,77.88,0,71.57,0,1,False,False
20260515,84.53,0.05,77.87,-0.01,71.57,0,2,False,False
20260522,84.52,-0.01,77.86,-0.01,71.57,0,0,False,False
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
