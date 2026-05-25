# INDIVIDUAL STOCK CHATGPT PACKET - 2023 燁輝

## Metadata
- generated_at: 2026-05-26 03:05:12 Asia/Taipei
- stock_id: 2023
- stock_name: 燁輝
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2023_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2023_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2023_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2023_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2023_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2023_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2023_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2023_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2023_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2023_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2023_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2023_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2023_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2023.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2023.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2023.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2023.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2023.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2023.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2023_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2023_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2023_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 13.6
- high: 13.7
- low: 13.45
- close: 13.7
- volume: 4350261
- ma5: 13.75
- ma20: 13.87
- ma60: 14.19
- ma120: 14.54
- ema23: 13.87
- return_5d: 0.37
- return_20d: -2.84
- volume_ratio: 1.33
- distance_to_ma20_pct: -1.19
- distance_to_high_60_pct: -8.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ema23,volume_ratio
20260430,14.1,14.1,13.9,14,3047393,14.07,14.12,14.51,14.16,1.6
20260504,13.95,13.95,13.8,13.9,3034610,14.05,14.1,14.5,14.14,1.51
20260505,13.9,13.95,13.8,13.95,2145894,14,14.07,14.48,14.12,1.04
20260506,13.95,14.1,13.85,14.05,2269549,14,14.05,14.47,14.12,1.06
20260507,13.95,14,13.85,14,1825761,13.98,14.04,14.46,14.11,0.83
20260508,14.05,14.5,13.9,14.4,3877161,14.06,14.05,14.44,14.13,1.71
20260511,14.15,14.2,13.85,13.95,4275674,14.07,14.05,14.41,14.12,1.88
20260512,13.95,13.95,13.75,13.9,3573382,14.06,14.03,14.39,14.1,1.54
20260513,13.9,13.9,13.75,13.9,2609126,14.03,14.02,14.38,14.08,1.1
20260514,13.85,13.95,13.8,13.95,2282854,14.02,14.02,14.37,14.07,0.95
20260515,13.95,13.95,13.65,13.9,4829769,13.92,14.01,14.35,14.06,1.93
20260518,13.9,13.9,13.6,13.75,2549523,13.88,14,14.33,14.03,0.99
20260519,13.65,13.8,13.6,13.6,2027823,13.82,13.98,14.31,14,0.78
20260520,13.65,13.65,13.35,13.65,3017403,13.77,13.96,14.29,13.97,1.12
20260521,13.6,13.75,13.55,13.65,1110730,13.71,13.94,14.27,13.94,0.42
20260522,13.6,13.7,13.45,13.7,4350261,13.67,13.93,14.25,13.92,1.66
20260523,13.6,13.7,13.45,13.7,4350261,13.66,13.91,14.24,13.9,1.58
20260524,13.6,13.7,13.45,13.7,4350261,13.68,13.89,14.22,13.89,1.52
20260525,13.6,14.35,13.5,13.95,5579706,13.74,13.88,14.21,13.89,1.81
20260526,13.6,13.7,13.45,13.7,4350261,13.75,13.87,14.19,13.87,1.33
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.54
- over_600_ratio: 77.47
- over_800_ratio: 76.92
- over_1000_ratio: 76.65
- over_400_change_1w: 0
- over_800_change_1w: -0.11
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.15,,76.59,,76.37,,0,False,False
20260508,78.3,0.15,76.8,0.21,76.57,0.2,1,True,True
20260515,78.54,0.24,77.03,0.23,76.71,0.14,2,True,True
20260522,78.54,0,76.92,-0.11,76.65,-0.06,0,False,False
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
