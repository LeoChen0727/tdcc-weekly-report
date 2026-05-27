# INDIVIDUAL STOCK CHATGPT PACKET - 2901 欣欣

## Metadata
- generated_at: 2026-05-27 21:26:49 Asia/Taipei
- stock_id: 2901
- stock_name: 欣欣
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2901_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2901_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2901_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2901_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2901_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2901_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2901_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2901_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2901_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2901_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2901_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2901_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2901_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2901.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2901.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2901.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2901.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2901.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2901.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2901_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2901_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2901_latest.md?ref=main

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
- open: 22.95
- high: 23.55
- low: 22.45
- close: 22.45
- volume: 33591
- ma5: 22.71
- ema23_primary: 23.1
- distance_to_ema23_pct: -2.82
- ma20: 23.3
- ma60: 23.5
- ma120: 24.1
- return_5d: -1.1
- return_20d: -4.47
- volume_ratio: 1.06
- distance_to_ma20_pct_auxiliary: -3.64
- distance_to_high_60_pct: -10.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,23.8,24.2,23.4,24.2,58245,23.51,2.92,23.49,23.89,1.34
20260430,24.2,24.3,23.95,24,23607,23.55,1.89,23.5,23.88,0.54
20260504,23.95,24.95,23.9,24.95,152829,23.67,5.41,23.59,23.89,3.17
20260505,24.8,24.8,24,24,20344,23.7,1.28,23.62,23.88,0.43
20260506,24.55,24.55,24,24.4,22446,23.76,2.71,23.67,23.87,0.47
20260507,23.8,23.8,23.35,23.6,23885,23.74,-0.6,23.66,23.85,0.51
20260508,23.6,23.65,23.6,23.65,15047,23.74,-0.36,23.66,23.84,0.33
20260511,23.45,23.85,23.4,23.45,22734,23.71,-1.1,23.64,23.82,0.5
20260512,23.45,23.45,22.9,23,26879,23.65,-2.76,23.59,23.79,0.58
20260513,23.3,23.5,23.25,23.35,29239,23.63,-1.17,23.58,23.77,0.65
20260514,23.35,23.35,22.9,22.9,49659,23.57,-2.83,23.54,23.74,1.11
20260515,23.05,23.05,22.85,22.9,13644,23.51,-2.6,23.51,23.71,0.32
20260518,22.8,22.9,22.55,22.6,36912,23.44,-3.56,23.46,23.68,0.86
20260519,22.95,22.95,22.5,22.7,13286,23.37,-2.88,23.42,23.65,0.32
20260520,22.55,22.7,22.45,22.7,12087,23.32,-2.65,23.38,23.62,0.31
20260521,22.7,22.7,22.5,22.55,18617,23.25,-3.03,23.34,23.59,0.5
20260522,22.55,22.65,22.55,22.6,16511,23.2,-2.58,23.34,23.57,0.47
20260525,22.95,23.7,22.95,23.3,16767,23.21,0.4,23.36,23.55,0.49
20260526,23.25,23.25,22.6,22.65,24988,23.16,-2.21,23.35,23.52,0.77
20260527,22.95,23.55,22.45,22.45,33591,23.1,-2.82,23.3,23.5,1.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.31
- over_600_ratio: 74
- over_800_ratio: 72.92
- over_1000_ratio: 71.68
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.29,,72.88,,71.64,,0,False,False
20260508,79.3,0.01,72.89,0.01,71.65,0.01,1,True,True
20260515,79.29,-0.01,72.9,0.01,71.66,0.01,2,False,True
20260522,79.31,0.02,72.92,0.02,71.68,0.02,3,True,True
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
