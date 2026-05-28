# INDIVIDUAL STOCK CHATGPT PACKET - 3128 昇銳

## Metadata
- generated_at: 2026-05-28 19:32:17 Asia/Taipei
- stock_id: 3128
- stock_name: 昇銳
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3128_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3128_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3128_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3128_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3128_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3128_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3128_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3128_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3128_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3128_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3128_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3128_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3128_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3128.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3128.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3128.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3128.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3128.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3128.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3128_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3128_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3128_latest.md?ref=main

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
- open: 23.25
- high: 23.5
- low: 22.75
- close: 22.8
- volume: 227516
- ma5: 23.73
- ema23_primary: 23.59
- distance_to_ema23_pct: -3.34
- ma20: 23.42
- ma60: 24.38
- ma120: 26.02
- return_5d: -4
- return_20d: -3.8
- volume_ratio: 1.71
- distance_to_ma20_pct_auxiliary: -2.66
- distance_to_high_60_pct: -15.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,23.65,24.2,23.6,23.8,124000,24.5,-2.85,24.36,25.55,0.89
20260504,23.9,24.5,23.9,24.25,102000,24.48,-0.93,24.36,25.46,0.73
20260505,24.3,24.3,23.9,24.15,93000,24.45,-1.22,24.35,25.38,0.67
20260506,24.15,24.15,23.75,23.9,140000,24.4,-2.06,24.34,25.3,0.99
20260507,24.35,24.35,23.7,23.75,149000,24.35,-2.46,24.31,25.23,1.07
20260508,23.7,24,23.5,23.7,130000,24.3,-2.45,24.27,25.16,0.93
20260511,23.6,24,23.4,23.45,124000,24.22,-3.2,24.23,25.11,0.9
20260512,23.45,23.45,22.85,23.05,192000,24.13,-4.46,24.17,25.05,1.35
20260513,22.9,22.9,22.55,22.7,87000,24.01,-5.45,24.09,25,0.61
20260514,23.45,23.45,22.75,22.9,79000,23.92,-4.25,24.02,24.93,0.56
20260515,23.5,23.5,22.7,22.7,87000,23.81,-4.68,23.93,24.87,0.63
20260518,22.95,23,22.8,23,37000,23.75,-3.14,23.84,24.81,0.28
20260519,23,23,21.3,21.3,171000,23.54,-9.53,23.67,24.73,1.33
20260520,21.7,23.4,21.7,23.4,249000,23.53,-0.56,23.57,24.68,1.91
20260521,24,24.1,23.25,23.75,573000,23.55,0.85,23.49,24.64,3.8
20260522,24.1,24.55,23.55,24.25,24000,23.61,2.72,23.48,24.6,0.17
20260525,24.7,24.75,24.1,24.5,24000,23.68,3.46,23.5,24.57,0.18
20260526,24.75,24.75,23.8,23.85,24000,23.7,0.65,23.5,24.51,0.19
20260527,23.9,23.9,23.05,23.25,23000,23.66,-1.73,23.47,24.45,0.18
20260528,23.25,23.5,22.75,22.8,227516,23.59,-3.34,23.42,24.38,1.71
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 31.12
- over_600_ratio: 30.1
- over_800_ratio: 25.86
- over_1000_ratio: 23.87
- over_400_change_1w: -0.06
- over_800_change_1w: 0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,31,,25.85,,23.87,,0,False,False
20260508,31.15,0.15,25.85,0,23.87,0,1,False,False
20260515,31.18,0.03,25.85,0,23.87,0,2,False,False
20260522,31.12,-0.06,25.86,0.01,23.87,0,3,False,True
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
