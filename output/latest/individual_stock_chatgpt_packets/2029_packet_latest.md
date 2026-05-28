# INDIVIDUAL STOCK CHATGPT PACKET - 2029 盛餘

## Metadata
- generated_at: 2026-05-28 19:31:45 Asia/Taipei
- stock_id: 2029
- stock_name: 盛餘
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2029_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2029_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2029_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2029_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2029_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2029_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2029_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2029_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2029_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2029_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2029_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2029_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2029_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2029.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2029.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2029.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2029.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2029.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2029.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2029_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2029_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2029_latest.md?ref=main

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
- open: 20.45
- high: 20.5
- low: 20.1
- close: 20.3
- volume: 364856
- ma5: 20.47
- ema23_primary: 20.37
- distance_to_ema23_pct: -0.37
- ma20: 20.3
- ma60: 20.51
- ma120: 20.82
- return_5d: -0.73
- return_20d: 0.99
- volume_ratio: 1.3
- distance_to_ma20_pct_auxiliary: -0.01
- distance_to_high_60_pct: -7.52

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,20.1,20.25,20.05,20.2,110237,20.46,-1.27,20.47,20.89,0.63
20260504,20.1,20.5,19.9,20.05,293846,20.43,-1.84,20.44,20.88,1.65
20260505,20.1,20.3,20,20.3,168169,20.42,-0.57,20.44,20.87,0.92
20260506,20.4,20.4,20.1,20.25,119206,20.4,-0.74,20.43,20.85,0.64
20260507,20.1,20.25,19.95,20.15,363936,20.38,-1.13,20.41,20.83,1.85
20260508,20.25,20.25,20.05,20.1,176664,20.36,-1.26,20.39,20.81,0.88
20260511,20.25,20.7,20.25,20.5,400037,20.37,0.64,20.39,20.79,1.88
20260512,20.75,20.75,20.25,20.25,336345,20.36,-0.54,20.37,20.77,1.52
20260513,20.25,20.4,20.2,20.35,119780,20.36,-0.04,20.35,20.75,0.55
20260514,20.25,20.3,20.1,20.15,227292,20.34,-0.94,20.32,20.73,1.01
20260515,20.35,20.35,20,20.15,214216,20.33,-0.86,20.3,20.7,0.94
20260518,20.05,20.1,20,20,194859,20.3,-1.47,20.27,20.68,0.87
20260519,20,20.5,20,20.45,372310,20.31,0.69,20.26,20.66,1.62
20260520,20.2,20.35,20.05,20.35,236054,20.31,0.18,20.24,20.64,1.02
20260521,20.35,20.45,20.2,20.45,120518,20.33,0.61,20.23,20.62,0.53
20260522,20.35,20.4,20.15,20.3,256380,20.32,-0.11,20.23,20.6,1.16
20260525,20.3,20.9,20.25,20.7,665384,20.35,1.7,20.25,20.58,2.69
20260526,20.95,21.25,20.6,20.6,589605,20.38,1.1,20.28,20.56,2.25
20260527,20.55,20.6,20.4,20.45,293343,20.38,0.34,20.29,20.54,1.09
20260528,20.45,20.5,20.1,20.3,364856,20.37,-0.37,20.3,20.51,1.3
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.01
- over_600_ratio: 69.69
- over_800_ratio: 68.79
- over_1000_ratio: 68.25
- over_400_change_1w: -0.08
- over_800_change_1w: -0.28
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.95,,69.05,,68.23,,0,False,False
20260508,70.95,0,69.05,0,68.23,0,0,False,False
20260515,71.09,0.14,69.07,0.02,68.25,0.02,1,False,True
20260522,71.01,-0.08,68.79,-0.28,68.25,0,0,False,False
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
