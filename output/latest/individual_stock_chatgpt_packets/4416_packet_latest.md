# INDIVIDUAL STOCK CHATGPT PACKET - 4416 三圓

## Metadata
- generated_at: 2026-05-30 23:42:20 Asia/Taipei
- stock_id: 4416
- stock_name: 三圓
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4416_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4416_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4416_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4416_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4416_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4416.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4416.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4416.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4416.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4416_latest.md?ref=main

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
- open: 10.95
- high: 11.15
- low: 10.85
- close: 10.9
- volume: 11000
- ma5: 11.17
- ema23_primary: 12
- distance_to_ema23_pct: -9.18
- ma20: 11.84
- ma60: 13.45
- ma120: 22.04
- return_5d: -2.68
- return_20d: -15.18
- volume_ratio: 0.1
- distance_to_ma20_pct_auxiliary: -7.94
- distance_to_high_60_pct: -47.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.95,13,12.45,12.65,410000,13.99,-9.59,13.47,18.49,0.8
20260505,12.65,13.1,12.65,12.7,109000,13.88,-8.53,13.42,18.2,0.21
20260506,12.75,12.75,12.5,12.6,157000,13.78,-8.54,13.39,17.91,0.31
20260507,12.6,12.6,12.3,12.5,225000,13.67,-8.56,13.38,17.63,0.45
20260508,12.5,12.7,12.5,12.55,89000,13.58,-7.57,13.39,17.34,0.18
20260511,12.4,12.75,12.35,12.45,81000,13.48,-7.66,13.38,17.06,0.17
20260512,12.45,12.45,12.25,12.25,102000,13.38,-8.45,13.36,16.77,0.22
20260513,12.25,12.95,12.25,12.3,81000,13.29,-7.45,13.35,16.49,0.18
20260514,12.5,12.5,12.15,12.4,90000,13.22,-6.18,13.31,16.21,0.2
20260515,12.35,12.35,11.5,11.55,264000,13.08,-11.68,13.21,15.92,0.6
20260518,10.55,11.7,10.55,11.55,212000,12.95,-10.81,13.03,15.63,0.55
20260519,11.8,11.9,11.2,11.4,50000,12.82,-11.08,12.81,15.37,0.19
20260520,11.45,11.6,11.05,11.3,97000,12.69,-10.98,12.63,15.09,0.39
20260521,11.3,11.75,11.3,11.55,74000,12.6,-8.33,12.46,14.82,0.31
20260522,11.55,11.55,11.2,11.2,11000,12.48,-10.27,12.32,14.56,0.05
20260525,11.8,12.3,11.8,12.3,12000,12.47,-1.34,12.24,14.33,0.06
20260526,12.15,12.15,11.1,11.1,11000,12.35,-10.14,12.15,14.1,0.07
20260527,10.55,11.05,10.15,10.75,11000,12.22,-12.03,12.04,13.87,0.08
20260528,10.8,11.25,10.8,10.8,11000,12.1,-10.75,11.94,13.65,0.09
20260529,10.95,11.15,10.85,10.9,11000,12,-9.18,11.84,13.45,0.1
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 80.22
- over_600_ratio: 73.8
- over_800_ratio: 69.98
- over_1000_ratio: 67.31
- over_400_change_1w: -2.51
- over_800_change_1w: -2.9
- over_1000_change_1w: -2.9
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.06,,72.78,,70.11,,0,False,False
20260508,82.06,0,72.78,0,70.11,0,0,False,False
20260515,82.68,0.62,72.85,0.07,70.18,0.07,1,True,True
20260522,82.73,0.05,72.88,0.03,70.21,0.03,2,True,True
20260529,80.22,-2.51,69.98,-2.9,67.31,-2.9,0,False,False
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
