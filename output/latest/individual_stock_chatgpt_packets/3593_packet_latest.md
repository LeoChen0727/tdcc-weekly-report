# INDIVIDUAL STOCK CHATGPT PACKET - 3593 力銘

## Metadata
- generated_at: 2026-05-29 19:32:40 Asia/Taipei
- stock_id: 3593
- stock_name: 力銘
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 129
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3593_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3593_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3593_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3593_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3593_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3593_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3593_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3593_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3593_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3593_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3593_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3593_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3593_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3593.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3593.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3593.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3593.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3593.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3593.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3593_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3593_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3593_latest.md?ref=main

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
- open: 16.95
- high: 17.1
- low: 16.5
- close: 16.65
- volume: 50092
- ma5: 17.15
- ema23_primary: 17.64
- distance_to_ema23_pct: -5.62
- ma20: 18.02
- ma60: 16.07
- ma120: 13.44
- return_5d: -4.58
- return_20d: -16.12
- volume_ratio: 1.37
- distance_to_ma20_pct_auxiliary: -7.63
- distance_to_high_60_pct: -18.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,19.85,19.95,19.7,19.85,55518,17.67,12.36,17.78,14.23,0.52
20260505,19.95,20.4,19.05,19.25,38430,17.8,8.15,18.1,14.35,0.36
20260506,20,20,19.2,19.2,51890,17.92,7.17,18.41,14.48,0.48
20260507,17.5,19.8,17.5,19,38009,18.01,5.52,18.69,14.59,0.35
20260508,19,19,18.4,18.95,34909,18.08,4.79,18.93,14.71,0.32
20260511,18.65,18.75,17.1,18.6,44845,18.13,2.61,19.08,14.81,0.45
20260512,17.1,18.45,17.1,17.95,38722,18.11,-0.9,19.16,14.91,0.42
20260513,17.95,17.95,17.35,17.9,39687,18.09,-1.08,19.16,15,0.48
20260514,18.1,18.1,17.1,17.45,40257,18.04,-3.28,19.11,15.08,0.57
20260515,17.45,17.5,17.25,17.5,33649,18,-2.76,19.02,15.16,0.52
20260518,17.3,17.5,17.1,17.5,23675,17.95,-2.53,18.93,15.25,0.39
20260519,17.5,18.5,16.9,18.5,20430,18,2.78,18.89,15.35,0.37
20260520,17.55,18,17.45,17.95,19153,18,-0.26,18.81,15.45,0.38
20260521,17.5,17.7,17.25,17.7,23657,17.97,-1.51,18.71,15.55,0.5
20260522,16.5,17.65,16.5,17.45,22629,17.93,-2.67,18.62,15.64,0.54
20260525,17.45,17.45,17.05,17.45,44213,17.89,-2.45,18.53,15.73,1.04
20260526,17.2,17.4,16.55,17.4,43269,17.85,-2.51,18.46,15.82,1.01
20260527,17.4,17.4,16.25,17.3,37921,17.8,-2.82,18.34,15.91,0.91
20260528,16.6,17.4,16.6,16.95,32070,17.73,-4.4,18.18,15.99,0.84
20260529,16.95,17.1,16.5,16.65,50092,17.64,-5.62,18.02,16.07,1.37
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 62.66
- over_600_ratio: 58.78
- over_800_ratio: 53
- over_1000_ratio: 50.01
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.58,,53,,50.01,,0,False,False
20260508,62.63,0.05,53,0,50.01,0,1,False,False
20260515,62.65,0.02,53,0,50.01,0,2,False,False
20260522,62.66,0.01,53,0,50.01,0,3,False,False
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
