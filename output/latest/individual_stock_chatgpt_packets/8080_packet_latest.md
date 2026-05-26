# INDIVIDUAL STOCK CHATGPT PACKET - 8080 泰霖

## Metadata
- generated_at: 2026-05-26 23:02:49 Asia/Taipei
- stock_id: 8080
- stock_name: 泰霖
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 131
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8080_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8080_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8080_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8080_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8080_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8080_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8080_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8080_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8080_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8080_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8080_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8080_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8080_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8080.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8080.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8080.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8080.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8080.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8080.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8080_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8080_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8080_latest.md?ref=main

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
- open: 27.7
- high: 27.85
- low: 27.7
- close: 27.8
- volume: 28000
- ma5: 27.7
- ema23_primary: 28.21
- distance_to_ema23_pct: -1.46
- ma20: 28.25
- ma60: 29.17
- ma120: 30.54
- return_5d: 1.83
- return_20d: -1.59
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: -1.6
- distance_to_high_60_pct: -15.24

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,28.2,28.35,28.2,28.35,24000,29.04,-2.37,28.87,30.79,0.74
20260429,28.35,28.95,28.35,28.35,23000,28.98,-2.18,28.83,30.59,0.72
20260430,28.35,28.75,28.2,28.3,58000,28.92,-2.16,28.78,30.41,1.71
20260504,28.3,29.65,28.3,29,5000,28.93,0.24,28.79,30.26,0.15
20260505,28.85,29,28.55,28.55,14000,28.9,-1.21,28.77,30.13,0.43
20260506,28.55,29.7,28.5,29.65,47000,28.96,2.38,28.81,30,1.39
20260507,29.35,29.85,28.75,29.55,41000,29.01,1.86,28.84,29.88,1.19
20260508,29.55,29.55,28.1,29.4,50000,29.04,1.23,28.86,29.82,1.37
20260511,29,29,28.4,28.7,73000,29.01,-1.08,28.8,29.78,1.91
20260512,28.55,28.7,28.35,28.35,41000,28.96,-2.1,28.75,29.75,1.07
20260513,29.6,29.6,28.3,28.4,55000,28.91,-1.77,28.72,29.71,1.38
20260514,28.4,28.4,28,28,95000,28.84,-2.9,28.66,29.66,2.2
20260515,28,28,27.3,27.4,141000,28.72,-4.59,28.59,29.61,2.87
20260518,27.4,27.4,26.85,27.25,84000,28.59,-4.7,28.52,29.56,1.61
20260519,27.25,27.6,27.25,27.3,32000,28.49,-4.17,28.45,29.49,0.63
20260520,27.3,27.3,27.25,27.3,11000,28.39,-3.83,28.38,29.45,0.23
20260521,28.55,28.55,27.35,28,24000,28.36,-1.25,28.35,29.4,0.5
20260522,28.85,28.85,27.75,27.75,28000,28.31,-1.96,28.32,29.35,0.6
20260525,27.7,28.4,27.6,27.65,28000,28.25,-2.13,28.27,29.24,0.61
20260526,27.7,27.85,27.7,27.8,28000,28.21,-1.46,28.25,29.17,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.77
- over_600_ratio: 83.48
- over_800_ratio: 82.53
- over_1000_ratio: 82.53
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
20260430,84.77,,82.53,,82.53,,0,False,False
20260508,84.77,0,82.53,0,82.53,0,0,False,False
20260515,84.77,0,82.53,0,82.53,0,0,False,False
20260522,84.77,0,82.53,0,82.53,0,0,False,False
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
