# INDIVIDUAL STOCK CHATGPT PACKET - 6997 博弘

## Metadata
- generated_at: 2026-05-28 20:20:25 Asia/Taipei
- stock_id: 6997
- stock_name: 博弘
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 109
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6997_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6997_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6997_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6997_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6997_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6997_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6997_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6997_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6997_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6997_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6997_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6997_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6997_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6997.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6997.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6997.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6997.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6997.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6997.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6997_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6997_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6997_latest.md?ref=main

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
- open: 68
- high: 68.5
- low: 68
- close: 68.5
- volume: 68000
- ma5: 68.96
- ema23_primary: 72.59
- distance_to_ema23_pct: -5.63
- ma20: 71.88
- ma60: 80.22
- ma120: 86.04
- return_5d: 0
- return_20d: -13.29
- volume_ratio: 2.27
- distance_to_ma20_pct_auxiliary: -4.7
- distance_to_high_60_pct: -24.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,78.9,79.2,78.5,79,14000,82.34,-4.06,82.03,86.18,2.24
20260504,79,79,78.6,78.6,6000,82.03,-4.18,81.89,85.99,0.96
20260505,78.6,79.6,78.5,78.7,11000,81.75,-3.73,81.6,85.78,1.67
20260506,77.7,77.7,73,73.1,79000,81.03,-9.79,81.1,85.47,7.56
20260507,70.4,72.2,70.1,71.2,37000,80.21,-11.24,80.5,85.12,3.06
20260508,70.3,70.9,70,70.6,18000,79.41,-11.1,79.89,84.76,1.39
20260511,70.9,75.5,70.9,75.1,23000,79.05,-5,79.56,84.46,1.65
20260512,76.4,76.4,74.9,74.9,7000,78.71,-4.84,79.27,84.2,0.5
20260513,75,75,74,74,9000,78.31,-5.51,78.85,83.93,0.63
20260514,74,74.5,73.6,74.5,3000,78,-4.48,78.4,83.64,0.21
20260515,73.9,73.9,70,72,19000,77.5,-7.09,77.9,83.33,1.24
20260518,68.1,69.6,68,68.3,15000,76.73,-10.99,77.21,82.97,0.96
20260519,67,67.2,67,67,5000,75.92,-11.75,76.44,82.58,0.32
20260520,67,67.3,67,67.3,3000,75.2,-10.51,75.63,82.22,0.2
20260521,70.3,70.3,68.5,68.5,3000,74.64,-8.23,74.88,81.87,0.2
20260522,70.9,72.2,70.7,71,71000,74.34,-4.49,74.33,81.56,3.91
20260525,71.1,71.1,71,71,71000,74.06,-4.13,73.81,81.25,3.33
20260526,70.8,70.8,66.4,66.4,69000,73.42,-9.56,73.06,80.89,2.84
20260527,68.1,68.1,67.5,67.9,68000,72.96,-6.94,72.41,80.55,2.48
20260528,68,68.5,68,68.5,68000,72.59,-5.63,71.88,80.22,2.27
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.26
- over_600_ratio: 82.26
- over_800_ratio: 82.26
- over_1000_ratio: 77.74
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
20260430,82.26,,82.26,,77.74,,0,False,False
20260508,82.26,0,82.26,0,77.74,0,0,False,False
20260515,82.26,0,82.26,0,77.74,0,0,False,False
20260522,82.26,0,82.26,0,77.74,0,0,False,False
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
