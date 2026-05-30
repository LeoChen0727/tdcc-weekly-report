# INDIVIDUAL STOCK CHATGPT PACKET - 2722 夏都

## Metadata
- generated_at: 2026-05-30 23:41:38 Asia/Taipei
- stock_id: 2722
- stock_name: 夏都
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2722_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2722_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2722_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2722_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2722_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2722_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2722_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2722_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2722_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2722_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2722_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2722_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2722_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2722.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2722.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2722.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2722.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2722.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2722.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2722_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2722_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2722_latest.md?ref=main

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
- open: 22.7
- high: 22.7
- low: 22.25
- close: 22.35
- volume: 75695
- ma5: 22.45
- ema23_primary: 22.92
- distance_to_ema23_pct: -2.5
- ma20: 22.93
- ma60: 23.39
- ma120: 24.74
- return_5d: -1.32
- return_20d: -4.08
- volume_ratio: 1.86
- distance_to_ma20_pct_auxiliary: -2.55
- distance_to_high_60_pct: -15.66

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,23.75,23.75,23.4,23.4,27866,23.79,-1.65,23.98,24.14,0.36
20260505,23.6,23.65,23.4,23.4,38759,23.76,-1.51,23.98,24.12,0.52
20260506,23.3,24,23.3,23.5,33555,23.74,-1,23.98,24.09,0.45
20260507,23.65,23.65,23.35,23.4,17172,23.71,-1.31,23.95,24.06,0.24
20260508,24.1,24.25,23.4,23.5,51030,23.69,-0.81,23.97,24.02,0.71
20260511,23.85,23.85,23.5,23.5,23205,23.68,-0.74,23.99,23.99,0.32
20260512,23.8,23.8,23.4,23.4,34966,23.65,-1.07,23.88,23.97,0.55
20260513,23.6,23.75,23,23.7,50112,23.66,0.18,23.82,23.95,1.05
20260514,23.2,23.9,23.15,23.3,49814,23.63,-1.39,23.73,23.93,1.07
20260515,23.55,23.55,22.85,23.05,40822,23.58,-2.24,23.64,23.88,0.88
20260518,23,23,22.4,22.5,92832,23.49,-4.21,23.54,23.83,1.95
20260519,22.55,22.55,22.15,22.5,20287,23.41,-3.87,23.45,23.79,0.49
20260520,22.6,22.6,22.25,22.3,24162,23.31,-4.35,23.34,23.74,0.6
20260521,22.75,22.75,22.2,22.35,23799,23.23,-3.81,23.24,23.69,0.6
20260522,22.6,22.65,22.2,22.65,21627,23.19,-2.31,23.19,23.64,0.57
20260525,23.1,23.1,22.15,22.55,46480,23.13,-2.52,23.12,23.59,1.23
20260526,22.85,22.85,22.3,22.4,43960,23.07,-2.91,23.07,23.53,1.17
20260527,22.95,22.95,22.3,22.6,66423,23.03,-1.88,23.04,23.48,1.66
20260528,22.55,22.75,22.35,22.35,31471,22.98,-2.72,22.98,23.44,0.78
20260529,22.7,22.7,22.25,22.35,75695,22.92,-2.5,22.93,23.39,1.86
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 87.41
- over_600_ratio: 86.14
- over_800_ratio: 83.67
- over_1000_ratio: 82.36
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
20260430,87.41,,83.53,,82.22,,0,False,False
20260508,87.41,0,83.53,0,82.22,0,0,False,False
20260515,87.42,0.01,83.53,0,82.22,0,1,False,False
20260522,87.41,-0.01,83.67,0.14,82.36,0.14,2,False,True
20260529,87.41,0,83.67,0,82.36,0,0,False,False
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
