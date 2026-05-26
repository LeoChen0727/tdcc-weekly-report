# INDIVIDUAL STOCK CHATGPT PACKET - 2514 龍邦

## Metadata
- generated_at: 2026-05-26 23:00:48 Asia/Taipei
- stock_id: 2514
- stock_name: 龍邦
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2514_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2514_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2514_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2514_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2514_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2514_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2514_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2514_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2514_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2514_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2514_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2514_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2514_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2514.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2514.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2514.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2514.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2514.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2514.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2514_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2514_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2514_latest.md?ref=main

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
- open: 12.95
- high: 12.95
- low: 12.85
- close: 12.95
- volume: 104477
- ma5: 12.97
- ema23_primary: 13.16
- distance_to_ema23_pct: -1.57
- ma20: 13.14
- ma60: 13.52
- ma120: 14.18
- return_5d: -0.38
- return_20d: -2.63
- volume_ratio: 0.39
- distance_to_ma20_pct_auxiliary: -1.43
- distance_to_high_60_pct: -13.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.4,13.4,13.1,13.25,198894,13.51,-1.9,13.44,14.07,1.05
20260429,13.35,13.4,13.2,13.25,91174,13.49,-1.74,13.43,14.04,0.48
20260430,13.3,13.3,13.2,13.3,65150,13.47,-1.26,13.43,14.02,0.34
20260504,13.35,13.4,13.2,13.25,233233,13.45,-1.5,13.41,13.99,1.18
20260505,13.25,13.35,13.2,13.25,54146,13.43,-1.37,13.4,13.96,0.28
20260506,13.3,13.35,13.2,13.35,50105,13.43,-0.58,13.39,13.93,0.27
20260507,13.25,13.35,13.2,13.25,882982,13.41,-1.21,13.38,13.9,3.99
20260508,13.35,13.35,13.15,13.25,217515,13.4,-1.11,13.37,13.87,0.96
20260511,13.35,13.35,13.25,13.3,620909,13.39,-0.68,13.36,13.84,2.47
20260512,13.3,13.3,13.1,13.1,272512,13.37,-1.99,13.34,13.81,1.04
20260513,13.1,13.2,13.1,13.15,69436,13.35,-1.49,13.32,13.79,0.27
20260514,13.1,13.2,13.05,13.05,192864,13.32,-2.05,13.3,13.76,0.76
20260515,13.1,13.15,13,13.1,702313,13.31,-1.54,13.28,13.73,2.46
20260518,13,13.1,12.95,13.05,125483,13.28,-1.76,13.26,13.7,0.45
20260519,13.2,13.2,12.95,13,93940,13.26,-1.96,13.23,13.68,0.36
20260520,13.1,13.1,12.85,13,399893,13.24,-1.8,13.22,13.65,1.49
20260521,13.05,13.05,12.9,13,372595,13.22,-1.65,13.2,13.62,1.34
20260522,12.95,13,12.85,12.95,110731,13.2,-1.87,13.18,13.59,0.4
20260525,12.95,12.95,12.75,12.95,505824,13.18,-1.71,13.15,13.55,1.71
20260526,12.95,12.95,12.85,12.95,104477,13.16,-1.57,13.14,13.52,0.39
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 88.22
- over_600_ratio: 87.4
- over_800_ratio: 85.84
- over_1000_ratio: 84.73
- over_400_change_1w: 0.01
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.2,,86.01,,84.68,,0,False,False
20260508,88.2,0,86.19,0.18,84.87,0.19,1,False,True
20260515,88.21,0.01,85.99,-0.2,84.88,0.01,2,False,True
20260522,88.22,0.01,85.84,-0.15,84.73,-0.15,3,False,False
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
