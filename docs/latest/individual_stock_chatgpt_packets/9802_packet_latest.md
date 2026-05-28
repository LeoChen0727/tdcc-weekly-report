# INDIVIDUAL STOCK CHATGPT PACKET - 9802 鈺齊-KY

## Metadata
- generated_at: 2026-05-28 19:33:55 Asia/Taipei
- stock_id: 9802
- stock_name: 鈺齊-KY
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9802_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9802_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9802_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9802_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9802_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9802_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9802_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9802_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9802_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9802_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9802_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9802_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9802_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9802.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9802.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9802.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9802.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9802.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9802.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9802_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9802_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9802_latest.md?ref=main

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
- open: 74
- high: 74.4
- low: 72.4
- close: 73.5
- volume: 1249537
- ma5: 74.04
- ema23_primary: 76.59
- distance_to_ema23_pct: -4.04
- ma20: 77.47
- ma60: 79.66
- ma120: 90.91
- return_5d: -2.52
- return_20d: -4.92
- volume_ratio: 1.29
- distance_to_ma20_pct_auxiliary: -5.12
- distance_to_high_60_pct: -22.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,77.7,78.3,76.6,77.5,856169,78.12,-0.79,76.99,85.11,0.7
20260504,77.5,80.4,76.6,80.3,1415702,78.3,2.55,77.09,84.83,1.16
20260505,80.5,81.5,78.9,80.9,1158041,78.52,3.04,77.3,84.59,0.96
20260506,82,82,78.2,79.9,1147511,78.63,1.61,77.52,84.31,0.95
20260507,80.2,81,78.9,81,987734,78.83,2.75,77.7,84.06,0.81
20260508,80.9,80.9,79.3,80.4,829103,78.96,1.82,77.94,83.8,0.68
20260511,80.8,85.7,80.7,83.1,1963505,79.31,4.79,78.3,83.61,1.53
20260512,83.5,83.5,80.5,80.7,955263,79.42,1.61,78.47,83.39,0.75
20260513,80.3,80.3,78.9,79.2,375676,79.4,-0.26,78.53,83.16,0.31
20260514,79.1,79.5,77,77,852830,79.2,-2.78,78.47,82.86,0.71
20260515,77,77.8,74.4,75.5,895346,78.89,-4.3,78.19,82.53,0.76
20260518,75.5,76.2,75,75.4,339301,78.6,-4.07,78.03,82.23,0.31
20260519,75.4,78.4,75.4,77,920503,78.47,-1.87,77.99,81.96,0.83
20260520,77,77,75.4,75.9,1076223,78.26,-3.01,77.87,81.66,0.98
20260521,76.5,76.5,75.4,75.4,838132,78.02,-3.35,77.78,81.37,0.78
20260522,75.4,75.9,74.9,75.1,611856,77.77,-3.44,77.75,81.03,0.62
20260525,75.9,75.9,73.1,73.8,1397987,77.44,-4.7,77.72,80.7,1.41
20260526,73.9,75.2,72.9,74.4,661143,77.19,-3.61,77.75,80.36,0.7
20260527,74.5,74.5,72.9,73.4,866111,76.87,-4.52,77.66,80.01,0.92
20260528,74,74.4,72.4,73.5,1249537,76.59,-4.04,77.47,79.66,1.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.32
- over_600_ratio: 60.43
- over_800_ratio: 58.04
- over_1000_ratio: 56.28
- over_400_change_1w: -0.01
- over_800_change_1w: -0.29
- over_1000_change_1w: 0.53
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.11,,57.99,,54.81,,0,False,False
20260508,65.56,0.45,59.14,1.15,56.06,1.25,1,True,True
20260515,65.33,-0.23,58.33,-0.81,55.75,-0.31,0,False,False
20260522,65.32,-0.01,58.04,-0.29,56.28,0.53,1,False,True
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 9802 | 鈺齊-KY | 7 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
