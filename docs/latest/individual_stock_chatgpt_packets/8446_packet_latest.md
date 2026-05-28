# INDIVIDUAL STOCK CHATGPT PACKET - 8446 華研

## Metadata
- generated_at: 2026-05-28 19:33:52 Asia/Taipei
- stock_id: 8446
- stock_name: 華研
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8446_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8446_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8446_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8446_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8446_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8446_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8446_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8446_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8446_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8446_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8446_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8446_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8446_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8446.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8446.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8446.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8446.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8446.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8446.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8446_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8446_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8446_latest.md?ref=main

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
- open: 85.5
- high: 86.7
- low: 85.2
- close: 85.6
- volume: 185777
- ma5: 85.02
- ema23_primary: 85.89
- distance_to_ema23_pct: -0.33
- ma20: 84.45
- ma60: 91.53
- ma120: 93.42
- return_5d: 0.12
- return_20d: -0.35
- volume_ratio: 1.42
- distance_to_ma20_pct_auxiliary: 1.36
- distance_to_high_60_pct: -14.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,85.7,85.7,84.2,84.4,154000,90.89,-7.14,92.08,94.69,0.62
20260504,84.4,84.4,82.9,83,311000,90.23,-8.01,91.31,94.48,1.19
20260505,83,83.3,82,83.3,145000,89.65,-7.09,90.58,94.28,0.55
20260506,83.3,85,82.8,84.5,178000,89.22,-5.29,89.89,94.09,0.67
20260507,85,86.2,84.5,85.2,220000,88.89,-4.15,89.23,93.94,0.82
20260508,85.6,85.6,83.7,83.7,198000,88.46,-5.38,88.53,93.76,0.74
20260511,83.7,84.5,83.5,84.2,101000,88.1,-4.43,87.82,93.6,0.39
20260512,84.2,84.4,83.7,83.7,113000,87.73,-4.6,87.06,93.43,0.47
20260513,84,84,83.4,83.8,108000,87.41,-4.13,86.33,93.26,0.48
20260514,83.8,84,83.4,83.6,90000,87.09,-4.01,85.56,93.08,0.44
20260515,83.7,84.6,83.7,84,156000,86.83,-3.26,85.22,92.92,0.8
20260518,84.2,85.8,84.2,85.1,103000,86.69,-1.83,84.95,92.77,0.54
20260519,85.1,85.1,84.7,84.8,53000,86.53,-2,84.73,92.62,0.3
20260520,84.9,85.1,84.8,85.1,56000,86.41,-1.52,84.58,92.47,0.33
20260521,85.8,86.3,85.2,85.5,104000,86.34,-0.97,84.54,92.32,0.69
20260522,85.5,85.5,84.5,84.8,85000,86.21,-1.63,84.52,92.16,0.61
20260525,85.2,85.2,84.3,84.5,85000,86.07,-1.82,84.51,92,0.63
20260526,84.3,84.9,84,84.7,84000,85.95,-1.46,84.53,91.84,0.64
20260527,84.7,85.5,84.7,85.5,85000,85.91,-0.48,84.47,91.69,0.68
20260528,85.5,86.7,85.2,85.6,185777,85.89,-0.33,84.45,91.53,1.42
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.03
- over_600_ratio: 44.31
- over_800_ratio: 44.31
- over_1000_ratio: 40.75
- over_400_change_1w: 0.74
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.93,,42.71,,41.03,,0,False,False
20260508,48.23,0.3,44.33,1.62,40.93,-0.1,1,False,True
20260515,48.29,0.06,44.39,0.06,40.84,-0.09,2,False,True
20260522,49.03,0.74,44.31,-0.08,40.75,-0.09,3,False,False
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
