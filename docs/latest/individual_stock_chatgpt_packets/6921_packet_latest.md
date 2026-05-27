# INDIVIDUAL STOCK CHATGPT PACKET - 6921 嘉雨思-創

## Metadata
- generated_at: 2026-05-27 21:28:18 Asia/Taipei
- stock_id: 6921
- stock_name: 嘉雨思-創
- packet_status: standard_rawdata_packet
- latest_price_date: 20260527
- price_rows: 99
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6921_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6921_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6921_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6921_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6921_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6921_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6921_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6921_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6921_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6921_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6921_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6921_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6921_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6921.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6921.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6921.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6921.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6921.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6921.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6921_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6921_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6921_latest.md?ref=main

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
- open: 77
- high: 78.1
- low: 75
- close: 76.1
- volume: 84323
- ma5: 77.1
- ema23_primary: 80.89
- distance_to_ema23_pct: -5.93
- ma20: 82.98
- ma60: 79.27
- ma120: 76.4
- return_5d: 0.26
- return_20d: -21.47
- volume_ratio: 1.49
- distance_to_ma20_pct_auxiliary: -8.3
- distance_to_high_60_pct: -27.18

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,92.4,95.5,92.1,93.2,67125,84.93,9.74,82.61,78.01,0.64
20260430,93.3,93.3,91.1,91.5,49590,85.47,7.05,83.88,78.4,0.48
20260504,92.1,94.8,91.5,93,53706,86.1,8.01,84.98,78.82,0.52
20260505,92.1,92.2,90.7,91.1,30577,86.52,5.3,86.03,79.09,0.29
20260506,91.1,93.2,90,91.5,91290,86.93,5.25,87.14,79.28,0.84
20260507,92.9,95.5,91.3,92.6,80701,87.41,5.94,88.16,79.5,0.75
20260508,93.5,93.5,90.5,90.9,32655,87.7,3.65,89.04,79.7,0.3
20260511,89.5,89.5,82,82.4,162002,87.25,-5.56,89.55,79.81,1.44
20260512,81.9,83.5,80.4,83,38424,86.9,-4.49,90.01,80.03,0.35
20260513,81.8,81.8,79.8,81,58907,86.41,-6.26,90.36,80.09,0.53
20260514,80,80,77.2,79.2,66793,85.81,-7.7,90.51,80.01,0.6
20260515,79.8,79.8,75.9,76,68870,84.99,-10.58,90.33,79.83,0.64
20260518,74.7,77.5,74.7,77,55335,84.32,-8.69,89.86,79.7,0.53
20260519,77.6,78.3,75.6,75.9,35518,83.62,-9.24,88.92,79.61,0.37
20260520,75.9,75.9,75.9,75.9,2651,82.98,-8.53,87.52,79.58,0.03
20260521,76.3,76.5,76,76.2,20490,82.41,-7.54,86.35,79.45,0.3
20260522,75.5,79.2,75.5,78.2,38371,82.06,-4.71,85.56,79.44,0.66
20260525,79.8,79.9,77,78,50080,81.72,-4.56,84.75,79.4,0.89
20260526,78.9,78.9,75.2,77,44097,81.33,-5.32,84.03,79.35,0.8
20260527,77,78.1,75,76.1,84323,80.89,-5.93,82.98,79.27,1.49
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.28
- over_600_ratio: 76.18
- over_800_ratio: 76.18
- over_1000_ratio: 76.18
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.28,,76.18,,76.18,,0,False,False
20260508,80.28,0,76.18,0,76.18,0,0,False,False
20260515,80.28,0,76.18,0,76.18,0,0,False,False
20260522,80.28,0,76.18,0,76.18,0,0,False,False
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
