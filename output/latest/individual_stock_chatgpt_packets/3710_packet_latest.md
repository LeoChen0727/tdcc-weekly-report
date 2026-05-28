# INDIVIDUAL STOCK CHATGPT PACKET - 3710 連展投控

## Metadata
- generated_at: 2026-05-28 19:32:36 Asia/Taipei
- stock_id: 3710
- stock_name: 連展投控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3710_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3710_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3710_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3710_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3710_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3710_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3710_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3710_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3710_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3710_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3710_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3710_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3710_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3710.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3710.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3710.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3710.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3710.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3710.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3710_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3710_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3710_latest.md?ref=main

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
- open: 6.4
- high: 6.4
- low: 6.1
- close: 6.23
- volume: 331438
- ma5: 6.26
- ema23_primary: 6.41
- distance_to_ema23_pct: -2.88
- ma20: 6.38
- ma60: 6.52
- ma120: 6.37
- return_5d: -1.11
- return_20d: -11.51
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: -2.28
- distance_to_high_60_pct: -31.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,6.9,7.1,6.9,6.99,468000,6.92,1.04,6.86,6.67,0.47
20260504,7.06,7.1,6.9,6.9,388000,6.92,-0.24,6.87,6.67,0.39
20260505,6.95,6.95,6.72,6.84,354000,6.91,-1.01,6.9,6.67,0.36
20260506,6.84,6.84,6.22,6.47,716000,6.87,-5.87,6.9,6.66,0.7
20260507,6.32,6.65,6.32,6.49,552000,6.84,-5.14,6.91,6.65,0.54
20260508,6.5,6.5,6.22,6.29,909000,6.8,-7.44,6.91,6.64,0.86
20260511,6.3,6.31,5.7,6.01,872000,6.73,-10.7,6.9,6.62,0.81
20260512,6.02,6.4,6.02,6.38,580000,6.7,-4.79,6.91,6.61,0.53
20260513,6.34,6.56,6.06,6.22,579000,6.66,-6.62,6.9,6.6,0.52
20260514,6.22,6.3,6.08,6.23,467000,6.62,-5.96,6.9,6.59,0.42
20260515,6.22,6.23,6.09,6.18,339000,6.59,-6.19,6.9,6.58,0.31
20260518,5.96,6.79,5.95,6.5,746000,6.58,-1.22,6.88,6.58,0.68
20260519,6.46,6.46,6.2,6.22,252000,6.55,-5.04,6.82,6.57,0.27
20260520,6.19,6.23,6.12,6.17,180000,6.52,-5.35,6.71,6.56,0.22
20260521,6.15,6.4,6.01,6.3,330000,6.5,-3.08,6.61,6.55,0.55
20260522,6.21,6.6,6.19,6.39,6000,6.49,-1.56,6.55,6.54,0.01
20260525,6.31,6.52,6.22,6.35,6000,6.48,-2,6.5,6.53,0.01
20260526,6.35,6.35,6.1,6.1,6000,6.45,-5.4,6.46,6.52,0.01
20260527,6.12,6.25,6.11,6.25,6000,6.43,-2.82,6.42,6.52,0.01
20260528,6.4,6.4,6.1,6.23,331438,6.41,-2.88,6.38,6.52,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 31.09
- over_600_ratio: 26.41
- over_800_ratio: 23.17
- over_1000_ratio: 21.94
- over_400_change_1w: 0.13
- over_800_change_1w: -0.15
- over_1000_change_1w: 0.43
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.82,,22.67,,21.39,,0,False,False
20260508,30.97,0.15,22.7,0.03,21.44,0.05,1,False,True
20260515,30.96,-0.01,23.32,0.62,21.51,0.07,2,False,True
20260522,31.09,0.13,23.17,-0.15,21.94,0.43,3,False,True
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
