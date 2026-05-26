# INDIVIDUAL STOCK CHATGPT PACKET - 2069 運錩

## Metadata
- generated_at: 2026-05-26 23:00:31 Asia/Taipei
- stock_id: 2069
- stock_name: 運錩
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2069_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2069_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2069_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2069_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2069_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2069_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2069_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2069_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2069_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2069_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2069_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2069_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2069_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2069.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2069.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2069.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2069.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2069.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2069.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2069_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2069_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2069_latest.md?ref=main

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
- open: 19.85
- high: 19.85
- low: 19.35
- close: 19.4
- volume: 411097
- ma5: 19.38
- ema23_primary: 19.31
- distance_to_ema23_pct: 0.48
- ma20: 19.36
- ma60: 18.91
- ma120: 18.52
- return_5d: 1.04
- return_20d: 3.74
- volume_ratio: 0.85
- distance_to_ma20_pct_auxiliary: 0.19
- distance_to_high_60_pct: -7.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,18.7,19.1,18.65,19.1,421793,18.74,1.91,18.68,18.93,1.55
20260429,19.2,19.35,19,19.1,400385,18.77,1.75,18.68,18.93,1.44
20260430,19.1,19.1,18.75,18.8,209248,18.77,0.14,18.7,18.93,0.76
20260504,18.65,18.8,18.5,18.5,369011,18.75,-1.34,18.7,18.91,1.3
20260505,18.45,18.65,18.4,18.55,212279,18.73,-0.99,18.7,18.89,0.75
20260506,18.6,19.05,18.55,18.75,401061,18.74,0.07,18.71,18.88,1.36
20260507,18.75,19,18.45,18.9,462236,18.75,0.8,18.72,18.86,1.49
20260508,19.6,20,19.4,19.6,908234,18.82,4.14,18.76,18.84,2.59
20260511,19.8,20.95,19.8,20.45,1218345,18.96,7.88,18.86,18.83,3.02
20260512,20.75,20.75,19.95,20.2,584575,19.06,5.98,18.95,18.83,1.39
20260513,20.2,20.2,19.8,20,384395,19.14,4.5,19.02,18.84,0.89
20260514,20.05,20.25,19.9,20,513638,19.21,4.11,19.1,18.84,1.16
20260515,20.2,20.2,19.6,19.7,453035,19.25,2.33,19.16,18.85,1
20260518,19.6,19.85,19.35,19.5,515408,19.27,1.18,19.21,18.86,1.11
20260519,19.5,19.6,19.15,19.2,379463,19.27,-0.34,19.24,18.87,0.81
20260520,19.15,19.35,19.15,19.35,194170,19.27,0.4,19.25,18.88,0.44
20260521,19.55,19.6,19.3,19.4,205655,19.28,0.6,19.27,18.89,0.47
20260522,19.3,19.55,19.15,19.2,655340,19.28,-0.4,19.29,18.9,1.47
20260525,19.2,20,19.2,19.55,825279,19.3,1.3,19.33,18.9,1.72
20260526,19.85,19.85,19.35,19.4,411097,19.31,0.48,19.36,18.91,0.85
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.27
- over_600_ratio: 58.58
- over_800_ratio: 54.32
- over_1000_ratio: 53.32
- over_400_change_1w: -0.21
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.02,,54.31,,53.31,,0,False,False
20260508,61.49,0.47,54.35,0.04,53.35,0.04,1,True,True
20260515,61.48,-0.01,54.35,0,53.35,0,2,False,False
20260522,61.27,-0.21,54.32,-0.03,53.32,-0.03,0,False,False
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
