# INDIVIDUAL STOCK CHATGPT PACKET - 5013 強新

## Metadata
- generated_at: 2026-05-30 23:42:34 Asia/Taipei
- stock_id: 5013
- stock_name: 強新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 255
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5013_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5013_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5013_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5013_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5013_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5013_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5013_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5013_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5013_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5013_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5013_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5013_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5013_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5013.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5013.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5013.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5013.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5013.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5013.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5013_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5013_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5013_latest.md?ref=main

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
- open: 28
- high: 28
- low: 27.55
- close: 27.85
- volume: 28000
- ma5: 28.19
- ema23_primary: 28.11
- distance_to_ema23_pct: -0.93
- ma20: 27.84
- ma60: 29.1
- ma120: 29.16
- return_5d: 2.39
- return_20d: -4.3
- volume_ratio: 1.47
- distance_to_ma20_pct_auxiliary: 0.05
- distance_to_high_60_pct: -11.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,29.15,29.15,28.75,28.8,76000,29.58,-2.65,29.69,29.96,5.03
20260504,28.55,28.8,28.3,28.3,5000,29.48,-3.99,29.61,29.94,0.33
20260505,28.3,29.15,28.3,28.75,22000,29.42,-2.27,29.55,29.91,1.35
20260506,28.7,28.75,27.9,27.9,23000,29.29,-4.75,29.48,29.87,1.36
20260507,27.8,28.5,27.8,28.1,24000,29.19,-3.74,29.39,29.82,1.36
20260508,27.85,28.25,27.7,28.25,14000,29.11,-2.96,29.34,29.78,0.77
20260511,29,29,28.25,28.45,17000,29.06,-2.09,29.3,29.74,0.89
20260512,28.15,28.2,27.8,27.85,13000,28.96,-3.82,29.23,29.7,0.7
20260513,27.3,27.35,27.3,27.35,7000,28.82,-5.11,29.12,29.65,0.38
20260514,27.35,27.7,27.3,27.5,11000,28.71,-4.22,28.92,29.59,0.62
20260515,27.3,27.5,27.25,27.25,6000,28.59,-4.69,28.75,29.53,0.37
20260518,27,27,26.9,26.9,2000,28.45,-5.45,28.54,29.48,0.14
20260519,26.9,26.9,26.5,26.55,11000,28.29,-6.16,28.34,29.4,0.77
20260520,26.55,26.6,26.55,26.6,4000,28.15,-5.51,28.17,29.31,0.28
20260521,27.2,27.2,27.2,27.2,6000,28.07,-3.1,28.08,29.24,0.41
20260522,27.25,27.5,27.15,27.2,27000,28,-2.85,27.99,29.19,1.73
20260525,27.3,29.45,27.3,29.45,28000,28.12,4.73,27.99,29.18,1.69
20260526,29.45,29.45,28.45,28.45,29000,28.15,1.08,27.96,29.16,1.64
20260528,27.5,28.4,27.5,28,28000,28.14,-0.48,27.9,29.13,1.5
20260529,28,28,27.55,27.85,28000,28.11,-0.93,27.84,29.1,1.47
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 86.96
- over_600_ratio: 84.58
- over_800_ratio: 82.5
- over_1000_ratio: 80.49
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
20260430,86.9,,82.08,,80.07,,0,False,False
20260508,86.96,0.06,82.08,0,80.07,0,1,False,False
20260515,86.96,0,82.08,0,80.07,0,0,False,False
20260522,86.96,0,82.5,0.42,80.49,0.42,1,False,True
20260529,86.96,0,82.5,0,80.49,0,0,False,False
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
