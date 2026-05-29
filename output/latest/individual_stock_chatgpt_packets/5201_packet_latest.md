# INDIVIDUAL STOCK CHATGPT PACKET - 5201 凱衛

## Metadata
- generated_at: 2026-05-29 19:33:02 Asia/Taipei
- stock_id: 5201
- stock_name: 凱衛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5201_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5201_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5201_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5201_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5201_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5201_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5201_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5201_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5201_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5201_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5201_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5201_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5201_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5201.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5201.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5201.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5201.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5201.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5201.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5201_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5201_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5201_latest.md?ref=main

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
- open: 28.7
- high: 28.7
- low: 27.85
- close: 28.35
- volume: 28000
- ma5: 28.42
- ema23_primary: 30.15
- distance_to_ema23_pct: -5.98
- ma20: 29.51
- ma60: 34.92
- ma120: 39.61
- return_5d: -2.07
- return_20d: -7.05
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: -3.94
- distance_to_high_60_pct: -30.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,30.75,30.75,29.95,30.35,201000,34.55,-12.15,35.23,38.82,0.75
20260505,30.5,30.7,30.45,30.6,63000,34.22,-10.58,34.8,38.58,0.23
20260506,31.25,31.25,30.35,30.7,47000,33.93,-9.51,34.38,38.33,0.18
20260507,31.1,31.1,30.5,30.65,52000,33.65,-8.92,33.98,38.09,0.2
20260508,30.65,30.7,30,30.4,49000,33.38,-8.93,33.55,37.85,0.19
20260511,30.6,30.8,30.2,30.55,50000,33.15,-7.83,33.13,37.66,0.19
20260512,30.6,30.65,30.15,30.5,39000,32.93,-7.37,32.72,37.48,0.15
20260513,30.5,30.5,29.4,29.55,120000,32.64,-9.48,32.23,37.26,0.45
20260514,29,29.55,28.35,28.8,146000,32.32,-10.9,31.7,37.04,0.54
20260515,30.05,30.05,28.9,29.4,58000,32.08,-8.35,31.2,36.85,0.21
20260518,29.1,29.5,29.05,29.45,12000,31.86,-7.57,30.72,36.67,0.04
20260519,29.55,29.55,28.5,29.4,30000,31.66,-7.13,30.33,36.49,0.11
20260520,29.4,29.65,29,29.45,28000,31.47,-6.42,30.13,36.29,0.12
20260521,29.45,29.9,28.9,29.4,42000,31.3,-6.07,30.08,36.1,0.45
20260522,29,29.2,27.55,28.95,28000,31.1,-6.92,30,35.9,0.39
20260525,28.95,29,28.45,28.75,29000,30.91,-6.98,29.91,35.72,0.46
20260526,29.75,29.75,28.4,28.4,29000,30.7,-7.49,29.82,35.52,0.48
20260527,28.6,28.75,27.95,28.3,28000,30.5,-7.21,29.73,35.33,0.47
20260528,28.3,28.3,27.15,28.3,28000,30.32,-6.65,29.62,35.1,0.49
20260529,28.7,28.7,27.85,28.35,28000,30.15,-5.98,29.51,34.92,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 59.25
- over_600_ratio: 52.1
- over_800_ratio: 42.67
- over_1000_ratio: 35.41
- over_400_change_1w: 1.12
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.22,,41.94,,34.68,,0,False,False
20260508,56.61,-0.61,42.37,0.43,35.11,0.43,1,False,True
20260515,58.13,1.52,42.65,0.28,35.39,0.28,2,True,True
20260522,59.25,1.12,42.67,0.02,35.41,0.02,3,True,True
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
