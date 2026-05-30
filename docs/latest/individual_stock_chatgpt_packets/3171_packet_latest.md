# INDIVIDUAL STOCK CHATGPT PACKET - 3171 炎洲流通

## Metadata
- generated_at: 2026-05-30 23:41:54 Asia/Taipei
- stock_id: 3171
- stock_name: 炎洲流通
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3171_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3171_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3171_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3171_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3171_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3171_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3171_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3171_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3171_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3171_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3171_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3171_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3171_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3171.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3171.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3171.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3171.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3171.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3171.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3171_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3171_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3171_latest.md?ref=main

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
- open: 70.3
- high: 70.7
- low: 69.5
- close: 70.1
- volume: 70000
- ma5: 70.1
- ema23_primary: 68.34
- distance_to_ema23_pct: 2.58
- ma20: 68.31
- ma60: 65.01
- ma120: 56.49
- return_5d: 2.94
- return_20d: 1.45
- volume_ratio: 1.09
- distance_to_ma20_pct_auxiliary: 2.62
- distance_to_high_60_pct: -5.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,70,70,68.4,68.9,104000,66.98,2.87,68.41,58.88,0.65
20260505,69,70.2,68.8,68.8,30000,67.13,2.49,68.53,59.22,0.19
20260506,69,69.8,68.6,69.5,27000,67.33,3.23,68.69,59.59,0.18
20260507,69.5,69.5,67.2,67.3,53000,67.33,-0.04,68.66,59.91,0.36
20260508,65.7,66,63.1,64,114000,67.05,-4.55,68.39,60.18,0.78
20260511,70.4,70.4,66.3,67.6,175000,67.09,0.75,68.26,60.49,1.16
20260512,66.9,67.9,64.5,67.2,122000,67.1,0.14,68,60.82,0.86
20260513,70.6,70.6,68.5,68.5,102000,67.22,1.91,67.89,61.16,0.76
20260514,68.6,70,68.5,69,13000,67.37,2.42,67.92,61.51,0.1
20260515,70.3,70.3,67.5,67.9,35000,67.41,0.72,68,61.84,0.33
20260518,66.8,67.8,65.6,67.7,25000,67.44,0.39,68.07,62.17,0.24
20260519,67.9,67.9,67,67.5,14000,67.44,0.09,68.23,62.5,0.15
20260520,66.8,67.7,66.5,66.8,38000,67.39,-0.87,68.28,62.79,0.44
20260521,66.8,67.4,66.6,66.9,15000,67.35,-0.66,68.17,63.08,0.19
20260522,68.9,68.9,66.8,68.1,68000,67.41,1.02,68.09,63.39,0.9
20260525,71.6,73.7,70,70.9,72000,67.7,4.73,68.13,63.73,1.02
20260526,70.8,71,70,70.5,70000,67.93,3.78,68.25,64.08,1.03
20260527,71.8,72.9,70,70.2,71000,68.12,3.05,68.27,64.41,1.06
20260528,71.4,71.5,68.8,68.8,70000,68.18,0.91,68.26,64.7,1.05
20260529,70.3,70.7,69.5,70.1,70000,68.34,2.58,68.31,65.01,1.09
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 76.93
- over_600_ratio: 76.93
- over_800_ratio: 74.76
- over_1000_ratio: 71.98
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.51,,74.34,,71.56,,0,False,False
20260508,76.93,0.42,74.76,0.42,71.98,0.42,1,True,True
20260515,76.93,0,74.76,0,71.98,0,0,False,False
20260522,76.93,0,74.76,0,71.98,0,0,False,False
20260529,76.93,0,74.76,0,71.98,0,0,False,False
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
