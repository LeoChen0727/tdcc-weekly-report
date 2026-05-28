# INDIVIDUAL STOCK CHATGPT PACKET - 2511 太子

## Metadata
- generated_at: 2026-05-28 20:18:47 Asia/Taipei
- stock_id: 2511
- stock_name: 太子
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2511_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2511_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2511_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2511_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2511_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2511_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2511_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2511_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2511_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2511_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2511_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2511_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2511_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2511.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2511.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2511.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2511.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2511.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2511.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2511_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2511_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2511_latest.md?ref=main

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
- open: 7.65
- high: 7.68
- low: 7.6
- close: 7.66
- volume: 937970
- ma5: 7.67
- ema23_primary: 7.76
- distance_to_ema23_pct: -1.3
- ma20: 7.73
- ma60: 7.99
- ma120: 8.14
- return_5d: -0.26
- return_20d: -4.25
- volume_ratio: 0.71
- distance_to_ma20_pct_auxiliary: -0.91
- distance_to_high_60_pct: -7.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,7.99,8,7.94,7.99,941964,8.09,-1.2,8.1,8.19,0.83
20260504,7.99,7.99,7.86,7.86,2587458,8.07,-2.58,8.09,8.18,2.08
20260505,7.87,7.9,7.85,7.89,920053,8.05,-2.02,8.08,8.17,0.74
20260506,7.95,7.95,7.88,7.9,854610,8.04,-1.74,8.07,8.16,0.68
20260507,7.87,7.89,7.82,7.88,1837061,8.03,-1.83,8.06,8.15,1.43
20260508,7.98,7.98,7.61,7.81,2789036,8.01,-2.48,8.04,8.14,2.02
20260511,7.79,7.86,7.75,7.82,856976,7.99,-2.17,8.02,8.13,0.62
20260512,7.82,7.82,7.67,7.69,2388637,7.97,-3.49,8,8.12,1.68
20260513,7.65,7.71,7.65,7.7,788639,7.95,-3.09,7.97,8.11,0.56
20260514,7.67,7.72,7.62,7.64,1413956,7.92,-3.54,7.94,8.1,0.98
20260515,7.65,7.67,7.58,7.6,1981669,7.89,-3.72,7.91,8.08,1.31
20260518,7.57,7.59,7.54,7.55,1137882,7.86,-4,7.88,8.07,0.76
20260519,7.56,7.63,7.55,7.6,607766,7.84,-3.09,7.86,8.06,0.41
20260520,7.6,7.66,7.58,7.66,779471,7.83,-2.14,7.83,8.05,0.53
20260521,7.66,7.69,7.64,7.68,696884,7.82,-1.73,7.81,8.04,0.49
20260522,7.67,7.76,7.65,7.74,898295,7.81,-0.88,7.8,8.03,0.65
20260525,7.75,7.75,7.62,7.69,1433189,7.8,-1.4,7.78,8.02,1.04
20260526,7.6,7.67,7.6,7.62,1085949,7.78,-2.11,7.77,8.01,0.84
20260527,7.62,7.64,7.58,7.62,1487093,7.77,-1.94,7.75,8,1.14
20260528,7.65,7.68,7.6,7.66,937970,7.76,-1.3,7.73,7.99,0.71
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.63
- over_600_ratio: 77.39
- over_800_ratio: 75.45
- over_1000_ratio: 73.92
- over_400_change_1w: 0.12
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.66,,75.71,,74.27,,0,False,False
20260508,79.63,-0.03,75.61,-0.1,74.05,-0.22,0,False,False
20260515,79.51,-0.12,75.48,-0.13,73.96,-0.09,0,False,False
20260522,79.63,0.12,75.45,-0.03,73.92,-0.04,1,False,False
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
