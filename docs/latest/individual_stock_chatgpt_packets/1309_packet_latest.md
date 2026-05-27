# INDIVIDUAL STOCK CHATGPT PACKET - 1309 台達化

## Metadata
- generated_at: 2026-05-27 21:26:07 Asia/Taipei
- stock_id: 1309
- stock_name: 台達化
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1309_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1309_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1309_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1309_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1309_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1309_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1309_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1309_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1309_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1309_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1309_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1309_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1309_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1309.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1309.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1309.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1309.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1309.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1309.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1309_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1309_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1309_latest.md?ref=main

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
- open: 15.2
- high: 15.45
- low: 14.75
- close: 14.8
- volume: 3898504
- ma5: 15.41
- ema23_primary: 16.89
- distance_to_ema23_pct: -12.38
- ma20: 16.85
- ma60: 18.27
- ma120: 14.99
- return_5d: -4.82
- return_20d: -23.71
- volume_ratio: 0.48
- distance_to_ma20_pct_auxiliary: -12.18
- distance_to_high_60_pct: -45.19

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,19.7,20.25,18.85,18.95,9500655,20.03,-5.4,21.59,16.83,0.34
20260430,19.65,20.8,19.35,20.8,24559783,20.1,3.5,21.48,16.98,0.97
20260504,19.7,19.75,18.85,19.2,16203835,20.02,-4.1,21.25,17.1,0.69
20260505,19.9,20.2,19.3,19.5,10352063,19.98,-2.39,20.93,17.21,0.48
20260506,18.6,18.8,18.15,18.25,11945561,19.83,-7.99,20.52,17.31,0.67
20260507,17.6,17.9,17.1,17.4,10704482,19.63,-11.37,20.2,17.39,0.6
20260508,17.7,17.85,16.75,16.85,7688320,19.4,-13.14,19.87,17.46,0.48
20260511,17.05,17.4,16.8,16.9,5214749,19.19,-11.94,19.58,17.54,0.34
20260512,16.75,16.9,16.45,16.65,3956508,18.98,-12.27,19.24,17.63,0.28
20260513,17.2,17.3,16.2,16.2,5867808,18.75,-13.59,18.92,17.7,0.43
20260514,16.25,16.25,15.95,16.1,4148416,18.53,-13.1,18.66,17.77,0.32
20260515,16.1,16.15,15.65,15.65,5148797,18.29,-14.42,18.41,17.82,0.4
20260518,16.5,17.2,16.4,16.5,16296765,18.14,-9.03,18.25,17.9,1.27
20260519,16,16.4,15.45,15.5,6152875,17.92,-13.5,18.07,17.95,0.49
20260520,15.5,15.8,15.25,15.55,3661810,17.72,-12.25,17.9,18.02,0.3
20260521,15.35,16,15.1,15.65,3478169,17.55,-10.82,17.75,18.07,0.29
20260522,15.35,15.8,15.25,15.75,4331166,17.4,-9.48,17.52,18.13,0.41
20260525,15.55,15.75,14.95,15.65,6346096,17.25,-9.29,17.27,18.19,0.71
20260526,15.45,15.85,15.15,15.2,3420820,17.08,-11.02,17.08,18.23,0.4
20260527,15.2,15.45,14.75,14.8,3898504,16.89,-12.38,16.85,18.27,0.48
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 46.3
- over_600_ratio: 44.11
- over_800_ratio: 43.58
- over_1000_ratio: 42.9
- over_400_change_1w: -0.12
- over_800_change_1w: 0.69
- over_1000_change_1w: 0.92
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.43,,43.58,,42.9,,0,False,False
20260508,46.91,0.48,43.26,-0.32,42.8,-0.1,1,False,False
20260515,46.42,-0.49,42.89,-0.37,41.98,-0.82,0,False,False
20260522,46.3,-0.12,43.58,0.69,42.9,0.92,1,False,True
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
| 20260527 | 1309 | 台達化 | 4 | 0 | 304500.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
