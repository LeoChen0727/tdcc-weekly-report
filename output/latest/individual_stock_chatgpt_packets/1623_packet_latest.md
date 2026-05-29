# INDIVIDUAL STOCK CHATGPT PACKET - 1623 大東電

## Metadata
- generated_at: 2026-05-29 19:31:46 Asia/Taipei
- stock_id: 1623
- stock_name: 大東電
- packet_status: standard_rawdata_packet
- latest_price_date: 20260529
- price_rows: 81
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1623_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1623_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1623_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1623_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1623_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1623_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1623_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1623_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1623_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1623_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1623_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1623_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1623_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1623.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1623.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1623.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1623.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1623.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1623.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1623_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1623_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1623_latest.md?ref=main

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
- open: 248
- high: 248.5
- low: 239.5
- close: 243.5
- volume: 403144
- ma5: 237
- ema23_primary: 230.42
- distance_to_ema23_pct: 5.68
- ma20: 233.78
- ma60: 213.97
- ma120: 221.56
- return_5d: 8.46
- return_20d: 1.88
- volume_ratio: 1.48
- distance_to_ma20_pct_auxiliary: 4.16
- distance_to_high_60_pct: -7.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,241.5,258,241.5,250,293063,221.86,12.69,214.12,214.77,0.78
20260505,244.5,246.5,242,246.5,145005,223.91,10.09,217.57,213.95,0.38
20260506,248,249,243,244.5,135116,225.62,8.37,220.97,213.47,0.35
20260507,247,247,244.5,246,135730,227.32,8.22,224.15,212.94,0.35
20260508,245,248.5,243,246,178907,228.88,7.48,227.38,212.67,0.46
20260511,249.5,250,240.5,242.5,349201,230.01,5.43,230.43,212.61,0.87
20260512,240,241,230.5,231.5,416410,230.14,0.59,233.03,212.6,1
20260513,231.5,231.5,222.5,226,255927,229.79,-1.65,234.97,212.48,0.61
20260514,226,228.5,220.5,222,196490,229.14,-3.12,236.75,212.39,0.47
20260515,222,242,222,229.5,431066,229.17,0.14,238.45,212.58,1
20260518,229,229,222,223.5,156849,228.7,-2.27,239.15,212.58,0.38
20260519,223.5,226,220.5,220.5,102626,228.02,-3.3,238.68,212.67,0.25
20260520,221,221,215,215.5,133097,226.97,-5.06,236.8,212.78,0.36
20260521,220,224,218.5,222,83875,226.56,-2.01,235.15,213.06,0.33
20260522,225,226,221,224.5,186243,226.39,-0.83,233.93,213.13,0.9
20260525,229,230,225,228,227518,226.52,0.65,233.32,213.28,1.13
20260526,232,232,227.5,229,193839,226.73,1,233.2,213.09,0.97
20260527,230,245,230,238.5,555880,227.71,4.74,233.25,213.18,2.53
20260528,242,254,238.5,246,872040,229.23,7.31,233.55,213.53,3.39
20260529,248,248.5,239.5,243.5,403144,230.42,5.68,233.78,213.97,1.48
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.69
- over_600_ratio: 77.96
- over_800_ratio: 74.84
- over_1000_ratio: 74.84
- over_400_change_1w: -0.09
- over_800_change_1w: -0.09
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.86,,74.99,,74.99,,0,False,False
20260508,78.8,-0.06,74.93,-0.06,74.93,-0.06,0,False,False
20260515,78.78,-0.02,74.93,0,74.93,0,0,False,False
20260522,78.69,-0.09,74.84,-0.09,74.84,-0.09,0,False,False
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
