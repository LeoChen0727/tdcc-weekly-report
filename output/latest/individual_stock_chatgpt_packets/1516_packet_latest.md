# INDIVIDUAL STOCK CHATGPT PACKET - 1516 川飛

## Metadata
- generated_at: 2026-05-30 23:41:01 Asia/Taipei
- stock_id: 1516
- stock_name: 川飛
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1516_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1516_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1516_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1516_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1516_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1516_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1516_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1516_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1516_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1516_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1516_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1516_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1516_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1516.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1516.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1516.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1516.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1516.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1516.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1516_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1516_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1516_latest.md?ref=main

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
- open: 21.1
- high: 21.1
- low: 20.55
- close: 20.7
- volume: 64262
- ma5: 20.86
- ema23_primary: 21.11
- distance_to_ema23_pct: -1.94
- ma20: 21.39
- ma60: 21.42
- ma120: 21.48
- return_5d: -0.24
- return_20d: -3.5
- volume_ratio: 0.61
- distance_to_ma20_pct_auxiliary: -3.24
- distance_to_high_60_pct: -20.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,21.45,21.9,20.8,21.8,46011,20.76,5,20.39,21.57,0.87
20260505,21.5,21.8,21,21.8,90427,20.85,4.57,20.46,21.56,1.81
20260506,21.8,21.95,20.55,21.8,151128,20.93,4.17,20.55,21.55,2.69
20260507,21.8,22.25,21.7,21.85,185190,21,4.03,20.6,21.53,2.88
20260508,21.7,21.95,21.55,21.7,34320,21.06,3.03,20.67,21.52,0.53
20260511,21.1,21.9,20.7,21.75,97427,21.12,2.99,20.73,21.52,1.41
20260512,21,21.65,21,21.6,78148,21.16,2.08,20.81,21.52,1.12
20260513,21.6,21.65,21,21.6,153118,21.2,1.9,20.9,21.52,2.01
20260514,21.6,21.85,21.6,21.8,98067,21.25,2.6,20.99,21.52,1.23
20260515,21.8,21.9,21.8,21.9,110581,21.3,2.81,21.09,21.53,1.32
20260518,22.3,22.3,21,21.1,241915,21.28,-0.87,21.16,21.52,2.58
20260519,21.6,22,21.5,21.8,138322,21.33,2.22,21.22,21.52,1.46
20260520,22,22,21.3,21.3,4768,21.32,-0.12,21.25,21.5,0.05
20260521,22.25,22.25,20.95,21,101815,21.3,-1.4,21.28,21.5,1.06
20260522,21.5,21.5,20.6,20.75,18117,21.25,-2.36,21.31,21.5,0.2
20260525,20.8,21.7,20.8,21,111826,21.23,-1.09,21.34,21.5,1.17
20260526,21,21,20.75,21,149161,21.21,-1,21.39,21.5,1.48
20260527,21.3,21.35,20.6,20.6,36471,21.16,-2.65,21.41,21.47,0.36
20260528,20.6,21.05,20.6,21,194972,21.15,-0.7,21.43,21.45,1.86
20260529,21.1,21.1,20.55,20.7,64262,21.11,-1.94,21.39,21.42,0.61
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 64.03
- over_600_ratio: 61.82
- over_800_ratio: 58.04
- over_1000_ratio: 58.04
- over_400_change_1w: 0.95
- over_800_change_1w: 0.95
- over_1000_change_1w: 0.95
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.96,,53.74,,53.74,,0,False,False
20260508,62.45,1.49,53.74,0,53.74,0,1,False,False
20260515,63.19,0.74,56.07,2.33,53.71,-0.03,2,False,True
20260522,63.08,-0.11,57.09,1.02,57.09,3.38,3,False,True
20260529,64.03,0.95,58.04,0.95,58.04,0.95,4,True,True
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
