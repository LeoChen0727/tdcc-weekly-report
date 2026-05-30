# INDIVIDUAL STOCK CHATGPT PACKET - 1464 得力

## Metadata
- generated_at: 2026-05-30 23:40:59 Asia/Taipei
- stock_id: 1464
- stock_name: 得力
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1464_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1464_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1464_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1464_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1464_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1464.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1464.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1464.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1464.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1464_latest.md?ref=main

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
- open: 10.1
- high: 10.2
- low: 10.05
- close: 10.2
- volume: 438997
- ma5: 10.11
- ema23_primary: 10.14
- distance_to_ema23_pct: 0.6
- ma20: 10.08
- ma60: 10.34
- ma120: 10.81
- return_5d: 0.99
- return_20d: 2
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: 1.19
- distance_to_high_60_pct: -10.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,10,10,9.92,9.94,1037850,10.28,-3.33,10.28,10.69,2.18
20260505,9.94,9.94,9.89,9.91,608672,10.25,-3.33,10.26,10.66,1.22
20260506,9.91,9.97,9.89,9.91,751955,10.22,-3.06,10.24,10.63,1.44
20260507,9.95,10.1,9.94,10.05,412898,10.21,-1.55,10.22,10.6,0.79
20260508,10.1,10.1,9.99,10,430720,10.19,-1.88,10.21,10.58,0.87
20260511,10,10.1,9.99,10.05,471925,10.18,-1.27,10.19,10.56,0.95
20260512,10.15,10.4,10.15,10.35,558882,10.19,1.53,10.19,10.55,1.1
20260513,10.4,10.4,10.1,10.15,702183,10.19,-0.39,10.17,10.53,1.38
20260514,10.15,10.2,9.99,10.15,802890,10.19,-0.36,10.16,10.51,1.49
20260515,10.15,10.15,10,10,421042,10.17,-1.68,10.14,10.49,0.78
20260518,10,10.15,10,10.05,712396,10.16,-1.09,10.11,10.48,1.29
20260519,10.05,10.2,10,10,319290,10.15,-1.45,10.09,10.46,0.58
20260520,10.1,10.15,10,10.15,416086,10.15,0.02,10.08,10.44,0.76
20260521,10.15,10.25,10.1,10.25,465439,10.16,0.92,10.08,10.43,0.84
20260522,10.25,10.25,10.05,10.1,445398,10.15,-0.51,10.07,10.41,0.83
20260525,10.1,10.1,10,10.05,918553,10.14,-0.92,10.06,10.39,1.63
20260526,10.05,10.2,10.05,10.1,302432,10.14,-0.39,10.07,10.38,0.56
20260527,10.15,10.15,10,10.1,619267,10.14,-0.36,10.07,10.36,1.12
20260528,10.1,10.1,10,10.1,723102,10.13,-0.33,10.07,10.35,1.26
20260529,10.1,10.2,10.05,10.2,438997,10.14,0.6,10.08,10.34,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 60.71
- over_600_ratio: 58
- over_800_ratio: 55.56
- over_1000_ratio: 53.84
- over_400_change_1w: 0.29
- over_800_change_1w: 0.4
- over_1000_change_1w: 0.39
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.55,,54.68,,52.79,,0,False,False
20260508,60.05,0.5,54.91,0.23,53,0.21,1,True,True
20260515,60.28,0.23,55.2,0.29,53.1,0.1,2,True,True
20260522,60.42,0.14,55.16,-0.04,53.45,0.35,3,False,True
20260529,60.71,0.29,55.56,0.4,53.84,0.39,4,True,True
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
