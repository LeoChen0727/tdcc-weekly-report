# INDIVIDUAL STOCK CHATGPT PACKET - 6261 久元

## Metadata
- generated_at: 2026-05-26 23:02:14 Asia/Taipei
- stock_id: 6261
- stock_name: 久元
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6261_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6261_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6261_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6261_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6261_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6261_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6261_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6261_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6261_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6261_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6261_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6261_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6261_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6261.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6261.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6261.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6261.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6261.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6261.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6261_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6261_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6261_latest.md?ref=main

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
- open: 122
- high: 124.5
- low: 115.5
- close: 123
- volume: 121000
- ma5: 119.1
- ema23_primary: 110.94
- distance_to_ema23_pct: 10.87
- ma20: 114.47
- ma60: 88.73
- ma120: 78.57
- return_5d: 6.96
- return_20d: 35.76
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: 7.45
- distance_to_high_60_pct: -9.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,90.5,96.5,88.4,95,9212000,83.42,13.88,82.8,75.07,2.19
20260429,95,104.5,94.1,95,21721000,84.39,12.58,83.85,75.48,4.12
20260430,95.8,96.5,88.9,91.5,12956000,84.98,7.67,84.83,75.83,2.21
20260504,91.1,100.5,88.1,100.5,13500000,86.27,16.49,86.11,76.33,2.08
20260505,102.5,110.5,102.5,110.5,6735000,88.29,25.15,88.04,76.98,0.99
20260506,121.5,121.5,121.5,121.5,2545000,91.06,33.43,90.16,77.82,0.37
20260507,133.5,133.5,133.5,133.5,2608000,94.6,41.13,92.87,78.83,0.39
20260508,131.5,136,120.5,120.5,18831000,96.76,24.54,94.88,79.64,2.48
20260511,121.5,124,118,121,8204000,98.78,22.5,96.97,80.47,1.03
20260512,120.5,123,112.5,120.5,9104000,100.59,19.8,98.86,81.3,1.11
20260513,120,123,114.5,119,4688000,102.12,16.53,100.73,82.07,0.56
20260514,121.5,127,116,120.5,8813000,103.65,16.25,102.83,82.84,1.01
20260515,120.5,122,112.5,114.5,6323000,104.56,9.51,104.63,83.53,0.71
20260518,112,119,110,115.5,3777000,105.47,9.51,106.49,84.25,0.42
20260519,115.5,116.5,110.5,115,3301000,106.26,8.22,107.94,84.97,0.37
20260520,114.5,118.5,111.5,114.5,3183000,106.95,7.06,109.05,85.67,0.37
20260521,118,119,112.5,113,3799000,107.45,5.16,110.11,86.34,0.45
20260522,114.5,124,113.5,124,120000,108.83,13.94,111.56,87.19,0.02
20260525,128,129,119.5,121,123000,109.85,10.15,112.86,87.94,0.02
20260526,122,124.5,115.5,123,121000,110.94,10.87,114.47,88.73,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 41.3
- over_600_ratio: 38.01
- over_800_ratio: 36.27
- over_1000_ratio: 33.46
- over_400_change_1w: -0.58
- over_800_change_1w: 0.5
- over_1000_change_1w: -0.83
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.04,,37.07,,32.24,,0,False,False
20260508,46.96,3.92,39.84,2.77,36.2,3.96,1,True,True
20260515,41.88,-5.08,35.77,-4.07,34.29,-1.91,0,False,False
20260522,41.3,-0.58,36.27,0.5,33.46,-0.83,1,False,True
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
