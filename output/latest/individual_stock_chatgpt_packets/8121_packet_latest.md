# INDIVIDUAL STOCK CHATGPT PACKET - 8121 越峰

## Metadata
- generated_at: 2026-05-28 19:33:47 Asia/Taipei
- stock_id: 8121
- stock_name: 越峰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8121_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8121_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8121_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8121_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8121_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8121_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8121_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8121_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8121_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8121_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8121_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8121_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8121_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8121.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8121.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8121.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8121.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8121.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8121.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8121_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8121_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8121_latest.md?ref=main

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
- open: 41.2
- high: 42.3
- low: 39.7
- close: 40
- volume: 2736853
- ma5: 41.11
- ema23_primary: 35
- distance_to_ema23_pct: 14.28
- ma20: 35.11
- ma60: 28.63
- ma120: 28.53
- return_5d: 7.09
- return_20d: 45.72
- volume_ratio: 1.19
- distance_to_ma20_pct_auxiliary: 13.94
- distance_to_high_60_pct: -8.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,27.8,29.4,27.45,28.5,943000,26.51,7.52,26.07,26.29,1.27
20260504,28.7,31.35,28.4,31.35,2784000,26.91,16.49,26.45,26.29,3.18
20260505,31.35,34.4,31.35,32.95,5200000,27.41,20.19,26.93,26.3,4.6
20260506,32.95,33.15,29.8,30.75,3126000,27.69,11.04,27.32,26.3,2.45
20260507,30.35,33.75,30.3,32.85,2575000,28.12,16.81,27.78,26.36,1.85
20260508,32.15,32.7,30.5,30.8,1566000,28.35,8.66,28.14,26.39,1.07
20260511,32.5,33.85,30.5,33.85,3454000,28.8,17.52,28.64,26.49,2.14
20260512,35,35.4,32.6,34,3628000,29.24,16.29,29.09,26.62,2.04
20260513,33.15,35.2,32,33.8,1952000,29.62,14.12,29.52,26.73,1.05
20260514,33.2,36.7,33.2,35.6,3597000,30.12,18.21,30.05,26.87,1.78
20260515,36,37,33.6,34,3262000,30.44,11.7,30.37,26.98,1.55
20260518,33,33.8,32,33.6,1158000,30.7,9.44,30.58,27.1,0.58
20260519,33.6,33.65,32,32,1021000,30.81,3.86,30.76,27.19,0.52
20260520,32.5,35.2,31.65,35.2,3708000,31.18,12.9,31.11,27.33,1.77
20260521,36.5,38.7,36,37.35,4956000,31.69,17.86,31.55,27.51,2.17
20260522,37.55,41,37.55,39.55,39000,32.35,22.27,32.2,27.71,0.02
20260525,40.3,43.5,37.6,43.5,41000,33.28,30.73,33.06,27.98,0.02
20260526,43.5,43.5,39.2,41.5,41000,33.96,22.2,33.78,28.21,0.02
20260527,40.8,43.2,40.2,41,41000,34.55,18.68,34.48,28.42,0.02
20260528,41.2,42.3,39.7,40,2736853,35,14.28,35.11,28.63,1.19
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.91
- over_600_ratio: 58.21
- over_800_ratio: 55.81
- over_1000_ratio: 54.22
- over_400_change_1w: 0.04
- over_800_change_1w: 0.36
- over_1000_change_1w: 1.14
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.37,,55.03,,53.05,,0,False,False
20260508,59.64,0.27,55.03,0,53.05,0,1,False,False
20260515,60.87,1.23,55.45,0.42,53.08,0.03,2,True,True
20260522,60.91,0.04,55.81,0.36,54.22,1.14,3,True,True
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
