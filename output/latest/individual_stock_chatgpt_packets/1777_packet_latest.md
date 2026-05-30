# INDIVIDUAL STOCK CHATGPT PACKET - 1777 生泰

## Metadata
- generated_at: 2026-05-30 23:41:09 Asia/Taipei
- stock_id: 1777
- stock_name: 生泰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1777_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1777_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1777_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1777_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1777_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1777_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1777_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1777_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1777_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1777_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1777_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1777_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1777_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1777.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1777.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1777.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1777.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1777.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1777.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1777_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1777_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1777_latest.md?ref=main

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
- open: 71.3
- high: 72.1
- low: 71.1
- close: 71.7
- volume: 72000
- ma5: 71.48
- ema23_primary: 71.31
- distance_to_ema23_pct: 0.54
- ma20: 71.22
- ma60: 71.45
- ma120: 72.52
- return_5d: 0.28
- return_20d: 1.13
- volume_ratio: 1.9
- distance_to_ma20_pct_auxiliary: 0.67
- distance_to_high_60_pct: -2.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,71,71,70.2,70.6,41000,71.23,-0.89,71.2,71.77,1.44
20260505,71.4,71.4,70.1,71.2,18000,71.23,-0.04,71.16,71.74,0.62
20260506,70.4,71.1,70,70.9,27000,71.2,-0.42,71.09,71.71,0.9
20260507,70.9,70.9,70.5,70.6,20000,71.15,-0.77,71.03,71.67,0.71
20260508,70.9,71.9,70.9,71.9,35000,71.21,0.96,71.05,71.66,1.23
20260511,71.9,71.9,71,71.1,22000,71.2,-0.15,71.03,71.65,0.77
20260512,71.1,71.8,71.1,71.3,11000,71.21,0.12,71.05,71.64,0.4
20260513,71.1,71.4,70.9,71,15000,71.19,-0.27,71.05,71.62,0.6
20260514,71,71,70,70.7,49000,71.15,-0.64,71.04,71.6,1.91
20260515,70.7,70.8,70.5,70.7,29000,71.12,-0.58,71.03,71.57,1.21
20260518,70.2,71.4,70.2,71.4,13000,71.14,0.37,71,71.58,0.56
20260519,71.4,72,71.4,71.4,29000,71.16,0.34,71.02,71.57,1.23
20260520,71.8,71.8,71.2,71.3,11000,71.17,0.18,71.03,71.57,0.47
20260521,71.9,71.9,71.3,71.4,11000,71.19,0.29,71.03,71.57,0.47
20260522,71,71.9,71,71.5,71000,71.22,0.4,71.06,71.57,2.85
20260525,71.5,71.7,71.2,71.5,72000,71.24,0.36,71.09,71.55,2.58
20260526,71.5,71.5,71.1,71.3,71000,71.25,0.08,71.12,71.51,2.39
20260527,71.1,72,71,71.4,71000,71.26,0.2,71.15,71.48,2.21
20260528,71.4,71.6,71.3,71.5,71000,71.28,0.31,71.18,71.47,2.02
20260529,71.3,72.1,71.1,71.7,72000,71.31,0.54,71.22,71.45,1.9
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 60.18
- over_600_ratio: 57.06
- over_800_ratio: 55.59
- over_1000_ratio: 51.67
- over_400_change_1w: 0.08
- over_800_change_1w: 1.8
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.96,,53.79,,51.67,,0,False,False
20260508,59.95,-0.01,53.79,0,51.67,0,0,False,False
20260515,60,0.05,53.79,0,51.67,0,1,False,False
20260522,60.1,0.1,53.79,0,51.67,0,2,False,False
20260529,60.18,0.08,55.59,1.8,51.67,0,3,False,True
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
