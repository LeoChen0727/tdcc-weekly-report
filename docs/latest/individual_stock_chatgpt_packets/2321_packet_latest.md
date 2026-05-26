# INDIVIDUAL STOCK CHATGPT PACKET - 2321 東訊

## Metadata
- generated_at: 2026-05-26 23:00:35 Asia/Taipei
- stock_id: 2321
- stock_name: 東訊
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 94
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2321_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2321_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2321_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2321_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2321_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2321_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2321_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2321_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2321_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2321_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2321_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2321_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2321_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2321.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2321.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2321.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2321.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2321.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2321.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2321_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2321_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2321_latest.md?ref=main

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
- open: 12.95
- high: 14.3
- low: 12.95
- close: 14.3
- volume: 23964
- ma5: 13.16
- ema23_primary: 13.29
- distance_to_ema23_pct: 7.6
- ma20: 12.96
- ma60: 14.68
- ma120: 15.62
- return_5d: 13.49
- return_20d: 7.52
- volume_ratio: 2.18
- distance_to_ma20_pct_auxiliary: 10.38
- distance_to_high_60_pct: -17.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260422,12.4,13.5,12.4,12.9,48602,14.45,-10.72,14.51,16.01,2.44
20260423,12.65,12.8,12.3,12.8,8478,14.31,-10.56,14.37,15.94,0.42
20260424,12.8,12.95,12.8,12.95,3413,14.2,-8.79,14.21,15.87,0.17
20260429,12.95,12.95,12.8,12.9,6168,14.09,-8.44,14.02,15.81,0.31
20260430,12.9,13.2,12.9,13.2,3272,14.02,-5.82,13.85,15.75,0.16
20260504,13.15,13.15,13.05,13.05,2547,13.94,-6.35,13.75,15.67,0.14
20260505,12.6,12.85,12.6,12.85,6573,13.84,-7.18,13.65,15.6,0.36
20260506,13,13,13,13,2640,13.77,-5.62,13.56,15.54,0.15
20260507,13,13,12.4,13,15559,13.71,-5.18,13.47,15.49,0.87
20260508,13,13,12.35,12.35,14000,13.6,-9.17,13.36,15.44,0.75
20260511,13,13,12.5,12.85,7832,13.53,-5.06,13.26,15.36,0.42
20260512,12.5,13,12.3,12.95,15777,13.49,-3.97,13.22,15.29,0.84
20260513,12.85,13.1,12.5,13.1,7162,13.45,-2.63,13.13,15.22,0.39
20260514,12.8,13,12.8,12.8,8010,13.4,-4.47,13.06,15.14,0.43
20260515,12.55,12.85,12.55,12.6,5804,13.33,-5.49,12.98,15.04,0.31
20260518,12.95,13.5,12.6,13,13111,13.3,-2.29,12.95,14.95,0.75
20260519,13,13,12.55,12.7,5301,13.25,-4.18,12.94,14.87,0.33
20260522,13,13,12.8,12.8,15230,13.22,-3.15,12.92,14.79,0.94
20260525,12.4,13,12.4,13,6084,13.2,-1.5,12.9,14.72,0.41
20260526,12.95,14.3,12.95,14.3,23964,13.29,7.6,12.96,14.68,2.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.73
- over_600_ratio: 70.73
- over_800_ratio: 70.73
- over_1000_ratio: 67.91
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.58,,70.58,,67.91,,0,False,False
20260508,70.62,0.04,70.62,0.04,67.91,0,1,False,True
20260515,70.71,0.09,70.71,0.09,67.91,0,2,False,True
20260522,70.73,0.02,70.73,0.02,67.91,0,3,False,True
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
