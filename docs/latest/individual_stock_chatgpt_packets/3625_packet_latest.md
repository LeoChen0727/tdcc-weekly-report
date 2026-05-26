# INDIVIDUAL STOCK CHATGPT PACKET - 3625 西勝

## Metadata
- generated_at: 2026-05-26 21:25:38 Asia/Taipei
- stock_id: 3625
- stock_name: 西勝
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3625_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3625_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3625_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3625_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3625_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3625_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3625_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3625_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3625_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3625_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3625_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3625_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3625_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3625.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3625.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3625.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3625.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3625.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3625.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3625_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3625_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3625_latest.md?ref=main

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
- open: 15.05
- high: 15.05
- low: 14.3
- close: 14.5
- volume: 14000
- ma5: 14.63
- ema23_primary: 15.27
- distance_to_ema23_pct: -5.01
- ma20: 15.18
- ma60: 16.52
- ma120: 18.26
- return_5d: 3.57
- return_20d: -16.43
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: -4.5
- distance_to_high_60_pct: -25.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,17.4,17.4,17,17.15,350000,17.32,-0.98,17.07,17.89,0.56
20260429,17.15,17.15,17,17.1,291000,17.3,-1.16,17.06,17.85,0.46
20260430,17,17,16.4,16.55,735000,17.24,-3.99,17.03,17.78,1.13
20260504,16.55,16.8,16.2,16.55,421000,17.18,-3.67,17.02,17.71,0.64
20260505,16.25,16.7,16.25,16.6,447000,17.13,-3.11,17.03,17.65,0.67
20260506,16.6,16.6,15,15.6,2359000,17,-8.26,17.01,17.58,3.06
20260507,15.45,15.75,15.25,15.3,818000,16.86,-9.27,16.92,17.5,1.02
20260508,15.3,15.9,15.15,15.3,603000,16.73,-8.56,16.85,17.43,0.74
20260511,15.3,15.35,14.75,15.1,556000,16.6,-9.02,16.79,17.36,0.67
20260512,15.1,15.2,14.65,14.65,644000,16.43,-10.86,16.69,17.3,0.75
20260513,14.5,15,14.25,14.9,665000,16.31,-8.63,16.61,17.23,0.77
20260514,14.55,14.55,13.55,13.9,1257000,16.11,-13.7,16.45,17.14,1.39
20260515,14.5,14.65,13.65,13.9,756000,15.92,-12.7,16.3,17.04,0.81
20260518,13.1,13.9,13.1,13.9,310000,15.75,-11.77,16.14,16.95,0.33
20260519,14,14.05,13.6,14,264000,15.61,-10.3,15.99,16.87,0.29
20260520,14.2,14.45,13.75,14.4,223000,15.51,-7.14,15.86,16.8,0.24
20260521,14.85,14.85,14.3,14.6,370000,15.43,-5.39,15.71,16.73,0.41
20260522,14.8,14.8,14.45,14.8,15000,15.38,-3.76,15.48,16.66,0.02
20260525,14.85,15.2,14.8,14.85,15000,15.33,-3.16,15.32,16.59,0.03
20260526,15.05,15.05,14.3,14.5,14000,15.27,-5.01,15.18,16.52,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 43.34
- over_600_ratio: 40.71
- over_800_ratio: 37.13
- over_1000_ratio: 35.72
- over_400_change_1w: 0.41
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.33,,37.38,,35.17,,0,False,False
20260508,43.51,-0.82,37.34,-0.04,35.18,0.01,1,False,True
20260515,42.93,-0.58,37.12,-0.22,35.71,0.53,2,False,True
20260522,43.34,0.41,37.13,0.01,35.72,0.01,3,True,True
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
