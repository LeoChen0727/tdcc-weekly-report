# INDIVIDUAL STOCK CHATGPT PACKET - 8040 九暘

## Metadata
- generated_at: 2026-05-30 23:43:48 Asia/Taipei
- stock_id: 8040
- stock_name: 九暘
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8040_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8040_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8040_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8040_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8040_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8040_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8040_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8040_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8040_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8040_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8040_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8040_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8040_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8040.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8040.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8040.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8040.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8040.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8040.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8040_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8040_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8040_latest.md?ref=main

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
- open: 110
- high: 114
- low: 109.5
- close: 111.5
- volume: 111000
- ma5: 114.9
- ema23_primary: 94.43
- distance_to_ema23_pct: 18.07
- ma20: 94.61
- ma60: 67.84
- ma120: 58.48
- return_5d: -6.3
- return_20d: 64.7
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 17.85
- distance_to_high_60_pct: -14.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,73,74.4,73,74.4,1165000,62.14,19.73,60.76,52.81,0.58
20260505,78.6,81.8,78.3,81.8,7676000,63.78,28.26,62.48,53.33,3.21
20260506,89.9,89.9,79.7,80.6,10784000,65.18,23.66,64.12,53.82,3.68
20260507,82,82.6,78.5,80,2531000,66.41,20.46,65.7,54.31,0.83
20260508,80,84.7,77.5,77.8,3144000,67.36,15.49,67.16,54.79,0.98
20260511,77,80.2,76.1,78,1579000,68.25,14.29,68.7,55.29,0.48
20260512,77.2,82.8,76.2,81.5,2203000,69.35,17.51,70.19,55.88,0.66
20260513,80.6,84.3,79.1,82.4,2988000,70.44,16.98,71.66,56.48,0.88
20260514,85.1,88.5,83.3,87.9,4478000,71.9,22.26,73.14,57.17,1.28
20260515,87.9,89.2,83,84.5,2411000,72.95,15.84,74.18,57.81,0.7
20260518,82.8,92.9,82.8,92.9,3414000,74.61,24.52,75.7,58.6,0.97
20260519,92.8,96.2,89.7,89.8,6497000,75.87,18.35,77.22,59.33,1.73
20260520,90.6,98.7,90.6,98.7,6685000,77.78,26.9,78.89,60.21,1.68
20260521,99.7,108.5,96.3,108.5,9305000,80.34,35.06,80.72,61.23,2.14
20260522,119,119,118,119,119000,83.56,42.41,83.42,62.43,0.03
20260525,130.5,130.5,120.5,122.5,127000,86.8,41.12,86.11,63.66,0.03
20260526,124,126.5,115,118,120000,89.4,31.99,88.41,64.82,0.03
20260527,120,126.5,112.5,113,118000,91.37,23.67,90.44,65.86,0.03
20260528,113.5,120,107,109.5,112000,92.88,17.89,92.42,66.82,0.03
20260529,110,114,109.5,111.5,111000,94.43,18.07,94.61,67.84,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 54.12
- over_600_ratio: 51.15
- over_800_ratio: 47.7
- over_1000_ratio: 45.81
- over_400_change_1w: -2.32
- over_800_change_1w: -0.73
- over_1000_change_1w: -0.68
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.38,,46.57,,44.6,,0,False,False
20260508,51.38,0,46.57,0,44.6,0,1,False,False
20260515,52.55,1.17,46.57,0,44.6,0,2,False,False
20260522,56.44,3.89,48.43,1.86,46.49,1.89,3,True,True
20260529,54.12,-2.32,47.7,-0.73,45.81,-0.68,4,False,False
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
