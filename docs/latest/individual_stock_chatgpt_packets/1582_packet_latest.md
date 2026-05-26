# INDIVIDUAL STOCK CHATGPT PACKET - 1582 信錦

## Metadata
- generated_at: 2026-05-26 23:00:20 Asia/Taipei
- stock_id: 1582
- stock_name: 信錦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 26
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1582_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1582_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1582_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1582_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1582_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1582_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1582_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1582_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1582_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1582_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1582_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1582_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1582_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1582.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1582.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1582.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1582.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1582.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1582.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1582_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1582_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1582_latest.md?ref=main

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
- open: 115.5
- high: 116.5
- low: 108.5
- close: 111.5
- volume: 8725077
- ma5: 113
- ema23_primary: 102.48
- distance_to_ema23_pct: 8.8
- ma20: 99.03
- ma60: 95.38
- ma120: 81.08
- return_5d: -4.7
- return_20d: 23.2
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 12.59
- distance_to_high_60_pct: -9.35

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,90.3,90.9,88.6,89.7,1334020,96.27,-6.83,100.5,85.62,0.13
20260429,89,92.5,88.5,90.7,1977963,95.81,-5.33,99.93,85.98,0.22
20260430,91.2,91.5,88.5,88.6,1957551,95.21,-6.94,99.43,86.32,0.23
20260504,89.4,97.4,88.7,94,6428352,95.11,-1.16,98.73,86.75,0.78
20260505,93.3,94.7,92.5,93.5,2420077,94.97,-1.55,98.16,87.14,0.33
20260506,93.7,94,88.8,90.6,3868067,94.61,-4.24,97.44,87.44,0.56
20260507,88,90.4,86.8,88.7,3455319,94.11,-5.75,96.62,87.73,0.53
20260508,88.5,90.4,86.7,87.8,2027041,93.59,-6.19,96.02,88.03,0.33
20260511,88.5,89.8,87.7,89.5,1637644,93.25,-4.02,95.63,88.39,0.28
20260512,91,92.8,89.7,89.8,2300680,92.96,-3.4,94.8,88.79,0.43
20260513,89.8,94.2,87.9,92,4975300,92.88,-0.95,94.27,89.22,1
20260514,93.8,99.8,93.2,97.8,7138184,93.29,4.83,94.06,89.72,1.41
20260515,100.5,107,98.9,99.4,12706443,93.8,5.97,93.95,90.25,2.34
20260518,99.4,109,97.9,106.5,16357370,94.86,12.27,94.32,90.91,2.71
20260519,106.5,117,106,117,24977663,96.7,20.99,94.82,91.74,3.85
20260520,114,118.5,106.5,107,36875636,97.56,9.67,94.87,92.39,4.65
20260521,117,117.5,115,117.5,6225173,99.22,18.42,95.62,93.21,0.77
20260522,119,120.5,112.5,115,16417505,100.54,14.38,96.72,93.96,1.99
20260525,119.5,123,113,114,15434704,101.66,12.14,97.98,94.69,1.79
20260526,115.5,116.5,108.5,111.5,8725077,102.48,8.8,99.03,95.38,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.42
- over_600_ratio: 38.7
- over_800_ratio: 36.32
- over_1000_ratio: 34.3
- over_400_change_1w: 8.61
- over_800_change_1w: 7.48
- over_1000_change_1w: 6.59
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260306,32.5,1.3,26.51,0.71,24.08,-0.54,3,False,True
20260313,35.61,3.11,29.89,3.38,26.15,2.07,4,True,True
20260320,33.26,-2.35,28.09,-1.8,26.24,0.09,5,False,True
20260327,36.64,3.38,27.58,-0.51,24.55,-1.69,6,False,False
20260402,38.88,2.24,30.88,3.3,27.32,2.77,7,True,True
20260410,35.91,-2.97,29.78,-1.1,26.82,-0.5,0,False,False
20260417,34.56,-1.35,29.56,-0.22,26.61,-0.21,0,False,False
20260424,33.22,-1.34,27.62,-1.94,26.44,-0.17,0,False,False
20260430,32.25,-0.97,27.15,-0.47,25.97,-0.47,0,False,False
20260508,32,-0.25,27.53,0.38,25.76,-0.21,1,False,True
20260515,33.81,1.81,28.84,1.31,27.71,1.95,2,True,True
20260522,42.42,8.61,36.32,7.48,34.3,6.59,3,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 1582 | 信錦 | 1 | 1 | 3 | 3 | 3 | repeated_but_no_breakout | 近 10 日上榜 3 日、近 20 日上榜 3 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 1582 | 信錦 | 35 | 1 | 6434480.0 | 5910.0 | 1088.74 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
