# INDIVIDUAL STOCK CHATGPT PACKET - 8488 吉源-KY

## Metadata
- generated_at: 2026-05-26 22:20:52 Asia/Taipei
- stock_id: 8488
- stock_name: 吉源-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 123
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8488_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8488_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8488_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8488_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8488_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8488_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8488_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8488_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8488_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8488_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8488_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8488_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8488_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8488.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8488.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8488.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8488.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8488.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8488.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8488_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8488_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8488_latest.md?ref=main

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
- open: 9.76
- high: 9.83
- low: 9.64
- close: 9.8
- volume: 5000
- ma5: 9.77
- ema23_primary: 9.99
- distance_to_ema23_pct: -1.94
- ma20: 10.03
- ma60: 9.99
- ma120: 10.03
- return_5d: -2.97
- return_20d: -2.49
- volume_ratio: 0.09
- distance_to_ma20_pct_auxiliary: -2.29
- distance_to_high_60_pct: -14.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260424,10,10.15,10,10.15,5000,10.08,0.66,10.03,9.97,0.05
20260428,10.2,10.2,9.9,9.9,2000,10.07,-1.67,10.03,9.97,0.02
20260429,9.95,10.1,9.95,10.1,6000,10.07,0.29,10.04,9.97,0.07
20260430,9.99,10.3,9.98,10.3,29000,10.09,2.08,10.06,9.97,0.48
20260504,10.3,10.3,10.2,10.2,3411,10.1,1,10.08,9.98,0.07
20260505,10.05,10.25,10.05,10.1,3000,10.1,0.01,10.1,9.98,0.07
20260506,10.1,10.2,9.99,10.1,12000,10.1,0.01,10.11,9.98,0.26
20260507,10.05,10.1,9.93,10.05,15000,10.1,-0.45,10.13,9.98,0.34
20260508,10.1,10.1,10.1,10.1,2832,10.1,0.04,10.15,9.98,0.06
20260511,10.1,10.1,9.99,10,4000,10.09,-0.87,10.16,9.98,0.14
20260512,9.99,10,9.91,9.91,22000,10.07,-1.62,10.17,9.98,0.76
20260513,10.05,10.1,9.9,9.99,14000,10.07,-0.75,10.17,9.98,0.48
20260514,9.91,9.98,9.85,9.89,14000,10.05,-1.6,10.16,9.98,0.51
20260518,9.84,10.85,9.8,10.85,358318,10.12,7.24,10.19,10,12.83
20260519,10.85,11.45,10,10.1,455684,10.12,-0.16,10.18,10,9.16
20260520,10.1,10.1,9.8,9.8,67422,10.09,-2.87,10.14,10.01,1.28
20260521,9.8,9.8,9.52,9.69,76025,10.06,-3.65,10.1,10,1.36
20260522,9.62,9.87,9.62,9.85,14000,10.04,-1.89,10.07,10,0.25
20260525,9.85,9.85,9.71,9.71,4000,10.01,-3.02,10.04,10,0.07
20260526,9.76,9.83,9.64,9.8,5000,9.99,-1.94,10.03,9.99,0.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 87.08
- over_600_ratio: 84.54
- over_800_ratio: 82.67
- over_1000_ratio: 81.43
- over_400_change_1w: -0.03
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.06,,82.66,,81.42,,0,False,False
20260508,87.07,0.01,82.67,0.01,81.43,0.01,1,True,True
20260515,87.11,0.04,82.71,0.04,81.47,0.04,2,True,True
20260522,87.08,-0.03,82.67,-0.04,81.43,-0.04,0,False,False
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
