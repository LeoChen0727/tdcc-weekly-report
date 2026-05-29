# INDIVIDUAL STOCK CHATGPT PACKET - 2732 六角

## Metadata
- generated_at: 2026-05-29 19:32:14 Asia/Taipei
- stock_id: 2732
- stock_name: 六角
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2732_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2732_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2732_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2732_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2732_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2732_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2732_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2732_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2732_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2732_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2732_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2732_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2732_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2732.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2732.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2732.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2732.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2732.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2732.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2732_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2732_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2732_latest.md?ref=main

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
- open: 64.9
- high: 65.4
- low: 63.5
- close: 64.2
- volume: 64000
- ma5: 63.76
- ema23_primary: 64.97
- distance_to_ema23_pct: -1.18
- ma20: 64.97
- ma60: 65.89
- ma120: 67.66
- return_5d: -1.83
- return_20d: -1.83
- volume_ratio: 1.13
- distance_to_ma20_pct_auxiliary: -1.19
- distance_to_high_60_pct: -8.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,65.5,65.5,65,65,64000,66.3,-1.96,66.31,66.36,1.39
20260505,65,65.3,64.9,64.9,44000,66.18,-1.94,66.17,66.3,0.93
20260506,64.9,65.1,64.2,64.7,42000,66.06,-2.06,66.1,66.25,0.87
20260507,64.7,65.1,64.5,65.1,88000,65.98,-1.33,65.98,66.2,1.72
20260508,66.5,67.5,65.1,66.9,170000,66.06,1.28,66.07,66.19,3
20260511,66.9,66.9,65.3,65.7,82000,66.03,-0.49,66.08,66.16,1.39
20260512,65.8,65.8,65.5,65.6,55000,65.99,-0.59,66.08,66.15,0.92
20260513,65.6,66.3,65.4,65.9,33000,65.98,-0.13,66.11,66.15,0.56
20260514,67,67,65.7,65.8,18000,65.97,-0.25,66.14,66.14,0.31
20260515,65.6,65.8,64.6,65.8,38000,65.95,-0.23,66.14,66.12,0.65
20260518,65,65.2,64.5,65.2,32000,65.89,-1.05,65.98,66.1,0.61
20260519,65.2,65.2,64.8,65,33000,65.82,-1.24,65.84,66.08,0.65
20260520,65,65,64.6,64.7,29000,65.72,-1.56,65.66,66.05,0.57
20260521,64.5,65,64.5,65,17000,65.66,-1.01,65.56,66.03,0.34
20260522,64.5,65.5,64.5,65.4,65000,65.64,-0.37,65.47,66.01,1.38
20260525,65.4,65.4,64.4,64.5,65000,65.55,-1.6,65.4,65.99,1.34
20260526,64.3,64.3,63.7,64,64000,65.42,-2.17,65.31,65.96,1.28
20260527,64,64,62.5,63.1,63000,65.22,-3.26,65.16,65.92,1.2
20260528,63.1,63.2,62.5,63,63000,65.04,-3.13,65.03,65.88,1.15
20260529,64.9,65.4,63.5,64.2,64000,64.97,-1.18,64.97,65.89,1.13
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.65
- over_600_ratio: 53.59
- over_800_ratio: 53.59
- over_1000_ratio: 53.59
- over_400_change_1w: -0.2
- over_800_change_1w: -0.2
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.62,,53.56,,53.56,,0,False,False
20260508,57.84,0.22,53.78,0.22,53.78,0.22,1,True,True
20260515,57.85,0.01,53.79,0.01,53.79,0.01,2,True,True
20260522,57.65,-0.2,53.59,-0.2,53.59,-0.2,0,False,False
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
