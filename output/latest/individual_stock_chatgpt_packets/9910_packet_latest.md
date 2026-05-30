# INDIVIDUAL STOCK CHATGPT PACKET - 9910 豐泰

## Metadata
- generated_at: 2026-05-30 23:44:03 Asia/Taipei
- stock_id: 9910
- stock_name: 豐泰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9910_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9910_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9910_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9910_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9910_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9910_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9910_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9910_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9910_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9910_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9910_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9910_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9910_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9910.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9910.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9910.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9910.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9910.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9910.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9910_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9910_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9910_latest.md?ref=main

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
- open: 69
- high: 70.2
- low: 68
- close: 70.2
- volume: 4100850
- ma5: 68.14
- ema23_primary: 70.78
- distance_to_ema23_pct: -0.82
- ma20: 70.08
- ma60: 77
- ma120: 92.68
- return_5d: 2.18
- return_20d: 0.14
- volume_ratio: 1.58
- distance_to_ma20_pct_auxiliary: 0.18
- distance_to_high_60_pct: -27.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,70.2,72.4,69.2,70.7,2606124,76.22,-7.24,75.86,84.51,1.19
20260505,70.7,70.7,69,69.3,2851762,75.64,-8.39,75.38,84.07,1.28
20260506,69.3,69.3,67.7,68.8,2913085,75.07,-8.36,74.88,83.6,1.26
20260507,68.5,70.8,68,70.1,3182357,74.66,-6.11,74.33,83.19,1.35
20260508,71,74.4,70.7,73.8,3581786,74.59,-1.06,74.09,82.86,1.46
20260511,74.4,77.5,73.8,74.4,2871152,74.57,-0.23,73.97,82.5,1.15
20260512,75.4,75.4,73.2,73.5,1998204,74.48,-1.32,73.74,82.17,0.78
20260513,72.7,73.2,71.5,71.6,1133835,74.24,-3.56,73.52,81.82,0.46
20260514,71,71.9,69.7,70.5,1295428,73.93,-4.64,73.2,81.44,0.53
20260515,70.8,71.8,70.1,70.3,2059928,73.63,-4.52,72.81,81.05,0.85
20260518,71.2,72.1,70,70.4,3253452,73.36,-4.03,72.46,80.67,1.3
20260519,70.4,70.9,69.3,69.4,1888697,73.03,-4.97,72.03,80.29,0.76
20260520,69.5,70.2,68.6,70.1,2198923,72.79,-3.69,71.63,79.92,0.88
20260521,70.5,70.7,69.2,69.2,1951826,72.49,-4.53,71.22,79.53,0.79
20260522,69.2,69.8,67.8,68.7,3534389,72.17,-4.81,70.85,79.11,1.4
20260525,69,69.3,67.8,67.8,2260102,71.81,-5.58,70.59,78.69,0.95
20260526,67.7,68,66.8,67.5,2485835,71.45,-5.53,70.44,78.23,1.05
20260527,67.5,67.8,66.4,67.2,3259714,71.09,-5.48,70.21,77.78,1.35
20260528,67.3,68.4,66.8,68,2558891,70.84,-4,70.07,77.37,1.04
20260529,69,70.2,68,70.2,4100850,70.78,-0.82,70.08,77,1.58
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 89.7
- over_600_ratio: 88.69
- over_800_ratio: 87.62
- over_1000_ratio: 86.81
- over_400_change_1w: -0.16
- over_800_change_1w: -0.4
- over_1000_change_1w: -0.4
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,90.03,,88.17,,87.54,,0,False,False
20260508,90.03,0,88.19,0.02,87.46,-0.08,1,False,True
20260515,89.93,-0.1,88.2,0.01,87.29,-0.17,2,False,True
20260522,89.86,-0.07,88.02,-0.18,87.21,-0.08,0,False,False
20260529,89.7,-0.16,87.62,-0.4,86.81,-0.4,0,False,False
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
