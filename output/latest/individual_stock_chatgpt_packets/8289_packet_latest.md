# INDIVIDUAL STOCK CHATGPT PACKET - 8289 泰藝

## Metadata
- generated_at: 2026-05-26 22:20:48 Asia/Taipei
- stock_id: 8289
- stock_name: 泰藝
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8289_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8289_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8289_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8289_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8289_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8289_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8289_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8289_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8289_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8289_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8289_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8289_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8289_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8289.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8289.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8289.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8289.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8289.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8289.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8289_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8289_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8289_latest.md?ref=main

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
- open: 67.9
- high: 69.9
- low: 64
- close: 69.5
- volume: 67000
- ma5: 64.06
- ema23_primary: 54.77
- distance_to_ema23_pct: 26.9
- ma20: 53.91
- ma60: 44.23
- ma120: 33.48
- return_5d: 28.94
- return_20d: 65.08
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: 28.91
- distance_to_high_60_pct: -5.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,42.6,46,42.6,46,929000,43.3,6.23,43.06,35.4,0.17
20260429,45.1,46.5,44.5,45.25,720000,43.46,4.11,43.39,35.74,0.15
20260430,45.6,46.2,44.6,45.35,530000,43.62,3.97,43.79,36.09,0.12
20260504,45.95,46.8,44.6,46.8,789000,43.89,6.64,44.27,36.44,0.18
20260505,47,49.35,46.1,49.35,659000,44.34,11.3,44.95,36.84,0.15
20260506,50,50,47.35,47.8,1011000,44.63,7.11,45.58,37.23,0.23
20260507,46.95,52.5,46.7,52.5,6807000,45.28,15.93,46.36,37.69,1.45
20260508,52.3,54.3,48,48.8,8153000,45.58,7.07,46.98,38.09,1.61
20260511,48.9,51.3,45.05,49.95,4500000,45.94,8.72,47.59,38.53,0.87
20260512,51.1,54.9,48.6,54.9,7072000,46.69,17.59,48.26,39.07,1.35
20260513,54.8,58.9,54.3,54.3,10403000,47.32,14.74,48.96,39.56,1.9
20260514,54.7,59.4,52.5,53,4547000,47.8,10.89,49.46,39.99,0.88
20260515,54.6,56.2,53.1,54,3378000,48.31,11.77,49.8,40.41,0.65
20260518,53.8,57,53.7,56.1,4449000,48.96,14.58,50.12,40.88,1.03
20260519,56.1,56.5,53.3,53.9,2481000,49.37,9.17,50.09,41.35,0.64
20260520,54.8,58.3,54.1,55.3,5154000,49.87,10.89,50.02,41.8,1.49
20260521,56.3,60.8,55.9,60.8,10326000,50.78,19.74,50.45,42.36,2.69
20260522,61.3,66.8,61.1,66.8,65000,52.11,28.18,51.4,42.99,0.02
20260525,71.2,73.4,66.7,67.9,70000,53.43,27.08,52.55,43.6,0.02
20260526,67.9,69.9,64,69.5,67000,54.77,26.9,53.91,44.23,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.29
- over_600_ratio: 42.23
- over_800_ratio: 40.24
- over_1000_ratio: 37.67
- over_400_change_1w: 1.3
- over_800_change_1w: -0.19
- over_1000_change_1w: 1.25
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.48,,38.1,,34.25,,0,False,False
20260508,48.97,1.49,40.35,2.25,37.78,3.53,1,True,True
20260515,47.99,-0.98,40.43,0.08,36.42,-1.36,2,False,True
20260522,49.29,1.3,40.24,-0.19,37.67,1.25,3,False,True
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
