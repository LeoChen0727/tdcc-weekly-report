# INDIVIDUAL STOCK CHATGPT PACKET - 3288 點晶

## Metadata
- generated_at: 2026-05-26 23:53:44 Asia/Taipei
- stock_id: 3288
- stock_name: 點晶
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 130
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3288_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3288_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3288_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3288_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3288_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3288_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3288_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3288_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3288_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3288_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3288_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3288_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3288_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3288.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3288.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3288.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3288.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3288.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3288.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3288_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3288_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3288_latest.md?ref=main

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
- open: 14.65
- high: 14.9
- low: 14.65
- close: 14.9
- volume: 15000
- ma5: 14.94
- ema23_primary: 15.09
- distance_to_ema23_pct: -1.28
- ma20: 15.09
- ma60: 15.19
- ma120: 15.82
- return_5d: -0.67
- return_20d: 2.05
- volume_ratio: 1.2
- distance_to_ma20_pct_auxiliary: -1.23
- distance_to_high_60_pct: -8.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,14.6,15.75,14.6,15.75,22000,15.38,2.41,15.23,15.6,1.35
20260429,15.65,15.65,15,15.45,10000,15.38,0.42,15.28,15.57,0.62
20260430,15.1,15.45,14.95,15.45,14000,15.39,0.39,15.31,15.55,0.84
20260504,14.95,15,14.55,14.55,24000,15.32,-5.03,15.31,15.51,1.36
20260505,14.55,14.7,14.55,14.7,7000,15.27,-3.72,15.32,15.47,0.4
20260506,14.75,15.25,14.75,15.15,20000,15.26,-0.71,15.31,15.44,1.14
20260507,15.05,15.1,14.8,15.1,20000,15.25,-0.95,15.31,15.41,1.1
20260508,15.1,15.25,14.85,14.85,10000,15.21,-2.38,15.3,15.39,0.55
20260511,14.8,15.1,14.8,15.1,5000,15.2,-0.68,15.3,15.36,0.28
20260512,15.1,15.4,15,15.25,20000,15.21,0.28,15.33,15.35,1.15
20260513,14.7,15.25,14.7,15.25,4000,15.21,0.26,15.36,15.34,0.23
20260514,15.25,15.5,14.9,14.95,16000,15.19,-1.57,15.36,15.31,0.95
20260515,15,15.25,15,15.25,5000,15.19,0.37,15.34,15.3,0.32
20260518,14.8,15.2,14.8,15.2,5000,15.19,0.04,15.31,15.29,0.35
20260519,14.9,15,14.85,15,4000,15.18,-1.17,15.28,15.27,0.29
20260520,14.9,15,14.85,15,11000,15.16,-1.08,15.21,15.25,0.86
20260521,15,15,14.95,14.95,8000,15.15,-1.29,15.15,15.23,0.67
20260522,15,15,14.9,14.95,15000,15.13,-1.19,15.12,15.21,1.27
20260525,14.9,14.95,14.35,14.9,15000,15.11,-1.39,15.07,15.2,1.2
20260526,14.65,14.9,14.65,14.9,15000,15.09,-1.28,15.09,15.19,1.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.21
- over_600_ratio: 41.91
- over_800_ratio: 41.91
- over_1000_ratio: 36.75
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
20260430,46.97,,40.52,,35.24,,0,False,False
20260508,46.97,0,40.52,0,35.24,0,0,False,False
20260515,48.21,1.24,41.91,1.39,36.75,1.51,1,True,True
20260522,48.21,0,41.91,0,36.75,0,0,False,False
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
