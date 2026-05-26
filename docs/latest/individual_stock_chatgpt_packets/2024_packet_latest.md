# INDIVIDUAL STOCK CHATGPT PACKET - 2024 志聯

## Metadata
- generated_at: 2026-05-26 23:53:07 Asia/Taipei
- stock_id: 2024
- stock_name: 志聯
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 126
- latest_tdcc_date: 20260522
- tdcc_rows: 26
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2024_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2024_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2024_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2024_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2024_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2024_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2024_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2024_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2024_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2024_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2024_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2024_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2024_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2024.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2024.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2024.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2024.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2024.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2024.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2024_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2024_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2024_latest.md?ref=main

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
- open: 14.2
- high: 14.2
- low: 13.9
- close: 14
- volume: 11305
- ma5: 14.01
- ema23_primary: 13.99
- distance_to_ema23_pct: 0.08
- ma20: 13.86
- ma60: 14.62
- ma120: 15.36
- return_5d: 5.66
- return_20d: -2.78
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: 1.05
- distance_to_high_60_pct: -16.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,14.35,14.35,13.8,13.8,26678,14.62,-5.59,14.57,15.3,1.59
20260428,14.2,14.2,14,14.15,17062,14.58,-2.94,14.53,15.26,1.02
20260429,14.1,14.35,14.1,14.1,16752,14.54,-3.02,14.5,15.23,0.97
20260430,14.1,14.3,14.1,14.1,26264,14.5,-2.77,14.46,15.21,1.42
20260504,14.1,14.1,13.8,13.8,18520,14.44,-4.46,14.42,15.17,0.99
20260505,13.9,14.3,13.9,14.05,21613,14.41,-2.5,14.39,15.14,1.09
20260506,14.35,14.35,13.95,13.95,33172,14.37,-2.94,14.36,15.12,1.58
20260507,13.9,13.95,13.9,13.95,10116,14.34,-2.7,14.33,15.09,0.51
20260508,14.2,14.3,14.2,14.3,6086,14.33,-0.24,14.31,15.07,0.31
20260511,14.05,14.15,13.9,13.9,15686,14.3,-2.78,14.28,15.03,0.78
20260512,13.8,13.8,13.2,13.55,75336,14.24,-4.82,14.22,14.98,3.44
20260513,13.3,13.75,13.3,13.65,35141,14.19,-3.78,14.17,14.94,1.54
20260514,13.45,13.55,13.4,13.4,13713,14.12,-5.11,14.12,14.9,0.6
20260515,13.4,13.5,13.1,13.1,33297,14.04,-6.67,14.04,14.85,1.42
20260518,13.1,13.3,13.1,13.25,10789,13.97,-5.16,13.96,14.8,0.47
20260519,13.45,13.85,13.45,13.85,28888,13.96,-0.79,13.93,14.77,1.26
20260520,13.6,13.8,13.6,13.8,3794,13.95,-1.06,13.89,14.73,0.17
20260521,13.8,14.3,13.8,14.15,40298,13.96,1.33,13.88,14.7,1.69
20260525,14.3,14.4,13.9,14.25,46987,13.99,1.87,13.88,14.66,1.85
20260526,14.2,14.2,13.9,14,11305,13.99,0.08,13.86,14.62,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.88
- over_600_ratio: 81.33
- over_800_ratio: 80.66
- over_1000_ratio: 80.66
- over_400_change_1w: 0.09
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260306,82.69,0,80.47,0,80.47,0,0,False,False
20260313,82.69,0,80.47,0,80.47,0,0,False,False
20260320,82.69,0,80.47,0,80.47,0,0,False,False
20260327,82.7,0.01,80.48,0.01,80.48,0.01,1,True,True
20260402,82.7,0,80.48,0,80.48,0,0,False,False
20260410,82.7,0,80.48,0,80.48,0,0,False,False
20260417,82.7,0,80.48,0,80.48,0,0,False,False
20260424,82.71,0.01,80.49,0.01,80.49,0.01,1,True,True
20260430,82.73,0.02,80.51,0.02,80.51,0.02,2,True,True
20260508,82.76,0.03,80.54,0.03,80.54,0.03,3,True,True
20260515,82.79,0.03,80.57,0.03,80.57,0.03,4,True,True
20260522,82.88,0.09,80.66,0.09,80.66,0.09,5,True,True
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
