# INDIVIDUAL STOCK CHATGPT PACKET - 6279 胡連

## Metadata
- generated_at: 2026-05-30 23:43:00 Asia/Taipei
- stock_id: 6279
- stock_name: 胡連
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6279_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6279_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6279_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6279_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6279_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6279_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6279_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6279_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6279_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6279_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6279_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6279_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6279_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6279.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6279.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6279.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6279.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6279.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6279.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6279_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6279_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6279_latest.md?ref=main

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
- open: 125
- high: 126
- low: 122
- close: 122.5
- volume: 123000
- ma5: 119.5
- ema23_primary: 116.48
- distance_to_ema23_pct: 5.17
- ma20: 117.58
- ma60: 112.32
- ma120: 117.62
- return_5d: 2.08
- return_20d: 13.95
- volume_ratio: 0.13
- distance_to_ma20_pct_auxiliary: 4.19
- distance_to_high_60_pct: -3.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,108.5,108.5,105,106,481000,107.58,-1.47,106.25,111.33,1.07
20260505,106.5,109.5,106,109,578000,107.7,1.21,106.3,111.07,1.24
20260506,110.5,116.5,108.5,116,2465000,108.39,7.02,106.78,110.94,4.36
20260507,115,124,115,124,4315000,109.69,13.05,107.7,110.97,5.83
20260508,123.5,126.5,122,124,2432000,110.88,11.83,108.75,111.03,2.96
20260511,122,123.5,120,120.5,1866000,111.68,7.89,109.6,111.1,2.1
20260512,120.5,121,118.5,119,1091000,112.29,5.97,110.38,111.2,1.18
20260513,119,121.5,118,118.5,732000,112.81,5.04,111.08,111.3,0.78
20260514,120,120,117,117.5,652000,113.2,3.8,111.7,111.38,0.69
20260515,117.5,118.5,115.5,115.5,645000,113.39,1.86,112.12,111.42,0.67
20260518,115,115,113.5,113.5,695000,113.4,0.09,112.35,111.45,0.72
20260519,114.5,116.5,113,113.5,695000,113.41,0.08,112.62,111.47,0.71
20260520,113.5,118.5,113.5,117.5,1235000,113.75,3.3,113.08,111.56,1.21
20260521,118.5,120.5,118.5,119.5,922000,114.23,4.61,113.55,111.67,0.88
20260522,119.5,120.5,118.5,120,120000,114.71,4.61,114.17,111.84,0.12
20260525,121,121,118,119,119000,115.07,3.42,114.83,111.99,0.12
20260526,119,119.5,116,117,117000,115.23,1.54,115.4,112.09,0.12
20260527,117,119,116,116.5,117000,115.33,1.01,116,112.08,0.12
20260528,119,127.5,119,122.5,124000,115.93,5.67,116.83,112.17,0.13
20260529,125,126,122,122.5,123000,116.48,5.17,117.58,112.32,0.13
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 46.09
- over_600_ratio: 41.05
- over_800_ratio: 38.69
- over_1000_ratio: 35.6
- over_400_change_1w: -0.39
- over_800_change_1w: 0.66
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.96,,40.54,,37.28,,0,False,False
20260508,47.04,-0.92,39.75,-0.79,36.49,-0.79,0,False,False
20260515,46.46,-0.58,39.71,-0.04,36.45,-0.04,0,False,False
20260522,46.48,0.02,38.03,-1.68,35.6,-0.85,1,False,False
20260529,46.09,-0.39,38.69,0.66,35.6,0,2,False,True
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
