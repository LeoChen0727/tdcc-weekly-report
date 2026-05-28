# INDIVIDUAL STOCK CHATGPT PACKET - 4609 唐鋒

## Metadata
- generated_at: 2026-05-28 20:19:32 Asia/Taipei
- stock_id: 4609
- stock_name: 唐鋒
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 108
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4609_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4609_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4609_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4609_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4609_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4609_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4609_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4609_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4609_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4609_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4609_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4609_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4609_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4609.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4609.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4609.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4609.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4609.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4609.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4609_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4609_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4609_latest.md?ref=main

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
- open: 5.28
- high: 5.72
- low: 5.28
- close: 5.72
- volume: 6000
- ma5: 5.44
- ema23_primary: 5.21
- distance_to_ema23_pct: 9.85
- ma20: 5.2
- ma60: 5.04
- ma120: 5.5
- return_5d: 4
- return_20d: 32.41
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: 9.93
- distance_to_high_60_pct: -4.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,4.32,4.59,4.32,4.59,25000,4.69,-2.07,4.7,5.2,0.7
20260429,4.4,4.4,4.4,4.4,4000,4.66,-5.64,4.66,5.16,0.11
20260430,4.84,4.84,4.84,4.84,36000,4.68,3.47,4.66,5.14,1
20260504,5.32,5.32,5.32,5.32,28000,4.73,12.44,4.67,5.13,0.75
20260505,5.53,5.7,5.53,5.53,54000,4.8,15.26,4.7,5.13,1.37
20260506,5.53,5.53,5.08,5.1,19000,4.82,5.74,4.69,5.11,0.48
20260507,4.81,5.03,4.73,4.76,16000,4.82,-1.2,4.67,5.09,0.4
20260508,5.23,5.23,5.23,5.23,36000,4.85,7.79,4.67,5.07,0.86
20260511,5.54,5.54,5.24,5.24,9000,4.88,7.28,4.67,5.06,0.21
20260512,5.24,5.24,4.88,5,10000,4.89,2.16,4.69,5.05,0.24
20260513,4.89,5,4.89,5,2000,4.9,1.98,4.7,5.04,0.05
20260514,5.09,5.16,5.09,5.16,3000,4.92,4.78,4.74,5.03,0.08
20260515,5.67,5.67,5.37,5.63,117000,4.98,12.98,4.82,5.04,3.1
20260518,5.63,5.99,5.56,5.56,5000,5.03,10.51,4.91,5.04,0.16
20260520,5.2,5.5,5.2,5.5,17000,5.07,8.47,4.98,5.04,0.55
20260522,5.16,5.16,5.16,5.16,5000,5.08,1.62,5.01,5.04,0.2
20260525,5.2,5.38,5.2,5.38,5000,5.1,5.43,5.04,5.04,0.22
20260526,5.38,5.78,5.38,5.75,6000,5.16,11.5,5.1,5.05,0.27
20260527,5.73,5.73,5.2,5.2,5000,5.16,0.77,5.13,5.04,0.23
20260528,5.28,5.72,5.28,5.72,6000,5.21,9.85,5.2,5.04,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 76
- over_600_ratio: 69.71
- over_800_ratio: 65.21
- over_1000_ratio: 63.36
- over_400_change_1w: -0.07
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.09,,65.3,,63.45,,0,False,False
20260508,76.08,-0.01,65.29,-0.01,63.44,-0.01,0,False,False
20260515,76.07,-0.01,65.28,-0.01,63.43,-0.01,0,False,False
20260522,76,-0.07,65.21,-0.07,63.36,-0.07,0,False,False
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
