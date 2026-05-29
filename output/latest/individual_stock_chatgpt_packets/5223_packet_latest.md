# INDIVIDUAL STOCK CHATGPT PACKET - 5223 安力-KY

## Metadata
- generated_at: 2026-05-29 19:33:03 Asia/Taipei
- stock_id: 5223
- stock_name: 安力-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5223_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5223_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5223_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5223_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5223_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5223_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5223_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5223_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5223_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5223_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5223_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5223_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5223_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5223.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5223.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5223.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5223.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5223.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5223.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5223_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5223_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5223_latest.md?ref=main

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
- open: 24.5
- high: 25.25
- low: 24.5
- close: 24.7
- volume: 25000
- ma5: 25.42
- ema23_primary: 25.03
- distance_to_ema23_pct: -1.31
- ma20: 24.76
- ma60: 26.38
- ma120: 27.39
- return_5d: 2.7
- return_20d: -1.79
- volume_ratio: 0.87
- distance_to_ma20_pct_auxiliary: -0.25
- distance_to_high_60_pct: -21.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,25,25.15,24.9,25.15,49000,26.01,-3.3,25.71,27.63,1.37
20260505,25.05,25.45,25.05,25.25,16000,25.95,-2.68,25.65,27.57,0.45
20260506,25.2,25.25,25,25,53000,25.87,-3.35,25.57,27.52,1.39
20260507,24.95,25,24.45,24.7,56000,25.77,-4.15,25.51,27.45,1.41
20260508,24.7,24.75,24.5,24.75,17000,25.68,-3.64,25.44,27.39,0.44
20260511,24.7,24.75,24.05,24.75,16000,25.61,-3.35,25.39,27.34,0.42
20260512,25,25,24.7,24.8,6000,25.54,-2.9,25.39,27.29,0.17
20260513,24.8,24.95,24.5,24.9,19000,25.49,-2.3,25.39,27.23,0.53
20260514,24.65,24.7,24.45,24.5,24000,25.4,-3.56,25.37,27.17,0.68
20260515,24.55,24.75,23.95,24.15,29000,25.3,-4.54,25.26,27.11,0.92
20260518,24.7,24.7,23.75,24.1,13000,25.2,-4.36,25.14,27.04,0.44
20260519,24.4,24.7,24.15,24.15,25000,25.11,-3.83,25.01,26.97,0.88
20260520,24.6,24.6,23.8,23.95,52000,25.02,-4.26,24.9,26.89,1.85
20260521,24,24.1,23.8,23.95,52000,24.93,-3.92,24.79,26.82,1.83
20260522,23.95,24.3,23.95,24.05,24000,24.85,-3.23,24.73,26.75,0.83
20260525,24.05,26.45,23.5,26.15,25000,24.96,4.76,24.75,26.7,0.86
20260526,26.2,27.1,25.7,26.05,26000,25.05,3.98,24.79,26.64,0.9
20260527,26.35,26.45,25.5,25.5,26000,25.09,1.64,24.81,26.56,0.94
20260528,25.45,25.5,24.7,24.7,25000,25.06,-1.42,24.79,26.47,0.88
20260529,24.5,25.25,24.5,24.7,25000,25.03,-1.31,24.76,26.38,0.87
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.1
- over_600_ratio: 61.06
- over_800_ratio: 56.33
- over_1000_ratio: 54.12
- over_400_change_1w: 0.03
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.03,,56.3,,54.09,,0,False,False
20260508,63.05,0.02,56.32,0.02,54.11,0.02,1,True,True
20260515,63.07,0.02,56.33,0.01,54.12,0.01,2,True,True
20260522,63.1,0.03,56.33,0,54.12,0,3,False,False
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
