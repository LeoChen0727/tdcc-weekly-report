# INDIVIDUAL STOCK CHATGPT PACKET - 5878 台名

## Metadata
- generated_at: 2026-05-26 23:54:25 Asia/Taipei
- stock_id: 5878
- stock_name: 台名
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 120
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5878_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5878_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5878_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5878_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5878_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5878_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5878_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5878_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5878_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5878_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5878_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5878_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5878_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5878.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5878.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5878.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5878.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5878.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5878.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5878_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5878_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5878_latest.md?ref=main

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
- open: 41.35
- high: 41.5
- low: 40.65
- close: 40.85
- volume: 41000
- ma5: 40.76
- ema23_primary: 40.81
- distance_to_ema23_pct: 0.09
- ma20: 40.75
- ma60: 41.16
- ma120: 41.23
- return_5d: 0.74
- return_20d: -0.61
- volume_ratio: 3.35
- distance_to_ma20_pct_auxiliary: 0.25
- distance_to_high_60_pct: -3.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,40.95,41,40.95,41,2000,41.16,-0.4,41.13,41.41,0.22
20260428,40.9,40.9,40.9,40.9,2000,41.14,-0.59,41.1,41.41,0.23
20260429,40.9,40.9,40.8,40.85,5000,41.12,-0.65,41.08,41.41,0.57
20260430,40.8,40.8,40.75,40.8,9000,41.09,-0.71,41.05,41.4,1
20260504,40.8,40.8,40.7,40.75,7000,41.06,-0.76,41.01,41.39,0.8
20260505,41,41.1,40.75,40.8,10000,41.04,-0.59,40.98,41.37,1.12
20260506,40.75,40.75,40.55,40.6,15000,41,-0.99,40.95,41.35,1.58
20260507,41.4,41.4,41,41,2000,41,-0.01,40.95,41.34,0.22
20260508,40.65,41,40.65,40.7,8000,40.98,-0.68,40.94,41.33,0.87
20260511,40.7,40.7,40.65,40.65,15000,40.95,-0.74,40.92,41.31,1.58
20260512,40.7,40.7,40.7,40.7,11000,40.93,-0.56,40.91,41.3,1.22
20260514,40.55,40.6,40.55,40.55,10000,40.9,-0.85,40.88,41.28,1.15
20260515,40.6,40.6,40.6,40.6,1000,40.87,-0.67,40.85,41.26,0.12
20260518,40.6,40.95,40.6,40.7,4000,40.86,-0.39,40.83,41.25,0.51
20260519,40.5,40.55,40.5,40.55,4000,40.83,-0.69,40.8,41.23,0.52
20260520,40.55,40.55,40.5,40.5,9000,40.81,-0.75,40.78,41.21,1.17
20260521,40.5,41,40.5,40.65,8000,40.79,-0.35,40.77,41.2,1.1
20260522,40.65,41,40.65,41,41000,40.81,0.47,40.77,41.19,4.69
20260525,41,41.3,40.8,40.8,41000,40.81,-0.02,40.76,41.17,3.83
20260526,41.35,41.5,40.65,40.85,41000,40.81,0.09,40.75,41.16,3.35
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.41
- over_600_ratio: 66.52
- over_800_ratio: 64.12
- over_1000_ratio: 64.12
- over_400_change_1w: -0.11
- over_800_change_1w: -0.11
- over_1000_change_1w: -0.11
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.56,,64.27,,64.27,,0,False,False
20260508,72.56,0,64.27,0,64.27,0,0,False,False
20260515,72.52,-0.04,64.23,-0.04,64.23,-0.04,0,False,False
20260522,72.41,-0.11,64.12,-0.11,64.12,-0.11,0,False,False
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
