# INDIVIDUAL STOCK CHATGPT PACKET - 1457 宜進

## Metadata
- generated_at: 2026-05-28 19:31:32 Asia/Taipei
- stock_id: 1457
- stock_name: 宜進
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1457_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1457_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1457_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1457_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1457_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1457_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1457_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1457_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1457_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1457_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1457_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1457_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1457_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1457.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1457.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1457.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1457.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1457.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1457.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1457_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1457_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1457_latest.md?ref=main

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
- open: 13.95
- high: 13.95
- low: 13.85
- close: 13.95
- volume: 104716
- ma5: 13.95
- ema23_primary: 14.27
- distance_to_ema23_pct: -2.23
- ma20: 14.21
- ma60: 14.95
- ma120: 15.29
- return_5d: -0.71
- return_20d: -4.45
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: -1.86
- distance_to_high_60_pct: -14.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,14.75,14.75,14.4,14.45,165791,14.93,-3.23,14.86,15.31,0.85
20260504,14.45,14.45,14.35,14.35,131395,14.88,-3.58,14.83,15.3,0.69
20260505,14.35,14.45,14.3,14.45,151618,14.85,-2.68,14.81,15.29,0.8
20260506,14.45,14.6,14.45,14.6,215701,14.83,-1.53,14.79,15.27,1.23
20260507,14.5,14.55,14.4,14.55,119069,14.8,-1.71,14.75,15.25,0.74
20260508,14.65,14.65,14.5,14.5,99567,14.78,-1.88,14.71,15.24,0.65
20260511,14.45,14.55,14.4,14.45,198751,14.75,-2.04,14.69,15.22,1.47
20260512,14.4,14.4,14.25,14.3,175641,14.71,-2.81,14.66,15.21,1.24
20260513,14.3,14.35,14.25,14.3,62549,14.68,-2.58,14.63,15.2,0.45
20260514,14.25,14.5,14.2,14.2,138038,14.64,-3,14.59,15.19,0.99
20260515,14.25,14.25,14.05,14.05,300560,14.59,-3.7,14.54,15.17,2.05
20260518,14.15,14.15,14.05,14.05,92536,14.54,-3.4,14.5,15.15,0.64
20260519,14.05,14.15,14.05,14.1,63163,14.51,-2.81,14.46,15.14,0.44
20260520,14.15,14.15,14.05,14.15,91337,14.48,-2.27,14.42,15.13,0.64
20260521,14.05,14.1,14.05,14.05,107145,14.44,-2.72,14.38,15.11,0.74
20260522,14.1,14.1,14,14.05,153555,14.41,-2.5,14.35,15.09,1.06
20260525,14.1,14.1,13.7,13.85,332845,14.36,-3.57,14.31,15.05,2.15
20260526,13.85,13.95,13.8,13.95,183677,14.33,-2.64,14.28,15.02,1.2
20260527,13.9,14,13.8,13.95,135580,14.3,-2.43,14.25,14.98,0.87
20260528,13.95,13.95,13.85,13.95,104716,14.27,-2.23,14.21,14.95,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.83
- over_600_ratio: 71.66
- over_800_ratio: 69.66
- over_1000_ratio: 67.63
- over_400_change_1w: 0.04
- over_800_change_1w: 0.05
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.73,,69.32,,67.62,,0,False,False
20260508,74.75,0.02,69.33,0.01,67.63,0.01,1,True,True
20260515,74.79,0.04,69.61,0.28,67.63,0,2,False,True
20260522,74.83,0.04,69.66,0.05,67.63,0,3,False,True
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
