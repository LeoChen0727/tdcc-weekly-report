# INDIVIDUAL STOCK CHATGPT PACKET - 1712 興農

## Metadata
- generated_at: 2026-05-30 23:41:07 Asia/Taipei
- stock_id: 1712
- stock_name: 興農
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1712_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1712_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1712_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1712_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1712_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1712_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1712_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1712_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1712_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1712_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1712_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1712_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1712_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1712.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1712.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1712.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1712.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1712.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1712.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1712_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1712_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1712_latest.md?ref=main

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
- open: 38.85
- high: 39.1
- low: 38.5
- close: 38.9
- volume: 1469112
- ma5: 39.18
- ema23_primary: 40.7
- distance_to_ema23_pct: -4.42
- ma20: 40.74
- ma60: 43.01
- ma120: 43.88
- return_5d: -2.51
- return_20d: -7.82
- volume_ratio: 1.54
- distance_to_ma20_pct_auxiliary: -4.52
- distance_to_high_60_pct: -19.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,42.2,42.35,42.05,42.15,481095,42.93,-1.82,42.62,44.69,0.77
20260505,41.7,42.15,41.7,41.95,419428,42.85,-2.1,42.54,44.61,0.69
20260506,41.95,42.2,41.9,42.15,384307,42.79,-1.5,42.47,44.55,0.63
20260507,42,42.45,41.9,42.3,787779,42.75,-1.06,42.43,44.48,1.28
20260508,42.2,42.2,41.8,41.95,700589,42.68,-1.72,42.38,44.42,1.1
20260511,41.95,41.95,41.1,41.45,1346490,42.58,-2.66,42.33,44.35,2.07
20260512,41.5,41.5,41.2,41.3,859270,42.48,-2.77,42.25,44.29,1.28
20260513,41.3,41.45,41.15,41.45,820909,42.39,-2.22,42.18,44.22,1.2
20260514,41.45,41.45,41.25,41.25,357050,42.29,-2.47,42.13,44.14,0.54
20260515,41.3,41.45,40.9,40.9,945539,42.18,-3.03,42.03,44.04,1.39
20260518,40.8,40.95,40.65,40.8,588562,42.06,-3,41.94,43.95,0.86
20260519,40.8,41.1,40.6,40.65,653513,41.95,-3.09,41.84,43.86,0.94
20260520,40.65,40.65,40.5,40.5,697084,41.83,-3.17,41.73,43.76,0.99
20260521,40.6,40.75,40.2,40.2,1337103,41.69,-3.57,41.62,43.67,1.79
20260522,40.2,40.2,39.75,39.9,1645403,41.54,-3.95,41.51,43.58,2.1
20260525,39.9,39.95,39.3,39.4,1799523,41.36,-4.74,41.38,43.47,2.14
20260526,39.4,39.75,39.2,39.2,992370,41.18,-4.81,41.24,43.37,1.17
20260527,39.25,39.6,39.05,39.55,1035166,41.05,-3.65,41.1,43.27,1.2
20260528,39.55,39.55,38.85,38.85,1775199,40.86,-4.93,40.91,43.14,1.92
20260529,38.85,39.1,38.5,38.9,1469112,40.7,-4.42,40.74,43.01,1.54
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 57.35
- over_600_ratio: 53.05
- over_800_ratio: 49.05
- over_1000_ratio: 46.7
- over_400_change_1w: -0.31
- over_800_change_1w: 0.06
- over_1000_change_1w: -0.14
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.23,,49.65,,46.87,,0,False,False
20260508,58.12,-0.11,49.19,-0.46,47.04,0.17,1,False,True
20260515,57.86,-0.26,49.12,-0.07,46.76,-0.28,2,False,False
20260522,57.66,-0.2,48.99,-0.13,46.84,0.08,3,False,True
20260529,57.35,-0.31,49.05,0.06,46.7,-0.14,4,False,True
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
