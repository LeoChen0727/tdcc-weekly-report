# INDIVIDUAL STOCK CHATGPT PACKET - 5011 久陽

## Metadata
- generated_at: 2026-05-29 19:33:01 Asia/Taipei
- stock_id: 5011
- stock_name: 久陽
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5011_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5011_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5011_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5011_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5011_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5011_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5011_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5011_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5011_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5011_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5011_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5011_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5011_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5011.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5011.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5011.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5011.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5011.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5011.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5011_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5011_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5011_latest.md?ref=main

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
- open: 18.1
- high: 19.9
- low: 18.1
- close: 18.7
- volume: 19000
- ma5: 18.53
- ema23_primary: 16.21
- distance_to_ema23_pct: 15.36
- ma20: 16.05
- ma60: 14.77
- ma120: 13.09
- return_5d: 16.15
- return_20d: 26.78
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: 16.51
- distance_to_high_60_pct: -6.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,14.8,14.9,14.45,14.85,346000,14.04,5.78,13.89,13.61,0.83
20260505,14.9,15.8,14.9,15.4,804000,14.15,8.81,14.01,13.65,1.77
20260506,15.4,15.4,14.85,15.05,356000,14.23,5.78,14.12,13.69,0.79
20260507,15.2,15.35,14.8,14.95,427000,14.29,4.64,14.21,13.72,0.93
20260508,14.9,15.1,14.6,14.6,304000,14.31,2,14.27,13.76,0.65
20260511,14.75,15.6,14.6,15.4,941000,14.4,6.91,14.39,13.8,1.88
20260512,15.4,15.6,15.1,15.1,260000,14.46,4.41,14.48,13.85,0.52
20260513,15.1,15.5,15,15.2,432000,14.52,4.66,14.58,13.91,0.85
20260514,15.3,16.3,15.3,15.7,957000,14.62,7.38,14.69,13.97,1.84
20260515,15.7,15.7,15.05,15.1,629000,14.66,2.99,14.69,14.02,1.34
20260518,15.05,15.15,14.5,15.05,248000,14.69,2.42,14.71,14.08,0.58
20260519,15.1,15.2,14.8,15.05,225000,14.72,2.22,14.74,14.13,0.53
20260520,15.05,15.25,15.05,15.05,167000,14.75,2.03,14.77,14.19,0.4
20260521,15.1,16.1,15.1,15.75,691000,14.83,6.17,14.82,14.25,1.58
20260522,15.9,16.2,15.5,16.1,16000,14.94,7.77,14.91,14.31,0.04
20260525,16.1,17.7,15.85,17.7,17000,15.17,16.68,15.1,14.4,0.04
20260526,18.1,19.45,17.9,19.45,19000,15.53,25.27,15.4,14.53,0.05
20260527,19.65,20,18.6,18.7,19000,15.79,18.42,15.65,14.62,0.05
20260528,18.7,18.9,18,18.1,18000,15.98,13.24,15.85,14.7,0.05
20260529,18.1,19.9,18.1,18.7,19000,16.21,15.36,16.05,14.77,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 43.75
- over_600_ratio: 40.8
- over_800_ratio: 35.09
- over_1000_ratio: 29.62
- over_400_change_1w: 0.12
- over_800_change_1w: -0.04
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.79,,33.28,,28.6,,0,False,False
20260508,43.36,-0.43,33.44,0.16,29.62,1.02,1,False,True
20260515,43.63,0.27,35.13,1.69,29.62,0,2,False,True
20260522,43.75,0.12,35.09,-0.04,29.62,0,3,False,False
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
