# INDIVIDUAL STOCK CHATGPT PACKET - 1538 正峰

## Metadata
- generated_at: 2026-05-30 23:41:03 Asia/Taipei
- stock_id: 1538
- stock_name: 正峰
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 231
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1538_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1538_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1538_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1538_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1538_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1538_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1538_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1538_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1538_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1538_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1538_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1538_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1538_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1538.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1538.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1538.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1538.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1538.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1538.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1538_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1538_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1538_latest.md?ref=main

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
- open: 11.9
- high: 11.9
- low: 11.6
- close: 11.8
- volume: 6776
- ma5: 11.79
- ema23_primary: 12.57
- distance_to_ema23_pct: -6.09
- ma20: 12.5
- ma60: 15.29
- ma120: 20.64
- return_5d: -1.67
- return_20d: -8.53
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: -5.58
- distance_to_high_60_pct: -56.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260424,13.3,13.3,13.3,13.3,1076,14.14,-5.92,13.03,19.66,0.03
20260428,14.25,14.25,14.25,14.25,1418,14.15,0.73,12.99,19.46,0.04
20260429,14.55,14.55,14.2,14.2,2147,14.15,0.34,12.99,19.26,0.06
20260430,13.35,13.35,13.35,13.35,1249,14.08,-5.22,13,19.04,0.04
20260505,13.35,13.35,13.35,13.35,1687,14.02,-4.8,13,18.82,0.06
20260506,12.15,12.95,12.15,12.95,23713,13.93,-7.06,12.99,18.6,1.02
20260507,12.35,12.5,11.7,12.2,100110,13.79,-11.53,12.95,18.36,3.61
20260508,11.1,12.2,11.1,12.2,3469,13.66,-10.67,12.93,18.13,0.15
20260511,11.35,12.2,11.1,11.65,41537,13.49,-13.64,12.88,17.89,1.71
20260512,12,12.4,12,12.15,11153,13.38,-9.18,12.86,17.66,0.55
20260513,11.15,12.2,10.95,12.2,99451,13.28,-8.13,12.83,17.42,3.98
20260515,12.6,12.6,12,12.4,10532,13.21,-6.11,12.81,17.19,0.43
20260518,12.4,12.4,12.4,12.4,2002,13.14,-5.63,12.8,16.96,0.09
20260519,12.4,12.4,12.4,12.4,1623,13.08,-5.18,12.79,16.73,0.07
20260522,11.55,12,11.55,12,3146,12.99,-7.61,12.76,16.5,0.15
20260525,12,12,11.2,11.8,29431,12.89,-8.45,12.71,16.26,1.55
20260526,11.9,11.9,11.75,11.75,5371,12.79,-8.16,12.66,16.02,0.28
20260527,11.75,11.8,11.15,11.8,20278,12.71,-7.17,12.61,15.78,1.12
20260528,11.8,11.8,11.75,11.8,3167,12.64,-6.61,12.55,15.54,0.17
20260529,11.9,11.9,11.6,11.8,6776,12.57,-6.09,12.5,15.29,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 78.45
- over_600_ratio: 75.36
- over_800_ratio: 70.77
- over_1000_ratio: 70.77
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
20260430,78.21,,70.77,,70.77,,0,False,False
20260508,78.3,0.09,70.77,0,70.77,0,1,False,False
20260515,78.45,0.15,70.77,0,70.77,0,2,False,False
20260522,78.45,0,70.77,0,70.77,0,0,False,False
20260529,78.45,0,70.77,0,70.77,0,0,False,False
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
