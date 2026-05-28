# INDIVIDUAL STOCK CHATGPT PACKET - 4121 優盛

## Metadata
- generated_at: 2026-05-28 19:32:37 Asia/Taipei
- stock_id: 4121
- stock_name: 優盛
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4121_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4121_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4121_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4121_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4121_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4121_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4121_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4121_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4121_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4121_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4121_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4121_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4121_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4121.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4121.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4121.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4121.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4121.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4121.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4121_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4121_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4121_latest.md?ref=main

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
- open: 14.05
- high: 14.25
- low: 13.95
- close: 14.15
- volume: 145295
- ma5: 14.34
- ema23_primary: 14.47
- distance_to_ema23_pct: -2.2
- ma20: 14.29
- ma60: 15.96
- ma120: 16.12
- return_5d: -0.7
- return_20d: -5.35
- volume_ratio: 1.36
- distance_to_ma20_pct_auxiliary: -1
- distance_to_high_60_pct: -31.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,14.85,15.15,14.7,14.7,171000,15.44,-4.79,15.17,17.33,0.95
20260504,14.7,14.8,14.5,14.55,79000,15.37,-5.31,15.1,17.29,0.45
20260505,14.6,14.95,14.45,14.65,118000,15.31,-4.28,15.05,17.25,0.71
20260506,14.6,14.6,14.35,14.35,144000,15.23,-5.75,15,17.18,0.88
20260507,14.35,14.55,14.35,14.55,58000,15.17,-4.08,14.96,17.1,0.37
20260508,14.6,15.1,14.6,14.65,157000,15.13,-3.15,14.92,17.02,0.98
20260511,14.65,14.7,14.5,14.6,68000,15.08,-3.2,14.88,16.96,0.43
20260512,14.7,14.7,14.2,14.25,201000,15.01,-5.08,14.82,16.88,1.22
20260513,14.2,14.3,14.15,14.15,149000,14.94,-5.3,14.76,16.8,0.88
20260514,14.2,14.3,13.8,13.85,285000,14.85,-6.74,14.67,16.72,1.72
20260515,13.95,13.95,13.7,13.7,95000,14.75,-7.15,14.58,16.64,0.58
20260518,13.7,13.9,13.55,13.75,91000,14.67,-6.28,14.49,16.58,0.56
20260519,13.85,14.15,13.8,14,166000,14.61,-4.21,14.43,16.52,1.03
20260520,14,14.4,13.95,14.15,76000,14.58,-2.92,14.38,16.47,0.49
20260521,14.15,14.55,14.15,14.25,76000,14.55,-2.05,14.35,16.42,0.51
20260522,14.2,14.4,14.1,14.4,14000,14.54,-0.94,14.34,16.34,0.1
20260525,14.4,15.5,14.2,14.7,15000,14.55,1.03,14.36,16.25,0.12
20260526,14.7,14.75,14.4,14.4,15000,14.54,-0.95,14.36,16.16,0.13
20260527,14.5,14.5,14,14.05,14000,14.5,-3.08,14.33,16.06,0.13
20260528,14.05,14.25,13.95,14.15,145295,14.47,-2.2,14.29,15.96,1.36
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.43
- over_600_ratio: 46.41
- over_800_ratio: 45.68
- over_1000_ratio: 43.6
- over_400_change_1w: -0.01
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.2,,45.33,,43.26,,0,False,False
20260508,49.3,0.1,45.42,0.09,43.35,0.09,1,True,True
20260515,49.44,0.14,45.57,0.15,43.49,0.14,2,True,True
20260522,49.43,-0.01,45.68,0.11,43.6,0.11,3,False,True
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
