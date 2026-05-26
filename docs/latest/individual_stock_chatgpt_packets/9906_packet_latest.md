# INDIVIDUAL STOCK CHATGPT PACKET - 9906 欣巴巴

## Metadata
- generated_at: 2026-05-26 21:27:01 Asia/Taipei
- stock_id: 9906
- stock_name: 欣巴巴
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9906_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9906_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9906_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9906_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9906_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9906_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9906_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9906_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9906_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9906_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9906_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9906_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9906_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9906.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9906.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9906.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9906.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9906.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9906.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9906_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9906_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9906_latest.md?ref=main

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
- open: 33.5
- high: 33.7
- low: 32.85
- close: 33.15
- volume: 134243
- ma5: 33.9
- ema23_primary: 35.46
- distance_to_ema23_pct: -6.53
- ma20: 35.12
- ma60: 39.3
- ma120: 43.69
- return_5d: 3.76
- return_20d: -11.36
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: -5.61
- distance_to_high_60_pct: -26.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,37.5,38.3,37.05,38.3,205022,40.66,-5.81,40.76,42.42,1.62
20260429,38.3,38.5,37.85,38.3,57451,40.47,-5.36,40.63,42.28,0.51
20260430,38.15,38.65,37.85,38.25,94168,40.28,-5.04,40.53,42.15,0.9
20260504,38.25,38.25,37.55,37.55,100560,40.05,-6.25,40.33,42.01,0.96
20260505,37.8,37.8,37.2,37.5,107895,39.84,-5.88,40.15,41.87,1
20260506,37.6,37.8,37.45,37.6,92150,39.65,-5.18,39.97,41.73,0.83
20260507,37.75,37.9,37,37.1,230260,39.44,-5.94,39.7,41.59,1.96
20260508,37,37.5,36.2,36.2,122391,39.17,-7.59,39.45,41.45,1.02
20260511,36.5,36.5,35.85,36.2,169289,38.92,-7,39.17,41.32,1.38
20260512,35.5,36,34.3,34.3,381843,38.54,-11,38.81,41.16,2.71
20260513,34,34.15,32.4,32.65,254207,38.05,-14.19,38.36,40.96,1.68
20260514,32.4,33.3,31.1,32.95,302828,37.62,-12.42,37.87,40.76,1.89
20260515,32.95,32.95,31.85,31.9,302883,37.15,-14.12,37.36,40.52,1.76
20260518,31.5,32.15,30.8,32.15,314747,36.73,-12.47,36.89,40.3,1.72
20260519,32,32.25,31.3,31.95,244365,36.33,-12.06,36.48,40.09,1.28
20260520,31.6,33.5,31.6,33.15,320305,36.07,-8.09,36.1,39.9,1.59
20260521,33.15,35,32.8,35,295430,35.98,-2.72,35.86,39.74,1.43
20260522,34.95,35.05,33.2,34.5,389972,35.85,-3.78,35.6,39.58,1.78
20260525,34.15,34.65,33.55,33.7,185352,35.67,-5.54,35.33,39.43,0.83
20260526,33.5,33.7,32.85,33.15,134243,35.46,-6.53,35.12,39.3,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 77.99
- over_600_ratio: 74.94
- over_800_ratio: 73.44
- over_1000_ratio: 72.34
- over_400_change_1w: 0.08
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,77.36,,74.24,,71.31,,0,False,False
20260508,77.51,0.15,74.4,0.16,71.47,0.16,1,True,True
20260515,77.91,0.4,73.47,-0.93,72.37,0.9,2,False,True
20260522,77.99,0.08,73.44,-0.03,72.34,-0.03,3,False,False
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
