# INDIVIDUAL STOCK CHATGPT PACKET - 6103 合邦

## Metadata
- generated_at: 2026-05-30 23:42:48 Asia/Taipei
- stock_id: 6103
- stock_name: 合邦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 194
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6103_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6103_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6103_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6103_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6103_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6103_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6103_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6103_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6103_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6103_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6103_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6103_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6103_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6103.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6103.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6103.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6103.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6103.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6103.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6103_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6103_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6103_latest.md?ref=main

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
- open: 39.5
- high: 39.5
- low: 38
- close: 38
- volume: 39000
- ma5: 37.11
- ema23_primary: 39.01
- distance_to_ema23_pct: -2.58
- ma20: 38.73
- ma60: 40.43
- ma120: 39.21
- return_5d: 0.26
- return_20d: -2.56
- volume_ratio: 3.5
- distance_to_ma20_pct_auxiliary: -1.87
- distance_to_high_60_pct: -30.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260421,39.1,39.1,39.1,39.1,1000,42.08,-7.07,43.42,40.2,0.11
20260422,39.5,39.6,39.5,39.6,2000,41.87,-5.42,43.12,40.23,0.23
20260423,39.7,39.7,39.6,39.6,3000,41.68,-4.99,42.83,40.26,0.35
20260428,38.3,38.3,38.3,38.3,1000,41.4,-7.48,42.4,40.26,0.13
20260430,38.3,39.7,38.3,39.7,2000,41.26,-3.77,41.96,40.29,0.28
20260505,39.7,39.7,39.6,39.6,4000,41.12,-3.69,41.52,40.32,0.56
20260506,39.6,39.6,39.6,39.6,1000,40.99,-3.4,41.05,40.34,0.14
20260507,40,40,39.7,39.7,4000,40.88,-2.9,40.72,40.37,0.57
20260508,39.7,40,39.7,40,2000,40.81,-1.99,40.6,40.4,0.28
20260511,40,40,40,40,2000,40.74,-1.82,40.63,40.44,0.3
20260512,40,40,40,40,3000,40.68,-1.67,40.46,40.47,0.46
20260513,40,40,38,39.1,10000,40.55,-3.57,40.3,40.49,1.89
20260514,39.1,39.1,39.1,39.1,1000,40.43,-3.29,40.17,40.51,0.2
20260515,37.65,37.65,37.65,37.65,1000,40.2,-6.34,40.09,40.5,0.2
20260518,37.9,37.9,37.9,37.9,1000,40.01,-5.26,39.83,40.5,0.24
20260522,36.2,36.2,36.2,36.2,36000,39.69,-8.79,39.44,40.47,6.67
20260525,37.15,37.15,37.15,37.15,37000,39.48,-5.89,39.25,40.46,5.83
20260526,37.2,37.2,37.2,37.2,37000,39.29,-5.31,39.02,40.44,4.62
20260528,35.15,37,35.15,37,36000,39.1,-5.36,38.77,40.43,3.73
20260529,39.5,39.5,38,38,39000,39.01,-2.58,38.73,40.43,3.5
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 91.11
- over_600_ratio: 83.84
- over_800_ratio: 83.84
- over_1000_ratio: 83.84
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
20260430,91.11,,83.84,,83.84,,0,False,False
20260508,91.11,0,83.84,0,83.84,0,0,False,False
20260515,91.11,0,83.84,0,83.84,0,0,False,False
20260522,91.11,0,83.84,0,83.84,0,0,False,False
20260529,91.11,0,83.84,0,83.84,0,0,False,False
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
