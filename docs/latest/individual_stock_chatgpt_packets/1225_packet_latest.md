# INDIVIDUAL STOCK CHATGPT PACKET - 1225 福懋油

## Metadata
- generated_at: 2026-05-26 21:24:32 Asia/Taipei
- stock_id: 1225
- stock_name: 福懋油
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1225_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1225_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1225_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1225_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1225_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1225_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1225_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1225_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1225_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1225_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1225_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1225_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1225_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1225.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1225.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1225.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1225.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1225.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1225.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1225_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1225_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1225_latest.md?ref=main

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
- open: 29.8
- high: 30.25
- low: 29.65
- close: 30.2
- volume: 201424
- ma5: 29.49
- ema23_primary: 30.73
- distance_to_ema23_pct: -1.72
- ma20: 30.92
- ma60: 31.83
- ma120: 30.5
- return_5d: 3.78
- return_20d: -3.67
- volume_ratio: 0.61
- distance_to_ma20_pct_auxiliary: -2.32
- distance_to_high_60_pct: -16.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,31.35,31.7,31.3,31.55,822648,32.37,-2.54,32.62,31.11,2.57
20260429,31.9,32.85,31.4,32.85,220636,32.41,1.35,32.67,31.18,0.69
20260430,32.85,32.85,31.65,32,150724,32.38,-1.17,32.71,31.24,0.47
20260504,32.25,32.4,31.6,32.05,179390,32.35,-0.93,32.73,31.3,0.56
20260505,32,32.1,31.75,31.95,733866,32.32,-1.13,32.73,31.35,2.08
20260506,32.05,33.15,31.9,33.15,462993,32.39,2.36,32.74,31.43,1.32
20260507,33.15,33.35,32.6,32.85,308947,32.42,1.31,32.78,31.5,0.87
20260508,32.85,32.85,31.8,32,188558,32.39,-1.2,32.76,31.56,0.53
20260511,32,32.25,31.7,32.05,627713,32.36,-0.96,32.73,31.62,1.68
20260512,32,32.1,31.4,31.55,251191,32.29,-2.3,32.62,31.68,0.67
20260513,31.45,31.7,31.35,31.5,122121,32.23,-2.26,32.48,31.73,0.35
20260514,30,30.75,29.75,30.25,1223003,32.06,-5.65,32.31,31.76,3.07
20260515,30.25,30.3,29.1,29.25,327437,31.83,-8.1,32.07,31.77,0.81
20260518,29.2,29.2,28.75,28.8,215069,31.58,-8.79,31.85,31.78,0.54
20260519,28.8,29.3,28.8,29.1,146825,31.37,-7.23,31.61,31.79,0.39
20260520,28.7,29,28.7,28.8,90842,31.16,-7.56,31.38,31.8,0.26
20260521,28.9,29.55,28.8,29.2,120353,30.99,-5.78,31.18,31.8,0.34
20260522,29.1,29.45,28.9,29.45,81126,30.86,-4.58,31.06,31.81,0.24
20260525,29.6,30.2,29.4,29.8,135028,30.78,-3.17,30.98,31.82,0.39
20260526,29.8,30.25,29.65,30.2,201424,30.73,-1.72,30.92,31.83,0.61
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 89.1
- over_600_ratio: 87.71
- over_800_ratio: 86.88
- over_1000_ratio: 86.17
- over_400_change_1w: -0.06
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.92,,87.14,,86.43,,0,False,False
20260508,88.96,0.04,87.18,0.04,86.47,0.04,1,True,True
20260515,89.16,0.2,86.95,-0.23,86.24,-0.23,2,False,False
20260522,89.1,-0.06,86.88,-0.07,86.17,-0.07,0,False,False
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
