# INDIVIDUAL STOCK CHATGPT PACKET - 2458 義隆

## Metadata
- generated_at: 2026-05-30 23:41:29 Asia/Taipei
- stock_id: 2458
- stock_name: 義隆
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2458_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2458_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2458_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2458_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2458_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2458_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2458_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2458_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2458_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2458_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2458_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2458_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2458_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2458.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2458.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2458.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2458.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2458.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2458.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2458_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2458_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2458_latest.md?ref=main

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
- open: 163.5
- high: 164.5
- low: 159.5
- close: 162
- volume: 2420522
- ma5: 163.4
- ema23_primary: 151.6
- distance_to_ema23_pct: 6.86
- ma20: 151.4
- ma60: 139.81
- ma120: 130.83
- return_5d: 0
- return_20d: 18.68
- volume_ratio: 0.57
- distance_to_ma20_pct_auxiliary: 7
- distance_to_high_60_pct: -4.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,137,138.5,136,137.5,1567611,134.65,2.12,134.6,129.33,0.43
20260505,138.5,141,136.5,140.5,4793411,135.14,3.97,135.45,129.68,1.28
20260506,141.5,142,137.5,142,4088408,135.71,4.64,136.3,130.07,1.07
20260507,143.5,149,141.5,144,5481547,136.4,5.57,136.95,130.52,1.42
20260508,144.5,155,144,151.5,8538310,137.66,10.06,137.88,131.07,2.07
20260511,151,154,149,150,4560713,138.69,8.16,138.85,131.62,1.08
20260512,151.5,151.5,144.5,145.5,3348565,139.25,4.49,139.4,132.11,0.81
20260513,145.5,147.5,141,142.5,3884586,139.52,2.13,139.7,132.49,0.94
20260514,144,151.5,143.5,149.5,4454806,140.36,6.52,140.35,132.99,1.06
20260515,150.5,150.5,141,142.5,3922993,140.53,1.4,140.55,133.41,0.96
20260518,140,145,138,145,2087946,140.91,2.91,140.9,133.88,0.52
20260519,145.5,153,145,147,6138861,141.41,3.95,141.5,134.36,1.46
20260520,146,154.5,145.5,153,5029399,142.38,7.46,142.3,134.9,1.18
20260521,159,164,157,158.5,7374831,143.72,10.28,143.22,135.56,1.74
20260522,160,164.5,157,162,4498869,145.25,11.53,144.53,136.28,1.08
20260525,167,169,163,163.5,4093334,146.77,11.4,145.88,137.03,0.98
20260526,165,167,161,166,2806262,148.37,11.88,147.38,137.8,0.68
20260527,168.5,170,163,164.5,3325020,149.71,9.88,148.78,138.51,0.79
20260528,164.5,166.5,158.5,161,3208940,150.65,6.87,150.12,139.16,0.75
20260529,163.5,164.5,159.5,162,2420522,151.6,6.86,151.4,139.81,0.57
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 59.88
- over_600_ratio: 55.45
- over_800_ratio: 52.92
- over_1000_ratio: 49.38
- over_400_change_1w: 0.57
- over_800_change_1w: 1.12
- over_1000_change_1w: 0.25
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.01,,52.52,,49.55,,0,False,False
20260508,57.06,0.05,51.87,-0.65,49.79,0.24,1,False,True
20260515,57.8,0.74,51.73,-0.14,49.08,-0.71,2,False,False
20260522,59.31,1.51,51.8,0.07,49.13,0.05,3,True,True
20260529,59.88,0.57,52.92,1.12,49.38,0.25,4,True,True
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
| 20260529 | 2458 | 義隆 | 29 | 0 | 1476380.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
