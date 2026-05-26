# INDIVIDUAL STOCK CHATGPT PACKET - 3285 微端

## Metadata
- generated_at: 2026-05-26 21:25:28 Asia/Taipei
- stock_id: 3285
- stock_name: 微端
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3285_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3285_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3285_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3285_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3285_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3285_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3285_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3285_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3285_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3285_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3285_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3285_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3285_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3285.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3285.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3285.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3285.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3285.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3285.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3285_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3285_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3285_latest.md?ref=main

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
- open: 29.3
- high: 29.45
- low: 29.15
- close: 29.35
- volume: 29000
- ma5: 28.87
- ema23_primary: 28.7
- distance_to_ema23_pct: 2.26
- ma20: 28.71
- ma60: 28.54
- ma120: 28.51
- return_5d: 2.98
- return_20d: 4.63
- volume_ratio: 1.14
- distance_to_ma20_pct_auxiliary: 2.23
- distance_to_high_60_pct: -3.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,28.05,28.2,27.9,28.05,28000,28.3,-0.88,28.28,28.53,1.35
20260429,28.05,28.05,28.05,28.05,6000,28.28,-0.81,28.31,28.52,0.3
20260430,28.4,28.7,28.05,28.5,13000,28.3,0.71,28.37,28.53,0.67
20260504,28.5,30.3,28.4,28.85,61000,28.34,1.79,28.4,28.55,2.76
20260505,28.85,29.3,28.6,29.3,57000,28.42,3.08,28.47,28.58,2.47
20260506,29.3,29.3,28.6,28.6,28000,28.44,0.57,28.48,28.59,1.17
20260507,29.1,29.1,28.5,28.55,15000,28.45,0.36,28.45,28.61,0.62
20260508,28.15,29.3,28.15,29.25,16000,28.51,2.58,28.48,28.65,0.65
20260511,29.55,29.55,28.9,29,16000,28.55,1.56,28.48,28.68,0.64
20260512,28.9,28.9,28.5,28.5,12000,28.55,-0.18,28.46,28.71,0.48
20260513,28.9,28.9,28.25,28.4,6000,28.54,-0.48,28.44,28.69,0.24
20260514,28.4,28.4,28.3,28.35,7000,28.52,-0.6,28.45,28.65,0.3
20260515,28.25,29,28,29,59000,28.56,1.53,28.48,28.63,2.28
20260518,28.5,28.95,28.25,28.95,19000,28.59,1.24,28.51,28.63,0.72
20260519,28.8,28.8,28.5,28.5,14000,28.59,-0.3,28.54,28.61,0.55
20260520,28.9,29.3,28.5,28.5,55000,28.58,-0.28,28.56,28.59,2.03
20260521,28.5,28.55,28.25,28.55,9000,28.58,-0.09,28.57,28.57,0.35
20260522,28.5,29.1,28.5,28.8,29000,28.6,0.72,28.59,28.55,1.15
20260525,29,29.15,28.8,29.15,29000,28.64,1.77,28.64,28.54,1.1
20260526,29.3,29.45,29.15,29.35,29000,28.7,2.26,28.71,28.54,1.14
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.36
- over_600_ratio: 57.17
- over_800_ratio: 55.68
- over_1000_ratio: 48.75
- over_400_change_1w: 0.06
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.28,,55.66,,48.74,,0,False,False
20260508,64.29,0.01,55.67,0.01,48.74,0,1,False,True
20260515,64.3,0.01,55.67,0,48.74,0,2,False,False
20260522,64.36,0.06,55.68,0.01,48.75,0.01,3,True,True
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
