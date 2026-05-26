# INDIVIDUAL STOCK CHATGPT PACKET - 8416 實威

## Metadata
- generated_at: 2026-05-26 23:55:11 Asia/Taipei
- stock_id: 8416
- stock_name: 實威
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 131
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8416_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8416_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8416_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8416_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8416_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8416.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8416.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8416.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8416.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8416_latest.md?ref=main

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
- open: 172
- high: 172.5
- low: 170
- close: 172.5
- volume: 171000
- ma5: 172.9
- ema23_primary: 172.37
- distance_to_ema23_pct: 0.07
- ma20: 172.35
- ma60: 170.59
- ma120: 174.62
- return_5d: 0.58
- return_20d: 0
- volume_ratio: 5.06
- distance_to_ma20_pct_auxiliary: 0.09
- distance_to_high_60_pct: -3.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,171.5,172.5,170,172.5,15000,171.19,0.77,170.53,172.91,1.51
20260429,170.5,172,168,169,28000,171.01,-1.17,170.47,172.71,2.51
20260430,169,169,168.5,169,5000,170.84,-1.08,170.57,172.52,0.44
20260504,170.5,170.5,169,169.5,14000,170.73,-0.72,170.62,172.34,1.18
20260505,170.5,172.5,170.5,171.5,12000,170.79,0.41,170.8,172.15,0.97
20260506,171.5,172.5,171.5,172.5,4000,170.93,0.92,170.97,171.99,0.32
20260507,174,174,171,171.5,9000,170.98,0.3,171.05,171.78,0.7
20260508,172,172.5,171.5,172.5,8000,171.11,0.81,171.18,171.57,0.61
20260511,174,178.5,174,175,22000,171.43,2.08,171.45,171.42,1.58
20260512,175.5,175.5,175,175,4000,171.73,1.9,171.75,171.32,0.29
20260513,174,174,173,173.5,6000,171.88,0.94,171.9,171.25,0.43
20260514,174.5,174.5,173.5,173.5,2000,172.01,0.86,172.07,171.14,0.15
20260515,173.5,174,173.5,173.5,7000,172.14,0.79,172.3,171.07,0.56
20260518,173,173,172,172.5,8000,172.17,0.19,172.45,170.95,0.64
20260519,172,172,171,171.5,7000,172.11,-0.35,172.43,170.85,0.59
20260520,171,173,171,173,2000,172.19,0.47,172.45,170.8,0.18
20260521,173.5,174,172,174,8000,172.34,0.97,172.4,170.75,0.79
20260522,175,175,170.5,173,172000,172.39,0.35,172.43,170.69,9.45
20260525,173,173,172,172,172000,172.36,-0.21,172.35,170.6,6.52
20260526,172,172.5,170,172.5,171000,172.37,0.07,172.35,170.59,5.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 77.08
- over_600_ratio: 77.08
- over_800_ratio: 77.08
- over_1000_ratio: 77.08
- over_400_change_1w: 0.01
- over_800_change_1w: 0.01
- over_1000_change_1w: 3.54
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,77.04,,77.04,,73.54,,0,False,False
20260508,77.05,0.01,77.05,0.01,73.54,0,1,False,True
20260515,77.07,0.02,77.07,0.02,73.54,0,2,False,True
20260522,77.08,0.01,77.08,0.01,77.08,3.54,3,True,True
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
