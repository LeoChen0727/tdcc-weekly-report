# INDIVIDUAL STOCK CHATGPT PACKET - 6021 美好證

## Metadata
- generated_at: 2026-05-29 19:33:13 Asia/Taipei
- stock_id: 6021
- stock_name: 美好證
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6021_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6021_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6021_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6021_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6021_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6021_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6021_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6021_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6021_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6021_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6021_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6021_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6021_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6021.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6021.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6021.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6021.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6021.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6021.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6021_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6021_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6021_latest.md?ref=main

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
- open: 35.8
- high: 37.15
- low: 35.55
- close: 36.9
- volume: 36000
- ma5: 34.32
- ema23_primary: 32.97
- distance_to_ema23_pct: 11.9
- ma20: 33.33
- ma60: 31.69
- ma120: 29.89
- return_5d: 14.42
- return_20d: 11.65
- volume_ratio: 0.14
- distance_to_ma20_pct_auxiliary: 10.73
- distance_to_high_60_pct: -0.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.05,34.2,33.05,34,389000,31.18,9.06,30.61,31.26,1.29
20260505,34.1,34.6,33.75,33.8,212000,31.39,7.66,30.82,31.3,0.69
20260506,34.3,34.3,33.7,34.05,305000,31.62,7.7,31.04,31.35,0.97
20260507,34.65,35.55,34.5,34.9,569000,31.89,9.44,31.27,31.41,1.69
20260508,35,35.2,34.3,34.95,384000,32.14,8.73,31.52,31.46,1.1
20260511,35.3,36.5,35.25,35.4,1055000,32.42,9.21,31.79,31.52,2.72
20260512,36.15,36.35,34.05,34.4,619000,32.58,5.58,32.02,31.58,1.51
20260513,34.05,34.05,32.15,32.4,403000,32.57,-0.51,32.12,31.6,0.97
20260514,32.4,32.9,31.7,32.05,351000,32.52,-1.45,32.17,31.61,0.87
20260515,32.45,32.65,31.5,31.55,203000,32.44,-2.75,32.31,31.61,0.51
20260518,30.95,31.25,30.75,31.15,136000,32.33,-3.66,32.42,31.62,0.34
20260519,31.05,31.35,30.8,30.9,106000,32.21,-4.08,32.52,31.62,0.27
20260520,30.8,31.2,30.8,31.1,71000,32.12,-3.18,32.61,31.62,0.18
20260521,31.7,32,31.5,32,112000,32.11,-0.35,32.74,31.64,0.29
20260522,31.85,32.25,31.65,32.25,32000,32.12,0.39,32.88,31.65,0.09
20260525,32.5,32.9,32.05,32.2,32000,32.13,0.22,32.94,31.65,0.1
20260526,32.45,32.5,31.8,32.25,32000,32.14,0.34,32.92,31.63,0.1
20260527,32.6,34.95,32.4,34.9,34000,32.37,7.82,33.02,31.62,0.12
20260528,35.4,35.85,34.25,35.35,35000,32.62,8.38,33.13,31.64,0.13
20260529,35.8,37.15,35.55,36.9,36000,32.97,11.9,33.33,31.69,0.14
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 90.12
- over_600_ratio: 88.24
- over_800_ratio: 87.07
- over_1000_ratio: 86.52
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
20260430,90.2,,87.11,,86.56,,0,False,False
20260508,90.17,-0.03,87.09,-0.02,86.54,-0.02,1,False,False
20260515,90.13,-0.04,87.08,-0.01,86.53,-0.01,0,False,False
20260522,90.12,-0.01,87.07,-0.01,86.52,-0.01,0,False,False
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
