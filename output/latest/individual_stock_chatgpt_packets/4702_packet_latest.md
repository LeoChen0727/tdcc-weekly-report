# INDIVIDUAL STOCK CHATGPT PACKET - 4702 中美實

## Metadata
- generated_at: 2026-05-29 19:32:54 Asia/Taipei
- stock_id: 4702
- stock_name: 中美實
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4702_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4702_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4702_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4702_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4702_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4702_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4702_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4702_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4702_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4702_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4702_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4702_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4702_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4702.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4702.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4702.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4702.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4702.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4702.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4702_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4702_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4702_latest.md?ref=main

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
- open: 9.69
- high: 9.75
- low: 9.64
- close: 9.69
- volume: 10000
- ma5: 9.72
- ema23_primary: 9.76
- distance_to_ema23_pct: -0.67
- ma20: 9.72
- ma60: 9.91
- ma120: 9.92
- return_5d: -0.41
- return_20d: -0.41
- volume_ratio: 0.13
- distance_to_ma20_pct_auxiliary: -0.33
- distance_to_high_60_pct: -8.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,9.74,9.83,9.66,9.69,95000,9.91,-2.18,9.92,9.97,0.92
20260505,9.69,9.69,9.63,9.64,49000,9.88,-2.47,9.9,9.96,0.48
20260506,9.63,9.9,9.56,9.71,148000,9.87,-1.61,9.89,9.96,1.4
20260507,9.74,9.78,9.68,9.69,32000,9.85,-1.67,9.88,9.95,0.31
20260508,9.81,9.85,9.67,9.67,110000,9.84,-1.72,9.86,9.95,1.03
20260511,9.79,9.91,9.73,9.87,156000,9.84,0.29,9.85,9.95,1.41
20260512,9.87,9.95,9.83,9.89,62000,9.85,0.45,9.85,9.95,0.56
20260513,9.79,9.84,9.62,9.71,181000,9.83,-1.26,9.83,9.94,1.59
20260514,9.71,9.77,9.67,9.67,53000,9.82,-1.53,9.81,9.94,0.47
20260515,9.67,9.96,9.67,9.79,231000,9.82,-0.29,9.8,9.94,2.02
20260518,9.7,9.79,9.65,9.72,88000,9.81,-0.92,9.79,9.94,0.82
20260519,9.72,9.84,9.65,9.7,72000,9.8,-1.03,9.77,9.94,0.69
20260520,9.66,9.76,9.6,9.66,97000,9.79,-1.32,9.76,9.94,0.92
20260521,9.68,9.78,9.66,9.71,58000,9.78,-0.74,9.74,9.94,0.55
20260522,9.79,9.79,9.68,9.73,10000,9.78,-0.49,9.73,9.94,0.1
20260525,9.7,9.74,9.6,9.7,10000,9.77,-0.73,9.72,9.93,0.1
20260526,9.74,9.9,9.71,9.85,10000,9.78,0.74,9.73,9.93,0.11
20260527,9.85,9.88,9.67,9.69,10000,9.77,-0.83,9.73,9.92,0.12
20260528,9.69,9.85,9.63,9.66,10000,9.76,-1.04,9.72,9.92,0.13
20260529,9.69,9.75,9.64,9.69,10000,9.76,-0.67,9.72,9.91,0.13
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.37
- over_600_ratio: 48.91
- over_800_ratio: 48.08
- over_1000_ratio: 48.08
- over_400_change_1w: -0.05
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.42,,48.13,,48.13,,0,False,False
20260508,51.39,-0.03,48.1,-0.03,48.1,-0.03,0,False,False
20260515,51.42,0.03,48.13,0.03,48.13,0.03,1,True,True
20260522,51.37,-0.05,48.08,-0.05,48.08,-0.05,0,False,False
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
