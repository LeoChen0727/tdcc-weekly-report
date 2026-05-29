# INDIVIDUAL STOCK CHATGPT PACKET - 4541 晟田

## Metadata
- generated_at: 2026-05-29 19:32:52 Asia/Taipei
- stock_id: 4541
- stock_name: 晟田
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4541_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4541_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4541_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4541_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4541_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4541_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4541_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4541_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4541_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4541_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4541_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4541_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4541_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4541.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4541.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4541.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4541.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4541.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4541.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4541_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4541_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4541_latest.md?ref=main

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
- open: 45.7
- high: 46.5
- low: 44.9
- close: 45.25
- volume: 46000
- ma5: 44.42
- ema23_primary: 45.04
- distance_to_ema23_pct: 0.46
- ma20: 45.52
- ma60: 44.39
- ma120: 44.18
- return_5d: 2.14
- return_20d: -2.37
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: -0.59
- distance_to_high_60_pct: -12.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,46.55,48.45,46.55,47.85,858000,46.07,3.87,46.27,44.21,0.66
20260505,47.85,51.8,47.3,51.7,2950000,46.54,11.09,46.81,44.27,2.05
20260506,51.7,51.7,48.1,48.7,2592000,46.72,4.24,47.21,44.3,1.67
20260507,49,50.9,48.5,50.2,1481000,47.01,6.79,47.65,44.36,0.93
20260508,49.4,50.7,47.8,47.95,2181000,47.09,1.83,47.78,44.39,1.36
20260511,48,48,44.4,45.7,1794000,46.97,-2.71,47.83,44.43,1.09
20260512,45.75,45.8,44.85,45,1008000,46.81,-3.86,47.76,44.47,0.62
20260513,44.95,45.35,43.85,43.85,1176000,46.56,-5.82,47.63,44.48,0.72
20260514,44.25,45.05,43.2,44.15,786000,46.36,-4.77,47.52,44.48,0.49
20260515,45.55,46.55,44.05,44.1,1799000,46.17,-4.49,47.32,44.5,1.21
20260518,44,44.35,43.35,44.05,582000,45.99,-4.23,47.11,44.54,0.4
20260519,44.6,44.6,43.5,43.5,446000,45.79,-4.99,46.81,44.55,0.34
20260520,43.7,44.3,43.15,43.15,615000,45.57,-5.3,46.54,44.55,0.49
20260521,43.6,44.35,43.5,44.1,478000,45.44,-2.96,46.27,44.55,0.4
20260522,44.45,44.45,43.75,44.3,44000,45.35,-2.31,46.1,44.52,0.04
20260525,44.65,44.8,43.6,44.1,44000,45.25,-2.53,45.93,44.48,0.04
20260526,44.35,44.6,43.45,43.75,44000,45.12,-3.04,45.79,44.45,0.04
20260527,44,44.2,43.3,44.2,44000,45.04,-1.87,45.65,44.4,0.04
20260528,45.1,45.25,43.5,44.8,45000,45.02,-0.5,45.58,44.39,0.05
20260529,45.7,46.5,44.9,45.25,46000,45.04,0.46,45.52,44.39,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 33.8
- over_600_ratio: 29.97
- over_800_ratio: 27.8
- over_1000_ratio: 25.31
- over_400_change_1w: -2.02
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.14,,28.33,,27.08,,0,False,False
20260508,38.29,0.15,29.34,1.01,26.77,-0.31,1,False,True
20260515,35.82,-2.47,27.88,-1.46,25.32,-1.45,0,False,False
20260522,33.8,-2.02,27.8,-0.08,25.31,-0.01,0,False,False
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
