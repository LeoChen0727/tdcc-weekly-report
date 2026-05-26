# INDIVIDUAL STOCK CHATGPT PACKET - 5522 遠雄

## Metadata
- generated_at: 2026-05-26 21:26:07 Asia/Taipei
- stock_id: 5522
- stock_name: 遠雄
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5522_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5522_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5522_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5522_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5522_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5522_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5522.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5522.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5522.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5522.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5522.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5522.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5522_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5522_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5522_latest.md?ref=main

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
- open: 69.3
- high: 71.2
- low: 69.2
- close: 71.1
- volume: 924632
- ma5: 70.2
- ema23_primary: 70.28
- distance_to_ema23_pct: 1.17
- ma20: 70.09
- ma60: 69.76
- ma120: 68.71
- return_5d: 0.42
- return_20d: 2.89
- volume_ratio: 1.05
- distance_to_ma20_pct_auxiliary: 1.44
- distance_to_high_60_pct: -4.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,69.8,69.8,68.1,68.4,715605,70.05,-2.36,70.86,68.71,0.7
20260429,69.1,69.8,68.2,69.2,589231,69.98,-1.12,70.81,68.73,0.58
20260430,69.4,69.5,68.1,68.8,1165825,69.88,-1.55,70.73,68.75,1.14
20260504,69,69.7,68.2,69.4,576177,69.84,-0.64,70.57,68.78,0.58
20260505,69.4,69.4,68.7,69.1,385960,69.78,-0.98,70.39,68.82,0.4
20260506,69.5,69.5,68.8,69.1,634649,69.72,-0.9,70.21,68.88,0.67
20260507,68.6,70,68.1,69.7,1112313,69.72,-0.03,70.02,68.94,1.17
20260508,70,70.4,69.5,70,1202130,69.75,0.36,69.83,68.97,1.24
20260511,70.2,72.7,70.2,72.7,1618880,69.99,3.87,69.8,69.08,1.61
20260512,72.8,72.8,69.1,69.8,1522084,69.98,-0.25,69.72,69.13,1.48
20260513,69.8,70.5,69.8,70.4,520439,70.01,0.55,69.69,69.19,0.55
20260514,70.2,71,69.8,70.5,603594,70.05,0.64,69.7,69.26,0.64
20260515,70.7,70.8,69.7,70.7,909830,70.11,0.85,69.72,69.33,0.96
20260518,70.8,72.3,70.2,72.2,1442257,70.28,2.73,69.84,69.44,1.47
20260519,72.2,72.2,70.8,70.8,753019,70.32,0.68,69.92,69.54,0.8
20260520,70.8,71.3,70.3,70.8,571777,70.36,0.62,69.97,69.6,0.64
20260521,71.5,71.5,70.1,70.4,472269,70.37,0.05,69.97,69.64,0.54
20260522,70.3,70.3,69.5,69.5,931098,70.29,-1.13,70,69.67,1.09
20260525,69.9,70.6,68.7,69.2,883165,70.2,-1.43,69.99,69.7,1.02
20260526,69.3,71.2,69.2,71.1,924632,70.28,1.17,70.09,69.76,1.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 89.06
- over_600_ratio: 88.2
- over_800_ratio: 87.39
- over_1000_ratio: 86.72
- over_400_change_1w: 0.04
- over_800_change_1w: -0.02
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.9,,87.68,,86.8,,0,False,False
20260508,89.02,0.12,87.65,-0.03,86.89,0.09,1,False,True
20260515,89.02,0,87.41,-0.24,86.65,-0.24,0,False,False
20260522,89.06,0.04,87.39,-0.02,86.72,0.07,1,False,True
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
