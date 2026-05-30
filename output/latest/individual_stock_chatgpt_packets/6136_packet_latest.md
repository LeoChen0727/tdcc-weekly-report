# INDIVIDUAL STOCK CHATGPT PACKET - 6136 富爾特

## Metadata
- generated_at: 2026-05-30 23:42:50 Asia/Taipei
- stock_id: 6136
- stock_name: 富爾特
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6136_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6136_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6136_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6136_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6136_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6136_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6136_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6136_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6136_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6136_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6136_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6136_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6136_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6136.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6136.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6136.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6136.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6136.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6136.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6136_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6136_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6136_latest.md?ref=main

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
- open: 25.7
- high: 25.85
- low: 25.65
- close: 25.75
- volume: 247374
- ma5: 25.68
- ema23_primary: 25.37
- distance_to_ema23_pct: 1.49
- ma20: 25.26
- ma60: 24.83
- ma120: 24.43
- return_5d: 0
- return_20d: 1.38
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: 1.93
- distance_to_high_60_pct: -12.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,25.4,25.75,25.25,25.3,595874,25.35,-0.19,25.31,24.42,0.57
20260505,25.3,25.45,24.7,24.9,663201,25.31,-1.62,25.34,24.43,0.62
20260506,25,25,24.6,24.6,470324,25.25,-2.58,25.36,24.44,0.43
20260507,24.7,24.85,24.45,24.85,409435,25.22,-1.46,25.39,24.45,0.37
20260508,24.85,25.95,24.85,25.95,815412,25.28,2.65,25.48,24.49,0.71
20260511,26.15,26.15,25.5,25.55,687731,25.3,0.98,25.53,24.52,0.59
20260512,25.65,25.65,25.15,25.2,570017,25.29,-0.37,25.57,24.54,0.48
20260513,25.15,25.25,24.85,24.85,347584,25.26,-1.61,25.58,24.56,0.29
20260514,24.85,25,24.8,25,233621,25.23,-0.93,25.6,24.58,0.2
20260515,25.2,25.2,24.8,24.85,461518,25.2,-1.4,25.64,24.6,0.39
20260518,24.8,25,24.5,24.9,164349,25.18,-1.1,25.67,24.61,0.14
20260519,24.9,25.25,24.55,24.55,344024,25.13,-2.29,25.67,24.62,0.29
20260520,24.75,25.4,24.7,25.15,488577,25.13,0.09,25.58,24.64,0.43
20260521,25.45,25.55,25.35,25.45,406646,25.15,1.18,25.47,24.66,0.43
20260522,25.45,25.8,25.05,25.75,568045,25.2,2.17,25.36,24.69,0.77
20260525,25.95,25.95,25.6,25.6,412818,25.24,1.44,25.24,24.72,0.7
20260526,25.8,26,25.65,25.75,280972,25.28,1.86,25.21,24.75,0.54
20260527,25.9,26,25.6,25.7,463041,25.31,1.52,25.22,24.77,0.94
20260528,25.65,25.9,25.4,25.6,406105,25.34,1.03,25.25,24.8,0.84
20260529,25.7,25.85,25.65,25.75,247374,25.37,1.49,25.26,24.83,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 44.12
- over_600_ratio: 39.04
- over_800_ratio: 34.58
- over_1000_ratio: 32.31
- over_400_change_1w: 0.58
- over_800_change_1w: 0.47
- over_1000_change_1w: 0.46
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,41.81,,33.08,,30.84,,0,False,False
20260508,42.17,0.36,33.17,0.09,30.91,0.07,1,True,True
20260515,42.9,0.73,33.5,0.33,31.23,0.32,2,True,True
20260522,43.54,0.64,34.11,0.61,31.85,0.62,3,True,True
20260529,44.12,0.58,34.58,0.47,32.31,0.46,4,True,True
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
