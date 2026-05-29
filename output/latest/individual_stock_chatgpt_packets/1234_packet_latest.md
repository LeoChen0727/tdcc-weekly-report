# INDIVIDUAL STOCK CHATGPT PACKET - 1234 黑松

## Metadata
- generated_at: 2026-05-29 19:31:34 Asia/Taipei
- stock_id: 1234
- stock_name: 黑松
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1234_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1234_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1234_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1234_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1234_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1234_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1234_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1234_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1234_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1234_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1234_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1234_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1234_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1234.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1234.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1234.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1234.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1234.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1234.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1234_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1234_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1234_latest.md?ref=main

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
- open: 34.35
- high: 34.55
- low: 34.25
- close: 34.4
- volume: 151511
- ma5: 34.21
- ema23_primary: 34.49
- distance_to_ema23_pct: -0.25
- ma20: 34.37
- ma60: 35.41
- ma120: 36.46
- return_5d: 2.53
- return_20d: -2.41
- volume_ratio: 0.73
- distance_to_ma20_pct_auxiliary: 0.08
- distance_to_high_60_pct: -7.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,35.2,35.2,35.05,35.05,215249,35.69,-1.78,35.7,36.29,1.46
20260505,35.05,35.05,34.9,35.05,262359,35.63,-1.64,35.67,36.26,1.69
20260506,35,35.1,35,35.05,169644,35.58,-1.5,35.63,36.22,1.06
20260507,35.05,35.25,35.05,35.25,192246,35.56,-0.86,35.6,36.19,1.23
20260508,35.3,35.35,35.1,35.2,134010,35.53,-0.92,35.57,36.16,0.85
20260511,35.2,35.2,35,35.05,160618,35.49,-1.23,35.54,36.13,1
20260512,35.05,35.05,34.85,34.9,192446,35.44,-1.52,35.49,36.09,1.17
20260513,34.85,34.85,34.5,34.5,275294,35.36,-2.43,35.43,36.05,1.61
20260514,34.6,34.6,33.9,34,533226,35.25,-3.54,35.32,36,2.79
20260515,34.05,34.05,33.75,33.75,283606,35.12,-3.91,35.2,35.95,1.43
20260518,33.8,33.8,33.3,33.4,332155,34.98,-4.51,35.06,35.89,1.58
20260519,33.4,34.2,33.4,34,191907,34.9,-2.57,34.95,35.84,0.9
20260520,34,34.05,33.45,33.75,110822,34.8,-3.02,34.84,35.79,0.53
20260521,33.75,34,33.55,33.9,55743,34.73,-2.38,34.74,35.73,0.27
20260522,33.75,33.85,33.55,33.55,137831,34.63,-3.11,34.64,35.67,0.69
20260525,33.55,33.95,33.55,33.95,140516,34.57,-1.8,34.56,35.61,0.7
20260526,33.95,34.4,33.95,34.25,197532,34.55,-0.85,34.52,35.56,1.01
20260527,34.25,34.35,34.05,34.25,283471,34.52,-0.78,34.47,35.51,1.38
20260528,34.35,34.35,34.05,34.2,122301,34.49,-0.85,34.41,35.46,0.59
20260529,34.35,34.55,34.25,34.4,151511,34.49,-0.25,34.37,35.41,0.73
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 83.33
- over_600_ratio: 79.96
- over_800_ratio: 76.37
- over_1000_ratio: 74.35
- over_400_change_1w: -0.02
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.25
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.44,,76.6,,74.12,,0,False,False
20260508,83.39,-0.05,76.58,-0.02,74.09,-0.03,0,False,False
20260515,83.35,-0.04,76.36,-0.22,74.1,0.01,1,False,True
20260522,83.33,-0.02,76.37,0.01,74.35,0.25,2,False,True
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
