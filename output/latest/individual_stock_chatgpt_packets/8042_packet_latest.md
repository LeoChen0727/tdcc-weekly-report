# INDIVIDUAL STOCK CHATGPT PACKET - 8042 金山電

## Metadata
- generated_at: 2026-05-26 23:55:04 Asia/Taipei
- stock_id: 8042
- stock_name: 金山電
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8042_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8042_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8042_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8042_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8042_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8042_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8042_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8042_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8042_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8042_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8042_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8042_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8042_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8042.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8042.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8042.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8042.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8042.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8042.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8042_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8042_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8042_latest.md?ref=main

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
- open: 133
- high: 148.5
- low: 121.5
- close: 147
- volume: 131000
- ma5: 129.3
- ema23_primary: 99.56
- distance_to_ema23_pct: 47.66
- ma20: 96.02
- ma60: 70.02
- ma120: 64.32
- return_5d: 35.48
- return_20d: 161.1
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 53.09
- distance_to_high_60_pct: -1.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,56.6,59.6,56.2,58.8,2081000,59.21,-0.69,59.15,57.93,0.58
20260429,60,60,57.5,59.2,1000000,59.21,-0.01,59.23,57.79,0.28
20260430,60,60.4,58.2,58.6,811000,59.16,-0.94,59.47,57.64,0.25
20260504,64.4,64.4,64.4,64.4,1411000,59.59,8.06,59.98,57.63,0.44
20260505,70.8,70.8,70.8,70.8,2332000,60.53,16.97,60.97,57.72,0.71
20260506,75,77.8,71.5,77.3,25122000,61.93,24.83,62.24,57.94,5.57
20260507,79.4,85,77.3,85,9735000,63.85,33.13,63.77,58.27,1.97
20260508,85,93.5,84,84.1,26068000,65.54,28.33,65.2,58.66,4.2
20260511,83.8,89.3,82.6,88.9,3722000,67.48,31.74,66.84,59.15,0.59
20260512,95,97.7,95,97.7,2572000,70,39.57,68.65,59.84,0.41
20260513,99.7,106,99.7,106,5198000,73,45.2,70.7,60.7,0.87
20260514,116.5,116.5,106.5,109,2511000,76,43.42,72.92,61.58,0.45
20260515,107.5,107.5,98.1,98.1,1826000,77.84,26.02,74.53,62.31,0.35
20260518,100,107.5,99.7,107.5,2243000,80.31,33.85,76.59,63.24,0.44
20260519,106.5,112.5,104,108.5,1396000,82.66,31.26,78.78,64.09,0.28
20260520,111,119,111,116.5,1664000,85.48,36.28,81.33,65.11,0.34
20260521,120,128,120,125,1230000,88.78,40.8,84.36,66.26,0.25
20260522,122,123,120,123,122000,91.63,34.24,87.56,67.32,0.03
20260525,129,135,129,135,134000,95.24,41.74,91.48,68.56,0.03
20260526,133,148.5,121.5,147,131000,99.56,47.66,96.02,70.02,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.15
- over_600_ratio: 70.68
- over_800_ratio: 69.07
- over_1000_ratio: 67.1
- over_400_change_1w: -0.5
- over_800_change_1w: -0.74
- over_1000_change_1w: -0.64
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.63,,60.4,,59.04,,0,False,False
20260508,73.43,7.8,67.4,7,66.07,7.03,1,True,True
20260515,74.65,1.22,69.81,2.41,67.74,1.67,2,True,True
20260522,74.15,-0.5,69.07,-0.74,67.1,-0.64,0,False,False
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
