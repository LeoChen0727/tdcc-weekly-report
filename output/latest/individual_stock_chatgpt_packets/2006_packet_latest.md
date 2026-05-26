# INDIVIDUAL STOCK CHATGPT PACKET - 2006 東和鋼鐵

## Metadata
- generated_at: 2026-05-26 23:00:28 Asia/Taipei
- stock_id: 2006
- stock_name: 東和鋼鐵
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2006_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2006_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2006_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2006_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2006_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2006_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2006_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2006_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2006_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2006_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2006_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2006_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2006_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2006.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2006.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2006.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2006.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2006.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2006.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2006_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2006_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2006_latest.md?ref=main

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
- open: 67.2
- high: 67.6
- low: 65.1
- close: 65.2
- volume: 3478968
- ma5: 65.56
- ema23_primary: 66.71
- distance_to_ema23_pct: -2.26
- ma20: 66.23
- ma60: 70.95
- ma120: 69.92
- return_5d: -0.61
- return_20d: -3.55
- volume_ratio: 1.68
- distance_to_ma20_pct_auxiliary: -1.56
- distance_to_high_60_pct: -22.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,68.1,68.7,67.5,68.6,1951639,70.21,-2.3,69.61,72.49,0.75
20260429,69.1,69.1,66.9,67.1,2401453,69.95,-4.08,69.52,72.45,0.94
20260430,67.1,67.1,65.2,65.2,4460673,69.56,-6.27,69.39,72.35,1.69
20260504,65.7,66.7,65.2,66.6,2073793,69.31,-3.91,69.29,72.28,0.8
20260505,66.6,67.6,66.1,66.8,1654474,69.1,-3.33,69.17,72.21,0.65
20260506,66.8,67.4,66.3,66.7,1695615,68.9,-3.2,69.02,72.15,0.67
20260507,67.2,67.8,67.1,67.6,2230189,68.79,-1.73,68.87,72.1,0.88
20260508,67.8,67.8,66.3,67.4,2125816,68.68,-1.86,68.66,72.04,0.86
20260511,67.8,67.8,67.2,67.7,1348129,68.6,-1.31,68.49,72.01,0.56
20260512,67.7,67.7,65.8,66.2,3270381,68.4,-3.21,68.24,71.96,1.34
20260513,66.2,66.2,65.3,65.5,1793677,68.15,-3.9,67.98,71.88,0.74
20260514,65.5,66.2,65.3,66.1,1401502,67.98,-2.77,67.78,71.8,0.59
20260515,66.1,66.2,65,65,1886006,67.73,-4.04,67.47,71.71,0.8
20260518,65.4,65.4,64.7,64.8,1649961,67.49,-3.99,67.12,71.61,0.71
20260519,65.3,66.3,65.2,65.6,1303695,67.33,-2.57,66.9,71.51,0.59
20260520,65.9,66,65.3,65.3,1146900,67.16,-2.77,66.66,71.41,0.53
20260521,66.1,66.1,65.4,65.5,922622,67.02,-2.27,66.47,71.3,0.45
20260522,65.7,65.8,65.1,65.5,1082443,66.9,-2.09,66.39,71.19,0.56
20260525,65.9,67.3,65.5,66.3,3433915,66.85,-0.82,66.36,71.08,1.7
20260526,67.2,67.6,65.1,65.2,3478968,66.71,-2.26,66.23,70.95,1.68
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.49
- over_600_ratio: 77.25
- over_800_ratio: 75.26
- over_1000_ratio: 73.88
- over_400_change_1w: -0.05
- over_800_change_1w: -0.02
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.99,,76.32,,75.06,,0,False,False
20260508,79.76,-0.23,75.76,-0.56,74.51,-0.55,0,False,False
20260515,79.54,-0.22,75.28,-0.48,73.87,-0.64,0,False,False
20260522,79.49,-0.05,75.26,-0.02,73.88,0.01,1,False,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2006 | 東和鋼鐵 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2006 | 東和鋼鐵 | 3 | 0 | 419670.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
