# INDIVIDUAL STOCK CHATGPT PACKET - 1512 瑞利

## Metadata
- generated_at: 2026-05-28 19:31:34 Asia/Taipei
- stock_id: 1512
- stock_name: 瑞利
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1512_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1512_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1512_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1512_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1512_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1512_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1512_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1512_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1512_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1512_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1512_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1512_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1512_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1512.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1512.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1512.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1512.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1512.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1512.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1512_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1512_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1512_latest.md?ref=main

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
- open: 6.51
- high: 6.91
- low: 6.5
- close: 6.89
- volume: 161485
- ma5: 6.92
- ema23_primary: 7.1
- distance_to_ema23_pct: -2.92
- ma20: 7.11
- ma60: 7.35
- ma120: 7.56
- return_5d: -1.01
- return_20d: -8.13
- volume_ratio: 1.65
- distance_to_ma20_pct_auxiliary: -3.07
- distance_to_high_60_pct: -19.04

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,7.5,7.6,7.4,7.48,28922,7.43,0.72,7.4,7.64,0.26
20260504,7.48,7.48,7.39,7.45,95871,7.43,0.29,7.38,7.63,0.92
20260505,7.45,7.45,7.25,7.32,61013,7.42,-1.34,7.37,7.61,0.59
20260506,7.66,7.66,7.3,7.35,133451,7.41,-0.86,7.37,7.6,1.25
20260507,7.3,7.34,7.24,7.28,105493,7.4,-1.65,7.36,7.58,1
20260508,7.45,7.45,7.2,7.35,48022,7.4,-0.65,7.36,7.57,0.47
20260511,7.23,7.3,7.2,7.21,123610,7.38,-2.33,7.34,7.55,1.19
20260512,7.21,7.21,7.1,7.13,176493,7.36,-3.14,7.34,7.54,1.7
20260513,7.14,7.18,7.02,7.03,147339,7.33,-4.14,7.33,7.52,1.4
20260514,7.02,7.05,6.92,6.96,205565,7.3,-4.69,7.31,7.51,1.89
20260515,6.96,7.1,6.95,6.96,87137,7.27,-4.32,7.28,7.49,0.82
20260518,6.87,7,6.75,6.96,25009,7.25,-3.97,7.26,7.48,0.24
20260519,7.23,7.23,6.91,7.01,10385,7.23,-3.02,7.24,7.46,0.11
20260520,6.82,7.24,6.79,7.1,44195,7.22,-1.63,7.23,7.45,0.45
20260521,7.1,7.1,6.84,6.96,101510,7.2,-3.28,7.21,7.43,1.05
20260522,6.87,6.99,6.84,6.99,77500,7.18,-2.63,7.2,7.41,0.84
20260525,6.97,7,6.85,6.97,153839,7.16,-2.67,7.18,7.4,1.66
20260526,7.05,7.05,6.86,6.94,73788,7.14,-2.84,7.17,7.38,0.8
20260527,6.94,6.96,6.81,6.82,97343,7.12,-4.16,7.14,7.37,1.03
20260528,6.51,6.91,6.5,6.89,161485,7.1,-2.92,7.11,7.35,1.65
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.27
- over_600_ratio: 49.94
- over_800_ratio: 47.8
- over_1000_ratio: 47.8
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.25,,47.81,,47.81,,0,False,False
20260508,54.28,0.03,47.81,0,47.81,0,1,False,False
20260515,54.28,0,47.81,0,47.81,0,0,False,False
20260522,54.27,-0.01,47.8,-0.01,47.8,-0.01,0,False,False
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
