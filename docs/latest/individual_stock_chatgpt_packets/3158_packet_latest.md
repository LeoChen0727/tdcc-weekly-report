# INDIVIDUAL STOCK CHATGPT PACKET - 3158 嘉實

## Metadata
- generated_at: 2026-05-26 22:19:00 Asia/Taipei
- stock_id: 3158
- stock_name: 嘉實
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 123
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3158_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3158_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3158_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3158_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3158_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3158_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3158_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3158_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3158_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3158_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3158_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3158_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3158_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3158.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3158.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3158.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3158.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3158.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3158.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3158_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3158_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3158_latest.md?ref=main

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
- open: 85.6
- high: 85.6
- low: 85.2
- close: 85.4
- volume: 86000
- ma5: 85.7
- ema23_primary: 87.76
- distance_to_ema23_pct: -2.69
- ma20: 87.86
- ma60: 90.09
- ma120: 91.41
- return_5d: -0.7
- return_20d: -6.15
- volume_ratio: 3.18
- distance_to_ma20_pct_auxiliary: -2.81
- distance_to_high_60_pct: -14.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,90.1,91,89.6,89.6,15000,90.79,-1.31,90.62,90.74,0.6
20260429,90,90,90,90,9000,90.72,-0.8,90.44,90.72,0.51
20260430,90.4,90.4,89.3,89.3,13000,90.61,-1.44,90.36,90.7,0.77
20260504,89.4,90.3,89.4,90.3,15000,90.58,-0.31,90.33,90.69,0.88
20260505,89.1,90.2,89.1,90.2,22000,90.55,-0.38,90.35,90.68,1.29
20260506,89.5,89.5,89,89.1,29000,90.43,-1.47,90.31,90.65,1.59
20260507,89.2,89.9,89,89,26000,90.31,-1.45,90.21,90.62,1.35
20260508,89,89.9,89,89,12000,90.2,-1.33,90.17,90.61,0.62
20260511,89.1,89.1,88.7,88.8,23000,90.08,-1.42,90,90.59,1.26
20260512,89,89,88.2,88.3,24000,89.93,-1.82,89.81,90.56,1.33
20260513,88.2,88.2,87.8,88,14000,89.77,-1.98,89.72,90.55,0.8
20260514,88,88,87.4,87.4,14000,89.58,-2.43,89.53,90.52,0.85
20260515,87.5,87.5,87,87.1,13000,89.37,-2.54,89.39,90.48,0.76
20260518,86.8,86.9,86.7,86.7,6000,89.15,-2.74,89.27,90.45,0.36
20260519,86.2,86.2,86,86,16000,88.88,-3.25,89,90.39,0.99
20260520,86.9,87,85.1,85.1,14000,88.57,-3.92,88.75,90.33,0.87
20260521,85.2,87.5,85.2,86.6,18000,88.4,-2.04,88.57,90.31,1.08
20260522,85.2,86.5,85.2,85.8,86000,88.19,-2.71,88.36,90.24,4.48
20260525,85.6,89.1,85.6,85.6,86000,87.97,-2.7,88.14,90.17,3.74
20260526,85.6,85.6,85.2,85.4,86000,87.76,-2.69,87.86,90.09,3.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 37.59
- over_600_ratio: 32.83
- over_800_ratio: 26.49
- over_1000_ratio: 23.42
- over_400_change_1w: 0.01
- over_800_change_1w: 0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,37.59,,26.49,,23.43,,0,False,False
20260508,37.59,0,26.49,0,23.43,0,0,False,False
20260515,37.58,-0.01,26.48,-0.01,23.42,-0.01,0,False,False
20260522,37.59,0.01,26.49,0.01,23.42,0,1,False,True
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
