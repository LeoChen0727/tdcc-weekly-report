# INDIVIDUAL STOCK CHATGPT PACKET - 6730 常廣

## Metadata
- generated_at: 2026-05-28 19:33:29 Asia/Taipei
- stock_id: 6730
- stock_name: 常廣
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 108
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6730_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6730_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6730_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6730_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6730_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6730_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6730_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6730_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6730_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6730_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6730_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6730_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6730_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6730.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6730.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6730.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6730.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6730.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6730.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6730_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6730_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6730_latest.md?ref=main

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
- open: 35.5
- high: 35.55
- low: 34
- close: 35.5
- volume: 195517
- ma5: 36.43
- ema23_primary: 37.31
- distance_to_ema23_pct: -4.85
- ma20: 37.52
- ma60: 37.27
- ma120: 36.95
- return_5d: -6.08
- return_20d: -8.74
- volume_ratio: 4.24
- distance_to_ma20_pct_auxiliary: -5.37
- distance_to_high_60_pct: -9.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,38.2,38.5,37.95,38.5,13000,38.09,1.08,38.11,37.23,0.25
20260504,38.05,38.5,38,38.5,32000,38.12,0.99,38.23,37.26,0.62
20260505,38.2,39,38,39,47000,38.2,2.11,38.4,37.28,0.91
20260506,38.25,38.25,37.85,37.9,46000,38.17,-0.71,38.49,37.28,0.86
20260507,38.05,38.05,37.7,37.7,30000,38.13,-1.13,38.54,37.28,0.57
20260508,37.75,37.75,37.5,37.6,52000,38.09,-1.28,38.57,37.28,0.97
20260511,37.3,37.5,37,37.5,39000,38.04,-1.41,38.59,37.28,0.78
20260512,37.5,39,37.4,38.75,24000,38.1,1.71,38.58,37.3,0.58
20260513,38,38,37.6,37.6,13000,38.06,-1.2,38.51,37.29,0.34
20260514,37.6,37.65,37.5,37.5,9000,38.01,-1.34,38.43,37.28,0.26
20260515,37.5,37.5,37.3,37.5,201000,37.97,-1.23,38.36,37.28,4.51
20260518,37.5,38.3,37.3,37.3,19000,37.91,-1.61,38.27,37.29,0.44
20260519,37.35,38,37.35,38,4000,37.92,0.21,38.22,37.31,0.09
20260520,37.15,37.15,37,37,16000,37.84,-2.23,38.14,37.31,0.41
20260521,37,37.8,36.9,37.8,35000,37.84,-0.1,38.08,37.32,0.88
20260522,37.7,37.7,37,37.7,38000,37.83,-0.34,38.06,37.33,1.03
20260525,37,37,36.7,36.75,37000,37.74,-2.62,37.96,37.33,0.97
20260526,36.5,36.95,35.95,36.2,36000,37.61,-3.75,37.84,37.31,0.91
20260527,36,36,35.6,36,36000,37.48,-3.94,37.69,37.3,0.92
20260528,35.5,35.55,34,35.5,195517,37.31,-4.85,37.52,37.27,4.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 73.92
- over_600_ratio: 68.49
- over_800_ratio: 60.59
- over_1000_ratio: 60.59
- over_400_change_1w: -1.17
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.03,,60.59,,60.59,,0,False,False
20260508,74.98,-0.05,60.59,0,60.59,0,0,False,False
20260515,75.09,0.11,60.59,0,60.59,0,1,False,False
20260522,73.92,-1.17,60.59,0,60.59,0,0,False,False
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
