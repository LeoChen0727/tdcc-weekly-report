# INDIVIDUAL STOCK CHATGPT PACKET - 8064 東捷

## Metadata
- generated_at: 2026-05-26 22:20:42 Asia/Taipei
- stock_id: 8064
- stock_name: 東捷
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8064_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8064_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8064_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8064_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8064_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8064_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8064_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8064_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8064_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8064_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8064_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8064_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8064_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8064.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8064.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8064.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8064.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8064.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8064.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8064_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8064_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8064_latest.md?ref=main

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
- open: 151
- high: 152.5
- low: 137
- close: 149
- volume: 146000
- ma5: 134.2
- ema23_primary: 116.21
- distance_to_ema23_pct: 28.22
- ma20: 118.71
- ma60: 83.92
- ma120: 65.93
- return_5d: 8.76
- return_20d: 89.81
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: 25.52
- distance_to_high_60_pct: -2.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,79.1,86.3,78.1,86.3,18898000,75.43,14.41,75.78,62.48,1.2
20260429,85.2,94.9,85.1,94.9,15537000,77.05,23.17,77.19,63.14,0.97
20260430,100.5,104,100,104,4084000,79.3,31.15,79.22,63.93,0.25
20260504,114,114,114,114,2678000,82.19,38.71,81.69,64.89,0.17
20260505,119.5,125,114,125,13489000,85.76,45.76,84.64,66.02,0.84
20260506,127.5,127.5,112.5,112.5,29577000,87.98,27.86,87.03,66.95,1.71
20260507,110.5,112,104.5,108,5439000,89.65,20.46,88.87,67.8,0.32
20260508,105,110.5,103.5,103.5,4062000,90.81,13.98,90.13,68.6,0.25
20260511,105,113.5,103.5,113.5,3355000,92.7,22.44,91.92,69.6,0.22
20260512,118,119.5,111.5,118.5,5080000,94.85,24.94,93.69,70.72,0.35
20260513,114.5,120,114,118.5,3340000,96.82,22.39,95.83,71.81,0.24
20260514,123,123,115.5,115.5,3435000,98.38,17.41,97.84,72.8,0.26
20260515,118.5,127,117.5,120,6079000,100.18,19.79,100.08,73.9,0.46
20260518,118,132,117.5,132,5125000,102.83,28.37,102.78,75.25,0.41
20260519,130.5,143.5,130.5,137,5566000,105.68,29.64,105.45,76.67,0.49
20260520,139,139,123.5,123.5,7022000,107.16,15.25,107.47,77.94,0.65
20260521,123.5,130.5,119.5,120.5,18859000,108.27,11.29,109.33,79.19,1.75
20260522,121,132.5,117,132.5,127000,110.29,20.13,112.12,80.61,0.01
20260525,141.5,145.5,139,145.5,144000,113.23,28.5,115.19,82.24,0.02
20260526,151,152.5,137,149,146000,116.21,28.22,118.71,83.92,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.43
- over_600_ratio: 46.04
- over_800_ratio: 43.4
- over_1000_ratio: 41.39
- over_400_change_1w: -3.13
- over_800_change_1w: -2.62
- over_1000_change_1w: -3.68
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.56,,52.1,,49.21,,0,False,False
20260508,53.42,-4.14,47.44,-4.66,45.56,-3.65,0,False,False
20260515,52.56,-0.86,46.02,-1.42,45.07,-0.49,0,False,False
20260522,49.43,-3.13,43.4,-2.62,41.39,-3.68,0,False,False
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
