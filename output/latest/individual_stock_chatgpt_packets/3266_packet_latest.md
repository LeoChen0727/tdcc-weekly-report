# INDIVIDUAL STOCK CHATGPT PACKET - 3266 昇陽

## Metadata
- generated_at: 2026-05-30 23:41:57 Asia/Taipei
- stock_id: 3266
- stock_name: 昇陽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3266_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3266_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3266_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3266_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3266_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3266_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3266_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3266_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3266_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3266_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3266_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3266_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3266_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3266.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3266.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3266.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3266.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3266.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3266.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3266_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3266_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3266_latest.md?ref=main

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
- date: 20260529
- open: 12.75
- high: 13.05
- low: 12.75
- close: 12.85
- volume: 114513
- ma5: 12.76
- ema23_primary: 12.93
- distance_to_ema23_pct: -0.61
- ma20: 12.92
- ma60: 13.31
- ma120: 13.61
- return_5d: 3.63
- return_20d: -4.81
- volume_ratio: 0.89
- distance_to_ma20_pct_auxiliary: -0.56
- distance_to_high_60_pct: -9.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,13.45,13.45,13.3,13.35,78112,13.61,-1.91,13.66,13.62,1.02
20260505,13.35,13.55,13.3,13.5,31792,13.6,-0.74,13.68,13.61,0.41
20260506,13.9,13.9,13.55,13.65,65059,13.61,0.33,13.71,13.61,0.83
20260507,13.65,13.7,13.35,13.5,117080,13.6,-0.71,13.71,13.6,1.47
20260508,13.8,13.8,13.35,13.75,76437,13.61,1.03,13.71,13.6,0.94
20260511,13.65,13.7,13.5,13.55,120215,13.6,-0.4,13.71,13.6,1.42
20260512,13.55,13.55,13.2,13.2,180298,13.57,-2.73,13.68,13.59,1.98
20260513,13.25,13.3,13,13.1,123020,13.53,-3.19,13.64,13.58,1.35
20260514,13.05,13.2,12.7,12.7,232771,13.46,-5.66,13.59,13.56,2.37
20260515,12.75,13,12.55,12.6,147771,13.39,-5.9,13.52,13.54,1.48
20260518,12.55,12.6,12.5,12.5,69562,13.32,-6.13,13.44,13.53,0.69
20260519,12.5,12.55,12.45,12.45,53881,13.24,-5.99,13.35,13.51,0.55
20260520,12.4,12.4,11.9,12.15,352357,13.15,-7.62,13.27,13.49,3.23
20260521,12.15,12.35,12.1,12.25,65620,13.08,-6.33,13.19,13.46,0.61
20260522,12.4,12.6,12.25,12.4,155648,13.02,-4.77,13.13,13.43,1.41
20260525,12.6,12.85,12.3,12.85,300305,13.01,-1.21,13.09,13.4,2.49
20260526,12.85,12.9,12.65,12.8,92678,12.99,-1.46,13.05,13.38,0.75
20260527,12.8,12.85,12.5,12.55,141820,12.95,-3.11,13,13.36,1.12
20260528,12.7,12.8,12.65,12.75,63531,12.94,-1.44,12.96,13.33,0.5
20260529,12.75,13.05,12.75,12.85,114513,12.93,-0.61,12.92,13.31,0.89
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 90.13
- over_600_ratio: 89.74
- over_800_ratio: 89.34
- over_1000_ratio: 89.08
- over_400_change_1w: -0.14
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,90.29,,89.2,,88.94,,0,False,False
20260508,90.3,0.01,89.21,0.01,88.95,0.01,1,True,True
20260515,90.2,-0.1,89.26,0.05,89,0.05,2,False,True
20260522,90.27,0.07,89.33,0.07,89.07,0.07,3,True,True
20260529,90.13,-0.14,89.34,0.01,89.08,0.01,4,False,True
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
