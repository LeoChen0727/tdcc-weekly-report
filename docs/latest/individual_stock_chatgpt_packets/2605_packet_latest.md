# INDIVIDUAL STOCK CHATGPT PACKET - 2605 新興

## Metadata
- generated_at: 2026-05-27 21:26:42 Asia/Taipei
- stock_id: 2605
- stock_name: 新興
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2605_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2605_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2605_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2605_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2605_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2605_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2605_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2605_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2605_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2605_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2605_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2605_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2605_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2605.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2605.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2605.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2605.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2605.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2605.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2605_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2605_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2605_latest.md?ref=main

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
- date: 20260527
- open: 31.15
- high: 31.45
- low: 30.75
- close: 31
- volume: 3391038
- ma5: 31.09
- ema23_primary: 32.42
- distance_to_ema23_pct: -4.38
- ma20: 32.31
- ma60: 35.9
- ma120: 31.84
- return_5d: 2.99
- return_20d: -5.92
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: -4.05
- distance_to_high_60_pct: -32.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,33.4,33.6,33.15,33.3,3117695,35.84,-7.1,36.77,35.05,0.28
20260430,33.6,34.85,33.55,34.7,8307810,35.75,-2.93,36.4,35.15,0.83
20260504,34.7,35.7,34.65,35,6330696,35.69,-1.92,36.1,35.25,0.68
20260505,35,35.15,34.6,34.9,2591913,35.62,-2.02,35.78,35.35,0.29
20260506,35.8,36.1,35.15,35.5,6454161,35.61,-0.31,35.48,35.45,0.73
20260507,35.6,35.65,34.3,34.4,8249674,35.51,-3.13,35.26,35.5,0.99
20260508,34.65,34.65,33,33.05,6967733,35.3,-6.39,34.96,35.56,0.83
20260511,33.05,34.65,31.65,34.1,9083117,35.2,-3.14,34.69,35.64,1.06
20260512,33.6,34.1,32.85,33,6221781,35.02,-5.77,34.33,35.73,0.73
20260513,33.4,33.5,32,32.1,4791838,34.78,-7.7,34.12,35.79,0.62
20260514,32.4,32.45,31.05,31.05,6673244,34.47,-9.91,33.89,35.82,0.92
20260515,31.05,31.2,29.3,29.3,7962624,34.04,-13.91,33.57,35.84,1.13
20260518,29.55,30.3,29.5,29.95,3999657,33.7,-11.12,33.28,35.87,0.59
20260519,30.4,30.65,30.1,30.3,3068043,33.41,-9.32,33.08,35.9,0.48
20260520,30.3,31.5,30.05,30.1,5612850,33.14,-9.16,32.88,35.91,0.9
20260521,30.1,30.7,29.9,30.6,3583481,32.93,-7.06,32.69,35.94,0.58
20260522,30.7,31.35,30.65,31.3,4496944,32.79,-4.54,32.6,35.96,0.8
20260525,31.3,31.5,30.3,31.3,5963042,32.67,-4.18,32.49,35.97,1.07
20260526,31.3,31.8,31.25,31.25,2920540,32.55,-3.99,32.41,35.94,0.53
20260527,31.15,31.45,30.75,31,3391038,32.42,-4.38,32.31,35.9,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.63
- over_600_ratio: 51.77
- over_800_ratio: 50.51
- over_1000_ratio: 49.58
- over_400_change_1w: -0.47
- over_800_change_1w: -0.26
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.47,,51.18,,49.62,,0,False,False
20260508,55.13,-0.34,51.14,-0.04,49.75,0.13,1,False,True
20260515,55.1,-0.03,50.77,-0.37,49.55,-0.2,0,False,False
20260522,54.63,-0.47,50.51,-0.26,49.58,0.03,1,False,True
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
| 20260527 | 2605 | 新興 | 92 | 6 | 1515170.0 | 26800.0 | 56.54 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
