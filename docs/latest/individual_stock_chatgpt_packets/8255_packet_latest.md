# INDIVIDUAL STOCK CHATGPT PACKET - 8255 朋程

## Metadata
- generated_at: 2026-05-30 23:43:54 Asia/Taipei
- stock_id: 8255
- stock_name: 朋程
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8255_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8255_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8255_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8255_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8255_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8255_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8255_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8255_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8255_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8255_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8255_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8255_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8255_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8255.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8255.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8255.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8255.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8255.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8255.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8255_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8255_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8255_latest.md?ref=main

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
- date: 20260529
- open: 198.5
- high: 202
- low: 193.5
- close: 199.5
- volume: 199000
- ma5: 185.3
- ema23_primary: 158.79
- distance_to_ema23_pct: 25.64
- ma20: 157.2
- ma60: 136.76
- ma120: 130.29
- return_5d: 27.07
- return_20d: 46.69
- volume_ratio: 0.16
- distance_to_ma20_pct_auxiliary: 26.91
- distance_to_high_60_pct: -2.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,138.5,145.5,136,142.5,1440000,130.58,9.13,128.82,127.42,2.43
20260505,141.5,152,141.5,148.5,2509000,132.07,12.44,130.38,127.7,3.55
20260506,150,150.5,141,143,1361000,132.99,7.53,131.4,127.9,1.79
20260507,143,148.5,141,146,1043000,134.07,8.9,132.55,128.14,1.31
20260508,146,149,141.5,145.5,694000,135.02,7.76,133.75,128.35,0.85
20260511,144,151,141.5,149,1288000,136.19,9.41,135.07,128.68,1.48
20260512,151,153,148,148.5,1547000,137.21,8.23,136.45,129.06,1.66
20260513,146,148.5,143.5,145,629000,137.86,5.18,137.5,129.39,0.67
20260514,149,150.5,143.5,144,927000,138.37,4.07,138.55,129.65,0.94
20260515,146,149.5,138,141,1488000,138.59,1.74,139.25,129.86,1.45
20260518,140.5,144,133,143,830000,138.96,2.91,139.82,130.13,0.81
20260519,143.5,157,141.5,154,3982000,140.21,9.83,140.9,130.6,3.33
20260520,157,158,150,156,3760000,141.53,10.22,142,131.1,2.79
20260521,157,160,154.5,154.5,1996000,142.61,8.34,142.9,131.61,1.43
20260522,156.5,158,155,157,156000,143.81,9.17,144.15,132.1,0.12
20260525,161,172,153,170,164000,145.99,16.45,146.18,132.74,0.12
20260526,171.5,187,169,187,182000,149.41,25.16,148.8,133.69,0.14
20260527,198.5,205,184.5,185.5,193000,152.42,21.71,151.53,134.59,0.15
20260528,186,200,179.5,184.5,190000,155.09,18.96,154.03,135.52,0.15
20260529,198.5,202,193.5,199.5,199000,158.79,25.64,157.2,136.76,0.16
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 55.68
- over_600_ratio: 53.63
- over_800_ratio: 49.53
- over_1000_ratio: 47.8
- over_400_change_1w: 2.23
- over_800_change_1w: -0.79
- over_1000_change_1w: -1.68
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.55,,50.91,,50.07,,0,False,False
20260508,53.1,-0.45,50.66,-0.25,49.82,-0.25,0,False,False
20260515,53.58,0.48,50.79,0.13,49.95,0.13,1,True,True
20260522,53.45,-0.13,50.32,-0.47,49.48,-0.47,0,False,False
20260529,55.68,2.23,49.53,-0.79,47.8,-1.68,1,False,False
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
