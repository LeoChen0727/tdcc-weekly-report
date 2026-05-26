# INDIVIDUAL STOCK CHATGPT PACKET - 9927 泰銘

## Metadata
- generated_at: 2026-05-26 23:03:02 Asia/Taipei
- stock_id: 9927
- stock_name: 泰銘
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 127
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9927_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9927_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9927_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9927_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9927_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9927_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9927_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9927_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9927_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9927_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9927_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9927_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9927_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9927.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9927.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9927.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9927.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9927.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9927.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9927_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9927_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9927_latest.md?ref=main

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
- open: 67.3
- high: 67.5
- low: 67.1
- close: 67.4
- volume: 117497
- ma5: 67.3
- ema23_primary: 67.91
- distance_to_ema23_pct: -0.75
- ma20: 67.94
- ma60: 68.26
- ma120: 68.49
- return_5d: 1.2
- return_20d: -1.75
- volume_ratio: 1
- distance_to_ma20_pct_auxiliary: -0.8
- distance_to_high_60_pct: -5.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,68.6,68.8,68.4,68.7,45876,69.02,-0.46,69.12,68.89,0.44
20260429,69,69.1,68.5,69.1,38520,69.03,0.11,69.14,68.87,0.41
20260430,69.1,69.1,68.2,68.3,125474,68.97,-0.97,69.18,68.83,1.31
20260504,68.4,68.6,68.3,68.3,50188,68.91,-0.89,69.19,68.8,0.54
20260505,68,68.5,67.9,68.3,62859,68.86,-0.81,69.19,68.77,0.68
20260506,68.3,68.5,67.8,68.5,136833,68.83,-0.48,69.22,68.75,1.43
20260507,68.5,68.8,68,68.5,155528,68.8,-0.44,69.21,68.7,1.58
20260508,69.7,69.7,68.7,69.2,105904,68.84,0.53,69.25,68.67,1.07
20260511,68.7,68.7,67.8,68.4,189115,68.8,-0.58,69.23,68.64,1.82
20260512,68.4,68.4,68.2,68.2,66108,68.75,-0.8,69.14,68.62,0.65
20260513,68.4,68.5,68.1,68.4,71595,68.72,-0.47,69.06,68.6,0.71
20260514,68.1,68.7,68.1,68.2,138211,68.68,-0.69,68.97,68.58,1.33
20260515,68.2,68.4,66.9,67,286127,68.54,-2.24,68.78,68.54,2.53
20260518,67.1,67.4,66.6,66.7,108327,68.38,-2.46,68.59,68.49,0.95
20260519,66.8,66.9,66.6,66.6,139987,68.24,-2.4,68.44,68.45,1.21
20260520,66.7,66.8,66.3,66.7,127430,68.11,-2.07,68.27,68.41,1.09
20260521,67,67.7,66.8,67.5,112332,68.06,-0.82,68.15,68.37,0.94
20260522,67.5,67.8,67.1,67.7,78785,68.03,-0.48,68.08,68.34,0.7
20260525,67.6,67.8,67,67.2,182204,67.96,-1.12,68,68.3,1.57
20260526,67.3,67.5,67.1,67.4,117497,67.91,-0.75,67.94,68.26,1
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.77
- over_600_ratio: 56.52
- over_800_ratio: 54.87
- over_1000_ratio: 52.67
- over_400_change_1w: 0.11
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.28,,54.87,,52.67,,0,False,False
20260508,58.63,0.35,54.87,0,52.67,0,1,False,False
20260515,58.66,0.03,54.87,0,52.67,0,2,False,False
20260522,58.77,0.11,54.87,0,52.67,0,3,False,False
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
