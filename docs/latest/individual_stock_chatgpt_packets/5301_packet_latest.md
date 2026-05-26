# INDIVIDUAL STOCK CHATGPT PACKET - 5301 寶得利

## Metadata
- generated_at: 2026-05-26 23:01:53 Asia/Taipei
- stock_id: 5301
- stock_name: 寶得利
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 119
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5301_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5301_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5301_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5301_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5301_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5301_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5301_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5301_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5301_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5301_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5301_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5301_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5301_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5301.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5301.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5301.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5301.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5301.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5301.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5301_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5301_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5301_latest.md?ref=main

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
- open: 6.7
- high: 6.78
- low: 6.7
- close: 6.73
- volume: 7000
- ma5: 6.8
- ema23_primary: 7.71
- distance_to_ema23_pct: -12.71
- ma20: 7.64
- ma60: 9.23
- ma120: 10.09
- return_5d: -6.92
- return_20d: -25.22
- volume_ratio: 0.32
- distance_to_ma20_pct_auxiliary: -11.97
- distance_to_high_60_pct: -44.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260423,9,9.1,9,9,5000,9.45,-4.71,9.32,10.3,0.6
20260424,8.8,8.8,8.8,8.8,2000,9.39,-6.3,9.28,10.28,0.24
20260427,8.79,8.85,8.79,8.85,34000,9.35,-5.31,9.25,10.24,3.56
20260504,8.51,9.09,8.51,9.09,10000,9.32,-2.52,9.23,10.21,1.02
20260505,8.46,8.66,8.19,8.19,70000,9.23,-11.27,9.19,10.16,5.53
20260506,7.8,8.18,7.8,7.86,35000,9.12,-13.78,9.11,10.08,2.49
20260507,7.86,7.86,7.34,7.34,32000,8.97,-18.16,9.01,10.02,2.05
20260508,7.34,7.4,7.22,7.4,43000,8.84,-16.27,8.9,9.95,2.44
20260511,7.4,7.56,7.33,7.55,10000,8.73,-13.52,8.81,9.89,0.56
20260512,7.55,7.78,7.55,7.78,2000,8.65,-10.07,8.72,9.83,0.11
20260513,7.77,7.77,7.15,7.66,9000,8.57,-10.6,8.65,9.78,0.5
20260514,7.66,7.66,7.25,7.32,28000,8.46,-13.52,8.55,9.72,1.53
20260515,7.32,7.55,7,7.45,7000,8.38,-11.1,8.47,9.67,0.42
20260518,7.44,7.44,7.16,7.37,8000,8.3,-11.16,8.36,9.62,0.47
20260519,7.36,7.36,7,7.23,33000,8.21,-11.9,8.25,9.56,1.8
20260520,7.14,7.14,6.78,6.82,65000,8.09,-15.71,8.12,9.51,3.02
20260521,6.82,6.84,6.7,6.8,24000,7.98,-14.83,7.99,9.44,1.07
20260522,6.76,7.13,6.76,6.96,7000,7.9,-11.88,7.87,9.38,0.32
20260525,6.96,6.99,6.7,6.7,7000,7.8,-14.09,7.76,9.31,0.32
20260526,6.7,6.78,6.7,6.73,7000,7.71,-12.71,7.64,9.23,0.32
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.63
- over_600_ratio: 79.14
- over_800_ratio: 77.12
- over_1000_ratio: 74.47
- over_400_change_1w: -0.02
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.61,,77.02,,74.37,,0,False,False
20260508,80.62,0.01,77.03,0.01,74.38,0.01,1,True,True
20260515,80.65,0.03,77.06,0.03,74.41,0.03,2,True,True
20260522,80.63,-0.02,77.12,0.06,74.47,0.06,3,False,True
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
