# INDIVIDUAL STOCK CHATGPT PACKET - 1539 巨庭

## Metadata
- generated_at: 2026-05-27 21:26:14 Asia/Taipei
- stock_id: 1539
- stock_name: 巨庭
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1539_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1539_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1539_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1539_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1539_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1539_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1539_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1539_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1539_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1539_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1539_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1539_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1539_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1539.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1539.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1539.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1539.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1539.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1539.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1539_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1539_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1539_latest.md?ref=main

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
- date: 20260527
- open: 16.05
- high: 16.05
- low: 15.7
- close: 15.8
- volume: 74440
- ma5: 15.79
- ema23_primary: 15.85
- distance_to_ema23_pct: -0.33
- ma20: 15.75
- ma60: 16.37
- ma120: 17.1
- return_5d: 1.94
- return_20d: -2.47
- volume_ratio: 0.79
- distance_to_ma20_pct_auxiliary: 0.33
- distance_to_high_60_pct: -12.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,16.35,16.35,16.15,16.2,45390,16.46,-1.59,16.34,17.27,0.47
20260430,16.2,16.2,16.05,16.15,31308,16.44,-1.74,16.34,17.2,0.34
20260504,16.15,16.15,16.05,16.05,59500,16.4,-2.16,16.32,17.14,0.64
20260505,16.2,16.2,15.9,15.95,82890,16.37,-2.54,16.31,17.07,0.89
20260506,16,16,15.7,15.8,186464,16.32,-3.18,16.28,17.01,1.88
20260507,15.95,16,15.65,15.8,98603,16.28,-2.92,16.24,16.96,0.98
20260508,15.9,15.95,15.55,15.75,111278,16.23,-2.97,16.21,16.91,1.07
20260511,15.55,15.9,15.55,15.7,114047,16.19,-3.01,16.18,16.86,1.07
20260512,15.7,15.7,15.55,15.65,72258,16.14,-3.05,16.15,16.82,0.87
20260513,15.8,15.8,15.55,15.6,34718,16.1,-3.09,16.11,16.79,0.42
20260514,15.7,15.9,15.55,15.55,145305,16.05,-3.13,16.07,16.74,1.69
20260515,15.85,15.85,15.55,15.55,110002,16.01,-2.87,16.02,16.69,1.29
20260518,15.6,15.6,15.05,15.35,107246,15.96,-3.79,15.97,16.65,1.22
20260519,15.35,15.4,15.2,15.4,49010,15.91,-3.2,15.92,16.61,0.56
20260520,15.5,15.6,15.4,15.5,20138,15.87,-2.36,15.87,16.57,0.23
20260521,15.5,15.55,15.45,15.5,48070,15.84,-2.17,15.82,16.53,0.56
20260522,15.45,15.5,15.25,15.45,89822,15.81,-2.28,15.78,16.48,1.12
20260525,15.5,16.7,15.5,16.2,304757,15.84,2.25,15.77,16.44,3.28
20260526,16.2,16.3,15.9,16,90706,15.86,0.91,15.77,16.41,0.97
20260527,16.05,16.05,15.7,15.8,74440,15.85,-0.33,15.75,16.37,0.79
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.22
- over_600_ratio: 59.6
- over_800_ratio: 58.44
- over_1000_ratio: 58.44
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.08,,58.44,,58.44,,0,False,False
20260508,60.13,0.05,58.44,0,58.44,0,1,False,False
20260515,60.21,0.08,58.44,0,58.44,0,2,False,False
20260522,60.22,0.01,58.44,0,58.44,0,3,False,False
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
