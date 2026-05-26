# INDIVIDUAL STOCK CHATGPT PACKET - 1470 大統新創

## Metadata
- generated_at: 2026-05-26 22:18:06 Asia/Taipei
- stock_id: 1470
- stock_name: 大統新創
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 97
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1470_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1470_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1470_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1470_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1470_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1470_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1470_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1470_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1470_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1470_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1470_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1470_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1470_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1470.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1470.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1470.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1470.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1470.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1470.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1470_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1470_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1470_latest.md?ref=main

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
- open: 22
- high: 22
- low: 21.7
- close: 21.7
- volume: 16059
- ma5: 21.74
- ema23_primary: 22.03
- distance_to_ema23_pct: -1.5
- ma20: 22.07
- ma60: 22.44
- ma120: 22.55
- return_5d: 2.84
- return_20d: -3.98
- volume_ratio: 0.49
- distance_to_ma20_pct_auxiliary: -1.68
- distance_to_high_60_pct: -11.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,21.95,22.45,21.95,22.45,2159,22.54,-0.39,22.36,22.7,0.16
20260428,23.3,23.3,22.3,23.25,13584,22.6,2.88,22.41,22.71,0.99
20260429,23.2,23.2,22.5,22.5,9065,22.59,-0.4,22.45,22.7,0.67
20260504,22.25,22.25,22.15,22.25,5005,22.56,-1.38,22.48,22.69,0.37
20260505,22.05,22.55,21.8,22.25,12003,22.54,-1.27,22.48,22.68,0.9
20260506,22.5,22.8,21.9,22.5,40883,22.53,-0.15,22.53,22.68,2.76
20260507,22.4,22.85,22.2,22.25,42001,22.51,-1.15,22.57,22.67,2.51
20260508,22.9,22.9,22.15,22.55,16605,22.51,0.17,22.57,22.66,1
20260511,22.15,22.35,22.15,22.25,37030,22.49,-1.07,22.57,22.65,2.12
20260512,21.65,22.4,21.65,22.3,45005,22.47,-0.78,22.58,22.64,2.29
20260513,21.65,21.65,21.5,21.5,4470,22.39,-3.99,22.57,22.62,0.23
20260514,21.25,21.8,21.25,21.4,26010,22.31,-4.08,22.5,22.6,1.36
20260515,21.85,21.85,21.85,21.85,1100,22.27,-1.9,22.46,22.58,0.06
20260518,22.55,22.55,22.3,22.3,2107,22.27,0.11,22.41,22.57,0.12
20260519,21.2,21.3,20.9,21.1,327153,22.18,-4.86,22.31,22.54,10.09
20260520,20.65,21.15,20.5,21.1,36155,22.09,-4.47,22.23,22.5,1.07
20260521,21.3,21.9,21.3,21.9,6266,22.07,-0.78,22.18,22.49,0.19
20260522,21.95,22,21.95,22,11001,22.07,-0.3,22.13,22.48,0.33
20260525,22,22,22,22,5000,22.06,-0.27,22.11,22.46,0.15
20260526,22,22,21.7,21.7,16059,22.03,-1.5,22.07,22.44,0.49
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 87.63
- over_600_ratio: 81.48
- over_800_ratio: 77.67
- over_1000_ratio: 71.51
- over_400_change_1w: 0.2
- over_800_change_1w: 0.24
- over_1000_change_1w: 0.24
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.48,,77.4,,71.24,,0,False,False
20260508,87.48,0,77.43,0.03,71.27,0.03,1,False,True
20260515,87.43,-0.05,77.43,0,71.27,0,0,False,False
20260522,87.63,0.2,77.67,0.24,71.51,0.24,1,True,True
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
