# INDIVIDUAL STOCK CHATGPT PACKET - 9928 中視

## Metadata
- generated_at: 2026-05-28 19:33:57 Asia/Taipei
- stock_id: 9928
- stock_name: 中視
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9928_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9928_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9928_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9928_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9928_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9928_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9928_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9928_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9928_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9928_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9928_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9928_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9928_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9928.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9928.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9928.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9928.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9928.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9928.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9928_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9928_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9928_latest.md?ref=main

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
- open: 17.75
- high: 18
- low: 17.6
- close: 17.9
- volume: 46746
- ma5: 17.9
- ema23_primary: 17.77
- distance_to_ema23_pct: 0.74
- ma20: 17.73
- ma60: 17.79
- ma120: 18.1
- return_5d: 1.42
- return_20d: 2.29
- volume_ratio: 1.15
- distance_to_ma20_pct_auxiliary: 0.99
- distance_to_high_60_pct: -2.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,17.55,17.75,17.5,17.55,34202,17.76,-1.2,17.81,17.94,0.62
20260504,17.6,17.7,17.5,17.7,34722,17.76,-0.32,17.8,17.93,0.63
20260505,17.5,17.7,17.45,17.7,43279,17.75,-0.3,17.79,17.93,0.83
20260506,17.85,17.85,17.55,17.7,38824,17.75,-0.27,17.77,17.92,0.78
20260507,17.65,17.7,17.5,17.7,43693,17.74,-0.25,17.75,17.91,0.87
20260508,17.65,17.7,17.55,17.65,20100,17.74,-0.49,17.73,17.89,0.41
20260511,17.55,17.7,17.45,17.7,89106,17.73,-0.19,17.72,17.88,1.73
20260512,17.5,17.6,17.5,17.6,16253,17.72,-0.69,17.7,17.87,0.38
20260513,17.7,17.7,17.55,17.65,27355,17.72,-0.37,17.69,17.86,0.63
20260514,17.6,17.65,17.6,17.65,35772,17.71,-0.34,17.67,17.85,0.85
20260515,17.65,17.65,17.45,17.65,52122,17.71,-0.31,17.66,17.85,1.31
20260518,17.65,17.85,17.65,17.7,23995,17.71,-0.03,17.66,17.84,0.63
20260519,17.55,17.7,17.55,17.7,19110,17.7,-0.03,17.66,17.83,0.52
20260520,17.55,17.7,17.55,17.7,20837,17.7,-0.03,17.66,17.82,0.58
20260521,17.6,17.7,17.6,17.65,18003,17.7,-0.28,17.66,17.81,0.52
20260522,17.7,17.95,17.7,17.95,125707,17.72,1.29,17.67,17.8,3.24
20260525,18,18.3,17.85,17.9,68434,17.74,0.93,17.69,17.8,1.62
20260526,18,18,17.85,17.95,13617,17.75,1.11,17.7,17.8,0.34
20260527,17.95,17.95,17.6,17.8,43816,17.76,0.24,17.7,17.79,1.06
20260528,17.75,18,17.6,17.9,46746,17.77,0.74,17.73,17.79,1.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.4
- over_600_ratio: 71.03
- over_800_ratio: 69.95
- over_1000_ratio: 67.16
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.32,,69.95,,67.16,,0,False,False
20260508,74.39,0.07,69.95,0,67.16,0,1,False,False
20260515,74.39,0,69.95,0,67.16,0,0,False,False
20260522,74.4,0.01,69.95,0,67.16,0,1,False,False
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
