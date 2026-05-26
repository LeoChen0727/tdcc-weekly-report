# INDIVIDUAL STOCK CHATGPT PACKET - 1437 勤益控

## Metadata
- generated_at: 2026-05-26 23:00:13 Asia/Taipei
- stock_id: 1437
- stock_name: 勤益控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1437_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1437_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1437_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1437_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1437_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1437_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1437_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1437_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1437_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1437_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1437_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1437_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1437_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1437.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1437.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1437.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1437.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1437.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1437.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1437_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1437_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1437_latest.md?ref=main

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
- open: 28.25
- high: 28.5
- low: 28
- close: 28.3
- volume: 207464
- ma5: 28.38
- ema23_primary: 28.94
- distance_to_ema23_pct: -2.22
- ma20: 28.83
- ma60: 30.25
- ma120: 31.77
- return_5d: -0.18
- return_20d: -4.87
- volume_ratio: 1.47
- distance_to_ma20_pct_auxiliary: -1.84
- distance_to_high_60_pct: -15.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,30.3,30.3,29.75,30,29585,30.51,-1.67,30.43,31.42,0.35
20260429,30.4,30.4,29.8,29.95,60279,30.46,-1.69,30.4,31.38,0.73
20260430,29.9,29.9,29.55,29.65,103472,30.4,-2.46,30.36,31.33,1.21
20260504,29.7,29.7,29.35,29.35,160874,30.31,-3.16,30.29,31.29,1.82
20260505,29.4,29.5,29.3,29.35,140658,30.23,-2.91,30.23,31.23,1.54
20260506,29.4,29.45,29.25,29.4,79406,30.16,-2.52,30.18,31.17,0.86
20260507,29.35,29.45,29.05,29.1,186322,30.07,-3.23,30.1,31.11,1.92
20260508,29.15,29.15,28.85,29,139343,29.98,-3.28,30.03,31.05,1.37
20260511,29,29,28.7,28.75,214956,29.88,-3.78,29.93,30.98,1.97
20260512,28.65,28.65,28.55,28.65,146488,29.78,-3.79,29.84,30.92,1.29
20260513,28.55,28.6,28.3,28.6,62108,29.68,-3.64,29.74,30.86,0.56
20260514,28.6,28.6,28.15,28.2,253958,29.56,-4.59,29.62,30.8,2.12
20260515,28.2,28.35,28,28.25,287338,29.45,-4.07,29.51,30.73,2.21
20260518,28.25,28.35,28.1,28.1,77656,29.33,-4.21,29.39,30.67,0.59
20260519,28.15,28.45,28.15,28.35,91200,29.25,-3.09,29.29,30.6,0.7
20260520,28.35,28.35,28,28.35,69734,29.18,-2.84,29.18,30.54,0.54
20260521,28.35,28.5,28.2,28.5,218177,29.12,-2.13,29.08,30.48,1.68
20260522,28.2,28.55,28.2,28.5,159845,29.07,-1.96,29,30.41,1.21
20260525,28.3,28.35,28.15,28.25,137440,29,-2.59,28.9,30.33,1.01
20260526,28.25,28.5,28,28.3,207464,28.94,-2.22,28.83,30.25,1.47
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.98
- over_600_ratio: 74.99
- over_800_ratio: 70.05
- over_1000_ratio: 65.81
- over_400_change_1w: -0.07
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.3,,69.88,,65.16,,0,False,False
20260508,79.28,-0.02,69.48,-0.4,65.68,0.52,1,False,True
20260515,79.05,-0.23,69.99,0.51,65.75,0.07,2,False,True
20260522,78.98,-0.07,70.05,0.06,65.81,0.06,3,False,True
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
