# INDIVIDUAL STOCK CHATGPT PACKET - 6212 理銘

## Metadata
- generated_at: 2026-05-26 22:20:04 Asia/Taipei
- stock_id: 6212
- stock_name: 理銘
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 113
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6212_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6212_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6212_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6212_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6212_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6212_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6212_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6212_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6212_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6212_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6212_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6212_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6212_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6212.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6212.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6212.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6212.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6212.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6212.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6212_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6212_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6212_latest.md?ref=main

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
- open: 27.6
- high: 27.6
- low: 27.3
- close: 27.6
- volume: 28000
- ma5: 27.44
- ema23_primary: 28.29
- distance_to_ema23_pct: -2.44
- ma20: 28.27
- ma60: 30.54
- ma120: 35.03
- return_5d: -0.72
- return_20d: -3.5
- volume_ratio: 3.71
- distance_to_ma20_pct_auxiliary: -2.35
- distance_to_high_60_pct: -29.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260423,28.6,28.6,28.3,28.3,2000,29.29,-3.38,28.4,34.06,0.14
20260424,28.3,28.3,28.3,28.3,1000,29.21,-3.1,28.36,33.84,0.08
20260427,28.5,28.5,28.5,28.5,1000,29.15,-2.22,28.29,33.64,0.1
20260428,28.8,28.95,28.8,28.95,2000,29.13,-0.62,28.21,33.45,0.2
20260429,29.5,29.6,29,29.15,16000,29.13,0.06,28.18,33.26,1.48
20260430,28.6,28.6,28.6,28.6,1000,29.09,-1.68,28.16,33.07,0.12
20260505,28.65,28.65,28.65,28.65,3000,29.05,-1.38,28.19,32.88,0.38
20260506,28.3,28.35,28,28,21000,28.96,-3.33,28.19,32.66,2.52
20260507,28.05,28.05,28,28,13000,28.88,-3.06,28.13,32.47,1.57
20260508,28.55,28.55,28.55,28.55,1000,28.86,-1.06,28.2,32.28,0.16
20260511,30,30,30,30,1000,28.95,3.62,28.35,32.13,0.18
20260513,29.5,29.5,29,29,4000,28.96,0.15,28.45,31.97,0.74
20260514,28.55,28.55,28.05,28.05,6000,28.88,-2.87,28.48,31.78,1.11
20260515,28.25,28.25,28.25,28.25,1000,28.83,-2,28.52,31.6,0.19
20260518,27.5,27.8,27.5,27.8,12000,28.74,-3.28,28.51,31.42,2.07
20260519,27.2,27.2,27.2,27.2,1000,28.61,-4.94,28.47,31.24,0.18
20260520,27.2,27.3,27.2,27.3,7000,28.5,-4.22,28.43,31.06,1.23
20260521,27.75,27.75,27.5,27.5,2000,28.42,-3.24,28.36,30.88,0.36
20260522,27.5,28.3,27.5,27.6,28000,28.35,-2.65,28.32,30.71,4.15
20260526,27.6,27.6,27.3,27.6,28000,28.29,-2.44,28.27,30.54,3.71
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 91.78
- over_600_ratio: 89.23
- over_800_ratio: 87.9
- over_1000_ratio: 86.12
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
20260430,91.78,,87.9,,86.12,,0,False,False
20260508,91.78,0,87.9,0,86.12,0,0,False,False
20260515,91.78,0,87.9,0,86.12,0,0,False,False
20260522,91.78,0,87.9,0,86.12,0,0,False,False
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
