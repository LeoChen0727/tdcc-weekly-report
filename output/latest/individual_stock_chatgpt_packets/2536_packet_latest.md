# INDIVIDUAL STOCK CHATGPT PACKET - 2536 宏普

## Metadata
- generated_at: 2026-05-29 19:32:10 Asia/Taipei
- stock_id: 2536
- stock_name: 宏普
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2536_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2536_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2536_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2536_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2536_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2536_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2536_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2536_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2536_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2536_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2536_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2536_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2536_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2536.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2536.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2536.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2536.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2536.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2536.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2536_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2536_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2536_latest.md?ref=main

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
- open: 19.8
- high: 19.8
- low: 19.3
- close: 19.5
- volume: 376736
- ma5: 19.47
- ema23_primary: 20.31
- distance_to_ema23_pct: -3.97
- ma20: 20.14
- ma60: 21.62
- ma120: 23.2
- return_5d: -2.26
- return_20d: -9.51
- volume_ratio: 0.8
- distance_to_ma20_pct_auxiliary: -3.19
- distance_to_high_60_pct: -17.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,21.6,21.7,21,21.1,541861,22.05,-4.29,22.08,22.52,1.55
20260505,21.05,21.25,20.85,20.9,218232,21.95,-4.79,22.02,22.48,0.61
20260506,20.9,21,20.25,20.4,656510,21.82,-6.51,21.92,22.43,1.71
20260507,21.4,21.8,20.75,20.85,739430,21.74,-4.1,21.83,22.4,2.13
20260508,20.95,21.05,20.6,20.65,461117,21.65,-4.62,21.74,22.37,1.37
20260511,20.65,20.65,20.5,20.5,326777,21.55,-4.89,21.66,22.34,0.96
20260512,20.5,20.5,20.25,20.35,516005,21.45,-5.14,21.55,22.3,1.48
20260513,20.3,20.45,20.25,20.3,372642,21.36,-4.95,21.46,22.26,1.04
20260514,20.3,20.45,20.1,20.1,560617,21.25,-5.42,21.34,22.22,1.49
20260515,20,20.15,20,20.05,477063,21.15,-5.21,21.23,22.18,1.21
20260518,20.05,20.3,20.05,20.1,200600,21.06,-4.58,21.11,22.14,0.51
20260519,20.15,20.3,20.15,20.15,136111,20.99,-4,21.02,22.1,0.35
20260520,20.15,20.15,19.9,20.05,414184,20.91,-4.11,20.91,22.06,1.05
20260521,20.1,20.2,19.95,20.05,372378,20.84,-3.78,20.82,22.01,0.96
20260522,20.05,20.05,19.9,19.95,431501,20.76,-3.92,20.72,21.96,1.12
20260525,19.95,19.95,19.6,19.65,980820,20.67,-4.94,20.61,21.91,2.27
20260526,19.75,19.8,19.45,19.55,491081,20.58,-5,20.51,21.84,1.14
20260527,19.7,19.75,19.05,19.2,632141,20.46,-6.17,20.39,21.77,1.41
20260528,19.35,19.6,19.15,19.45,457510,20.38,-4.56,20.25,21.7,0.99
20260529,19.8,19.8,19.3,19.5,376736,20.31,-3.97,20.14,21.62,0.8
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.58
- over_600_ratio: 75.98
- over_800_ratio: 73.49
- over_1000_ratio: 70.48
- over_400_change_1w: 0.24
- over_800_change_1w: 0.07
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.49,,73.8,,70,,0,False,False
20260508,79.54,0.05,73.61,-0.19,70.05,0.05,1,False,True
20260515,79.34,-0.2,73.42,-0.19,70.39,0.34,2,False,True
20260522,79.58,0.24,73.49,0.07,70.48,0.09,3,True,True
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
