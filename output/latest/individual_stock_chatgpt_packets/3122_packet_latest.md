# INDIVIDUAL STOCK CHATGPT PACKET - 3122 笙泉

## Metadata
- generated_at: 2026-05-29 19:32:26 Asia/Taipei
- stock_id: 3122
- stock_name: 笙泉
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3122_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3122_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3122_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3122_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3122_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3122_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3122_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3122_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3122_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3122_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3122_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3122_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3122_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3122.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3122.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3122.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3122.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3122.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3122.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3122_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3122_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3122_latest.md?ref=main

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
- open: 32.9
- high: 33
- low: 32
- close: 32.75
- volume: 33000
- ma5: 33.78
- ema23_primary: 34.18
- distance_to_ema23_pct: -4.18
- ma20: 35.89
- ma60: 30.03
- ma120: 26.6
- return_5d: -8.65
- return_20d: 0.15
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -8.76
- distance_to_high_60_pct: -22.58

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.35,33.35,31,32.4,670000,29.27,10.7,28.32,26.83,0.92
20260505,32.4,33,31.6,33,499000,29.58,11.56,28.74,26.98,0.66
20260506,33.9,36.3,33.3,36.3,1652000,30.14,20.44,29.32,27.14,1.98
20260507,37.5,39.9,37.5,39.9,3180000,30.95,28.9,30.06,27.32,3.22
20260508,42.25,42.3,38.9,40.2,2774000,31.72,26.72,30.82,27.56,2.47
20260511,40.05,40.15,38.2,38.5,2588000,32.29,19.24,31.5,27.79,2.07
20260512,38.15,41.6,37.55,38.9,1578000,32.84,18.45,32.19,28.03,1.19
20260513,38,38.85,37,37.4,754000,33.22,12.58,32.78,28.25,0.56
20260514,37.55,38.15,36.5,37.35,548000,33.56,11.28,33.36,28.46,0.4
20260515,38.5,39,36.25,36.8,720000,33.83,8.77,33.9,28.62,0.51
20260518,36.05,36.05,34.5,35.9,302000,34.01,5.57,34.4,28.8,0.21
20260519,36.3,36.8,35.1,35.55,299000,34.13,4.15,34.88,28.97,0.21
20260520,35.55,37.45,35.2,35.3,408000,34.23,3.12,35.23,29.13,0.29
20260521,36,36.85,35.2,35.6,486000,34.35,3.65,35.57,29.3,0.35
20260522,35.6,36.2,35.05,35.85,36000,34.47,4,35.86,29.46,0.03
20260525,36.25,36.8,35.75,35.8,36000,34.58,3.52,36,29.61,0.03
20260526,36,36,33.85,34.5,34000,34.57,-0.22,35.92,29.74,0.03
20260527,34.7,35.6,33.2,33.35,34000,34.47,-3.26,35.95,29.86,0.04
20260528,33.15,34.15,32.5,32.5,33000,34.31,-5.27,35.89,29.93,0.04
20260529,32.9,33,32,32.75,33000,34.18,-4.18,35.89,30.03,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 26.93
- over_600_ratio: 25.93
- over_800_ratio: 20.57
- over_1000_ratio: 16.08
- over_400_change_1w: 1.22
- over_800_change_1w: 2.06
- over_1000_change_1w: -0.34
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.04,,21.2,,19.19,,0,False,False
20260508,27.85,0.81,19.68,-1.52,19.68,0.49,1,False,True
20260515,25.71,-2.14,18.51,-1.17,16.42,-3.26,0,False,False
20260522,26.93,1.22,20.57,2.06,16.08,-0.34,1,False,True
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
