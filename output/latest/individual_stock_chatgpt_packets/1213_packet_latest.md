# INDIVIDUAL STOCK CHATGPT PACKET - 1213 大飲

## Metadata
- generated_at: 2026-05-26 23:00:07 Asia/Taipei
- stock_id: 1213
- stock_name: 大飲
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 128
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1213_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1213_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1213_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1213_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1213_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1213_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1213_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1213_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1213_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1213_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1213_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1213_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1213_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1213.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1213.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1213.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1213.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1213.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1213.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1213_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1213_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1213_latest.md?ref=main

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
- open: 8.52
- high: 8.52
- low: 8
- close: 8.23
- volume: 39371
- ma5: 8.38
- ema23_primary: 8.73
- distance_to_ema23_pct: -5.68
- ma20: 8.69
- ma60: 9.3
- ma120: 9.77
- return_5d: 0.37
- return_20d: -8.04
- volume_ratio: 1.41
- distance_to_ma20_pct_auxiliary: -5.31
- distance_to_high_60_pct: -17.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,8.95,8.95,8.33,8.84,120670,9.34,-5.36,9.33,9.73,4.61
20260429,8.5,8.84,8.5,8.84,10100,9.3,-4.94,9.28,9.72,0.38
20260430,9.1,9.1,8.8,9.03,6005,9.28,-2.66,9.25,9.7,0.23
20260504,8.88,9,8.74,8.79,50119,9.24,-4.83,9.21,9.68,1.78
20260505,9.09,9.09,9,9,3003,9.22,-2.35,9.18,9.66,0.12
20260506,8.92,8.92,8.8,8.85,15100,9.19,-3.66,9.16,9.64,0.62
20260507,8.85,9.05,8.65,8.85,30133,9.16,-3.36,9.13,9.62,1.19
20260508,8.7,8.83,8.7,8.75,33156,9.12,-4.1,9.1,9.59,1.29
20260511,8.58,9,8.34,9,43201,9.11,-1.25,9.08,9.57,1.59
20260512,8.62,8.77,8.4,8.7,30120,9.08,-4.18,9.04,9.55,1.06
20260513,8.96,8.96,8.69,8.7,8114,9.05,-3.84,9,9.52,0.29
20260514,8.5,8.95,8.34,8.95,8658,9.04,-0.99,8.98,9.5,0.31
20260515,8.99,8.99,8.5,8.9,9151,9.03,-1.42,8.96,9.48,0.34
20260518,8.23,8.59,8.23,8.54,9102,8.99,-4.97,8.92,9.46,0.35
20260519,8.38,8.52,8,8.2,57179,8.92,-8.09,8.87,9.43,2.05
20260520,8.45,8.45,8.21,8.43,15303,8.88,-5.07,8.84,9.4,0.62
20260521,8.7,8.7,8.31,8.49,4002,8.85,-4.05,8.8,9.38,0.16
20260522,8.75,8.75,8.25,8.47,15002,8.82,-3.93,8.77,9.35,0.6
20260525,8.47,8.47,8.1,8.27,52193,8.77,-5.71,8.73,9.32,1.98
20260526,8.52,8.52,8,8.23,39371,8.73,-5.68,8.69,9.3,1.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.15
- over_600_ratio: 80.68
- over_800_ratio: 80.68
- over_1000_ratio: 77.46
- over_400_change_1w: 0.04
- over_800_change_1w: 0.04
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.03,,80.56,,77.46,,0,False,False
20260508,82.04,0.01,80.57,0.01,77.46,0,1,False,True
20260515,82.11,0.07,80.64,0.07,77.46,0,2,False,True
20260522,82.15,0.04,80.68,0.04,77.46,0,3,False,True
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
