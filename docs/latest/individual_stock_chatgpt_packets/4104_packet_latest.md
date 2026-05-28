# INDIVIDUAL STOCK CHATGPT PACKET - 4104 佳醫

## Metadata
- generated_at: 2026-05-28 20:19:23 Asia/Taipei
- stock_id: 4104
- stock_name: 佳醫
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4104_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4104_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4104_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4104_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4104_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4104_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4104_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4104_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4104_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4104_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4104_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4104_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4104_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4104.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4104.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4104.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4104.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4104.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4104.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4104_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4104_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4104_latest.md?ref=main

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
- open: 70.8
- high: 70.8
- low: 69.4
- close: 69.5
- volume: 373431
- ma5: 70.06
- ema23_primary: 70.97
- distance_to_ema23_pct: -2.07
- ma20: 69.96
- ma60: 74.48
- ma120: 77.19
- return_5d: -1.84
- return_20d: -3.34
- volume_ratio: 0.91
- distance_to_ma20_pct_auxiliary: -0.66
- distance_to_high_60_pct: -12.58

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,71.9,71.9,71.3,71.4,356158,75.76,-5.76,76.62,77.04,0.94
20260504,71.5,71.5,70.7,70.9,444567,75.36,-5.92,76.3,76.91,1.13
20260505,70.9,70.9,70.4,70.8,297651,74.98,-5.57,75.94,76.76,0.75
20260506,70.8,70.8,70.4,70.6,362585,74.61,-5.38,75.58,76.61,0.89
20260507,70.5,70.7,70.1,70.6,408358,74.28,-4.95,75.23,76.47,0.99
20260508,70.5,71.2,70.4,70.6,369575,73.97,-4.56,74.88,76.33,0.88
20260511,70.6,70.8,70,70.2,529630,73.66,-4.69,74.48,76.19,1.22
20260512,70.2,70.2,69.5,69.7,565881,73.33,-4.95,74.05,76.05,1.26
20260513,69.7,69.7,68.8,69.3,660003,72.99,-5.06,73.58,75.93,1.41
20260514,69.2,69.4,68.5,68.5,578798,72.62,-5.67,73.08,75.81,1.19
20260515,68.5,68.8,68,68.1,611889,72.24,-5.73,72.51,75.67,1.21
20260518,68,68.4,67.3,68.1,361372,71.9,-5.28,71.96,75.53,0.71
20260519,68.1,69.3,67.9,68.7,379199,71.63,-4.09,71.44,75.41,0.75
20260520,69.4,70.6,68.9,70.6,428022,71.54,-1.32,71.04,75.29,0.87
20260521,70.6,70.8,70.1,70.8,199258,71.48,-0.95,70.65,75.18,0.43
20260522,70.8,70.8,70,70.4,159361,71.39,-1.39,70.47,75.04,0.38
20260525,70.2,70.2,69.1,70,385689,71.28,-1.79,70.31,74.89,0.93
20260526,70,70.4,69.3,70,315856,71.17,-1.64,70.19,74.75,0.79
20260527,70.3,70.8,70.1,70.4,396511,71.11,-0.99,70.08,74.62,0.98
20260528,70.8,70.8,69.4,69.5,373431,70.97,-2.07,69.96,74.48,0.91
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.89
- over_600_ratio: 42.98
- over_800_ratio: 40.85
- over_1000_ratio: 39.53
- over_400_change_1w: 0.29
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.18,,40.85,,39.53,,0,False,False
20260508,45.61,-0.57,40.85,0,39.53,0,0,False,False
20260515,45.6,-0.01,40.85,0,39.53,0,1,False,False
20260522,45.89,0.29,40.85,0,39.53,0,2,False,False
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
