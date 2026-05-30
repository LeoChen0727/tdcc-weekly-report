# INDIVIDUAL STOCK CHATGPT PACKET - 2064 晉椿

## Metadata
- generated_at: 2026-05-30 23:41:15 Asia/Taipei
- stock_id: 2064
- stock_name: 晉椿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 258
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2064_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2064_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2064_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2064_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2064_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2064_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2064_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2064_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2064_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2064_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2064_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2064_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2064_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2064.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2064.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2064.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2064.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2064.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2064.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2064_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2064_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2064_latest.md?ref=main

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
- open: 13.75
- high: 14.05
- low: 13.75
- close: 13.8
- volume: 14000
- ma5: 13.54
- ema23_primary: 12.89
- distance_to_ema23_pct: 7.06
- ma20: 12.91
- ma60: 12.2
- ma120: 11.98
- return_5d: 5.75
- return_20d: 18.97
- volume_ratio: 0.45
- distance_to_ma20_pct_auxiliary: 6.85
- distance_to_high_60_pct: -1.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,11.5,12,11.5,11.95,55000,11.72,1.94,11.7,11.9,1.12
20260505,11.95,12,11.75,11.8,27000,11.73,0.61,11.69,11.91,0.77
20260506,12,12.05,11.85,12.05,39000,11.76,2.5,11.71,11.91,1.64
20260507,12.05,12.8,12.05,12.8,110000,11.84,8.08,11.76,11.92,3.81
20260508,13.6,13.6,12.6,12.8,27000,11.92,7.36,11.81,11.93,0.9
20260511,12.7,12.8,12.55,12.6,52000,11.98,5.19,11.86,11.95,1.62
20260512,12.5,12.95,12.5,12.95,47000,12.06,7.38,11.91,11.96,1.39
20260513,12.75,12.8,12.55,12.8,33000,12.12,5.6,11.96,11.97,0.94
20260514,12.85,12.85,12.75,12.8,32000,12.18,5.11,12.02,11.98,0.89
20260515,12.85,12.85,12.8,12.85,33000,12.23,5.04,12.08,11.99,0.88
20260518,12.85,12.9,12.85,12.9,4000,12.29,4.97,12.14,12.01,0.11
20260519,12.85,12.9,12.85,12.9,21000,12.34,4.53,12.2,12.02,0.56
20260520,13.15,13.2,13.05,13.1,12000,12.4,5.61,12.27,12.04,0.34
20260521,13.1,13.25,12.8,13.25,45000,12.47,6.22,12.35,12.06,1.31
20260522,13.1,13.7,12.85,13.05,13000,12.52,4.21,12.42,12.08,0.41
20260525,13.1,13.3,12.85,13.3,13000,12.59,5.66,12.51,12.1,0.41
20260526,13.15,13.4,13.15,13.4,13000,12.65,5.89,12.6,12.13,0.41
20260527,13.55,13.55,13.4,13.45,13000,12.72,5.73,12.7,12.15,0.41
20260528,13.6,13.75,13.55,13.75,14000,12.81,7.37,12.8,12.17,0.44
20260529,13.75,14.05,13.75,13.8,14000,12.89,7.06,12.91,12.2,0.45
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 82.5
- over_600_ratio: 73.18
- over_800_ratio: 73.18
- over_1000_ratio: 71.94
- over_400_change_1w: 0.2
- over_800_change_1w: 0.19
- over_1000_change_1w: 0.19
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,81.74,,72.44,,71.2,,0,False,False
20260508,82.04,0.3,72.73,0.29,71.49,0.29,1,True,True
20260515,82.19,0.15,72.88,0.15,71.64,0.15,2,True,True
20260522,82.3,0.11,72.99,0.11,71.75,0.11,3,True,True
20260529,82.5,0.2,73.18,0.19,71.94,0.19,4,True,True
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
