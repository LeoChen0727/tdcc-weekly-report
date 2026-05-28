# INDIVIDUAL STOCK CHATGPT PACKET - 3508 位速

## Metadata
- generated_at: 2026-05-28 20:19:14 Asia/Taipei
- stock_id: 3508
- stock_name: 位速
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3508_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3508_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3508_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3508_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3508_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3508_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3508_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3508_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3508_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3508_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3508_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3508_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3508_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3508.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3508.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3508.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3508.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3508.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3508.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3508_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3508_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3508_latest.md?ref=main

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
- open: 20.95
- high: 21.55
- low: 19.75
- close: 20.2
- volume: 21000
- ma5: 20.38
- ema23_primary: 22.03
- distance_to_ema23_pct: -8.29
- ma20: 20.86
- ma60: 29.98
- ma120: 27.74
- return_5d: 2.28
- return_20d: -17.21
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -3.15
- distance_to_high_60_pct: -63.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,24.8,24.8,22.35,22.85,906000,28.35,-19.39,26.91,33.28,1.1
20260504,23.2,23.7,22.05,22.3,536000,27.84,-19.91,26.02,33.25,0.67
20260505,21.75,22.95,21.75,21.9,434000,27.35,-19.92,25.31,33.22,0.56
20260506,21,21.85,20.5,20.7,809000,26.79,-22.75,24.73,33.15,1.01
20260507,21.7,22.75,18.9,22.75,1066000,26.46,-14.01,24.4,33.13,1.26
20260508,22.3,24.5,22,22,763000,26.09,-15.66,24.18,33.11,0.87
20260511,22,22.1,20.75,21,533000,25.66,-18.17,24.05,33.05,0.6
20260512,20.85,21.5,20.1,21.1,379000,25.28,-16.54,23.8,32.96,0.57
20260513,20,21,20,20.3,273000,24.87,-18.37,23.64,32.81,0.48
20260514,20,20.55,19.5,19.8,577000,24.44,-19,23.41,32.61,1.06
20260515,20,20.15,19.35,19.55,390000,24.04,-18.67,23.06,32.35,0.75
20260518,19.1,21.5,19.05,21.25,323000,23.8,-10.73,22.86,32.12,0.64
20260519,21,21.05,20.1,20.1,214000,23.5,-14.45,22.67,31.91,0.44
20260520,20.1,20.5,19.5,19.9,127000,23.2,-14.21,22.45,31.69,0.27
20260521,19.55,19.95,19.5,19.75,235000,22.91,-13.79,22.1,31.43,0.51
20260522,19.75,20.35,19.6,20.1,20000,22.67,-11.36,21.77,31.16,0.05
20260525,19.7,20.1,19.15,19.45,20000,22.41,-13.19,21.46,30.84,0.05
20260526,19.95,21.35,19.95,21.35,21000,22.32,-4.34,21.29,30.59,0.05
20260527,21.6,22.2,20.55,20.8,21000,22.19,-6.27,21.07,30.32,0.05
20260528,20.95,21.55,19.75,20.2,21000,22.03,-8.29,20.86,29.98,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.54
- over_600_ratio: 38.98
- over_800_ratio: 35.69
- over_1000_ratio: 33.05
- over_400_change_1w: 0.92
- over_800_change_1w: 0.07
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.87,,35.53,,32.89,,0,False,False
20260508,41.95,1.08,35.57,0.04,32.93,0.04,1,True,True
20260515,41.62,-0.33,35.62,0.05,32.98,0.05,2,False,True
20260522,42.54,0.92,35.69,0.07,33.05,0.07,3,True,True
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
