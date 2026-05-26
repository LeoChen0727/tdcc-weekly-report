# INDIVIDUAL STOCK CHATGPT PACKET - 1909 榮成

## Metadata
- generated_at: 2026-05-26 21:24:49 Asia/Taipei
- stock_id: 1909
- stock_name: 榮成
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1909_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1909_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1909_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1909_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1909_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1909_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1909_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1909_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1909_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1909_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1909_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1909_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1909_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1909.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1909.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1909.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1909.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1909.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1909.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1909_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1909_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1909_latest.md?ref=main

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
- open: 8.93
- high: 8.96
- low: 8.82
- close: 8.91
- volume: 3528356
- ma5: 8.95
- ema23_primary: 9.11
- distance_to_ema23_pct: -2.2
- ma20: 9.05
- ma60: 9.4
- ma120: 9.8
- return_5d: -1.44
- return_20d: -1.33
- volume_ratio: 1.25
- distance_to_ma20_pct_auxiliary: -1.55
- distance_to_high_60_pct: -20.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,9.05,9.14,9,9.13,1509207,9.51,-3.99,9.69,9.66,0.24
20260429,9.18,9.21,9.08,9.21,1739461,9.48,-2.9,9.62,9.65,0.36
20260430,9.21,9.21,9.02,9.05,2398789,9.45,-4.22,9.54,9.64,0.65
20260504,9.05,9.1,8.98,9.01,2992298,9.41,-4.27,9.48,9.63,0.92
20260505,8.98,9.02,8.94,9.02,2210984,9.38,-3.83,9.43,9.61,0.72
20260506,9.03,9.04,8.94,8.97,3642525,9.35,-4.01,9.39,9.59,1.17
20260507,8.93,9.18,8.8,9.16,4351962,9.33,-1.82,9.37,9.58,1.46
20260508,9.19,9.25,9.11,9.17,2371119,9.32,-1.57,9.34,9.56,0.81
20260511,9.18,9.31,9.15,9.27,3075118,9.31,-0.46,9.31,9.55,1.05
20260512,9.2,9.33,9.16,9.19,2815831,9.3,-1.21,9.28,9.54,0.96
20260513,9.1,9.14,9.04,9.11,3150389,9.29,-1.9,9.24,9.53,1.05
20260514,9.01,9.06,8.91,8.95,4181912,9.26,-3.33,9.21,9.52,1.37
20260515,8.93,9.24,8.93,8.97,2939791,9.23,-2.86,9.17,9.51,0.94
20260518,8.9,9.01,8.87,9,2285414,9.21,-2.33,9.14,9.5,0.74
20260519,8.92,9.12,8.92,9.04,2329379,9.2,-1.74,9.13,9.48,0.77
20260520,8.97,8.99,8.9,8.95,2280641,9.18,-2.5,9.1,9.47,0.76
20260521,8.9,9.02,8.9,9.02,1865108,9.17,-1.59,9.08,9.45,0.63
20260522,8.95,9,8.93,8.96,2533307,9.15,-2.06,9.07,9.44,0.91
20260525,8.92,8.94,8.81,8.91,4443020,9.13,-2.4,9.06,9.42,1.56
20260526,8.93,8.96,8.82,8.91,3528356,9.11,-2.2,9.05,9.4,1.25
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.15
- over_600_ratio: 63.95
- over_800_ratio: 62.69
- over_1000_ratio: 61.73
- over_400_change_1w: -0.04
- over_800_change_1w: 0
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.09,,62.77,,61.53,,0,False,False
20260508,66.18,0.09,62.91,0.14,61.73,0.2,1,True,True
20260515,66.19,0.01,62.69,-0.22,61.66,-0.07,2,False,False
20260522,66.15,-0.04,62.69,0,61.73,0.07,3,False,True
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
