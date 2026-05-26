# INDIVIDUAL STOCK CHATGPT PACKET - 6165 浪凡

## Metadata
- generated_at: 2026-05-26 23:02:07 Asia/Taipei
- stock_id: 6165
- stock_name: 浪凡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6165_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6165_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6165_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6165_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6165_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6165_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6165_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6165_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6165_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6165_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6165_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6165_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6165_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6165.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6165.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6165.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6165.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6165.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6165.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6165_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6165_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6165_latest.md?ref=main

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
- open: 48.75
- high: 49.95
- low: 48
- close: 49.15
- volume: 664674
- ma5: 48.63
- ema23_primary: 49.12
- distance_to_ema23_pct: 0.05
- ma20: 50.17
- ma60: 47.27
- ma120: 46.75
- return_5d: 2.93
- return_20d: -5.48
- volume_ratio: 0.45
- distance_to_ma20_pct_auxiliary: -2.03
- distance_to_high_60_pct: -10.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,52.1,53,50.1,50.5,1065915,47.49,6.34,46.81,44.99,1.53
20260429,50.7,53,50.2,52.2,5860070,47.88,9.01,47.13,45.12,6.03
20260430,54.4,55,52.1,53.1,4788395,48.32,9.9,47.55,45.28,4.02
20260504,54.8,54.8,51.6,51.6,2175545,48.59,6.19,47.88,45.4,1.69
20260505,51.6,53.4,51.3,52,1135758,48.88,6.39,48.2,45.54,0.85
20260506,52.1,53,51.2,52.2,2198230,49.15,6.2,48.55,45.7,1.53
20260507,52.5,52.5,51.3,51.4,883536,49.34,4.17,48.85,45.84,0.6
20260508,51.2,53.8,51.1,52,4250055,49.56,4.92,49.19,45.99,2.54
20260511,52.8,53.5,51.5,51.8,1078229,49.75,4.12,49.49,46.14,0.63
20260512,51.8,51.8,49.85,49.95,1303268,49.77,0.37,49.73,46.28,0.74
20260513,50,50,49,49.2,497303,49.72,-1.04,49.95,46.4,0.28
20260514,49.15,49.5,48.5,48.95,575362,49.65,-1.42,50.15,46.51,0.33
20260515,49,49.25,48.25,48.25,385710,49.54,-2.6,50.32,46.62,0.22
20260518,48,49.3,47.9,49.3,298929,49.52,-0.44,50.52,46.75,0.17
20260519,49.55,49.75,47.7,47.75,478501,49.37,-3.28,50.57,46.83,0.27
20260520,48,48.2,47.7,47.9,264457,49.25,-2.74,50.53,46.91,0.16
20260521,48.75,48.85,48.3,48.3,358792,49.17,-1.77,50.51,46.99,0.21
20260522,49,49.5,48.35,49.45,472554,49.19,0.52,50.47,47.08,0.3
20260525,49.5,49.55,48.1,48.35,838763,49.12,-1.57,50.31,47.17,0.55
20260526,48.75,49.95,48,49.15,664674,49.12,0.05,50.17,47.27,0.45
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.92
- over_600_ratio: 45.54
- over_800_ratio: 41.79
- over_1000_ratio: 37.13
- over_400_change_1w: -0.04
- over_800_change_1w: 1.08
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.89,,42.13,,31.63,,0,False,False
20260508,49.04,-1.85,41.06,-1.07,36.39,4.76,1,False,True
20260515,47.96,-1.08,40.71,-0.35,37.13,0.74,2,False,True
20260522,47.92,-0.04,41.79,1.08,37.13,0,3,False,True
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
