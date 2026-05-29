# INDIVIDUAL STOCK CHATGPT PACKET - 5425 台半

## Metadata
- generated_at: 2026-05-29 19:33:07 Asia/Taipei
- stock_id: 5425
- stock_name: 台半
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5425_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5425_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5425_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5425_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5425_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5425_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5425_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5425_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5425_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5425_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5425_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5425_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5425_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5425.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5425.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5425.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5425.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5425.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5425.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5425_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5425_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5425_latest.md?ref=main

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
- open: 125.5
- high: 125.5
- low: 113
- close: 116.5
- volume: 118000
- ma5: 105.52
- ema23_primary: 85.54
- distance_to_ema23_pct: 36.19
- ma20: 83.89
- ma60: 67.12
- ma120: 63.09
- return_5d: 33.75
- return_20d: 85.51
- volume_ratio: 0.01
- distance_to_ma20_pct_auxiliary: 38.88
- distance_to_high_60_pct: -7.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,63,63.8,61.8,62.3,5633000,60.14,3.59,59.7,59.98,0.75
20260505,62.6,65.5,62.4,64.6,8811000,60.51,6.75,60.27,59.94,1.12
20260506,68.9,70.9,67.2,68.5,21252000,61.18,11.97,60.77,59.96,2.49
20260507,69.8,73,68,71.5,20712000,62.04,15.25,61.45,60.02,2.28
20260508,70.8,74.9,68.9,73,23417000,62.95,15.96,62.27,60.11,2.31
20260511,77.4,80.3,72.3,80.3,37121000,64.4,24.69,63.46,60.39,3.13
20260512,81,84.8,78.8,81.1,43746000,65.79,23.27,64.64,60.73,3.13
20260513,79.2,80.5,74.3,76.2,21804000,66.66,14.31,65.55,60.97,1.46
20260514,78.5,80.3,72.3,72.7,26188000,67.16,8.25,66.28,61.14,1.63
20260515,73,77,71.9,72,14383000,67.56,6.56,66.89,61.31,0.88
20260518,71,78.5,69.5,77.9,20500000,68.43,13.85,67.5,61.59,1.24
20260519,82,85.6,79.3,85.6,25974000,69.86,22.54,68.67,62.02,1.54
20260520,85.6,89.3,78.7,86.9,66487000,71.28,21.92,69.89,62.46,3.34
20260521,90.6,93.5,86.6,90.4,57173000,72.87,24.05,71.31,62.99,2.54
20260522,89.5,92,87.1,87.1,89000,74.06,17.61,72.7,63.44,0
20260525,91,94.8,89.7,91.6,93000,75.52,21.29,74.38,63.92,0
20260526,95,100.5,94.7,100.5,98000,77.6,29.51,76.42,64.57,0
20260527,108.5,110.5,98.4,104.5,105000,79.84,30.88,78.7,65.28,0
20260528,104.5,114.5,102.5,114.5,112000,82.73,38.4,81.2,66.17,0.01
20260529,125.5,125.5,113,116.5,118000,85.54,36.19,83.89,67.12,0.01
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 46.4
- over_600_ratio: 44.69
- over_800_ratio: 42.13
- over_1000_ratio: 41.07
- over_400_change_1w: 7.81
- over_800_change_1w: 7.6
- over_1000_change_1w: 8.59
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,37.96,,34.88,,32.11,,0,False,False
20260508,39.07,1.11,35.64,0.76,33.96,1.85,1,True,True
20260515,38.59,-0.48,34.53,-1.11,32.48,-1.48,0,False,False
20260522,46.4,7.81,42.13,7.6,41.07,8.59,1,True,True
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
