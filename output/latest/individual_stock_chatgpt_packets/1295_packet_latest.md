# INDIVIDUAL STOCK CHATGPT PACKET - 1295 生合

## Metadata
- generated_at: 2026-05-27 21:26:06 Asia/Taipei
- stock_id: 1295
- stock_name: 生合
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1295_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1295_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1295_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1295_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1295_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1295_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1295_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1295_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1295_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1295_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1295_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1295_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1295_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1295.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1295.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1295.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1295.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1295.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1295.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1295_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1295_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1295_latest.md?ref=main

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
- open: 51.4
- high: 51.4
- low: 50.1
- close: 50.3
- volume: 51000
- ma5: 50.98
- ema23_primary: 53.64
- distance_to_ema23_pct: -6.23
- ma20: 52.7
- ma60: 61.53
- ma120: 73.84
- return_5d: -2.14
- return_20d: -12.22
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: -4.55
- distance_to_high_60_pct: -35.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,57.3,57.5,56.8,57.2,40000,61.38,-6.8,60.02,70.43,0.58
20260430,57.2,57.2,55,55,207000,60.85,-9.61,59.58,69.91,2.72
20260504,55.1,55.1,53.2,53.6,157000,60.24,-11.02,59.02,69.37,1.91
20260505,53.3,56.7,53.1,55.2,146000,59.82,-7.73,58.57,68.82,1.65
20260506,55.2,55.2,53.8,55.2,83000,59.44,-7.13,58.34,68.29,0.99
20260507,55,56.8,54.6,56,77000,59.15,-5.33,58.05,67.8,0.94
20260508,55.5,55.5,52.6,54.1,102000,58.73,-7.88,57.73,67.31,1.2
20260511,54.1,54.2,53.4,53.7,83000,58.31,-7.91,57.41,66.85,0.95
20260512,53.4,53.4,50.8,51,208000,57.7,-11.61,57.05,66.37,2.32
20260513,51,52.5,51,52,98000,57.23,-9.13,56.68,65.91,1.07
20260514,51.1,51.6,50.5,50.9,72000,56.7,-10.23,56.26,65.44,0.78
20260515,51.1,51.5,50.6,50.6,44000,56.19,-9.95,55.79,64.98,0.47
20260518,50.6,52.2,49.9,52.2,91000,55.86,-6.55,55.44,64.59,0.96
20260519,52.2,52.3,50.8,51,57000,55.45,-8.03,54.9,64.18,0.6
20260520,50.9,51.5,50.7,51.4,37000,55.12,-6.74,54.49,63.78,0.4
20260521,50.2,51.5,50.2,51,55000,54.77,-6.89,54.03,63.35,0.61
20260522,51,52,51,51.9,52000,54.53,-4.83,53.7,62.92,0.6
20260525,52.1,52.1,50.2,50.3,51000,54.18,-7.16,53.33,62.45,0.59
20260526,51.7,51.7,50.9,51.4,51000,53.95,-4.72,53.05,62.01,0.59
20260527,51.4,51.4,50.1,50.3,51000,53.64,-6.23,52.7,61.53,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.57
- over_600_ratio: 53.06
- over_800_ratio: 46.68
- over_1000_ratio: 44.11
- over_400_change_1w: -0.04
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.35,,46.5,,41.04,,0,False,False
20260508,55.63,0.28,46.73,0.23,44.16,3.12,1,True,True
20260515,55.61,-0.02,46.71,-0.02,44.14,-0.02,0,False,False
20260522,55.57,-0.04,46.68,-0.03,44.11,-0.03,0,False,False
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
