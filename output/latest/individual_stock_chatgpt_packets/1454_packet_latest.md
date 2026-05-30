# INDIVIDUAL STOCK CHATGPT PACKET - 1454 台富

## Metadata
- generated_at: 2026-05-30 23:40:58 Asia/Taipei
- stock_id: 1454
- stock_name: 台富
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 271
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1454_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1454_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1454_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1454_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1454_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1454_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1454_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1454_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1454_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1454_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1454_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1454_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1454_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1454.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1454.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1454.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1454.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1454.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1454.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1454_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1454_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1454_latest.md?ref=main

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
- open: 12.7
- high: 12.75
- low: 12.55
- close: 12.55
- volume: 39891
- ma5: 12.57
- ema23_primary: 13.01
- distance_to_ema23_pct: -3.52
- ma20: 13.2
- ma60: 13.07
- ma120: 13.27
- return_5d: -0.4
- return_20d: -11.62
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: -4.94
- distance_to_high_60_pct: -15.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,13.85,14.4,13.65,14.25,163002,13.35,6.73,13.19,13.39,1.22
20260505,13.9,13.95,13.7,13.95,32366,13.4,4.1,13.24,13.41,0.24
20260506,14,14,13.65,13.95,31029,13.45,3.74,13.3,13.43,0.23
20260507,13.9,13.9,13.5,13.65,50901,13.46,1.38,13.35,13.44,0.38
20260508,14.7,14.7,13.75,14.05,67593,13.51,3.98,13.41,13.45,0.51
20260511,13.7,14.1,13.55,13.65,46543,13.52,0.93,13.47,13.44,0.36
20260512,13.5,13.85,13.5,13.7,105912,13.54,1.19,13.52,13.4,0.8
20260513,13.5,13.6,13.3,13.6,66216,13.54,0.42,13.56,13.35,0.49
20260514,13.35,13.35,12.9,12.95,103412,13.49,-4.03,13.56,13.31,0.74
20260515,12.95,13,12.9,12.9,39360,13.44,-4.05,13.54,13.29,0.29
20260518,13.65,13.65,12.8,13.25,69326,13.43,-1.33,13.54,13.27,0.52
20260519,13.7,13.7,13.05,13.15,13997,13.41,-1.9,13.54,13.26,0.11
20260520,13.45,13.45,12.4,12.85,110564,13.36,-3.81,13.52,13.23,0.82
20260521,13.1,13.1,12.7,12.7,42290,13.3,-4.54,13.52,13.2,0.31
20260522,12.85,12.85,12.55,12.6,48493,13.25,-4.87,13.52,13.18,0.36
20260525,12.6,12.75,12.45,12.5,87878,13.18,-5.18,13.45,13.15,0.71
20260526,12.5,12.7,12.45,12.65,62740,13.14,-3.72,13.4,13.13,0.61
20260527,12.55,12.55,12.4,12.5,42410,13.09,-4.48,13.36,13.1,0.44
20260528,12.65,12.7,12.4,12.65,128046,13.05,-3.06,13.29,13.08,1.75
20260529,12.7,12.75,12.55,12.55,39891,13.01,-3.52,13.2,13.07,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.73
- over_600_ratio: 80.51
- over_800_ratio: 78.94
- over_1000_ratio: 77.53
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,81.71,,78.91,,77.5,,0,False,False
20260508,81.69,-0.02,78.93,0.02,77.52,0.02,1,False,True
20260515,81.72,0.03,78.94,0.01,77.53,0.01,2,True,True
20260522,81.72,0,78.94,0,77.53,0,0,False,False
20260529,81.73,0.01,78.94,0,77.53,0,1,False,False
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
