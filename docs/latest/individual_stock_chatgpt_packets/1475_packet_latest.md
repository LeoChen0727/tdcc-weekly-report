# INDIVIDUAL STOCK CHATGPT PACKET - 1475 業旺

## Metadata
- generated_at: 2026-05-29 19:31:41 Asia/Taipei
- stock_id: 1475
- stock_name: 業旺
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1475_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1475_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1475_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1475_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1475_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1475_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1475_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1475_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1475_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1475_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1475_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1475_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1475_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1475.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1475.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1475.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1475.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1475.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1475.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1475_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1475_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1475_latest.md?ref=main

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
- open: 24.9
- high: 25
- low: 24.75
- close: 24.9
- volume: 38074
- ma5: 24.97
- ema23_primary: 26.27
- distance_to_ema23_pct: -5.21
- ma20: 26.29
- ma60: 27.86
- ma120: 29.95
- return_5d: -0.8
- return_20d: -10.59
- volume_ratio: 0.63
- distance_to_ma20_pct_auxiliary: -5.3
- distance_to_high_60_pct: -18.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,27.9,28,27.5,27.6,66077,28.46,-3.03,28.67,29.44,1.45
20260505,27.5,27.85,27.45,27.45,50022,28.38,-3.27,28.6,29.36,1.06
20260506,27.5,27.55,27.4,27.45,57483,28.3,-3.01,28.55,29.27,1.19
20260507,27.35,27.55,27.3,27.4,41219,28.23,-2.93,28.45,29.19,0.86
20260508,27.35,27.8,27.35,27.7,86728,28.18,-1.71,28.37,29.11,1.69
20260511,27.5,27.8,27.35,27.65,54157,28.14,-1.73,28.25,29.04,1.09
20260512,27.95,27.95,27.35,27.35,28338,28.07,-2.57,28.09,28.96,0.6
20260513,27.45,27.45,26.7,27.3,66034,28.01,-2.53,27.93,28.9,1.5
20260514,27.3,27.3,26.65,26.95,76064,27.92,-3.47,27.84,28.83,1.76
20260515,26.95,26.95,26.25,26.45,79083,27.8,-4.85,27.74,28.75,1.75
20260518,26.75,26.75,26,26.1,74003,27.66,-5.62,27.63,28.68,1.56
20260519,26,26.3,25.8,26.1,27881,27.53,-5.18,27.52,28.6,0.59
20260520,26.1,26.1,25.3,25.3,91000,27.34,-7.46,27.35,28.51,1.86
20260521,25.5,25.5,24.65,25.1,71451,27.15,-7.56,27.16,28.42,1.4
20260522,25,25.1,24.8,25.1,43410,26.98,-6.98,27.01,28.32,0.83
20260525,24.95,25.25,24.7,25.1,68678,26.83,-6.43,26.86,28.23,1.27
20260526,25.1,25.2,24.7,25,43090,26.67,-6.27,26.73,28.13,0.8
20260527,25,25.2,24.55,25,102060,26.53,-5.78,26.61,28.03,1.75
20260528,24.9,25,24.5,24.85,49304,26.39,-5.85,26.44,27.94,0.83
20260529,24.9,25,24.75,24.9,38074,26.27,-5.21,26.29,27.86,0.63
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 76.24
- over_600_ratio: 73.28
- over_800_ratio: 70.17
- over_1000_ratio: 68.95
- over_400_change_1w: 0.01
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.36,,70.15,,68.93,,0,False,False
20260508,76.36,0,70.15,0,68.93,0,0,False,False
20260515,76.23,-0.13,70.16,0.01,68.94,0.01,1,False,True
20260522,76.24,0.01,70.17,0.01,68.95,0.01,2,True,True
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
