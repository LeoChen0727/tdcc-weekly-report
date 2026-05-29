# INDIVIDUAL STOCK CHATGPT PACKET - 3703 欣陸

## Metadata
- generated_at: 2026-05-29 19:32:43 Asia/Taipei
- stock_id: 3703
- stock_name: 欣陸
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3703_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3703_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3703_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3703_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3703_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3703_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3703_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3703_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3703_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3703_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3703_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3703_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3703_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3703.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3703.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3703.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3703.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3703.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3703.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3703_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3703_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3703_latest.md?ref=main

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
- open: 20.1
- high: 20.3
- low: 20.05
- close: 20.2
- volume: 1366687
- ma5: 20.16
- ema23_primary: 20.48
- distance_to_ema23_pct: -1.38
- ma20: 20.32
- ma60: 21.45
- ma120: 22.14
- return_5d: 0.25
- return_20d: -2.65
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -0.61
- distance_to_high_60_pct: -13.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,20.75,20.8,20.5,20.55,1382845,21.51,-4.47,21.59,22.21,1.21
20260505,20.55,20.65,20.4,20.45,1261488,21.42,-4.54,21.5,22.16,1.06
20260506,20.6,20.6,20.45,20.55,1091670,21.35,-3.75,21.41,22.12,0.9
20260507,20.5,21,20.5,20.9,965520,21.31,-1.94,21.35,22.08,0.8
20260508,20.95,20.95,20.5,20.7,1216574,21.26,-2.64,21.27,22.05,0.97
20260511,20.7,20.85,20.55,20.75,1102490,21.22,-2.21,21.2,22.02,0.87
20260512,20.8,20.8,20.45,20.5,1868901,21.16,-3.11,21.11,21.98,1.45
20260513,20.5,20.5,20.1,20.3,1186040,21.09,-3.73,21.02,21.95,0.9
20260514,20.25,20.3,20.1,20.15,1127009,21.01,-4.09,20.92,21.91,0.86
20260515,20.2,20.3,20.05,20.1,1330866,20.93,-3.98,20.82,21.86,1.01
20260518,20.1,20.1,19.9,20.1,1492926,20.86,-3.66,20.74,21.82,1.14
20260519,20.05,20.3,19.95,20.1,696325,20.8,-3.37,20.67,21.77,0.58
20260520,20.1,20.2,19.9,20.1,1121883,20.74,-3.1,20.6,21.72,0.93
20260521,20.25,20.3,20.1,20.3,814944,20.71,-1.96,20.55,21.68,0.69
20260522,20.2,20.25,20,20.15,1129863,20.66,-2.46,20.5,21.64,1
20260525,20.25,20.25,19.8,20.05,2509105,20.61,-2.71,20.45,21.6,2.09
20260526,20,20.5,20,20.4,1649640,20.59,-0.93,20.44,21.56,1.37
20260527,20.45,20.45,20,20.1,3816104,20.55,-2.19,20.4,21.53,2.78
20260528,20.1,20.3,20,20.05,1500795,20.51,-2.23,20.35,21.49,1.07
20260529,20.1,20.3,20.05,20.2,1366687,20.48,-1.38,20.32,21.45,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.09
- over_600_ratio: 69.78
- over_800_ratio: 69.12
- over_1000_ratio: 68.36
- over_400_change_1w: -0.15
- over_800_change_1w: -0.36
- over_1000_change_1w: -0.48
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.35,,69.66,,68.91,,0,False,False
20260508,72.38,0.03,69.63,-0.03,69,0.09,1,False,True
20260515,72.24,-0.14,69.48,-0.15,68.84,-0.16,0,False,False
20260522,72.09,-0.15,69.12,-0.36,68.36,-0.48,0,False,False
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
