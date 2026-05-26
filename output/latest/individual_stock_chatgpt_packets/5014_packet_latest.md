# INDIVIDUAL STOCK CHATGPT PACKET - 5014 建錩

## Metadata
- generated_at: 2026-05-26 23:54:15 Asia/Taipei
- stock_id: 5014
- stock_name: 建錩
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5014_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5014_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5014_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5014_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5014_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5014_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5014_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5014_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5014_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5014_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5014_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5014_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5014_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5014.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5014.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5014.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5014.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5014.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5014.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5014_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5014_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5014_latest.md?ref=main

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
- open: 11.3
- high: 11.35
- low: 10.85
- close: 10.95
- volume: 11000
- ma5: 10.63
- ema23_primary: 10.28
- distance_to_ema23_pct: 6.54
- ma20: 10.09
- ma60: 10.32
- ma120: 10.51
- return_5d: 6.31
- return_20d: 10.49
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 8.51
- distance_to_high_60_pct: -4.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,9.87,9.92,9.8,9.86,682000,10.19,-3.23,10.15,10.71,2.37
20260429,10,10,9.79,9.84,323000,10.16,-3.15,10.12,10.69,1.12
20260430,9.84,10.05,9.8,9.81,223000,10.13,-3.17,10.09,10.66,0.79
20260504,9.79,9.79,9.54,9.56,650000,10.08,-5.19,10.05,10.63,2.1
20260505,9.56,9.56,9.44,9.46,344000,10.03,-5.7,10.01,10.59,1.07
20260506,9.47,9.47,9.31,9.42,429000,9.98,-5.62,9.97,10.56,1.28
20260507,9.42,9.46,9.32,9.44,372000,9.94,-4.99,9.93,10.52,1.08
20260508,9.46,9.61,9.4,9.43,410000,9.89,-4.69,9.89,10.48,1.24
20260511,10.1,10.35,10.1,10.35,1077000,9.93,4.21,9.9,10.46,3.04
20260512,10.5,10.55,10.15,10.25,994000,9.96,2.93,9.9,10.44,2.54
20260513,10.2,10.3,10.15,10.3,362000,9.99,3.14,9.91,10.42,0.91
20260514,10.4,10.5,10.2,10.2,237000,10,1.96,9.91,10.4,0.6
20260515,10.1,10.2,10.1,10.15,308000,10.02,1.33,9.91,10.37,0.76
20260518,10.15,10.35,10.15,10.3,198000,10.04,2.59,9.92,10.36,0.49
20260519,10.4,10.55,10.2,10.3,239000,10.06,2.37,9.93,10.35,0.59
20260520,10.2,10.3,10.2,10.2,170000,10.07,1.26,9.94,10.34,0.42
20260521,10.25,10.35,10.2,10.25,139000,10.09,1.61,9.95,10.32,0.35
20260522,10.25,10.5,10.25,10.45,10000,10.12,3.28,9.97,10.31,0.03
20260525,10.5,11.45,10.5,11.3,11000,10.22,10.6,10.04,10.32,0.03
20260526,11.3,11.35,10.85,10.95,11000,10.28,6.54,10.09,10.32,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 36.75
- over_600_ratio: 33.13
- over_800_ratio: 30.07
- over_1000_ratio: 26.12
- over_400_change_1w: 0.26
- over_800_change_1w: 0.04
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,36.9,,30.06,,26.69,,0,False,False
20260508,36.84,-0.06,30.07,0.01,26.69,0,1,False,True
20260515,36.49,-0.35,30.03,-0.04,26.12,-0.57,0,False,False
20260522,36.75,0.26,30.07,0.04,26.12,0,1,False,True
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
