# INDIVIDUAL STOCK CHATGPT PACKET - 3498 陽程

## Metadata
- generated_at: 2026-05-30 23:42:04 Asia/Taipei
- stock_id: 3498
- stock_name: 陽程
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3498_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3498_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3498_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3498_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3498_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3498.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3498.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3498.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3498.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3498_latest.md?ref=main

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
- open: 149.5
- high: 152.5
- low: 148
- close: 151
- volume: 151000
- ma5: 153.1
- ema23_primary: 129.37
- distance_to_ema23_pct: 16.72
- ma20: 130.33
- ma60: 93.88
- ma120: 72.32
- return_5d: -5.62
- return_20d: 72.18
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 15.86
- distance_to_high_60_pct: -8.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,92,96.4,89,96.4,7659000,80.91,19.14,82.3,68.06,1.79
20260505,98.5,105.5,98.1,101,7855000,82.59,22.3,83.71,68.89,1.73
20260506,102,103.5,93.1,98.9,5693000,83.94,17.82,85.05,69.72,1.21
20260507,100,103.5,96,97.3,5183000,85.06,14.39,86.09,70.49,1.1
20260508,95.9,99.6,90,93.5,3209000,85.76,9.02,86.56,71.14,0.7
20260511,102.5,102.5,102.5,102.5,1426000,87.16,17.6,87.7,72.02,0.34
20260512,112,112.5,110,112.5,3363000,89.27,26.02,88.94,73.08,0.81
20260513,113,123.5,113,123.5,4723000,92.12,34.06,90.83,74.34,1.2
20260514,133.5,135.5,132,135.5,1393000,95.74,41.54,93.51,75.75,0.37
20260515,141,149,132.5,149,7484000,100.17,48.74,96.89,77.42,1.85
20260518,148.5,153.5,138.5,144.5,9552000,103.87,39.12,99.89,79.02,2.23
20260519,143,150,135,136.5,1574000,106.59,28.06,102.42,80.45,0.38
20260520,140,148.5,140,143.5,1250000,109.66,30.85,105.21,82.03,0.31
20260521,150,150,144,146.5,922000,112.73,29.95,108.2,83.69,0.23
20260522,152,160,149.5,160,156000,116.67,37.14,112.22,85.53,0.04
20260525,162.5,164.5,156,159,160000,120.2,32.28,116.25,87.36,0.04
20260526,160,160,151.5,155,153000,123.1,25.91,120.16,89.12,0.04
20260527,155,156,149,155.5,152000,125.8,23.61,123.91,90.87,0.04
20260528,155.5,156,143,145,150000,127.4,13.82,127.17,92.37,0.04
20260529,149.5,152.5,148,151,151000,129.37,16.72,130.33,93.88,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 54.6
- over_600_ratio: 52.34
- over_800_ratio: 50.24
- over_1000_ratio: 48.83
- over_400_change_1w: 0.09
- over_800_change_1w: -1.66
- over_1000_change_1w: -0.24
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.12,,43.66,,40.56,,0,False,False
20260508,45.03,-1.09,43.34,-0.32,40.43,-0.13,0,False,False
20260515,51.96,6.93,47.64,4.3,46.04,5.61,1,True,True
20260522,54.51,2.55,51.9,4.26,49.07,3.03,2,True,True
20260529,54.6,0.09,50.24,-1.66,48.83,-0.24,3,False,False
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
