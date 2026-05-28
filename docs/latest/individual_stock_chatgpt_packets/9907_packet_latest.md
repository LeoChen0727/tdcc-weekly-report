# INDIVIDUAL STOCK CHATGPT PACKET - 9907 統一實

## Metadata
- generated_at: 2026-05-28 20:20:43 Asia/Taipei
- stock_id: 9907
- stock_name: 統一實
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9907_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9907_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9907_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9907_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9907_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9907_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9907_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9907_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9907_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9907_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9907_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9907_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9907_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9907.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9907.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9907.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9907.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9907.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9907.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9907_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9907_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9907_latest.md?ref=main

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
- open: 15.85
- high: 15.95
- low: 15.8
- close: 15.8
- volume: 2923040
- ma5: 15.88
- ema23_primary: 16.55
- distance_to_ema23_pct: -4.55
- ma20: 16.52
- ma60: 17.65
- ma120: 18.03
- return_5d: -1.56
- return_20d: -10.73
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: -4.39
- distance_to_high_60_pct: -18.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,17.7,17.75,17.55,17.55,3693661,17.98,-2.4,18.06,18.25,1.16
20260504,17.65,17.8,17.5,17.65,3398894,17.95,-1.69,18.01,18.23,1.09
20260505,17.7,17.85,17.5,17.6,4521987,17.92,-1.81,17.97,18.21,1.38
20260506,17.5,17.5,17.3,17.3,7444099,17.87,-3.2,17.9,18.19,2.09
20260507,17.3,17.35,17,17.25,4900610,17.82,-3.2,17.84,18.18,1.33
20260508,17.25,17.25,17,17.1,3918226,17.76,-3.72,17.77,18.16,1.04
20260511,17.15,17.15,16.9,17,4378947,17.7,-3.94,17.71,18.15,1.12
20260512,17.05,17.05,16.85,16.85,4356611,17.63,-4.41,17.65,18.13,1.1
20260513,16.85,16.85,16.45,16.45,8215709,17.53,-6.15,17.57,18.11,1.95
20260514,16.45,16.55,16.2,16.4,5580235,17.43,-5.93,17.49,18.08,1.28
20260515,16.45,16.5,16.1,16.1,7650600,17.32,-7.06,17.39,18.05,1.65
20260518,16,16.1,15.8,15.9,6503182,17.2,-7.58,17.29,18.02,1.35
20260519,16.05,16.25,15.9,16,3599179,17.1,-6.46,17.19,17.99,0.75
20260520,16.1,16.1,15.85,15.9,4015151,17,-6.49,17.09,17.96,0.84
20260521,16,16.15,15.9,16.05,2750731,16.92,-5.17,17,17.92,0.58
20260522,16.05,16.15,15.9,15.95,3990305,16.84,-5.3,16.91,17.87,0.86
20260525,16,16.05,15.85,15.95,2994642,16.77,-4.88,16.82,17.82,0.65
20260526,15.95,16.1,15.85,15.85,3809121,16.69,-5.05,16.71,17.76,0.83
20260527,15.95,16,15.8,15.85,3163955,16.62,-4.64,16.62,17.71,0.68
20260528,15.85,15.95,15.8,15.8,2923040,16.55,-4.55,16.52,17.65,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 76.68
- over_600_ratio: 75.02
- over_800_ratio: 73.79
- over_1000_ratio: 72.44
- over_400_change_1w: -0.54
- over_800_change_1w: -0.25
- over_1000_change_1w: -0.48
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.49,,75.33,,74.14,,0,False,False
20260508,78,-0.49,74.85,-0.48,73.72,-0.42,0,False,False
20260515,77.22,-0.78,74.04,-0.81,72.92,-0.8,0,False,False
20260522,76.68,-0.54,73.79,-0.25,72.44,-0.48,0,False,False
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
| 20260528 | 9907 | 統一實 | 1 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
