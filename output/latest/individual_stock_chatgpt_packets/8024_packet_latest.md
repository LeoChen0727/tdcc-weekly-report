# INDIVIDUAL STOCK CHATGPT PACKET - 8024 佑華

## Metadata
- generated_at: 2026-05-30 23:43:47 Asia/Taipei
- stock_id: 8024
- stock_name: 佑華
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8024_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8024_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8024_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8024_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8024_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8024_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8024_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8024_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8024_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8024_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8024_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8024_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8024_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8024.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8024.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8024.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8024.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8024.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8024.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8024_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8024_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8024_latest.md?ref=main

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
- open: 12.7
- high: 12.7
- low: 12.45
- close: 12.5
- volume: 13000
- ma5: 12.69
- ema23_primary: 12.56
- distance_to_ema23_pct: -0.48
- ma20: 12.47
- ma60: 12.73
- ma120: 12.74
- return_5d: -3.1
- return_20d: -1.57
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: 0.24
- distance_to_high_60_pct: -10.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.8,12.8,12.55,12.7,28000,12.83,-1.01,12.89,13.01,0.44
20260505,12.5,12.75,12.45,12.75,68000,12.82,-0.57,12.88,13,1.04
20260506,12.75,12.8,12.5,12.65,71000,12.81,-1.24,12.87,12.98,1.05
20260507,12.75,12.75,12.4,12.5,102000,12.78,-2.21,12.86,12.96,1.43
20260508,12.5,12.75,12.3,12.4,70000,12.75,-2.75,12.84,12.93,0.94
20260511,12.65,12.65,12.2,12.3,103000,12.71,-3.25,12.8,12.92,1.4
20260512,12.35,12.7,12.25,12.45,85000,12.69,-1.9,12.76,12.89,1.22
20260513,12.35,12.45,12.25,12.3,81000,12.66,-2.84,12.7,12.88,1.13
20260514,12.3,12.4,12.1,12.2,166000,12.62,-3.33,12.65,12.85,2.13
20260515,12.1,12.35,12,12.2,162000,12.59,-3.06,12.61,12.83,1.96
20260518,12.1,12.4,12,12.05,63000,12.54,-3.92,12.56,12.8,0.75
20260519,12,12.15,11.9,12.05,98000,12.5,-3.6,12.51,12.78,1.21
20260520,12,12.3,11.95,12.15,56000,12.47,-2.57,12.47,12.77,0.71
20260521,12.45,12.5,12.1,12.35,80000,12.46,-0.89,12.45,12.76,1.04
20260522,12.35,12.95,12.25,12.9,13000,12.5,3.22,12.46,12.76,0.17
20260525,12.95,13.2,12.65,12.85,13000,12.53,2.58,12.46,12.75,0.19
20260526,12.85,12.95,12.6,12.75,13000,12.55,1.63,12.47,12.75,0.19
20260527,12.75,12.9,12.5,12.7,13000,12.56,1.13,12.47,12.74,0.19
20260528,12.7,12.85,12.45,12.65,13000,12.57,0.67,12.48,12.74,0.19
20260529,12.7,12.7,12.45,12.5,13000,12.56,-0.48,12.47,12.73,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 28.79
- over_600_ratio: 25.66
- over_800_ratio: 22.7
- over_1000_ratio: 18.86
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
20260430,28.79,,22.7,,18.86,,0,False,False
20260508,28.79,0,22.7,0,18.86,0,0,False,False
20260515,28.79,0,22.7,0,18.86,0,0,False,False
20260522,28.79,0,22.7,0,18.86,0,0,False,False
20260529,28.79,0,22.7,0,18.86,0,0,False,False
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
