# INDIVIDUAL STOCK CHATGPT PACKET - 2430 燦坤

## Metadata
- generated_at: 2026-05-29 19:32:04 Asia/Taipei
- stock_id: 2430
- stock_name: 燦坤
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2430_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2430_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2430_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2430_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2430_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2430_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2430_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2430_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2430_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2430_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2430_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2430_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2430_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2430.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2430.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2430.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2430.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2430.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2430.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2430_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2430_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2430_latest.md?ref=main

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
- open: 18.25
- high: 18.3
- low: 18.15
- close: 18.3
- volume: 114718
- ma5: 18.43
- ema23_primary: 19.14
- distance_to_ema23_pct: -4.38
- ma20: 18.94
- ma60: 20.92
- ma120: 21.92
- return_5d: 0
- return_20d: -8.27
- volume_ratio: 0.73
- distance_to_ma20_pct_auxiliary: -3.39
- distance_to_high_60_pct: -20.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,20,20,19.9,19.95,148009,21.24,-6.08,21.32,22.14,1.17
20260505,19.95,20.1,19.95,20,60250,21.14,-5.38,21.23,22.1,0.47
20260506,20,20,19.9,19.9,311218,21.03,-5.39,21.14,22.05,2.2
20260507,19.9,20,19.9,19.9,99866,20.94,-4.97,21.04,22,0.7
20260508,19.95,19.95,19.85,19.9,106507,20.85,-4.57,20.94,21.96,0.72
20260511,19.9,19.9,19.7,19.75,148250,20.76,-4.87,20.84,21.91,1
20260512,19.75,19.75,19.6,19.65,101132,20.67,-4.93,20.73,21.86,0.68
20260513,19.65,19.65,19.1,19.3,251872,20.55,-6.1,20.61,21.81,1.6
20260514,19.2,19.2,18.7,18.75,294323,20.4,-8.11,20.46,21.74,1.75
20260515,18.65,18.65,18.35,18.4,169371,20.24,-9.08,20.3,21.67,0.98
20260518,18.3,18.35,18.25,18.25,87409,20.07,-9.08,20.12,21.6,0.53
20260519,18.2,18.3,18.05,18.15,91382,19.91,-8.85,19.95,21.53,0.57
20260520,18.1,18.25,18.1,18.2,92071,19.77,-7.94,19.78,21.45,0.58
20260521,18.2,18.3,18.1,18.3,129943,19.65,-6.85,19.62,21.38,0.81
20260522,18.3,18.3,18.2,18.3,118610,19.53,-6.32,19.46,21.3,0.75
20260525,18.35,18.5,18.35,18.45,189815,19.44,-5.11,19.34,21.23,1.21
20260526,18.45,18.95,18.4,18.8,192868,19.39,-3.04,19.25,21.16,1.22
20260527,18.8,18.85,18.5,18.55,203616,19.32,-3.99,19.14,21.08,1.24
20260528,18.65,18.65,18.05,18.05,237017,19.21,-6.06,19.02,21,1.38
20260529,18.25,18.3,18.15,18.3,114718,19.14,-4.38,18.94,20.92,0.73
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.21
- over_600_ratio: 60.88
- over_800_ratio: 59.2
- over_1000_ratio: 57.8
- over_400_change_1w: -0.06
- over_800_change_1w: -0.13
- over_1000_change_1w: -0.13
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.3,,59.5,,58.1,,0,False,False
20260508,64.23,-0.07,59.35,-0.15,57.95,-0.15,0,False,False
20260515,64.27,0.04,59.33,-0.02,57.93,-0.02,1,False,False
20260522,64.21,-0.06,59.2,-0.13,57.8,-0.13,2,False,False
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
