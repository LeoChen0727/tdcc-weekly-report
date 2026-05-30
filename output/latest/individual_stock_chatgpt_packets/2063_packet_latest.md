# INDIVIDUAL STOCK CHATGPT PACKET - 2063 世鎧

## Metadata
- generated_at: 2026-05-30 23:41:15 Asia/Taipei
- stock_id: 2063
- stock_name: 世鎧
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 272
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2063_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2063_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2063_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2063_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2063_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2063_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2063_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2063_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2063_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2063_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2063_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2063_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2063_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2063.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2063.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2063.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2063.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2063.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2063.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2063_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2063_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2063_latest.md?ref=main

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
- open: 24.9
- high: 25.55
- low: 24.8
- close: 25.2
- volume: 25000
- ma5: 25.18
- ema23_primary: 25.51
- distance_to_ema23_pct: -1.21
- ma20: 25.36
- ma60: 26.35
- ma120: 26.12
- return_5d: -0.4
- return_20d: -2.7
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: -0.63
- distance_to_high_60_pct: -8.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,25.9,25.9,25.4,25.8,14000,26.5,-2.66,26.7,26.88,0.58
20260505,25.7,25.7,25.25,25.6,45000,26.43,-3.14,26.6,26.84,1.72
20260506,25.5,25.6,25,25.35,43000,26.34,-3.76,26.5,26.79,1.58
20260507,25.35,25.35,25.05,25.3,32000,26.25,-3.63,26.4,26.75,1.16
20260508,25.1,25.55,25,25.55,25000,26.19,-2.46,26.33,26.72,0.88
20260511,25.5,26.15,25.5,26.15,76000,26.19,-0.16,26.27,26.7,2.38
20260512,25.85,26.05,25.5,25.5,12000,26.13,-2.42,26.19,26.68,0.37
20260513,25.5,25.5,24.95,25,132000,26.04,-3.99,26.08,26.65,3.61
20260514,25.05,25.5,25.05,25.5,13000,25.99,-1.9,26,26.64,0.36
20260515,25.35,25.35,24.9,25.15,19000,25.92,-2.98,25.89,26.62,0.53
20260518,25.15,25.6,25.15,25.6,16000,25.9,-1.15,25.8,26.61,0.46
20260519,25.3,25.3,25.3,25.3,2000,25.85,-2.12,25.73,26.59,0.06
20260520,25.3,25.3,24.8,25.1,13000,25.78,-2.66,25.64,26.56,0.41
20260521,25.3,25.3,25,25.1,9000,25.73,-2.44,25.57,26.53,0.3
20260522,25.1,25.3,25,25.3,25000,25.69,-1.53,25.52,26.5,0.82
20260525,25.3,25.3,25,25.15,25000,25.65,-1.94,25.49,26.47,0.85
20260526,25.15,25.4,25.15,25.4,25000,25.63,-0.88,25.48,26.45,0.87
20260527,25.2,25.25,25.2,25.25,25000,25.59,-1.35,25.45,26.41,0.86
20260528,25.05,25.05,24.65,24.9,25000,25.54,-2.49,25.39,26.37,0.85
20260529,24.9,25.55,24.8,25.2,25000,25.51,-1.21,25.36,26.35,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 54.01
- over_600_ratio: 47.75
- over_800_ratio: 41.52
- over_1000_ratio: 39.73
- over_400_change_1w: 0.05
- over_800_change_1w: 0.05
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.54,,41.22,,39.43,,0,False,False
20260508,54.56,0.02,41.24,0.02,39.45,0.02,1,True,True
20260515,54.79,0.23,41.47,0.23,39.68,0.23,2,True,True
20260522,53.96,-0.83,41.47,0,39.68,0,0,False,False
20260529,54.01,0.05,41.52,0.05,39.73,0.05,1,True,True
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
