# INDIVIDUAL STOCK CHATGPT PACKET - 1336 台翰

## Metadata
- generated_at: 2026-05-29 19:31:37 Asia/Taipei
- stock_id: 1336
- stock_name: 台翰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1336_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1336_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1336_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1336_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1336_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1336_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1336_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1336_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1336_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1336_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1336_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1336_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1336_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1336.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1336.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1336.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1336.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1336.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1336.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1336_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1336_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1336_latest.md?ref=main

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
- open: 13.2
- high: 13.35
- low: 13.15
- close: 13.25
- volume: 13000
- ma5: 13.14
- ema23_primary: 13.43
- distance_to_ema23_pct: -1.38
- ma20: 13.42
- ma60: 14.02
- ma120: 15.02
- return_5d: 1.15
- return_20d: -4.68
- volume_ratio: 0.17
- distance_to_ma20_pct_auxiliary: -1.25
- distance_to_high_60_pct: -13.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,14,14,13.7,13.7,52000,14.09,-2.76,13.99,14.82,0.51
20260505,13.75,14,13.7,13.95,78000,14.08,-0.9,13.99,14.78,0.76
20260506,14,14,13.7,13.75,106000,14.05,-2.13,13.98,14.72,1.05
20260507,13.8,13.8,13.7,13.75,66000,14.02,-1.96,13.97,14.68,0.67
20260508,13.75,13.95,13.75,13.85,81000,14.01,-1.14,13.97,14.63,0.81
20260511,13.85,13.95,13.8,13.8,71000,13.99,-1.38,13.96,14.59,0.7
20260512,13.8,14.3,13.8,13.8,163000,13.98,-1.26,13.96,14.56,1.52
20260513,13.8,13.8,13.65,13.65,68000,13.95,-2.15,13.93,14.52,0.65
20260514,13.7,13.7,13.65,13.65,83000,13.92,-1.97,13.9,14.48,0.8
20260515,13.65,13.7,13.45,13.45,98000,13.88,-3.13,13.87,14.45,0.95
20260518,13.45,13.45,13.25,13.25,95000,13.83,-4.21,13.82,14.41,0.91
20260519,13.25,13.5,12.8,12.95,220000,13.76,-5.88,13.76,14.36,1.96
20260520,13.2,13.2,12.9,12.95,174000,13.69,-5.41,13.7,14.32,1.54
20260521,13.2,13.2,13.05,13.05,59000,13.64,-4.31,13.64,14.28,0.55
20260522,13.05,13.15,13.05,13.1,13000,13.59,-3.63,13.6,14.23,0.13
20260525,13.15,13.2,13.05,13.15,13000,13.56,-2.99,13.56,14.19,0.14
20260526,13.25,13.25,13.05,13.05,13000,13.51,-3.43,13.52,14.14,0.15
20260527,13.1,13.25,13.05,13.15,13000,13.48,-2.47,13.49,14.09,0.16
20260528,13.3,13.3,13.1,13.1,13000,13.45,-2.61,13.45,14.05,0.17
20260529,13.2,13.35,13.15,13.25,13000,13.43,-1.38,13.42,14.02,0.17
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.97
- over_600_ratio: 44.11
- over_800_ratio: 41.58
- over_1000_ratio: 38.24
- over_400_change_1w: 0.08
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.82,,41.57,,38.23,,0,False,False
20260508,50.5,0.68,41.57,0,38.23,0,1,False,False
20260515,49.89,-0.61,41.57,0,38.23,0,0,False,False
20260522,49.97,0.08,41.58,0.01,38.24,0.01,1,True,True
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
