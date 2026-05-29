# INDIVIDUAL STOCK CHATGPT PACKET - 7811 民盛

## Metadata
- generated_at: 2026-05-29 19:33:51 Asia/Taipei
- stock_id: 7811
- stock_name: 民盛
- packet_status: partial_rawdata_packet
- latest_price_date: 20260529
- price_rows: 45
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7811_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7811_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7811_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7811_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7811_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7811_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7811_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7811_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7811_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7811_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7811_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7811_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7811_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7811.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7811.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7811.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7811.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7811.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7811.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7811_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7811_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7811_latest.md?ref=main

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
- open: 79
- high: 80.5
- low: 79
- close: 80
- volume: 80000
- ma5: 79.44
- ema23_primary: 80.92
- distance_to_ema23_pct: -1.13
- ma20: 80.14
- ma60: 84.32
- ma120: 84.32
- return_5d: 3.9
- return_20d: -5.21
- volume_ratio: 1.29
- distance_to_ma20_pct_auxiliary: -0.17
- distance_to_high_60_pct: -14.35

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,85,85,84.4,85,28000,86.95,-2.24,86.53,87.56,0.45
20260505,85,85.3,83.6,83.6,27000,86.67,-3.54,86.27,87.41,0.45
20260506,83.6,83.6,79.8,81.5,147000,86.24,-5.5,85.98,87.2,2.23
20260507,81.4,81.5,80.1,80.2,70000,85.74,-6.46,85.66,86.96,1.05
20260508,80.5,81.5,80.5,81.2,41000,85.36,-4.87,85.41,86.77,0.62
20260511,81.1,81.3,80,80.9,35000,84.99,-4.81,85.18,86.58,0.54
20260512,80.9,80.9,80.4,80.4,23000,84.61,-4.97,84.81,86.38,0.41
20260513,79.7,81.7,75,81.3,187000,84.33,-3.59,84.47,86.23,2.99
20260514,79.3,83.4,78.5,81.4,65000,84.09,-3.19,84.04,86.09,1.09
20260515,78.9,82,78.6,80.9,76000,83.82,-3.48,83.64,85.94,1.24
20260518,79.1,79.1,78.9,78.9,16000,83.41,-5.41,83.16,85.74,0.27
20260519,78.9,79,78.2,78.4,25000,82.99,-5.53,82.74,85.55,0.43
20260520,78,78,77.1,77.1,20000,82.5,-6.55,82.28,85.32,0.35
20260521,77.5,78,77.5,77.7,9000,82.1,-5.36,81.88,85.13,0.16
20260522,77.7,77.7,77,77,77000,81.68,-5.73,81.47,84.92,1.34
20260525,77.3,77.5,77,77.5,77000,81.33,-4.71,81.08,84.74,1.32
20260526,78,81.5,78,80.5,80000,81.26,-0.93,80.87,84.64,1.31
20260527,81.5,81.5,78.9,78.9,80000,81.06,-2.67,80.64,84.51,1.32
20260528,78.9,81.6,75.8,80.3,80000,81,-0.86,80.36,84.41,1.36
20260529,79,80.5,79,80,80000,80.92,-1.13,80.14,84.32,1.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.38
- over_600_ratio: 66.93
- over_800_ratio: 64.77
- over_1000_ratio: 64.77
- over_400_change_1w: 0.17
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.84,,64.26,,64.26,,0,False,False
20260508,70.85,0.01,64.26,0,64.26,0,1,False,False
20260515,71.21,0.36,64.6,0.34,64.6,0.34,2,True,True
20260522,71.38,0.17,64.77,0.17,64.77,0.17,3,True,True
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
