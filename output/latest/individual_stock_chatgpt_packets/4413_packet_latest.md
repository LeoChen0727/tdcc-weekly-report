# INDIVIDUAL STOCK CHATGPT PACKET - 4413 飛寶企業

## Metadata
- generated_at: 2026-05-26 21:25:47 Asia/Taipei
- stock_id: 4413
- stock_name: 飛寶企業
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 119
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4413_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4413_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4413_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4413_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4413_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4413_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4413_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4413_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4413_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4413_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4413_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4413_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4413_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4413.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4413.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4413.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4413.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4413.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4413.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4413_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4413_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4413_latest.md?ref=main

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
- open: 16.55
- high: 17.4
- low: 16.4
- close: 17
- volume: 17000
- ma5: 17.6
- ema23_primary: 18.16
- distance_to_ema23_pct: -6.4
- ma20: 18.46
- ma60: 18.13
- ma120: 18.15
- return_5d: -7.61
- return_20d: -12.14
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -7.92
- distance_to_high_60_pct: -15.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260422,19,19.2,18.55,18.8,67000,18.09,3.9,17.98,18.01,5.34
20260423,18.6,19.2,18.6,18.85,3000,18.16,3.82,18.02,18.04,0.24
20260424,18.3,19.2,18.3,19.2,12000,18.24,5.24,18.07,18.06,0.93
20260427,18.85,19.25,18.85,19,22000,18.31,3.79,18.12,18.09,1.58
20260429,18.75,18.75,18.75,18.75,3000,18.34,2.22,18.15,18.1,0.21
20260430,18.2,19.05,18.15,19.05,14000,18.4,3.52,18.21,18.12,0.96
20260504,19.05,19.2,18.9,18.9,61000,18.44,2.47,18.29,18.13,3.52
20260505,19.05,19.05,18.7,19,36000,18.49,2.76,18.36,18.14,1.9
20260506,18.95,18.95,18.55,18.6,8000,18.5,0.54,18.41,18.15,0.42
20260507,18.9,19.1,18.7,18.7,8000,18.52,0.99,18.44,18.16,0.41
20260508,18.2,18.6,17.8,18.6,10000,18.52,0.41,18.5,18.16,0.51
20260511,18.8,19.1,18.6,18.6,10000,18.53,0.38,18.54,18.16,0.51
20260512,18.7,19.05,18.7,18.7,17000,18.54,0.84,18.61,18.17,0.86
20260514,18.1,18.2,18.1,18.1,4000,18.51,-2.2,18.63,18.17,0.2
20260515,18.15,18.4,18.1,18.4,4000,18.5,-0.53,18.64,18.17,0.2
20260518,18.4,18.4,18.1,18.1,9000,18.46,-1.98,18.66,18.17,0.47
20260520,17.85,18,17.4,18,11000,18.43,-2.31,18.66,18.16,0.57
20260522,17.5,17.7,17.35,17.7,18000,18.37,-3.62,18.64,18.16,0.9
20260525,17.2,17.2,16.3,17.2,17000,18.27,-5.85,18.58,18.15,0.87
20260526,16.55,17.4,16.4,17,17000,18.16,-6.4,18.46,18.13,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.25
- over_600_ratio: 61.01
- over_800_ratio: 52.55
- over_1000_ratio: 52.55
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
20260430,69.25,,52.55,,52.55,,0,False,False
20260508,69.25,0,52.55,0,52.55,0,0,False,False
20260515,69.25,0,52.55,0,52.55,0,0,False,False
20260522,69.25,0,52.55,0,52.55,0,0,False,False
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
