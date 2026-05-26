# INDIVIDUAL STOCK CHATGPT PACKET - 1314 中石化

## Metadata
- generated_at: 2026-05-26 22:18:01 Asia/Taipei
- stock_id: 1314
- stock_name: 中石化
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1314_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1314_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1314_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1314_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1314_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1314_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1314_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1314_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1314_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1314_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1314_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1314_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1314_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1314.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1314.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1314.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1314.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1314.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1314.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1314_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1314_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1314_latest.md?ref=main

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
- open: 7.07
- high: 7.13
- low: 6.96
- close: 6.97
- volume: 13300441
- ma5: 7.07
- ema23_primary: 7.21
- distance_to_ema23_pct: -3.34
- ma20: 7.13
- ma60: 7.86
- ma120: 7.94
- return_5d: 0.43
- return_20d: -5.56
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: -2.19
- distance_to_high_60_pct: -28.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,7.39,7.58,7.39,7.51,11719864,7.85,-4.38,7.85,8.16,0.37
20260429,7.57,7.61,7.43,7.43,9812623,7.82,-4.97,7.81,8.15,0.34
20260430,7.48,7.51,7.36,7.42,10905423,7.79,-4.69,7.77,8.14,0.43
20260504,7.42,7.42,7.23,7.23,22499242,7.74,-6.58,7.73,8.13,0.92
20260505,7.25,7.37,7.25,7.34,11584671,7.71,-4.75,7.68,8.11,0.49
20260506,7.4,7.4,7.22,7.23,15355551,7.67,-5.69,7.64,8.09,0.65
20260507,7.23,7.29,7.17,7.25,15765137,7.63,-5,7.59,8.08,0.69
20260508,7.25,7.33,7.13,7.14,21973327,7.59,-5.93,7.54,8.06,1.02
20260511,7.14,7.19,7.07,7.09,20804080,7.55,-6.08,7.51,8.04,1.13
20260512,7.09,7.13,7.01,7.08,16856899,7.51,-5.72,7.47,8.03,0.96
20260513,7.08,7.08,6.98,7.02,20976716,7.47,-6.01,7.43,8.01,1.18
20260514,7.02,7.03,6.87,6.91,27451039,7.42,-6.9,7.39,8,1.55
20260515,6.91,6.93,6.71,6.72,25849958,7.36,-8.74,7.33,7.97,1.42
20260518,6.73,6.93,6.69,6.87,18404819,7.32,-6.18,7.29,7.96,1.03
20260519,7.03,7.15,6.93,6.94,20071715,7.29,-4.81,7.25,7.94,1.13
20260520,6.96,7.03,6.94,7.02,10255639,7.27,-3.41,7.21,7.92,0.58
20260521,7.02,7.2,6.98,7.2,16645602,7.26,-0.86,7.19,7.91,0.94
20260522,7.21,7.24,7.06,7.08,19582127,7.25,-2.31,7.16,7.9,1.13
20260525,7.11,7.11,6.92,7.07,18807365,7.23,-2.25,7.15,7.88,1.08
20260526,7.07,7.13,6.96,6.97,13300441,7.21,-3.34,7.13,7.86,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 38.79
- over_600_ratio: 34.87
- over_800_ratio: 32.32
- over_1000_ratio: 30.57
- over_400_change_1w: 0.05
- over_800_change_1w: 0.1
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.71,,32.28,,30.57,,0,False,False
20260508,38.81,0.1,32.35,0.07,30.6,0.03,1,True,True
20260515,38.74,-0.07,32.22,-0.13,30.46,-0.14,0,False,False
20260522,38.79,0.05,32.32,0.1,30.57,0.11,1,True,True
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
