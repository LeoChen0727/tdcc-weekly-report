# INDIVIDUAL STOCK CHATGPT PACKET - 2067 嘉鋼

## Metadata
- generated_at: 2026-05-30 23:41:15 Asia/Taipei
- stock_id: 2067
- stock_name: 嘉鋼
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2067_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2067_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2067_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2067_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2067_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2067_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2067_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2067_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2067_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2067_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2067_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2067_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2067_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2067.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2067.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2067.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2067.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2067.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2067.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2067_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2067_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2067_latest.md?ref=main

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
- open: 6.6
- high: 6.6
- low: 6.55
- close: 6.56
- volume: 7000
- ma5: 6.65
- ema23_primary: 6.94
- distance_to_ema23_pct: -5.48
- ma20: 6.91
- ma60: 7.51
- ma120: 8.87
- return_5d: -5.2
- return_20d: -9.27
- volume_ratio: 0.21
- distance_to_ma20_pct_auxiliary: -5.02
- distance_to_high_60_pct: -33.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,7.23,7.26,6.85,6.9,129000,7.42,-7.04,7.27,8.6,1.48
20260505,6.9,7.2,6.8,7.05,55000,7.39,-4.62,7.23,8.55,0.62
20260506,6.81,7,6.8,6.82,32000,7.34,-7.13,7.19,8.48,0.38
20260507,6.83,7.04,6.82,7.04,45000,7.32,-3.81,7.16,8.43,0.53
20260508,6.79,7.51,6.68,7.51,95000,7.33,2.39,7.15,8.38,1.06
20260511,7.51,7.51,6.85,7.24,96000,7.33,-1.18,7.15,8.33,1.05
20260512,6.91,7.23,6.91,7.04,23000,7.3,-3.6,7.13,8.28,0.27
20260513,6.92,7.13,6.92,7.12,33000,7.29,-2.3,7.12,8.24,0.38
20260514,6.88,7.06,6.88,6.92,29000,7.26,-4.64,7.11,8.17,0.34
20260515,6.92,6.92,6.77,6.87,35000,7.22,-4.91,7.09,8.11,0.41
20260518,6.87,6.87,6.87,6.87,3000,7.2,-4.52,7.07,8.05,0.04
20260519,6.87,6.87,6.67,6.85,33000,7.17,-4.41,7.05,7.99,0.39
20260520,6.85,6.85,6.85,6.85,2000,7.14,-4.06,7.04,7.93,0.03
20260521,6.88,6.88,6.8,6.87,10000,7.12,-3.48,7.04,7.87,0.13
20260522,6.87,7.09,6.71,6.92,7000,7.1,-2.55,7.04,7.81,0.1
20260525,6.75,6.9,6.53,6.73,7000,7.07,-4.81,7.04,7.75,0.1
20260526,6.73,6.78,6.55,6.7,7000,7.04,-4.82,7.04,7.69,0.1
20260527,6.7,6.7,6.5,6.68,7000,7.01,-4.7,7.01,7.63,0.11
20260528,6.84,6.84,6.52,6.6,7000,6.98,-5.38,6.94,7.57,0.15
20260529,6.6,6.6,6.55,6.56,7000,6.94,-5.48,6.91,7.51,0.21
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 56.5
- over_600_ratio: 52.25
- over_800_ratio: 49.07
- over_1000_ratio: 49.07
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
20260430,56.5,,49.07,,49.07,,0,False,False
20260508,56.5,0,49.07,0,49.07,0,0,False,False
20260515,56.5,0,49.07,0,49.07,0,0,False,False
20260522,56.5,0,49.07,0,49.07,0,0,False,False
20260529,56.5,0,49.07,0,49.07,0,0,False,False
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
