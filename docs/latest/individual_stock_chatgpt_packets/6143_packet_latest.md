# INDIVIDUAL STOCK CHATGPT PACKET - 6143 振曜

## Metadata
- generated_at: 2026-05-27 21:27:49 Asia/Taipei
- stock_id: 6143
- stock_name: 振曜
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6143_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6143_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6143_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6143_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6143_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6143_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6143_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6143_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6143_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6143_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6143_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6143_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6143_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6143.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6143.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6143.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6143.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6143.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6143.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6143_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6143_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6143_latest.md?ref=main

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
- open: 99.7
- high: 101
- low: 98.3
- close: 100
- volume: 100000
- ma5: 98.62
- ema23_primary: 96.02
- distance_to_ema23_pct: 4.14
- ma20: 95.02
- ma60: 96.42
- ma120: 106.49
- return_5d: 5.04
- return_20d: 13.77
- volume_ratio: 0.08
- distance_to_ma20_pct_auxiliary: 5.25
- distance_to_high_60_pct: -9.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,88,88.5,86.8,87.1,433000,93.31,-6.65,93.01,99.8,0.44
20260430,87.1,88.4,86.6,87.1,441000,92.79,-6.13,92.61,99.39,0.46
20260504,87.3,89.6,87.3,89,492000,92.47,-3.76,92.26,99.03,0.52
20260505,89.8,91.2,89.1,91.2,671000,92.37,-1.26,92.06,98.7,0.71
20260506,91.4,91.4,89.2,90.6,618000,92.22,-1.76,91.81,98.38,0.65
20260507,91.8,94.1,90.9,93.3,994000,92.31,1.07,91.47,98.1,1.05
20260508,94,95.1,91.6,92,956000,92.28,-0.31,91.08,97.81,1.05
20260511,94.2,97.8,92.4,97.6,4108000,92.73,5.25,91.36,97.65,3.97
20260512,97.6,101.5,96.5,99.7,4304000,93.31,6.85,91.81,97.57,3.55
20260513,99.7,104.5,98.8,101.5,3854000,93.99,7.99,92.33,97.53,2.84
20260514,102,102,98.8,98.8,2756000,94.39,4.67,92.64,97.42,1.9
20260515,98.6,98.8,95.1,95.1,1811000,94.45,0.69,92.66,97.28,1.22
20260518,95.1,96.2,94,95,884000,94.5,0.53,92.75,97.17,0.6
20260519,95,96.3,94,94,620000,94.46,-0.48,92.83,97.03,0.42
20260520,94,95.7,93.4,95.2,518000,94.52,0.72,92.98,96.89,0.35
20260521,95.6,96.5,95.3,96.1,546000,94.65,1.53,93,96.75,0.38
20260522,96.3,98.4,95.8,98.1,97000,94.94,3.33,93.31,96.68,0.07
20260525,97.8,99.8,97.5,99.3,99000,95.3,4.2,93.81,96.64,0.08
20260526,100,101,97.8,99.6,99000,95.66,4.12,94.41,96.53,0.08
20260527,99.7,101,98.3,100,100000,96.02,4.14,95.02,96.42,0.08
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 33.1
- over_600_ratio: 27.89
- over_800_ratio: 23.16
- over_1000_ratio: 18.87
- over_400_change_1w: 0.04
- over_800_change_1w: 0.85
- over_1000_change_1w: -0.13
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,36.23,,25.05,,20.77,,0,False,False
20260508,36.24,0.01,25.06,0.01,20.63,-0.14,1,False,True
20260515,33.06,-3.18,22.31,-2.75,19,-1.63,0,False,False
20260522,33.1,0.04,23.16,0.85,18.87,-0.13,1,False,True
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
