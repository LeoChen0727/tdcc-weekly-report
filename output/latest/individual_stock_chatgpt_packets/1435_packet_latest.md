# INDIVIDUAL STOCK CHATGPT PACKET - 1435 中福

## Metadata
- generated_at: 2026-05-26 22:18:04 Asia/Taipei
- stock_id: 1435
- stock_name: 中福
- packet_status: standard_rawdata_packet
- latest_price_date: 20260428
- price_rows: 105
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1435_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1435_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1435_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1435_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1435_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1435_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1435_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1435_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1435_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1435_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1435_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1435_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1435_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1435.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1435.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1435.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1435.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1435.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1435.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1435_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1435_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1435_latest.md?ref=main

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
- date: 20260428
- open: 12.8
- high: 13.1
- low: 12.8
- close: 12.85
- volume: 70976
- ma5: 13.95
- ema23_primary: 15.82
- distance_to_ema23_pct: -18.78
- ma20: 15.68
- ma60: 19.3
- ma120: 21.22
- return_5d: -9.82
- return_20d: -30.73
- volume_ratio: 7.4
- distance_to_ma20_pct_auxiliary: -18.05
- distance_to_high_60_pct: -48.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260323,18.15,18.15,17.5,18.15,10004,20.08,-9.63,20.6,21.35,0.18
20260324,18.1,18.1,18.1,18.1,1711,19.92,-9.13,20.36,21.24,0.03
20260325,18.8,18.9,18.75,18.75,11418,19.82,-5.4,20.14,21.15,0.21
20260326,19.2,19.2,19.2,19.2,1638,19.77,-2.88,19.91,21.11,0.03
20260330,18.35,18.35,17.75,18.3,11371,19.65,-6.86,19.64,21.05,0.21
20260331,17.6,17.6,17.5,17.5,15406,19.47,-10.11,19.36,20.97,0.28
20260401,18,18.75,17.7,17.7,11515,19.32,-8.39,19.12,20.9,0.21
20260402,17.7,17.8,16.3,16.35,17020,19.07,-14.28,18.89,20.81,0.31
20260407,14.75,14.75,14.75,14.75,14516,18.71,-21.18,18.55,20.69,0.27
20260408,14.75,14.75,14.75,14.75,2121,18.38,-19.76,18.25,20.57,0.04
20260413,13.65,13.65,13.65,13.65,4148,17.99,-24.12,17.97,20.43,0.08
20260414,13.7,13.7,13.7,13.7,1501,17.63,-22.3,17.68,20.3,0.03
20260416,14.55,14.6,14.55,14.6,3232,17.38,-15.99,17.4,20.17,0.06
20260417,14.1,14.1,14.1,14.1,1563,17.11,-17.57,17.12,20.04,0.17
20260420,14.25,14.25,14.25,14.25,1012,16.87,-15.52,16.89,19.92,0.12
20260421,14.15,14.15,14,14.15,4348,16.64,-14.97,16.64,19.8,0.57
20260422,14.2,14.25,14.2,14.25,4206,16.44,-13.33,16.4,19.68,0.56
20260423,14.2,14.3,14.2,14.3,2009,16.26,-12.07,16.18,19.56,0.29
20260424,14.2,14.2,14.2,14.2,2016,16.09,-11.75,15.96,19.44,0.33
20260428,12.8,13.1,12.8,12.85,70976,15.82,-18.78,15.68,19.3,7.4
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 94.89
- over_600_ratio: 93.56
- over_800_ratio: 93.06
- over_1000_ratio: 93.06
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
20260430,94.89,,93.06,,93.06,,0,False,False
20260508,94.89,0,93.06,0,93.06,0,0,False,False
20260515,94.89,0,93.06,0,93.06,0,0,False,False
20260522,94.89,0,93.06,0,93.06,0,0,False,False
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
