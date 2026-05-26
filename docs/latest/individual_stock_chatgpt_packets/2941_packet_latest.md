# INDIVIDUAL STOCK CHATGPT PACKET - 2941 米斯特

## Metadata
- generated_at: 2026-05-26 22:18:52 Asia/Taipei
- stock_id: 2941
- stock_name: 米斯特
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 93
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2941_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2941_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2941_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2941_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2941_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2941_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2941_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2941_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2941_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2941_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2941_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2941_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2941_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2941.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2941.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2941.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2941.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2941.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2941.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2941_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2941_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2941_latest.md?ref=main

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
- open: 31.8
- high: 31.8
- low: 31.8
- close: 31.8
- volume: 32000
- ma5: 31.5
- ema23_primary: 32.18
- distance_to_ema23_pct: -1.18
- ma20: 30.91
- ma60: 36.24
- ma120: 39.24
- return_5d: -1.55
- return_20d: -3.78
- volume_ratio: 2.3
- distance_to_ma20_pct_auxiliary: 2.9
- distance_to_high_60_pct: -27.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260424,32.35,32.35,31.5,31.5,42000,36.66,-14.06,37.24,40.33,3.75
20260427,31.45,31.5,29.5,30.95,28000,36.18,-14.45,36.73,40.08,2.33
20260429,30.9,30.9,30.15,30.15,4000,35.68,-15.49,36.2,39.81,0.33
20260430,30.5,30.5,30.5,30.5,4000,35.25,-13.46,35.62,39.56,0.33
20260504,30.5,30.6,30.5,30.6,4000,34.86,-12.22,35.04,39.3,0.33
20260505,30.55,30.65,30.5,30.65,8000,34.51,-11.18,34.48,39.04,0.68
20260506,30.4,30.4,29.8,29.8,15000,34.12,-12.65,34.03,38.78,1.21
20260507,30.05,30.1,30,30,12000,33.77,-11.17,33.59,38.56,0.93
20260508,30,30.1,29.8,30.1,12000,33.47,-10.06,33.24,38.34,0.91
20260511,30,30,29.5,30,16000,33.18,-9.58,32.84,38.12,1.17
20260512,29.1,29.85,29.1,29.85,10000,32.9,-9.27,32.47,37.91,0.72
20260513,29.5,29.6,29.5,29.6,10000,32.63,-9.27,32.17,37.7,0.7
20260514,30,32.1,30,31.7,8000,32.55,-2.61,31.85,37.51,0.56
20260515,31.05,32.95,30.85,32.9,15000,32.58,0.99,31.73,37.36,1.12
20260518,33.2,33.2,32.3,32.3,9000,32.55,-0.78,31.59,37.17,0.7
20260519,30.6,31.8,30.5,31.8,9000,32.49,-2.13,31.42,36.97,0.7
20260520,31.8,31.8,30.2,31.75,8000,32.43,-2.1,31.28,36.77,0.61
20260521,31,31,31,31,1000,32.31,-4.06,31.09,36.58,0.08
20260525,30.95,31.95,30.5,31.15,31000,32.21,-3.3,30.97,36.4,2.26
20260526,31.8,31.8,31.8,31.8,32000,32.18,-1.18,30.91,36.24,2.3
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.38
- over_600_ratio: 48.14
- over_800_ratio: 20.53
- over_1000_ratio: 20.53
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
20260430,66.36,,20.53,,20.53,,0,False,False
20260508,66.36,0,20.53,0,20.53,0,0,False,False
20260515,66.38,0.02,20.53,0,20.53,0,1,False,False
20260522,66.38,0,20.53,0,20.53,0,0,False,False
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
