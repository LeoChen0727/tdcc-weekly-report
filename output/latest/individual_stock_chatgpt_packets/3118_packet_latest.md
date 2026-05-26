# INDIVIDUAL STOCK CHATGPT PACKET - 3118 進階

## Metadata
- generated_at: 2026-05-26 23:01:07 Asia/Taipei
- stock_id: 3118
- stock_name: 進階
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3118_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3118_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3118_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3118_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3118_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3118_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3118_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3118_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3118_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3118_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3118_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3118_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3118_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3118.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3118.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3118.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3118.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3118.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3118.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3118_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3118_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3118_latest.md?ref=main

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
- open: 33.3
- high: 33.7
- low: 33.1
- close: 33.65
- volume: 33000
- ma5: 33.44
- ema23_primary: 33.54
- distance_to_ema23_pct: 0.33
- ma20: 33.59
- ma60: 33.47
- ma120: 33.26
- return_5d: 0.3
- return_20d: 0
- volume_ratio: 1.45
- distance_to_ma20_pct_auxiliary: 0.17
- distance_to_high_60_pct: -3.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,33.65,33.65,33.5,33.55,26000,33.48,0.22,33.48,33.25,1.03
20260429,33.9,33.9,33.6,33.75,33000,33.5,0.75,33.52,33.27,1.24
20260430,34.7,34.7,33.5,33.6,14000,33.51,0.27,33.54,33.28,0.55
20260504,33.6,33.6,33.5,33.5,19000,33.51,-0.02,33.55,33.29,0.73
20260505,33.4,33.7,33.4,33.7,12000,33.52,0.53,33.56,33.3,0.49
20260506,33.7,33.7,33.55,33.7,15000,33.54,0.48,33.56,33.32,0.61
20260507,33.7,33.8,33.6,33.7,21000,33.55,0.44,33.56,33.33,0.85
20260508,33.8,33.85,33.7,33.8,30000,33.57,0.68,33.58,33.34,1.19
20260511,33.65,33.65,33.55,33.65,27000,33.58,0.21,33.58,33.35,1.06
20260512,33.8,33.8,33.55,33.65,25000,33.59,0.19,33.59,33.37,0.97
20260513,34.5,34.5,33.6,33.65,16000,33.59,0.18,33.6,33.38,0.62
20260514,33.65,33.85,33.5,33.85,22000,33.61,0.71,33.62,33.4,0.86
20260515,33.55,33.65,33.55,33.55,8000,33.61,-0.17,33.62,33.41,0.31
20260518,33.5,33.5,33.35,33.45,14000,33.59,-0.43,33.62,33.42,0.54
20260519,33.35,33.55,33.35,33.55,21000,33.59,-0.12,33.63,33.43,0.82
20260520,33.55,33.8,33.3,33.35,35000,33.57,-0.66,33.62,33.44,1.33
20260521,33.35,33.5,33.35,33.5,19000,33.56,-0.19,33.61,33.45,0.77
20260522,33.4,33.6,33.2,33.4,33000,33.55,-0.45,33.6,33.45,1.47
20260525,33.4,33.4,33.3,33.3,33000,33.53,-0.69,33.59,33.46,1.47
20260526,33.3,33.7,33.1,33.65,33000,33.54,0.33,33.59,33.47,1.45
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 35.2
- over_600_ratio: 29.19
- over_800_ratio: 17.82
- over_1000_ratio: 11.97
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
20260430,35.2,,17.82,,11.97,,0,False,False
20260508,35.2,0,17.82,0,11.97,0,0,False,False
20260515,35.2,0,17.82,0,11.97,0,0,False,False
20260522,35.2,0,17.82,0,11.97,0,0,False,False
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
