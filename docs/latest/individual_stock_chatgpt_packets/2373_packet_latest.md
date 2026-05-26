# INDIVIDUAL STOCK CHATGPT PACKET - 2373 震旦行

## Metadata
- generated_at: 2026-05-26 23:00:39 Asia/Taipei
- stock_id: 2373
- stock_name: 震旦行
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2373_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2373_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2373_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2373_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2373_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2373_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2373_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2373_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2373_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2373_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2373_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2373_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2373_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2373.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2373.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2373.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2373.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2373.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2373.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2373_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2373_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2373_latest.md?ref=main

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
- open: 57.3
- high: 57.4
- low: 56.6
- close: 57.2
- volume: 25694
- ma5: 56.92
- ema23_primary: 56.72
- distance_to_ema23_pct: 0.84
- ma20: 56.69
- ma60: 56.51
- ma120: 56.26
- return_5d: 1.96
- return_20d: 0.53
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: 0.9
- distance_to_high_60_pct: -3.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,56.9,57.3,56.9,56.9,45599,57,-0.17,57.02,55.99,1.07
20260429,58.4,58.4,57.1,57.6,20816,57.05,0.97,57.12,56.03,0.49
20260430,57.5,57.8,57,57.1,43221,57.05,0.09,57.19,56.08,0.98
20260504,57.1,57.1,56.9,56.9,23575,57.04,-0.24,57.21,56.12,0.56
20260505,56.9,57,56.7,56.7,25926,57.01,-0.54,57.24,56.15,0.61
20260506,57,57.5,56.7,57.5,58625,57.05,0.79,57.31,56.19,1.32
20260507,57.5,57.6,56.7,56.8,63764,57.03,-0.4,57.31,56.22,1.42
20260508,57,57.3,56.3,56.8,51467,57.01,-0.37,57.33,56.25,1.1
20260511,56.8,57.5,56.4,56.4,66729,56.96,-0.98,57.3,56.27,1.4
20260512,58,58,56.6,56.6,44949,56.93,-0.58,57.3,56.31,0.94
20260513,56.7,56.7,55.9,56.3,22146,56.88,-1.01,57.26,56.35,0.48
20260514,56.3,57.3,55.7,55.7,61880,56.78,-1.9,57.17,56.36,1.33
20260515,56.2,56.2,55.7,55.8,34079,56.7,-1.58,57.09,56.38,0.77
20260518,56.6,56.6,55.9,56,23293,56.64,-1.13,56.98,56.41,0.57
20260519,55.9,56.4,55.6,56.1,38975,56.59,-0.87,56.87,56.43,0.97
20260520,56.4,56.7,56.1,56.5,51846,56.59,-0.15,56.76,56.46,1.31
20260521,56.5,57.7,56.5,56.8,45778,56.6,0.35,56.69,56.48,1.12
20260522,56.6,58,56.4,56.8,102486,56.62,0.32,56.67,56.49,2.29
20260525,57.3,57.8,56.8,57.3,37534,56.68,1.1,56.67,56.5,0.83
20260526,57.3,57.4,56.6,57.2,25694,56.72,0.84,56.69,56.51,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 87.18
- over_600_ratio: 87.18
- over_800_ratio: 86.01
- over_1000_ratio: 86.01
- over_400_change_1w: -0.19
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.36,,86.01,,86.01,,0,False,False
20260508,87.36,0,86.01,0,86.01,0,0,False,False
20260515,87.37,0.01,86.01,0,86.01,0,1,False,False
20260522,87.18,-0.19,86.01,0,86.01,0,0,False,False
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
