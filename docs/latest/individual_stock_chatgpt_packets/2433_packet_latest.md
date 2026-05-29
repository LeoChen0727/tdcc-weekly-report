# INDIVIDUAL STOCK CHATGPT PACKET - 2433 互盛電

## Metadata
- generated_at: 2026-05-29 19:32:04 Asia/Taipei
- stock_id: 2433
- stock_name: 互盛電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2433_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2433_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2433_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2433_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2433_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2433_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2433_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2433_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2433_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2433_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2433_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2433_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2433_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2433.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2433.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2433.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2433.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2433.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2433.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2433_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2433_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2433_latest.md?ref=main

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
- open: 43.9
- high: 43.9
- low: 43.1
- close: 43.4
- volume: 43342
- ma5: 43.53
- ema23_primary: 44.62
- distance_to_ema23_pct: -2.73
- ma20: 44.76
- ma60: 45.53
- ma120: 46.38
- return_5d: -2.36
- return_20d: -4.3
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: -3.03
- distance_to_high_60_pct: -8.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,45.35,45.35,45.2,45.25,40463,45.71,-1.02,45.68,46.17,1.13
20260505,45.1,45.25,45.1,45.2,29881,45.67,-1.03,45.66,46.15,0.82
20260506,45.3,45.5,45.25,45.45,42493,45.65,-0.44,45.66,46.13,1.16
20260507,45.45,45.8,45.45,45.6,41963,45.65,-0.11,45.66,46.11,1.13
20260508,45.75,45.9,45.5,45.75,45398,45.66,0.2,45.66,46.1,1.19
20260511,45.8,45.8,45.5,45.55,37220,45.65,-0.21,45.66,46.09,0.95
20260512,45.5,45.65,45.5,45.5,29241,45.64,-0.3,45.66,46.06,0.73
20260513,45.5,45.6,45.2,45.55,36932,45.63,-0.17,45.63,46.05,0.92
20260514,45.45,45.45,45.15,45.15,38449,45.59,-0.96,45.59,46.02,1
20260515,45.25,45.25,45,45.1,41833,45.55,-0.98,45.55,45.99,1.07
20260518,45.1,45.1,44.9,44.95,58987,45.5,-1.2,45.5,45.97,1.45
20260519,44.85,44.95,44.85,44.85,42376,45.44,-1.31,45.45,45.94,1.06
20260520,44.8,44.8,44.2,44.6,124534,45.37,-1.71,45.38,45.91,2.81
20260521,44.6,44.8,44.5,44.5,43999,45.3,-1.77,45.31,45.87,0.99
20260522,44.4,44.55,44.2,44.45,70262,45.23,-1.72,45.25,45.82,1.52
20260525,44.2,45,44.05,44.1,182103,45.14,-2.3,45.17,45.77,3.49
20260526,44.1,44.1,43.7,43.8,147211,45.02,-2.72,45.1,45.72,2.59
20260527,43.85,43.85,43.35,43.4,111660,44.89,-3.32,45,45.65,1.82
20260528,43.85,43.85,42.8,42.95,128448,44.73,-3.97,44.85,45.59,1.93
20260529,43.9,43.9,43.1,43.4,43342,44.62,-2.73,44.76,45.53,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.9
- over_600_ratio: 78.03
- over_800_ratio: 78.03
- over_1000_ratio: 78.03
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.9,,78.03,,78.03,,0,False,False
20260508,78.9,0,78.03,0,78.03,0,0,False,False
20260515,78.9,0,78.03,0,78.03,0,0,False,False
20260522,78.9,0,78.03,0,78.03,0,0,False,False
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
