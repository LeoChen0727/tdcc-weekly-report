# INDIVIDUAL STOCK CHATGPT PACKET - 1219 福壽

## Metadata
- generated_at: 2026-05-28 19:31:26 Asia/Taipei
- stock_id: 1219
- stock_name: 福壽
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1219_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1219_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1219_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1219_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1219_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1219_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1219_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1219_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1219_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1219_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1219_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1219_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1219_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1219.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1219.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1219.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1219.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1219.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1219.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1219_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1219_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1219_latest.md?ref=main

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
- open: 12.35
- high: 12.5
- low: 12.3
- close: 12.5
- volume: 287988
- ma5: 12.45
- ema23_primary: 12.93
- distance_to_ema23_pct: -3.3
- ma20: 12.92
- ma60: 13.51
- ma120: 13.53
- return_5d: 0
- return_20d: -7.41
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -3.23
- distance_to_high_60_pct: -15.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,13.5,13.5,13.4,13.5,215198,13.83,-2.36,13.96,13.72,0.32
20260504,13.45,13.5,13.45,13.45,377078,13.8,-2.5,13.93,13.72,0.56
20260505,13.45,13.45,13.3,13.45,582410,13.77,-2.3,13.91,13.72,0.85
20260506,13.45,13.45,13.35,13.4,531726,13.74,-2.44,13.89,13.72,0.77
20260507,13.4,13.45,13.3,13.4,519018,13.71,-2.25,13.87,13.71,0.75
20260508,13.4,13.45,13.35,13.4,334222,13.68,-2.06,13.84,13.71,0.52
20260511,13.4,13.4,13.25,13.3,838149,13.65,-2.57,13.79,13.71,1.29
20260512,13.35,13.35,13.2,13.2,549554,13.61,-3.03,13.72,13.7,0.98
20260513,13.2,13.2,13,13.1,1006861,13.57,-3.46,13.66,13.7,1.75
20260514,13,13.1,12.95,12.95,621053,13.52,-4.2,13.58,13.69,1.15
20260515,12.95,13,12.75,12.8,1148363,13.46,-4.89,13.51,13.68,2.14
20260518,12.9,12.9,12.45,12.5,982564,13.38,-6.57,13.42,13.66,1.74
20260519,12.5,12.65,12.5,12.65,384296,13.32,-5.02,13.35,13.64,0.68
20260520,12.6,12.6,12.45,12.5,707298,13.25,-5.66,13.27,13.62,1.22
20260521,12.5,12.6,12.5,12.5,421594,13.19,-5.21,13.2,13.61,0.72
20260522,12.55,12.55,12.4,12.45,585279,13.13,-5.15,13.14,13.59,1.02
20260525,12.4,12.55,12.3,12.45,597781,13.07,-4.74,13.08,13.57,1.02
20260526,12.55,12.65,12.45,12.5,399918,13.02,-4.01,13.03,13.55,0.71
20260527,12.5,12.5,12.35,12.35,538490,12.97,-4.75,12.97,13.53,0.93
20260528,12.35,12.5,12.3,12.5,287988,12.93,-3.3,12.92,13.51,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.71
- over_600_ratio: 59.9
- over_800_ratio: 58.18
- over_1000_ratio: 56.41
- over_400_change_1w: -0.08
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.28
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.89,,58.1,,56.33,,0,False,False
20260508,61.94,0.05,58.17,0.07,56.4,0.07,1,False,True
20260515,61.79,-0.15,58.14,-0.03,56.13,-0.27,2,False,False
20260522,61.71,-0.08,58.18,0.04,56.41,0.28,3,False,True
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
