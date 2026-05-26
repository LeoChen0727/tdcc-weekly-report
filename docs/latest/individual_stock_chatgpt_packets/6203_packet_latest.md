# INDIVIDUAL STOCK CHATGPT PACKET - 6203 海韻電

## Metadata
- generated_at: 2026-05-26 23:02:10 Asia/Taipei
- stock_id: 6203
- stock_name: 海韻電
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6203_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6203_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6203_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6203_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6203_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6203_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6203_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6203_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6203_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6203_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6203_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6203_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6203_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6203.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6203.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6203.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6203.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6203.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6203.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6203_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6203_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6203_latest.md?ref=main

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
- open: 73
- high: 73.2
- low: 71.7
- close: 72
- volume: 72000
- ma5: 71.32
- ema23_primary: 69.61
- distance_to_ema23_pct: 3.43
- ma20: 70.01
- ma60: 67.14
- ma120: 69.13
- return_5d: 5.42
- return_20d: 12.85
- volume_ratio: 0.11
- distance_to_ma20_pct_auxiliary: 2.84
- distance_to_high_60_pct: -7.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,63.7,63.9,63.4,63.6,135000,65.4,-2.75,65.52,65.92,0.79
20260429,63.6,64.4,63.2,64,89000,65.28,-1.97,65.4,65.87,0.52
20260430,64.3,64.8,63.9,64.5,125000,65.22,-1.1,65.39,65.82,0.74
20260504,65.1,69.3,65.1,69.3,580000,65.56,5.71,65.53,65.84,3.03
20260505,71.9,76.2,71.2,76.2,1982000,66.45,14.68,66.03,65.96,6.93
20260506,76.6,78.1,72.1,75.3,3331000,67.18,12.08,66.45,66.08,7.43
20260507,75.1,77,70.2,71.1,2061000,67.51,5.32,66.62,66.15,3.79
20260508,71,71,68.6,68.9,533000,67.63,1.88,66.69,66.19,0.94
20260511,68.9,75.7,68.7,74.7,1830000,68.21,9.51,67.19,66.36,2.88
20260512,73.2,74.7,71.1,71.8,782000,68.51,4.8,67.56,66.48,1.18
20260513,70.6,71.4,69.6,69.8,372000,68.62,1.72,67.85,66.56,0.55
20260514,70.2,71.1,69.4,69.4,393000,68.69,1.04,68.12,66.63,0.58
20260515,70,70.1,67.9,68.1,296000,68.64,-0.78,68.28,66.68,0.43
20260518,67.3,69,67,68.6,177000,68.63,-0.05,68.44,66.76,0.26
20260519,68.1,69.3,68,68.3,178000,68.61,-0.45,68.57,66.84,0.26
20260520,68.2,69.5,67.7,69,195000,68.64,0.53,68.7,66.92,0.28
20260521,69.5,71.1,69.4,70.7,333000,68.81,2.75,68.89,66.95,0.48
20260522,71.1,72.3,70.4,72.3,71000,69.1,4.63,69.22,67.01,0.1
20260525,72.5,73.5,72.1,72.6,73000,69.39,4.62,69.6,67.09,0.11
20260526,73,73.2,71.7,72,72000,69.61,3.43,70.01,67.14,0.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.92
- over_600_ratio: 54.7
- over_800_ratio: 52.13
- over_1000_ratio: 52.13
- over_400_change_1w: 0.64
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.79,,52.13,,52.13,,0,False,False
20260508,58.28,-0.51,52.13,0,52.13,0,0,False,False
20260515,58.28,0,52.13,0,52.13,0,0,False,False
20260522,58.92,0.64,52.13,0,52.13,0,1,False,False
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
