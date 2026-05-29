# INDIVIDUAL STOCK CHATGPT PACKET - 2066 世德

## Metadata
- generated_at: 2026-05-29 19:31:54 Asia/Taipei
- stock_id: 2066
- stock_name: 世德
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2066_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2066_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2066_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2066_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2066_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2066_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2066_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2066_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2066_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2066_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2066_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2066_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2066_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2066.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2066.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2066.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2066.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2066.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2066.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2066_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2066_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2066_latest.md?ref=main

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
- open: 59.3
- high: 59.6
- low: 57.1
- close: 58.3
- volume: 59000
- ma5: 57.42
- ema23_primary: 53.73
- distance_to_ema23_pct: 8.51
- ma20: 52.83
- ma60: 50.34
- ma120: 50.93
- return_5d: 0.69
- return_20d: 25.38
- volume_ratio: 0.4
- distance_to_ma20_pct_auxiliary: 10.36
- distance_to_high_60_pct: -4.58

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,46.5,46.5,45.1,45.85,53000,47.66,-3.79,47.56,50.18,0.92
20260505,45.9,45.9,45.1,45.3,38000,47.46,-4.55,47.36,50.01,0.65
20260506,45.4,45.95,44.5,44.85,54000,47.24,-5.06,47.1,49.81,0.89
20260507,44.85,44.95,44.5,44.6,60000,47.02,-5.15,46.85,49.64,0.98
20260508,44.7,44.7,43.6,44.1,62000,46.78,-5.73,46.57,49.48,0.97
20260511,43,47,43,47,67000,46.8,0.43,46.45,49.39,1.01
20260512,47.4,47.4,45.2,46,56000,46.73,-1.56,46.34,49.3,0.85
20260513,50.6,50.6,50.6,50.6,159000,47.05,7.54,46.52,49.28,2.3
20260514,55.6,55.6,55.6,55.6,163000,47.77,16.4,46.92,49.34,2.16
20260515,61.1,61.1,57.6,60.7,1216000,48.84,24.27,47.57,49.49,9.13
20260518,58.9,59.8,58,58,272000,49.61,16.92,48.16,49.62,1.95
20260519,58,59.3,57.7,57.7,148000,50.28,14.76,48.76,49.75,1.04
20260520,58,58,54.8,54.8,151000,50.66,8.18,49.17,49.83,1.04
20260521,55.6,56.8,55.2,56.4,125000,51.14,10.29,49.59,49.88,0.86
20260522,56.4,58,56.4,57.9,58000,51.7,11.99,50.1,49.96,0.4
20260525,58.3,59.8,57,57.6,58000,52.19,10.36,50.6,50.04,0.4
20260526,57.9,59,57.7,57.7,58000,52.65,9.59,51.18,50.13,0.41
20260527,57.7,57.7,55,55.7,56000,52.9,5.28,51.66,50.18,0.39
20260528,56.6,58.7,56.6,57.8,58000,53.31,8.42,52.23,50.24,0.4
20260529,59.3,59.6,57.1,58.3,59000,53.73,8.51,52.83,50.34,0.4
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.49
- over_600_ratio: 60.81
- over_800_ratio: 59.34
- over_1000_ratio: 53.56
- over_400_change_1w: -0.02
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.63,,59.33,,53.54,,0,False,False
20260508,68.59,-0.04,59.33,0,53.54,0,0,False,False
20260515,68.51,-0.08,59.31,-0.02,53.54,0,0,False,False
20260522,68.49,-0.02,59.34,0.03,53.56,0.02,1,False,True
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
