# INDIVIDUAL STOCK CHATGPT PACKET - 4406 新昕纖

## Metadata
- generated_at: 2026-05-26 21:25:47 Asia/Taipei
- stock_id: 4406
- stock_name: 新昕纖
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 115
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4406_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4406_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4406_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4406_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4406_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4406_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4406_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4406_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4406_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4406_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4406_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4406_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4406_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4406.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4406.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4406.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4406.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4406.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4406.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4406_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4406_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4406_latest.md?ref=main

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
- open: 10
- high: 10.15
- low: 10
- close: 10
- volume: 10000
- ma5: 10
- ema23_primary: 10.01
- distance_to_ema23_pct: -0.13
- ma20: 10.01
- ma60: 10.03
- ma120: 10.03
- return_5d: -0.5
- return_20d: -0.5
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: -0.1
- distance_to_high_60_pct: -10.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,10,10.05,9.96,10.05,16000,10.06,-0.11,10.05,10.09,0.51
20260429,10,10,10,10,11000,10.06,-0.56,10.04,10.09,0.34
20260430,9.97,10.1,9.95,10.1,21000,10.06,0.4,10.05,10.1,0.64
20260504,10.1,10.15,10.05,10.15,14000,10.07,0.82,10.05,10.1,0.42
20260505,10.05,10.05,10.05,10.05,11000,10.07,-0.16,10.05,10.1,0.32
20260506,10,10,10,10,11000,10.06,-0.6,10.04,10.1,0.32
20260507,10.05,10.05,9.97,10,36000,10.06,-0.55,10.04,10.1,1
20260508,10,10,10,10,12000,10.05,-0.51,10.04,10.1,0.33
20260511,9.95,9.95,9.95,9.95,74000,10.04,-0.92,10.04,10.09,1.88
20260512,9.95,10,9.95,10,14000,10.04,-0.39,10.04,10.09,0.35
20260513,10,10,9.9,9.95,25000,10.03,-0.81,10.04,10.08,0.62
20260514,9.95,10,9.9,10,18000,10.03,-0.29,10.05,10.07,0.44
20260515,10,10,9.81,9.91,486000,10.02,-1.09,10.05,10.06,7.52
20260518,9.95,10,9.91,10,207000,10.02,-0.17,10.05,10.06,2.77
20260519,10.1,10.1,10.05,10.05,4000,10.02,0.3,10.05,10.05,0.05
20260520,10.15,10.15,9.95,10,21000,10.02,-0.18,10.04,10.05,0.28
20260521,10,10,10,10,5000,10.02,-0.17,10.01,10.05,0.09
20260522,10,10.15,10,10,10000,10.02,-0.15,10.01,10.04,0.2
20260525,10.05,10.05,10,10,10000,10.01,-0.14,10.01,10.04,0.2
20260526,10,10.15,10,10,10000,10.01,-0.13,10.01,10.03,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.64
- over_600_ratio: 67.87
- over_800_ratio: 64.07
- over_1000_ratio: 59.1
- over_400_change_1w: -1.38
- over_800_change_1w: 0.78
- over_1000_change_1w: 0.78
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.77,,63.03,,58.06,,0,False,False
20260508,75.84,0.07,63.1,0.07,58.13,0.07,1,True,True
20260515,76.02,0.18,63.29,0.19,58.32,0.19,2,True,True
20260522,74.64,-1.38,64.07,0.78,59.1,0.78,3,False,True
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
