# INDIVIDUAL STOCK CHATGPT PACKET - 1109 信大

## Metadata
- generated_at: 2026-05-26 23:00:07 Asia/Taipei
- stock_id: 1109
- stock_name: 信大
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1109_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1109_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1109_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1109_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1109_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1109_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1109_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1109_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1109_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1109_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1109_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1109_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1109_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1109.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1109.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1109.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1109.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1109.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1109.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1109_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1109_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1109_latest.md?ref=main

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
- open: 14.4
- high: 14.5
- low: 14.35
- close: 14.5
- volume: 181234
- ma5: 14.54
- ema23_primary: 14.98
- distance_to_ema23_pct: -3.21
- ma20: 15.08
- ma60: 15.28
- ma120: 15.4
- return_5d: -0.68
- return_20d: -6.15
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: -3.85
- distance_to_high_60_pct: -9.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,15.5,15.5,15.35,15.5,98467,15.41,0.61,15.39,15.41,0.63
20260429,15.5,15.5,15.4,15.45,68797,15.41,0.26,15.4,15.41,0.46
20260430,15.45,15.45,15.35,15.45,140092,15.41,0.24,15.41,15.41,0.98
20260504,15.45,15.5,15.4,15.45,95125,15.42,0.22,15.43,15.42,0.69
20260505,15.3,15.45,15.3,15.4,137365,15.41,-0.09,15.43,15.42,0.97
20260506,15.45,15.45,15.3,15.4,177696,15.41,-0.09,15.44,15.41,1.19
20260507,15.4,15.45,15.3,15.4,136373,15.41,-0.08,15.44,15.41,0.93
20260508,15.45,15.45,15.4,15.4,122570,15.41,-0.07,15.43,15.41,0.81
20260511,15.45,15.5,15.3,15.5,283942,15.42,0.53,15.44,15.41,1.75
20260512,15.4,15.4,15.3,15.3,72174,15.41,-0.71,15.43,15.41,0.44
20260513,15.3,15.4,15.1,15.4,84725,15.41,-0.05,15.43,15.41,0.53
20260514,15.3,15.3,14.95,15.2,922378,15.39,-1.24,15.41,15.41,4.68
20260515,15.05,15.05,14.8,14.85,471539,15.35,-3.23,15.38,15.4,2.22
20260518,14.8,14.8,14.45,14.6,492854,15.28,-4.47,15.34,15.38,2.17
20260519,14.65,14.65,14.4,14.6,181185,15.23,-4.11,15.3,15.37,0.81
20260520,14.45,14.6,14.45,14.6,87290,15.17,-3.78,15.26,15.36,0.39
20260521,14.6,14.65,14.55,14.65,101794,15.13,-3.18,15.22,15.35,0.46
20260522,14.65,14.65,14.4,14.55,402830,15.08,-3.53,15.18,15.33,1.8
20260525,14.6,14.6,14.4,14.4,404137,15.03,-4.16,15.13,15.3,1.71
20260526,14.4,14.5,14.35,14.5,181234,14.98,-3.21,15.08,15.28,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.68
- over_600_ratio: 76.52
- over_800_ratio: 74.69
- over_1000_ratio: 72.8
- over_400_change_1w: -0.04
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.81,,74.63,,72.49,,0,False,False
20260508,79.97,0.16,74.67,0.04,72.49,0,1,False,True
20260515,79.72,-0.25,74.68,0.01,72.79,0.3,2,False,True
20260522,79.68,-0.04,74.69,0.01,72.8,0.01,3,False,True
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
