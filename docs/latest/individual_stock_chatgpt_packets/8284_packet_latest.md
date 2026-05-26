# INDIVIDUAL STOCK CHATGPT PACKET - 8284 三竹

## Metadata
- generated_at: 2026-05-26 23:02:53 Asia/Taipei
- stock_id: 8284
- stock_name: 三竹
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8284_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8284_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8284_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8284_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8284_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8284_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8284_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8284_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8284_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8284_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8284_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8284_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8284_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8284.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8284.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8284.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8284.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8284.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8284.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8284_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8284_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8284_latest.md?ref=main

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
- open: 63.1
- high: 63.5
- low: 63
- close: 63.3
- volume: 63000
- ma5: 63.36
- ema23_primary: 63.57
- distance_to_ema23_pct: -0.42
- ma20: 63.63
- ma60: 63.42
- ma120: 63.23
- return_5d: -0.94
- return_20d: -1.4
- volume_ratio: 2.38
- distance_to_ma20_pct_auxiliary: -0.53
- distance_to_high_60_pct: -2.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,63.6,63.6,63.6,63.6,3000,63.69,-0.14,63.75,63.21,0.27
20260429,63.6,64.1,63.6,63.6,3000,63.68,-0.13,63.76,63.22,0.28
20260430,63.5,64,63.4,64,20000,63.71,0.46,63.8,63.24,1.75
20260504,63.8,64.2,63.8,63.8,32000,63.71,0.13,63.79,63.25,2.47
20260505,63.8,64.3,63.8,64.1,18000,63.75,0.55,63.82,63.27,1.31
20260506,64.1,65,63.7,63.7,30000,63.74,-0.07,63.83,63.28,2.03
20260507,64,64.4,63.9,64,14000,63.76,0.37,63.84,63.29,0.92
20260508,64.9,64.9,64.1,64.2,16000,63.8,0.63,63.85,63.3,1.01
20260511,64.4,64.9,63.8,64.1,42000,63.83,0.43,63.87,63.32,2.49
20260512,63.7,63.7,62.7,63.4,60000,63.79,-0.61,63.84,63.33,3.2
20260513,63.1,63.5,63.1,63.3,23000,63.75,-0.7,63.81,63.34,1.22
20260514,63.4,63.5,63.3,63.4,10000,63.72,-0.5,63.8,63.34,0.54
20260515,63.6,63.8,63.5,63.8,24000,63.73,0.11,63.81,63.35,1.24
20260518,63.7,63.7,63,63,21000,63.67,-1.05,63.77,63.35,1.07
20260519,63.1,63.9,63.1,63.9,10000,63.69,0.34,63.77,63.38,0.51
20260520,63.1,63.5,63.1,63.2,6000,63.65,-0.7,63.73,63.38,0.31
20260521,63.5,63.7,63.5,63.7,8000,63.65,0.08,63.71,63.39,0.44
20260522,63.2,63.6,63.2,63.5,63000,63.64,-0.22,63.71,63.41,3.01
20260525,63.5,63.5,62.6,63.1,63000,63.59,-0.77,63.68,63.41,2.68
20260526,63.1,63.5,63,63.3,63000,63.57,-0.42,63.63,63.42,2.38
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.57
- over_600_ratio: 58.47
- over_800_ratio: 54.12
- over_1000_ratio: 44.33
- over_400_change_1w: 0.52
- over_800_change_1w: 0.54
- over_1000_change_1w: 0.54
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.05,,53.58,,43.79,,0,False,False
20260508,63.05,0,53.58,0,43.79,0,0,False,False
20260515,63.05,0,53.58,0,43.79,0,0,False,False
20260522,63.57,0.52,54.12,0.54,44.33,0.54,1,True,True
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
