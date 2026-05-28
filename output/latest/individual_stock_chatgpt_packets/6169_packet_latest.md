# INDIVIDUAL STOCK CHATGPT PACKET - 6169 昱泉

## Metadata
- generated_at: 2026-05-28 20:19:56 Asia/Taipei
- stock_id: 6169
- stock_name: 昱泉
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6169_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6169_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6169_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6169_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6169_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6169_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6169_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6169_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6169_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6169_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6169_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6169_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6169_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6169.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6169.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6169.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6169.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6169.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6169.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6169_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6169_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6169_latest.md?ref=main

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
- open: 14.15
- high: 14.2
- low: 13.75
- close: 13.85
- volume: 14000
- ma5: 14.15
- ema23_primary: 15.21
- distance_to_ema23_pct: -8.91
- ma20: 15.37
- ma60: 16.32
- ma120: 17.69
- return_5d: -3.82
- return_20d: -18.53
- volume_ratio: 0.4
- distance_to_ma20_pct_auxiliary: -9.9
- distance_to_high_60_pct: -23.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,17,17,16.5,16.9,17000,16.8,0.57,16.69,17.29,0.7
20260430,16.75,16.75,16.7,16.7,2000,16.8,-0.57,16.7,17.25,0.09
20260504,16.5,16.6,16.5,16.6,2000,16.78,-1.07,16.71,17.21,0.09
20260505,16.5,16.6,16.5,16.6,8000,16.76,-0.98,16.72,17.17,0.41
20260506,16.6,16.75,16.55,16.55,6000,16.75,-1.18,16.73,17.12,0.31
20260507,17,17.1,16.7,16.95,82000,16.76,1.11,16.76,17.09,3.75
20260508,17.1,17.1,16.5,16.6,18000,16.75,-0.9,16.78,17.05,0.87
20260511,16.6,16.65,16.3,16.3,116000,16.71,-2.47,16.78,17,4.39
20260512,16.35,16.7,15.8,15.9,119000,16.64,-4.48,16.71,16.96,3.97
20260514,15.85,15.85,15,15,55000,16.51,-9.13,16.6,16.9,1.79
20260515,14.75,14.75,14.35,14.5,60000,16.34,-11.26,16.46,16.82,1.8
20260518,14.35,15,14.35,14.9,24000,16.22,-8.14,16.36,16.77,0.71
20260519,14.7,14.9,14.35,14.35,74000,16.06,-10.67,16.23,16.71,2.03
20260520,14.2,14.65,14.2,14.45,33000,15.93,-9.29,16.12,16.65,0.9
20260521,14.05,14.5,14.05,14.4,11000,15.8,-8.88,16.01,16.59,0.3
20260522,14.9,15,14.5,14.75,15000,15.71,-6.14,15.9,16.54,0.43
20260525,14.75,14.75,14.2,14.3,14000,15.6,-8.32,15.8,16.49,0.4
20260526,14.3,14.3,13.8,14.15,14000,15.48,-8.57,15.68,16.44,0.39
20260527,14.35,14.35,13.6,13.7,14000,15.33,-10.62,15.53,16.38,0.4
20260528,14.15,14.2,13.75,13.85,14000,15.21,-8.91,15.37,16.32,0.4
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 30.31
- over_600_ratio: 26.44
- over_800_ratio: 26.44
- over_1000_ratio: 26.44
- over_400_change_1w: 1.74
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,28.57,,26.44,,26.44,,0,False,False
20260508,28.57,0,26.44,0,26.44,0,0,False,False
20260515,28.57,0,26.44,0,26.44,0,0,False,False
20260522,30.31,1.74,26.44,0,26.44,0,1,False,False
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
