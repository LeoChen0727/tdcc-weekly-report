# INDIVIDUAL STOCK CHATGPT PACKET - 9904 寶成

## Metadata
- generated_at: 2026-05-26 21:27:01 Asia/Taipei
- stock_id: 9904
- stock_name: 寶成
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9904_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9904_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9904_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9904_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9904_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9904_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9904_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9904_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9904_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9904_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9904_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9904_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9904_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9904.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9904.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9904.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9904.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9904.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9904.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9904_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9904_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9904_latest.md?ref=main

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
- open: 25.7
- high: 25.85
- low: 25.5
- close: 25.55
- volume: 11925417
- ma5: 25.69
- ema23_primary: 26.18
- distance_to_ema23_pct: -2.41
- ma20: 25.82
- ma60: 27.72
- ma120: 29.28
- return_5d: -2.11
- return_20d: -2.48
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: -1.06
- distance_to_high_60_pct: -17.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,26.05,26.2,25.8,25.8,20819946,27.69,-6.83,27.76,29.32,1.53
20260429,25.8,25.95,25.8,25.85,11634499,27.54,-6.13,27.62,29.23,0.84
20260430,25.9,26.3,25.75,25.75,12978022,27.39,-5.99,27.5,29.15,0.91
20260504,26.05,26.05,25.55,25.6,12176446,27.24,-6.02,27.33,29.06,0.84
20260505,25.6,25.8,25.4,25.6,10157036,27.1,-5.55,27.19,28.97,0.69
20260506,25.7,25.8,25.5,25.6,10258887,26.98,-5.11,27.05,28.87,0.68
20260507,25.7,26.1,25.55,25.95,14713908,26.89,-3.51,26.9,28.79,0.95
20260508,26.2,26.2,25.75,25.9,11645528,26.81,-3.39,26.77,28.71,0.74
20260511,25.95,26.2,25.75,25.8,17539248,26.73,-3.46,26.64,28.63,1.1
20260512,26,26.15,25.8,25.85,14870302,26.65,-3.01,26.53,28.55,0.95
20260513,25.85,26.15,25.6,26.05,12929948,26.6,-2.08,26.43,28.48,0.82
20260514,26.05,26.15,25.85,25.85,11112269,26.54,-2.6,26.32,28.39,0.7
20260515,26.15,26.7,25.9,26,21747884,26.49,-1.87,26.21,28.31,1.32
20260518,26.5,26.65,26.05,26.35,16398819,26.48,-0.5,26.14,28.24,1
20260519,26.35,26.65,26.1,26.1,14663811,26.45,-1.33,26.07,28.16,0.92
20260520,26.2,26.2,25.65,25.65,18311172,26.38,-2.78,26,28.07,1.18
20260521,25.75,25.9,25.6,25.8,16077250,26.34,-2.03,25.95,27.98,1.08
20260522,25.8,25.9,25.7,25.8,12592104,26.29,-1.87,25.91,27.9,0.87
20260525,25.85,25.85,25.55,25.65,13594173,26.24,-2.24,25.86,27.81,0.94
20260526,25.7,25.85,25.5,25.55,11925417,26.18,-2.41,25.82,27.72,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.14
- over_600_ratio: 73.47
- over_800_ratio: 72.43
- over_1000_ratio: 71.4
- over_400_change_1w: -0.49
- over_800_change_1w: -0.4
- over_1000_change_1w: -0.4
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.73,,74,,73.13,,0,False,False
20260508,76.21,-0.52,73.39,-0.61,72.45,-0.68,0,False,False
20260515,75.63,-0.58,72.83,-0.56,71.8,-0.65,0,False,False
20260522,75.14,-0.49,72.43,-0.4,71.4,-0.4,0,False,False
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
| 20260526 | 9904 | 寶成 | 9 | 0 | 88030.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
