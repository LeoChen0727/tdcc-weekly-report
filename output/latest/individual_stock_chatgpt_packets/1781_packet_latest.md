# INDIVIDUAL STOCK CHATGPT PACKET - 1781 合世

## Metadata
- generated_at: 2026-05-27 21:26:20 Asia/Taipei
- stock_id: 1781
- stock_name: 合世
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1781_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1781_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1781_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1781_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1781_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1781_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1781_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1781_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1781_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1781_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1781_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1781_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1781_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1781.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1781.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1781.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1781.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1781.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1781.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1781_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1781_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1781_latest.md?ref=main

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
- date: 20260527
- open: 11
- high: 11
- low: 10.55
- close: 10.6
- volume: 11000
- ma5: 10.78
- ema23_primary: 10.83
- distance_to_ema23_pct: -2.11
- ma20: 10.69
- ma60: 11.54
- ma120: 11.68
- return_5d: 0.95
- return_20d: -4.5
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: -0.84
- distance_to_high_60_pct: -16.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,11.15,11.15,10.75,11,51000,11.54,-4.69,11.58,12.19,1.1
20260430,11,11,10.8,10.8,27000,11.48,-5.92,11.51,12.17,0.59
20260504,10.85,10.85,10.8,10.8,13000,11.42,-5.45,11.44,12.15,0.29
20260505,10.85,11,10.7,10.95,47000,11.38,-3.81,11.38,12.12,1.02
20260506,10.95,10.95,10.75,10.8,20000,11.33,-4.72,11.31,12.08,0.43
20260507,10.75,10.8,10.65,10.75,75000,11.29,-4.75,11.25,12.03,1.51
20260508,10.8,10.95,10.75,10.85,34000,11.25,-3.55,11.19,12,0.68
20260511,10.85,10.85,10.75,10.85,62000,11.22,-3.27,11.14,11.96,1.2
20260512,10.85,10.85,10.7,10.7,72000,11.17,-4.24,11.09,11.93,1.36
20260513,10.7,10.7,10.55,10.55,75000,11.12,-5.14,11.04,11.88,1.67
20260514,10.55,10.55,10.5,10.5,30000,11.07,-5.15,10.99,11.84,0.67
20260515,10.4,10.5,10.3,10.4,40000,11.01,-5.57,10.93,11.81,0.91
20260518,10.35,10.35,10.15,10.25,62000,10.95,-6.39,10.86,11.77,1.39
20260519,10.25,10.45,10.2,10.2,21000,10.89,-6.32,10.81,11.72,0.49
20260520,10.25,10.5,10.25,10.5,25000,10.86,-3.27,10.77,11.69,0.59
20260521,10.45,10.65,10.45,10.55,44000,10.83,-2.58,10.73,11.66,1.05
20260522,10.9,11.1,10.9,11,11000,10.84,1.44,10.73,11.63,0.27
20260525,11,11,10.9,10.9,11000,10.85,0.47,10.72,11.6,0.27
20260526,10.9,10.9,10.65,10.85,11000,10.85,0.01,10.71,11.57,0.29
20260527,11,11,10.55,10.6,11000,10.83,-2.11,10.69,11.54,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.58
- over_600_ratio: 33.57
- over_800_ratio: 30.6
- over_1000_ratio: 28.77
- over_400_change_1w: 0.89
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.8,,32.31,,28.79,,0,False,False
20260508,40.81,0.01,30.63,-1.68,28.8,0.01,1,False,True
20260515,41.69,0.88,30.61,-0.02,28.78,-0.02,2,False,False
20260522,42.58,0.89,30.6,-0.01,28.77,-0.01,3,False,False
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
