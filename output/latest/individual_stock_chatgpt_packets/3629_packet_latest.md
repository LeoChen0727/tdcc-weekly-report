# INDIVIDUAL STOCK CHATGPT PACKET - 3629 地心引力

## Metadata
- generated_at: 2026-05-27 21:27:13 Asia/Taipei
- stock_id: 3629
- stock_name: 地心引力
- packet_status: standard_rawdata_packet
- latest_price_date: 20260527
- price_rows: 88
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3629_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3629_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3629_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3629_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3629_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3629_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3629_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3629_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3629_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3629_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3629_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3629_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3629_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3629.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3629.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3629.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3629.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3629.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3629.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3629_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3629_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3629_latest.md?ref=main

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
- date: 20260527
- open: 16.25
- high: 16.3
- low: 16
- close: 16
- volume: 16000
- ma5: 16.52
- ema23_primary: 17.18
- distance_to_ema23_pct: -6.85
- ma20: 16.79
- ma60: 18.76
- ma120: 20.42
- return_5d: -4.19
- return_20d: -11.11
- volume_ratio: 1.63
- distance_to_ma20_pct_auxiliary: -4.68
- distance_to_high_60_pct: -39.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260417,17.45,17.45,17.45,17.45,8000,18.95,-7.94,18.54,20.84,1.04
20260420,17.45,17.45,17.45,17.45,1000,18.83,-7.33,18.51,20.73,0.18
20260421,15.75,16.9,15.75,16.6,22000,18.64,-10.96,18.45,20.63,3.33
20260422,16,16.7,16,16.7,8000,18.48,-9.64,18.34,20.52,1.16
20260423,16.8,16.8,16,16,9000,18.27,-12.45,18.23,20.41,1.27
20260427,16,16,16,16,2000,18.09,-11.53,18.11,20.31,0.29
20260430,16.6,16.7,16.6,16.6,10000,17.96,-7.58,18.05,20.2,1.37
20260504,16.2,16.2,16.2,16.2,3000,17.81,-9.06,17.96,20.09,0.41
20260506,16.2,16.45,16.2,16.45,2000,17.7,-7.07,17.91,19.95,0.27
20260507,16.65,16.65,16.65,16.65,10000,17.61,-5.47,17.79,19.85,1.38
20260508,16.65,16.65,16.5,16.6,22000,17.53,-5.3,17.7,19.75,2.67
20260511,17.3,17.95,17.3,17.95,2000,17.56,2.2,17.7,19.66,0.26
20260512,18.8,18.8,18.8,18.8,1000,17.67,6.41,17.64,19.58,0.14
20260513,17.15,17.15,16.95,16.95,24000,17.61,-3.73,17.42,19.46,2.87
20260514,16.7,16.7,16.7,16.7,1000,17.53,-4.74,17.24,19.3,0.12
20260520,16.5,16.5,16.5,16.5,5000,17.45,-5.42,17.07,19.18,0.6
20260522,16.55,16.55,16.1,16.1,16000,17.33,-7.12,16.96,19.04,1.9
20260525,16.05,17.55,16.05,16.6,17000,17.27,-3.89,16.94,18.94,1.86
20260526,17.95,17.95,17.4,17.4,17000,17.28,0.68,16.89,18.86,1.73
20260527,16.25,16.3,16,16,16000,17.18,-6.85,16.79,18.76,1.63
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.89
- over_600_ratio: 84.01
- over_800_ratio: 84.01
- over_1000_ratio: 84.01
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
20260430,86.89,,84.01,,84.01,,0,False,False
20260508,86.89,0,84.01,0,84.01,0,0,False,False
20260515,86.89,0,84.01,0,84.01,0,0,False,False
20260522,86.89,0,84.01,0,84.01,0,0,False,False
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
