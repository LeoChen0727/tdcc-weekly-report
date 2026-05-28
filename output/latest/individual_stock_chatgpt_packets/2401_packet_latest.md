# INDIVIDUAL STOCK CHATGPT PACKET - 2401 凌陽

## Metadata
- generated_at: 2026-05-28 19:31:54 Asia/Taipei
- stock_id: 2401
- stock_name: 凌陽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2401_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2401_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2401_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2401_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2401_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2401_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2401_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2401_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2401_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2401_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2401_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2401_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2401_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2401.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2401.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2401.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2401.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2401.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2401.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2401_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2401_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2401_latest.md?ref=main

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
- date: 20260528
- open: 30.9
- high: 31.65
- low: 29.9
- close: 30.05
- volume: 18548201
- ma5: 30.28
- ema23_primary: 26.83
- distance_to_ema23_pct: 12
- ma20: 26.7
- ma60: 23.29
- ma120: 22.22
- return_5d: 1.69
- return_20d: 28.69
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: 12.55
- distance_to_high_60_pct: -8.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,23.5,24.5,23.35,24.1,5921473,22.84,5.53,22.5,21.83,0.72
20260504,24.6,25.95,24.5,25.3,15239517,23.04,9.8,22.77,21.87,1.7
20260505,24.8,25.7,24.6,25.15,7225790,23.22,8.32,23.05,21.91,0.78
20260506,25.65,25.75,24.75,25.1,6703179,23.37,7.38,23.34,21.94,0.7
20260507,25.5,25.75,25.05,25.4,6343689,23.54,7.89,23.6,21.98,0.65
20260508,25.55,26.35,24.65,25.3,11519199,23.69,6.8,23.86,22.03,1.12
20260511,25.55,26.25,25.25,25.65,8348210,23.85,7.53,24.16,22.09,0.79
20260512,25.85,26.35,25.05,25.95,7540846,24.03,8,24.41,22.18,0.7
20260513,25.4,25.4,24.2,24.95,6411646,24.1,3.51,24.55,22.23,0.6
20260514,25.05,25.2,24.25,24.85,5533656,24.17,2.83,24.67,22.28,0.52
20260515,25.05,25.3,24.4,24.65,4555114,24.21,1.83,24.77,22.33,0.42
20260518,24.8,24.9,23.45,24.8,4362868,24.26,2.24,24.82,22.39,0.42
20260519,24.95,25.6,24.35,24.95,4948035,24.31,2.61,24.86,22.46,0.54
20260520,25.15,27.4,25,26.9,34827879,24.53,9.66,24.93,22.55,3.5
20260521,27.3,29.55,26.75,29.55,47782529,24.95,18.45,25.13,22.69,4.21
20260522,30.45,31.75,29.2,30.75,57498129,25.43,20.91,25.43,22.82,4.26
20260525,30.75,31,29.35,29.45,27071134,25.77,14.3,25.63,22.91,1.91
20260526,29.5,30.25,28.45,30.1,22630155,26.13,15.2,25.98,23.04,1.55
20260527,30.35,33,30.35,31.05,30654029,26.54,17,26.36,23.17,1.93
20260528,30.9,31.65,29.9,30.05,18548201,26.83,12,26.7,23.29,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 40.85
- over_600_ratio: 38.2
- over_800_ratio: 36.96
- over_1000_ratio: 35.57
- over_400_change_1w: 2.67
- over_800_change_1w: 2.22
- over_1000_change_1w: 2.54
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,37.3,,33.87,,32.3,,0,False,False
20260508,37.85,0.55,34.48,0.61,32.27,-0.03,1,False,True
20260515,38.18,0.33,34.74,0.26,33.03,0.76,2,True,True
20260522,40.85,2.67,36.96,2.22,35.57,2.54,3,True,True
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
| 20260528 | 2401 | 凌陽 | 14 | 0 | 4606750.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
