# INDIVIDUAL STOCK CHATGPT PACKET - 6228 全譜

## Metadata
- generated_at: 2026-05-27 21:27:55 Asia/Taipei
- stock_id: 6228
- stock_name: 全譜
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 131
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6228_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6228_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6228_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6228_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6228_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6228_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6228_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6228_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6228_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6228_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6228_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6228_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6228_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6228.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6228.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6228.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6228.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6228.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6228.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6228_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6228_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6228_latest.md?ref=main

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
- open: 21.05
- high: 21.05
- low: 20.95
- close: 20.95
- volume: 21000
- ma5: 21.5
- ema23_primary: 22.4
- distance_to_ema23_pct: -6.49
- ma20: 22.37
- ma60: 23.63
- ma120: 24.7
- return_5d: -3.01
- return_20d: -11.97
- volume_ratio: 1.09
- distance_to_ma20_pct_auxiliary: -6.35
- distance_to_high_60_pct: -19.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,23.5,24.3,23.05,24.3,5000,24.34,-0.17,24.25,24.63,0.63
20260429,24.3,24.75,23.55,23.75,6000,24.29,-2.23,24.22,24.59,0.75
20260430,23.75,23.8,23,23.75,10000,24.25,-2.05,24.19,24.56,1.18
20260504,23.7,24.3,23.7,24.3,3000,24.25,0.2,24.19,24.53,0.37
20260506,24.45,24.45,23.25,23.3,22000,24.17,-3.61,24.19,24.5,2.42
20260507,22.2,23.3,22.05,22.4,9000,24.02,-6.76,24.14,24.43,0.95
20260508,22.4,23.45,22.4,22.45,14000,23.89,-6.04,24.09,24.38,1.42
20260511,22.5,22.5,22.1,22.1,16000,23.74,-6.92,24,24.32,1.64
20260512,22,22,21.4,21.55,12000,23.56,-8.53,23.88,24.26,1.18
20260513,21.45,21.45,20.65,20.65,29000,23.32,-11.44,23.73,24.19,2.58
20260514,20.65,22.7,20.65,22.7,69000,23.27,-2.44,23.61,24.16,4.98
20260515,22.7,22.7,20.5,22.45,73000,23.2,-3.23,23.48,24.12,4.38
20260518,22.3,22.3,21.6,22.3,4000,23.12,-3.56,23.33,24.08,0.24
20260519,22.3,22.3,20.5,22.3,15000,23.05,-3.27,23.19,24.04,0.87
20260520,21.35,22.3,21.35,21.6,8000,22.93,-5.82,23.07,23.98,0.46
20260521,22.85,22.85,21.4,22.6,5000,22.91,-1.34,22.98,23.94,0.29
20260522,22.95,22.95,21.65,21.85,22000,22.82,-4.24,22.85,23.87,1.26
20260525,21.1,21.15,21,21.05,21000,22.67,-7.15,22.68,23.78,1.21
20260526,21.3,21.3,21.05,21.05,21000,22.54,-6.59,22.51,23.7,1.14
20260527,21.05,21.05,20.95,20.95,21000,22.4,-6.49,22.37,23.63,1.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.44
- over_600_ratio: 78.44
- over_800_ratio: 75.5
- over_1000_ratio: 75.5
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
20260430,80.44,,75.5,,75.5,,0,False,False
20260508,80.44,0,75.5,0,75.5,0,0,False,False
20260515,80.44,0,75.5,0,75.5,0,0,False,False
20260522,80.44,0,75.5,0,75.5,0,0,False,False
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
