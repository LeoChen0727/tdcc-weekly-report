# INDIVIDUAL STOCK CHATGPT PACKET - 1595 川寶

## Metadata
- generated_at: 2026-05-28 20:18:22 Asia/Taipei
- stock_id: 1595
- stock_name: 川寶
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1595_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1595_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1595_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1595_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1595_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1595_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1595_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1595_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1595_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1595_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1595_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1595_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1595_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1595.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1595.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1595.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1595.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1595.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1595.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1595_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1595_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1595_latest.md?ref=main

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
- open: 92.3
- high: 94.4
- low: 86.2
- close: 87.3
- volume: 90000
- ma5: 94.7
- ema23_primary: 85.06
- distance_to_ema23_pct: 2.63
- ma20: 90.56
- ma60: 61.05
- ma120: 50.09
- return_5d: -10.46
- return_20d: 31.87
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -3.61
- distance_to_high_60_pct: -18.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,68.2,72.8,68.2,72.8,5174000,54.79,32.88,53,44.88,1.87
20260504,77,80,75.4,77,8789000,56.64,35.95,54.78,45.51,2.74
20260505,75.5,84.7,75.2,84.7,5440000,58.98,43.62,56.96,46.26,1.57
20260506,93.1,93.1,87,93.1,5711000,61.82,50.6,59.57,47.15,1.52
20260507,89.5,101,89.5,96.2,7536000,64.68,48.72,62.27,48.09,1.83
20260508,96.4,99.9,90.1,98.2,7053000,67.48,45.53,64.95,49.08,1.59
20260511,93.1,94.6,92.5,94.1,995000,69.7,35.02,67.48,50.02,0.22
20260512,92,93,86,90.5,1466000,71.43,26.7,69.61,50.87,0.33
20260513,90.1,94.8,88,93.2,882000,73.24,27.25,71.78,51.74,0.2
20260514,94.6,94.8,90.2,90.2,857000,74.66,20.82,73.89,52.55,0.2
20260515,92.7,92.7,85,85,931000,75.52,12.56,75.48,53.27,0.22
20260518,84.9,90.8,80.5,89.6,695000,76.69,16.83,77.34,54.08,0.18
20260519,89.1,91,85,87,509000,77.55,12.18,79.06,54.85,0.13
20260520,87.2,90.8,87,88.7,411000,78.48,13.02,80.99,55.64,0.11
20260521,90.4,97.5,89.2,97.5,1234000,80.07,21.78,83.11,56.6,0.32
20260522,97.5,101.5,96.1,98.1,99000,81.57,20.27,84.98,57.55,0.03
20260525,97,107,93.8,96,100000,82.77,15.98,86.45,58.47,0.03
20260526,97,101.5,89.6,100.5,95000,84.25,19.29,88.19,59.44,0.03
20260527,100.5,105,91.4,91.6,98000,84.86,7.94,89.51,60.28,0.04
20260528,92.3,94.4,86.2,87.3,90000,85.06,2.63,90.56,61.05,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.79
- over_600_ratio: 44.87
- over_800_ratio: 42.23
- over_1000_ratio: 40.66
- over_400_change_1w: -0.71
- over_800_change_1w: -0.16
- over_1000_change_1w: -0.16
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.6,,40.81,,39.23,,0,False,False
20260508,51.92,0.32,42.44,1.63,39.34,0.11,1,True,True
20260515,50.5,-1.42,42.39,-0.05,40.82,1.48,2,False,True
20260522,49.79,-0.71,42.23,-0.16,40.66,-0.16,0,False,False
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
