# INDIVIDUAL STOCK CHATGPT PACKET - 4147 中裕

## Metadata
- generated_at: 2026-05-26 22:19:24 Asia/Taipei
- stock_id: 4147
- stock_name: 中裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4147_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4147_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4147_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4147_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4147_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4147_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4147_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4147_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4147_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4147_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4147_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4147_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4147_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4147.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4147.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4147.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4147.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4147.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4147.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4147_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4147_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4147_latest.md?ref=main

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
- open: 49.45
- high: 50.2
- low: 48.65
- close: 48.75
- volume: 49000
- ma5: 49.3
- ema23_primary: 50.09
- distance_to_ema23_pct: -2.67
- ma20: 49.6
- ma60: 51.46
- ma120: 56.36
- return_5d: -0.91
- return_20d: 0.93
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: -1.72
- distance_to_high_60_pct: -16.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,48.3,48.3,47.75,48.05,454000,51.76,-7.17,52.67,53.45,0.4
20260429,48.1,49.9,48.05,49.4,907000,51.56,-4.2,52.45,53.31,0.8
20260430,49,49.9,48.7,49.45,799000,51.39,-3.77,52.35,53.17,0.71
20260504,49.45,49.8,48.55,48.55,815000,51.15,-5.09,51.98,52.98,0.75
20260505,48.35,50.1,48.25,49.8,776000,51.04,-2.43,51.62,52.83,0.79
20260506,49.8,50.1,49.3,49.45,576000,50.91,-2.86,51.34,52.66,0.6
20260507,49.2,49.7,48.6,48.9,801000,50.74,-3.63,50.98,52.5,0.86
20260508,49.35,51.9,49.35,49.7,1238000,50.65,-1.88,50.71,52.35,1.36
20260511,50,50,48.6,48.85,858000,50.5,-3.27,50.4,52.23,0.94
20260512,48.85,50.4,48.55,50.1,858000,50.47,-0.73,50.22,52.13,0.94
20260513,49.9,50.9,49.1,49.1,691000,50.36,-2.49,50.03,52,0.77
20260514,49.15,54,49.15,53.7,3016000,50.63,6.06,50.03,51.95,3
20260515,52.8,54,50.5,51.1,1525000,50.67,0.84,49.91,51.87,1.46
20260518,51.1,51.4,50,50.2,806000,50.63,-0.86,49.76,51.8,0.78
20260519,50.2,50.4,49.2,49.2,975000,50.51,-2.6,49.69,51.71,0.96
20260520,49.4,49.4,48.2,48.85,1489000,50.38,-3.03,49.59,51.64,1.42
20260521,49.1,49.35,48.6,49,1028000,50.26,-2.51,49.5,51.56,0.97
20260522,49.25,51.2,49.25,50.5,50000,50.28,0.44,49.52,51.54,0.05
20260525,51,51,49.3,49.4,50000,50.21,-1.61,49.58,51.5,0.05
20260526,49.45,50.2,48.65,48.75,49000,50.09,-2.67,49.6,51.46,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.23
- over_600_ratio: 48.84
- over_800_ratio: 45.28
- over_1000_ratio: 42.99
- over_400_change_1w: -0.42
- over_800_change_1w: -0.31
- over_1000_change_1w: -0.3
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.43,,45.15,,42.21,,0,False,False
20260508,52.57,0.14,45.28,0.13,42.69,0.48,1,True,True
20260515,52.65,0.08,45.59,0.31,43.29,0.6,2,True,True
20260522,52.23,-0.42,45.28,-0.31,42.99,-0.3,0,False,False
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
