# INDIVIDUAL STOCK CHATGPT PACKET - 4113 聯上

## Metadata
- generated_at: 2026-05-26 22:19:22 Asia/Taipei
- stock_id: 4113
- stock_name: 聯上
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4113_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4113_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4113_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4113_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4113_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4113_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4113_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4113_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4113_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4113_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4113_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4113_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4113_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4113.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4113.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4113.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4113.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4113.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4113.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4113_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4113_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4113_latest.md?ref=main

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
- open: 14.65
- high: 14.7
- low: 14.35
- close: 14.65
- volume: 15000
- ma5: 15.11
- ema23_primary: 15.21
- distance_to_ema23_pct: -3.65
- ma20: 14.95
- ma60: 16.6
- ma120: 19.35
- return_5d: -0.68
- return_20d: 1.74
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -1.99
- distance_to_high_60_pct: -27.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,14.4,14.55,14.1,14.3,349000,16.2,-11.75,16.08,18.58,1.11
20260429,14.1,14.25,14,14.2,165000,16.04,-11.46,15.93,18.45,0.52
20260430,14.35,14.6,14.05,14.55,289000,15.91,-8.57,15.81,18.33,0.94
20260504,14.55,15,14.15,14.8,368000,15.82,-6.45,15.7,18.2,1.17
20260505,14.7,16.25,14.4,16.25,868000,15.86,2.48,15.66,18.1,2.48
20260506,17.1,17.35,16.1,16.3,1184000,15.89,2.56,15.63,18,3
20260507,16.3,16.45,15.35,15.35,366000,15.85,-3.14,15.57,17.88,0.96
20260508,15.2,15.2,14.75,14.85,231000,15.77,-5.8,15.49,17.75,0.59
20260511,14.9,14.95,14.5,14.75,434000,15.68,-5.93,15.41,17.63,1.09
20260512,14.6,14.9,14.55,14.8,196000,15.61,-5.17,15.32,17.53,0.5
20260513,14.55,14.8,14.45,14.8,448000,15.54,-4.76,15.25,17.43,1.11
20260514,14.8,14.8,14.4,14.45,158000,15.45,-6.47,15.19,17.33,0.42
20260515,14.4,14.6,14.35,14.6,238000,15.38,-5.06,15.11,17.23,0.63
20260518,14.3,14.7,14.3,14.65,200000,15.32,-4.36,15.04,17.13,0.53
20260519,14.65,14.8,14.6,14.75,100000,15.27,-3.41,14.98,17.04,0.27
20260520,14.75,15.1,14.75,15,290000,15.25,-1.62,14.94,16.95,0.77
20260521,16.45,16.45,15.25,15.5,253000,15.27,1.51,14.94,16.87,0.68
20260522,15.5,15.5,15.05,15.45,15000,15.28,1.09,14.94,16.78,0.04
20260525,15.25,15.25,14.6,14.95,15000,15.26,-2.01,14.94,16.69,0.04
20260526,14.65,14.7,14.35,14.65,15000,15.21,-3.65,14.95,16.6,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.61
- over_600_ratio: 69.12
- over_800_ratio: 64.33
- over_1000_ratio: 62.43
- over_400_change_1w: 0.3
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.8
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.04,,64.23,,63.47,,0,False,False
20260508,74.22,0.18,64.32,0.09,63.56,0.09,1,False,True
20260515,74.31,0.09,64.38,0.06,63.23,-0.33,2,False,True
20260522,74.61,0.3,64.33,-0.05,62.43,-0.8,3,False,False
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
