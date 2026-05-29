# INDIVIDUAL STOCK CHATGPT PACKET - 3709 鑫聯大投控

## Metadata
- generated_at: 2026-05-29 19:32:44 Asia/Taipei
- stock_id: 3709
- stock_name: 鑫聯大投控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3709_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3709_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3709_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3709_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3709_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3709_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3709_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3709_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3709_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3709_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3709_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3709_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3709_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3709.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3709.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3709.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3709.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3709.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3709.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3709_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3709_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3709_latest.md?ref=main

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
- open: 88.4
- high: 89.5
- low: 87.4
- close: 88.8
- volume: 89000
- ma5: 88.4
- ema23_primary: 83.94
- distance_to_ema23_pct: 5.78
- ma20: 85.34
- ma60: 75.67
- ma120: 67.09
- return_5d: 0.68
- return_20d: 7.64
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 4.05
- distance_to_high_60_pct: -4.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,84.4,86.4,80.6,85.2,5062000,75.37,13.04,74.22,69.14,1.07
20260505,85,85.4,82.8,85,2672000,76.17,11.59,75.3,69.53,0.56
20260506,85.7,85.9,81.4,82.5,4230000,76.7,7.56,76.16,69.89,0.86
20260507,83.7,90.5,82.7,84.5,7774000,77.35,9.24,76.93,70.27,1.49
20260508,85.3,92.9,83.6,92.9,9341000,78.65,18.12,78.17,70.78,1.66
20260511,91,91.1,84.6,89.1,8274000,79.52,12.05,79.22,71.24,1.39
20260512,86,86.5,80.3,82,9174000,79.73,2.85,79.89,71.61,1.46
20260513,82,83.5,80.6,81.9,2300000,79.91,2.5,80.24,71.89,0.4
20260514,83.4,85.6,81.6,81.8,3589000,80.06,2.17,80.82,72.14,0.63
20260515,82.3,84.5,79.8,81.1,2660000,80.15,1.18,81.42,72.45,0.47
20260518,80.5,82,78.1,81.3,2299000,80.25,1.31,81.92,72.77,0.4
20260519,81.5,82.4,78.6,78.9,1974000,80.13,-1.54,82.36,73.03,0.35
20260520,80,85,79.6,83.4,4157000,80.41,3.72,82.66,73.4,0.77
20260521,84.1,87.8,83.5,87,3756000,80.96,7.47,83.13,73.82,0.75
20260522,87.6,90.4,87.5,88.2,89000,81.56,8.14,83.55,74.22,0.02
20260525,89.4,91.7,85.2,90.2,89000,82.28,9.63,84.02,74.68,0.02
20260526,90.5,91,88.1,89.4,89000,82.87,7.88,84.41,75.01,0.02
20260527,91.5,91.8,86.3,86.3,88000,83.16,3.78,84.62,75.18,0.02
20260528,86,89.3,85.1,87.3,87000,83.5,4.55,85.03,75.36,0.02
20260529,88.4,89.5,87.4,88.8,89000,83.94,5.78,85.34,75.67,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.87
- over_600_ratio: 72.25
- over_800_ratio: 68.34
- over_1000_ratio: 66.3
- over_400_change_1w: 2.71
- over_800_change_1w: 1.16
- over_1000_change_1w: 1.33
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,73.69,,68.27,,63.22,,0,False,False
20260508,73.01,-0.68,68.25,-0.02,63.99,0.77,1,False,True
20260515,72.16,-0.85,67.18,-1.07,64.97,0.98,2,False,True
20260522,74.87,2.71,68.34,1.16,66.3,1.33,3,True,True
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
