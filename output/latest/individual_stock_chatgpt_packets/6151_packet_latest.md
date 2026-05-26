# INDIVIDUAL STOCK CHATGPT PACKET - 6151 晉倫

## Metadata
- generated_at: 2026-05-26 22:19:59 Asia/Taipei
- stock_id: 6151
- stock_name: 晉倫
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6151_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6151_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6151_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6151_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6151_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6151_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6151_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6151_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6151_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6151_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6151_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6151_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6151_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6151.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6151.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6151.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6151.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6151.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6151.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6151_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6151_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6151_latest.md?ref=main

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
- open: 49
- high: 49.15
- low: 46.25
- close: 46.45
- volume: 48000
- ma5: 46.79
- ema23_primary: 41.3
- distance_to_ema23_pct: 12.46
- ma20: 40.65
- ma60: 35.03
- ma120: 32.32
- return_5d: 7.27
- return_20d: 31.03
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 14.28
- distance_to_high_60_pct: -8.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,35.45,35.55,35,35.3,174000,34.32,2.86,34.58,31.66,0.25
20260429,34.95,36.8,34.5,36.4,483000,34.49,5.53,34.86,31.74,0.68
20260430,37,37,35.65,35.65,223000,34.59,3.07,35.12,31.82,0.32
20260504,35.65,36.35,35.45,35.6,298000,34.67,2.67,35.22,31.9,0.45
20260505,35.45,36.35,35.3,35.65,274000,34.76,2.58,35.37,31.98,0.48
20260506,35.7,35.8,34.65,35.65,489000,34.83,2.36,35.52,32.07,0.85
20260507,35.85,36.4,35.4,36.15,228000,34.94,3.46,35.7,32.17,0.41
20260508,36.4,38.6,36.4,37.05,1012000,35.12,5.51,35.79,32.28,1.8
20260511,38.9,40.75,38.15,39,2617000,35.44,10.05,36.07,32.43,4.01
20260512,40.3,42.4,39.8,41.5,2079000,35.94,15.46,36.4,32.63,2.96
20260513,40.6,40.85,39.85,39.9,1138000,36.27,10,36.53,32.8,1.63
20260514,41.85,42.55,41.2,41.3,988000,36.69,12.56,36.8,32.99,1.41
20260515,41.95,42.4,40.85,41.45,1191000,37.09,11.76,37.1,33.19,1.6
20260518,41.7,45.1,41,45.1,1851000,37.76,19.45,37.58,33.46,2.26
20260519,44.6,44.7,42.75,43.3,1422000,38.22,13.3,37.91,33.69,1.67
20260520,43.3,43.8,41.6,42.35,1029000,38.56,9.82,38.19,33.91,1.17
20260521,43.15,46.55,42.75,46.55,2029000,39.23,18.66,38.71,34.17,2.11
20260522,48.5,50.5,47.4,49.8,49000,40.11,24.16,39.42,34.48,0.05
20260525,51,51,48.7,48.8,49000,40.83,19.51,40.1,34.77,0.05
20260526,49,49.15,46.25,46.45,48000,41.3,12.46,40.65,35.03,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 35.07
- over_600_ratio: 30.96
- over_800_ratio: 27.02
- over_1000_ratio: 20.92
- over_400_change_1w: -0.12
- over_800_change_1w: -0.12
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.06,,27.59,,23.08,,0,False,False
20260508,34.3,0.24,27.64,0.05,23.13,0.05,1,True,True
20260515,35.19,0.89,27.14,-0.5,21.01,-2.12,2,False,False
20260522,35.07,-0.12,27.02,-0.12,20.92,-0.09,0,False,False
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
