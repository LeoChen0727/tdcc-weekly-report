# INDIVIDUAL STOCK CHATGPT PACKET - 1310 台苯

## Metadata
- generated_at: 2026-05-28 19:31:28 Asia/Taipei
- stock_id: 1310
- stock_name: 台苯
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1310_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1310_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1310_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1310_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1310_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1310_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1310_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1310_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1310_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1310_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1310_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1310_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1310_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1310.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1310.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1310.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1310.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1310.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1310.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1310_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1310_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1310_latest.md?ref=main

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
- open: 7.72
- high: 8.23
- low: 7.7
- close: 8.12
- volume: 5886572
- ma5: 7.93
- ema23_primary: 8.51
- distance_to_ema23_pct: -4.63
- ma20: 8.35
- ma60: 9.93
- ma120: 9.4
- return_5d: 0.62
- return_20d: -13.53
- volume_ratio: 1.6
- distance_to_ma20_pct_auxiliary: -2.74
- distance_to_high_60_pct: -38.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,9.5,9.68,9.36,9.5,3902363,10.12,-6.12,10.17,10.17,0.45
20260504,9.45,9.45,8.99,9,6013834,10.03,-10.23,10.07,10.17,0.72
20260505,9.05,9.16,9,9.03,3936383,9.94,-9.18,9.98,10.17,0.49
20260506,8.99,8.99,8.76,8.78,4106488,9.85,-10.82,9.85,10.16,0.54
20260507,8.68,8.88,8.55,8.88,3712795,9.77,-9.07,9.78,10.16,0.51
20260508,8.84,8.91,8.62,8.63,3764830,9.67,-10.76,9.68,10.15,0.55
20260511,8.6,8.81,8.59,8.64,2922793,9.58,-9.86,9.6,10.15,0.44
20260512,8.67,8.71,8.52,8.52,2618495,9.5,-10.28,9.51,10.14,0.45
20260513,8.53,8.6,8.35,8.35,4110305,9.4,-11.18,9.38,10.13,0.83
20260514,8.35,8.35,8.02,8.04,5741911,9.29,-13.43,9.27,10.12,1.21
20260515,8.05,8.1,7.9,7.9,3379462,9.17,-13.86,9.15,10.1,0.73
20260518,7.97,8.09,7.94,8.03,3364302,9.08,-11.53,9.05,10.09,0.76
20260519,8.03,8.11,7.96,7.97,1856439,8.98,-11.29,8.96,10.07,0.45
20260520,7.98,8.03,7.94,7.98,1609423,8.9,-10.34,8.86,10.05,0.4
20260521,8.01,8.1,8.01,8.07,1799778,8.83,-8.62,8.78,10.04,0.46
20260522,8.03,8.08,7.9,7.98,3803198,8.76,-8.91,8.68,10.02,1.05
20260525,7.95,8.05,7.78,8.01,3883784,8.7,-7.91,8.59,10,1.1
20260526,8.01,8.07,7.83,7.85,3168689,8.63,-9.01,8.51,9.98,0.91
20260527,7.85,7.91,7.7,7.7,3829374,8.55,-9.94,8.41,9.95,1.07
20260528,7.72,8.23,7.7,8.12,5886572,8.51,-4.63,8.35,9.93,1.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 30.24
- over_600_ratio: 27.22
- over_800_ratio: 24.75
- over_1000_ratio: 23.38
- over_400_change_1w: -0.05
- over_800_change_1w: 0.33
- over_1000_change_1w: 0.39
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.6,,24.69,,23.65,,0,False,False
20260508,30.83,0.23,24.46,-0.23,23.63,-0.02,1,False,False
20260515,30.29,-0.54,24.42,-0.04,22.99,-0.64,2,False,False
20260522,30.24,-0.05,24.75,0.33,23.38,0.39,3,False,True
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
