# INDIVIDUAL STOCK CHATGPT PACKET - 1321 大洋

## Metadata
- generated_at: 2026-05-26 21:24:34 Asia/Taipei
- stock_id: 1321
- stock_name: 大洋
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1321_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1321_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1321_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1321_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1321_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1321_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1321_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1321_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1321_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1321_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1321_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1321_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1321_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1321.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1321.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1321.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1321.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1321.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1321.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1321_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1321_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1321_latest.md?ref=main

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
- open: 29
- high: 29.3
- low: 28.6
- close: 29
- volume: 290276
- ma5: 29.28
- ema23_primary: 30.05
- distance_to_ema23_pct: -3.49
- ma20: 29.66
- ma60: 32.04
- ma120: 33.31
- return_5d: -1.53
- return_20d: -5.38
- volume_ratio: 1.29
- distance_to_ma20_pct_auxiliary: -2.24
- distance_to_high_60_pct: -16.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,31,31.2,30.65,30.8,175302,32.56,-5.4,32.78,33.22,0.77
20260429,30.8,31.15,30.65,30.85,168401,32.42,-4.83,32.63,33.18,0.74
20260430,30.85,30.85,30.35,30.4,225941,32.25,-5.73,32.48,33.13,0.97
20260504,30.4,30.45,30.15,30.4,203388,32.09,-5.28,32.32,33.08,0.86
20260505,30.25,30.25,29.8,29.85,419803,31.91,-6.45,32.13,33.01,1.64
20260506,29.8,29.8,29.15,29.25,657132,31.69,-7.69,31.92,32.94,2.3
20260507,29.3,29.55,29.25,29.5,178531,31.5,-6.36,31.71,32.87,0.64
20260508,29.75,29.75,29.25,29.55,180399,31.34,-5.72,31.52,32.81,0.64
20260511,29.55,29.7,29.4,29.6,131043,31.2,-5.12,31.34,32.75,0.47
20260512,29.6,29.65,29.15,29.45,220357,31.05,-5.16,31.16,32.69,0.79
20260513,29.3,29.55,29.15,29.45,131902,30.92,-4.75,30.98,32.63,0.49
20260514,29.25,29.95,29.25,29.5,146100,30.8,-4.22,30.8,32.56,0.54
20260515,29.5,29.65,29.15,29.35,151780,30.68,-4.33,30.61,32.49,0.56
20260518,29.6,29.6,29.2,29.5,115230,30.58,-3.53,30.45,32.43,0.43
20260519,29.3,29.6,29.3,29.45,161759,30.49,-3.4,30.29,32.38,0.61
20260520,29.45,29.75,29.35,29.6,203208,30.41,-2.67,30.14,32.32,0.76
20260521,29.55,29.7,29.45,29.6,96877,30.34,-2.45,30,32.26,0.39
20260522,29.5,29.65,29.1,29.35,303163,30.26,-3.01,29.88,32.19,1.31
20260525,29.2,29.4,28.65,28.85,345556,30.14,-4.29,29.75,32.11,1.47
20260526,29,29.3,28.6,29,290276,30.05,-3.49,29.66,32.04,1.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.63
- over_600_ratio: 62.83
- over_800_ratio: 59.48
- over_1000_ratio: 53.5
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
20260430,69.33,,59.32,,53.34,,0,False,False
20260508,69.38,0.05,59.47,0.15,53.49,0.15,1,False,True
20260515,69.62,0.24,59.48,0.01,53.5,0.01,2,True,True
20260522,69.63,0.01,59.48,0,53.5,0,3,False,False
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
