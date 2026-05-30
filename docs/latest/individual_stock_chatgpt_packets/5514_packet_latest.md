# INDIVIDUAL STOCK CHATGPT PACKET - 5514 三豐

## Metadata
- generated_at: 2026-05-30 23:42:43 Asia/Taipei
- stock_id: 5514
- stock_name: 三豐
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 247
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5514_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5514_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5514_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5514_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5514_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5514_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5514_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5514_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5514_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5514_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5514_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5514_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5514_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5514.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5514.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5514.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5514.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5514.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5514.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5514_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5514_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5514_latest.md?ref=main

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
- open: 14.05
- high: 14.05
- low: 13.7
- close: 13.9
- volume: 14000
- ma5: 14.65
- ema23_primary: 15.22
- distance_to_ema23_pct: -8.68
- ma20: 15.28
- ma60: 15.7
- ma120: 15.91
- return_5d: -8.85
- return_20d: -10.03
- volume_ratio: 1.78
- distance_to_ma20_pct_auxiliary: -9
- distance_to_high_60_pct: -17.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,15.5,15.5,15.45,15.5,5000,15.88,-2.42,15.92,15.92,0.41
20260428,15,15.5,15,15.5,22000,15.85,-2.23,15.89,15.9,1.82
20260429,15.5,15.5,15.5,15.5,1000,15.82,-2.04,15.86,15.89,0.08
20260430,15.6,15.7,15.5,15.7,14000,15.81,-0.72,15.85,15.88,1.15
20260504,15.85,15.9,15.85,15.9,3000,15.82,0.5,15.85,15.87,0.24
20260505,15.85,15.85,15.85,15.85,1000,15.82,0.17,15.86,15.88,0.08
20260506,15.95,15.95,15.5,15.5,3000,15.8,-1.87,15.82,15.87,0.25
20260507,15.5,15.6,15.4,15.6,8000,15.78,-1.14,15.81,15.87,0.7
20260508,15.55,15.55,15.55,15.55,1000,15.76,-1.34,15.79,15.86,0.09
20260511,15.4,15.5,15.2,15.2,11000,15.71,-3.27,15.77,15.85,1.05
20260512,15.3,15.35,15.3,15.35,7000,15.68,-2.13,15.73,15.85,0.84
20260514,15.3,15.3,15.25,15.3,3000,15.65,-2.25,15.7,15.84,0.35
20260515,15.3,15.3,15.3,15.3,1000,15.62,-2.06,15.66,15.83,0.12
20260519,15.25,15.25,15.25,15.25,1000,15.59,-2.19,15.6,15.81,0.13
20260520,15.25,15.25,15.25,15.25,1000,15.56,-2.01,15.56,15.8,0.14
20260522,15.2,16.1,14.7,15.2,16000,15.53,-2.14,15.53,15.79,2.08
20260526,14.8,15.7,14.8,15,15000,15.49,-3.15,15.48,15.78,1.86
20260527,15,15.5,14.6,14.7,15000,15.42,-4.68,15.42,15.76,1.78
20260528,14.55,15.2,14.2,14.45,15000,15.34,-5.81,15.35,15.73,1.88
20260529,14.05,14.05,13.7,13.9,14000,15.22,-8.68,15.28,15.7,1.78
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 92.46
- over_600_ratio: 90.39
- over_800_ratio: 88.66
- over_1000_ratio: 87.52
- over_400_change_1w: 0.02
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,92.39,,88.65,,87.51,,0,False,False
20260508,92.39,0,88.65,0,87.51,0,0,False,False
20260515,92.44,0.05,88.65,0,87.51,0,1,False,False
20260522,92.44,0,88.65,0,87.51,0,0,False,False
20260529,92.46,0.02,88.66,0.01,87.52,0.01,1,True,True
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
