# INDIVIDUAL STOCK CHATGPT PACKET - 3040 遠見

## Metadata
- generated_at: 2026-05-26 23:53:37 Asia/Taipei
- stock_id: 3040
- stock_name: 遠見
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3040_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3040_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3040_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3040_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3040_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3040_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3040_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3040_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3040_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3040_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3040_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3040_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3040_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3040.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3040.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3040.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3040.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3040.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3040.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3040_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3040_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3040_latest.md?ref=main

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
- open: 40.7
- high: 41.5
- low: 39.65
- close: 41.15
- volume: 169114
- ma5: 40.1
- ema23_primary: 41.58
- distance_to_ema23_pct: -1.02
- ma20: 41.01
- ma60: 44.51
- ma120: 48.64
- return_5d: 4.18
- return_20d: -7.53
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: 0.35
- distance_to_high_60_pct: -23.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,44.9,45.1,44.25,44.25,95307,46.67,-5.19,47.63,46.39,0.48
20260429,44.25,44.45,43.8,43.8,79660,46.43,-5.67,47.15,46.3,0.4
20260430,43.85,43.85,42.85,42.85,129828,46.13,-7.12,46.66,46.2,0.66
20260504,42.9,44.35,41.6,43.45,221754,45.91,-5.36,46.26,46.1,1.13
20260505,43.5,44.25,43.1,43.2,55658,45.69,-5.44,45.91,46.02,0.29
20260506,43.55,43.6,42.05,42.8,169401,45.44,-5.82,45.55,45.95,0.89
20260507,42,42.8,42,42.35,118240,45.19,-6.28,45.16,45.91,0.63
20260508,42.35,42.35,40.5,40.9,297047,44.83,-8.77,44.78,45.8,1.52
20260511,40.9,40.9,40,40,203449,44.43,-9.96,44.4,45.61,1.12
20260512,40,40.25,39,39,221643,43.97,-11.31,44,45.33,1.26
20260513,39.5,40.2,38.4,39.8,107975,43.63,-8.77,43.63,45.1,0.65
20260514,39.8,40.05,39.05,39.05,92237,43.25,-9.7,43.27,44.88,0.56
20260515,39.15,41,39.1,39.2,142344,42.91,-8.64,42.91,44.75,0.85
20260518,39,40.55,38.9,39.5,146232,42.62,-7.33,42.66,44.67,0.9
20260519,40,40.15,39,39.5,184516,42.36,-6.76,42.43,44.62,1.16
20260520,40.05,40.5,39.5,40.05,53590,42.17,-5.03,42.19,44.58,0.35
20260521,40.05,40.3,40,40.2,30135,42.01,-4.3,41.86,44.55,0.21
20260522,39.95,40.2,39.35,39.6,117239,41.81,-5.28,41.52,44.52,0.85
20260525,40.05,40.3,39.2,39.5,102874,41.61,-5.08,41.17,44.49,0.75
20260526,40.7,41.5,39.65,41.15,169114,41.58,-1.02,41.01,44.51,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.97
- over_600_ratio: 65.46
- over_800_ratio: 65.46
- over_1000_ratio: 65.46
- over_400_change_1w: 0.08
- over_800_change_1w: 0.08
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.45,,65.35,,65.35,,0,False,False
20260508,70.95,0.5,65.27,-0.08,65.27,-0.08,1,False,False
20260515,69.89,-1.06,65.38,0.11,65.38,0.11,2,False,True
20260522,69.97,0.08,65.46,0.08,65.46,0.08,3,True,True
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
