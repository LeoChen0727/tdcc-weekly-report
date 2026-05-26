# INDIVIDUAL STOCK CHATGPT PACKET - 5864 致和證

## Metadata
- generated_at: 2026-05-26 23:54:25 Asia/Taipei
- stock_id: 5864
- stock_name: 致和證
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5864_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5864_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5864_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5864_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5864_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5864_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5864_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5864_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5864_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5864_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5864_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5864_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5864_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5864.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5864.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5864.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5864.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5864.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5864.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5864_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5864_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5864_latest.md?ref=main

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
- open: 34
- high: 35.45
- low: 33.45
- close: 35.1
- volume: 35000
- ma5: 33.14
- ema23_primary: 31.03
- distance_to_ema23_pct: 13.13
- ma20: 31.77
- ma60: 27.09
- ma120: 22.56
- return_5d: 13.23
- return_20d: 29.52
- volume_ratio: 0.01
- distance_to_ma20_pct_auxiliary: 10.5
- distance_to_high_60_pct: -7.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,27.3,27.5,26.85,27.4,2757000,25.15,8.94,24.77,24.28,0.94
20260429,27.2,27.6,26.95,27.45,2074000,25.34,8.32,24.95,24.41,0.71
20260430,27.65,28.75,27.4,28.5,5173000,25.61,11.31,25.21,24.53,1.68
20260504,29.3,30.3,29,30,5397000,25.97,15.51,25.52,24.66,1.64
20260505,29.95,30.8,29.8,30.4,3300000,26.34,15.41,25.86,24.79,0.97
20260506,30.85,31.2,30.45,31.2,4081000,26.75,16.66,26.23,24.93,1.16
20260507,34.25,34.3,33.1,34.3,10137000,27.38,25.3,26.75,25.1,2.68
20260508,35.75,35.75,34.3,34.9,9314000,28,24.63,27.33,25.29,2.24
20260511,35.85,37.75,35.7,36.7,8531000,28.73,27.75,27.95,25.5,1.91
20260512,36.9,36.9,33.7,33.85,10765000,29.15,16.11,28.46,25.68,2.19
20260513,33.3,33.5,31.8,31.9,6215000,29.38,8.57,28.81,25.82,1.23
20260514,32.6,32.75,30.5,30.8,6100000,29.5,4.4,29.08,25.95,1.17
20260515,31.05,31.95,29.85,30.2,6376000,29.56,2.17,29.33,26.06,1.17
20260518,29.85,31.05,29.5,31,4667000,29.68,4.45,29.66,26.2,0.85
20260519,31,31.75,30.55,31,3431000,29.79,4.06,29.96,26.33,0.62
20260520,31.5,31.9,30.9,31.35,3811000,29.92,4.78,30.26,26.47,0.68
20260521,31.95,32.35,31.45,32.3,4912000,30.12,7.25,30.62,26.62,0.85
20260522,32.6,33.4,32.35,33.2,33000,30.37,9.3,31,26.79,0.01
20260525,33.8,34.8,33.7,33.75,34000,30.66,10.09,31.36,26.95,0.01
20260526,34,35.45,33.45,35.1,35000,31.03,13.13,31.77,27.09,0.01
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.54
- over_600_ratio: 68.19
- over_800_ratio: 64.5
- over_1000_ratio: 62.89
- over_400_change_1w: -0.84
- over_800_change_1w: -0.91
- over_1000_change_1w: -0.92
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.53,,66.13,,64.24,,0,False,False
20260508,73.85,1.32,67.05,0.92,65.25,1.01,1,True,True
20260515,72.38,-1.47,65.41,-1.64,63.81,-1.44,0,False,False
20260522,71.54,-0.84,64.5,-0.91,62.89,-0.92,0,False,False
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
