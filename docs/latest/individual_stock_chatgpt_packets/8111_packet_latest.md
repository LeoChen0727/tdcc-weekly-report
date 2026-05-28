# INDIVIDUAL STOCK CHATGPT PACKET - 8111 立碁

## Metadata
- generated_at: 2026-05-28 20:20:34 Asia/Taipei
- stock_id: 8111
- stock_name: 立碁
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8111_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8111_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8111_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8111_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8111_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8111_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8111_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8111_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8111_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8111_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8111_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8111_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8111_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8111.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8111.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8111.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8111.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8111.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8111.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8111_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8111_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8111_latest.md?ref=main

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
- open: 68
- high: 68.6
- low: 64.4
- close: 64.4
- volume: 66000
- ma5: 67.12
- ema23_primary: 66.26
- distance_to_ema23_pct: -2.81
- ma20: 66.06
- ma60: 66.33
- ma120: 67.67
- return_5d: 3.04
- return_20d: -8.39
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -2.51
- distance_to_high_60_pct: -23.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,70.4,72.4,69.4,69.4,3872000,69.19,0.31,68.83,66.79,0.56
20260504,70.4,70.6,68.5,69.1,2684000,69.18,-0.11,69.25,66.86,0.39
20260505,69.5,71.4,68.9,70.8,2832000,69.31,2.14,69.86,66.97,0.4
20260506,71.5,71.7,66.2,68.6,3863000,69.25,-0.94,70.27,67.02,0.54
20260507,69,69.7,67.4,69.2,2243000,69.25,-0.07,70.67,66.98,0.31
20260508,68.2,70.1,66.2,66.8,2648000,69.05,-3.25,70.96,66.94,0.37
20260511,66.5,67.4,64.6,66.2,2983000,68.81,-3.79,71.02,66.94,0.42
20260512,67.5,68.5,66.1,66.8,2448000,68.64,-2.68,71.02,66.97,0.35
20260513,65.7,66.3,64,64,2517000,68.25,-6.23,70.78,66.95,0.37
20260514,65.2,66.6,63.9,64.6,2224000,67.95,-4.93,70.47,66.9,0.35
20260515,65.1,65.7,62.4,62.4,2142000,67.49,-7.54,70,66.81,0.35
20260518,61.2,63.1,60,62.7,1610000,67.09,-6.54,69.17,66.78,0.29
20260519,62.7,63,61,61.5,1143000,66.62,-7.69,68.36,66.72,0.29
20260520,61.7,62.4,61,61,1036000,66.15,-7.79,67.37,66.62,0.29
20260521,62.2,63.1,61.9,62.5,854000,65.85,-5.09,66.64,66.57,0.27
20260522,63.1,68.1,63.1,66.8,66000,65.93,1.32,66.44,66.55,0.03
20260525,67.5,69.8,67.5,68,68000,66.1,2.87,66.43,66.52,0.03
20260526,68.8,69.3,66.3,68.8,68000,66.33,3.73,66.53,66.48,0.03
20260527,69.6,69.6,66.8,67.6,68000,66.43,1.76,66.36,66.44,0.03
20260528,68,68.6,64.4,64.4,66000,66.26,-2.81,66.06,66.33,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 38.51
- over_600_ratio: 34.37
- over_800_ratio: 31.31
- over_1000_ratio: 28.81
- over_400_change_1w: -0.3
- over_800_change_1w: 0.95
- over_1000_change_1w: 1.04
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.16,,34.63,,33.05,,0,False,False
20260508,41.05,-1.11,33.32,-1.31,30.83,-2.22,0,False,False
20260515,38.81,-2.24,30.36,-2.96,27.77,-3.06,0,False,False
20260522,38.51,-0.3,31.31,0.95,28.81,1.04,1,False,True
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
