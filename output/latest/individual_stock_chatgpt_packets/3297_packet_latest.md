# INDIVIDUAL STOCK CHATGPT PACKET - 3297 杭特

## Metadata
- generated_at: 2026-05-26 22:19:05 Asia/Taipei
- stock_id: 3297
- stock_name: 杭特
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3297_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3297_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3297_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3297_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3297_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3297_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3297_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3297_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3297_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3297_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3297_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3297_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3297_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3297.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3297.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3297.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3297.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3297.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3297.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3297_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3297_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3297_latest.md?ref=main

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
- date: 20260526
- open: 30.2
- high: 30.35
- low: 29.9
- close: 30.1
- volume: 30000
- ma5: 30.45
- ema23_primary: 31.73
- distance_to_ema23_pct: -5.14
- ma20: 31.34
- ma60: 34.27
- ma120: 37.74
- return_5d: 0
- return_20d: -6.08
- volume_ratio: 0.43
- distance_to_ma20_pct_auxiliary: -3.94
- distance_to_high_60_pct: -23.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,32.05,32.35,31.7,31.85,64000,34.78,-8.42,34.52,36.75,0.36
20260429,31.9,31.9,31.65,31.8,44000,34.53,-7.9,34.41,36.56,0.25
20260430,31.8,32.05,31.75,32.05,73000,34.32,-6.62,34.35,36.39,0.43
20260504,32.05,32.05,31.1,31.7,53000,34.1,-7.05,34.25,36.24,0.32
20260505,31.7,32.15,31.5,31.75,96000,33.91,-6.36,34.16,36.07,0.57
20260506,31.75,31.75,31.05,31.5,126000,33.71,-6.55,34.1,35.93,0.75
20260507,31.95,32.2,31.6,31.9,102000,33.56,-4.94,34.06,35.78,0.6
20260508,32,32.2,31.65,31.8,93000,33.41,-4.82,33.86,35.65,0.6
20260511,30.8,32.6,30.35,32.6,144000,33.34,-2.23,33.76,35.53,1.1
20260512,33.35,33.35,32.6,32.85,50000,33.3,-1.36,33.55,35.43,0.44
20260513,31.65,31.95,31.6,31.8,51000,33.18,-4.15,33.34,35.32,0.49
20260514,31.85,32.85,31.05,31.35,68000,33.02,-5.07,33.12,35.2,0.68
20260515,31.35,31.7,30.3,30.6,101000,32.82,-6.77,32.82,35.07,1.05
20260518,30.3,31.2,30.3,30.8,21000,32.65,-5.68,32.52,34.95,0.23
20260519,31.6,31.6,30.1,30.1,79000,32.44,-7.22,32.22,34.84,0.88
20260520,30,30.5,30,30.3,57000,32.26,-6.08,31.94,34.73,0.65
20260521,30.3,31,30.3,30.85,84000,32.14,-4.03,31.7,34.63,0.96
20260522,30.5,30.9,30.4,30.75,31000,32.03,-3.99,31.55,34.51,0.39
20260525,30.75,30.75,29.9,30.25,30000,31.88,-5.11,31.43,34.39,0.41
20260526,30.2,30.35,29.9,30.1,30000,31.73,-5.14,31.34,34.27,0.43
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.33
- over_600_ratio: 49.33
- over_800_ratio: 41.61
- over_1000_ratio: 36.6
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.58,,41.61,,36.6,,0,False,False
20260508,49.33,-1.25,41.61,0,36.6,0,0,False,False
20260515,49.33,0,41.61,0,36.6,0,0,False,False
20260522,49.33,0,41.61,0,36.6,0,0,False,False
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
