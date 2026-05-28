# INDIVIDUAL STOCK CHATGPT PACKET - 1417 嘉裕

## Metadata
- generated_at: 2026-05-28 19:31:30 Asia/Taipei
- stock_id: 1417
- stock_name: 嘉裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1417_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1417_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1417_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1417_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1417_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1417_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1417_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1417_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1417_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1417_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1417_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1417_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1417_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1417.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1417.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1417.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1417.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1417.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1417.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1417_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1417_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1417_latest.md?ref=main

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
- date: 20260528
- open: 8.06
- high: 8.12
- low: 8.05
- close: 8.06
- volume: 140137
- ma5: 8.13
- ema23_primary: 8.42
- distance_to_ema23_pct: -4.32
- ma20: 8.44
- ma60: 8.77
- ma120: 8.82
- return_5d: -1.95
- return_20d: -9.13
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -4.48
- distance_to_high_60_pct: -14.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,8.95,8.99,8.81,8.85,140061,8.95,-1.15,9,8.88,1.02
20260504,8.9,8.96,8.79,8.9,108362,8.95,-0.54,8.98,8.88,0.82
20260505,8.85,8.91,8.8,8.89,87329,8.94,-0.6,8.97,8.88,0.66
20260506,8.93,8.93,8.82,8.86,115433,8.94,-0.86,8.96,8.88,0.86
20260507,8.82,8.85,8.6,8.77,184814,8.92,-1.71,8.94,8.88,1.35
20260508,8.74,8.74,8.62,8.71,74714,8.9,-2.19,8.92,8.88,0.57
20260511,8.71,8.79,8.61,8.67,191040,8.89,-2.42,8.91,8.88,1.42
20260512,8.67,8.87,8.35,8.55,228079,8.86,-3.47,8.89,8.88,1.59
20260513,8.45,8.45,8.29,8.38,165302,8.82,-4.96,8.85,8.87,1.14
20260514,8.38,8.5,8.3,8.3,106448,8.77,-5.41,8.82,8.87,0.77
20260515,8.3,8.35,8.22,8.26,243374,8.73,-5.4,8.78,8.86,1.73
20260518,8.28,8.28,8.18,8.27,76375,8.69,-4.87,8.74,8.85,0.57
20260519,8.29,8.29,8.16,8.27,106919,8.66,-4.48,8.71,8.84,0.8
20260520,8.22,8.22,8.15,8.2,100780,8.62,-4.87,8.67,8.83,0.76
20260521,8.24,8.3,8.16,8.22,76192,8.59,-4.27,8.63,8.82,0.58
20260522,8.18,8.27,8.16,8.16,183094,8.55,-4.57,8.59,8.81,1.45
20260525,8.16,8.23,8.08,8.2,243401,8.52,-3.77,8.55,8.8,1.8
20260526,8.21,8.23,8.15,8.18,74227,8.49,-3.69,8.52,8.79,0.56
20260527,8.23,8.23,8,8.06,254337,8.46,-4.69,8.48,8.78,1.78
20260528,8.06,8.12,8.05,8.06,140137,8.42,-4.32,8.44,8.77,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.52
- over_600_ratio: 52.89
- over_800_ratio: 51.1
- over_1000_ratio: 48.09
- over_400_change_1w: 0.08
- over_800_change_1w: 0.22
- over_1000_change_1w: 0.21
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.58,,51.06,,48.06,,0,False,False
20260508,57.6,0.02,51.08,0.02,48.08,0.02,1,True,True
20260515,57.44,-0.16,50.88,-0.2,47.88,-0.2,0,False,False
20260522,57.52,0.08,51.1,0.22,48.09,0.21,1,True,True
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
