# INDIVIDUAL STOCK CHATGPT PACKET - 2425 承啟

## Metadata
- generated_at: 2026-05-26 23:00:42 Asia/Taipei
- stock_id: 2425
- stock_name: 承啟
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2425_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2425_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2425_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2425_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2425_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2425_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2425_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2425_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2425_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2425_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2425_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2425_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2425_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2425.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2425.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2425.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2425.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2425.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2425.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2425_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2425_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2425_latest.md?ref=main

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
- open: 35.2
- high: 35.45
- low: 34.4
- close: 34.9
- volume: 687851
- ma5: 34.26
- ema23_primary: 32.72
- distance_to_ema23_pct: 6.67
- ma20: 32.76
- ma60: 30.08
- ma120: 29.84
- return_5d: 7.38
- return_20d: 18.31
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: 6.55
- distance_to_high_60_pct: -2.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,29.7,30.35,29.05,30,225394,29.37,2.16,28.8,28.87,0.5
20260429,30.35,30.35,29.75,29.85,138419,29.41,1.51,28.93,28.85,0.31
20260430,30.3,31.1,30.15,30.3,642177,29.48,2.78,29.13,28.84,1.36
20260504,30.65,31.3,30.45,30.85,617415,29.59,4.24,29.34,28.84,1.25
20260505,31.2,32.35,31,32.25,870100,29.82,8.16,29.65,28.87,1.65
20260506,32.7,32.7,31.2,31.55,723057,29.96,5.31,29.92,28.89,1.3
20260507,31.05,31.3,30.65,31,552052,30.05,3.17,30.12,28.9,0.97
20260508,31,31.9,30.5,30.85,443717,30.11,2.44,30.32,28.93,0.76
20260511,32.85,33.8,32.85,32.9,2021491,30.35,8.42,30.63,29,3.01
20260512,33.7,34.6,33.1,34,1871812,30.65,10.93,30.86,29.1,2.51
20260513,33.9,34.5,33.2,33.6,948638,30.9,8.75,31.02,29.18,1.32
20260514,33.65,35.4,33.65,35.2,2092642,31.25,12.62,31.22,29.28,2.8
20260515,35.4,35.95,34.3,34.6,1923583,31.53,9.72,31.39,29.38,2.36
20260518,34.3,35.4,33.8,34.35,763815,31.77,8.13,31.6,29.48,0.92
20260519,34.5,34.6,32.4,32.5,808578,31.83,2.11,31.73,29.56,0.95
20260520,32.6,33.2,32.3,32.65,347679,31.9,2.36,31.8,29.63,0.42
20260521,33.3,34.5,33.05,34.05,575172,32.08,6.15,31.96,29.74,0.68
20260522,34.4,34.85,34.15,34.7,618830,32.3,7.44,32.22,29.85,0.73
20260525,35,35.65,34.85,35,877321,32.52,7.62,32.48,29.96,1.01
20260526,35.2,35.45,34.4,34.9,687851,32.72,6.67,32.76,30.08,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.89
- over_600_ratio: 43.82
- over_800_ratio: 39.73
- over_1000_ratio: 37.91
- over_400_change_1w: 0.44
- over_800_change_1w: 1.02
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.71,,39.98,,39.03,,0,False,False
20260508,46.73,0.02,39.13,-0.85,38.18,-0.85,1,False,False
20260515,47.45,0.72,38.71,-0.42,37.76,-0.42,2,False,False
20260522,47.89,0.44,39.73,1.02,37.91,0.15,3,True,True
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
