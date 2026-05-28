# INDIVIDUAL STOCK CHATGPT PACKET - 0061 元大寶滬深

## Metadata
- generated_at: 2026-05-28 19:31:21 Asia/Taipei
- stock_id: 0061
- stock_name: 元大寶滬深
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 
- tdcc_rows: 0
- tdcc_history_status: tdcc_missing
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history missing

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/0061_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/0061_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/0061_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/0061_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/0061_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/0061_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/0061_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/0061_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/0061_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/0061_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/0061_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/0061_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/0061_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/0061.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/0061.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/0061.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/0061.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/0061.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/0061.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/0061_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/0061_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/0061_latest.md?ref=main

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
- open: 25
- high: 25
- low: 24.74
- close: 24.75
- volume: 225893
- ma5: 24.86
- ema23_primary: 24.73
- distance_to_ema23_pct: 0.09
- ma20: 24.9
- ma60: 24.05
- ma120: 23.63
- return_5d: -0.96
- return_20d: 1.98
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -0.61
- distance_to_high_60_pct: -3.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,24.39,24.51,24.38,24.4,167788,23.93,1.95,23.89,23.63,0.58
20260504,24.41,24.7,24.41,24.62,432180,23.99,2.62,23.96,23.64,1.42
20260505,24.64,24.76,24.55,24.59,273132,24.04,2.29,24.04,23.66,0.87
20260506,24.55,24.96,24.55,24.95,789037,24.12,3.46,24.15,23.68,2.26
20260507,24.99,25.08,24.84,24.92,129123,24.18,3.05,24.22,23.71,0.38
20260508,24.86,24.97,24.69,24.82,186776,24.24,2.41,24.29,23.73,0.55
20260511,24.82,25.19,24.82,25.17,414601,24.31,3.52,24.36,23.75,1.2
20260512,25.28,25.37,25.2,25.3,323923,24.4,3.7,24.44,23.79,0.92
20260513,25.3,25.44,25.23,25.42,446258,24.48,3.83,24.51,23.82,1.3
20260514,25.5,25.7,25.21,25.34,236567,24.55,3.2,24.57,23.86,0.69
20260515,25.32,25.32,24.89,25,199777,24.59,1.67,24.61,23.88,0.58
20260518,25,25,24.74,24.8,289870,24.61,0.78,24.65,23.91,0.87
20260519,24.8,24.8,24.6,24.65,145887,24.61,0.16,24.68,23.92,0.44
20260520,24.7,24.86,24.7,24.79,160870,24.63,0.67,24.71,23.94,0.49
20260521,24.79,25.27,24.79,24.99,307281,24.66,1.35,24.74,23.96,1.01
20260522,24.88,24.88,24.6,24.69,279022,24.66,0.12,24.77,23.98,0.93
20260525,24.79,24.99,24.79,24.83,325822,24.67,0.63,24.8,23.99,1.09
20260526,24.83,25.1,24.83,24.96,377629,24.7,1.06,24.84,24.01,1.25
20260527,25.02,25.28,24.98,25.05,396438,24.73,1.31,24.88,24.03,1.31
20260528,25,25,24.74,24.75,225893,24.73,0.09,24.9,24.05,0.74
```

## Latest TDCC Snapshot
- as_of_date: 
- over_400_ratio: 
- over_600_ratio: 
- over_800_ratio: 
- over_1000_ratio: 
- over_400_change_1w: 
- over_800_change_1w: 
- over_1000_change_1w: 
- tdcc_consecutive_up_weeks: 
- all_thresholds_up: 
- high_thresholds_up: 

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
status,no_rows
no_rows,True
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
