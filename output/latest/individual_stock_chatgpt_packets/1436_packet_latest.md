# INDIVIDUAL STOCK CHATGPT PACKET - 1436 華友聯

## Metadata
- generated_at: 2026-05-29 19:31:38 Asia/Taipei
- stock_id: 1436
- stock_name: 華友聯
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1436_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1436_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1436_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1436_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1436_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1436_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1436_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1436_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1436_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1436_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1436_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1436_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1436_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1436.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1436.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1436.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1436.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1436.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1436.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1436_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1436_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1436_latest.md?ref=main

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
- open: 44.25
- high: 44.25
- low: 43.95
- close: 44.25
- volume: 167382
- ma5: 44.38
- ema23_primary: 47.03
- distance_to_ema23_pct: -5.91
- ma20: 46.85
- ma60: 51.06
- ma120: 56.48
- return_5d: -2.64
- return_20d: -11.41
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -5.55
- distance_to_high_60_pct: -24.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,49.95,49.95,49.45,49.65,274613,51.95,-4.44,51.95,54.96,1.17
20260505,49.6,50.2,49.6,49.9,116178,51.78,-3.64,51.77,54.75,0.5
20260506,50,50,49.05,49.3,259683,51.58,-4.41,51.55,54.54,1.07
20260507,49.45,49.45,48.65,49.05,383149,51.37,-4.51,51.31,54.34,1.51
20260508,48.7,49.1,48.45,48.85,286167,51.16,-4.51,51.1,54.14,1.14
20260511,48.9,49.3,48.35,48.7,308877,50.95,-4.42,50.91,53.93,1.21
20260512,48.65,48.65,47.9,48.35,364022,50.73,-4.7,50.71,53.74,1.36
20260513,48.3,48.3,47.9,48,237856,50.51,-4.96,50.47,53.54,0.89
20260514,48,48.45,47.7,48.05,261882,50.3,-4.48,50.21,53.33,0.96
20260515,48.05,48.25,45.85,46.2,838324,49.96,-7.53,49.85,53.09,2.76
20260518,46.2,46.8,45.35,46.3,306402,49.66,-6.76,49.53,52.89,1
20260519,46.2,46.7,46.1,46.1,128683,49.36,-6.6,49.26,52.71,0.44
20260520,46.1,46.1,45.15,45.75,425383,49.06,-6.74,48.94,52.53,1.4
20260521,45,45.85,44.5,45.5,685660,48.76,-6.69,48.62,52.34,2.1
20260522,45.35,45.45,44.9,45.45,248056,48.49,-6.26,48.34,52.12,0.78
20260525,45.45,45.6,44.35,44.6,575218,48.16,-7.4,48.03,51.87,1.71
20260526,44.6,44.8,44.05,44.75,215833,47.88,-6.53,47.77,51.63,0.66
20260527,44.75,44.9,44.05,44.05,219854,47.56,-7.38,47.45,51.42,0.67
20260528,44.15,44.3,43.85,44.25,349012,47.28,-6.41,47.14,51.23,1.04
20260529,44.25,44.25,43.95,44.25,167382,47.03,-5.91,46.85,51.06,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.65
- over_600_ratio: 76.29
- over_800_ratio: 75.89
- over_1000_ratio: 73.58
- over_400_change_1w: 0.7
- over_800_change_1w: 0.18
- over_1000_change_1w: 0.18
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.11,,75.82,,73.51,,0,False,False
20260508,78.14,0.03,75.86,0.04,73.55,0.04,1,True,True
20260515,77.95,-0.19,75.71,-0.15,73.4,-0.15,0,False,False
20260522,78.65,0.7,75.89,0.18,73.58,0.18,1,False,True
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
