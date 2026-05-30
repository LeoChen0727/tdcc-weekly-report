# INDIVIDUAL STOCK CHATGPT PACKET - 5438 東友

## Metadata
- generated_at: 2026-05-30 23:42:41 Asia/Taipei
- stock_id: 5438
- stock_name: 東友
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5438_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5438_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5438_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5438_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5438_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5438_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5438_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5438_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5438_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5438_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5438_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5438_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5438_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5438.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5438.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5438.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5438.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5438.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5438.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5438_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5438_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5438_latest.md?ref=main

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
- high: 19.5
- low: 18.95
- close: 19.1
- volume: 19000
- ma5: 19.18
- ema23_primary: 19.08
- distance_to_ema23_pct: 0.1
- ma20: 19.07
- ma60: 19.5
- ma120: 20.83
- return_5d: 0.79
- return_20d: 0.53
- volume_ratio: 0.24
- distance_to_ma20_pct_auxiliary: 0.13
- distance_to_high_60_pct: -13.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,19,19.9,19,19.2,173000,19.32,-0.62,19.1,20.4,1.71
20260505,19.35,19.65,19.2,19.55,119000,19.34,1.09,19.12,20.34,1.17
20260506,19.6,19.65,19.25,19.65,100000,19.37,1.47,19.17,20.28,1
20260507,19.45,20.25,19.45,20.05,222000,19.42,3.23,19.2,20.24,2.09
20260508,20.3,20.3,19.3,19.5,131000,19.43,0.37,19.21,20.19,1.19
20260511,19.75,19.75,19.35,19.4,59000,19.43,-0.14,19.23,20.16,0.54
20260512,19.55,19.55,18.9,18.9,98000,19.38,-2.49,19.23,20.13,0.89
20260513,18.75,19.2,18.75,18.9,79000,19.34,-2.29,19.23,20.09,0.75
20260514,18.95,19,18.65,18.65,122000,19.28,-3.29,19.23,20.03,1.14
20260515,18.65,18.8,18.55,18.55,85000,19.22,-3.5,19.19,19.97,0.8
20260518,18.55,18.85,18.5,18.6,63000,19.17,-2.98,19.16,19.92,0.61
20260519,18.8,18.9,18.5,18.5,59000,19.12,-3.22,19.11,19.87,0.58
20260520,18.5,18.55,18.2,18.5,72000,19.06,-2.96,19.07,19.81,0.72
20260521,18.7,18.95,18.6,18.7,55000,19.03,-1.75,19.03,19.77,0.56
20260522,18.55,19,18.55,18.95,19000,19.03,-0.4,19.02,19.73,0.21
20260525,18.8,19.05,18.7,18.75,19000,19,-1.34,19.02,19.67,0.21
20260526,18.9,19.95,18.55,19.7,19000,19.06,3.35,19.07,19.64,0.22
20260527,19.7,21,19.3,19.3,20000,19.08,1.14,19.08,19.59,0.24
20260528,19.35,19.65,19.05,19.05,19000,19.08,-0.15,19.07,19.54,0.23
20260529,19.5,19.5,18.95,19.1,19000,19.08,0.1,19.07,19.5,0.24
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 75.34
- over_600_ratio: 74.14
- over_800_ratio: 74.14
- over_1000_ratio: 74.14
- over_400_change_1w: -0.39
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.7,,74.08,,74.08,,0,False,False
20260508,75.72,0.02,74.11,0.03,74.11,0.03,1,True,True
20260515,75.71,-0.01,74.11,0,74.11,0,0,False,False
20260522,75.73,0.02,74.11,0,74.11,0,1,False,False
20260529,75.34,-0.39,74.14,0.03,74.14,0.03,2,False,True
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
