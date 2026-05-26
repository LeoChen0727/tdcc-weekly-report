# INDIVIDUAL STOCK CHATGPT PACKET - 5489 彩富

## Metadata
- generated_at: 2026-05-26 21:26:06 Asia/Taipei
- stock_id: 5489
- stock_name: 彩富
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5489_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5489_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5489_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5489_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5489_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5489_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5489_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5489_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5489_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5489_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5489_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5489_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5489_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5489.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5489.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5489.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5489.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5489.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5489.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5489_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5489_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5489_latest.md?ref=main

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
- open: 39.45
- high: 39.7
- low: 39.4
- close: 39.5
- volume: 40000
- ma5: 39.77
- ema23_primary: 40.15
- distance_to_ema23_pct: -1.63
- ma20: 40.23
- ma60: 40.21
- ma120: 40.5
- return_5d: -0.13
- return_20d: -3.42
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: -1.83
- distance_to_high_60_pct: -6.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,41.1,41.1,40.6,40.85,40000,40.64,0.52,40.62,40.73,0.67
20260429,40.8,40.9,40.55,40.75,42000,40.65,0.25,40.67,40.72,0.68
20260430,40.7,40.9,40.55,40.85,62000,40.67,0.45,40.73,40.72,0.98
20260504,40.15,40.9,40.1,40.8,59000,40.68,0.3,40.8,40.7,0.9
20260505,40.15,40.75,40.15,40.55,73000,40.67,-0.29,40.86,40.66,1.07
20260506,40.55,40.75,40.15,40.55,75000,40.66,-0.26,40.88,40.62,1.08
20260507,40.55,40.65,40.4,40.5,54000,40.64,-0.35,40.85,40.58,0.8
20260508,40.2,40.65,40.2,40.5,43000,40.63,-0.32,40.84,40.54,0.66
20260511,40.5,40.5,40,40.05,66000,40.58,-1.31,40.78,40.49,1.1
20260512,39.9,40.35,39.15,40.15,53000,40.55,-0.98,40.72,40.46,0.89
20260513,39.35,40.4,39.35,40.2,40000,40.52,-0.78,40.69,40.42,0.7
20260514,40.2,40.4,40.2,40.3,19000,40.5,-0.49,40.66,40.39,0.35
20260515,40.3,40.45,40.05,40.05,37000,40.46,-1.02,40.61,40.36,0.69
20260518,39.25,40.4,39.25,40.2,38000,40.44,-0.59,40.57,40.33,0.71
20260519,39.5,40.2,39.3,39.55,66000,40.37,-2.02,40.51,40.31,1.21
20260520,39.6,40,39.35,39.5,75000,40.29,-1.97,40.42,40.29,1.37
20260521,40.15,40.15,40,40,17000,40.27,-0.67,40.38,40.26,0.32
20260522,39.65,40.2,39.5,40.15,40000,40.26,-0.27,40.34,40.25,0.79
20260525,39.8,39.85,39.3,39.7,40000,40.21,-1.28,40.3,40.23,0.8
20260526,39.45,39.7,39.4,39.5,40000,40.15,-1.63,40.23,40.21,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 85.17
- over_600_ratio: 82.66
- over_800_ratio: 82.66
- over_1000_ratio: 82.66
- over_400_change_1w: 0.12
- over_800_change_1w: 0.13
- over_1000_change_1w: 0.13
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.75,,82.23,,82.23,,0,False,False
20260508,84.92,0.17,82.41,0.18,82.41,0.18,1,True,True
20260515,85.05,0.13,82.53,0.12,82.53,0.12,2,True,True
20260522,85.17,0.12,82.66,0.13,82.66,0.13,3,True,True
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
