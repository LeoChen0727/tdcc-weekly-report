# INDIVIDUAL STOCK CHATGPT PACKET - 8476 台境*

## Metadata
- generated_at: 2026-05-29 19:34:02 Asia/Taipei
- stock_id: 8476
- stock_name: 台境*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8476_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8476_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8476_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8476_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8476_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8476_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8476_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8476_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8476_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8476_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8476_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8476_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8476_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8476.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8476.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8476.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8476.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8476.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8476.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8476_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8476_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8476_latest.md?ref=main

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
- open: 15.35
- high: 15.6
- low: 15.3
- close: 15.35
- volume: 456167
- ma5: 15.35
- ema23_primary: 16.36
- distance_to_ema23_pct: -6.15
- ma20: 16.27
- ma60: 17.94
- ma120: 18.42
- return_5d: -3.15
- return_20d: -12.03
- volume_ratio: 1.08
- distance_to_ma20_pct_auxiliary: -5.68
- distance_to_high_60_pct: -25.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,17.55,17.65,17.25,17.25,300151,18.23,-5.39,18.21,18.85,0.5
20260505,17.25,17.35,17.1,17.25,513782,18.15,-4.96,18.14,18.8,0.84
20260506,17.3,17.3,17.1,17.2,354434,18.07,-4.82,18.09,18.74,0.57
20260507,17.6,17.6,17.1,17.3,319956,18.01,-3.93,18.01,18.69,0.52
20260508,17.35,17.4,16.95,17.15,529029,17.94,-4.38,17.92,18.66,0.87
20260511,17.05,17.15,16.95,17.1,482676,17.87,-4.29,17.83,18.63,0.79
20260512,17.25,17.25,16.85,17,339452,17.79,-4.46,17.75,18.61,0.56
20260513,16.85,17,16.75,16.75,249745,17.71,-5.41,17.66,18.59,0.42
20260514,16.75,16.9,16.05,16.2,950104,17.58,-7.86,17.55,18.55,1.56
20260515,16.25,16.85,15.95,16.1,555048,17.46,-7.78,17.45,18.51,0.89
20260518,16.1,16.1,15.6,15.85,236364,17.32,-8.51,17.33,18.47,0.39
20260519,15.85,16.05,15.6,15.75,293250,17.19,-8.39,17.21,18.44,0.49
20260520,15.75,16.1,15.7,15.9,225776,17.09,-6.94,17.1,18.39,0.39
20260521,16.05,16.25,15.95,16.1,194351,17,-5.31,16.99,18.36,0.35
20260522,16.1,16.1,15.85,15.85,380523,16.91,-6.25,16.89,18.3,0.71
20260525,15.85,15.85,15.4,15.45,815862,16.79,-7.96,16.76,18.22,1.48
20260526,15.6,15.6,15.2,15.45,411524,16.67,-7.34,16.64,18.16,0.75
20260527,15.45,15.45,15.1,15.15,508162,16.55,-8.44,16.5,18.08,0.9
20260528,15.2,15.55,15.2,15.35,367515,16.45,-6.67,16.38,18.01,0.89
20260529,15.35,15.6,15.3,15.35,456167,16.36,-6.15,16.27,17.94,1.08
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.2
- over_600_ratio: 62.09
- over_800_ratio: 59.98
- over_1000_ratio: 57.81
- over_400_change_1w: -0.13
- over_800_change_1w: 0.08
- over_1000_change_1w: 0.67
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.76,,59.51,,57.38,,0,False,False
20260508,64.83,0.07,59.69,0.18,56.97,-0.41,1,False,True
20260515,65.33,0.5,59.9,0.21,57.14,0.17,2,True,True
20260522,65.2,-0.13,59.98,0.08,57.81,0.67,3,False,True
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
