# INDIVIDUAL STOCK CHATGPT PACKET - 4728 雙美

## Metadata
- generated_at: 2026-05-28 19:32:46 Asia/Taipei
- stock_id: 4728
- stock_name: 雙美
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 127
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4728_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4728_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4728_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4728_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4728_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4728_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4728_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4728_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4728_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4728_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4728_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4728_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4728_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4728.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4728.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4728.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4728.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4728.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4728.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4728_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4728_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4728_latest.md?ref=main

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
- open: 378
- high: 380.5
- low: 378
- close: 380
- volume: 5475
- ma5: 381.7
- ema23_primary: 384.81
- distance_to_ema23_pct: -1.25
- ma20: 384.6
- ma60: 388.88
- ma120: 390.89
- return_5d: -1.17
- return_20d: -3.06
- volume_ratio: 0.07
- distance_to_ma20_pct_auxiliary: -1.2
- distance_to_high_60_pct: -7.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260423,390.5,394,387,394,44000,392.44,0.4,391.43,391.07,3.12
20260424,389,394.5,389,389.5,39000,392.19,-0.69,391.4,391.02,2.45
20260427,385,395,382,395,19000,392.43,0.66,391.73,390.99,1.15
20260428,388.5,389,388,388.5,8000,392.1,-0.92,391.7,390.89,0.49
20260429,387.5,387.5,387.5,387.5,1000,391.72,-1.08,391.38,390.81,0.06
20260504,387.5,387.5,382.5,384.5,64000,391.11,-1.69,391.43,390.7,3.52
20260505,383,384,383,383.5,7000,390.48,-1.79,391.25,390.59,0.38
20260506,383.5,383.5,383.5,383.5,2000,389.9,-1.64,391.2,390.48,0.11
20260507,383,384,383,383.5,8000,389.37,-1.51,391.2,390.38,0.43
20260508,353.5,383,350,382,74000,388.75,-1.74,391.12,390.24,3.36
20260511,382,382,380,381,6000,388.11,-1.83,390.85,390.08,0.27
20260512,380.5,381,380,381,8000,387.51,-1.68,390.68,389.89,0.36
20260513,380,381,380,381,6000,386.97,-1.54,389.52,389.73,0.27
20260515,384.5,384.5,384.5,384.5,5000,386.76,-0.59,388.6,389.68,0.22
20260520,385,387,384,384.5,26000,386.58,-0.54,387.82,389.6,1.13
20260521,381.5,382,370.5,382,35000,386.19,-1.09,386.93,389.49,1.46
20260522,382,383,382,383,382000,385.93,-0.76,386.2,389.39,9.01
20260525,383.5,383.5,383.5,383.5,383000,385.73,-0.58,385.7,389.25,6.3
20260527,380,380,380,380,380000,385.25,-1.36,385.2,389.07,4.87
20260528,378,380.5,378,380,5475,384.81,-1.25,384.6,388.88,0.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.46
- over_600_ratio: 73.25
- over_800_ratio: 69.28
- over_1000_ratio: 64.08
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.2,,69.05,,63.87,,0,False,False
20260508,84.28,0.08,69.1,0.05,63.92,0.05,1,True,True
20260515,84.47,0.19,69.29,0.19,64.08,0.16,2,True,True
20260522,84.46,-0.01,69.28,-0.01,64.08,0,0,False,False
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
