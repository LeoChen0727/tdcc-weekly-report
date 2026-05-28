# INDIVIDUAL STOCK CHATGPT PACKET - 6113 亞矽

## Metadata
- generated_at: 2026-05-28 20:19:52 Asia/Taipei
- stock_id: 6113
- stock_name: 亞矽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6113_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6113_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6113_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6113_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6113_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6113_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6113_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6113_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6113_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6113_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6113_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6113_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6113_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6113.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6113.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6113.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6113.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6113.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6113.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6113_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6113_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6113_latest.md?ref=main

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
- open: 27
- high: 27.9
- low: 26.2
- close: 26.2
- volume: 27000
- ma5: 26.9
- ema23_primary: 24.77
- distance_to_ema23_pct: 5.77
- ma20: 24.75
- ma60: 22.43
- ma120: 21.8
- return_5d: 3.35
- return_20d: 16.19
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 5.85
- distance_to_high_60_pct: -6.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,22.65,23.6,22.4,22.5,222000,22.11,1.78,22.05,21.43,0.44
20260504,22.8,23.65,22.55,23.45,437000,22.22,5.54,22.2,21.45,0.86
20260505,23.85,23.85,23.05,23.25,221000,22.3,4.24,22.36,21.47,0.44
20260506,23.55,23.55,22.65,22.8,251000,22.35,2.03,22.52,21.47,0.49
20260507,23,25.05,23,25.05,2916000,22.57,10.98,22.77,21.5,4.48
20260508,25,26.4,24.2,24.55,2692000,22.74,7.98,23,21.52,3.45
20260511,24.35,25.25,24.05,24.5,616000,22.88,7.07,23.14,21.58,0.78
20260512,24.85,25.05,23.9,23.95,454000,22.97,4.26,23.27,21.64,0.58
20260513,23.8,24.15,23.25,24,210000,23.06,4.09,23.38,21.71,0.27
20260514,24.2,24.25,23.45,23.8,364000,23.12,2.94,23.38,21.75,0.52
20260515,24.2,24.3,23.7,23.75,223000,23.17,2.49,23.41,21.81,0.35
20260518,23.8,24.95,23.25,24.65,362000,23.3,5.82,23.5,21.88,0.57
20260519,24.8,25.5,24.2,24.25,363000,23.37,3.74,23.55,21.92,0.59
20260520,24.3,25.5,24.3,24.7,411000,23.49,5.17,23.63,21.97,0.67
20260521,25.05,25.8,24.85,25.35,597000,23.64,7.23,23.71,22.03,1.03
20260522,25.7,27.85,25.6,27.6,27000,23.97,15.14,23.95,22.12,0.05
20260525,28.15,28.15,26.95,27.2,27000,24.24,12.21,24.16,22.21,0.05
20260526,27.4,27.5,26,26.6,26000,24.44,8.85,24.36,22.28,0.05
20260527,26.9,27.75,26.8,26.9,27000,24.64,9.16,24.57,22.36,0.05
20260528,27,27.9,26.2,26.2,27000,24.77,5.77,24.75,22.43,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.96
- over_600_ratio: 50.21
- over_800_ratio: 50.21
- over_1000_ratio: 50.21
- over_400_change_1w: 2.43
- over_800_change_1w: 1.93
- over_1000_change_1w: 1.93
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.07,,48.28,,48.28,,0,False,False
20260508,49.2,0.13,48.28,0,48.28,0,1,False,False
20260515,50.53,1.33,48.28,0,48.28,0,2,False,False
20260522,52.96,2.43,50.21,1.93,50.21,1.93,3,True,True
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
