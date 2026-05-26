# INDIVIDUAL STOCK CHATGPT PACKET - 3086 華義*

## Metadata
- generated_at: 2026-05-26 22:18:58 Asia/Taipei
- stock_id: 3086
- stock_name: 華義*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 127
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3086_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3086_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3086_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3086_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3086_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3086_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3086_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3086_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3086_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3086_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3086_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3086_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3086_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3086.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3086.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3086.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3086.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3086.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3086.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3086_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3086_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3086_latest.md?ref=main

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
- open: 36
- high: 36.25
- low: 35
- close: 35.05
- volume: 35000
- ma5: 36.24
- ema23_primary: 63.36
- distance_to_ema23_pct: -44.68
- ma20: 38.69
- ma60: 163.66
- ma120: 193.42
- return_5d: -2.91
- return_20d: -14.62
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -9.4
- distance_to_high_60_pct: -89.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,40.7,41.25,39.5,40.35,968000,171.66,-76.49,209.46,222.34,1
20260429,40.55,41.35,38.9,39,1022000,160.6,-75.72,197.36,219.6,1.01
20260430,39,40,37.25,38.6,1586000,150.44,-74.34,184.46,216.71,1.46
20260504,39.4,41.9,38.4,41.2,1504000,141.33,-70.85,171.95,213.87,1.31
20260505,41.1,44.45,40.7,43.4,1266000,133.17,-67.41,159.04,211.04,1.05
20260506,44.25,45.4,43.1,43.5,1627000,125.7,-65.39,146.19,208.05,1.27
20260507,43.8,44.2,40.25,40.55,1293000,118.6,-65.81,133.5,204.91,0.97
20260508,39.5,41.05,39.5,39.9,644000,112.05,-64.39,120.67,201.6,0.47
20260511,39.9,41.5,39.8,40.05,629000,106.05,-62.23,108.02,198.44,0.45
20260512,40,40.65,39.1,39.15,487000,100.47,-61.03,95.47,195.31,0.34
20260513,39.95,39.95,38.3,38.3,533000,95.29,-59.81,82.64,192.24,0.37
20260514,38.5,39.8,37.8,37.95,461000,90.51,-58.07,69.19,189.05,0.32
20260515,38.7,39.65,37.65,37.85,402000,86.12,-56.05,54.33,185.94,0.28
20260518,37,37.35,36.1,36.65,430000,82,-55.31,39.91,182.79,0.29
20260519,36.65,37.65,35.9,36.1,474000,78.18,-53.82,39.93,179.53,0.33
20260520,36.1,38.1,36,36.6,650000,74.71,-51.01,39.8,176.39,0.44
20260521,37.7,37.85,36.6,36.85,408000,71.56,-48.5,39.48,173.25,0.28
20260522,37.35,37.4,36.7,36.9,37000,68.67,-46.26,39.32,170.09,0.04
20260525,37.95,37.95,35.8,35.8,36000,65.93,-45.7,38.99,166.81,0.05
20260526,36,36.25,35,35.05,35000,63.36,-44.68,38.69,163.66,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.64
- over_600_ratio: 85.88
- over_800_ratio: 84.67
- over_1000_ratio: 83.68
- over_400_change_1w: -0.11
- over_800_change_1w: -0.34
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.59,,85.84,,83.85,,0,False,False
20260508,87.18,-0.41,85.36,-0.48,83.75,-0.1,0,False,False
20260515,86.75,-0.43,85.01,-0.35,83.7,-0.05,0,False,False
20260522,86.64,-0.11,84.67,-0.34,83.68,-0.02,0,False,False
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
