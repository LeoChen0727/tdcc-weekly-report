# INDIVIDUAL STOCK CHATGPT PACKET - 1784 訊聯

## Metadata
- generated_at: 2026-05-26 21:24:47 Asia/Taipei
- stock_id: 1784
- stock_name: 訊聯
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1784_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1784_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1784_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1784_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1784_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1784_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1784_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1784_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1784_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1784_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1784_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1784_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1784_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1784.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1784.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1784.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1784.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1784.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1784.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1784_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1784_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1784_latest.md?ref=main

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
- open: 69.5
- high: 69.5
- low: 67
- close: 67.4
- volume: 68000
- ma5: 70.06
- ema23_primary: 73.23
- distance_to_ema23_pct: -7.96
- ma20: 72.61
- ma60: 80.23
- ma120: 91
- return_5d: -3.71
- return_20d: -9.53
- volume_ratio: 0.39
- distance_to_ma20_pct_auxiliary: -7.18
- distance_to_high_60_pct: -37.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,74.5,76,74.5,76,72000,79.91,-4.89,78.59,88.29,0.38
20260429,76,76.3,75,75.7,78000,79.56,-4.85,78.53,87.83,0.43
20260430,75.8,77.8,75.5,75.5,127000,79.22,-4.69,78.52,87.39,0.73
20260504,75,75.4,73.5,73.7,227000,78.76,-6.42,78.3,86.95,1.28
20260505,73.1,74,72.9,73.7,127000,78.34,-5.92,78.06,86.52,0.71
20260506,75.5,76,72.2,72.2,219000,77.82,-7.23,77.75,86.05,1.19
20260507,72.3,72.5,71.6,71.9,160000,77.33,-7.02,77.39,85.62,0.86
20260508,71.9,73.2,71.1,72.6,163000,76.94,-5.64,77.09,85.19,0.87
20260511,73,74,72.7,73.5,219000,76.65,-4.11,76.84,84.81,1.15
20260512,74,74,72,72.7,164000,76.32,-4.74,76.45,84.44,0.87
20260513,73,73.1,72,72.5,114000,76,-4.61,75.86,84.06,0.65
20260514,73.6,77.7,73.1,77.5,488000,76.13,1.8,75.61,83.72,2.61
20260515,78.6,78.6,73,73,331000,75.87,-3.78,75.17,83.36,1.7
20260518,72.8,72.8,70.9,71.5,225000,75.5,-5.3,74.74,83.01,1.14
20260519,71.6,72.5,69.7,70,276000,75.04,-6.72,74.27,82.6,1.36
20260520,70.4,71.2,69.8,70.8,130000,74.69,-5.21,73.86,82.19,0.65
20260521,70.8,72.2,70.6,71.3,133000,74.41,-4.18,73.5,81.86,0.67
20260522,71.9,72.4,71,71.3,71000,74.15,-3.84,73.27,81.37,0.38
20260525,71.3,71.3,69.3,69.5,70000,73.76,-5.78,72.97,80.79,0.4
20260526,69.5,69.5,67,67.4,68000,73.23,-7.96,72.61,80.23,0.39
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 27.53
- over_600_ratio: 24.85
- over_800_ratio: 20.53
- over_1000_ratio: 13.44
- over_400_change_1w: -0.7
- over_800_change_1w: 0.15
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,28.51,,21.96,,13.44,,0,False,False
20260508,28.61,0.1,23.45,1.49,13.44,0,1,False,True
20260515,28.23,-0.38,20.38,-3.07,13.44,0,0,False,False
20260522,27.53,-0.7,20.53,0.15,13.44,0,1,False,True
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
