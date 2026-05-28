# INDIVIDUAL STOCK CHATGPT PACKET - 3021 鴻名

## Metadata
- generated_at: 2026-05-28 19:32:12 Asia/Taipei
- stock_id: 3021
- stock_name: 鴻名
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3021_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3021_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3021_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3021_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3021_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3021_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3021_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3021_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3021_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3021_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3021_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3021_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3021_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3021.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3021.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3021.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3021.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3021.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3021.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3021_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3021_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3021_latest.md?ref=main

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
- open: 27.4
- high: 27.4
- low: 27.4
- close: 27.4
- volume: 536841
- ma5: 22.9
- ema23_primary: 18.97
- distance_to_ema23_pct: 44.41
- ma20: 18.21
- ma60: 16.95
- ma120: 17.36
- return_5d: 60.23
- return_20d: 66.57
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: 50.47
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,16.75,17.55,16.7,17.2,459563,16.47,4.43,16.37,16.76,3.05
20260504,17.4,17.4,16.7,16.7,186664,16.49,1.28,16.41,16.73,1.19
20260505,16.3,16.45,16.2,16.2,553747,16.46,-1.61,16.43,16.69,3.03
20260506,16.3,16.55,16.15,16.45,125255,16.46,-0.08,16.47,16.66,0.67
20260507,16.5,16.5,16.2,16.25,116119,16.45,-1.19,16.48,16.63,0.61
20260508,16.4,16.5,16.25,16.3,129031,16.43,-0.81,16.51,16.6,0.67
20260511,16.35,16.65,16.3,16.4,95580,16.43,-0.19,16.51,16.57,0.5
20260512,16.55,16.55,16.15,16.15,100129,16.41,-1.57,16.48,16.55,0.56
20260513,16.2,16.3,16.05,16.2,91516,16.39,-1.16,16.44,16.54,0.53
20260514,16.4,17.6,16.25,17,379393,16.44,3.4,16.45,16.52,2.09
20260515,17.65,17.9,16.8,17,802315,16.49,3.11,16.48,16.5,3.78
20260518,17,17.25,16.6,17,261098,16.53,2.84,16.51,16.5,1.17
20260519,17,17.2,16.75,16.75,106299,16.55,1.22,16.53,16.49,0.48
20260520,16.85,17.2,16.85,17,128910,16.59,2.49,16.57,16.49,0.57
20260521,17,17.2,17,17.1,133543,16.63,2.83,16.6,16.49,0.6
20260522,17.55,18.8,17.35,18.8,1360416,16.81,11.84,16.73,16.51,4.87
20260525,19.5,20.65,19.5,20.65,2939616,17.13,20.55,16.92,16.57,7.14
20260526,22.7,22.7,22.7,22.7,627301,17.59,29.02,17.24,16.66,1.44
20260527,24.95,24.95,24.95,24.95,500771,18.21,37.03,17.66,16.78,1.09
20260528,27.4,27.4,27.4,27.4,536841,18.97,44.41,18.21,16.95,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.91
- over_600_ratio: 69.88
- over_800_ratio: 68.26
- over_1000_ratio: 65.24
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.92,,68.27,,65.25,,0,False,False
20260508,70.92,0,68.27,0,65.25,0,0,False,False
20260515,70.92,0,68.27,0,65.25,0,0,False,False
20260522,70.91,-0.01,68.26,-0.01,65.24,-0.01,0,False,False
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
