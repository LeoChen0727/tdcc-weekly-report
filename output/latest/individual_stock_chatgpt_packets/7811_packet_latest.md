# INDIVIDUAL STOCK CHATGPT PACKET - 7811 民盛

## Metadata
- generated_at: 2026-05-30 23:43:46 Asia/Taipei
- stock_id: 7811
- stock_name: 民盛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 181
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

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
- ema23_primary: 80.68
- distance_to_ema23_pct: -0.84
- ma20: 80.14
- ma60: 83.24
- ma120: 81.62
- return_5d: 3.9
- return_20d: -5.21
- volume_ratio: 1.29
- distance_to_ma20_pct_auxiliary: -0.17
- distance_to_high_60_pct: -14.35

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,85,85,84.4,85,28000,85.7,-0.82,86.53,83.28,0.45
20260505,85,85.3,83.6,83.6,27000,85.53,-2.25,86.27,83.33,0.45
20260506,83.6,83.6,79.8,81.5,147000,85.19,-4.33,85.98,83.36,2.23
20260507,81.4,81.5,80.1,80.2,70000,84.77,-5.4,85.66,83.36,1.05
20260508,80.5,81.5,80.5,81.2,41000,84.48,-3.88,85.41,83.38,0.62
20260511,81.1,81.3,80,80.9,35000,84.18,-3.89,85.18,83.4,0.54
20260512,80.9,80.9,80.4,80.4,23000,83.86,-4.13,84.81,83.41,0.41
20260513,79.7,81.7,75,81.3,187000,83.65,-2.81,84.47,83.43,2.99
20260514,79.3,83.4,78.5,81.4,65000,83.46,-2.47,84.04,83.45,1.09
20260515,78.9,82,78.6,80.9,76000,83.25,-2.82,83.64,83.47,1.24
20260518,79.1,79.1,78.9,78.9,16000,82.89,-4.81,83.16,83.45,0.27
20260519,78.9,79,78.2,78.4,25000,82.51,-4.98,82.74,83.42,0.43
20260520,78,78,77.1,77.1,20000,82.06,-6.05,82.28,83.37,0.35
20260521,77.5,78,77.5,77.7,9000,81.7,-4.89,81.88,83.33,0.16
20260522,77.7,77.7,77,77,77000,81.31,-5.3,81.47,83.28,1.34
20260525,77.3,77.5,77,77.5,77000,80.99,-4.31,81.08,83.24,1.32
20260526,78,81.5,78,80.5,80000,80.95,-0.55,80.87,83.25,1.31
20260527,81.5,81.5,78.9,78.9,80000,80.78,-2.32,80.64,83.23,1.32
20260528,78.9,81.6,75.8,80.3,80000,80.74,-0.54,80.36,83.24,1.36
20260529,79,80.5,79,80,80000,80.68,-0.84,80.14,83.24,1.29
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 71.78
- over_600_ratio: 67.33
- over_800_ratio: 65.17
- over_1000_ratio: 65.17
- over_400_change_1w: 0.4
- over_800_change_1w: 0.4
- over_1000_change_1w: 0.4
- tdcc_consecutive_up_weeks: 4
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
20260529,71.78,0.4,65.17,0.4,65.17,0.4,4,True,True
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
