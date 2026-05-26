# INDIVIDUAL STOCK CHATGPT PACKET - 5228 鈺鎧

## Metadata
- generated_at: 2026-05-26 23:54:16 Asia/Taipei
- stock_id: 5228
- stock_name: 鈺鎧
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5228_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5228_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5228_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5228_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5228_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5228_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5228_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5228_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5228_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5228_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5228_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5228_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5228_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5228.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5228.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5228.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5228.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5228.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5228.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5228_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5228_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5228_latest.md?ref=main

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
- open: 53.3
- high: 55
- low: 53.1
- close: 54.9
- volume: 54000
- ma5: 52.8
- ema23_primary: 43.85
- distance_to_ema23_pct: 25.2
- ma20: 43.37
- ma60: 31.95
- ma120: 26.69
- return_5d: 20.13
- return_20d: 81.79
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: 26.6
- distance_to_high_60_pct: -1.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,30,32.1,30,32,243000,29.78,7.45,29.36,25.58,0.25
20260429,33.3,34.6,32.3,33.95,324000,30.13,12.69,29.89,25.71,0.33
20260430,34.8,34.8,32.75,34,256000,30.45,11.66,30.43,25.8,0.26
20260504,33.7,35.25,33.7,34.55,490000,30.79,12.2,30.95,25.95,0.49
20260505,34.6,34.95,32.25,33.3,748000,31,7.42,31.45,26.08,0.73
20260506,33.35,34.8,32.25,33.05,749000,31.17,6.02,31.95,26.21,0.7
20260507,32.8,36.35,32.8,36.35,890000,31.6,15.02,32.63,26.4,0.81
20260508,39.95,39.95,39.95,39.95,805000,32.3,23.69,33.37,26.68,0.71
20260511,43.9,43.9,39.1,41.7,4822000,33.08,26.05,34.07,26.97,3.57
20260512,41.4,45.85,39.75,45.85,4241000,34.15,34.27,34.88,27.37,3.21
20260513,45.65,49.9,44.25,49.15,5990000,35.4,38.85,35.86,27.82,3.85
20260514,53.2,53.9,49.8,50.2,4290000,36.63,37.05,36.84,28.27,2.61
20260515,49.2,54.8,48.35,49.15,3580000,37.67,30.46,37.6,28.71,2.08
20260518,46.1,46.1,44.25,44.4,686000,38.23,16.13,37.97,29.08,0.43
20260519,44.8,47.7,44.8,45.7,383000,38.86,17.61,38.42,29.47,0.25
20260520,48.75,50.1,47.85,50.1,422000,39.79,25.9,39.13,29.93,0.28
20260521,50.8,52.5,50.5,52.5,496000,40.85,28.51,40.05,30.45,0.33
20260522,52.5,52.5,50.5,51.6,52000,41.75,23.6,40.97,30.92,0.03
20260525,56,56,53.5,54.9,55000,42.84,28.14,42.13,31.44,0.04
20260526,53.3,55,53.1,54.9,54000,43.85,25.2,43.37,31.95,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.52
- over_600_ratio: 51.02
- over_800_ratio: 49.31
- over_1000_ratio: 49.31
- over_400_change_1w: -0.59
- over_800_change_1w: -0.42
- over_1000_change_1w: -0.42
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.43,,51.98,,51.98,,0,False,False
20260508,65.29,-0.14,51.76,-0.22,51.76,-0.22,0,False,False
20260515,59.11,-6.18,49.73,-2.03,49.73,-2.03,0,False,False
20260522,58.52,-0.59,49.31,-0.42,49.31,-0.42,0,False,False
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
