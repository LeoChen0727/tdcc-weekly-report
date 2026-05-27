# INDIVIDUAL STOCK CHATGPT PACKET - 1611 中電

## Metadata
- generated_at: 2026-05-27 21:26:16 Asia/Taipei
- stock_id: 1611
- stock_name: 中電
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1611_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1611_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1611_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1611_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1611_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1611_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1611_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1611_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1611_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1611_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1611_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1611_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1611_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1611.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1611.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1611.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1611.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1611.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1611.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1611_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1611_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1611_latest.md?ref=main

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
- open: 11.45
- high: 11.65
- low: 11.4
- close: 11.5
- volume: 912648
- ma5: 11.41
- ema23_primary: 11.6
- distance_to_ema23_pct: -0.84
- ma20: 11.54
- ma60: 12.26
- ma120: 12.64
- return_5d: 3.14
- return_20d: -4.17
- volume_ratio: 1.62
- distance_to_ma20_pct_auxiliary: -0.33
- distance_to_high_60_pct: -16.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,11.95,12.1,11.85,11.85,253764,12.27,-3.4,12.16,12.84,0.47
20260430,11.85,12,11.85,11.95,421895,12.24,-2.37,12.16,12.81,0.81
20260504,11.9,11.9,11.75,11.85,468457,12.21,-2.93,12.13,12.77,0.89
20260505,11.8,11.9,11.8,11.8,364640,12.17,-3.07,12.12,12.73,0.69
20260506,11.8,11.9,11.75,11.8,436889,12.14,-2.82,12.1,12.7,0.81
20260507,11.8,11.9,11.7,11.9,712598,12.12,-1.84,12.07,12.67,1.28
20260508,11.9,12.1,11.85,11.9,607072,12.1,-1.69,12.05,12.65,1.07
20260511,11.9,11.9,11.75,11.8,526548,12.08,-2.31,12.04,12.63,0.93
20260512,11.8,11.8,11.6,11.65,874079,12.04,-3.26,12,12.61,1.51
20260513,11.6,11.6,11.4,11.45,615887,11.99,-4.53,11.96,12.58,1.05
20260514,11.45,11.5,11.2,11.2,798037,11.93,-6.1,11.9,12.55,1.34
20260515,11.2,11.3,11,11,579058,11.85,-7.17,11.83,12.51,0.96
20260518,11,11.4,11,11.2,788675,11.8,-5.05,11.78,12.47,1.3
20260519,11.25,11.3,11.1,11.2,352282,11.75,-4.65,11.74,12.44,0.61
20260520,11.2,11.3,11.1,11.15,302318,11.7,-4.67,11.69,12.41,0.54
20260521,11.2,11.4,11.2,11.3,526983,11.66,-3.12,11.64,12.38,0.93
20260522,11.45,11.5,11.3,11.5,464642,11.65,-1.29,11.62,12.35,0.86
20260525,11.5,11.6,11.3,11.4,779470,11.63,-1.97,11.59,12.32,1.39
20260526,11.4,11.45,11.3,11.35,476645,11.61,-2.2,11.56,12.29,0.87
20260527,11.45,11.65,11.4,11.5,912648,11.6,-0.84,11.54,12.26,1.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 53.43
- over_600_ratio: 50.07
- over_800_ratio: 48.29
- over_1000_ratio: 45.1
- over_400_change_1w: -0.03
- over_800_change_1w: -0.27
- over_1000_change_1w: -0.59
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.82,,48.42,,45.82,,0,False,False
20260508,53.59,-0.23,48.33,-0.09,45.73,-0.09,0,False,False
20260515,53.46,-0.13,48.56,0.23,45.69,-0.04,1,False,True
20260522,53.43,-0.03,48.29,-0.27,45.1,-0.59,0,False,False
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
