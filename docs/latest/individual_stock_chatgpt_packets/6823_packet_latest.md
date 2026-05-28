# INDIVIDUAL STOCK CHATGPT PACKET - 6823 濾能

## Metadata
- generated_at: 2026-05-28 20:20:19 Asia/Taipei
- stock_id: 6823
- stock_name: 濾能
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6823_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6823_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6823_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6823_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6823_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6823_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6823_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6823_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6823_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6823_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6823_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6823_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6823_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6823.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6823.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6823.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6823.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6823.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6823.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6823_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6823_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6823_latest.md?ref=main

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
- date: 20260528
- open: 75.9
- high: 75.9
- low: 72.5
- close: 72.7
- volume: 74000
- ma5: 78.52
- ema23_primary: 81.19
- distance_to_ema23_pct: -10.46
- ma20: 86.25
- ma60: 74.17
- ma120: 72.75
- return_5d: -7.62
- return_20d: -20.98
- volume_ratio: 0.12
- distance_to_ma20_pct_auxiliary: -15.71
- distance_to_high_60_pct: -35.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,94.2,99.9,91,96.8,2094000,76.74,26.14,74.75,66.52,3.33
20260504,99,105,97.2,104,1522000,79.01,31.62,76.78,67.2,2.17
20260505,103,113.5,102.5,105.5,1678000,81.22,29.89,78.97,67.97,2.15
20260506,105,105,95.1,96.2,1117000,82.47,16.65,80.68,68.55,1.34
20260507,97.2,105,97.2,98.5,848000,83.81,17.53,82.49,69.17,0.98
20260508,91,95.3,88.7,88.7,1585000,84.21,5.33,83.81,69.62,1.69
20260511,89.1,91,86.1,88.8,650000,84.6,4.97,85.08,70.08,0.68
20260512,90.8,90.8,88,89,445000,84.96,4.75,86.05,70.51,0.47
20260513,88.6,88.6,84.6,84.9,434000,84.96,-0.07,86.84,70.89,0.46
20260514,85.3,85.4,80.2,80.6,605000,84.59,-4.72,87.41,71.2,0.62
20260515,81.1,82.7,80.6,82,271000,84.38,-2.82,88,71.55,0.28
20260518,80,81.4,78.5,79.9,221000,84,-4.89,88.14,71.86,0.23
20260519,79.2,80.5,78.9,79.5,230000,83.63,-4.94,87.94,72.17,0.27
20260520,78.8,80.1,78.4,79.2,157000,83.26,-4.88,87.72,72.48,0.19
20260521,78.6,80.6,78.6,78.7,274000,82.88,-5.04,87.27,72.8,0.34
20260522,80,82.8,80,82.2,82000,82.82,-0.75,87.29,73.12,0.11
20260525,83.1,83.1,80.7,81.4,81000,82.7,-1.58,87.52,73.44,0.11
20260526,80.8,82.3,80.2,80.6,81000,82.53,-2.34,87.68,73.76,0.11
20260527,83.2,83.2,74.1,75.7,77000,81.96,-7.64,87.21,74,0.11
20260528,75.9,75.9,72.5,72.7,74000,81.19,-10.46,86.25,74.17,0.12
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.56
- over_600_ratio: 53.06
- over_800_ratio: 53.06
- over_1000_ratio: 53.06
- over_400_change_1w: 1.84
- over_800_change_1w: -0.17
- over_1000_change_1w: -0.17
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.91,,53.39,,53.39,,0,False,False
20260508,53.32,-1.59,53.32,-0.07,53.32,-0.07,0,False,False
20260515,54.72,1.4,53.23,-0.09,53.23,-0.09,1,False,False
20260522,56.56,1.84,53.06,-0.17,53.06,-0.17,2,False,False
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
