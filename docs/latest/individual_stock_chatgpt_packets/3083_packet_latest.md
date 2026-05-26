# INDIVIDUAL STOCK CHATGPT PACKET - 3083 網龍

## Metadata
- generated_at: 2026-05-26 23:01:06 Asia/Taipei
- stock_id: 3083
- stock_name: 網龍
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3083_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3083_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3083_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3083_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3083_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3083_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3083_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3083_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3083_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3083_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3083_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3083_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3083_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3083.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3083.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3083.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3083.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3083.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3083.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3083_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3083_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3083_latest.md?ref=main

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
- high: 27.2
- low: 26.65
- close: 26.95
- volume: 27000
- ma5: 27.53
- ema23_primary: 27.23
- distance_to_ema23_pct: -1.02
- ma20: 27.08
- ma60: 27.67
- ma120: 30.93
- return_5d: -2.71
- return_20d: 0.19
- volume_ratio: 0.19
- distance_to_ma20_pct_auxiliary: -0.49
- distance_to_high_60_pct: -12.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,26.9,27.1,26.85,27.05,61000,27.45,-1.45,27.1,29.64,0.49
20260429,27.5,27.5,27.1,27.15,70000,27.42,-0.99,27.1,29.49,0.57
20260430,27.65,27.65,27.15,27.25,84000,27.41,-0.58,27.12,29.35,0.69
20260504,27.25,27.25,26.65,26.9,157000,27.37,-1.7,27.1,29.2,1.25
20260505,26.9,27,26.7,26.75,86000,27.31,-2.07,27.09,29.04,0.69
20260506,27.55,27.55,26.8,26.85,163000,27.28,-1.56,27.08,28.9,1.23
20260507,27.05,27.05,26.8,26.95,93000,27.25,-1.09,27.07,28.77,0.69
20260508,27.3,27.3,26.65,26.9,127000,27.22,-1.17,27.08,28.64,0.94
20260511,26.9,27,26.75,26.8,80000,27.18,-1.41,27.05,28.52,0.6
20260512,27.05,27.05,26.45,26.8,164000,27.15,-1.3,27.03,28.41,1.19
20260513,26.8,26.9,26.3,26.45,126000,27.09,-2.38,26.98,28.31,0.9
20260514,26.45,26.5,26,26.15,156000,27.02,-3.2,26.92,28.19,1.1
20260515,26.45,27.85,26.25,27.35,398000,27.04,1.14,26.93,28.1,2.57
20260518,27.35,27.35,26.6,26.95,99000,27.04,-0.32,26.93,28.02,0.64
20260519,27.2,28.2,27,27.7,390000,27.09,2.25,26.97,27.94,2.36
20260520,28.4,28.5,27.65,28,299000,27.17,3.07,27.04,27.87,1.81
20260521,28.6,28.6,27.85,27.85,154000,27.22,2.3,27.05,27.82,0.97
20260522,28.1,28.2,27.5,27.7,28000,27.26,1.6,27.09,27.77,0.19
20260525,28.25,28.25,26.85,27.15,27000,27.25,-0.38,27.08,27.72,0.19
20260526,27.2,27.2,26.65,26.95,27000,27.23,-1.02,27.08,27.67,0.19
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.61
- over_600_ratio: 55.08
- over_800_ratio: 55.08
- over_1000_ratio: 53.1
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.64,,55.08,,53.1,,0,False,False
20260508,56.59,-0.05,55.08,0,53.1,0,0,False,False
20260515,56.6,0.01,55.08,0,53.1,0,1,False,False
20260522,56.61,0.01,55.08,0,53.1,0,2,False,False
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
