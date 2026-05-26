# INDIVIDUAL STOCK CHATGPT PACKET - 6024 群益期

## Metadata
- generated_at: 2026-05-26 21:26:11 Asia/Taipei
- stock_id: 6024
- stock_name: 群益期
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6024_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6024_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6024_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6024_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6024_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6024_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6024_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6024_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6024_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6024_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6024_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6024_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6024_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6024.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6024.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6024.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6024.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6024.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6024.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6024_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6024_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6024_latest.md?ref=main

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
- open: 55.8
- high: 56.3
- low: 55.5
- close: 56.2
- volume: 334657
- ma5: 56.18
- ema23_primary: 56.42
- distance_to_ema23_pct: -0.4
- ma20: 56.75
- ma60: 55.66
- ma120: 53.42
- return_5d: 0.36
- return_20d: 1.26
- volume_ratio: 0.81
- distance_to_ma20_pct_auxiliary: -0.97
- distance_to_high_60_pct: -4.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,55.5,56.3,55.4,56,408149,55.67,0.59,56.15,54.06,1.03
20260429,56,56,55.6,55.7,171942,55.67,0.05,56.17,54.14,0.46
20260430,56.1,56.5,55.7,56.2,281993,55.72,0.86,56.18,54.21,0.84
20260504,56.2,57.6,56.2,57.1,987529,55.83,2.27,56.22,54.3,2.66
20260505,56.8,57.8,56.8,57.2,376617,55.95,2.24,56.28,54.38,1
20260506,57.6,57.9,57.2,57.6,346085,56.09,2.7,56.32,54.48,0.93
20260507,57.6,58.3,57.4,58.2,732302,56.26,3.45,56.36,54.58,1.88
20260508,58.4,58.4,57.9,58.2,258284,56.42,3.15,56.45,54.68,0.69
20260511,58.2,59,57.8,58.2,448579,56.57,2.88,56.52,54.8,1.16
20260512,58.2,58.2,57.1,57.5,639890,56.65,1.5,56.56,54.91,1.62
20260513,57.3,57.4,56.7,57.2,399047,56.69,0.89,56.6,55.01,1.01
20260514,57.2,57.3,56.3,56.5,609230,56.68,-0.31,56.59,55.1,1.46
20260515,56.6,57.3,56.5,56.5,226562,56.66,-0.29,56.59,55.19,0.55
20260518,56.2,56.5,55.9,56,284577,56.61,-1.07,56.57,55.28,0.69
20260519,56,56.5,55.9,56,162876,56.56,-0.99,56.56,55.36,0.4
20260520,55.9,56.2,55.7,55.8,244308,56.49,-1.23,56.56,55.41,0.61
20260521,56,56.6,56,56.6,274950,56.5,0.17,56.62,55.48,0.7
20260522,56.6,56.6,56.2,56.5,358520,56.5,-0.01,56.68,55.55,0.93
20260525,56.3,56.4,55.7,55.8,750860,56.44,-1.14,56.72,55.6,1.82
20260526,55.8,56.3,55.5,56.2,334657,56.42,-0.4,56.75,55.66,0.81
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.36
- over_600_ratio: 65.78
- over_800_ratio: 64.98
- over_1000_ratio: 63.94
- over_400_change_1w: -0.05
- over_800_change_1w: 0.01
- over_1000_change_1w: -0.36
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.93,,64.13,,63.81,,0,False,False
20260508,68.4,0.47,64.93,0.8,63.87,0.06,1,True,True
20260515,68.41,0.01,64.97,0.04,64.3,0.43,2,True,True
20260522,68.36,-0.05,64.98,0.01,63.94,-0.36,3,False,True
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
