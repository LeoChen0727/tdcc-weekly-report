# INDIVIDUAL STOCK CHATGPT PACKET - 2314 台揚

## Metadata
- generated_at: 2026-05-28 19:31:50 Asia/Taipei
- stock_id: 2314
- stock_name: 台揚
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2314_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2314_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2314_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2314_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2314_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2314_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2314_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2314_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2314_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2314_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2314_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2314_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2314_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2314.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2314.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2314.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2314.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2314.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2314.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2314_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2314_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2314_latest.md?ref=main

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
- open: 15.8
- high: 15.85
- low: 15.6
- close: 15.75
- volume: 437413
- ma5: 15.98
- ema23_primary: 14.77
- distance_to_ema23_pct: 6.65
- ma20: 14.07
- ma60: 15.97
- ma120: 19.08
- return_5d: -1.87
- return_20d: 11.7
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: 11.94
- distance_to_high_60_pct: -29.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,14.1,14.25,14.1,14.1,261195,15.61,-9.66,14.95,18.17,0.45
20260504,14.15,14.5,14.15,14.2,181444,15.49,-8.33,14.71,18.04,0.31
20260505,14.25,14.25,13.8,13.8,431779,15.35,-10.1,14.56,17.9,0.79
20260506,14.1,14.1,13.8,13.8,324759,15.22,-9.33,14.48,17.77,0.6
20260507,13.8,13.8,12.8,12.95,786356,15.03,-13.85,14.44,17.62,1.42
20260508,13,13,12.9,13,395675,14.86,-12.53,14.47,17.47,0.72
20260511,13.2,13.2,12.5,12.6,619076,14.67,-14.13,14.41,17.33,1.33
20260512,12.7,13,12.6,13,497149,14.53,-10.56,14.38,17.21,1.13
20260513,12.7,13.45,12.7,13.05,247484,14.41,-9.44,14.37,17.08,0.59
20260514,12.85,13.2,12.6,12.6,348034,14.26,-11.64,14.32,16.93,0.83
20260515,12.85,13.2,12.35,12.35,297770,14.1,-12.41,14.23,16.79,0.72
20260518,12.35,12.35,12.05,12.1,266831,13.93,-13.16,14.06,16.65,0.66
20260519,13.25,13.3,13.25,13.3,794449,13.88,-4.19,13.88,16.52,1.94
20260520,13.45,14.6,13.45,14.6,1386121,13.94,4.73,13.83,16.42,3.28
20260521,16,16.05,16,16.05,1576371,14.12,13.7,13.84,16.35,3.25
20260522,17.6,17.6,15.8,15.8,1909285,14.26,10.82,13.79,16.27,3.41
20260525,17.35,17.35,16.35,16.4,1003227,14.44,13.61,13.83,16.21,1.67
20260526,16.8,16.8,16.3,16.35,526389,14.6,12.02,13.92,16.13,0.86
20260527,16.4,16.8,15.6,15.6,734191,14.68,6.28,13.99,16.05,1.15
20260528,15.8,15.85,15.6,15.75,437413,14.77,6.65,14.07,15.97,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 10.84
- over_600_ratio: 7.74
- over_800_ratio: 5.21
- over_1000_ratio: 5.21
- over_400_change_1w: -1.3
- over_800_change_1w: -1.43
- over_1000_change_1w: -1.43
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,12.43,,7.66,,7.66,,0,False,False
20260508,11.94,-0.49,7.06,-0.6,7.06,-0.6,1,False,False
20260515,12.14,0.2,6.64,-0.42,6.64,-0.42,2,False,False
20260522,10.84,-1.3,5.21,-1.43,5.21,-1.43,0,False,False
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
