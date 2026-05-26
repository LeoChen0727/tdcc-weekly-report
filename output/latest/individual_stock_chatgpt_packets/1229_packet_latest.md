# INDIVIDUAL STOCK CHATGPT PACKET - 1229 聯華

## Metadata
- generated_at: 2026-05-26 22:17:59 Asia/Taipei
- stock_id: 1229
- stock_name: 聯華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1229_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1229_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1229_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1229_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1229_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1229_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1229_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1229_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1229_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1229_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1229_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1229_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1229_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1229.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1229.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1229.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1229.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1229.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1229.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1229_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1229_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1229_latest.md?ref=main

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
- open: 39.3
- high: 40.2
- low: 39.2
- close: 39.9
- volume: 4698930
- ma5: 38.85
- ema23_primary: 40.48
- distance_to_ema23_pct: -1.44
- ma20: 40.3
- ma60: 42.89
- ma120: 44.81
- return_5d: 3.23
- return_20d: -4.32
- volume_ratio: 1.31
- distance_to_ma20_pct_auxiliary: -1
- distance_to_high_60_pct: -15.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,41.7,42.05,41.65,41.8,2167167,43.68,-4.31,43.95,44.62,0.81
20260429,42.2,42.2,41.75,41.9,1754382,43.54,-3.76,43.81,44.55,0.66
20260430,41.7,42,41.3,41.3,3003240,43.35,-4.73,43.62,44.47,1.14
20260504,41.3,41.4,41.05,41.25,3744010,43.17,-4.46,43.45,44.38,1.37
20260505,41.3,41.85,41.25,41.6,2304314,43.04,-3.35,43.28,44.29,0.83
20260506,41.6,41.6,41.15,41.35,3059182,42.9,-3.62,43.09,44.2,1.06
20260507,41.35,41.75,41.15,41.7,3190981,42.8,-2.57,42.94,44.12,1.08
20260508,41.75,42.35,41.75,42.15,3007407,42.75,-1.4,42.81,44.05,0.99
20260511,42.1,42.1,41,41.1,5460594,42.61,-3.54,42.65,43.96,1.7
20260512,41.2,41.2,40.35,40.5,4754538,42.43,-4.56,42.46,43.88,1.43
20260513,40.15,40.5,39.7,40.3,4180833,42.26,-4.63,42.28,43.8,1.22
20260514,40.3,40.6,39.8,39.95,3408595,42.06,-5.03,42.09,43.71,0.98
20260515,39.95,40,39.3,39.45,5492819,41.85,-5.73,41.84,43.61,1.5
20260518,39.3,39.3,38.75,38.8,4305252,41.59,-6.71,41.56,43.51,1.15
20260519,38.8,39.4,38.55,38.65,3206788,41.35,-6.52,41.31,43.41,0.87
20260520,38.65,38.65,38.25,38.3,3565313,41.09,-6.8,41.04,43.29,0.96
20260521,38.35,39,38.35,38.85,1873714,40.91,-5.03,40.81,43.18,0.51
20260522,38.9,39.05,38.55,38.7,3163692,40.72,-4.97,40.59,43.08,0.88
20260525,38.7,38.95,38,38.5,5426303,40.54,-5.03,40.39,42.97,1.49
20260526,39.3,40.2,39.2,39.9,4698930,40.48,-1.44,40.3,42.89,1.31
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.03
- over_600_ratio: 63.69
- over_800_ratio: 62.88
- over_1000_ratio: 61.97
- over_400_change_1w: -0.05
- over_800_change_1w: -0.13
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.37,,63.22,,62.42,,0,False,False
20260508,65.39,0.02,63.24,0.02,62.39,-0.03,1,False,True
20260515,65.08,-0.31,63.01,-0.23,62.17,-0.22,0,False,False
20260522,65.03,-0.05,62.88,-0.13,61.97,-0.2,0,False,False
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
