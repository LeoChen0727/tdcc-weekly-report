# INDIVIDUAL STOCK CHATGPT PACKET - 6266 泰詠

## Metadata
- generated_at: 2026-05-26 23:54:36 Asia/Taipei
- stock_id: 6266
- stock_name: 泰詠
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6266_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6266_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6266_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6266_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6266_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6266_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6266_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6266_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6266_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6266_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6266_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6266_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6266_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6266.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6266.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6266.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6266.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6266.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6266.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6266_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6266_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6266_latest.md?ref=main

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
- open: 27.75
- high: 27.75
- low: 27.3
- close: 27.65
- volume: 27000
- ma5: 27.24
- ema23_primary: 27.38
- distance_to_ema23_pct: 1
- ma20: 27.32
- ma60: 28.06
- ma120: 28.53
- return_5d: 4.93
- return_20d: -0.36
- volume_ratio: 0.11
- distance_to_ma20_pct_auxiliary: 1.21
- distance_to_high_60_pct: -6.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,27.75,27.75,27.5,27.65,221000,28.18,-1.88,28.1,28.67,0.68
20260429,27.8,28.1,27.6,27.85,232000,28.15,-1.07,28.06,28.65,0.7
20260430,27.85,27.85,27.65,27.85,194000,28.13,-0.99,28.03,28.6,0.72
20260504,28.05,28.05,27.6,27.7,403000,28.09,-1.39,28,28.56,1.43
20260505,27.7,27.95,27.6,27.95,287000,28.08,-0.46,27.99,28.53,1.01
20260506,28.05,28.05,27.6,27.85,250000,28.06,-0.75,27.98,28.5,0.87
20260507,27.85,27.9,27.7,27.85,241000,28.04,-0.69,27.96,28.46,0.82
20260508,27.85,28,27.8,27.95,217000,28.04,-0.3,27.96,28.44,0.75
20260511,27.8,27.8,27.5,27.55,402000,27.99,-1.59,27.95,28.41,1.36
20260512,27.55,27.6,27.15,27.25,542000,27.93,-2.44,27.92,28.38,1.76
20260513,27.15,27.15,26.8,26.8,402000,27.84,-3.73,27.86,28.35,1.26
20260514,26.8,27,26.6,26.9,311000,27.76,-3.1,27.81,28.31,0.96
20260515,27,27,26.3,26.4,368000,27.65,-4.51,27.73,28.27,1.12
20260518,26.3,26.45,26,26.3,143000,27.53,-4.48,27.63,28.23,0.45
20260519,26.3,26.45,26.15,26.35,157000,27.44,-3.96,27.55,28.19,0.5
20260520,26.6,27.2,26.6,27,241000,27.4,-1.46,27.5,28.17,0.78
20260521,27,27.15,26.85,27.05,222000,27.37,-1.17,27.42,28.14,0.75
20260522,27.1,27.2,26.8,27.05,27000,27.34,-1.07,27.36,28.11,0.1
20260525,27.25,27.7,27.05,27.45,27000,27.35,0.36,27.32,28.08,0.1
20260526,27.75,27.75,27.3,27.65,27000,27.38,1,27.32,28.06,0.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.71
- over_600_ratio: 36.63
- over_800_ratio: 33.44
- over_1000_ratio: 31.65
- over_400_change_1w: -0.07
- over_800_change_1w: 0.6
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.76,,33.44,,31.67,,0,False,False
20260508,40.07,0.31,33.42,-0.02,31.65,-0.02,1,False,False
20260515,39.78,-0.29,32.84,-0.58,31.65,0,0,False,False
20260522,39.71,-0.07,33.44,0.6,31.65,0,1,False,True
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
