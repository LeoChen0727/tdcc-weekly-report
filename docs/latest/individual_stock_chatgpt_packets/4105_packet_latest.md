# INDIVIDUAL STOCK CHATGPT PACKET - 4105 東洋

## Metadata
- generated_at: 2026-05-30 23:42:15 Asia/Taipei
- stock_id: 4105
- stock_name: 東洋
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4105_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4105_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4105_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4105_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4105_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4105_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4105_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4105_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4105_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4105_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4105_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4105_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4105_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4105.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4105.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4105.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4105.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4105.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4105.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4105_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4105_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4105_latest.md?ref=main

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
- open: 73.1
- high: 73.9
- low: 73.1
- close: 73.4
- volume: 73000
- ma5: 73.4
- ema23_primary: 74.16
- distance_to_ema23_pct: -1.03
- ma20: 74.33
- ma60: 75.91
- ma120: 79.64
- return_5d: -0.94
- return_20d: -1.08
- volume_ratio: 0.14
- distance_to_ma20_pct_auxiliary: -1.24
- distance_to_high_60_pct: -13.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,74.3,74.4,73.2,73.8,1055000,74.47,-0.9,73.69,79.19,1.27
20260505,74,74.8,73.7,74.2,1134000,74.45,-0.33,73.72,79.01,1.35
20260506,74.5,74.5,73.1,73.5,984000,74.37,-1.17,73.69,78.8,1.17
20260507,74.3,74.7,73.9,74.5,1196000,74.38,0.16,73.72,78.61,1.39
20260508,74.2,75.6,74.2,75.4,902000,74.47,1.26,73.8,78.45,1.04
20260511,75.6,75.7,74.9,75.2,574000,74.53,0.9,73.83,78.28,0.68
20260512,75.3,75.3,74.6,75.3,515000,74.59,0.95,73.86,78.14,0.61
20260513,75.3,75.7,75,75.6,632000,74.68,1.24,73.93,78,0.75
20260514,75.7,76.2,75,76,594000,74.79,1.62,74.02,77.85,0.7
20260515,76.2,76.4,74.5,75.1,687000,74.81,0.39,74.06,77.69,0.81
20260518,75,75,74.2,74.4,374000,74.78,-0.5,74.06,77.52,0.44
20260519,74.4,75.3,74.2,74.2,616000,74.73,-0.71,74.08,77.34,0.75
20260520,74.4,74.7,73.6,74,476000,74.67,-0.9,74.09,77.18,0.6
20260521,74.1,74.3,73.9,74.2,270000,74.63,-0.58,74.14,77.02,0.36
20260522,74.1,74.4,73.5,74.1,74000,74.59,-0.65,74.25,76.84,0.11
20260525,74.2,74.4,73.5,73.5,74000,74.49,-1.34,74.31,76.65,0.11
20260526,73.6,74.1,73.5,73.9,74000,74.45,-0.73,74.41,76.48,0.12
20260527,73.9,73.9,73,73.2,73000,74.34,-1.54,74.41,76.29,0.12
20260528,73.6,73.8,72.8,73,73000,74.23,-1.66,74.36,76.09,0.13
20260529,73.1,73.9,73.1,73.4,73000,74.16,-1.03,74.33,75.91,0.14
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 48.19
- over_600_ratio: 44.47
- over_800_ratio: 41.39
- over_1000_ratio: 37.83
- over_400_change_1w: -0.28
- over_800_change_1w: 0.16
- over_1000_change_1w: -0.54
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.67,,40.63,,37.39,,0,False,False
20260508,47.81,0.14,40.97,0.34,37.75,0.36,1,True,True
20260515,48.55,0.74,41.2,0.23,38.34,0.59,2,True,True
20260522,48.47,-0.08,41.23,0.03,38.37,0.03,3,False,True
20260529,48.19,-0.28,41.39,0.16,37.83,-0.54,4,False,True
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
