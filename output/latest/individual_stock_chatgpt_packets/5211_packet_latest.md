# INDIVIDUAL STOCK CHATGPT PACKET - 5211 蒙恬

## Metadata
- generated_at: 2026-05-26 23:54:15 Asia/Taipei
- stock_id: 5211
- stock_name: 蒙恬
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5211_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5211_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5211_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5211_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5211_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5211_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5211_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5211_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5211_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5211_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5211_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5211_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5211_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5211.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5211.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5211.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5211.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5211.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5211.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5211_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5211_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5211_latest.md?ref=main

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
- open: 18.3
- high: 18.3
- low: 18
- close: 18
- volume: 18000
- ma5: 17.86
- ema23_primary: 19.63
- distance_to_ema23_pct: -8.31
- ma20: 19.59
- ma60: 21.46
- ma120: 23.88
- return_5d: 0
- return_20d: -11.11
- volume_ratio: 0.12
- distance_to_ma20_pct_auxiliary: -8.1
- distance_to_high_60_pct: -26.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,20.7,21.1,20.7,21,34000,22.08,-4.89,21.77,23.35,0.49
20260429,21.05,21.2,20.5,20.5,117000,21.95,-6.6,21.74,23.25,1.58
20260430,21.15,21.2,20.5,20.6,93000,21.84,-5.66,21.72,23.14,1.21
20260504,20.8,21,20.1,20.15,185000,21.7,-7.12,21.68,23.04,2.22
20260505,20.15,20.5,20.1,20.1,149000,21.56,-6.78,21.65,22.93,1.69
20260506,20.1,20.25,20.1,20.2,93000,21.45,-5.82,21.6,22.82,1.03
20260507,20.25,20.25,20.05,20.25,107000,21.35,-5.15,21.55,22.71,1.14
20260508,20.3,20.4,20.15,20.15,63000,21.25,-5.17,21.5,22.6,0.65
20260511,20.15,20.3,20.1,20.3,68000,21.17,-4.11,21.45,22.5,0.7
20260512,20.3,20.35,20,20.2,141000,21.09,-4.22,21.4,22.39,1.37
20260513,20,21.9,19.15,21.45,701000,21.12,1.57,21.4,22.32,5.22
20260514,21.5,21.5,20.3,20.3,86000,21.05,-3.57,21.23,22.24,0.65
20260515,20.45,20.45,19.6,19.75,72000,20.94,-5.69,21.07,22.15,0.57
20260518,19.7,19.75,19.45,19.5,57000,20.82,-6.35,20.87,22.06,0.45
20260519,19.55,19.6,17.9,18,532000,20.59,-12.57,20.6,21.96,3.5
20260520,18.15,18.6,17.7,17.85,150000,20.36,-12.32,20.32,21.86,0.95
20260521,18,18.15,17.6,17.65,212000,20.13,-12.33,20.07,21.75,1.3
20260522,17.65,17.85,17.4,17.6,18000,19.92,-11.66,19.86,21.64,0.11
20260525,17.8,18.25,17.2,18.2,18000,19.78,-7.98,19.7,21.55,0.11
20260526,18.3,18.3,18,18,18000,19.63,-8.31,19.59,21.46,0.12
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.9
- over_600_ratio: 40.82
- over_800_ratio: 40.82
- over_1000_ratio: 40.82
- over_400_change_1w: -2.39
- over_800_change_1w: 0.05
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.8,,43.87,,43.87,,0,False,False
20260508,52.48,-0.32,43.88,0.01,43.88,0.01,1,False,True
20260515,50.29,-2.19,40.77,-3.11,40.77,-3.11,0,False,False
20260522,47.9,-2.39,40.82,0.05,40.82,0.05,1,False,True
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
