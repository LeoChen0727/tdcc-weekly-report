# INDIVIDUAL STOCK CHATGPT PACKET - 4207 環泰

## Metadata
- generated_at: 2026-05-26 21:25:46 Asia/Taipei
- stock_id: 4207
- stock_name: 環泰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4207_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4207_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4207_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4207_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4207_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4207_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4207_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4207_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4207_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4207_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4207_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4207_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4207_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4207.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4207.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4207.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4207.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4207.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4207.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4207_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4207_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4207_latest.md?ref=main

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
- open: 19.55
- high: 19.55
- low: 19.15
- close: 19.35
- volume: 19000
- ma5: 19.38
- ema23_primary: 18.76
- distance_to_ema23_pct: 3.13
- ma20: 18.5
- ma60: 18.93
- ma120: 18.95
- return_5d: 0.52
- return_20d: 10.89
- volume_ratio: 0.1
- distance_to_ma20_pct_auxiliary: 4.62
- distance_to_high_60_pct: -4.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,17.45,17.6,17.45,17.55,40000,18.26,-3.91,18.29,19.05,0.12
20260429,17.5,17.55,17.45,17.45,109000,18.2,-4.1,18.18,19.03,0.34
20260430,17.65,17.65,17.5,17.5,129000,18.14,-3.52,18.09,19.01,0.41
20260504,17.5,17.65,17.5,17.5,76000,18.08,-3.23,17.98,19,0.25
20260505,17.5,17.75,17.45,17.5,225000,18.04,-2.97,17.87,18.98,0.77
20260506,17.5,17.5,17.3,17.5,176000,17.99,-2.73,17.76,18.97,0.71
20260507,17.45,17.65,17.45,17.6,173000,17.96,-2,17.71,18.95,0.79
20260508,17.7,17.9,17.65,17.9,99000,17.95,-0.3,17.69,18.94,0.46
20260511,17.95,18.5,17.9,18.5,237000,18,2.78,17.71,18.94,1.25
20260512,18.55,18.7,18.4,18.7,274000,18.06,3.56,17.75,18.94,1.49
20260513,18.4,18.8,18.4,18.7,138000,18.11,3.25,17.78,18.94,0.77
20260514,18.8,19.05,18.8,19,401000,18.19,4.48,17.83,18.94,2.11
20260515,19.05,19.05,18.65,18.85,413000,18.24,3.34,17.88,18.93,2.04
20260518,18.7,19.5,18.7,19.5,326000,18.35,6.29,17.97,18.95,1.57
20260519,19.5,19.5,19.1,19.25,416000,18.42,4.5,18.05,18.95,1.99
20260520,19.4,19.4,19.05,19.25,253000,18.49,4.11,18.12,18.95,1.18
20260521,19.3,19.3,19.1,19.2,103000,18.55,3.51,18.2,18.95,0.48
20260522,19.2,19.6,19.1,19.6,19000,18.64,5.17,18.3,18.95,0.1
20260525,19.6,19.7,19.25,19.5,19000,18.71,4.23,18.4,18.94,0.1
20260526,19.55,19.55,19.15,19.35,19000,18.76,3.13,18.5,18.93,0.1
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.96
- over_600_ratio: 67.11
- over_800_ratio: 65.39
- over_1000_ratio: 62.75
- over_400_change_1w: 0.26
- over_800_change_1w: 0.31
- over_1000_change_1w: 0.31
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.23,,64.82,,62.18,,0,False,False
20260508,70.33,0.1,64.91,0.09,62.27,0.09,1,True,True
20260515,70.7,0.37,65.08,0.17,62.44,0.17,2,True,True
20260522,70.96,0.26,65.39,0.31,62.75,0.31,3,True,True
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
