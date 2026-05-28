# INDIVIDUAL STOCK CHATGPT PACKET - 8401 白紗科

## Metadata
- generated_at: 2026-05-28 20:20:37 Asia/Taipei
- stock_id: 8401
- stock_name: 白紗科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8401_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8401_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8401_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8401_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8401_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8401_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8401_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8401_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8401_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8401_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8401_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8401_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8401_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8401.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8401.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8401.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8401.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8401.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8401.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8401_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8401_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8401_latest.md?ref=main

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
- open: 24
- high: 24
- low: 23.15
- close: 23.2
- volume: 23000
- ma5: 22.97
- ema23_primary: 23.72
- distance_to_ema23_pct: -2.2
- ma20: 23.73
- ma60: 25.2
- ma120: 27.07
- return_5d: 0.87
- return_20d: -5.31
- volume_ratio: 0.38
- distance_to_ma20_pct_auxiliary: -2.23
- distance_to_high_60_pct: -20.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,24.5,24.5,24.3,24.45,37000,24.99,-2.16,24.68,26.89,0.65
20260504,24,25,24,24.75,77000,24.97,-0.88,24.67,26.81,1.3
20260505,24.7,24.7,24.45,24.6,30000,24.94,-1.36,24.65,26.74,0.51
20260506,24.6,24.65,24.4,24.45,66000,24.9,-1.8,24.63,26.66,1.07
20260507,24.45,24.55,24.2,24.4,58000,24.86,-1.83,24.6,26.58,0.92
20260508,24.4,24.4,24.15,24.2,62000,24.8,-2.42,24.57,26.51,0.98
20260511,24.25,24.25,24.1,24.2,101000,24.75,-2.23,24.53,26.43,1.57
20260512,24.25,24.25,24,24.05,92000,24.69,-2.6,24.5,26.34,1.37
20260513,24.05,24.05,23.8,23.8,118000,24.62,-3.32,24.45,26.25,1.68
20260514,24.75,24.75,23.85,24,44000,24.57,-2.31,24.4,26.17,0.62
20260515,24.4,24.4,23.85,23.95,66000,24.52,-2.31,24.34,26.09,0.91
20260518,23.7,23.9,23.3,23.7,84000,24.45,-3.06,24.29,26.01,1.11
20260519,23.7,23.7,23.1,23.2,133000,24.34,-4.7,24.22,25.91,1.72
20260520,23.1,23.2,22.8,23,63000,24.23,-5.08,24.14,25.81,0.82
20260521,23,23,22.8,23,69000,24.13,-4.68,24.07,25.72,0.91
20260522,23,23.05,22.85,22.9,23000,24.03,-4.69,24,25.61,0.32
20260525,23.15,23.45,23,23.05,23000,23.95,-3.74,23.94,25.51,0.35
20260526,22.95,23,22.85,22.95,23000,23.86,-3.82,23.87,25.41,0.38
20260527,22.9,22.9,22.7,22.75,23000,23.77,-4.29,23.8,25.3,0.38
20260528,24,24,23.15,23.2,23000,23.72,-2.2,23.73,25.2,0.38
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 62.52
- over_600_ratio: 59.97
- over_800_ratio: 58.09
- over_1000_ratio: 54.12
- over_400_change_1w: 0.16
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.09,,57.68,,53.73,,0,False,False
20260508,62.21,0.12,57.8,0.12,53.85,0.12,1,True,True
20260515,62.36,0.15,57.94,0.14,53.97,0.12,2,True,True
20260522,62.52,0.16,58.09,0.15,54.12,0.15,3,True,True
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
