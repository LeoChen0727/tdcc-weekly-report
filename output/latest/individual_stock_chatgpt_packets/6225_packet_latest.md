# INDIVIDUAL STOCK CHATGPT PACKET - 6225 天瀚

## Metadata
- generated_at: 2026-05-26 21:26:19 Asia/Taipei
- stock_id: 6225
- stock_name: 天瀚
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 124
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6225_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6225_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6225_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6225_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6225_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6225_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6225_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6225_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6225_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6225_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6225_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6225_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6225_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6225.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6225.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6225.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6225.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6225.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6225.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6225_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6225_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6225_latest.md?ref=main

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
- open: 25.4
- high: 27.5
- low: 25.4
- close: 26
- volume: 80116
- ma5: 25.8
- ema23_primary: 25.19
- distance_to_ema23_pct: 3.21
- ma20: 25.56
- ma60: 22.02
- ma120: 19.66
- return_5d: -9.72
- return_20d: 42.08
- volume_ratio: 1.74
- distance_to_ma20_pct_auxiliary: 1.71
- distance_to_high_60_pct: -25.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,18.9,18.9,18.35,18.35,3274,18.94,-3.11,18.72,19.38,0.19
20260429,18.9,20.15,18.9,20.15,19338,19.04,5.83,18.76,19.43,1.1
20260430,20.15,22.15,20.15,20.45,37889,19.16,6.75,18.84,19.49,1.96
20260504,22,22.45,21.3,21.3,36982,19.34,10.16,18.95,19.57,1.77
20260505,21.3,23.4,21.3,22.4,22709,19.59,14.33,19.11,19.66,1.06
20260506,20.65,24.6,20.65,23.45,58895,19.91,17.76,19.3,19.76,2.42
20260507,25.75,25.75,24.05,24.05,47894,20.26,18.72,19.49,19.87,1.81
20260508,23.3,25.6,23.25,24.4,23451,20.6,18.43,19.7,19.99,0.85
20260511,24.9,26,24.5,24.9,28322,20.96,18.79,20,20.12,1.03
20260512,25.95,27.35,25.8,26.4,75957,21.41,23.28,20.38,20.25,2.45
20260513,26.9,29,26.9,29,64311,22.05,31.54,20.91,20.45,2.03
20260514,31.9,31.9,31.9,31.9,82374,22.87,39.5,21.59,20.69,2.36
20260515,35,35.05,34.95,35.05,83282,23.88,46.76,22.42,20.97,2.14
20260518,31.55,35.05,31.55,31.65,105988,24.53,29.03,23.05,21.18,2.43
20260519,29.2,29.5,28.8,28.8,48882,24.89,15.73,23.61,21.37,1.18
20260520,26.95,27.5,26.95,26.95,22270,25.06,7.55,24.09,21.51,0.55
20260521,26,26.95,25,26.05,36374,25.14,3.62,24.5,21.64,0.88
20260522,26.2,26.85,25,25,18356,25.13,-0.51,24.84,21.77,0.44
20260525,26.3,27.5,25,25,24737,25.12,-0.47,25.18,21.89,0.58
20260526,25.4,27.5,25.4,26,80116,25.19,3.21,25.56,22.02,1.74
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.01
- over_600_ratio: 56.46
- over_800_ratio: 54.13
- over_1000_ratio: 50.7
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
20260430,64.01,,54.13,,50.7,,0,False,False
20260508,64.01,0,54.13,0,50.7,0,0,False,False
20260515,64.01,0,54.13,0,50.7,0,0,False,False
20260522,64.01,0,54.13,0,50.7,0,0,False,False
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
