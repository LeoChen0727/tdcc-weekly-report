# INDIVIDUAL STOCK CHATGPT PACKET - 3232 昱捷

## Metadata
- generated_at: 2026-05-28 19:32:20 Asia/Taipei
- stock_id: 3232
- stock_name: 昱捷
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3232_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3232_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3232_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3232_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3232_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3232_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3232_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3232_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3232_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3232_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3232_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3232_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3232_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3232.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3232.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3232.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3232.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3232.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3232.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3232_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3232_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3232_latest.md?ref=main

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
- open: 20.75
- high: 22.9
- low: 20.75
- close: 22.9
- volume: 336052
- ma5: 21.85
- ema23_primary: 21.52
- distance_to_ema23_pct: 6.43
- ma20: 21.22
- ma60: 22.04
- ma120: 22.77
- return_5d: 2.69
- return_20d: 5.77
- volume_ratio: 4.37
- distance_to_ma20_pct_auxiliary: 7.9
- distance_to_high_60_pct: -3.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,21.5,21.6,21.35,21.4,58000,22.11,-3.23,22.14,22.56,1.01
20260504,21.4,21.55,21,21,128000,22.02,-4.64,22.07,22.52,2.06
20260505,21.1,21.15,20.8,21.15,85000,21.95,-3.64,22,22.49,1.29
20260506,21.6,21.6,21.05,21.15,73000,21.88,-3.35,21.94,22.46,1.08
20260507,20.95,21.15,20.85,21.1,96000,21.82,-3.29,21.88,22.43,1.33
20260508,21.1,21.1,20.7,20.8,83000,21.73,-4.29,21.8,22.39,1.1
20260511,21.05,21.05,20.8,20.85,71000,21.66,-3.73,21.73,22.36,0.92
20260512,20.8,20.95,20.65,20.95,57000,21.6,-3.01,21.67,22.33,0.75
20260513,20.8,21.05,20.7,21.05,45000,21.55,-2.34,21.62,22.31,0.59
20260514,20.95,20.95,20.75,20.85,39000,21.5,-3,21.55,22.28,0.52
20260515,20.8,20.8,20.25,20.75,98000,21.43,-3.19,21.46,22.25,1.27
20260518,20.65,20.65,20.45,20.6,11000,21.36,-3.57,21.36,22.22,0.15
20260519,20.3,20.7,20.25,20.7,32000,21.31,-2.86,21.27,22.2,0.43
20260520,20.4,20.65,20.4,20.55,58000,21.25,-3.27,21.19,22.17,0.82
20260521,20.5,22.6,20.5,22.3,180000,21.33,4.53,21.2,22.16,2.39
20260522,22.75,22.75,22,22.3,22000,21.41,4.14,21.21,22.14,0.31
20260525,22.3,22.55,21.8,22,22000,21.46,2.5,21.22,22.13,0.32
20260526,22.2,22.2,21.1,21.2,22000,21.44,-1.12,21.2,22.09,0.34
20260527,21.2,21.2,20.85,20.85,21000,21.39,-2.53,21.16,22.05,0.33
20260528,20.75,22.9,20.75,22.9,336052,21.52,6.43,21.22,22.04,4.37
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.88
- over_600_ratio: 49.5
- over_800_ratio: 45.17
- over_1000_ratio: 41.44
- over_400_change_1w: 0.05
- over_800_change_1w: 0.05
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.02,,45.16,,41.51,,0,False,False
20260508,58.81,0.79,45.14,-0.02,41.48,-0.03,1,False,False
20260515,57.83,-0.98,45.12,-0.02,41.45,-0.03,0,False,False
20260522,57.88,0.05,45.17,0.05,41.44,-0.01,1,False,True
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
