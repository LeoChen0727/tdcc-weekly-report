# INDIVIDUAL STOCK CHATGPT PACKET - 2033 佳大

## Metadata
- generated_at: 2026-05-26 23:53:08 Asia/Taipei
- stock_id: 2033
- stock_name: 佳大
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2033_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2033_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2033_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2033_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2033_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2033_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2033_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2033_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2033_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2033_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2033_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2033_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2033_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2033.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2033.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2033.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2033.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2033.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2033.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2033_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2033_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2033_latest.md?ref=main

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
- open: 15.8
- high: 15.8
- low: 15.15
- close: 15.4
- volume: 213880
- ma5: 15.35
- ema23_primary: 15.42
- distance_to_ema23_pct: -0.14
- ma20: 15.29
- ma60: 15.84
- ma120: 15.91
- return_5d: 2.67
- return_20d: -4.05
- volume_ratio: 0.84
- distance_to_ma20_pct_auxiliary: 0.74
- distance_to_high_60_pct: -11.24

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,16,16.1,15.8,16.1,108118,16.24,-0.83,16.26,16.18,0.89
20260429,15.9,16.05,15.9,16.05,89152,16.22,-1.05,16.28,16.18,0.73
20260430,16.1,16.1,15.3,15.5,389926,16.16,-4.08,16.29,16.17,2.87
20260504,15.5,15.5,15,15.3,726332,16.09,-4.9,16.26,16.16,4.29
20260505,15.15,15.3,15.15,15.3,78002,16.02,-4.51,16.24,16.14,0.46
20260506,15.3,15.5,15.1,15.5,176068,15.98,-3,16.21,16.13,1.01
20260507,15.4,15.4,14.9,15.15,543263,15.91,-4.78,16.16,16.12,2.77
20260508,15.1,15.2,14.9,15.2,163720,15.85,-4.11,16.09,16.1,0.82
20260511,15.2,15.2,14.95,15.1,287103,15.79,-4.36,16.01,16.07,1.42
20260512,15.15,15.15,14.8,15.05,207250,15.73,-4.3,15.93,16.04,0.99
20260513,15,15,14.8,15,223115,15.67,-4.25,15.86,16.03,1.04
20260514,15,15,14.75,15,157343,15.61,-3.91,15.78,16,0.73
20260515,14.8,14.9,14.75,14.85,133349,15.55,-4.49,15.69,15.97,0.62
20260518,14.85,14.9,14.55,14.9,667152,15.49,-3.83,15.61,15.95,2.76
20260519,14.9,15,14.7,15,118033,15.45,-2.93,15.52,15.93,0.49
20260520,14.85,15.15,14.8,15.15,92227,15.43,-1.8,15.45,15.91,0.39
20260521,15.15,15.15,15,15.15,100378,15.4,-1.65,15.39,15.89,0.43
20260522,15,15.45,15,15.45,164758,15.41,0.27,15.35,15.88,0.7
20260525,15.6,16.05,15.35,15.6,460859,15.42,1.14,15.32,15.86,1.83
20260526,15.8,15.8,15.15,15.4,213880,15.42,-0.14,15.29,15.84,0.84
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74
- over_600_ratio: 70.42
- over_800_ratio: 68.58
- over_1000_ratio: 59.45
- over_400_change_1w: 0.33
- over_800_change_1w: -0.61
- over_1000_change_1w: -1.85
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.11,,69.8,,60.71,,0,False,False
20260508,74.06,-1.05,68.94,-0.86,61.05,0.34,1,False,True
20260515,73.67,-0.39,69.19,0.25,61.3,0.25,2,False,True
20260522,74,0.33,68.58,-0.61,59.45,-1.85,3,False,False
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
