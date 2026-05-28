# INDIVIDUAL STOCK CHATGPT PACKET - 1466 聚隆

## Metadata
- generated_at: 2026-05-28 19:31:33 Asia/Taipei
- stock_id: 1466
- stock_name: 聚隆
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1466_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1466_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1466_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1466_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1466_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1466_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1466_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1466_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1466_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1466_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1466_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1466_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1466_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1466.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1466.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1466.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1466.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1466.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1466.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1466_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1466_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1466_latest.md?ref=main

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
- open: 13.55
- high: 14.15
- low: 13.55
- close: 13.8
- volume: 409748
- ma5: 14.29
- ema23_primary: 15.06
- distance_to_ema23_pct: -8.37
- ma20: 15
- ma60: 16.39
- ma120: 15.64
- return_5d: -6.12
- return_20d: -14.29
- volume_ratio: 2.04
- distance_to_ma20_pct_auxiliary: -8.02
- distance_to_high_60_pct: -30.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,16.1,16.6,15.8,16.3,191164,16.73,-2.57,16.73,16.81,0.88
20260504,16.25,16.4,15.8,15.8,281906,16.65,-5.12,16.68,16.84,1.28
20260505,15.95,16.1,15.75,15.85,149422,16.59,-4.43,16.64,16.86,0.69
20260506,16.1,16.1,15.15,15.95,334442,16.53,-3.52,16.59,16.88,1.46
20260507,15.9,16,15.45,15.95,164127,16.48,-3.24,16.54,16.9,0.73
20260508,15.95,15.95,15.6,15.6,104411,16.41,-4.94,16.46,16.92,0.46
20260511,15.85,15.85,15.3,15.85,274097,16.36,-3.14,16.41,16.94,1.19
20260512,15.9,15.95,15.25,15.25,243596,16.27,-6.27,16.34,16.95,1.05
20260513,15.2,15.7,14.5,14.5,384400,16.12,-10.07,16.23,16.94,1.68
20260514,14.55,14.85,14.3,14.35,197655,15.98,-10.17,16.13,16.94,0.85
20260515,14.5,14.8,14.35,14.4,113021,15.84,-9.11,16.01,16.92,0.5
20260518,14.4,14.6,14.3,14.55,135479,15.74,-7.54,15.9,16.89,0.6
20260519,14.55,14.9,14.35,14.9,50090,15.67,-4.89,15.8,16.85,0.23
20260520,14.8,14.8,14.5,14.65,146004,15.58,-5.98,15.68,16.8,0.69
20260521,14.7,14.7,14.5,14.7,87245,15.51,-5.21,15.56,16.75,0.43
20260522,14.8,14.8,14.45,14.75,137575,15.45,-4.5,15.45,16.7,0.69
20260525,14.95,14.95,14.2,14.7,250269,15.38,-4.44,15.34,16.65,1.27
20260526,14.6,14.6,14.2,14.45,128432,15.31,-5.59,15.23,16.59,0.67
20260527,14.45,14.45,13.7,13.75,243328,15.18,-9.39,15.12,16.49,1.27
20260528,13.55,14.15,13.55,13.8,409748,15.06,-8.37,15,16.39,2.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.77
- over_600_ratio: 69.06
- over_800_ratio: 66.05
- over_1000_ratio: 65.16
- over_400_change_1w: 0.04
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.79,,66,,65.11,,0,False,False
20260508,72.78,-0.01,65.99,-0.01,65.1,-0.01,0,False,False
20260515,72.73,-0.05,65.99,0,65.1,0,0,False,False
20260522,72.77,0.04,66.05,0.06,65.16,0.06,1,True,True
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
