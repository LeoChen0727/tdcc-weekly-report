# INDIVIDUAL STOCK CHATGPT PACKET - 3162 精確

## Metadata
- generated_at: 2026-05-30 23:41:53 Asia/Taipei
- stock_id: 3162
- stock_name: 精確
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3162_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3162_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3162_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3162_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3162_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3162_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3162_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3162_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3162_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3162_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3162_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3162_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3162_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3162.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3162.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3162.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3162.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3162.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3162.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3162_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3162_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3162_latest.md?ref=main

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
- open: 83
- high: 84.7
- low: 81
- close: 84.7
- volume: 82000
- ma5: 85.54
- ema23_primary: 83.35
- distance_to_ema23_pct: 1.62
- ma20: 86.43
- ma60: 70.79
- ma120: 65.16
- return_5d: -3.31
- return_20d: 15.71
- volume_ratio: 0.01
- distance_to_ma20_pct_auxiliary: -2
- distance_to_high_60_pct: -13.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,72.3,77.3,70.6,75.5,7415000,70.65,6.86,70.82,62.09,1.08
20260505,74.9,83,74.7,83,8650000,71.68,15.79,72.03,62.41,1.21
20260506,87.9,91.3,85.9,89.8,23316000,73.19,22.69,73.47,62.88,2.85
20260507,88.6,97.2,84.6,95.9,20147000,75.09,27.72,74.92,63.44,2.29
20260508,94.9,97.8,90.3,91.1,10292000,76.42,19.21,76.11,63.94,1.15
20260511,91.5,92.3,86.1,90.5,8228000,77.59,16.63,77.47,64.44,0.9
20260512,89.1,91.1,86.9,88.2,4251000,78.48,12.39,78.55,64.92,0.47
20260513,87.2,88.2,86.2,87.5,2608000,79.23,10.44,79.55,65.36,0.29
20260514,86.2,87.4,83.1,83.7,5540000,79.6,5.15,80.38,65.74,0.61
20260515,83.7,86.8,83.5,83.7,3579000,79.94,4.7,81.42,66.17,0.4
20260518,83,86.5,79.5,84,3520000,80.28,4.63,82.39,66.62,0.39
20260519,84.2,91.5,84.1,87.2,5754000,80.86,7.84,83.3,67.1,0.65
20260520,87.6,88.7,84.9,85.1,2930000,81.21,4.79,84.08,67.54,0.33
20260521,86.4,89.3,85.5,88.1,3414000,81.79,7.72,84.67,68.01,0.39
20260522,88.5,90.3,87.1,87.6,89000,82.27,6.48,84.86,68.5,0.01
20260525,88.6,89.2,85.1,87,87000,82.66,5.25,85.12,69,0.01
20260526,89,93.8,88.7,90.1,92000,83.28,8.18,85.55,69.54,0.01
20260527,93,93,82,83.6,86000,83.31,0.35,85.64,69.95,0.01
20260528,84.7,86.1,80.3,82.3,83000,83.23,-1.11,85.86,70.33,0.01
20260529,83,84.7,81,84.7,82000,83.35,1.62,86.43,70.79,0.01
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 58.89
- over_600_ratio: 57.6
- over_800_ratio: 55.93
- over_1000_ratio: 53.7
- over_400_change_1w: -4.18
- over_800_change_1w: -4.02
- over_1000_change_1w: -3.36
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.99,,56.83,,56.3,,0,False,False
20260508,64.01,2.02,57.1,0.27,55.39,-0.91,1,False,True
20260515,61.79,-2.22,57.42,0.32,56.25,0.86,2,False,True
20260522,63.07,1.28,59.95,2.53,57.06,0.81,3,True,True
20260529,58.89,-4.18,55.93,-4.02,53.7,-3.36,0,False,False
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
