# INDIVIDUAL STOCK CHATGPT PACKET - 6248 沛波

## Metadata
- generated_at: 2026-05-30 23:42:59 Asia/Taipei
- stock_id: 6248
- stock_name: 沛波
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6248_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6248_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6248_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6248_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6248_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6248_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6248_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6248_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6248_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6248_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6248_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6248_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6248_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6248.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6248.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6248.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6248.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6248.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6248.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6248_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6248_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6248_latest.md?ref=main

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
- open: 18.4
- high: 18.5
- low: 18.35
- close: 18.45
- volume: 18000
- ma5: 18.64
- ema23_primary: 18.88
- distance_to_ema23_pct: -2.3
- ma20: 18.82
- ma60: 19.66
- ma120: 20.08
- return_5d: 1.1
- return_20d: -5.63
- volume_ratio: 0.25
- distance_to_ma20_pct_auxiliary: -1.94
- distance_to_high_60_pct: -13.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,19.55,19.55,19.3,19.5,113000,19.91,-2.07,19.9,20.57,0.86
20260505,19.45,19.45,19.3,19.3,112000,19.86,-2.83,19.86,20.54,0.84
20260506,19.35,19.5,19.25,19.5,104000,19.83,-1.67,19.84,20.51,0.76
20260507,19.5,19.65,19.4,19.6,117000,19.81,-1.07,19.81,20.48,0.84
20260508,19.6,19.6,19.1,19.6,184000,19.79,-0.98,19.78,20.44,1.28
20260511,19.45,19.45,19.3,19.3,71000,19.75,-2.3,19.74,20.4,0.5
20260512,19.25,19.25,18.9,18.95,136000,19.69,-3.74,19.68,20.36,0.98
20260513,18.85,18.85,18.65,18.75,116000,19.61,-4.38,19.62,20.31,0.85
20260514,18.75,18.75,18.5,18.55,105000,19.52,-4.97,19.54,20.26,0.79
20260515,18.55,18.65,18.4,18.55,79000,19.44,-4.58,19.47,20.21,0.62
20260518,18.4,18.55,18.3,18.45,27000,19.36,-4.69,19.39,20.15,0.22
20260519,18.45,18.45,18.2,18.3,34000,19.27,-5.03,19.3,20.09,0.3
20260520,18.3,18.3,18.1,18.25,99000,19.18,-4.87,19.22,20.03,0.86
20260521,18.3,18.3,18.2,18.25,45000,19.11,-4.48,19.14,19.97,0.41
20260522,18.25,18.3,18.05,18.25,18000,19.03,-4.12,19.07,19.91,0.18
20260525,18.35,19.2,18.35,19.2,19000,19.05,0.79,19.04,19.86,0.21
20260526,19.5,19.5,18.8,18.8,19000,19.03,-1.2,19,19.81,0.23
20260527,18.65,18.65,18.4,18.4,18000,18.98,-3.03,18.93,19.75,0.24
20260528,18.4,18.5,18.3,18.35,18000,18.92,-3.03,18.87,19.7,0.24
20260529,18.4,18.5,18.35,18.45,18000,18.88,-2.3,18.82,19.66,0.25
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 49.25
- over_600_ratio: 46.15
- over_800_ratio: 44.83
- over_1000_ratio: 43.98
- over_400_change_1w: 0
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.19,,44.78,,43.93,,0,False,False
20260508,49.29,0.1,44.88,0.1,44.03,0.1,1,True,True
20260515,49.23,-0.06,44.82,-0.06,43.97,-0.06,0,False,False
20260522,49.25,0.02,44.84,0.02,43.99,0.02,1,True,True
20260529,49.25,0,44.83,-0.01,43.98,-0.01,0,False,False
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
