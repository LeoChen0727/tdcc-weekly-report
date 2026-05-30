# INDIVIDUAL STOCK CHATGPT PACKET - 4545 銘鈺

## Metadata
- generated_at: 2026-05-30 23:42:23 Asia/Taipei
- stock_id: 4545
- stock_name: 銘鈺
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4545_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4545_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4545_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4545_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4545_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4545_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4545_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4545_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4545_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4545_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4545_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4545_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4545_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4545.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4545.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4545.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4545.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4545.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4545.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4545_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4545_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4545_latest.md?ref=main

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
- open: 38.9
- high: 39.15
- low: 38.1
- close: 38.5
- volume: 543037
- ma5: 35.94
- ema23_primary: 32.64
- distance_to_ema23_pct: 17.97
- ma20: 31.81
- ma60: 31.5
- ma120: 33.83
- return_5d: 15.96
- return_20d: 27.48
- volume_ratio: 1.52
- distance_to_ma20_pct_auxiliary: 21.04
- distance_to_high_60_pct: -3.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,30.35,31.15,30.15,30.25,105434,30.8,-1.77,30.63,32.52,0.66
20260505,30.3,30.75,30.3,30.65,63047,30.78,-0.44,30.66,32.41,0.4
20260506,31.95,31.95,29.2,29.85,227158,30.71,-2.79,30.66,32.31,1.39
20260507,29.95,31,29.9,30.65,177162,30.7,-0.17,30.61,32.21,1.08
20260508,31.35,31.35,30.05,30.05,128254,30.65,-1.95,30.57,32.09,0.77
20260511,30.65,30.8,30.15,30.65,157172,30.65,0.01,30.55,31.99,0.95
20260512,30.6,30.6,29.85,29.95,149150,30.59,-2.09,30.49,31.92,0.89
20260513,29.95,30.05,29.7,29.9,98583,30.53,-2.07,30.43,31.85,0.6
20260514,30,30,29.5,29.95,156216,30.48,-1.75,30.37,31.76,0.95
20260515,29.95,30,29,29,168417,30.36,-4.48,30.24,31.67,1.02
20260518,28.4,31.25,28.4,29.05,126386,30.25,-3.97,30.12,31.61,0.78
20260519,29,31.95,29,31.45,559832,30.35,3.62,30.16,31.57,3.11
20260520,31.75,32,30.1,30.1,353303,30.33,-0.76,30.12,31.52,1.84
20260521,30.85,32.4,30.75,31.75,380101,30.45,4.28,30.17,31.49,1.86
20260522,32.9,34,32.15,33.2,599376,30.68,8.22,30.34,31.45,2.69
20260525,34.2,34.2,32.8,32.85,320091,30.86,6.45,30.5,31.4,1.37
20260526,33,33.2,32.5,33.2,225711,31.05,6.91,30.68,31.36,0.96
20260527,33.35,36.5,33.35,36.5,720514,31.51,15.85,31.01,31.38,2.7
20260528,37.6,40.1,37.1,38.65,1908918,32.1,20.39,31.39,31.44,5.63
20260529,38.9,39.15,38.1,38.5,543037,32.64,17.97,31.81,31.5,1.52
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 73.18
- over_600_ratio: 71.95
- over_800_ratio: 70.93
- over_1000_ratio: 70.93
- over_400_change_1w: -0.09
- over_800_change_1w: -0.09
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,73.37,,71.12,,71.12,,0,False,False
20260508,73.37,0,71.12,0,71.12,0,0,False,False
20260515,73.37,0,71.12,0,71.12,0,0,False,False
20260522,73.27,-0.1,71.02,-0.1,71.02,-0.1,0,False,False
20260529,73.18,-0.09,70.93,-0.09,70.93,-0.09,0,False,False
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
