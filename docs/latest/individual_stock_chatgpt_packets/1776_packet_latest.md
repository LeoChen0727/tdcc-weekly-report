# INDIVIDUAL STOCK CHATGPT PACKET - 1776 展宇

## Metadata
- generated_at: 2026-05-28 20:18:26 Asia/Taipei
- stock_id: 1776
- stock_name: 展宇
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1776_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1776_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1776_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1776_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1776_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1776_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1776_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1776_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1776_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1776_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1776_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1776_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1776_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1776.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1776.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1776.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1776.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1776.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1776.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1776_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1776_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1776_latest.md?ref=main

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
- open: 18.15
- high: 18.6
- low: 18.1
- close: 18.15
- volume: 154413
- ma5: 18.43
- ema23_primary: 17.65
- distance_to_ema23_pct: 2.82
- ma20: 17.71
- ma60: 16.46
- ma120: 15.86
- return_5d: 0
- return_20d: 10.33
- volume_ratio: 0.4
- distance_to_ma20_pct_auxiliary: 2.5
- distance_to_high_60_pct: -11.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,16.5,16.7,16.45,16.5,82140,16.17,2.01,16.16,15.67,0.88
20260504,16.55,16.85,16.55,16.8,200619,16.23,3.53,16.21,15.69,1.98
20260505,16.9,17.2,16.85,17.15,155020,16.3,5.19,16.29,15.72,1.46
20260506,17.5,17.55,16.9,16.95,111406,16.36,3.62,16.37,15.74,1.01
20260507,17.2,17.45,16.95,17.35,175771,16.44,5.53,16.46,15.77,1.5
20260508,17.25,17.25,16.95,17,81402,16.49,3.11,16.52,15.8,0.7
20260511,17.25,17.3,16.85,16.85,89773,16.52,2.02,16.57,15.82,0.75
20260512,17,17,16.55,16.85,41551,16.54,1.84,16.6,15.85,0.37
20260513,16.85,17,16.7,17,227641,16.58,2.52,16.64,15.88,1.88
20260514,17.5,18.7,17.5,18.7,800623,16.76,11.58,16.76,15.94,5.1
20260515,19.15,20.55,19,19,3474091,16.95,12.12,16.9,16,10.67
20260518,18.9,18.9,17.55,18.1,429443,17.04,6.21,17,16.05,1.24
20260519,18,18.25,17.7,17.7,275469,17.1,3.53,17.05,16.1,0.79
20260520,17.75,18.3,17.75,17.9,157157,17.16,4.29,17.09,16.15,0.45
20260521,17.95,18.5,17.95,18.15,197917,17.25,5.24,17.17,16.2,0.56
20260522,18.2,19.15,18.2,18.95,411051,17.39,8.98,17.3,16.26,1.14
20260525,19.15,19.3,18.5,18.6,347388,17.49,6.35,17.43,16.32,0.93
20260526,18.8,18.8,18.05,18.3,157474,17.56,4.23,17.54,16.36,0.42
20260527,18.2,18.6,18.1,18.15,132727,17.61,3.09,17.62,16.41,0.35
20260528,18.15,18.6,18.1,18.15,154413,17.65,2.82,17.71,16.46,0.4
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.69
- over_600_ratio: 60.32
- over_800_ratio: 50.91
- over_1000_ratio: 43.59
- over_400_change_1w: -1.06
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.24,,52,,43.24,,0,False,False
20260508,67.23,-0.01,52,0,43.24,0,0,False,False
20260515,67.75,0.52,50.91,-1.09,43.59,0.35,1,False,True
20260522,66.69,-1.06,50.91,0,43.59,0,0,False,False
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
| status |
| --- |
| no rows |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
