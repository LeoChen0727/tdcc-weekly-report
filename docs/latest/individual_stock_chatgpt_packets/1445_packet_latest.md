# INDIVIDUAL STOCK CHATGPT PACKET - 1445 大宇

## Metadata
- generated_at: 2026-05-26 22:18:04 Asia/Taipei
- stock_id: 1445
- stock_name: 大宇
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1445_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1445_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1445_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1445_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1445_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1445_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1445_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1445_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1445_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1445_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1445_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1445_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1445_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1445.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1445.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1445.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1445.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1445.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1445.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1445_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1445_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1445_latest.md?ref=main

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
- open: 11.7
- high: 11.7
- low: 11.5
- close: 11.55
- volume: 45330
- ma5: 11.74
- ema23_primary: 12.11
- distance_to_ema23_pct: -4.65
- ma20: 12.14
- ma60: 12.72
- ma120: 13.25
- return_5d: 1.76
- return_20d: -9.77
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: -4.86
- distance_to_high_60_pct: -24.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.45,12.85,12.45,12.85,17359,12.94,-0.7,12.8,13.6,0.22
20260429,12.8,12.85,12.6,12.65,45835,12.92,-2.06,12.8,13.57,0.56
20260430,12.7,12.75,12.55,12.7,28634,12.9,-1.53,12.77,13.54,0.4
20260504,12.65,12.65,12.55,12.55,34493,12.87,-2.48,12.76,13.51,0.54
20260505,12.5,12.65,12.5,12.55,37251,12.84,-2.28,12.77,13.48,0.61
20260506,12.55,13.8,12.55,12.8,143723,12.84,-0.3,12.8,13.45,2.31
20260507,12.8,12.8,12.6,12.75,81236,12.83,-0.63,12.82,13.43,1.3
20260508,12.95,12.95,12.55,12.7,13928,12.82,-0.94,12.84,13.4,0.22
20260511,12.55,12.55,12.3,12.5,101681,12.79,-2.3,12.83,13.37,1.63
20260512,12.5,12.5,12.1,12.2,109254,12.74,-4.27,12.82,13.33,1.66
20260513,12.25,12.25,11.9,11.9,104340,12.67,-6.11,12.78,13.27,1.52
20260514,11.85,12,11.75,11.8,97139,12.6,-6.36,12.72,13.21,1.51
20260515,11.8,11.8,11.45,11.45,95400,12.51,-8.44,12.64,13.13,1.44
20260518,11.2,11.8,11.2,11.35,54095,12.41,-8.53,12.55,13.06,0.81
20260519,11.4,11.5,11.35,11.35,54037,12.32,-7.88,12.47,13,0.86
20260520,11.4,11.5,11.35,11.5,33115,12.25,-6.14,12.38,12.94,0.55
20260521,11.35,12.3,11.35,12.15,160101,12.24,-0.77,12.32,12.89,2.43
20260522,12.1,12.1,11.8,11.8,211061,12.21,-3.33,12.27,12.83,2.78
20260525,11.9,11.9,11.6,11.7,194657,12.16,-3.82,12.2,12.78,2.28
20260526,11.7,11.7,11.5,11.55,45330,12.11,-4.65,12.14,12.72,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.84
- over_600_ratio: 65.02
- over_800_ratio: 61.2
- over_1000_ratio: 59.67
- over_400_change_1w: 0.08
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.73,,61.21,,59.68,,0,False,False
20260508,68.78,0.05,61.18,-0.03,59.65,-0.03,1,False,False
20260515,68.76,-0.02,61.18,0,59.65,0,0,False,False
20260522,68.84,0.08,61.2,0.02,59.67,0.02,1,True,True
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
