# INDIVIDUAL STOCK CHATGPT PACKET - 6244 茂迪

## Metadata
- generated_at: 2026-05-30 23:42:59 Asia/Taipei
- stock_id: 6244
- stock_name: 茂迪
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6244_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6244_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6244_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6244_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6244_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6244_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6244_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6244_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6244_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6244_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6244_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6244_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6244_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6244.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6244.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6244.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6244.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6244.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6244.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6244_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6244_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6244_latest.md?ref=main

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
- open: 30.65
- high: 30.8
- low: 29.8
- close: 30.05
- volume: 30000
- ma5: 29.97
- ema23_primary: 28.99
- distance_to_ema23_pct: 3.64
- ma20: 29.02
- ma60: 29.03
- ma120: 25.77
- return_5d: 2.21
- return_20d: 9.67
- volume_ratio: 0
- distance_to_ma20_pct_auxiliary: 3.55
- distance_to_high_60_pct: -14.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,27.5,28.25,27,27.7,7003000,27.83,-0.46,27.32,28.44,0.82
20260505,27.7,28.8,27.7,27.9,7928000,27.83,0.24,27.45,28.52,0.92
20260506,28.25,28.75,27.3,27.55,5802000,27.81,-0.94,27.56,28.58,0.67
20260507,27.95,30.3,27.7,30.3,12935000,28.02,8.14,27.75,28.7,1.42
20260508,31,31.25,28.9,29.7,18966000,28.16,5.47,27.96,28.82,1.94
20260511,30.2,30.55,29.2,29.9,8399000,28.3,5.64,28.17,28.93,0.85
20260512,30,30.75,29.4,29.4,6799000,28.39,3.54,28.34,29.05,0.68
20260513,29.4,31.1,28.55,29.4,20783000,28.48,3.24,28.46,29.14,1.94
20260514,29.35,29.65,28.2,28.25,6818000,28.46,-0.74,28.39,29.16,0.68
20260515,28.5,28.8,27.25,27.55,5058000,28.38,-2.94,28.33,29.12,0.54
20260518,27.55,27.9,27,27.85,3052000,28.34,-1.73,28.29,29.14,0.36
20260519,28.1,30.25,27.9,29,9922000,28.39,2.13,28.3,29.21,1.17
20260520,29.15,29.2,27.7,28.3,4686000,28.39,-0.3,28.27,29.27,0.56
20260521,28.6,28.9,28.35,28.35,2883000,28.38,-0.12,28.26,29.32,0.35
20260522,28.7,29.4,28.5,29.4,29000,28.47,3.27,28.33,29.34,0
20260525,29.75,31.2,29.25,30.65,30000,28.65,6.98,28.45,29.34,0
20260526,30.7,32,29.55,29.7,31000,28.74,3.35,28.57,29.29,0
20260527,30.1,30.25,28.9,29.35,30000,28.79,1.95,28.71,29.22,0
20260528,29.4,31.2,29.35,30.1,30000,28.9,4.16,28.89,29.12,0
20260529,30.65,30.8,29.8,30.05,30000,28.99,3.64,29.02,29.03,0
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 35.26
- over_600_ratio: 32.46
- over_800_ratio: 30.97
- over_1000_ratio: 29.86
- over_400_change_1w: 1.49
- over_800_change_1w: 1.38
- over_1000_change_1w: 1.39
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,32.17,,27.8,,27.36,,0,False,False
20260508,34.3,2.13,29.98,2.18,29.32,1.96,1,True,True
20260515,33.39,-0.91,28.77,-1.21,27.86,-1.46,0,False,False
20260522,33.77,0.38,29.59,0.82,28.47,0.61,1,True,True
20260529,35.26,1.49,30.97,1.38,29.86,1.39,2,True,True
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
