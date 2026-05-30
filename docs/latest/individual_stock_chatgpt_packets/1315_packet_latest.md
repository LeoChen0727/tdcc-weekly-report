# INDIVIDUAL STOCK CHATGPT PACKET - 1315 達新

## Metadata
- generated_at: 2026-05-30 23:40:54 Asia/Taipei
- stock_id: 1315
- stock_name: 達新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 265
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1315_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1315_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1315_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1315_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1315_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1315_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1315_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1315_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1315_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1315_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1315_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1315_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1315_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1315.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1315.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1315.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1315.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1315.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1315.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1315_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1315_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1315_latest.md?ref=main

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
- open: 61.8
- high: 62
- low: 61.6
- close: 61.6
- volume: 34247
- ma5: 61.36
- ema23_primary: 61.71
- distance_to_ema23_pct: -0.18
- ma20: 61.35
- ma60: 62.99
- ma120: 63.75
- return_5d: 1.15
- return_20d: -1.12
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: 0.4
- distance_to_high_60_pct: -9.28

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,62.4,62.5,62.1,62.2,18333,63.67,-2.31,63.98,64.04,0.44
20260505,62.3,62.4,62.1,62.2,15891,63.55,-2.13,63.94,64.01,0.38
20260506,62.6,62.6,62.1,62.4,27155,63.46,-1.66,63.9,63.97,0.64
20260507,62.3,62.3,61.5,61.5,65018,63.29,-2.83,63.77,63.92,1.46
20260508,62,62,61.6,61.8,15048,63.17,-2.17,63.62,63.87,0.37
20260511,61.6,61.8,61.6,61.8,17717,63.05,-1.99,63.47,63.82,0.43
20260512,61.8,62,61.5,61.5,21816,62.92,-2.26,63.34,63.78,0.56
20260513,61.3,61.7,60.9,61.7,37020,62.82,-1.79,63.2,63.74,0.93
20260514,61.2,61.4,60.7,61.1,32711,62.68,-2.52,63.04,63.69,0.81
20260515,61.4,61.4,60.4,60.5,35788,62.5,-3.2,62.83,63.63,0.89
20260518,61,61.2,60.3,60.3,16071,62.31,-3.23,62.6,63.57,0.4
20260519,60.5,61,60.3,61,8654,62.2,-1.94,62.37,63.52,0.23
20260520,60.4,60.4,60.3,60.4,5331,62.05,-2.67,62.11,63.45,0.14
20260521,60.6,61.2,60.6,61,29808,61.97,-1.56,61.89,63.38,0.84
20260522,60.4,61.1,60.4,60.9,21263,61.88,-1.58,61.65,63.31,0.7
20260525,60.9,60.9,60.5,60.9,16973,61.8,-1.45,61.56,63.23,0.65
20260526,60.9,61,60.7,60.7,15004,61.7,-1.63,61.48,63.15,0.58
20260527,61,62,61,62,130171,61.73,0.44,61.45,63.1,4.1
20260528,62,63,61.5,61.6,51199,61.72,-0.19,61.39,63.05,1.53
20260529,61.8,62,61.6,61.6,34247,61.71,-0.18,61.35,62.99,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 80.72
- over_600_ratio: 75.44
- over_800_ratio: 71.24
- over_1000_ratio: 70.27
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
20260430,80.71,,71.24,,70.27,,0,False,False
20260508,80.71,0,71.24,0,70.27,0,0,False,False
20260515,80.71,0,71.24,0,70.27,0,0,False,False
20260522,80.72,0.01,71.24,0,70.27,0,1,False,False
20260529,80.72,0,71.24,0,70.27,0,0,False,False
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
