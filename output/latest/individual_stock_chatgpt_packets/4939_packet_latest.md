# INDIVIDUAL STOCK CHATGPT PACKET - 4939 亞電

## Metadata
- generated_at: 2026-05-30 23:42:31 Asia/Taipei
- stock_id: 4939
- stock_name: 亞電
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4939_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4939_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4939_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4939_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4939_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4939_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4939_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4939_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4939_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4939_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4939_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4939_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4939_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4939.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4939.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4939.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4939.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4939.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4939.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4939_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4939_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4939_latest.md?ref=main

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
- open: 47.05
- high: 50.5
- low: 45.75
- close: 50.5
- volume: 49000
- ma5: 44.57
- ema23_primary: 41.19
- distance_to_ema23_pct: 22.6
- ma20: 41.2
- ma60: 36.4
- ma120: 36.91
- return_5d: 27.69
- return_20d: 15.03
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 22.59
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,44.1,44.65,43.5,44,1082000,38.84,13.3,37.98,34.81,0.17
20260505,44,44,43.65,43.9,1227000,39.26,11.83,38.8,34.82,0.2
20260506,44,44,42.5,43,1836000,39.57,8.67,39.55,34.84,0.29
20260507,42.2,46.5,42.2,43.7,5744000,39.91,9.49,40.24,34.86,0.88
20260508,44.5,44.9,40.6,41.5,3925000,40.05,3.63,40.86,34.91,0.59
20260511,41.75,42.4,40,40.1,3044000,40.05,0.12,41.31,34.95,0.46
20260512,40.5,40.8,38.8,39.45,3443000,40,-1.38,41.7,35.03,0.52
20260513,39.45,40.3,36.3,37.8,3646000,39.82,-5.06,41.95,35.07,0.55
20260514,38.4,39.55,37.4,37.8,2485000,39.65,-4.66,42.14,35.11,0.4
20260515,38.5,40,37.55,37.9,3027000,39.5,-4.06,42.16,35.17,0.54
20260518,37.85,38.65,35.6,38.4,2066000,39.41,-2.57,42.02,35.27,0.37
20260519,38,39.3,37.5,38.35,1836000,39.32,-2.47,41.68,35.38,0.44
20260520,38.8,39.7,37.35,37.55,2286000,39.17,-4.15,41.25,35.46,0.88
20260521,38.05,38.8,37.85,38.05,1739000,39.08,-2.64,40.92,35.54,0.69
20260522,38.55,40.75,38.55,39.55,40000,39.12,1.1,40.7,35.63,0.02
20260525,40.45,41,38.8,39.65,40000,39.16,1.24,40.61,35.7,0.02
20260526,40.4,43.6,39.3,43.6,43000,39.53,10.28,40.79,35.84,0.02
20260527,43.75,47.95,42.3,43.15,45000,39.84,8.32,40.77,35.96,0.02
20260528,44.75,47,43.4,45.95,45000,40.34,13.89,40.87,36.13,0.02
20260529,47.05,50.5,45.75,50.5,49000,41.19,22.6,41.2,36.4,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 28.87
- over_600_ratio: 23.7
- over_800_ratio: 20.85
- over_1000_ratio: 18.37
- over_400_change_1w: 4.05
- over_800_change_1w: 2.83
- over_1000_change_1w: 2.98
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,25.61,,19.36,,16.78,,0,False,False
20260508,25.29,-0.32,18.94,-0.42,16.41,-0.37,0,False,False
20260515,24.97,-0.32,17.91,-1.03,15.39,-1.02,1,False,False
20260522,24.82,-0.15,18.02,0.11,15.39,0,2,False,True
20260529,28.87,4.05,20.85,2.83,18.37,2.98,3,True,True
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
