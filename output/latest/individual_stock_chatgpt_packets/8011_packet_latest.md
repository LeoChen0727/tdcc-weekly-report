# INDIVIDUAL STOCK CHATGPT PACKET - 8011 台通

## Metadata
- generated_at: 2026-05-28 20:20:29 Asia/Taipei
- stock_id: 8011
- stock_name: 台通
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8011_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8011_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8011_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8011_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8011_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8011_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8011_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8011_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8011_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8011_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8011_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8011_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8011_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8011.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8011.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8011.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8011.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8011.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8011.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8011_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8011_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8011_latest.md?ref=main

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
- open: 17.5
- high: 18.4
- low: 17.5
- close: 17.75
- volume: 1670998
- ma5: 17.97
- ema23_primary: 18.65
- distance_to_ema23_pct: -4.81
- ma20: 18.57
- ma60: 19.82
- ma120: 20.84
- return_5d: -1.66
- return_20d: -8.97
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -4.44
- distance_to_high_60_pct: -19.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,20,20,19.35,19.35,2157377,20.32,-4.75,20.43,20.6,1.03
20260504,19.6,19.6,19.25,19.25,861637,20.23,-4.83,20.37,20.55,0.41
20260505,19.3,20.25,19.2,20.15,2402977,20.22,-0.35,20.37,20.51,1.1
20260506,20.5,20.5,19.6,19.8,1757135,20.19,-1.91,20.36,20.48,0.79
20260507,19.85,19.9,19.6,19.65,1548872,20.14,-2.44,20.29,20.45,0.75
20260508,19.85,20.2,19.2,19.3,2091105,20.07,-3.84,20.19,20.42,1.02
20260511,19.3,19.5,19.2,19.3,1060395,20.01,-3.53,20.13,20.4,0.53
20260512,19.3,19.4,18.8,18.8,1915971,19.91,-5.56,20.04,20.37,0.93
20260513,18.7,18.75,18.1,18.2,1542471,19.76,-7.91,19.92,20.33,0.74
20260514,18.45,18.8,17.95,18.1,2477220,19.63,-7.77,19.8,20.28,1.14
20260515,18.5,18.75,17.65,17.85,1880234,19.48,-8.36,19.68,20.24,0.85
20260518,17.6,18.45,17.4,18.2,2376497,19.37,-6.04,19.57,20.21,1.04
20260519,18.2,18.6,17.8,17.85,1303454,19.24,-7.24,19.39,20.17,0.66
20260520,17.9,18.25,17.55,17.8,2507815,19.12,-6.92,19.2,20.13,1.32
20260521,18,18.4,18,18.05,2477325,19.03,-5.17,19.05,20.09,1.31
20260522,18.1,18.4,17.85,18.4,1701485,18.98,-3.06,18.95,20.04,0.93
20260525,18.6,18.65,18.2,18.25,1092197,18.92,-3.54,18.86,19.99,0.61
20260526,18.3,18.4,17.85,17.9,1380912,18.84,-4.97,18.77,19.94,0.79
20260527,17.9,17.9,17.55,17.55,1011103,18.73,-6.29,18.66,19.88,0.58
20260528,17.5,18.4,17.5,17.75,1670998,18.65,-4.81,18.57,19.82,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 30.29
- over_600_ratio: 28.57
- over_800_ratio: 27.32
- over_1000_ratio: 24.64
- over_400_change_1w: -0.21
- over_800_change_1w: 0.37
- over_1000_change_1w: -0.71
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.72,,27.57,,25.39,,0,False,False
20260508,30.74,0.02,28.03,0.46,25.33,-0.06,1,False,True
20260515,30.5,-0.24,26.95,-1.08,25.35,0.02,2,False,True
20260522,30.29,-0.21,27.32,0.37,24.64,-0.71,3,False,True
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
