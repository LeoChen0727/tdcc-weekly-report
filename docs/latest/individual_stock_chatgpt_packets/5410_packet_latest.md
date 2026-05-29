# INDIVIDUAL STOCK CHATGPT PACKET - 5410 國眾

## Metadata
- generated_at: 2026-05-29 19:33:07 Asia/Taipei
- stock_id: 5410
- stock_name: 國眾
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5410_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5410_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5410_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5410_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5410_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5410_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5410_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5410_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5410_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5410_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5410_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5410_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5410_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5410.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5410.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5410.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5410.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5410.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5410.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5410_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5410_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5410_latest.md?ref=main

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
- open: 39.85
- high: 39.95
- low: 38.8
- close: 39.95
- volume: 39000
- ma5: 38.75
- ema23_primary: 36.82
- distance_to_ema23_pct: 8.51
- ma20: 37.21
- ma60: 33.15
- ma120: 31.8
- return_5d: 2.96
- return_20d: 21.8
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 7.36
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.25,33.3,32.85,33.05,441000,31.89,3.65,31.82,30.82,0.99
20260505,32.75,34,32.75,33.7,588000,32.04,5.19,32.01,30.88,1.26
20260506,33.5,35.2,33.35,34.8,1063000,32.27,7.85,32.25,30.95,2.09
20260507,38.25,38.25,36.5,36.5,4409000,32.62,11.9,32.56,31.05,6.17
20260508,36,37.55,35.85,36.7,1383000,32.96,11.35,32.89,31.16,1.79
20260511,36.9,37,36.3,37,578000,33.3,11.12,33.22,31.28,0.73
20260512,38.4,38.4,36.6,37.2,971000,33.62,10.64,33.47,31.4,1.33
20260513,37.2,37.2,36.6,36.8,439000,33.89,8.6,33.7,31.52,0.61
20260514,36.9,37.9,36.9,37.35,1117000,34.18,9.29,33.96,31.64,1.47
20260515,37.85,37.85,36.7,36.95,659000,34.41,7.39,34.19,31.75,0.84
20260518,36.9,38.25,36.35,37.7,975000,34.68,8.71,34.46,31.88,1.2
20260519,37.75,37.8,37.1,37.45,889000,34.91,7.27,34.73,32.01,1.07
20260520,37.25,37.95,37.25,37.85,648000,35.16,7.66,35.02,32.15,0.76
20260521,38,39,37.9,38.65,1013000,35.45,9.03,35.34,32.29,1.14
20260522,38.95,38.95,38.55,38.8,39000,35.73,8.6,35.64,32.43,0.05
20260525,39.05,39.4,38.05,38.7,39000,35.97,7.58,35.97,32.58,0.05
20260526,38.2,38.45,37.75,37.75,38000,36.12,4.5,36.26,32.7,0.05
20260527,38,38.75,37.7,38.35,38000,36.31,5.62,36.57,32.84,0.05
20260528,38.15,39.25,38.15,39,39000,36.53,6.75,36.85,32.98,0.05
20260529,39.85,39.95,38.8,39.95,39000,36.82,8.51,37.21,33.15,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 36.61
- over_600_ratio: 33.89
- over_800_ratio: 33.23
- over_1000_ratio: 30.32
- over_400_change_1w: 1.58
- over_800_change_1w: 1.96
- over_1000_change_1w: 0.99
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.04,,29.64,,26.67,,0,False,False
20260508,34.96,1.92,29.83,0.19,27.89,1.22,1,True,True
20260515,35.03,0.07,31.27,1.44,29.33,1.44,2,True,True
20260522,36.61,1.58,33.23,1.96,30.32,0.99,3,True,True
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
