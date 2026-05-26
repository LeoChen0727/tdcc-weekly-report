# INDIVIDUAL STOCK CHATGPT PACKET - 3207 耀勝

## Metadata
- generated_at: 2026-05-26 23:01:10 Asia/Taipei
- stock_id: 3207
- stock_name: 耀勝
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3207_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3207_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3207_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3207_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3207_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3207_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3207_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3207_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3207_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3207_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3207_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3207_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3207_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3207.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3207.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3207.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3207.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3207.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3207.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3207_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3207_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3207_latest.md?ref=main

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
- high: 64.7
- low: 61.8
- close: 63
- volume: 63000
- ma5: 59.2
- ema23_primary: 61.27
- distance_to_ema23_pct: 2.83
- ma20: 60.43
- ma60: 66.88
- ma120: 68.72
- return_5d: 4.3
- return_20d: -0.79
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: 4.25
- distance_to_high_60_pct: -29.53

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,62.8,66.6,62,64.6,499000,66.8,-3.3,66.09,69.95,1.47
20260429,64.9,64.9,63.5,63.5,116000,66.53,-4.55,65.97,69.77,0.35
20260430,63.5,64,62.1,62.3,148000,66.17,-5.85,65.83,69.54,0.47
20260504,62.5,62.7,61.1,61.4,302000,65.78,-6.65,65.55,69.32,0.93
20260505,61.6,63.9,59.9,62.6,997000,65.51,-4.44,65.39,69.14,2.72
20260506,62.6,62.6,59.8,60.8,591000,65.12,-6.63,65.13,68.97,1.52
20260507,61,61,60,60.6,228000,64.74,-6.4,64.75,68.79,0.6
20260508,60.6,61.4,59.4,59.5,298000,64.31,-7.47,64.41,68.62,0.76
20260511,59.6,59.7,58,59.2,343000,63.88,-7.33,64.1,68.44,0.87
20260512,59.8,60.3,58.1,58.4,450000,63.42,-7.92,63.75,68.3,1.1
20260513,58.1,58.7,56.5,56.8,298000,62.87,-9.66,63.27,68.11,0.72
20260514,56.9,58.5,56.9,57.3,157000,62.41,-8.18,62.77,67.94,0.39
20260515,57.3,62.9,54.6,62.9,758000,62.45,0.72,62.55,67.87,1.82
20260518,61,62.3,59,62.3,528000,62.44,-0.22,62.39,67.83,1.27
20260519,62.3,62.3,60.1,60.4,195000,62.27,-3,62.16,67.77,0.47
20260520,61.2,61.2,58.1,58.1,182000,61.92,-6.17,61.62,67.67,0.47
20260521,59.1,59.1,57.5,57.6,161000,61.56,-6.43,61.13,67.6,0.44
20260522,57.8,57.8,56.6,56.6,57000,61.15,-7.43,60.67,67.42,0.16
20260525,57,62.2,57,60.7,61000,61.11,-0.67,60.45,67.19,0.18
20260526,62.1,64.7,61.8,63,63000,61.27,2.83,60.43,66.88,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.94
- over_600_ratio: 33.28
- over_800_ratio: 25.85
- over_1000_ratio: 20.35
- over_400_change_1w: -1.12
- over_800_change_1w: 0.3
- over_1000_change_1w: 0.37
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.2,,24.58,,21.75,,0,False,False
20260508,41.24,-0.96,25.67,1.09,21.59,-0.16,1,False,True
20260515,41.06,-0.18,25.55,-0.12,19.98,-1.61,0,False,False
20260522,39.94,-1.12,25.85,0.3,20.35,0.37,1,False,True
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
