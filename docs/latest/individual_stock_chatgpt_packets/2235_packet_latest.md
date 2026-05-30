# INDIVIDUAL STOCK CHATGPT PACKET - 2235 謚源

## Metadata
- generated_at: 2026-05-30 23:41:17 Asia/Taipei
- stock_id: 2235
- stock_name: 謚源
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 232
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2235_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2235_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2235_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2235_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2235_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2235_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2235_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2235_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2235_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2235_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2235_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2235_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2235_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2235.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2235.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2235.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2235.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2235.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2235.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2235_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2235_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2235_latest.md?ref=main

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
- open: 32
- high: 32.6
- low: 31.8
- close: 32.3
- volume: 32000
- ma5: 30.99
- ema23_primary: 31.12
- distance_to_ema23_pct: 3.78
- ma20: 30.77
- ma60: 32.92
- ma120: 33.13
- return_5d: 7.31
- return_20d: -3.15
- volume_ratio: 2.08
- distance_to_ma20_pct_auxiliary: 4.98
- distance_to_high_60_pct: -14.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,32.15,32.4,32.15,32.3,7000,33.07,-2.34,33.02,34.02,0.71
20260430,32.35,33.3,32.3,32.5,13000,33.03,-1.59,32.9,34.01,1.28
20260504,32.2,32.3,32,32,17000,32.94,-2.86,32.81,33.97,1.55
20260505,32.3,32.7,32,32,23000,32.86,-2.62,32.77,33.93,1.94
20260506,32.6,32.6,31.15,31.2,15000,32.72,-4.66,32.68,33.9,1.23
20260507,31.05,31.05,30.25,30.5,13000,32.54,-6.26,32.52,33.85,1.07
20260508,30.5,30.85,29.9,29.9,11000,32.32,-7.48,32.3,33.77,0.89
20260511,30.6,30.7,30.3,30.3,6000,32.15,-5.76,32.12,33.72,0.47
20260512,30.5,30.5,30.05,30.05,5000,31.98,-6.02,31.96,33.66,0.41
20260513,30.4,30.4,30.4,30.4,1000,31.84,-4.53,31.84,33.61,0.08
20260514,30.4,30.4,30,30,6000,31.69,-5.33,31.68,33.55,0.51
20260515,30.05,30.4,30.05,30.4,4000,31.58,-3.75,31.57,33.51,0.36
20260518,30.05,30.15,29.35,29.35,11000,31.4,-6.52,31.41,33.42,0.94
20260519,29.35,29.85,29.35,29.4,14000,31.23,-5.86,31.27,33.33,1.37
20260521,30.1,30.15,30.1,30.1,9000,31.14,-3.33,31.15,33.25,0.86
20260522,31.45,31.45,30.1,30.1,30000,31.05,-3.06,31.04,33.17,2.9
20260525,30.1,30.1,30.1,30.1,30000,30.97,-2.81,30.94,33.09,2.61
20260527,29.25,30.5,29.25,30.5,30000,30.93,-1.39,30.86,33.02,2.36
20260528,30.5,31.95,30.5,31.95,31000,31.02,3.01,30.82,32.97,2.19
20260529,32,32.6,31.8,32.3,32000,31.12,3.78,30.77,32.92,2.08
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 83.55
- over_600_ratio: 80.77
- over_800_ratio: 80.77
- over_1000_ratio: 75.95
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.49,,80.74,,75.95,,0,False,False
20260508,83.49,0,80.74,0,75.95,0,0,False,False
20260515,83.51,0.02,80.76,0.02,75.95,0,1,False,True
20260522,83.54,0.03,80.77,0.01,75.95,0,2,False,True
20260529,83.55,0.01,80.77,0,75.95,0,3,False,False
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
