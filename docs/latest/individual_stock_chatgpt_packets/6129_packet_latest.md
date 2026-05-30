# INDIVIDUAL STOCK CHATGPT PACKET - 6129 普誠

## Metadata
- generated_at: 2026-05-30 23:42:50 Asia/Taipei
- stock_id: 6129
- stock_name: 普誠
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6129_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6129_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6129_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6129_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6129_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6129_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6129_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6129_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6129_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6129_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6129_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6129_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6129_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6129.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6129.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6129.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6129.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6129.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6129.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6129_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6129_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6129_latest.md?ref=main

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
- open: 15.15
- high: 16.6
- low: 15.1
- close: 16.6
- volume: 16000
- ma5: 15.67
- ema23_primary: 15.86
- distance_to_ema23_pct: 4.63
- ma20: 15.97
- ma60: 15.85
- ma120: 15.37
- return_5d: 4.4
- return_20d: -1.48
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: 3.94
- distance_to_high_60_pct: -11.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,16.85,17.55,16.85,17.2,721000,16.44,4.63,16.38,15.78,0.71
20260505,17.2,18.8,17.2,18.1,2073000,16.58,9.18,16.55,15.79,1.88
20260506,18.2,18.2,17.25,17.45,1485000,16.65,4.8,16.7,15.81,1.28
20260507,17.45,17.45,16.7,16.75,1676000,16.66,0.55,16.74,15.8,1.38
20260508,16.7,16.7,16.1,16.15,1166000,16.62,-2.81,16.78,15.8,0.96
20260511,16.15,16.75,16.1,16.4,597000,16.6,-1.2,16.81,15.82,0.49
20260512,16.5,16.5,16.05,16.1,1041000,16.56,-2.76,16.81,15.83,0.84
20260513,16,16.2,15.7,15.85,622000,16.5,-3.93,16.79,15.84,0.5
20260514,16,16.1,15.5,15.6,631000,16.42,-5.01,16.77,15.84,0.51
20260515,15.55,15.85,15.15,15.2,784000,16.32,-6.87,16.71,15.84,0.62
20260518,15.1,15.1,14.8,15,582000,16.21,-7.47,16.64,15.84,0.46
20260519,15.15,15.15,14.75,14.85,633000,16.1,-7.75,16.56,15.84,0.51
20260520,14.85,15.4,14.6,14.95,831000,16,-6.57,16.42,15.83,0.79
20260521,15.15,15.7,15.15,15.55,701000,15.96,-2.6,16.32,15.84,0.74
20260522,15.75,15.9,15.55,15.9,16000,15.96,-0.37,16.26,15.84,0.02
20260525,16.05,16.25,15.8,15.8,16000,15.95,-0.91,16.2,15.85,0.02
20260526,15.8,15.9,15.45,15.6,16000,15.92,-1.99,16.14,15.84,0.02
20260527,15.6,15.65,15.2,15.25,15000,15.86,-3.85,16.07,15.83,0.02
20260528,15.35,15.9,15,15.1,15000,15.8,-4.42,15.98,15.82,0.02
20260529,15.15,16.6,15.1,16.6,16000,15.86,4.63,15.97,15.85,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 16.95
- over_600_ratio: 14.65
- over_800_ratio: 13.92
- over_1000_ratio: 13.43
- over_400_change_1w: 0.24
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,16.45,,13.92,,13.43,,0,False,False
20260508,16.78,0.33,13.92,0,13.43,0,1,False,False
20260515,17.31,0.53,14.4,0.48,13.43,0,2,False,True
20260522,16.71,-0.6,13.92,-0.48,13.43,0,0,False,False
20260529,16.95,0.24,13.92,0,13.43,0,1,False,False
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
