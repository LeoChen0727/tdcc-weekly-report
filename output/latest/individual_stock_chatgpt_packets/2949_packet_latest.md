# INDIVIDUAL STOCK CHATGPT PACKET - 2949 欣新網

## Metadata
- generated_at: 2026-05-26 21:25:17 Asia/Taipei
- stock_id: 2949
- stock_name: 欣新網
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 104
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2949_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2949_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2949_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2949_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2949_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2949_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2949_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2949_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2949_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2949_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2949_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2949_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2949_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2949.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2949.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2949.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2949.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2949.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2949.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2949_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2949_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2949_latest.md?ref=main

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
- open: 62.1
- high: 62.9
- low: 62
- close: 62.9
- volume: 62000
- ma5: 61.66
- ema23_primary: 58.92
- distance_to_ema23_pct: 6.76
- ma20: 57.25
- ma60: 60.02
- ma120: 63.39
- return_5d: 5.18
- return_20d: 7.34
- volume_ratio: 2.89
- distance_to_ma20_pct_auxiliary: 9.87
- distance_to_high_60_pct: -5.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,57,57,56,56,3000,59.26,-5.51,58.85,62.85,0.63
20260428,55.6,55.6,55,55.6,18000,58.96,-5.7,58.53,62.63,3.24
20260429,54,54.5,54,54.4,3000,58.58,-7.13,58.2,62.4,0.55
20260430,54.4,55.2,54.4,55.2,3000,58.3,-5.31,57.96,62.19,0.54
20260504,54.7,54.7,54,54,6000,57.94,-6.8,57.78,61.97,1.03
20260505,52.7,53.5,52.5,53.5,7000,57.57,-7.07,57.45,61.77,1.47
20260506,52.3,54,51.8,54,30000,57.27,-5.71,57.18,61.55,4.88
20260508,55.6,55.6,51.2,52.4,24000,56.87,-7.85,56.78,61.3,3.31
20260511,52.8,54.4,52.8,53.5,13000,56.59,-5.45,56.47,61.09,1.69
20260512,54.8,54.8,53,53.3,12000,56.31,-5.35,56.22,60.9,1.46
20260513,53.3,53.3,53.2,53.2,2000,56.05,-5.09,55.92,60.7,0.25
20260514,53.5,58.5,53.5,58.5,24000,56.26,3.99,55.92,60.57,2.64
20260515,58.5,63,58.5,61.2,40000,56.67,8,56.09,60.48,3.83
20260518,62.9,62.9,58.8,62.1,14000,57.12,8.72,56.27,60.41,1.27
20260519,59.5,62.5,58.4,59.8,26000,57.34,4.28,56.39,60.32,2.13
20260520,60.8,60.8,58.7,60.1,10000,57.57,4.39,56.48,60.25,0.8
20260521,59,60.5,58.9,60.5,9000,57.82,4.64,56.61,60.14,0.7
20260522,60,61.9,60,61.9,61000,58.16,6.43,56.77,60.09,3.94
20260525,61.9,62.9,61.9,62.9,62000,58.55,7.42,57.03,60.06,3.36
20260526,62.1,62.9,62,62.9,62000,58.92,6.76,57.25,60.02,2.89
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.74
- over_600_ratio: 76.66
- over_800_ratio: 76.66
- over_1000_ratio: 62.1
- over_400_change_1w: 0.04
- over_800_change_1w: 0.04
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,81.7,,76.62,,62.1,,0,False,False
20260508,81.7,0,76.62,0,62.1,0,0,False,False
20260515,81.7,0,76.62,0,62.1,0,0,False,False
20260522,81.74,0.04,76.66,0.04,62.1,0,1,False,True
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
