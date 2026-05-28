# INDIVIDUAL STOCK CHATGPT PACKET - 8072 陞泰

## Metadata
- generated_at: 2026-05-28 19:33:44 Asia/Taipei
- stock_id: 8072
- stock_name: 陞泰
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8072_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8072_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8072_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8072_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8072_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8072_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8072_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8072_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8072_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8072_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8072_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8072_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8072_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8072.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8072.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8072.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8072.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8072.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8072.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8072_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8072_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8072_latest.md?ref=main

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
- open: 27.8
- high: 28.65
- low: 27.3
- close: 27.3
- volume: 375019
- ma5: 27.77
- ema23_primary: 27.78
- distance_to_ema23_pct: -1.73
- ma20: 27.71
- ma60: 28.04
- ma120: 29.41
- return_5d: -1.09
- return_20d: -1.8
- volume_ratio: 1.56
- distance_to_ma20_pct_auxiliary: -1.49
- distance_to_high_60_pct: -12.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,27.9,28.15,27.4,27.45,121693,28.42,-3.42,28.48,29.06,0.36
20260504,27.95,28.85,27.6,28.05,216621,28.39,-1.2,28.52,28.99,0.63
20260505,28.05,28.65,28.05,28.5,101888,28.4,0.35,28.61,28.93,0.3
20260506,28.65,28.65,27.95,28.35,151939,28.4,-0.16,28.71,28.88,0.45
20260507,28.6,29,27.95,28.5,292423,28.41,0.33,28.71,28.81,0.91
20260508,28.9,29.2,28.2,28.75,253492,28.43,1.11,28.67,28.77,0.94
20260511,28.4,28.4,27.5,28,343138,28.4,-1.4,28.63,28.73,1.3
20260512,28,28.15,27.45,27.55,160749,28.33,-2.74,28.57,28.69,0.61
20260513,27.55,28.2,27.05,27.8,365815,28.28,-1.71,28.52,28.66,1.33
20260514,27.9,27.9,27.2,27.2,182594,28.19,-3.52,28.45,28.61,0.66
20260515,27.25,27.7,26.5,26.6,319443,28.06,-5.2,28.28,28.55,1.25
20260518,27.5,27.5,26.35,27,124341,27.97,-3.47,28.15,28.49,0.52
20260519,27.05,27.05,26.5,26.8,198912,27.87,-3.85,28.03,28.42,0.83
20260520,26.75,27.6,26.75,27.25,151530,27.82,-2.06,27.95,28.37,0.64
20260521,27.3,28.05,27.3,27.6,227854,27.8,-0.73,27.88,28.33,0.96
20260522,27.95,28.1,27.6,27.9,142597,27.81,0.32,27.8,28.28,0.67
20260525,28.15,28.65,27.55,28.2,588031,27.84,1.28,27.75,28.23,2.58
20260526,28.45,28.55,27.65,27.8,223173,27.84,-0.14,27.75,28.17,1.01
20260527,27.9,27.95,27.45,27.65,277708,27.82,-0.63,27.74,28.11,1.22
20260528,27.8,28.65,27.3,27.3,375019,27.78,-1.73,27.71,28.04,1.56
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.8
- over_600_ratio: 58.98
- over_800_ratio: 58.98
- over_1000_ratio: 57.87
- over_400_change_1w: -0.1
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.84,,58.98,,57.87,,0,False,False
20260508,60.97,0.13,58.98,0,57.87,0,1,False,False
20260515,60.9,-0.07,58.98,0,57.87,0,0,False,False
20260522,60.8,-0.1,58.98,0,57.87,0,0,False,False
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
