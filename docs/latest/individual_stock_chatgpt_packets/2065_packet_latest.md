# INDIVIDUAL STOCK CHATGPT PACKET - 2065 世豐

## Metadata
- generated_at: 2026-05-28 20:18:31 Asia/Taipei
- stock_id: 2065
- stock_name: 世豐
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2065_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2065_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2065_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2065_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2065_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2065_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2065_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2065_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2065_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2065_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2065_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2065_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2065_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2065.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2065.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2065.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2065.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2065.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2065.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2065_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2065_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2065_latest.md?ref=main

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
- open: 35.55
- high: 35.6
- low: 35.5
- close: 35.5
- volume: 36000
- ma5: 35.44
- ema23_primary: 33.01
- distance_to_ema23_pct: 7.54
- ma20: 32.45
- ma60: 31.26
- ma120: 30.95
- return_5d: 2.9
- return_20d: 21.16
- volume_ratio: 0.25
- distance_to_ma20_pct_auxiliary: 9.41
- distance_to_high_60_pct: -0.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,29.3,29.3,29,29.05,18000,30.19,-3.78,30.14,31.18,0.23
20260504,29.15,29.15,28,28.55,230000,30.06,-5.01,30.07,31.09,2.7
20260505,28.55,28.9,28.3,28.6,109000,29.93,-4.46,30,31,1.23
20260506,28.5,29,28.1,28.55,66000,29.82,-4.26,29.86,30.9,0.77
20260507,28.55,28.9,28.5,28.9,89000,29.74,-2.83,29.77,30.82,1.01
20260508,28.6,30.45,28.6,30.1,158000,29.77,1.1,29.76,30.77,1.7
20260511,31,33.1,30.7,32.35,800000,29.99,7.88,29.85,30.77,6.11
20260512,32.3,32.3,31.5,31.7,91000,30.13,5.21,29.92,30.77,0.69
20260513,31.65,31.8,31.15,31.7,93000,30.26,4.76,29.96,30.76,0.7
20260514,32,34.4,31.7,33.5,534000,30.53,9.73,30.11,30.77,3.43
20260515,33.25,33.7,33,33.5,198000,30.78,8.84,30.23,30.79,1.25
20260518,33.35,33.6,33.05,33.5,51000,31,8.05,30.36,30.81,0.32
20260519,33.55,33.95,33.5,33.5,68000,31.21,7.33,30.51,30.83,0.43
20260520,33.55,33.85,32.95,33.75,96000,31.42,7.4,30.69,30.86,0.62
20260521,33.75,34.65,33.55,34.5,126000,31.68,8.9,30.91,30.91,0.79
20260522,34.5,35.2,34.5,35.15,35000,31.97,9.95,31.18,30.97,0.22
20260525,34.65,35.55,34.55,35.5,35000,32.26,10.03,31.5,31.03,0.24
20260526,35.5,35.7,33.95,35.5,35000,32.53,9.12,31.82,31.11,0.24
20260527,35.5,35.6,35.45,35.55,36000,32.78,8.43,32.14,31.18,0.25
20260528,35.55,35.6,35.5,35.5,36000,33.01,7.54,32.45,31.26,0.25
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.83
- over_600_ratio: 47.47
- over_800_ratio: 44.26
- over_1000_ratio: 39.59
- over_400_change_1w: 0.19
- over_800_change_1w: -0.86
- over_1000_change_1w: -1.13
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.29,,43.79,,40.69,,0,False,False
20260508,48.56,-0.73,43.05,-0.74,39.95,-0.74,0,False,False
20260515,50.64,2.08,45.12,2.07,40.72,0.77,1,True,True
20260522,50.83,0.19,44.26,-0.86,39.59,-1.13,2,False,False
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
