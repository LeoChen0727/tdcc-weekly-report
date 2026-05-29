# INDIVIDUAL STOCK CHATGPT PACKET - 8067 志旭

## Metadata
- generated_at: 2026-05-29 19:33:54 Asia/Taipei
- stock_id: 8067
- stock_name: 志旭
- packet_status: standard_rawdata_packet
- latest_price_date: 20260529
- price_rows: 118
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8067_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8067_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8067_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8067_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8067_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8067_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8067_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8067_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8067_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8067_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8067_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8067_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8067_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8067.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8067.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8067.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8067.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8067.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8067.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8067_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8067_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8067_latest.md?ref=main

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
- open: 13.55
- high: 13.55
- low: 12.6
- close: 13.5
- volume: 13000
- ma5: 13.56
- ema23_primary: 13.42
- distance_to_ema23_pct: 0.6
- ma20: 13.2
- ma60: 13.98
- ma120: 14.35
- return_5d: -1.1
- return_20d: 1.5
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: 2.29
- distance_to_high_60_pct: -15.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.6,12.65,12.6,12.65,5000,13.66,-7.42,13.7,14.41,0.72
20260429,12.65,13.05,12.65,13.05,2000,13.61,-4.13,13.62,14.36,0.35
20260430,12.9,12.9,12.9,12.9,1000,13.55,-4.82,13.55,14.32,0.18
20260504,13.35,13.35,13.35,13.35,1000,13.54,-1.37,13.5,14.29,0.19
20260505,12.5,13.05,12.5,12.9,5000,13.48,-4.32,13.39,14.25,0.89
20260506,13.4,13.4,12.75,13.15,3000,13.46,-2.27,13.37,14.22,0.57
20260511,12.55,12.7,12.45,12.45,6000,13.37,-6.89,13.3,14.18,1.15
20260512,12.25,12.6,12.2,12.6,3000,13.31,-5.31,13.21,14.15,0.58
20260513,12.45,12.85,12.45,12.8,3000,13.26,-3.5,13.1,14.12,0.57
20260514,12.5,12.9,12.5,12.9,3000,13.23,-2.53,13.07,14.08,0.71
20260515,12.9,12.9,12.35,12.65,7000,13.19,-4.06,13.02,14.05,1.63
20260518,12.65,12.65,12.65,12.65,1000,13.14,-3.74,12.95,14.01,0.24
20260519,12.35,13.65,12.35,13.6,6000,13.18,3.19,12.95,14,1.67
20260521,13.75,14.95,13.7,14.85,82000,13.32,11.5,13.03,14.01,10.93
20260522,14.4,14.4,13.5,13.65,14000,13.35,2.28,13.06,14,1.75
20260525,13.8,13.8,13.6,13.6,14000,13.37,1.74,13.09,13.98,1.65
20260526,12.5,13.6,12.5,13.6,13000,13.39,1.59,13.1,13.98,1.44
20260527,14.6,14.6,13.1,13.55,14000,13.4,1.12,13.13,13.98,1.44
20260528,12.85,13.55,12.85,13.55,13000,13.41,1.02,13.19,13.98,1.3
20260529,13.55,13.55,12.6,13.5,13000,13.42,0.6,13.2,13.98,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.35
- over_600_ratio: 78.76
- over_800_ratio: 75.32
- over_1000_ratio: 56.73
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
20260430,81.35,,75.32,,56.73,,0,False,False
20260508,81.35,0,75.32,0,56.73,0,0,False,False
20260515,81.35,0,75.32,0,56.73,0,0,False,False
20260522,81.35,0,75.32,0,56.73,0,0,False,False
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
