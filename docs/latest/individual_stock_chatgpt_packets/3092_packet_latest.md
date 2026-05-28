# INDIVIDUAL STOCK CHATGPT PACKET - 3092 鴻碩

## Metadata
- generated_at: 2026-05-28 19:32:17 Asia/Taipei
- stock_id: 3092
- stock_name: 鴻碩
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3092_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3092_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3092_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3092_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3092_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3092_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3092_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3092_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3092_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3092_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3092_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3092_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3092_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3092.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3092.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3092.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3092.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3092.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3092.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3092_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3092_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3092_latest.md?ref=main

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
- date: 20260528
- open: 29.5
- high: 30.5
- low: 28.75
- close: 28.9
- volume: 503097
- ma5: 29.94
- ema23_primary: 30.28
- distance_to_ema23_pct: -4.54
- ma20: 30.22
- ma60: 31.58
- ma120: 26.96
- return_5d: -0.34
- return_20d: -11.35
- volume_ratio: 0.92
- distance_to_ma20_pct_auxiliary: -4.36
- distance_to_high_60_pct: -28.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,32.75,32.75,32,32,442602,32.2,-0.61,32,30.28,0.31
20260504,31.8,31.95,31.15,31.35,611985,32.13,-2.42,32.13,30.38,0.43
20260505,31.35,32.3,31.35,32.3,428059,32.14,0.5,32.29,30.5,0.3
20260506,32.3,32.9,31.1,31.4,707030,32.08,-2.12,32.43,30.57,0.49
20260507,31.3,32.4,31.15,32,664826,32.07,-0.23,32.58,30.65,0.46
20260508,32,32.7,30.95,30.95,781648,31.98,-3.22,32.69,30.73,0.53
20260511,30.1,30.75,29.9,30.25,571184,31.83,-4.98,32.74,30.82,0.39
20260512,30.3,30.8,30.25,30.8,307891,31.75,-2.99,32.78,30.93,0.22
20260513,30.35,30.55,29.5,30.1,471395,31.61,-4.78,32.63,31.04,0.34
20260514,30.05,30.2,29.15,29.35,610619,31.42,-6.6,32.28,31.13,0.45
20260515,30.2,30.2,28.4,29.15,655622,31.23,-6.67,32.02,31.2,0.68
20260518,28.8,29.95,28.1,29.2,401095,31.06,-6,31.72,31.29,0.46
20260519,29.3,29.45,28.5,28.7,263605,30.87,-7.02,31.42,31.39,0.35
20260520,28.65,28.8,28.1,28.1,238174,30.64,-8.28,31.1,31.47,0.35
20260521,28.5,29.35,28.5,29,368266,30.5,-4.92,30.84,31.56,0.57
20260522,28.95,31.9,28.95,30.7,1042808,30.52,0.6,30.75,31.65,1.7
20260525,31,31.4,30.05,30.3,750162,30.5,-0.65,30.68,31.71,1.22
20260526,30.05,30.4,29.8,30.3,566796,30.48,-0.6,30.6,31.73,0.94
20260527,30.5,30.85,29.4,29.5,607302,30.4,-2.96,30.4,31.69,1.1
20260528,29.5,30.5,28.75,28.9,503097,30.28,-4.54,30.22,31.58,0.92
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.55
- over_600_ratio: 32.6
- over_800_ratio: 30.05
- over_1000_ratio: 29.19
- over_400_change_1w: 0.21
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.36,,30.05,,29.19,,0,False,False
20260508,33.88,-0.48,30.05,0,29.19,0,0,False,False
20260515,34.34,0.46,30.05,0,29.19,0,1,False,False
20260522,34.55,0.21,30.05,0,29.19,0,2,False,False
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
