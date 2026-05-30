# INDIVIDUAL STOCK CHATGPT PACKET - 3325 旭品

## Metadata
- generated_at: 2026-05-30 23:41:59 Asia/Taipei
- stock_id: 3325
- stock_name: 旭品
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3325_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3325_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3325_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3325_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3325_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3325_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3325_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3325_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3325_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3325_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3325_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3325_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3325_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3325.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3325.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3325.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3325.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3325.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3325.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3325_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3325_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3325_latest.md?ref=main

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
- open: 11.8
- high: 11.95
- low: 11.7
- close: 11.8
- volume: 12000
- ma5: 11.99
- ema23_primary: 12.31
- distance_to_ema23_pct: -4.13
- ma20: 12.25
- ma60: 12.99
- ma120: 14.78
- return_5d: -1.26
- return_20d: -9.23
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -3.65
- distance_to_high_60_pct: -26.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,13.5,13.5,12.6,12.8,325000,13.27,-3.53,13.04,13.93,0.85
20260505,12.8,13.2,12.65,12.9,261000,13.24,-2.55,13.06,13.88,0.67
20260506,12.9,13.3,12.75,12.95,229000,13.21,-1.99,13.09,13.83,0.59
20260507,12.95,12.95,12.65,12.9,284000,13.19,-2.18,13.1,13.78,0.72
20260508,12.9,12.95,12.6,12.6,253000,13.14,-4.1,13.11,13.72,0.64
20260511,12.95,12.95,12.7,12.75,154000,13.11,-2.71,13.12,13.68,0.39
20260512,12.65,12.65,12.1,12.3,498000,13.04,-5.67,13.12,13.63,1.2
20260513,12.2,12.45,12,12.2,537000,12.97,-5.93,13.12,13.58,1.28
20260514,12.9,12.9,11.95,12.05,434000,12.89,-6.53,13.12,13.52,1.07
20260515,12.1,12.35,12,12.05,505000,12.82,-6.02,13.11,13.47,1.21
20260518,12.1,12.1,11.9,12,233000,12.75,-5.91,13.04,13.43,0.58
20260519,12.05,12.3,11.75,11.8,422000,12.67,-6.9,12.9,13.38,1.08
20260520,11.75,11.95,11.7,11.8,153000,12.6,-6.36,12.77,13.33,0.49
20260521,11.85,12.1,11.8,11.95,263000,12.55,-4.76,12.64,13.29,0.87
20260522,12.1,12.15,11.9,11.95,12000,12.5,-4.38,12.56,13.24,0.04
20260525,12,12.4,11.8,12.4,12000,12.49,-0.71,12.5,13.19,0.04
20260526,12.4,12.4,12,12.15,12000,12.46,-2.49,12.46,13.14,0.05
20260527,12.05,12.1,11.8,11.85,12000,12.41,-4.51,12.38,13.09,0.05
20260528,11.65,12.05,11.65,11.75,12000,12.35,-4.9,12.31,13.03,0.05
20260529,11.8,11.95,11.7,11.8,12000,12.31,-4.13,12.25,12.99,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 30.1
- over_600_ratio: 23.29
- over_800_ratio: 19.59
- over_1000_ratio: 14.69
- over_400_change_1w: 0.45
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,29.68,,19.58,,14.69,,0,False,False
20260508,30.02,0.34,19.58,0,14.69,0,1,False,False
20260515,29.63,-0.39,19.58,0,14.69,0,0,False,False
20260522,29.65,0.02,19.59,0.01,14.69,0,1,False,True
20260529,30.1,0.45,19.59,0,14.69,0,2,False,False
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
