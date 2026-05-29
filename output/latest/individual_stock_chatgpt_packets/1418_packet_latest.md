# INDIVIDUAL STOCK CHATGPT PACKET - 1418 東華

## Metadata
- generated_at: 2026-05-29 19:31:38 Asia/Taipei
- stock_id: 1418
- stock_name: 東華
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1418_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1418_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1418_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1418_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1418_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1418_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1418_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1418_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1418_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1418_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1418_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1418_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1418_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1418.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1418.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1418.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1418.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1418.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1418.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1418_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1418_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1418_latest.md?ref=main

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
- open: 18.1
- high: 18.55
- low: 18.1
- close: 18.5
- volume: 51696
- ma5: 18.03
- ema23_primary: 18.29
- distance_to_ema23_pct: 1.15
- ma20: 18.39
- ma60: 18.62
- ma120: 19.23
- return_5d: 4.23
- return_20d: -3.65
- volume_ratio: 1.41
- distance_to_ma20_pct_auxiliary: 0.61
- distance_to_high_60_pct: -9.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,19.2,19.45,19.15,19.35,55316,18.69,3.52,18.64,19.08,2.5
20260505,19.65,19.65,19.1,19.2,50681,18.73,2.48,18.66,19.06,2.08
20260506,19.1,19.6,19.1,19.1,46238,18.76,1.79,18.66,19.05,1.79
20260507,19.7,19.7,18.65,18.9,25902,18.78,0.66,18.66,19.03,1.02
20260508,18.75,19.3,18.75,19.1,5327,18.8,1.58,18.67,19.01,0.21
20260511,19.45,19.45,18.7,18.8,14189,18.8,-0.02,18.67,19,0.56
20260512,18.6,18.7,18.1,18.4,25732,18.77,-1.97,18.66,18.98,1
20260513,18.4,18.55,18.4,18.4,4433,18.74,-1.81,18.64,18.95,0.18
20260514,18.7,18.7,18.2,18.35,22233,18.71,-1.9,18.64,18.93,0.88
20260515,18.55,18.55,18.15,18.3,34480,18.67,-1.99,18.62,18.9,1.31
20260518,18.1,18.25,18.05,18.15,29022,18.63,-2.57,18.59,18.87,1.06
20260519,18.05,18.05,18,18,13657,18.58,-3.1,18.57,18.84,0.52
20260520,17.85,18.05,17.8,17.9,6033,18.52,-3.35,18.55,18.81,0.23
20260521,17.9,17.9,17.65,17.9,25140,18.47,-3.08,18.53,18.78,0.95
20260522,18,18,17.7,17.75,31476,18.41,-3.58,18.51,18.75,1.18
20260525,17.9,18.15,17.5,17.75,37834,18.35,-3.29,18.49,18.72,1.35
20260526,17.5,17.7,16.95,17.1,59650,18.25,-6.3,18.43,18.68,1.95
20260527,17.35,18.8,17.3,18.8,139636,18.3,2.76,18.48,18.66,3.75
20260528,19,19,18,18,56567,18.27,-1.48,18.42,18.64,1.51
20260529,18.1,18.55,18.1,18.5,51696,18.29,1.15,18.39,18.62,1.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.35
- over_600_ratio: 64.22
- over_800_ratio: 62.08
- over_1000_ratio: 58.93
- over_400_change_1w: 0.04
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.31,,62.06,,58.92,,0,False,False
20260508,71.31,0,62.07,0.01,58.92,0,1,False,True
20260515,71.31,0,62.07,0,58.92,0,0,False,False
20260522,71.35,0.04,62.08,0.01,58.93,0.01,1,True,True
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
