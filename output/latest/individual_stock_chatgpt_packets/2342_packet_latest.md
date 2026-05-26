# INDIVIDUAL STOCK CHATGPT PACKET - 2342 茂矽

## Metadata
- generated_at: 2026-05-26 23:53:14 Asia/Taipei
- stock_id: 2342
- stock_name: 茂矽
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2342_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2342_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2342_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2342_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2342_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2342_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2342_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2342_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2342_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2342_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2342_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2342_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2342_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2342.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2342.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2342.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2342.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2342.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2342.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2342_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2342_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2342_latest.md?ref=main

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
- open: 45.85
- high: 47.45
- low: 43.05
- close: 43.35
- volume: 19274704
- ma5: 41.32
- ema23_primary: 39.07
- distance_to_ema23_pct: 10.96
- ma20: 40.03
- ma60: 33.81
- ma120: 32.52
- return_5d: 12.45
- return_20d: 38.06
- volume_ratio: 1.73
- distance_to_ma20_pct_auxiliary: 8.3
- distance_to_high_60_pct: -8.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,31.2,32.9,30.4,31.55,2272833,30.89,2.14,30.16,31.5,1.37
20260429,31.85,32.65,30.95,32.5,2150562,31.02,4.76,30.33,31.41,1.25
20260430,32.55,34.85,32.5,33.6,6981784,31.24,7.56,30.61,31.32,3.48
20260504,33.9,36.6,33.8,36.1,10334062,31.64,14.09,30.97,31.33,4.14
20260505,37.65,39.7,37.65,39.7,7017435,32.31,22.86,31.56,31.4,2.5
20260506,42,43.6,38.65,41.8,38069104,33.1,26.27,32.21,31.53,8.16
20260507,41.75,45.95,40.6,45.95,16079768,34.17,34.46,33.02,31.7,2.98
20260508,45.75,46.7,42.4,43.8,31903418,34.98,25.23,33.74,31.87,4.58
20260511,43.8,45.2,41.9,43.05,15791982,35.65,20.76,34.43,32.04,2.05
20260512,42.2,44.8,40.9,44.1,13768248,36.35,21.31,35.18,32.25,1.64
20260513,43.8,44.55,41,41,12724719,36.74,11.59,35.76,32.4,1.42
20260514,41.75,43.55,41.5,42.15,9221897,37.19,13.33,36.38,32.56,0.99
20260515,42.8,43.2,40,40.45,6889946,37.46,7.97,36.91,32.7,0.72
20260518,39.5,40.2,38.05,39.65,3850197,37.65,5.32,37.36,32.84,0.4
20260519,39.75,40.3,37.6,38.55,5533234,37.72,2.2,37.73,32.97,0.56
20260520,39.1,39.4,38,38.25,2390871,37.77,1.28,38.02,33.1,0.24
20260521,39.95,41.5,39.95,40.45,4483929,37.99,6.48,38.38,33.26,0.45
20260522,41.3,41.6,40.4,41.4,4583060,38.27,8.17,38.85,33.43,0.46
20260525,43.35,44.4,42.2,43.15,8930361,38.68,11.56,39.43,33.61,0.87
20260526,45.85,47.45,43.05,43.35,19274704,39.07,10.96,40.03,33.81,1.73
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 40.56
- over_600_ratio: 39.24
- over_800_ratio: 37.47
- over_1000_ratio: 35.78
- over_400_change_1w: 1.08
- over_800_change_1w: 0.99
- over_1000_change_1w: 1.61
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.05,,36.01,,33.21,,0,False,False
20260508,44.05,5,40.21,4.2,37.95,4.74,1,True,True
20260515,39.48,-4.57,36.48,-3.73,34.17,-3.78,0,False,False
20260522,40.56,1.08,37.47,0.99,35.78,1.61,1,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2342 | 茂矽 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
