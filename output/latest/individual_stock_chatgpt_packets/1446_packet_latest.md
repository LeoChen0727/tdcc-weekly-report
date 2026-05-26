# INDIVIDUAL STOCK CHATGPT PACKET - 1446 宏和

## Metadata
- generated_at: 2026-05-26 23:52:54 Asia/Taipei
- stock_id: 1446
- stock_name: 宏和
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1446_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1446_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1446_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1446_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1446_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1446_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1446_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1446_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1446_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1446_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1446_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1446_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1446_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1446.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1446.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1446.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1446.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1446.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1446.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1446_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1446_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1446_latest.md?ref=main

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
- open: 15.5
- high: 15.65
- low: 15.4
- close: 15.65
- volume: 162481
- ma5: 15.57
- ema23_primary: 15.67
- distance_to_ema23_pct: -0.12
- ma20: 15.54
- ma60: 16.11
- ma120: 16.92
- return_5d: 0.97
- return_20d: -1.57
- volume_ratio: 0.8
- distance_to_ma20_pct_auxiliary: 0.68
- distance_to_high_60_pct: -10.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,16,16.05,15.8,15.9,119528,16.37,-2.9,16.39,16.54,0.63
20260429,15.9,15.95,15.6,15.8,150041,16.33,-3.22,16.34,16.52,0.79
20260430,15.8,15.85,15.65,15.8,166428,16.28,-2.96,16.31,16.49,0.93
20260504,15.8,15.9,15.65,15.65,143052,16.23,-3.57,16.25,16.46,0.82
20260505,15.6,15.65,15.45,15.55,122228,16.17,-3.85,16.21,16.43,0.73
20260506,15.55,15.65,15.45,15.6,155107,16.13,-3.26,16.18,16.4,0.92
20260507,15.65,15.8,15.6,15.75,199571,16.09,-2.14,16.14,16.37,1.17
20260508,15.75,15.85,15.75,15.8,124124,16.07,-1.68,16.11,16.34,0.71
20260511,15.8,15.8,15.45,15.6,325476,16.03,-2.69,16.07,16.32,1.76
20260512,15.6,15.6,15.45,15.55,307160,15.99,-2.75,16.02,16.3,1.59
20260513,15.75,15.75,15.1,15.1,743675,15.92,-5.13,15.96,16.28,3.35
20260514,15.2,15.35,15.2,15.2,219342,15.86,-4.14,15.9,16.25,0.97
20260515,15.3,15.45,15.1,15.1,176720,15.79,-4.39,15.82,16.22,0.77
20260518,15.2,15.3,15.05,15.15,85939,15.74,-3.75,15.75,16.2,0.38
20260519,15.2,15.55,15.2,15.5,133834,15.72,-1.4,15.7,16.18,0.6
20260520,15.65,15.8,15.3,15.45,150651,15.7,-1.58,15.65,16.16,0.67
20260521,15.55,15.7,15.55,15.55,114139,15.69,-0.86,15.61,16.15,0.53
20260522,15.5,15.8,15.45,15.7,142915,15.69,0.09,15.58,16.13,0.7
20260525,15.8,15.8,15.35,15.5,338404,15.67,-1.09,15.56,16.12,1.64
20260526,15.5,15.65,15.4,15.65,162481,15.67,-0.12,15.54,16.11,0.8
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.02
- over_600_ratio: 65.96
- over_800_ratio: 65.07
- over_1000_ratio: 63.89
- over_400_change_1w: -0.2
- over_800_change_1w: 0.58
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.8,,63.89,,63.89,,0,False,False
20260508,68.83,0.03,64.47,0.58,63.89,0,1,False,True
20260515,68.22,-0.61,64.49,0.02,63.89,0,2,False,True
20260522,68.02,-0.2,65.07,0.58,63.89,0,3,False,True
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
