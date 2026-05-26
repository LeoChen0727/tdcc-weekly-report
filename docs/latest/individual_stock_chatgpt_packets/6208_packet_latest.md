# INDIVIDUAL STOCK CHATGPT PACKET - 6208 日揚

## Metadata
- generated_at: 2026-05-26 23:54:33 Asia/Taipei
- stock_id: 6208
- stock_name: 日揚
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6208_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6208_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6208_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6208_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6208_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6208_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6208_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6208_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6208_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6208_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6208_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6208_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6208_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6208.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6208.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6208.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6208.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6208.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6208.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6208_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6208_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6208_latest.md?ref=main

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
- open: 103
- high: 103
- low: 96.6
- close: 97.8
- volume: 98000
- ma5: 98.52
- ema23_primary: 88.59
- distance_to_ema23_pct: 10.39
- ma20: 89.27
- ma60: 66.89
- ma120: 55.66
- return_5d: -5.51
- return_20d: 17.13
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 9.56
- distance_to_high_60_pct: -9.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,83.5,84.5,81.5,81.9,563000,68.01,20.42,66.31,52.59,0.43
20260429,82.3,82.8,78,78.4,655000,68.88,13.82,67.86,53.18,0.49
20260430,81,83,78,80,506000,69.81,14.6,69.49,53.78,0.37
20260504,81.6,83.9,81.3,82.3,604000,70.85,16.17,71.22,54.43,0.44
20260505,83,83.6,80.8,83.3,543000,71.88,15.88,72.77,55.09,0.4
20260506,83.3,84.6,75,75.2,1990000,72.16,4.21,73.64,55.62,1.49
20260507,77.3,77.5,75,76.5,812000,72.52,5.49,74.64,56.16,0.64
20260508,75.4,76,72.2,72.4,832000,72.51,-0.15,75.52,56.63,0.65
20260511,74.1,79.4,74.1,78.7,1055000,73.03,7.77,76.7,57.2,0.81
20260512,86.5,86.5,86.5,86.5,1248000,74.15,16.65,78.19,57.9,0.94
20260513,95.1,95.1,95.1,95.1,1296000,75.9,25.3,79.83,58.73,0.96
20260514,104.5,104.5,98.7,104.5,9909000,78.28,33.5,81.62,59.73,5.47
20260515,106,108.5,97.5,99.8,6968000,80.07,24.64,82.84,60.65,3.69
20260518,97.5,97.9,90.9,94.6,2132000,81.28,16.38,83.82,61.48,1.15
20260519,93,104,93,103.5,6587000,83.14,24.5,85.27,62.46,3.11
20260520,100,101.5,93.8,93.8,3621000,84.02,11.63,86.21,63.27,1.59
20260521,96.3,103,96.1,102,2796000,85.52,19.27,87.19,64.23,1.2
20260522,103,104,98.6,99,101000,86.64,14.26,87.7,65.12,0.05
20260525,99.8,103,99.1,100,101000,87.76,13.95,88.55,66.02,0.05
20260526,103,103,96.6,97.8,98000,88.59,10.39,89.27,66.89,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.85
- over_600_ratio: 60.79
- over_800_ratio: 57.85
- over_1000_ratio: 53.15
- over_400_change_1w: -2.71
- over_800_change_1w: -3.16
- over_1000_change_1w: -3.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.72,,59.77,,55.08,,0,False,False
20260508,68.17,-0.55,59.76,-0.01,55.07,-0.01,0,False,False
20260515,68.56,0.39,61.01,1.25,56.3,1.23,1,True,True
20260522,65.85,-2.71,57.85,-3.16,53.15,-3.15,0,False,False
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
