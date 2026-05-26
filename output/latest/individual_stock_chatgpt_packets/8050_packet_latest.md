# INDIVIDUAL STOCK CHATGPT PACKET - 8050 廣積

## Metadata
- generated_at: 2026-05-26 22:20:42 Asia/Taipei
- stock_id: 8050
- stock_name: 廣積
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8050_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8050_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8050_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8050_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8050_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8050_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8050_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8050_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8050_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8050_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8050_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8050_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8050_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8050.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8050.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8050.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8050.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8050.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8050.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8050_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8050_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8050_latest.md?ref=main

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
- open: 54.9
- high: 60.1
- low: 53.9
- close: 60.1
- volume: 57000
- ma5: 54.24
- ema23_primary: 48.45
- distance_to_ema23_pct: 24.06
- ma20: 47.72
- ma60: 43.35
- ma120: 43.38
- return_5d: 21.91
- return_20d: 45.52
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: 25.95
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,41.3,42,41.15,41.7,268000,41.47,0.56,41.16,41.65,0.69
20260429,42,42.25,41.5,41.85,232000,41.5,0.85,41.25,41.62,0.6
20260430,41.9,41.9,41.5,41.55,262000,41.5,0.11,41.36,41.58,0.7
20260504,41.75,43.7,41.75,42.9,821000,41.62,3.08,41.48,41.56,2.03
20260505,43.45,45.25,43,45.2,1964000,41.92,7.83,41.72,41.57,3.99
20260506,45.2,45.2,44,44.35,963000,42.12,5.29,41.94,41.58,1.82
20260507,44,44.85,43.85,44.45,518000,42.31,5.05,42.13,41.59,0.95
20260508,44,44.9,43.8,44.45,567000,42.49,4.61,42.31,41.62,1.01
20260511,44.5,47.75,44.5,47.6,2052000,42.92,10.91,42.63,41.71,3.15
20260512,47.8,48.7,47.2,47.4,1191000,43.29,9.49,42.96,41.8,1.71
20260513,47,48.4,46.3,47.95,883000,43.68,9.78,43.33,41.9,1.22
20260514,48,50.3,47.6,49.05,2377000,44.13,11.16,43.74,42.01,2.89
20260515,49.55,49.55,46.85,47,1621000,44.37,5.94,44.03,42.08,1.84
20260518,46.8,49,46.3,48.4,852000,44.7,8.27,44.35,42.19,0.97
20260519,48.4,50.3,48.4,49.3,1831000,45.09,9.35,44.7,42.32,1.93
20260520,49.6,52.2,49.35,51.3,2356000,45.6,12.49,45.14,42.47,2.25
20260521,51.8,52,50.9,51.3,1279000,46.08,11.33,45.56,42.63,1.19
20260522,51.8,54.5,51.4,53.8,53000,46.72,15.15,46.15,42.84,0.05
20260525,55.2,56.6,53.9,54.7,55000,47.39,15.43,46.78,43.05,0.05
20260526,54.9,60.1,53.9,60.1,57000,48.45,24.06,47.72,43.35,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 43.37
- over_600_ratio: 41.03
- over_800_ratio: 39.69
- over_1000_ratio: 37.44
- over_400_change_1w: -0.18
- over_800_change_1w: 0.4
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.63,,39.79,,37.99,,0,False,False
20260508,43.24,-0.39,39.32,-0.47,37.45,-0.54,0,False,False
20260515,43.55,0.31,39.29,-0.03,37.44,-0.01,1,False,False
20260522,43.37,-0.18,39.69,0.4,37.44,0,2,False,True
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
