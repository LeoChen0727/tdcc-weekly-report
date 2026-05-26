# INDIVIDUAL STOCK CHATGPT PACKET - 6961 旅天下

## Metadata
- generated_at: 2026-05-26 21:26:43 Asia/Taipei
- stock_id: 6961
- stock_name: 旅天下
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 78
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6961_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6961_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6961_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6961_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6961_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6961_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6961_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6961_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6961_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6961_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6961_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6961_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6961_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6961.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6961.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6961.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6961.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6961.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6961.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6961_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6961_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6961_latest.md?ref=main

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
- open: 58.5
- high: 58.5
- low: 58.3
- close: 58.5
- volume: 58000
- ma5: 58.42
- ema23_primary: 58.59
- distance_to_ema23_pct: -0.15
- ma20: 58.86
- ma60: 58.15
- ma120: 58.24
- return_5d: 0
- return_20d: 1.04
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: -0.61
- distance_to_high_60_pct: -4.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,58.1,58.1,57.4,58,46000,57.73,0.47,57.4,58.03,0.89
20260429,57.6,58.1,57.6,58,26000,57.75,0.43,57.4,58.03,0.51
20260430,58.2,58.8,58.2,58.3,71000,57.8,0.87,57.48,57.97,1.43
20260504,58.1,58.4,57.6,58.3,60000,57.84,0.8,57.55,57.93,1.2
20260505,58.6,58.7,58.1,58.7,30000,57.91,1.36,57.67,57.91,0.6
20260506,58,58.9,58,58.9,51000,57.99,1.57,57.8,57.88,1.01
20260507,60.2,60.9,59.8,60.5,230000,58.2,3.95,57.96,57.89,3.92
20260508,61.4,61.4,60.5,60.9,144000,58.43,4.23,58.15,57.93,2.23
20260511,60.9,61.3,59.3,60,114000,58.56,2.46,58.3,57.97,1.65
20260512,60.4,60.5,59.5,59.6,55000,58.64,1.63,58.34,58.01,0.84
20260513,60,60,58.5,59,23000,58.67,0.56,58.43,58.05,0.36
20260514,59.1,59.3,58.7,59,21000,58.7,0.51,58.49,58.08,0.33
20260515,59,59.1,58.6,58.8,34000,58.71,0.15,58.56,58.07,0.54
20260518,58.5,58.7,58.5,58.6,11000,58.7,-0.17,58.62,58.06,0.18
20260519,58.6,58.6,58.4,58.5,26000,58.68,-0.31,58.67,58.06,0.42
20260520,58.5,58.9,58.1,58.5,32000,58.67,-0.29,58.74,58.07,0.54
20260521,58.5,58.8,58.1,58.5,31000,58.65,-0.26,58.8,58.09,0.53
20260522,58.4,58.5,58.3,58.4,58000,58.63,-0.4,58.82,58.1,1.01
20260525,58.8,58.8,58.2,58.2,58000,58.6,-0.68,58.83,58.12,1
20260526,58.5,58.5,58.3,58.5,58000,58.59,-0.15,58.86,58.15,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.77
- over_600_ratio: 38.85
- over_800_ratio: 33.34
- over_1000_ratio: 33.34
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
20260430,44.33,,33.34,,33.34,,0,False,False
20260508,42.77,-1.56,33.34,0,33.34,0,0,False,False
20260515,42.77,0,33.34,0,33.34,0,0,False,False
20260522,42.77,0,33.34,0,33.34,0,0,False,False
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
