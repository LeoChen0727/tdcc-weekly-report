# INDIVIDUAL STOCK CHATGPT PACKET - 9929 秋雨

## Metadata
- generated_at: 2026-05-26 22:20:57 Asia/Taipei
- stock_id: 9929
- stock_name: 秋雨
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 128
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9929_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9929_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9929_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9929_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9929_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9929_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9929_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9929_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9929_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9929_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9929_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9929_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9929_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9929.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9929.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9929.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9929.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9929.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9929.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9929_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9929_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9929_latest.md?ref=main

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
- open: 11.9
- high: 12
- low: 11.85
- close: 11.85
- volume: 9389
- ma5: 11.53
- ema23_primary: 11.72
- distance_to_ema23_pct: 1.07
- ma20: 11.66
- ma60: 11.78
- ma120: 11.18
- return_5d: 1.72
- return_20d: 3.95
- volume_ratio: 0.35
- distance_to_ma20_pct_auxiliary: 1.63
- distance_to_high_60_pct: -21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,11.45,11.8,11.45,11.65,3029,12.07,-3.52,12.24,11.45,0.06
20260429,11.9,11.9,11.2,11.45,9706,12.02,-4.76,12.18,11.47,0.22
20260430,11.6,11.6,11,11.2,11818,11.95,-6.31,12.16,11.48,0.29
20260504,10.9,11.1,10.9,10.95,35431,11.87,-7.75,12.08,11.49,0.96
20260505,10.9,11.9,10.85,11.65,40231,11.85,-1.7,12.03,11.5,1.17
20260506,11.9,11.9,11.5,11.85,26964,11.85,-0.02,12.03,11.52,0.8
20260507,12.15,12.75,12.1,12.6,93302,11.91,5.76,12.04,11.56,2.54
20260508,13,13,11.55,12.45,79225,11.96,4.11,12.05,11.59,2.09
20260511,12.35,12.35,12,12,12074,11.96,0.32,12.04,11.61,0.33
20260512,12,12,11.8,11.8,10255,11.95,-1.25,12.02,11.62,0.28
20260513,12.45,12.45,11.9,11.9,29105,11.94,-0.37,12.01,11.64,0.84
20260514,11.75,11.9,11.5,11.5,23101,11.91,-3.42,11.96,11.65,0.71
20260515,11.05,11.45,11.05,11.45,13562,11.87,-3.53,11.86,11.67,0.45
20260518,11,11.45,11,11.45,8352,11.83,-3.25,11.8,11.69,0.31
20260519,11.4,11.65,11,11.65,24215,11.82,-1.43,11.76,11.7,0.93
20260520,11.45,11.5,11.05,11.4,31226,11.78,-3.26,11.71,11.72,1.21
20260521,11.4,11.4,11.1,11.4,50000,11.75,-3,11.67,11.73,1.81
20260522,11.4,11.4,11.25,11.4,25095,11.72,-2.75,11.64,11.74,0.88
20260525,11.3,11.6,11.3,11.6,4954,11.71,-0.96,11.64,11.76,0.18
20260526,11.9,12,11.85,11.85,9389,11.72,1.07,11.66,11.78,0.35
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 87.97
- over_600_ratio: 84.47
- over_800_ratio: 83.86
- over_1000_ratio: 83.86
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
20260430,87.97,,83.86,,83.86,,0,False,False
20260508,87.97,0,83.86,0,83.86,0,0,False,False
20260515,87.97,0,83.86,0,83.86,0,0,False,False
20260522,87.97,0,83.86,0,83.86,0,0,False,False
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
