# INDIVIDUAL STOCK CHATGPT PACKET - 7770 君曜

## Metadata
- generated_at: 2026-05-26 23:55:02 Asia/Taipei
- stock_id: 7770
- stock_name: 君曜
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 106
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7770_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7770_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7770_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7770_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7770_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7770_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7770_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7770_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7770_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7770_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7770_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7770_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7770_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7770.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7770.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7770.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7770.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7770.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7770.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7770_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7770_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7770_latest.md?ref=main

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
- open: 42.65
- high: 42.65
- low: 41.3
- close: 41.8
- volume: 42000
- ma5: 41.79
- ema23_primary: 45.29
- distance_to_ema23_pct: -7.7
- ma20: 45.59
- ma60: 47.91
- ma120: 51.98
- return_5d: -2.79
- return_20d: -16.4
- volume_ratio: 2.27
- distance_to_ma20_pct_auxiliary: -8.32
- distance_to_high_60_pct: -22.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,49.15,49.3,48.1,48.3,13000,49.36,-2.15,49.33,50.82,0.32
20260428,48.1,48.1,47.6,47.6,21000,49.21,-3.28,49.26,50.66,0.52
20260429,47.6,48,47.6,47.6,6000,49.08,-3.01,48.95,50.49,0.18
20260430,47.8,48,47.8,47.8,8000,48.97,-2.39,48.84,50.34,0.27
20260504,47.8,48,47.1,48,6000,48.89,-1.82,48.71,50.18,0.22
20260505,48,48.8,47.5,48.8,10000,48.88,-0.17,48.6,50.04,0.38
20260506,49.1,49.1,47.5,48.05,14000,48.81,-1.57,48.53,49.88,0.53
20260507,48.05,48.05,47.5,47.7,23000,48.72,-2.1,48.42,49.73,0.87
20260508,48,48,47,47.15,13000,48.59,-2.96,48.48,49.58,0.58
20260511,47.2,47.5,43.85,47.5,27000,48.5,-2.06,48.52,49.44,1.24
20260512,47.5,47.5,47.5,47.5,6000,48.42,-1.89,48.52,49.32,0.28
20260514,45.7,46,45.1,45.4,21000,48.16,-5.74,48.42,49.16,0.96
20260515,45.4,45.4,44.1,45.4,12000,47.93,-5.29,48.35,49.02,0.55
20260518,45.9,45.9,43.05,43.15,11000,47.54,-9.23,48.1,48.84,0.5
20260519,42.2,43,42.2,43,20000,47.16,-8.82,47.74,48.69,1
20260520,39.3,42.55,39.3,40.2,14000,46.58,-13.69,47.2,48.47,0.77
20260521,40.25,43,40.25,42,18000,46.2,-9.08,46.8,48.32,1
20260522,42.4,43,42,42.4,42000,45.88,-7.59,46.32,48.18,2.25
20260525,42.95,43,42.05,42.55,43000,45.6,-6.69,46.01,48.05,2.25
20260526,42.65,42.65,41.3,41.8,42000,45.29,-7.7,45.59,47.91,2.27
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.23
- over_600_ratio: 67.76
- over_800_ratio: 65.14
- over_1000_ratio: 65.14
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
20260430,72.23,,65.14,,65.14,,0,False,False
20260508,72.23,0,65.14,0,65.14,0,0,False,False
20260515,72.23,0,65.14,0,65.14,0,0,False,False
20260522,72.23,0,65.14,0,65.14,0,0,False,False
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
