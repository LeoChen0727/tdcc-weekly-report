# INDIVIDUAL STOCK CHATGPT PACKET - 1236 宏亞

## Metadata
- generated_at: 2026-05-26 21:24:33 Asia/Taipei
- stock_id: 1236
- stock_name: 宏亞
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1236_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1236_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1236_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1236_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1236_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1236_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1236_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1236_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1236_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1236_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1236_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1236_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1236_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1236.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1236.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1236.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1236.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1236.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1236.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1236_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1236_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1236_latest.md?ref=main

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
- open: 24.2
- high: 24.8
- low: 24.1
- close: 24.2
- volume: 38994
- ma5: 23.99
- ema23_primary: 24.87
- distance_to_ema23_pct: -2.71
- ma20: 24.99
- ma60: 26.12
- ma120: 25.77
- return_5d: 2.11
- return_20d: -5.47
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: -3.17
- distance_to_high_60_pct: -15.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,25.6,25.9,25.35,25.65,44871,26.12,-1.78,26.01,26.44,0.84
20260429,26.1,26.15,25.7,25.75,32530,26.09,-1.28,25.99,26.46,0.62
20260430,26.35,26.35,25.6,25.75,39138,26.06,-1.18,25.98,26.47,0.74
20260504,25.8,25.9,25.75,25.8,19698,26.04,-0.91,25.96,26.48,0.38
20260505,25.95,26.1,25.85,26,24352,26.03,-0.13,25.96,26.5,0.47
20260506,26.1,26.3,25.95,26.15,94420,26.04,0.41,25.99,26.52,1.71
20260507,26.15,26.4,26.05,26.35,66398,26.07,1.08,26.03,26.52,1.18
20260508,26.4,26.55,26.15,26.35,64445,26.09,0.99,26.08,26.52,1.11
20260511,26.15,26.45,26,26.4,51218,26.12,1.08,26.12,26.53,0.87
20260512,26.75,26.75,25.15,25.15,124223,26.04,-3.41,26.05,26.51,2.08
20260513,25,25.15,24.4,24.55,79051,25.91,-5.26,25.95,26.48,1.27
20260514,24.35,24.55,24.1,24.5,37370,25.8,-5.02,25.83,26.44,0.63
20260515,24.5,24.55,24.45,24.45,14749,25.68,-4.8,25.71,26.41,0.26
20260518,24.45,24.45,23.2,23.35,115809,25.49,-8.39,25.53,26.35,1.87
20260519,23.5,23.7,23.35,23.7,26921,25.34,-6.47,25.37,26.31,0.45
20260520,23.9,23.9,23.45,23.7,43293,25.2,-5.96,25.29,26.26,0.85
20260521,23.9,23.9,23.55,23.7,50669,25.08,-5.49,25.2,26.22,0.97
20260522,23.6,24,23.6,24,23742,24.99,-3.95,25.12,26.18,0.46
20260525,25,25,24,24.35,36165,24.93,-2.35,25.06,26.15,0.7
20260526,24.2,24.8,24.1,24.2,38994,24.87,-2.71,24.99,26.12,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 83.5
- over_600_ratio: 82.96
- over_800_ratio: 82.23
- over_1000_ratio: 77.85
- over_400_change_1w: -0.46
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.87,,82.12,,77.74,,0,False,False
20260508,83.9,0.03,82.18,0.06,77.8,0.06,1,True,True
20260515,83.96,0.06,82.22,0.04,77.84,0.04,2,True,True
20260522,83.5,-0.46,82.23,0.01,77.85,0.01,3,False,True
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
