# INDIVIDUAL STOCK CHATGPT PACKET - 5464 霖宏

## Metadata
- generated_at: 2026-05-26 23:01:56 Asia/Taipei
- stock_id: 5464
- stock_name: 霖宏
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5464_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5464_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5464_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5464.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5464.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5464.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5464.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5464_latest.md?ref=main

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
- high: 73
- low: 69.8
- close: 72.2
- volume: 71000
- ma5: 71.04
- ema23_primary: 55.25
- distance_to_ema23_pct: 30.68
- ma20: 54.49
- ma60: 37.26
- ma120: 31.58
- return_5d: 15.52
- return_20d: 132.9
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: 32.5
- distance_to_high_60_pct: -3.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,30.75,32,30.75,31.8,295000,30.01,5.98,29.89,27.85,0.87
20260429,31.35,31.95,31.2,31.8,301000,30.16,5.45,30.09,27.95,0.88
20260430,31.85,33.2,31.5,33,863000,30.39,8.58,30.33,28.07,2.29
20260504,33.7,36.3,33.65,35.9,3684000,30.85,16.36,30.71,28.24,6.76
20260505,37,39.45,37,39.45,5772000,31.57,24.97,31.28,28.46,6.98
20260506,43.35,43.35,43.35,43.35,1410000,32.55,33.18,32.03,28.75,1.58
20260507,47.65,47.65,47.65,47.65,1583000,33.81,40.94,32.99,29.12,1.67
20260508,52.4,52.4,50.4,52.4,7811000,35.36,48.2,34.19,29.57,5.86
20260511,52.6,57.6,50.5,57.6,2645000,37.21,54.79,35.62,30.11,1.81
20260512,62.9,63.3,62.9,63.3,1018000,39.39,60.72,37.29,30.74,0.68
20260513,68.7,68.7,62,62,2514000,41.27,50.23,38.91,31.36,1.57
20260514,61.5,64,59,59.5,1355000,42.79,39.05,40.4,31.93,0.82
20260515,60.2,60.2,53.6,57.1,1402000,43.98,29.83,41.77,32.45,0.82
20260518,53.8,61.1,53.8,57.3,968000,45.09,27.07,43.13,32.97,0.55
20260519,57.4,62.9,55.8,62.5,834000,46.54,34.29,44.67,33.57,0.48
20260520,68,68,62.7,67.5,901000,48.29,39.78,46.42,34.26,0.51
20260521,68,72,68,71.5,718000,50.22,42.37,48.36,35.02,0.4
20260522,71.5,72,70,71,71000,51.95,36.66,50.33,35.75,0.04
20260525,71.5,75,71.5,73,73000,53.71,35.92,52.43,36.51,0.04
20260526,73,73,69.8,72.2,71000,55.25,30.68,54.49,37.26,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.59
- over_600_ratio: 67.93
- over_800_ratio: 64.11
- over_1000_ratio: 56.24
- over_400_change_1w: 1.86
- over_800_change_1w: -0.5
- over_1000_change_1w: -1.81
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.27,,58.64,,52.07,,0,False,False
20260508,66.57,4.3,63.43,4.79,54.28,2.21,1,True,True
20260515,69.73,3.16,64.61,1.18,58.05,3.77,2,True,True
20260522,71.59,1.86,64.11,-0.5,56.24,-1.81,3,False,False
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
