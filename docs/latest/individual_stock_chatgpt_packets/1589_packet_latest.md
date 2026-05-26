# INDIVIDUAL STOCK CHATGPT PACKET - 1589 永冠-KY

## Metadata
- generated_at: 2026-05-26 22:18:11 Asia/Taipei
- stock_id: 1589
- stock_name: 永冠-KY
- packet_status: standard_rawdata_packet
- latest_price_date: 20260402
- price_rows: 99
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1589_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1589_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1589_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1589_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1589_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1589_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1589_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1589_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1589_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1589_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1589_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1589_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1589_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1589.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1589.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1589.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1589.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1589.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1589.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1589_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1589_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1589_latest.md?ref=main

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
- date: 20260402
- open: 5.54
- high: 5.54
- low: 5.54
- close: 5.54
- volume: 8432214
- ma5: 6.47
- ema23_primary: 8.42
- distance_to_ema23_pct: -34.24
- ma20: 7.39
- ma60: 13.22
- ma120: 14.94
- return_5d: -27.68
- return_20d: -32.36
- volume_ratio: 4.02
- distance_to_ma20_pct_auxiliary: -25.01
- distance_to_high_60_pct: -70.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260306,7.38,7.38,7.38,7.38,749453,13.69,-46.08,14.41,16.34,1.06
20260309,6.65,6.65,6.65,6.65,552340,13.1,-49.24,13.85,16.16,0.8
20260310,5.99,7.31,5.99,7.31,9205657,12.62,-42.07,13.34,15.99,8.3
20260311,6.58,6.75,6.58,6.6,3941471,12.12,-45.53,12.81,15.8,3.16
20260312,6.8,7.26,6.8,7.26,1800618,11.71,-38.01,12.34,15.63,1.39
20260313,7.5,7.98,7.5,7.98,1158662,11.4,-30.01,11.92,15.47,0.9
20260316,8,8.77,8,8.77,1691555,11.18,-21.57,11.53,15.34,1.26
20260317,8.88,9.64,7.9,7.9,3932001,10.91,-27.58,11.09,15.19,2.63
20260318,7.9,8.65,7.9,8.64,1176608,10.72,-19.4,10.71,15.04,0.78
20260319,8.99,8.99,8.4,8.4,1405179,10.53,-20.2,10.32,14.9,0.92
20260320,8.17,8.17,7.71,7.71,996954,10.29,-25.08,9.9,14.73,0.65
20260323,6.96,7.71,6.95,7.71,1243650,10.08,-23.48,9.46,14.56,0.79
20260324,7.83,7.98,7.5,7.81,555037,9.89,-21.01,9.01,14.4,0.36
20260325,7.56,7.79,7.3,7.64,561256,9.7,-21.24,8.62,14.25,0.36
20260326,7.67,7.72,7.66,7.66,496906,9.53,-19.62,8.32,14.09,0.32
20260327,7.21,7.33,7.2,7.2,554105,9.34,-22.88,8.06,13.93,0.35
20260330,6.63,6.84,6.61,6.84,810355,9.13,-25.07,7.84,13.76,0.5
20260331,6.69,6.82,6.5,6.6,736381,8.92,-25.99,7.67,13.59,0.45
20260401,5.94,6.15,5.94,6.15,1905289,8.69,-29.2,7.52,13.41,1.12
20260402,5.54,5.54,5.54,5.54,8432214,8.42,-34.24,7.39,13.22,4.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 28.57
- over_600_ratio: 24.63
- over_800_ratio: 23.28
- over_1000_ratio: 21.01
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
20260430,28.6,,23.31,,21.04,,0,False,False
20260508,28.6,0,23.31,0,21.04,0,0,False,False
20260515,28.57,-0.03,23.28,-0.03,21.01,-0.03,0,False,False
20260522,28.57,0,23.28,0,21.01,0,0,False,False
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
