# INDIVIDUAL STOCK CHATGPT PACKET - 8150 南茂

## Metadata
- generated_at: 2026-05-28 19:33:47 Asia/Taipei
- stock_id: 8150
- stock_name: 南茂
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8150_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8150_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8150_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8150_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8150_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8150_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8150_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8150_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8150_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8150_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8150_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8150_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8150_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8150.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8150.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8150.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8150.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8150.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8150.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8150_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8150_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8150_latest.md?ref=main

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
- open: 98.8
- high: 103
- low: 98.5
- close: 103
- volume: 112421888
- ma5: 89.64
- ema23_primary: 82.42
- distance_to_ema23_pct: 24.97
- ma20: 84.86
- ma60: 70.22
- ma120: 61.83
- return_5d: 35.7
- return_20d: 53.73
- volume_ratio: 2.41
- distance_to_ma20_pct_auxiliary: 21.38
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,67.3,73.5,67.2,69.8,32774904,66.48,4.99,66.08,62.12,1.05
20260504,71.2,76.7,70.7,76.5,43860152,67.32,13.64,67.14,62.3,1.32
20260505,79.9,84.1,79.8,84.1,20021669,68.71,22.39,68.5,62.59,0.59
20260506,92.5,92.5,87.5,89.2,74820219,70.42,26.67,70.11,62.97,2.02
20260507,90,98.1,84.5,98.1,80749867,72.73,34.89,71.97,63.51,2
20260508,100.5,103,88.3,92.7,101806451,74.39,24.61,73.59,64.02,2.26
20260511,95,97.9,90.3,91,51675179,75.78,20.09,75.07,64.53,1.1
20260512,90.4,90.6,86.1,87,34358540,76.71,13.41,76.28,65.02,0.72
20260513,85.1,89.4,84.6,85.5,28772358,77.44,10.4,77.4,65.5,0.59
20260514,86,88,82.5,83.9,31450051,77.98,7.59,78.25,65.97,0.65
20260515,84.2,84.2,80,80.9,23693876,78.23,3.42,78.61,66.43,0.5
20260518,79,84.4,76.9,82.3,18660090,78.56,4.75,79.36,66.93,0.42
20260519,81.3,82.2,77.3,77.6,17459593,78.48,-1.13,79.86,67.33,0.41
20260520,77.6,77.6,74.2,74.4,15031169,78.14,-4.79,79.88,67.69,0.37
20260521,76.5,78.6,75.9,75.9,13812607,77.96,-2.64,79.69,68.06,0.38
20260522,77.4,82.4,76.3,79.1,46238424,78.05,1.34,80.05,68.46,1.3
20260525,80.5,87,79.1,86.8,51440041,78.78,10.18,80.89,68.92,1.41
20260526,86.8,88.1,83.8,85.4,44236285,79.33,7.65,81.78,69.26,1.18
20260527,89.7,93.9,86,93.9,90891826,80.55,16.58,83.06,69.64,2.19
20260528,98.8,103,98.5,103,112421888,82.42,24.97,84.86,70.22,2.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.62
- over_600_ratio: 68.88
- over_800_ratio: 67.34
- over_1000_ratio: 65.33
- over_400_change_1w: -1.12
- over_800_change_1w: -0.78
- over_1000_change_1w: -1.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.83,,68.91,,66.61,,0,False,False
20260508,77.98,5.15,73.77,4.86,72.25,5.64,1,True,True
20260515,71.74,-6.24,68.12,-5.65,66.48,-5.77,0,False,False
20260522,70.62,-1.12,67.34,-0.78,65.33,-1.15,0,False,False
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8150 | 南茂 | 150 | 3 | 33805050.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
