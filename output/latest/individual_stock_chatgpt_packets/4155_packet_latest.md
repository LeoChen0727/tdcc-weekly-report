# INDIVIDUAL STOCK CHATGPT PACKET - 4155 訊映

## Metadata
- generated_at: 2026-05-26 21:25:44 Asia/Taipei
- stock_id: 4155
- stock_name: 訊映
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4155_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4155_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4155_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4155_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4155_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4155_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4155_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4155_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4155_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4155_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4155_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4155_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4155_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4155.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4155.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4155.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4155.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4155.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4155.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4155_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4155_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4155_latest.md?ref=main

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
- open: 14.95
- high: 14.95
- low: 14.7
- close: 14.9
- volume: 342281
- ma5: 14.99
- ema23_primary: 14.07
- distance_to_ema23_pct: 5.87
- ma20: 13.86
- ma60: 13.59
- ma120: 14.16
- return_5d: 1.36
- return_20d: 15.5
- volume_ratio: 0.63
- distance_to_ma20_pct_auxiliary: 7.52
- distance_to_high_60_pct: -3.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.85,13,12.85,12.9,88714,13.26,-2.72,13.19,13.77,0.4
20260429,13,13,12.85,12.95,171709,13.23,-2.15,13.18,13.74,0.77
20260430,13.1,13.1,12.95,13,320867,13.22,-1.63,13.17,13.72,1.37
20260504,13,13.45,13,13.15,380070,13.21,-0.45,13.16,13.69,1.57
20260505,13.15,13.35,13.1,13.2,216821,13.21,-0.07,13.16,13.67,0.86
20260506,13.3,13.3,13.1,13.2,201600,13.21,-0.06,13.16,13.64,0.78
20260507,13.2,13.25,13.15,13.2,123965,13.21,-0.06,13.16,13.61,0.48
20260508,13.2,13.25,13,13.05,251631,13.19,-1.09,13.16,13.59,0.98
20260511,13,13.05,12.9,12.95,220346,13.17,-1.7,13.15,13.56,0.92
20260512,12.95,13,12.9,12.95,149797,13.16,-1.56,13.14,13.53,0.63
20260513,14.15,14.2,13.7,14.2,2351098,13.24,7.23,13.2,13.53,6.76
20260514,14.5,14.5,13.75,14,1751976,13.31,5.22,13.24,13.52,4.11
20260515,14.2,14.45,14.1,14.3,755993,13.39,6.81,13.3,13.52,1.68
20260518,14.35,14.85,14.3,14.45,619304,13.48,7.22,13.35,13.52,1.34
20260519,14.4,14.8,14.15,14.7,605528,13.58,8.26,13.4,13.53,1.3
20260520,14.7,14.8,14.45,14.8,472541,13.68,8.18,13.47,13.54,0.99
20260521,14.8,15.3,14.8,15.3,629363,13.82,10.74,13.56,13.56,1.25
20260522,15.5,15.5,15.2,15.2,547323,13.93,9.11,13.68,13.58,1.07
20260525,15.2,15.35,14.75,14.75,598245,14,5.36,13.76,13.58,1.12
20260526,14.95,14.95,14.7,14.9,342281,14.07,5.87,13.86,13.59,0.63
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.45
- over_600_ratio: 37.63
- over_800_ratio: 34.31
- over_1000_ratio: 31.27
- over_400_change_1w: 1.09
- over_800_change_1w: 0.77
- over_1000_change_1w: 0.75
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.48,,33,,30.53,,0,False,False
20260508,41.04,0.56,33.55,0.55,30.52,-0.01,1,False,True
20260515,41.36,0.32,33.54,-0.01,30.52,0,2,False,False
20260522,42.45,1.09,34.31,0.77,31.27,0.75,3,True,True
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
