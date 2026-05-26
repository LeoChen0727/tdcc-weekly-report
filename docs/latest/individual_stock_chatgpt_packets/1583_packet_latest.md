# INDIVIDUAL STOCK CHATGPT PACKET - 1583 程泰

## Metadata
- generated_at: 2026-05-26 21:24:42 Asia/Taipei
- stock_id: 1583
- stock_name: 程泰
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1583_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1583_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1583_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1583_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1583_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1583_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1583_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1583_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1583_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1583_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1583_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1583_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1583_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1583.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1583.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1583.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1583.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1583.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1583.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1583_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1583_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1583_latest.md?ref=main

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
- open: 48
- high: 50.6
- low: 48
- close: 49.85
- volume: 98160
- ma5: 47.76
- ema23_primary: 47.59
- distance_to_ema23_pct: 4.74
- ma20: 47.76
- ma60: 46.18
- ma120: 46.37
- return_5d: 3.96
- return_20d: 5.73
- volume_ratio: 2.32
- distance_to_ma20_pct_auxiliary: 4.37
- distance_to_high_60_pct: -2.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,47.15,47.6,47.15,47.45,10438,46.31,2.46,45.9,46.44,0.48
20260429,48.4,48.4,47.1,47.1,19116,46.38,1.56,46.03,46.4,0.88
20260430,46.65,47.05,46.6,46.6,16048,46.4,0.44,46.14,46.37,0.73
20260504,46.6,46.8,46.5,46.75,28720,46.43,0.7,46.28,46.33,1.3
20260505,46.35,47,46.35,47,7015,46.47,1.13,46.45,46.31,0.32
20260506,48.25,48.45,47,48.45,63334,46.64,3.88,46.71,46.31,2.54
20260507,48.9,48.9,48.45,48.45,40640,46.79,3.55,46.92,46.31,1.59
20260508,48.45,48.45,47,47.5,29310,46.85,1.39,47.08,46.28,1.09
20260511,47.6,49.5,47.6,49,92162,47.03,4.19,47.3,46.28,3.06
20260512,48.8,49,47.9,48.7,34519,47.17,3.25,47.52,46.28,1.13
20260513,47.35,47.9,47.15,47.25,16509,47.17,0.16,47.59,46.27,0.56
20260514,47.05,48,46.7,46.7,31430,47.13,-0.92,47.62,46.23,1.07
20260515,46.5,51.3,46.45,48.15,126134,47.22,1.97,47.65,46.23,3.73
20260518,48,50.2,47.55,49.4,69697,47.4,4.22,47.7,46.27,1.93
20260519,48.3,49,47.95,47.95,33560,47.45,1.06,47.69,46.27,0.93
20260520,47.4,47.4,46.65,47.1,25307,47.42,-0.67,47.66,46.25,0.71
20260521,47.45,47.6,47.1,47.1,44866,47.39,-0.62,47.61,46.24,1.2
20260522,47.85,47.85,47.25,47.25,20232,47.38,-0.27,47.6,46.2,0.54
20260525,47.25,49,47.25,47.5,38067,47.39,0.23,47.63,46.17,1.01
20260526,48,50.6,48,49.85,98160,47.59,4.74,47.76,46.18,2.32
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 91.21
- over_600_ratio: 90.26
- over_800_ratio: 90.26
- over_1000_ratio: 89.47
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,91.21,,90.26,,89.47,,0,False,False
20260508,91.21,0,90.26,0,89.47,0,0,False,False
20260515,91.21,0,90.26,0,89.47,0,0,False,False
20260522,91.21,0,90.26,0,89.47,0,0,False,False
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
