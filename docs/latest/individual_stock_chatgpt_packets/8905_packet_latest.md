# INDIVIDUAL STOCK CHATGPT PACKET - 8905 裕國

## Metadata
- generated_at: 2026-05-28 19:33:53 Asia/Taipei
- stock_id: 8905
- stock_name: 裕國
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 128
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8905_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8905_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8905_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8905_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8905_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8905_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8905_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8905_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8905_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8905_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8905_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8905_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8905_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8905.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8905.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8905.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8905.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8905.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8905.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8905_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8905_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8905_latest.md?ref=main

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
- open: 29.8
- high: 30
- low: 29.35
- close: 30
- volume: 9108
- ma5: 30.11
- ema23_primary: 33.04
- distance_to_ema23_pct: -9.21
- ma20: 33.21
- ma60: 37.4
- ma120: 34.96
- return_5d: 1.69
- return_20d: -23.18
- volume_ratio: 0.44
- distance_to_ma20_pct_auxiliary: -9.67
- distance_to_high_60_pct: -27.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,40,40,38.65,39.75,13000,39.66,0.23,39.94,38.46,0.63
20260430,41.1,41.1,40.75,40.75,2000,39.75,2.52,39.96,38.6,0.11
20260504,40.05,40.05,39.35,39.35,33000,39.72,-0.92,39.93,38.71,1.83
20260505,38.95,38.95,38.3,38.3,14000,39.6,-3.28,39.82,38.81,0.77
20260506,38.3,38.3,37.1,38.3,16000,39.49,-3.01,39.76,38.92,0.86
20260507,37.05,38.15,37.05,38.15,7000,39.38,-3.12,39.64,39.03,0.39
20260508,39.45,39.45,36.4,36.6,31000,39.15,-6.5,39.45,39.11,1.75
20260511,37.85,37.85,33,33,61000,38.63,-14.58,39.09,39.07,3.05
20260512,33,33,31,31.5,45000,38.04,-17.19,38.66,39.01,2.12
20260513,30.8,30.8,29.2,29.7,33000,37.34,-20.47,38.16,38.9,1.46
20260514,29.95,29.95,29.1,29.35,27000,36.68,-19.98,37.63,38.8,1.15
20260515,29.35,29.9,29.35,29.7,11000,36.1,-17.72,37.1,38.65,0.53
20260518,28.8,29.85,28.8,29.55,11000,35.55,-16.88,36.55,38.49,0.57
20260519,28.85,30.2,28.85,30.2,5000,35.11,-13.97,36.06,38.34,0.26
20260520,30.2,30.2,29.2,29.5,5000,34.64,-14.83,35.53,38.19,0.26
20260521,29.2,29.55,29.2,29.55,2000,34.21,-13.63,35.01,38.02,0.11
20260522,29.15,30.3,29.15,30.3,30000,33.89,-10.59,34.55,37.87,1.55
20260525,30.3,31,30.1,31,31000,33.65,-7.87,34.13,37.73,1.49
20260527,30.15,31.2,29.6,29.7,30000,33.32,-10.86,33.66,37.56,1.41
20260528,29.8,30,29.35,30,9108,33.04,-9.21,33.21,37.4,0.44
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 92.37
- over_600_ratio: 91.19
- over_800_ratio: 89.57
- over_1000_ratio: 88.78
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
20260430,92.4,,89.57,,88.78,,0,False,False
20260508,92.4,0,89.57,0,88.78,0,0,False,False
20260515,92.37,-0.03,89.57,0,88.78,0,0,False,False
20260522,92.37,0,89.57,0,88.78,0,0,False,False
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
