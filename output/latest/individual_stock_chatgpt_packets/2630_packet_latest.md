# INDIVIDUAL STOCK CHATGPT PACKET - 2630 亞航

## Metadata
- generated_at: 2026-05-28 20:18:50 Asia/Taipei
- stock_id: 2630
- stock_name: 亞航
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2630_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2630_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2630_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2630_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2630_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2630_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2630_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2630_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2630_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2630_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2630_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2630_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2630_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2630.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2630.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2630.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2630.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2630.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2630.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2630_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2630_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2630_latest.md?ref=main

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
- open: 41.35
- high: 42.25
- low: 41.2
- close: 41.8
- volume: 789235
- ma5: 42.3
- ema23_primary: 44.69
- distance_to_ema23_pct: -6.47
- ma20: 45.02
- ma60: 47.69
- ma120: 49.85
- return_5d: -4.02
- return_20d: -11.44
- volume_ratio: 0.61
- distance_to_ma20_pct_auxiliary: -7.15
- distance_to_high_60_pct: -23.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,47.35,47.55,46.75,46.95,656338,48.61,-3.42,48.01,49.73,0.54
20260504,46.8,49.5,46.8,48.95,1433442,48.64,0.63,48.07,49.63,1.15
20260505,48.65,50.8,48.35,50.3,1181239,48.78,3.12,48.26,49.55,0.93
20260506,50.8,50.9,49.05,49.3,800197,48.82,0.98,48.4,49.48,0.62
20260507,49.4,50.3,48.7,49.75,719464,48.9,1.74,48.52,49.43,0.55
20260508,50.5,51.9,49.95,50.4,2732916,49.03,2.8,48.72,49.4,1.94
20260511,47.6,47.6,45.4,45.6,4771044,48.74,-6.44,48.7,49.32,2.96
20260512,45.6,45.95,45.05,45.15,1415464,48.44,-6.79,48.7,49.27,0.86
20260513,45.2,45.7,44,44.05,1294322,48.07,-8.37,48.59,49.18,0.78
20260514,44.05,44.1,42.95,42.95,1289016,47.65,-9.86,48.41,49.06,0.77
20260515,43.3,44.45,43.1,43.35,1247830,47.29,-8.33,48.14,48.98,0.78
20260518,43.35,43.5,42.85,43.05,759668,46.94,-8.28,47.83,48.89,0.48
20260519,43,43.7,42.7,42.75,556451,46.59,-8.24,47.46,48.8,0.37
20260520,43,44.1,42.75,42.75,1051187,46.27,-7.6,47.14,48.7,0.69
20260521,43.25,43.85,43,43.55,604868,46.04,-5.41,46.76,48.58,0.44
20260522,43.8,43.95,43,43.5,794051,45.83,-5.08,46.37,48.43,0.63
20260525,43.35,43.6,42.7,42.95,1282582,45.59,-5.79,46,48.25,1.01
20260526,43,43.4,42,42,1128469,45.29,-7.27,45.64,48.06,0.88
20260527,42.1,42.25,41.1,41.25,1272661,44.95,-8.24,45.29,47.87,0.98
20260528,41.35,42.25,41.2,41.8,789235,44.69,-6.47,45.02,47.69,0.61
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.7
- over_600_ratio: 64.81
- over_800_ratio: 64.14
- over_1000_ratio: 62.49
- over_400_change_1w: 0.06
- over_800_change_1w: 0.36
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.14,,64.78,,63.47,,0,False,False
20260508,66.71,0.57,65.29,0.51,63.57,0.1,1,True,True
20260515,65.64,-1.07,63.78,-1.51,62.49,-1.08,0,False,False
20260522,65.7,0.06,64.14,0.36,62.49,0,1,False,True
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
| 20260528 | 2630 | 亞航 | 16 | 0 | 17610.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
