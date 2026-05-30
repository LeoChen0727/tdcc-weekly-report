# INDIVIDUAL STOCK CHATGPT PACKET - 1216 統一

## Metadata
- generated_at: 2026-05-30 23:40:51 Asia/Taipei
- stock_id: 1216
- stock_name: 統一
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1216_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1216_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1216_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1216_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1216_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1216_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1216_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1216_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1216_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1216_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1216_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1216_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1216_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1216.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1216.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1216.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1216.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1216.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1216.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1216_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1216_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1216_latest.md?ref=main

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
- open: 71.6
- high: 73.1
- low: 70.8
- close: 71.8
- volume: 38842511
- ma5: 70.96
- ema23_primary: 72.07
- distance_to_ema23_pct: -0.37
- ma20: 72.25
- ma60: 71.64
- ma120: 73.42
- return_5d: 0.42
- return_20d: 3.61
- volume_ratio: 2.13
- distance_to_ma20_pct_auxiliary: -0.62
- distance_to_high_60_pct: -6.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,70,70.2,69.4,69.6,12773554,71.31,-2.4,71.75,71.89,1.22
20260505,69.9,69.9,69.1,69.1,10847905,71.13,-2.85,71.58,71.81,1.02
20260506,69.6,69.6,68.5,68.7,16462509,70.93,-3.14,71.39,71.74,1.47
20260507,68.7,69.9,68.7,69.4,19155077,70.8,-1.98,71.23,71.69,1.63
20260508,70.2,73.4,70,73.2,35053381,71,3.1,71.29,71.7,2.67
20260511,73,74.2,72.5,73.9,15953926,71.24,3.73,71.39,71.74,1.21
20260512,73.9,74.7,73.1,73.1,15905294,71.4,2.39,71.45,71.76,1.17
20260513,73.5,75.6,73.2,75.2,24861423,71.71,4.86,71.61,71.81,1.72
20260514,74.6,75.6,74.6,74.8,12388191,71.97,3.93,71.72,71.85,0.86
20260515,75,76.7,74.9,75.7,17694457,72.28,4.73,71.85,71.89,1.19
20260518,76.2,76.4,74.1,74.7,10538962,72.48,3.06,71.91,71.9,0.7
20260519,75.6,75.6,74.5,74.8,12364345,72.68,2.92,72.02,71.93,0.83
20260520,74.8,74.8,72.7,73.4,13838366,72.74,0.91,72.09,71.93,0.92
20260521,73.5,73.8,72.6,73.1,13692208,72.77,0.46,72.12,71.93,0.9
20260522,72.8,72.9,71.4,71.5,18384453,72.66,-1.6,72.11,71.87,1.19
20260525,72,72,71.2,71.2,13632732,72.54,-1.85,72.09,71.82,0.88
20260526,71.3,71.9,70.8,70.8,17786937,72.39,-2.2,72.11,71.76,1.12
20260527,70.8,71.2,70,70.2,21423701,72.21,-2.79,72.08,71.72,1.29
20260528,70.8,71.5,70.4,70.8,22407549,72.09,-1.79,72.12,71.67,1.32
20260529,71.6,73.1,70.8,71.8,38842511,72.07,-0.37,72.25,71.64,2.13
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 88.39
- over_600_ratio: 87.11
- over_800_ratio: 85.87
- over_1000_ratio: 84.82
- over_400_change_1w: -0.28
- over_800_change_1w: -0.33
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.2,,85.7,,84.63,,0,False,False
20260508,87.92,-0.28,85.4,-0.3,84.39,-0.24,0,False,False
20260515,88.54,0.62,86.05,0.65,84.98,0.59,1,True,True
20260522,88.67,0.13,86.2,0.15,85.11,0.13,2,True,True
20260529,88.39,-0.28,85.87,-0.33,84.82,-0.29,0,False,False
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
| 20260529 | 1216 | 統一 | 15 | 0 | 1406560.0 | 0.0 |  | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
