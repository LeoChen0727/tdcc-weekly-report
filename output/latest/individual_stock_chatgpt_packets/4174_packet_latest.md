# INDIVIDUAL STOCK CHATGPT PACKET - 4174 浩鼎

## Metadata
- generated_at: 2026-05-30 23:42:18 Asia/Taipei
- stock_id: 4174
- stock_name: 浩鼎
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 268
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4174_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4174_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4174_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4174_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4174_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4174_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4174_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4174_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4174_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4174_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4174_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4174_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4174_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4174.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4174.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4174.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4174.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4174.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4174.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4174_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4174_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4174_latest.md?ref=main

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
- open: 28.35
- high: 28.9
- low: 28.3
- close: 28.6
- volume: 29000
- ma5: 29.05
- ema23_primary: 31.93
- distance_to_ema23_pct: -10.42
- ma20: 32.08
- ma60: 35.6
- ma120: 33.37
- return_5d: -9.64
- return_20d: -10.2
- volume_ratio: 0.08
- distance_to_ma20_pct_auxiliary: -10.85
- distance_to_high_60_pct: -30.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,32.05,32.5,31.65,31.7,330000,35.14,-9.8,35.73,37.72,0.69
20260505,31.85,34.85,31.8,34.85,1215000,35.12,-0.76,35.58,37.85,2.29
20260506,34.4,37.3,34.3,35.25,2014000,35.13,0.34,35.39,38.01,3.26
20260507,35.35,35.45,34.8,34.8,467000,35.1,-0.86,35.18,38.17,0.75
20260508,35.15,35.5,33.7,34.05,431000,35.01,-2.75,34.99,38.32,0.69
20260511,34,34.2,33.25,33.35,359000,34.88,-4.37,34.76,38.44,0.57
20260512,33.6,33.7,32.6,32.8,279000,34.7,-5.48,34.52,38.53,0.45
20260513,32.25,33.35,32.25,32.7,624000,34.54,-5.31,34.27,38.23,0.98
20260514,32.8,33.4,32.5,33,284000,34.41,-4.09,34.01,37.96,0.46
20260515,33.5,33.6,32.5,32.5,433000,34.25,-5.11,33.74,37.68,0.69
20260518,32.4,32.85,31.45,32.45,284000,34.1,-4.83,33.47,37.42,0.46
20260519,32.45,33.25,32.45,32.5,271000,33.97,-4.31,33.26,37.18,0.45
20260520,33,33.05,32.3,32.35,208000,33.83,-4.38,33.04,36.97,0.35
20260521,32.45,32.55,32.2,32.4,249000,33.71,-3.89,32.84,36.77,0.42
20260522,32.3,32.6,31.55,31.65,32000,33.54,-5.63,32.77,36.6,0.06
20260525,31.95,31.95,30.35,30.35,31000,33.27,-8.79,32.72,36.42,0.06
20260526,30.45,30.7,29.3,29.45,30000,32.96,-10.64,32.59,36.21,0.07
20260527,29.3,29.45,28.6,28.65,29000,32.6,-12.11,32.42,35.99,0.07
20260528,28.7,28.85,28.05,28.2,28000,32.23,-12.5,32.24,35.79,0.07
20260529,28.35,28.9,28.3,28.6,29000,31.93,-10.42,32.08,35.6,0.08
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 43.46
- over_600_ratio: 39.83
- over_800_ratio: 37.7
- over_1000_ratio: 35.55
- over_400_change_1w: 0.5
- over_800_change_1w: -0.64
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.69,,38.04,,35.18,,0,False,False
20260508,42.64,-0.05,38.6,0.56,35.1,-0.08,1,False,True
20260515,42.93,0.29,38.24,-0.36,35.35,0.25,2,False,True
20260522,42.96,0.03,38.34,0.1,35.54,0.19,3,True,True
20260529,43.46,0.5,37.7,-0.64,35.55,0.01,4,False,True
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
