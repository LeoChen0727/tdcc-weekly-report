# INDIVIDUAL STOCK CHATGPT PACKET - 2493 揚博

## Metadata
- generated_at: 2026-05-30 23:41:31 Asia/Taipei
- stock_id: 2493
- stock_name: 揚博
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2493_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2493_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2493_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2493_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2493_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2493_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2493_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2493_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2493_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2493_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2493_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2493_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2493_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2493.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2493.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2493.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2493.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2493.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2493.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2493_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2493_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2493_latest.md?ref=main

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
- high: 166
- low: 158
- close: 160
- volume: 4547361
- ma5: 158.7
- ema23_primary: 140.83
- distance_to_ema23_pct: 13.62
- ma20: 139.68
- ma60: 124.27
- ma120: 117.44
- return_5d: 16.36
- return_20d: 30.08
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: 14.55
- distance_to_high_60_pct: -7.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,123.5,127,120,124,1640358,123.75,0.21,126.45,114.76,0.43
20260505,125,136,125,136,4686113,124.77,9,128.07,115.18,1.18
20260506,136.5,142,127,139,6839587,125.95,10.36,129.78,115.64,1.59
20260507,142,145,140.5,141,6490247,127.21,10.84,131.05,116.11,1.43
20260508,136.5,138,130,131.5,4012582,127.56,3.08,131.8,116.43,0.87
20260511,131.5,131.5,128.5,129.5,1602783,127.73,1.39,132.32,116.77,0.35
20260512,131,132.5,125.5,127.5,1501307,127.71,-0.16,132.18,117.05,0.35
20260513,127.5,128.5,124,127.5,1194021,127.69,-0.15,131.6,117.35,0.3
20260514,130.5,140,129,140,4605575,128.72,8.77,130.97,117.87,1.22
20260515,140,145.5,133.5,136.5,6786806,129.36,5.52,130.45,118.34,1.85
20260518,134.5,138.5,131.5,134.5,2602200,129.79,3.63,130.12,118.83,0.74
20260519,133.5,135,130.5,131.5,1736459,129.93,1.2,129.88,119.22,0.5
20260520,132,134,128,128.5,1545063,129.82,-1.01,129.53,119.59,0.47
20260521,131.5,137,131,135.5,1709823,130.29,4,129.95,120.08,0.55
20260522,137.5,140.5,136,137.5,2529238,130.89,5.05,130.82,120.56,0.82
20260525,139.5,151,138.5,149,6981961,132.4,12.54,132.32,121.25,2.15
20260526,155.5,163.5,153,163.5,13254705,134.99,21.12,134.32,122.01,3.5
20260527,171,171.5,151,158,10164240,136.91,15.41,135.9,122.57,2.43
20260528,162.5,173.5,162,163,9554309,139.08,17.2,137.82,123.4,2.11
20260529,163.5,166,158,160,4547361,140.83,13.62,139.68,124.27,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 51.08
- over_600_ratio: 47.74
- over_800_ratio: 46.05
- over_1000_ratio: 46.05
- over_400_change_1w: 4.35
- over_800_change_1w: 3.78
- over_1000_change_1w: 3.78
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.87,,42.28,,42.28,,0,False,False
20260508,47.62,-0.25,42.69,0.41,42.04,-0.24,1,False,True
20260515,48.42,0.8,43.44,0.75,43.44,1.4,2,True,True
20260522,46.73,-1.69,42.27,-1.17,42.27,-1.17,0,False,False
20260529,51.08,4.35,46.05,3.78,46.05,3.78,1,True,True
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
| 20260529 | 2493 | 揚博 | 56 | 1 | 8896590.0 | 18900.0 | 470.72 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
