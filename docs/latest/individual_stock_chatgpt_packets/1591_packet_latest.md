# INDIVIDUAL STOCK CHATGPT PACKET - 1591 駿吉-KY

## Metadata
- generated_at: 2026-05-28 20:18:22 Asia/Taipei
- stock_id: 1591
- stock_name: 駿吉-KY
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1591_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1591_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1591_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1591_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1591_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1591_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1591_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1591_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1591_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1591_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1591_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1591_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1591_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1591.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1591.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1591.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1591.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1591.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1591.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1591_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1591_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1591_latest.md?ref=main

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
- open: 44.6
- high: 44.6
- low: 42
- close: 42.1
- volume: 43000
- ma5: 42.63
- ema23_primary: 49.35
- distance_to_ema23_pct: -14.7
- ma20: 52.41
- ma60: 50.45
- ma120: 49.98
- return_5d: 22.38
- return_20d: -32.96
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -19.68
- distance_to_high_60_pct: -39.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,63.2,67.7,61.5,64.9,2646000,56.6,14.67,56.33,49.89,1.92
20260504,67,67.4,64.2,65.3,2162000,57.32,13.92,57.57,50.16,1.46
20260505,64,68.9,61.8,67.7,2245000,58.19,16.35,58.92,50.45,1.42
20260506,68.7,69.6,64.4,65.2,1940000,58.77,10.94,59.99,50.7,1.17
20260507,65.5,66.4,63.8,64.6,1033000,59.26,9.02,61.02,50.95,0.61
20260508,64.6,64.7,62.3,64.5,1056000,59.69,8.05,61.83,51.19,0.61
20260511,65.5,66.1,62.9,63.6,1335000,60.02,5.97,62.34,51.42,0.79
20260512,63,64.3,59.9,59.9,1741000,60.01,-0.18,62.45,51.58,1.1
20260513,57.5,57.5,54,54,2239000,59.51,-9.26,62.21,51.65,1.45
20260514,54.1,54.1,52.2,52.7,878000,58.94,-10.59,61.9,51.69,0.57
20260515,52.9,53.8,50,50.6,881000,58.25,-13.13,61.52,51.68,0.57
20260518,48.1,48.7,46.5,47.1,1034000,57.32,-17.83,60.99,51.62,0.66
20260519,42.4,42.4,42.4,42.4,435000,56.07,-24.39,59.95,51.5,0.29
20260520,38.2,38.2,38.2,38.2,293000,54.58,-30.02,58.52,51.29,0.2
20260521,34.4,34.4,34.4,34.4,590000,52.9,-34.97,57.06,51.02,0.42
20260522,32.5,37.8,32.5,37.8,34000,51.64,-26.81,55.97,50.81,0.03
20260525,40,41.55,40,41.55,40000,50.8,-18.21,55.08,50.67,0.03
20260526,45.7,45.7,45.7,45.7,46000,50.38,-9.28,54.23,50.61,0.04
20260527,50.2,50.2,42.95,46,48000,50.01,-8.02,53.45,50.56,0.04
20260528,44.6,44.6,42,42.1,43000,49.35,-14.7,52.41,50.45,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 22.06
- over_600_ratio: 12.64
- over_800_ratio: 10.81
- over_1000_ratio: 8.54
- over_400_change_1w: 1.24
- over_800_change_1w: 2.27
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,19.06,,8.54,,8.54,,0,False,False
20260508,20.01,0.95,8.54,0,8.54,0,1,False,False
20260515,20.82,0.81,8.54,0,8.54,0,2,False,False
20260522,22.06,1.24,10.81,2.27,8.54,0,3,False,True
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
