# INDIVIDUAL STOCK CHATGPT PACKET - 2424 隴華

## Metadata
- generated_at: 2026-05-26 23:53:19 Asia/Taipei
- stock_id: 2424
- stock_name: 隴華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2424_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2424_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2424_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2424_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2424_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2424_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2424_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2424_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2424_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2424_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2424_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2424_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2424_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2424.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2424.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2424.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2424.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2424.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2424.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2424_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2424_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2424_latest.md?ref=main

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
- open: 12.25
- high: 13.75
- low: 12.25
- close: 12.35
- volume: 541180
- ma5: 14.86
- ema23_primary: 19.61
- distance_to_ema23_pct: -37.02
- ma20: 19.62
- ma60: 24.72
- ma120: 30.32
- return_5d: -38.1
- return_20d: -43.74
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: -37.06
- distance_to_high_60_pct: -65.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,21.95,22.9,21.95,22.35,33073,24.69,-9.48,24.02,30.06,0.19
20260429,22.35,22.35,21.9,21.9,80691,24.46,-10.46,23.79,29.84,0.5
20260430,21.9,21.9,21.4,21.6,53327,24.22,-10.82,23.65,29.6,0.34
20260504,21.6,21.6,20.3,20.4,253592,23.9,-14.65,23.39,29.35,1.53
20260505,20.05,20.45,19.75,19.95,184945,23.57,-15.37,23.11,29.07,1.08
20260506,19.95,20.45,18.15,18.3,459186,23.13,-20.89,22.8,28.77,2.42
20260507,18.55,18.6,17.3,17.5,477014,22.66,-22.79,22.45,28.4,2.25
20260508,17.8,19.25,17.2,19.25,448277,22.38,-13.98,22.12,28.02,1.98
20260511,21.15,21.15,21.15,21.15,123217,22.28,-5.06,21.95,27.72,0.55
20260512,23.25,23.25,23.25,23.25,398147,22.36,3.99,21.9,27.47,1.65
20260513,25.5,25.55,23.95,25.55,1095022,22.62,12.93,22.01,27.27,3.77
20260514,27.65,27.65,23,23.6,1008212,22.71,3.94,22,27.02,2.98
20260515,21.25,23.45,21.25,21.25,444095,22.58,-5.91,21.92,26.73,1.3
20260518,21,22.2,20,22.15,181718,22.55,-1.76,21.91,26.49,0.53
20260519,19.95,19.95,19.95,19.95,250192,22.33,-10.66,21.78,26.23,0.72
20260520,18,18,18,18,84435,21.97,-18.07,21.53,25.99,0.24
20260521,16.2,16.2,16.2,16.2,92316,21.49,-24.61,21.09,25.72,0.27
20260522,14.6,14.6,14.6,14.6,93765,20.92,-30.2,20.59,25.4,0.3
20260525,13.15,13.15,13.15,13.15,106132,20.27,-35.12,20.1,25.07,0.35
20260526,12.25,13.75,12.25,12.35,541180,19.61,-37.02,19.62,24.72,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.25
- over_600_ratio: 83.42
- over_800_ratio: 83.42
- over_1000_ratio: 81.75
- over_400_change_1w: -0.24
- over_800_change_1w: -0.24
- over_1000_change_1w: -0.24
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.5,,83.66,,81.99,,0,False,False
20260508,84.49,-1.01,83.66,0,81.99,0,0,False,False
20260515,84.49,0,83.66,0,81.99,0,0,False,False
20260522,84.25,-0.24,83.42,-0.24,81.75,-0.24,0,False,False
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
