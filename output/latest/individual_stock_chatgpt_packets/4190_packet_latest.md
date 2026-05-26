# INDIVIDUAL STOCK CHATGPT PACKET - 4190 佐登-KY

## Metadata
- generated_at: 2026-05-26 23:01:33 Asia/Taipei
- stock_id: 4190
- stock_name: 佐登-KY
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4190_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4190_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4190_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4190_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4190_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4190_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4190_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4190_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4190_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4190_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4190_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4190_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4190_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4190.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4190.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4190.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4190.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4190.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4190.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4190_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4190_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4190_latest.md?ref=main

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
- open: 24.4
- high: 24.75
- low: 24.2
- close: 24.75
- volume: 97032
- ma5: 24.76
- ema23_primary: 25.11
- distance_to_ema23_pct: -1.43
- ma20: 24.74
- ma60: 26.74
- ma120: 28.3
- return_5d: 1.02
- return_20d: -1.59
- volume_ratio: 2.03
- distance_to_ma20_pct_auxiliary: 0.04
- distance_to_high_60_pct: -17.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,25.1,25.1,24.8,24.9,100111,26.78,-7.02,26.72,28.2,2.01
20260429,25,25,24.7,24.7,36545,26.61,-7.17,26.59,28.12,0.76
20260430,24.7,25.15,24.6,25.15,63435,26.49,-5.04,26.49,28.04,1.29
20260504,25.15,25.15,24.9,25,38343,26.36,-5.17,26.37,27.96,0.76
20260505,25,25.05,24.8,24.85,20322,26.24,-5.28,26.25,27.89,0.4
20260506,25.15,25.15,24.8,25,25423,26.13,-4.33,26.14,27.81,0.5
20260507,25.05,25.05,24.7,24.7,40042,26.01,-5.05,26.03,27.72,0.8
20260508,24.7,24.95,24.6,24.6,26620,25.9,-5,25.91,27.64,0.53
20260511,24.55,24.9,24.5,24.6,16081,25.79,-4.61,25.8,27.56,0.32
20260512,24.65,24.7,24.5,24.5,28952,25.68,-4.6,25.68,27.48,0.62
20260513,24.5,25,24.3,24.75,47475,25.6,-3.33,25.56,27.4,1.02
20260514,24.8,25.1,24.6,24.6,22583,25.52,-3.6,25.42,27.33,0.49
20260515,24.55,24.6,24.15,24.55,47627,25.44,-3.49,25.3,27.25,1.03
20260518,24.8,24.8,24.15,24.6,43468,25.37,-3.03,25.18,27.17,0.94
20260519,24.8,24.8,24.2,24.5,17731,25.3,-3.15,25.08,27.1,0.39
20260520,24.7,24.7,24.3,24.7,33019,25.25,-2.16,24.98,27.02,0.78
20260521,24.55,24.8,24,24.75,121050,25.21,-1.81,24.89,26.95,2.64
20260522,24.35,24.8,24.15,24.75,43080,25.17,-1.66,24.83,26.88,0.97
20260525,24.55,24.85,24.05,24.85,85151,25.14,-1.16,24.76,26.81,1.84
20260526,24.4,24.75,24.2,24.75,97032,25.11,-1.43,24.74,26.74,2.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.66
- over_600_ratio: 65.66
- over_800_ratio: 63.55
- over_1000_ratio: 62.19
- over_400_change_1w: 0.16
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.5,,63.52,,62.16,,0,False,False
20260508,65.5,0,63.52,0,62.16,0,0,False,False
20260515,65.5,0,63.52,0,62.16,0,0,False,False
20260522,65.66,0.16,63.55,0.03,62.19,0.03,1,True,True
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
