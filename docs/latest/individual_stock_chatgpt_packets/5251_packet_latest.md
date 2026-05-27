# INDIVIDUAL STOCK CHATGPT PACKET - 5251 天鉞電

## Metadata
- generated_at: 2026-05-27 21:27:36 Asia/Taipei
- stock_id: 5251
- stock_name: 天鉞電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5251_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5251_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5251_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5251_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5251_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5251_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5251_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5251_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5251_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5251_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5251_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5251_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5251_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5251.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5251.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5251.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5251.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5251.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5251.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5251_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5251_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5251_latest.md?ref=main

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
- date: 20260527
- open: 27.7
- high: 27.7
- low: 26.65
- close: 26.8
- volume: 27000
- ma5: 26.99
- ema23_primary: 27.9
- distance_to_ema23_pct: -3.95
- ma20: 27.79
- ma60: 29.5
- ma120: 32.37
- return_5d: -0.56
- return_20d: -8.06
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: -3.56
- distance_to_high_60_pct: -21.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,28.8,29,28.5,28.6,53000,29.9,-4.34,29.56,31.26,0.38
20260430,28.6,28.8,28.4,28.5,76000,29.78,-4.3,29.56,31.16,0.57
20260504,28.5,28.65,28.2,28.35,112000,29.66,-4.42,29.54,31.04,0.83
20260505,28.6,29.3,28.6,29.05,95000,29.61,-1.89,29.56,30.94,0.72
20260506,29.05,29.2,28.5,28.6,100000,29.53,-3.14,29.58,30.84,0.76
20260507,28.6,29.3,28.6,29.1,145000,29.49,-1.32,29.6,30.75,1.08
20260508,29.3,29.3,28.4,28.75,121000,29.43,-2.31,29.56,30.66,0.93
20260511,28.25,28.8,26.35,28.5,350000,29.35,-2.9,29.49,30.58,2.48
20260512,28.75,28.75,28.2,28.2,87000,29.26,-3.61,29.41,30.51,0.62
20260513,27.8,28.1,27.6,27.7,85000,29.13,-4.9,29.31,30.41,0.61
20260514,27.75,27.75,27.5,27.65,55000,29,-4.66,29.18,30.32,0.4
20260515,27.65,27.7,26.85,27,125000,28.84,-6.37,29.03,30.22,0.91
20260518,27,27.45,27,27.4,33000,28.72,-4.58,28.88,30.13,0.25
20260519,27.4,27.45,26.5,26.5,97000,28.53,-7.12,28.68,30.03,0.73
20260520,26.8,27.15,26.6,26.95,87000,28.4,-5.1,28.52,29.95,0.71
20260521,26.95,27.45,26.95,26.95,67000,28.28,-4.7,28.27,29.87,0.58
20260522,26.85,27.4,26.8,27.1,27000,28.18,-3.83,28.13,29.78,0.26
20260525,27.1,27.1,26.3,26.6,27000,28.05,-5.17,27.98,29.68,0.28
20260526,27,27.5,26.6,27.5,27000,28,-1.8,27.91,29.59,0.29
20260527,27.7,27.7,26.65,26.8,27000,27.9,-3.95,27.79,29.5,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 35.2
- over_600_ratio: 33.43
- over_800_ratio: 29.21
- over_1000_ratio: 29.21
- over_400_change_1w: -0.02
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,35.25,,29.21,,29.21,,0,False,False
20260508,35.19,-0.06,29.21,0,29.21,0,0,False,False
20260515,35.22,0.03,29.21,0,29.21,0,1,False,False
20260522,35.2,-0.02,29.21,0,29.21,0,0,False,False
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
