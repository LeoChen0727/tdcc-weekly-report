# INDIVIDUAL STOCK CHATGPT PACKET - 1568 倉佑

## Metadata
- generated_at: 2026-05-30 23:41:03 Asia/Taipei
- stock_id: 1568
- stock_name: 倉佑
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1568_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1568_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1568_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1568_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1568_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1568_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1568_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1568_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1568_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1568_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1568_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1568_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1568_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1568.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1568.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1568.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1568.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1568.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1568.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1568_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1568_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1568_latest.md?ref=main

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
- open: 45.35
- high: 45.35
- low: 43.85
- close: 45.35
- volume: 13595230
- ma5: 38.23
- ema23_primary: 31.79
- distance_to_ema23_pct: 42.67
- ma20: 31.15
- ma60: 26.39
- ma120: 24.63
- return_5d: 56.11
- return_20d: 59.12
- volume_ratio: 9.97
- distance_to_ma20_pct_auxiliary: 45.6
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,28.5,31,28.5,30.2,1657016,26.49,14.01,26.25,23.88,2.55
20260505,30.4,30.6,29.15,29.55,639229,26.74,10.49,26.59,23.97,0.94
20260506,29.95,29.95,28.8,29.05,381122,26.94,7.85,26.91,24.05,0.55
20260507,29.05,29.9,29.05,29.45,440073,27.15,8.49,27.25,24.14,0.62
20260508,29.15,29.95,28.6,28.9,283879,27.29,5.89,27.56,24.22,0.39
20260511,28.95,29.2,28.25,28.8,403089,27.42,5.04,27.82,24.3,0.56
20260512,28.85,29.4,28.1,28.9,618531,27.54,4.93,28.01,24.4,0.88
20260513,28.5,29.15,28.5,28.6,245643,27.63,3.51,28.18,24.48,0.35
20260514,28.6,29.15,28.2,28.35,347861,27.69,2.39,28.33,24.56,0.5
20260515,28.8,29.05,28.35,28.65,234733,27.77,3.17,28.5,24.65,0.34
20260518,28.95,28.95,28.15,28.35,182953,27.82,1.91,28.65,24.73,0.26
20260519,28.6,28.75,27.4,27.5,353130,27.79,-1.05,28.75,24.81,0.5
20260520,28.1,28.8,27.7,28,212904,27.81,0.69,28.75,24.89,0.33
20260521,28.35,28.5,28.05,28.45,218889,27.86,2.11,28.7,24.98,0.43
20260522,28.95,29.2,28.65,29.05,279808,27.96,3.89,28.67,25.09,0.63
20260525,29.5,31.95,29.05,31.95,2240761,28.29,12.92,28.88,25.24,4.42
20260526,35.1,35.1,35.1,35.1,1870870,28.86,21.62,29.24,25.45,3.22
20260527,37.5,37.5,37.5,37.5,1409682,29.58,26.77,29.66,25.7,2.24
20260528,41.25,41.25,41.25,41.25,1658522,30.55,35.01,30.3,26.01,2.38
20260529,45.35,45.35,43.85,45.35,13595230,31.79,42.67,31.15,26.39,9.97
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 67.81
- over_600_ratio: 65.03
- over_800_ratio: 62.41
- over_1000_ratio: 59.09
- over_400_change_1w: 3.69
- over_800_change_1w: 2.4
- over_1000_change_1w: 2.45
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.78,,59.91,,56.52,,0,False,False
20260508,63.41,0.63,59.9,-0.01,56.53,0.01,1,False,True
20260515,64.42,1.01,60.01,0.11,56.64,0.11,2,True,True
20260522,64.12,-0.3,60.01,0,56.64,0,0,False,False
20260529,67.81,3.69,62.41,2.4,59.09,2.45,1,True,True
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
