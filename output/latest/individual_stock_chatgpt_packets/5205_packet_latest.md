# INDIVIDUAL STOCK CHATGPT PACKET - 5205 中茂

## Metadata
- generated_at: 2026-05-26 21:25:59 Asia/Taipei
- stock_id: 5205
- stock_name: 中茂
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 107
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5205_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5205_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5205_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5205_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5205_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5205_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5205_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5205_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5205_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5205_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5205_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5205_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5205_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5205.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5205.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5205.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5205.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5205.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5205.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5205_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5205_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5205_latest.md?ref=main

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
- open: 23.85
- high: 23.85
- low: 23.85
- close: 23.85
- volume: 24000
- ma5: 23.22
- ema23_primary: 23.45
- distance_to_ema23_pct: 1.72
- ma20: 22.53
- ma60: 26.18
- ma120: 27.87
- return_5d: 11.19
- return_20d: -0.42
- volume_ratio: 2.74
- distance_to_ma20_pct_auxiliary: 5.87
- distance_to_high_60_pct: -22.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,24.75,24.75,22.7,23.4,6000,26.86,-12.89,27.4,28.18,1.29
20260429,22.2,22.8,22.2,22.8,4000,26.52,-14.04,27.13,28.03,0.88
20260430,22.1,22.75,22.1,22.15,8000,26.16,-15.32,26.79,27.87,1.63
20260504,21.95,21.95,21.95,21.95,1000,25.81,-14.95,26.43,27.74,0.2
20260505,21.9,21.9,21.9,21.9,1000,25.48,-14.06,26.06,27.61,0.2
20260506,21.2,21.65,20.15,21.65,11000,25.16,-13.96,25.68,27.48,2.06
20260507,20.95,22.45,19.85,22.3,12000,24.92,-10.53,25.36,27.36,2.03
20260508,22.2,23.4,20.6,23,15000,24.76,-7.12,25.06,27.25,2.46
20260511,23.7,23.7,21,23.2,15000,24.63,-5.82,24.78,27.13,2.21
20260512,22.85,22.85,22.85,22.85,1000,24.48,-6.68,24.41,27.01,0.15
20260513,22.55,22.55,22.55,22.55,1000,24.32,-7.29,24.11,26.91,0.15
20260514,22,22.6,22,22.6,2000,24.18,-6.53,23.79,26.82,0.3
20260515,22.5,22.5,20.8,21.75,3000,23.98,-9.29,23.48,26.72,0.48
20260518,21.6,21.6,20.9,20.9,3000,23.72,-11.89,23.23,26.61,0.52
20260519,19.95,22.25,19.8,21.45,13000,23.53,-8.85,23,26.51,2.08
20260520,22.2,22.2,22.2,22.2,1000,23.42,-5.21,22.82,26.42,0.16
20260521,22.95,22.95,22.4,22.7,7000,23.36,-2.83,22.68,26.34,1.1
20260522,23.35,23.65,20.9,23.65,23000,23.38,1.13,22.59,26.3,3.54
20260525,23.7,23.7,23.7,23.7,24000,23.41,1.23,22.53,26.25,3.14
20260526,23.85,23.85,23.85,23.85,24000,23.45,1.72,22.53,26.18,2.74
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.44
- over_600_ratio: 71.26
- over_800_ratio: 71.26
- over_1000_ratio: 71.26
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
20260430,74.44,,71.26,,71.26,,0,False,False
20260508,74.44,0,71.26,0,71.26,0,0,False,False
20260515,74.44,0,71.26,0,71.26,0,0,False,False
20260522,74.44,0,71.26,0,71.26,0,0,False,False
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
