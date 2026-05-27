# INDIVIDUAL STOCK CHATGPT PACKET - 4807 日成-KY

## Metadata
- generated_at: 2026-05-27 21:27:30 Asia/Taipei
- stock_id: 4807
- stock_name: 日成-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4807_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4807_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4807_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4807_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4807_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4807_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4807_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4807_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4807_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4807_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4807_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4807_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4807_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4807.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4807.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4807.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4807.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4807.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4807.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4807_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4807_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4807_latest.md?ref=main

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
- open: 24
- high: 25.65
- low: 23.35
- close: 25.05
- volume: 715904
- ma5: 23.62
- ema23_primary: 21.98
- distance_to_ema23_pct: 13.97
- ma20: 22.91
- ma60: 18.18
- ma120: 18.07
- return_5d: 10.35
- return_20d: 45.64
- volume_ratio: 1.6
- distance_to_ma20_pct_auxiliary: 9.32
- distance_to_high_60_pct: -9.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,17.25,18.9,17.25,18.9,438246,15.92,18.72,15.32,16.53,3.35
20260430,19.1,20.75,18.8,20.75,873708,16.32,27.13,15.64,16.57,5.19
20260504,20.95,22.8,20.9,22.8,974367,16.86,35.22,16.06,16.64,4.6
20260505,23,23.8,21.45,21.45,789586,17.24,24.39,16.42,16.7,3.18
20260506,21.55,23.1,20.6,21.35,450342,17.59,21.4,16.77,16.76,1.68
20260507,21.5,21.5,20.6,21.1,189228,17.88,18.01,17.11,16.81,0.69
20260508,20.6,21.65,20.55,21.55,147157,18.18,18.5,17.48,16.87,0.52
20260511,21.3,23.7,21.25,23.7,504384,18.64,27.11,17.95,16.97,1.66
20260512,23.7,25.75,23.4,25.6,544305,19.22,33.17,18.45,17.09,1.7
20260513,24.45,25.6,24.2,25.05,170866,19.71,27.09,18.95,17.21,0.54
20260514,27.5,27.55,25.2,25.2,759528,20.17,24.96,19.45,17.34,2.17
20260515,26.05,26.05,24,24.1,395569,20.5,17.59,19.91,17.44,1.08
20260518,23.1,23.9,22.8,23.35,239916,20.73,12.62,20.3,17.53,0.64
20260519,23.7,23.95,22.6,22.6,272151,20.89,8.19,20.66,17.61,0.71
20260520,23.3,24.35,22.7,22.7,236341,21.04,7.89,21.04,17.69,0.6
20260521,22.4,24.5,22.4,22.9,268142,21.19,8.05,21.43,17.78,0.67
20260522,22.95,23.7,22.85,22.95,160414,21.34,7.54,21.81,17.87,0.4
20260525,23.7,24,22.95,23.85,214442,21.55,10.67,22.2,17.97,0.53
20260526,24.45,25.65,23.05,23.35,608809,21.7,7.6,22.52,18.06,1.45
20260527,24,25.65,23.35,25.05,715904,21.98,13.97,22.91,18.18,1.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.82
- over_600_ratio: 69.45
- over_800_ratio: 65.13
- over_1000_ratio: 63.36
- over_400_change_1w: -1.01
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.84,,65.15,,63.38,,0,False,False
20260508,73.01,1.17,65.15,0,63.38,0,1,False,False
20260515,73.83,0.82,65.15,0,63.38,0,2,False,False
20260522,72.82,-1.01,65.13,-0.02,63.36,-0.02,0,False,False
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
