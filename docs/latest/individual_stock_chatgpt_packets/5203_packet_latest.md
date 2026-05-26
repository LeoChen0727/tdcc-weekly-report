# INDIVIDUAL STOCK CHATGPT PACKET - 5203 訊連

## Metadata
- generated_at: 2026-05-26 22:19:42 Asia/Taipei
- stock_id: 5203
- stock_name: 訊連
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5203_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5203_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5203_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5203_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5203_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5203_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5203_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5203_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5203_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5203_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5203_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5203_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5203_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5203.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5203.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5203.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5203.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5203.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5203.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5203_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5203_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5203_latest.md?ref=main

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
- open: 65.2
- high: 66.4
- low: 64.3
- close: 65.7
- volume: 261021
- ma5: 64.92
- ema23_primary: 64.69
- distance_to_ema23_pct: 1.56
- ma20: 64.89
- ma60: 63.95
- ma120: 76.42
- return_5d: 2.02
- return_20d: 4.78
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 1.25
- distance_to_high_60_pct: -12.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,62.7,64.1,62.5,63.5,146323,63.99,-0.76,63.28,69.42,0.54
20260429,63.7,64.4,63.4,64.1,106533,64,0.16,63.36,69.06,0.4
20260430,67.3,68.4,65.4,65.4,740673,64.11,2.01,63.55,68.72,2.54
20260504,65.9,67.8,65.9,66.8,391517,64.34,3.83,63.73,68.37,1.3
20260505,66.8,67.3,66.4,67.2,219056,64.58,4.06,63.9,68.04,0.8
20260506,67.6,67.6,65.2,65.8,287693,64.68,1.74,64.06,67.7,1.04
20260507,66.3,66.3,64.9,65.2,280818,64.72,0.74,64.17,67.36,1.03
20260508,65.2,66.6,65.2,65.6,223344,64.79,1.24,64.35,67.03,0.83
20260511,65.6,65.6,64.6,64.7,254857,64.79,-0.13,64.5,66.72,0.93
20260512,64.7,64.8,64,64.4,176829,64.75,-0.55,64.62,66.39,0.65
20260513,64.1,64.1,63,63.6,297629,64.66,-1.64,64.65,66.03,1.11
20260514,63.3,64.1,63,63.8,371577,64.59,-1.22,64.64,65.7,1.33
20260515,63.5,64.6,63.5,63.9,220455,64.53,-0.98,64.56,65.39,0.81
20260518,63.6,65,63.4,64.8,189111,64.55,0.38,64.53,65.11,0.7
20260519,64.8,65.7,64.4,64.4,151757,64.54,-0.22,64.56,64.91,0.58
20260520,64.2,65,63.8,64.5,228593,64.54,-0.06,64.56,64.72,0.88
20260521,64.6,65.5,64.4,64.6,162646,64.54,0.09,64.55,64.53,0.63
20260522,64.4,65,64.1,64.9,247306,64.57,0.51,64.62,64.34,0.97
20260525,65.4,66.5,64.4,64.9,376266,64.6,0.47,64.74,64.14,1.43
20260526,65.2,66.4,64.3,65.7,261021,64.69,1.56,64.89,63.95,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 44.21
- over_600_ratio: 39.8
- over_800_ratio: 35.32
- over_1000_ratio: 34.27
- over_400_change_1w: 0.16
- over_800_change_1w: 1.08
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.79,,34.27,,34.27,,0,False,False
20260508,43.89,0.1,34.23,-0.04,34.23,-0.04,1,False,False
20260515,44.05,0.16,34.24,0.01,34.24,0.01,2,False,True
20260522,44.21,0.16,35.32,1.08,34.27,0.03,3,True,True
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
