# INDIVIDUAL STOCK CHATGPT PACKET - 5015 華祺

## Metadata
- generated_at: 2026-05-26 22:19:41 Asia/Taipei
- stock_id: 5015
- stock_name: 華祺
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5015_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5015_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5015_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5015_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5015_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5015_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5015_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5015_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5015_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5015_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5015_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5015_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5015_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5015.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5015.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5015.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5015.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5015.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5015.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5015_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5015_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5015_latest.md?ref=main

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
- open: 26.6
- high: 26.6
- low: 24.75
- close: 24.75
- volume: 26000
- ma5: 22.99
- ema23_primary: 23.2
- distance_to_ema23_pct: 6.66
- ma20: 22.88
- ma60: 24.88
- ma120: 26.54
- return_5d: 11.24
- return_20d: 3.56
- volume_ratio: 0.61
- distance_to_ma20_pct_auxiliary: 8.17
- distance_to_high_60_pct: -12.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,23.3,23.85,23.3,23.85,19000,24.88,-4.15,24.84,26.76,0.43
20260429,23.6,23.8,23.55,23.8,26000,24.79,-4.01,24.74,26.69,0.57
20260430,23.7,23.8,23.6,23.7,19000,24.7,-4.06,24.65,26.61,0.42
20260504,23.5,23.6,23.5,23.6,22000,24.61,-4.11,24.54,26.54,0.48
20260505,23.55,23.55,23.15,23.5,44000,24.52,-4.15,24.43,26.44,0.96
20260506,23.5,23.5,23.2,23.4,45000,24.42,-4.2,24.34,26.35,0.94
20260507,23.4,23.4,23,23,100000,24.31,-5.37,24.2,26.26,1.92
20260508,22.95,23,22.85,22.95,46000,24.19,-5.14,24.05,26.14,0.88
20260511,22.9,22.9,22.4,22.5,109000,24.05,-6.45,23.91,26.02,1.91
20260512,22.4,22.4,22,22,124000,23.88,-7.88,23.75,25.9,1.98
20260513,22,22,21.65,21.85,37000,23.71,-7.85,23.57,25.78,0.59
20260514,21.85,22.25,21.85,22,60000,23.57,-6.66,23.42,25.66,0.94
20260515,22.25,22.25,22.05,22.2,26000,23.45,-5.35,23.3,25.55,0.44
20260518,22.2,22.2,21.9,22.05,28000,23.34,-5.52,23.18,25.43,0.49
20260519,23,23.1,21.95,22.25,27000,23.25,-4.29,23.08,25.32,0.48
20260520,22.05,22.1,22,22,14000,23.14,-4.94,22.98,25.21,0.29
20260521,22,22.1,21.85,22,42000,23.05,-4.55,22.9,25.11,0.89
20260522,22,22.05,21.9,22,22000,22.96,-4.18,22.83,25,0.49
20260525,22.05,24.2,22.05,24.2,23000,23.06,4.93,22.84,24.93,0.53
20260526,26.6,26.6,24.75,24.75,26000,23.2,6.66,22.88,24.88,0.61
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.89
- over_600_ratio: 47.02
- over_800_ratio: 43.76
- over_1000_ratio: 42.13
- over_400_change_1w: 1.36
- over_800_change_1w: -0.14
- over_1000_change_1w: -1.77
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.32,,43.72,,43.72,,0,False,False
20260508,50.39,0.07,43.79,0.07,43.79,0.07,1,True,True
20260515,50.53,0.14,43.9,0.11,43.9,0.11,2,True,True
20260522,51.89,1.36,43.76,-0.14,42.13,-1.77,3,False,False
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
