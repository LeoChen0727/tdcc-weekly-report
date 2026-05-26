# INDIVIDUAL STOCK CHATGPT PACKET - 8234 新漢

## Metadata
- generated_at: 2026-05-26 23:55:09 Asia/Taipei
- stock_id: 8234
- stock_name: 新漢
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8234_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8234_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8234_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8234_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8234_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8234_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8234_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8234_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8234_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8234_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8234_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8234_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8234_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8234.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8234.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8234.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8234.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8234.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8234.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8234_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8234_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8234_latest.md?ref=main

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
- open: 75.4
- high: 76.5
- low: 71.1
- close: 73.2
- volume: 74000
- ma5: 70.24
- ema23_primary: 68.8
- distance_to_ema23_pct: 6.4
- ma20: 69.8
- ma60: 65.57
- ma120: 69.16
- return_5d: 8.93
- return_20d: 19.8
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 4.88
- distance_to_high_60_pct: -6.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,60.8,65.8,60.3,65.1,1381000,62.81,3.65,61.41,66.16,1.85
20260429,64.6,66.5,63.9,63.9,929000,62.9,1.59,61.52,66,1.19
20260430,64.2,69.2,64,66.9,1891000,63.23,5.8,61.87,65.89,2.24
20260504,68.6,70.4,66.9,69,2393000,63.71,8.3,62.27,65.78,2.51
20260505,69.5,75.7,68.6,75.4,4777000,64.69,16.56,63.05,65.77,4.06
20260506,77.7,78.4,72.9,74,5325000,65.46,13.04,63.84,65.76,3.75
20260507,74.2,74.8,72.9,73.3,1330000,66.12,10.87,64.47,65.7,0.91
20260508,72.6,74.3,69.8,70.5,1550000,66.48,6.04,65.01,65.59,1.01
20260511,70.5,72.6,70.2,71.2,948000,66.87,6.47,65.61,65.56,0.61
20260512,71.9,72.1,69.5,70.8,973000,67.2,5.35,66.17,65.57,0.61
20260513,70.1,70.3,68.3,68.6,736000,67.32,1.9,66.52,65.54,0.47
20260514,68.1,69.1,67.2,68.1,839000,67.38,1.06,66.86,65.49,0.53
20260515,68.1,73.3,68.1,70.8,3482000,67.67,4.63,67.33,65.52,1.98
20260518,70,70.9,67.5,69.9,1136000,67.85,3.02,67.78,65.56,0.63
20260519,70.4,70.8,67,67.2,1053000,67.8,-0.88,68.09,65.55,0.58
20260520,67.7,67.9,65,65.5,804000,67.61,-3.12,68.28,65.5,0.44
20260521,66.5,68.1,66.3,67.6,597000,67.61,-0.01,68.27,65.47,0.35
20260522,67.8,70.5,67.6,70.2,70000,67.82,3.5,68.56,65.44,0.04
20260525,72,76.3,72,74.7,74000,68.4,9.22,69.19,65.5,0.05
20260526,75.4,76.5,71.1,73.2,74000,68.8,6.4,69.8,65.57,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.78
- over_600_ratio: 50.4
- over_800_ratio: 48.32
- over_1000_ratio: 46.59
- over_400_change_1w: -0.63
- over_800_change_1w: 0.84
- over_1000_change_1w: 0.87
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.33,,48.14,,45.8,,0,False,False
20260508,53.15,-1.18,47.98,-0.16,45.64,-0.16,0,False,False
20260515,53.41,0.26,47.48,-0.5,45.72,0.08,1,False,True
20260522,52.78,-0.63,48.32,0.84,46.59,0.87,2,False,True
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
