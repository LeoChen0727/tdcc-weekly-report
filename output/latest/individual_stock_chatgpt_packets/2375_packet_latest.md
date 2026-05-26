# INDIVIDUAL STOCK CHATGPT PACKET - 2375 凱美

## Metadata
- generated_at: 2026-05-26 23:00:39 Asia/Taipei
- stock_id: 2375
- stock_name: 凱美
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 6
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2375_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2375_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2375_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2375_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2375_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2375_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2375_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2375_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2375_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2375_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2375_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2375_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2375_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2375.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2375.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2375.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2375.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2375.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2375.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2375_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2375_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2375_latest.md?ref=main

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
- open: 134
- high: 135.5
- low: 126
- close: 134
- volume: 17340152
- ma5: 128.1
- ema23_primary: 104.87
- distance_to_ema23_pct: 27.78
- ma20: 101.83
- ma60: 88.54
- ma120: 90.89
- return_5d: 32.02
- return_20d: 66.87
- volume_ratio: 1.41
- distance_to_ma20_pct_auxiliary: 31.59
- distance_to_high_60_pct: -7.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,80,88.3,80,88.3,7531149,82.95,6.45,81.64,85.31,2.04
20260429,88.3,90.5,87.2,87.6,8332575,83.34,5.12,82.1,85.05,2.05
20260430,88.2,89.9,85,85,3765002,83.47,1.83,82.66,84.71,0.91
20260504,86.4,89.9,85.1,87.6,3342542,83.82,4.51,83.23,84.47,0.78
20260505,88.3,90.4,87.6,90,5116377,84.33,6.72,84.1,84.27,1.14
20260506,91,92.5,86.3,88.7,4797352,84.7,4.73,84.83,84.08,1.02
20260507,91,96.5,88.2,91.3,11589793,85.25,7.1,85.48,83.95,2.22
20260508,92.1,95.5,89.5,90.4,9064706,85.68,5.51,86.11,83.88,1.61
20260511,90,91.8,86.5,91.5,4904848,86.16,6.2,86.79,83.89,0.85
20260512,91.5,95.9,89.6,94.8,10395859,86.88,9.11,87.25,84.05,1.71
20260513,93.8,96.4,91.7,96,7092583,87.64,9.54,87.79,84.23,1.19
20260514,103.5,105.5,98.1,101,18728691,88.76,13.8,88.55,84.48,2.9
20260515,100,110.5,99.4,99.4,21501438,89.64,10.89,89.14,84.74,3.03
20260518,101,104.5,99.4,103,13180403,90.76,13.49,89.89,85.1,1.77
20260519,100,103,98.7,101.5,8200143,91.65,10.75,90.5,85.41,1.09
20260520,101.5,111.5,101,111.5,12093316,93.3,19.5,91.67,85.86,1.52
20260521,116.5,122.5,116.5,122.5,10748130,95.74,27.95,93.51,86.48,1.29
20260522,131.5,134.5,125.5,134.5,28362060,98.97,35.9,96.2,87.2,2.95
20260525,142,145,133.5,138,40344995,102.22,35,99.14,87.9,3.5
20260526,134,135.5,126,134,17340152,104.87,27.78,101.83,88.54,1.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 35.1
- over_600_ratio: 32.23
- over_800_ratio: 31.57
- over_1000_ratio: 29.08
- over_400_change_1w: 7.79
- over_800_change_1w: 8.18
- over_1000_change_1w: 8.27
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260417,26.65,,22.35,,21.5,,0,False,False
20260424,26.61,-0.04,22.64,0.29,21.87,0.37,1,False,True
20260430,25.38,-1.23,22.29,-0.35,21.52,-0.35,0,False,False
20260508,26.71,1.33,21.76,-0.53,20.08,-1.44,1,False,False
20260515,27.31,0.6,23.39,1.63,20.81,0.73,2,True,True
20260522,35.1,7.79,31.57,8.18,29.08,8.27,3,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2375 | 凱美 | 2 | 1 | 2 | 2 | 2 | continued_2_3d | 連續 2 個交易日上榜，訊號延續但仍需確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2375 | 凱美 | 30 | 1 | 12370160.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
