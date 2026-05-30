# INDIVIDUAL STOCK CHATGPT PACKET - 4721 美琪瑪

## Metadata
- generated_at: 2026-05-30 23:42:26 Asia/Taipei
- stock_id: 4721
- stock_name: 美琪瑪
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4721_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4721_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4721_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4721_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4721_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4721_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4721_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4721_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4721_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4721_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4721_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4721_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4721_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4721.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4721.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4721.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4721.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4721.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4721.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4721_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4721_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4721_latest.md?ref=main

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
- open: 89
- high: 93.3
- low: 88.2
- close: 92.7
- volume: 92000
- ma5: 90.62
- ema23_primary: 88.91
- distance_to_ema23_pct: 4.27
- ma20: 90.83
- ma60: 80.94
- ma120: 74.25
- return_5d: 2.54
- return_20d: 11.02
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: 2.06
- distance_to_high_60_pct: -5.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,83.1,87,81.5,86.5,1365000,82.29,5.12,83.33,73.09,0.54
20260505,86,90.4,84.5,89,3062000,82.84,7.43,84.17,73.4,1.16
20260506,90,94.9,88.5,93.3,7380000,83.72,11.45,85.27,73.8,2.47
20260507,92.4,94.8,91.9,93.2,3811000,84.51,10.29,86.23,74.2,1.21
20260508,94.2,96.5,92,95.5,8244000,85.42,11.8,87.3,74.66,2.34
20260511,94,97.2,90.2,95.1,6021000,86.23,10.29,88.14,75.15,1.62
20260512,95.1,98,94,97.8,7353000,87.19,12.16,88.98,75.71,1.9
20260513,95.7,96.5,93.7,94,3194000,87.76,7.11,89.67,76.21,0.81
20260514,94.7,96,92.1,92.1,2799000,88.12,4.51,90,76.66,0.72
20260515,94.4,94.4,89.4,89.8,1608000,88.26,1.74,90.02,77.08,0.45
20260518,88.5,89.4,86.2,88.4,914000,88.27,0.14,89.88,77.5,0.27
20260519,89,91,88,88.3,810000,88.28,0.03,89.72,77.89,0.25
20260520,89.6,89.6,83.6,83.7,1300000,87.89,-4.77,89.25,78.21,0.41
20260521,85.2,86.8,85,86.3,770000,87.76,-1.67,88.89,78.57,0.25
20260522,88,91.8,87.2,90.4,90000,87.98,2.75,89,78.97,0.03
20260525,92,92.7,89.6,90.9,91000,88.22,3.03,89.41,79.38,0.03
20260526,91.4,93.2,90.4,92.1,92000,88.55,4.01,89.91,79.79,0.04
20260527,93.5,93.5,90.1,90.4,91000,88.7,1.91,90.28,80.17,0.04
20260528,90.4,91.7,87,87,89000,88.56,-1.76,90.36,80.51,0.04
20260529,89,93.3,88.2,92.7,92000,88.91,4.27,90.83,80.94,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 34.38
- over_600_ratio: 29.14
- over_800_ratio: 29.14
- over_1000_ratio: 28.04
- over_400_change_1w: 1.65
- over_800_change_1w: 1.1
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,35.79,,29.21,,28.03,,0,False,False
20260508,35.5,-0.29,28.03,-1.18,28.03,0,0,False,False
20260515,31.98,-3.52,28.04,0.01,28.04,0.01,1,False,True
20260522,32.73,0.75,28.04,0,28.04,0,2,False,False
20260529,34.38,1.65,29.14,1.1,28.04,0,3,False,True
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
