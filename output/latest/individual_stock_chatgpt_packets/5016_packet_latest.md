# INDIVIDUAL STOCK CHATGPT PACKET - 5016 松和

## Metadata
- generated_at: 2026-05-28 20:19:40 Asia/Taipei
- stock_id: 5016
- stock_name: 松和
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 130
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5016_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5016_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5016_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5016_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5016_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5016_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5016_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5016_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5016_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5016_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5016_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5016_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5016_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5016.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5016.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5016.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5016.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5016.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5016.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5016_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5016_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5016_latest.md?ref=main

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
- open: 25.85
- high: 26.1
- low: 25.4
- close: 25.65
- volume: 26000
- ma5: 26.21
- ema23_primary: 26.02
- distance_to_ema23_pct: -1.42
- ma20: 25.55
- ma60: 26.65
- ma120: 25.85
- return_5d: 3.01
- return_20d: -2.47
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: 0.37
- distance_to_high_60_pct: -25.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,26.3,26.55,25.95,26,82000,27.67,-6.03,29.08,26.53,0.15
20260504,26.05,26.05,25.65,25.75,66000,27.51,-6.4,28.8,26.54,0.13
20260505,25.8,26.2,25.5,25.75,104000,27.36,-5.89,28.52,26.55,0.24
20260506,25.8,25.95,25.65,25.65,44000,27.22,-5.77,28.26,26.55,0.11
20260507,25.95,25.95,25.45,25.55,46000,27.08,-5.65,27.97,26.56,0.13
20260508,26,26,25.35,25.55,34000,26.95,-5.21,27.67,26.56,0.1
20260511,25.5,25.5,25.2,25.3,60000,26.82,-5.65,27.32,26.56,0.19
20260512,25.15,25.7,24.85,25.1,78000,26.67,-5.9,27.07,26.56,0.26
20260513,25,25.75,24.7,25.45,88000,26.57,-4.22,26.91,26.57,0.31
20260514,25.95,25.95,25.3,25.45,53000,26.48,-3.88,26.63,26.58,0.25
20260515,25.1,25.2,24.6,25,102000,26.35,-5.14,26.32,26.58,0.62
20260518,25.3,25.3,24.85,24.9,24000,26.23,-5.08,26.04,26.57,0.16
20260519,24.9,25.3,24.8,24.9,32000,26.12,-4.68,25.81,26.57,0.22
20260520,25.2,25.2,24.5,24.8,45000,26.01,-4.66,25.63,26.56,0.35
20260521,25.1,25.15,24.8,24.9,27000,25.92,-3.93,25.52,26.55,0.25
20260522,24.9,25.15,24.9,25.1,25000,25.85,-2.9,25.47,26.55,0.33
20260525,25.4,27.35,25,27.35,26000,25.98,5.29,25.53,26.59,0.37
20260526,28.15,28.95,26.65,26.85,28000,26.05,3.08,25.59,26.62,0.46
20260527,26.85,26.85,25.8,26.1,26000,26.05,0.18,25.59,26.64,0.47
20260528,25.85,26.1,25.4,25.65,26000,26.02,-1.42,25.55,26.65,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.83
- over_600_ratio: 61.59
- over_800_ratio: 61.59
- over_1000_ratio: 59.98
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.86,,61.62,,60.01,,0,False,False
20260508,65.85,-0.01,61.61,-0.01,60,-0.01,0,False,False
20260515,65.84,-0.01,61.6,-0.01,59.99,-0.01,0,False,False
20260522,65.83,-0.01,61.59,-0.01,59.98,-0.01,0,False,False
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
