# INDIVIDUAL STOCK CHATGPT PACKET - 4426 利勤

## Metadata
- generated_at: 2026-05-26 23:54:03 Asia/Taipei
- stock_id: 4426
- stock_name: 利勤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4426_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4426_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4426_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4426_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4426_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4426_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4426_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4426_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4426_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4426_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4426_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4426_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4426_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4426.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4426.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4426.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4426.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4426.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4426.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4426_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4426_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4426_latest.md?ref=main

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
- open: 7.63
- high: 7.63
- low: 7.48
- close: 7.54
- volume: 138727
- ma5: 7.65
- ema23_primary: 8.02
- distance_to_ema23_pct: -5.97
- ma20: 7.97
- ma60: 8.62
- ma120: 9.11
- return_5d: -3.46
- return_20d: -10.66
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: -5.44
- distance_to_high_60_pct: -20.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,8.44,8.44,8.41,8.41,55683,8.75,-3.83,8.71,9.12,0.33
20260429,8.62,8.62,8.38,8.43,67706,8.72,-3.31,8.68,9.09,0.4
20260430,8.43,8.43,8.33,8.34,102284,8.69,-4,8.64,9.07,0.61
20260504,8.36,8.36,8.16,8.2,152511,8.65,-5.17,8.6,9.05,0.89
20260505,8.2,8.2,8.1,8.15,88678,8.61,-5.29,8.57,9.02,0.55
20260506,8.33,8.33,8.11,8.12,185588,8.56,-5.19,8.53,8.99,1.13
20260507,8.12,8.13,7.88,8,414140,8.52,-6.08,8.5,8.96,2.42
20260508,8.03,8.13,7.87,8.04,350251,8.48,-5.17,8.48,8.94,2.13
20260511,8.04,8.14,7.91,8,186675,8.44,-5.19,8.45,8.91,1.11
20260512,8,8,7.95,8,138018,8.4,-4.78,8.43,8.89,0.82
20260513,8.05,8.05,7.94,7.98,123669,8.37,-4.62,8.4,8.86,0.75
20260514,7.98,8.05,7.93,7.98,217132,8.33,-4.25,8.37,8.84,1.29
20260515,7.91,8.05,7.91,7.91,47419,8.3,-4.69,8.34,8.81,0.3
20260518,7.85,8.03,7.81,7.85,114994,8.26,-4.98,8.28,8.78,0.75
20260519,7.82,7.89,7.8,7.81,95770,8.22,-5.03,8.23,8.76,0.63
20260520,7.82,7.82,7.78,7.8,60391,8.19,-4.75,8.17,8.74,0.4
20260521,7.99,7.99,7.65,7.71,330588,8.15,-5.38,8.12,8.71,2.05
20260522,7.72,7.72,7.46,7.61,260396,8.1,-6.09,8.07,8.68,1.59
20260525,7.64,7.65,7.49,7.6,264998,8.06,-5.73,8.02,8.65,1.56
20260526,7.63,7.63,7.48,7.54,138727,8.02,-5.97,7.97,8.62,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.92
- over_600_ratio: 58.45
- over_800_ratio: 56.94
- over_1000_ratio: 53.78
- over_400_change_1w: 0.36
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.36,,56.7,,53.55,,0,False,False
20260508,61.55,0.19,56.88,0.18,53.72,0.17,1,True,True
20260515,61.56,0.01,56.9,0.02,53.74,0.02,2,True,True
20260522,61.92,0.36,56.94,0.04,53.78,0.04,3,True,True
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
