# INDIVIDUAL STOCK CHATGPT PACKET - 9902 台火

## Metadata
- generated_at: 2026-05-26 22:20:55 Asia/Taipei
- stock_id: 9902
- stock_name: 台火
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9902_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9902_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9902_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9902_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9902_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9902_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9902_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9902_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9902_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9902_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9902_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9902_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9902_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9902.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9902.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9902.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9902.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9902.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9902.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9902_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9902_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9902_latest.md?ref=main

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
- open: 14
- high: 14.1
- low: 13.8
- close: 13.8
- volume: 86398
- ma5: 13.77
- ema23_primary: 14.1
- distance_to_ema23_pct: -2.14
- ma20: 14.11
- ma60: 14.59
- ma120: 15.87
- return_5d: 0.36
- return_20d: -3.83
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: -2.18
- distance_to_high_60_pct: -18.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,14.65,14.65,14.2,14.55,67178,14.69,-0.99,14.53,15.54,0.48
20260429,14.55,14.65,14.45,14.55,89605,14.68,-0.9,14.54,15.49,0.66
20260430,14.4,14.95,14.4,14.65,148970,14.68,-0.2,14.56,15.43,1.06
20260504,14.65,14.85,14.5,14.65,118832,14.68,-0.19,14.58,15.38,0.86
20260505,14.55,14.55,14.3,14.3,126088,14.65,-2.36,14.59,15.32,0.91
20260506,14.5,14.5,14.25,14.35,125037,14.62,-1.86,14.59,15.27,0.91
20260507,14.35,14.9,14.3,14.55,158430,14.62,-0.45,14.59,15.21,1.16
20260508,14.6,14.95,13.9,13.9,355810,14.56,-4.51,14.57,15.15,2.36
20260511,14.2,14.2,13.9,14.1,197384,14.52,-2.88,14.56,15.1,1.27
20260512,14.25,14.35,14.1,14.1,114785,14.48,-2.64,14.55,15.06,0.74
20260513,14.1,14.35,14,14.15,159505,14.46,-2.11,14.53,15.02,1.02
20260514,14.15,14.3,14,14,224371,14.42,-2.89,14.51,14.98,1.4
20260515,14.15,14.25,13.9,13.9,165578,14.37,-3.3,14.46,14.93,1.04
20260518,13.85,14.25,13.8,13.8,71884,14.33,-3.67,14.41,14.89,0.48
20260519,14.05,14.1,13.7,13.75,168338,14.28,-3.7,14.35,14.83,1.14
20260520,13.75,13.9,13.7,13.7,48798,14.23,-3.73,14.29,14.79,0.34
20260521,13.75,13.95,13.7,13.7,128205,14.19,-3.43,14.22,14.73,0.89
20260522,13.8,13.9,13.5,13.65,173087,14.14,-3.47,14.17,14.68,1.23
20260525,13.95,14.3,13.9,14,252442,14.13,-0.92,14.13,14.64,1.69
20260526,14,14.1,13.8,13.8,86398,14.1,-2.14,14.11,14.59,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.97
- over_600_ratio: 53.03
- over_800_ratio: 50.18
- over_1000_ratio: 50.18
- over_400_change_1w: 0.14
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.07,,49.77,,49.77,,0,False,False
20260508,56.53,0.46,49.78,0.01,49.78,0.01,1,False,True
20260515,56.83,0.3,50.03,0.25,50.03,0.25,2,True,True
20260522,56.97,0.14,50.18,0.15,50.18,0.15,3,True,True
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
