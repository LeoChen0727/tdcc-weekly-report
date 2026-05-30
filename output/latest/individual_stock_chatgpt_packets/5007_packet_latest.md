# INDIVIDUAL STOCK CHATGPT PACKET - 5007 三星

## Metadata
- generated_at: 2026-05-30 23:42:34 Asia/Taipei
- stock_id: 5007
- stock_name: 三星
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5007_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5007_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5007_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5007_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5007_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5007_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5007_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5007_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5007_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5007_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5007_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5007_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5007_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5007.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5007.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5007.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5007.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5007.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5007.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5007_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5007_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5007_latest.md?ref=main

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
- open: 57.6
- high: 57.8
- low: 57.5
- close: 57.8
- volume: 64528
- ma5: 57.3
- ema23_primary: 57.22
- distance_to_ema23_pct: 1.01
- ma20: 57.26
- ma60: 57.05
- ma120: 56.89
- return_5d: 1.76
- return_20d: 0
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 0.94
- distance_to_high_60_pct: -2.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,57.8,57.8,57.6,57.8,16121,57.62,0.31,57.44,57.73,0.24
20260505,57.4,58,57.4,57.9,4502,57.64,0.44,57.56,57.75,0.07
20260506,58,58.5,57.3,58.3,96808,57.7,1.04,57.72,57.76,1.41
20260507,57.9,58.1,57.6,58,36682,57.72,0.48,57.78,57.75,0.56
20260508,58.4,58.4,57.6,58,45413,57.75,0.44,57.86,57.71,0.68
20260511,58,58.1,57.8,58,26783,57.77,0.4,57.92,57.68,0.4
20260512,58,58,57.2,57.5,49255,57.75,-0.43,57.95,57.66,0.73
20260513,57,58,56.9,58,19301,57.77,0.4,57.94,57.64,0.3
20260514,57.3,57.3,56,57,66161,57.7,-1.22,57.91,57.6,0.99
20260515,56.6,57,56.1,57,29157,57.64,-1.12,57.88,57.56,0.45
20260518,57,57,56,56.7,132165,57.57,-1.5,57.84,57.52,1.89
20260519,56.6,56.6,55.9,56.2,27302,57.45,-2.18,57.74,57.47,0.4
20260520,56.2,56.2,55.3,55.3,101784,57.27,-3.44,57.6,57.41,1.51
20260521,55.5,56.5,55.5,56.2,277129,57.18,-1.72,57.52,57.36,3.48
20260522,57,57,56.2,56.8,62863,57.15,-0.61,57.43,57.29,1.06
20260525,57,57.4,56.7,56.7,44839,57.11,-0.72,57.37,57.21,0.77
20260526,56.7,57,56.4,57,48097,57.1,-0.18,57.31,57.14,0.82
20260527,57,57.4,56.5,57.4,95022,57.13,0.47,57.28,57.08,1.53
20260528,57.8,57.8,56.8,57.6,70124,57.17,0.76,57.26,57.05,1.08
20260529,57.6,57.8,57.5,57.8,64528,57.22,1.01,57.26,57.05,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 87.78
- over_600_ratio: 86.18
- over_800_ratio: 84.49
- over_1000_ratio: 84.19
- over_400_change_1w: 0.17
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.51,,84,,84,,0,False,False
20260508,87.52,0.01,84.01,0.01,84.01,0.01,1,True,True
20260515,87.53,0.01,84.02,0.01,84.02,0.01,2,True,True
20260522,87.61,0.08,84.32,0.3,84.02,0,3,False,True
20260529,87.78,0.17,84.49,0.17,84.19,0.17,4,True,True
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
