# INDIVIDUAL STOCK CHATGPT PACKET - 8048 德勝

## Metadata
- generated_at: 2026-05-26 23:55:04 Asia/Taipei
- stock_id: 8048
- stock_name: 德勝
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8048_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8048_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8048_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8048_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8048_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8048_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8048_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8048_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8048_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8048_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8048_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8048_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8048_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8048.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8048.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8048.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8048.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8048.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8048.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8048_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8048_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8048_latest.md?ref=main

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
- open: 64.9
- high: 65.2
- low: 62.2
- close: 62.8
- volume: 63000
- ma5: 62.32
- ema23_primary: 62.15
- distance_to_ema23_pct: 1.04
- ma20: 62.12
- ma60: 61.03
- ma120: 59.07
- return_5d: 3.63
- return_20d: 1.62
- volume_ratio: 0.18
- distance_to_ma20_pct_auxiliary: 1.09
- distance_to_high_60_pct: -18.23

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,61.3,63.3,61.3,61.8,359000,61.82,-0.04,60.15,58.7,0.32
20260429,61.8,63.2,61,62.2,325000,61.86,0.56,60.56,58.79,0.29
20260430,62,62.9,61.3,61.5,305000,61.83,-0.53,61.01,58.87,0.27
20260504,62.5,63.3,61.7,62.4,289000,61.87,0.85,61.5,58.99,0.26
20260505,62.1,64.1,62.1,62.4,384000,61.92,0.78,62.02,59.14,0.34
20260506,63.8,63.8,61,61.2,431000,61.86,-1.06,62.45,59.27,0.38
20260507,61.3,63,60.3,62.6,343000,61.92,1.1,62.83,59.43,0.3
20260508,62.2,63.3,60.5,62,375000,61.93,0.12,63.2,59.58,0.33
20260511,64.3,64.5,61,61.8,542000,61.92,-0.19,63.48,59.73,0.48
20260512,63.3,64.7,62.1,63.4,695000,62.04,2.19,63.77,59.9,0.61
20260513,62.5,62.7,61.4,61.6,360000,62,-0.65,63.91,60.02,0.32
20260514,62.4,62.5,61.1,62.1,317000,62.01,0.14,63.93,60.16,0.29
20260515,62.1,65.2,61.6,61.8,531000,61.99,-0.31,63.9,60.28,0.49
20260518,61,64.3,60.1,63.5,393000,62.12,2.22,63.84,60.43,0.37
20260519,63.5,63.9,60.4,60.6,425000,61.99,-2.25,63.33,60.52,0.44
20260520,60.6,62.5,60.6,60.7,340000,61.88,-1.91,62.69,60.61,0.55
20260521,61,62,61,61,230000,61.81,-1.31,62.28,60.7,0.45
20260522,61.5,63.4,60.8,62.7,62000,61.89,1.32,62.07,60.8,0.15
20260525,63.6,64.9,63.2,64.4,64000,62.09,3.71,62.08,60.93,0.17
20260526,64.9,65.2,62.2,62.8,63000,62.15,1.04,62.12,61.03,0.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.54
- over_600_ratio: 33.68
- over_800_ratio: 32.63
- over_1000_ratio: 28.03
- over_400_change_1w: -0.13
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.34,,32.65,,28.18,,0,False,False
20260508,40.32,-0.02,32.66,0.01,28.17,-0.01,1,False,True
20260515,39.67,-0.65,32.68,0.02,28.12,-0.05,2,False,True
20260522,39.54,-0.13,32.63,-0.05,28.03,-0.09,0,False,False
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
