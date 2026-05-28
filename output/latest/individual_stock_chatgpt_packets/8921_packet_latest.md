# INDIVIDUAL STOCK CHATGPT PACKET - 8921 沈氏

## Metadata
- generated_at: 2026-05-28 19:33:53 Asia/Taipei
- stock_id: 8921
- stock_name: 沈氏
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 93
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8921_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8921_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8921_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8921_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8921_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8921_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8921_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8921_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8921_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8921_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8921_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8921_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8921_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8921.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8921.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8921.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8921.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8921.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8921.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8921_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8921_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8921_latest.md?ref=main

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
- open: 18.55
- high: 18.55
- low: 17.8
- close: 18.5
- volume: 3113
- ma5: 18.39
- ema23_primary: 18.14
- distance_to_ema23_pct: 2.01
- ma20: 18.25
- ma60: 17.98
- ma120: 17.8
- return_5d: 0
- return_20d: 3.64
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: 1.34
- distance_to_high_60_pct: -5.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260421,17.95,17.95,17.95,17.95,1000,17.54,2.36,17.32,17.82,0.11
20260422,18,18,17.5,18,24000,17.57,2.42,17.35,17.84,2.93
20260423,18.2,18.2,17.7,17.7,3000,17.58,0.66,17.41,17.85,0.39
20260424,18,18.95,18,18.95,93000,17.7,7.07,17.51,17.88,7.62
20260428,18.7,18.7,18.7,18.7,1000,17.78,5.16,17.59,17.91,0.08
20260504,18.6,18.6,18.6,18.6,1000,17.85,4.2,17.67,17.93,0.08
20260505,18.5,18.5,18.5,18.5,1000,17.9,3.33,17.74,17.95,0.08
20260506,18.8,18.8,18.8,18.8,1000,17.98,4.57,17.79,17.96,0.08
20260507,17.8,18.45,17.8,18,7000,17.98,0.11,17.81,17.97,0.57
20260508,18,18.05,18,18.05,4000,17.99,0.35,17.82,17.98,0.34
20260512,17.8,17.8,17.8,17.8,1000,17.97,-0.95,17.86,17.98,0.09
20260513,17.8,18,17.8,18,5000,17.97,0.15,17.89,17.98,0.43
20260514,18.5,18.5,17.8,17.8,5000,17.96,-0.89,17.91,17.98,0.44
20260515,17.8,17.8,17.8,17.8,2000,17.95,-0.81,17.93,17.97,0.19
20260518,18.5,18.5,18.5,18.5,1000,17.99,2.82,18,17.97,0.09
20260520,18.35,18.35,17.8,18.3,3000,18.02,1.57,18.05,17.97,0.31
20260522,18.45,18.45,18.45,18.45,18000,18.05,2.2,18.11,17.98,1.79
20260525,17.5,18.35,17.5,18.2,18000,18.07,0.74,18.15,17.97,1.82
20260526,18.5,18.5,18.5,18.5,18000,18.1,2.2,18.22,17.98,1.73
20260528,18.55,18.55,17.8,18.5,3113,18.14,2.01,18.25,17.98,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 85.15
- over_600_ratio: 76.01
- over_800_ratio: 67.45
- over_1000_ratio: 61.67
- over_400_change_1w: 0.44
- over_800_change_1w: -0.47
- over_1000_change_1w: -0.47
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.71,,67.92,,62.14,,0,False,False
20260508,84.71,0,67.92,0,62.14,0,0,False,False
20260515,84.71,0,67.92,0,62.14,0,0,False,False
20260522,85.15,0.44,67.45,-0.47,61.67,-0.47,1,False,False
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
