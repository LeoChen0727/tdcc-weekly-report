# INDIVIDUAL STOCK CHATGPT PACKET - 4192 杏國

## Metadata
- generated_at: 2026-05-29 19:32:48 Asia/Taipei
- stock_id: 4192
- stock_name: 杏國
- packet_status: standard_rawdata_packet
- latest_price_date: 20260529
- price_rows: 116
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4192_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4192_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4192_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4192_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4192_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4192_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4192_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4192_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4192_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4192_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4192_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4192_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4192_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4192.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4192.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4192.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4192.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4192.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4192.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4192_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4192_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4192_latest.md?ref=main

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
- open: 19.5
- high: 20
- low: 19.5
- close: 20
- volume: 20000
- ma5: 19.84
- ema23_primary: 20.14
- distance_to_ema23_pct: -0.68
- ma20: 20.05
- ma60: 20.64
- ma120: 22.85
- return_5d: 0
- return_20d: 1.01
- volume_ratio: 1.17
- distance_to_ma20_pct_auxiliary: -0.24
- distance_to_high_60_pct: -14.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260420,19.7,19.7,19.5,19.5,14000,20.48,-4.8,20.27,21.92,1.54
20260421,20,20,19.3,19.9,13000,20.44,-2.62,20.24,21.85,1.35
20260423,19.9,19.9,19.5,19.55,11000,20.36,-3.99,20.19,21.78,1.23
20260424,19.5,19.85,19.5,19.85,14000,20.32,-2.31,20.18,21.7,1.48
20260427,19.7,19.95,19.7,19.95,11000,20.29,-1.67,20.18,21.62,1.2
20260430,19.5,19.6,19.5,19.6,8000,20.23,-3.12,20.16,21.55,0.85
20260504,19.15,20.6,19,20.6,45000,20.26,1.67,20.19,21.49,4.09
20260505,20.6,20.6,20,20,7000,20.24,-1.19,20.18,21.41,0.7
20260506,20.05,20.45,19.95,20.45,41000,20.26,0.95,20.18,21.34,3.4
20260507,20.4,20.9,20.1,20.8,25000,20.3,2.45,20.19,21.28,1.93
20260508,20.1,20.8,20,20.5,19000,20.32,0.89,20.21,21.22,1.38
20260511,20.05,20.05,20.05,20.05,10000,20.3,-1.22,20.19,21.15,0.71
20260512,19.5,21,19.5,21,8000,20.36,3.17,20.22,21.09,0.57
20260518,20,20,20,20,2000,20.33,-1.6,20.19,21.02,0.14
20260521,19.65,20,19.65,20,16000,20.3,-1.47,20.17,20.96,1.1
20260522,19.4,20.1,19.4,19.8,20000,20.26,-2.26,20.14,20.89,1.3
20260525,19.8,20,19.8,19.95,20000,20.23,-1.39,20.11,20.82,1.24
20260527,19.75,19.95,19.15,19.95,19000,20.21,-1.28,20.09,20.76,1.12
20260528,19.5,19.5,19.5,19.5,19000,20.15,-3.22,20.04,20.69,1.12
20260529,19.5,20,19.5,20,20000,20.14,-0.68,20.05,20.64,1.17
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 67.91
- over_600_ratio: 66.6
- over_800_ratio: 66.6
- over_1000_ratio: 66.6
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
20260430,67.87,,66.6,,66.6,,0,False,False
20260508,67.89,0.02,66.6,0,66.6,0,1,False,False
20260515,67.91,0.02,66.6,0,66.6,0,2,False,False
20260522,67.91,0,66.6,0,66.6,0,0,False,False
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
