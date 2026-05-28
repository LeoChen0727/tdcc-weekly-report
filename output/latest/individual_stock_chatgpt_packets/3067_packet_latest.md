# INDIVIDUAL STOCK CHATGPT PACKET - 3067 全域

## Metadata
- generated_at: 2026-05-28 19:32:16 Asia/Taipei
- stock_id: 3067
- stock_name: 全域
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 98
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3067_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3067_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3067_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3067_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3067_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3067_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3067_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3067_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3067_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3067_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3067_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3067_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3067_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3067.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3067.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3067.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3067.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3067.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3067.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3067_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3067_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3067_latest.md?ref=main

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
- date: 20260528
- open: 18.85
- high: 19.4
- low: 18.8
- close: 18.8
- volume: 17389
- ma5: 18.23
- ema23_primary: 17.92
- distance_to_ema23_pct: 4.89
- ma20: 17.72
- ma60: 18.06
- ma120: 18.36
- return_5d: 7.43
- return_20d: 7.43
- volume_ratio: 1.84
- distance_to_ma20_pct_auxiliary: 6.08
- distance_to_high_60_pct: -10.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,17.55,17.55,17.5,17.5,9000,18.31,-4.41,18.4,18.45,0.68
20260429,17.45,18.1,17,18.1,7000,18.29,-1.03,18.38,18.43,0.52
20260430,18,18,18,18,3000,18.27,-1.45,18.37,18.42,0.22
20260504,18,18,18,18,6000,18.24,-1.33,18.41,18.4,0.44
20260505,17.95,18,17.7,17.7,8000,18.2,-2.74,18.43,18.36,0.57
20260507,17.55,17.55,17.55,17.55,4000,18.14,-3.27,18.44,18.33,0.28
20260508,17.45,17.75,17.45,17.5,16000,18.09,-3.26,18.36,18.31,1.1
20260512,17.5,17.5,17.5,17.5,9000,18.04,-3,18.34,18.29,0.62
20260513,17.5,17.5,17.5,17.5,3000,18,-2.76,18.25,18.27,0.26
20260514,17.5,17.5,17.25,17.25,5000,17.93,-3.81,18.12,18.24,0.56
20260515,17.25,17.3,17.25,17.3,13000,17.88,-3.25,17.99,18.21,1.58
20260518,17.3,17.3,17.3,17.3,1000,17.83,-2.99,17.88,18.16,0.15
20260519,17.35,17.35,17.3,17.3,9000,17.79,-2.74,17.82,18.14,1.42
20260520,17.3,17.3,17.3,17.3,8000,17.75,-2.52,17.75,18.12,1.22
20260521,17.5,17.5,17.5,17.5,1000,17.73,-1.28,17.68,18.1,0.16
20260522,17.1,17.25,17.1,17.25,17000,17.69,-2.47,17.63,18.08,2.45
20260525,17.35,18.45,17.25,18.45,17000,17.75,3.94,17.66,18.07,2.27
20260526,18.3,18.3,18.15,18.15,18000,17.78,2.06,17.65,18.06,2.18
20260527,18.45,18.5,18.45,18.5,18000,17.84,3.68,17.66,18.06,1.99
20260528,18.85,19.4,18.8,18.8,17389,17.92,4.89,17.72,18.06,1.84
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.39
- over_600_ratio: 68.66
- over_800_ratio: 68.66
- over_1000_ratio: 63.68
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.4,,68.67,,63.69,,0,False,False
20260508,71.4,0,68.67,0,63.69,0,0,False,False
20260515,71.4,0,68.67,0,63.69,0,0,False,False
20260522,71.39,-0.01,68.66,-0.01,63.68,-0.01,0,False,False
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
