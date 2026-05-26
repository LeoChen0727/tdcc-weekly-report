# INDIVIDUAL STOCK CHATGPT PACKET - 5381 光譜

## Metadata
- generated_at: 2026-05-26 21:26:04 Asia/Taipei
- stock_id: 5381
- stock_name: 光譜
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 128
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5381_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5381_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5381_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5381_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5381_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5381_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5381_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5381_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5381_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5381_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5381_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5381_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5381_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5381.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5381.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5381.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5381.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5381.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5381.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5381_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5381_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5381_latest.md?ref=main

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
- open: 27.2
- high: 27.25
- low: 26.2
- close: 26.75
- volume: 27000
- ma5: 25.76
- ema23_primary: 25.1
- distance_to_ema23_pct: 6.57
- ma20: 24.83
- ma60: 24.96
- ma120: 25.33
- return_5d: 5.73
- return_20d: 17.84
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 7.73
- distance_to_high_60_pct: -7.76

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.85,23.9,22.65,23.3,1135000,24.25,-3.9,23.88,26.29,1.1
20260429,23.3,23.7,22.95,23.6,612000,24.19,-2.45,23.82,26.26,0.63
20260430,23.6,23.85,23.4,23.5,425000,24.14,-2.63,23.79,26.2,0.45
20260504,23.5,24.5,23.15,23.85,695000,24.11,-1.08,23.81,26.12,0.76
20260505,23.85,24.5,23.8,23.85,429000,24.09,-0.99,23.8,26.04,0.48
20260506,24,24,23.45,23.65,561000,24.05,-1.68,23.82,25.92,0.65
20260507,23.95,24.3,23.55,24.2,644000,24.07,0.56,23.88,25.77,0.75
20260508,24.25,25.2,24.2,24.3,1500000,24.08,0.89,23.97,25.61,1.73
20260511,24.8,24.8,23.8,23.8,677000,24.06,-1.08,24.03,25.45,0.79
20260512,24.3,25.35,24.25,24.4,1068000,24.09,1.29,23.99,25.34,1.25
20260513,24.5,26.8,24.5,26.8,2664000,24.32,10.22,24.12,25.28,2.87
20260514,28,28.05,26.3,26.65,5315000,24.51,8.73,24.24,25.23,4.58
20260515,26.8,26.8,25.4,25.4,1586000,24.58,3.32,24.27,25.15,1.31
20260518,25,25.75,25,25.2,607000,24.64,2.29,24.27,25.09,0.5
20260519,25.3,26.1,24.95,25.3,1030000,24.69,2.47,24.28,25.04,0.84
20260520,25.3,25.45,24.75,24.75,615000,24.7,0.22,24.29,25,0.52
20260521,25.2,25.65,25,25.3,655000,24.75,2.24,24.34,24.96,0.56
20260522,25.65,25.75,25.25,25.45,25000,24.8,2.6,24.44,24.93,0.02
20260525,26,26.8,25.6,26.55,26000,24.95,6.41,24.63,24.94,0.02
20260526,27.2,27.25,26.2,26.75,27000,25.1,6.57,24.83,24.96,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.73
- over_600_ratio: 52.09
- over_800_ratio: 50.09
- over_1000_ratio: 47.56
- over_400_change_1w: 0.26
- over_800_change_1w: 0.06
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.92,,50.6,,48.16,,0,False,False
20260508,54.18,0.26,50.63,0.03,48.12,-0.04,1,False,True
20260515,54.47,0.29,50.03,-0.6,47.56,-0.56,2,False,False
20260522,54.73,0.26,50.09,0.06,47.56,0,3,False,True
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
