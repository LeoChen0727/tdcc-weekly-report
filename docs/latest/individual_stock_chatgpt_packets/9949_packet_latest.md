# INDIVIDUAL STOCK CHATGPT PACKET - 9949 琉園

## Metadata
- generated_at: 2026-05-30 23:44:05 Asia/Taipei
- stock_id: 9949
- stock_name: 琉園
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9949_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9949_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9949_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9949_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9949_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9949_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9949_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9949_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9949_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9949_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9949_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9949_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9949_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9949.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9949.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9949.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9949.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9949.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9949.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9949_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9949_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9949_latest.md?ref=main

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
- open: 22.5
- high: 23.7
- low: 22.3
- close: 23
- volume: 23000
- ma5: 22.8
- ema23_primary: 24.78
- distance_to_ema23_pct: -7.17
- ma20: 23.77
- ma60: 28.19
- ma120: 27.27
- return_5d: -1.92
- return_20d: -7.63
- volume_ratio: 0.79
- distance_to_ma20_pct_auxiliary: -3.24
- distance_to_high_60_pct: -38.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,25.05,25.4,24.45,24.95,54000,30.53,-18.29,32.21,29.22,0.24
20260505,24.95,25,24.85,24.85,15000,30.06,-17.33,31.85,29.18,0.07
20260506,24.75,24.75,24.4,24.4,24000,29.59,-17.54,31.47,29.15,0.11
20260507,24.4,24.75,24.4,24.75,5000,29.19,-15.2,31.12,29.12,0.02
20260508,26.8,26.8,24.4,24.5,56000,28.8,-14.92,30.73,29.08,0.26
20260511,24.3,24.45,24,24,75000,28.4,-15.48,30.29,29.04,0.35
20260512,23.8,24.25,23.4,24.25,65000,28.05,-13.55,29.85,29.01,0.31
20260513,24.25,24.25,24.15,24.15,16000,27.73,-12.9,29.3,28.98,0.09
20260514,24.15,24.15,23.9,23.95,26000,27.41,-12.63,28.75,28.93,0.15
20260515,23.55,23.8,23.55,23.7,9000,27.1,-12.55,28.16,28.89,0.06
20260518,22.5,24,22.5,24,38000,26.84,-10.59,27.58,28.84,0.27
20260519,24,24,23.45,23.55,32000,26.57,-11.36,26.93,28.8,0.24
20260520,23.55,23.55,22.9,23.35,20000,26.3,-11.22,26.27,28.74,0.17
20260521,23.35,23.55,23.35,23.55,7000,26.07,-9.67,25.71,28.7,0.08
20260522,23.8,23.8,23.45,23.45,22000,25.85,-9.29,25.05,28.63,0.34
20260525,23.5,23.5,22.45,22.85,23000,25.6,-10.75,24.54,28.54,0.36
20260526,22.5,22.8,22.4,22.8,23000,25.37,-10.13,24.19,28.46,0.37
20260527,22.75,22.75,22.4,22.75,23000,25.15,-9.55,23.98,28.36,0.39
20260528,22.75,22.85,22.55,22.6,23000,24.94,-9.38,23.86,28.27,0.66
20260529,22.5,23.7,22.3,23,23000,24.78,-7.17,23.77,28.19,0.79
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 74.48
- over_600_ratio: 69.81
- over_800_ratio: 66.77
- over_1000_ratio: 58.74
- over_400_change_1w: 0.34
- over_800_change_1w: 0.34
- over_1000_change_1w: 0.34
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.03,,67.33,,59.12,,0,False,False
20260508,74.11,-0.92,66.43,-0.9,58.4,-0.72,0,False,False
20260515,74.13,0.02,66.43,0,58.4,0,1,False,False
20260522,74.14,0.01,66.43,0,58.4,0,2,False,False
20260529,74.48,0.34,66.77,0.34,58.74,0.34,3,True,True
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
