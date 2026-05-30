# INDIVIDUAL STOCK CHATGPT PACKET - 3713 新晶投控

## Metadata
- generated_at: 2026-05-30 23:42:14 Asia/Taipei
- stock_id: 3713
- stock_name: 新晶投控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3713_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3713_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3713_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3713_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3713_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3713_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3713_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3713_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3713_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3713_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3713_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3713_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3713_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3713.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3713.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3713.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3713.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3713.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3713.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3713_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3713_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3713_latest.md?ref=main

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
- open: 17
- high: 17
- low: 15.3
- close: 15.75
- volume: 16000
- ma5: 14.84
- ema23_primary: 14.42
- distance_to_ema23_pct: 9.2
- ma20: 14.03
- ma60: 15.58
- ma120: 18.48
- return_5d: 21.62
- return_20d: 6.06
- volume_ratio: 0.17
- distance_to_ma20_pct_auxiliary: 12.28
- distance_to_high_60_pct: -19.23

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,14.8,14.9,14.5,14.9,68000,15.62,-4.6,15.16,17.41,0.36
20260505,14.6,14.6,14.3,14.45,102000,15.52,-6.9,15.18,17.3,0.64
20260506,14.55,14.55,14.2,14.45,58000,15.43,-6.36,15.2,17.2,0.39
20260507,14.5,14.55,13.9,14.1,187000,15.32,-7.97,15.2,17.09,1.26
20260508,14.05,14.05,13.5,13.7,320000,15.19,-9.79,15.19,16.98,2
20260511,13.7,14.2,13.5,14.2,132000,15.1,-5.98,15.2,16.89,0.81
20260512,14.2,14.35,13.7,14.2,57000,15.03,-5.51,15.18,16.81,0.36
20260513,14.15,14.15,13.4,13.85,154000,14.93,-7.24,15.07,16.72,1.09
20260514,13.9,14.15,13.55,13.8,85000,14.84,-6.98,14.91,16.61,0.7
20260515,13.55,13.55,12.95,13.25,287000,14.7,-9.89,14.74,16.5,2.28
20260518,13,13.2,12.5,13.2,152000,14.58,-9.46,14.59,16.4,1.23
20260519,13.2,13.3,13.1,13.3,64000,14.47,-8.1,14.45,16.3,0.54
20260520,13.35,13.35,12.75,13,44000,14.35,-9.4,14.33,16.2,0.38
20260521,13,13.1,12.75,13,104000,14.24,-8.69,14.19,16.09,0.9
20260522,13,13,12.7,12.95,13000,14.13,-8.35,14.04,15.97,0.11
20260525,12.95,13,12.75,12.95,13000,14.03,-7.71,13.93,15.86,0.13
20260526,12.95,14.2,12.95,14.2,14000,14.05,1.1,13.9,15.76,0.14
20260527,14.6,15.6,14.6,15.6,15000,14.18,10.05,13.94,15.7,0.15
20260528,14.05,16.7,14.05,15.7,15000,14.3,9.77,13.98,15.64,0.15
20260529,17,17,15.3,15.75,16000,14.42,9.2,14.03,15.58,0.17
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 55.83
- over_600_ratio: 46.95
- over_800_ratio: 45.41
- over_1000_ratio: 42.35
- over_400_change_1w: 0.03
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.72,,45.32,,42.34,,0,False,False
20260508,55.74,0.02,45.34,0.02,42.34,0,1,False,True
20260515,55.76,0.02,45.36,0.02,42.34,0,2,False,True
20260522,55.8,0.04,45.38,0.02,42.34,0,3,False,True
20260529,55.83,0.03,45.41,0.03,42.35,0.01,4,True,True
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
