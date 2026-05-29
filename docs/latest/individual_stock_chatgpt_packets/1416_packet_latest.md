# INDIVIDUAL STOCK CHATGPT PACKET - 1416 廣豐

## Metadata
- generated_at: 2026-05-29 19:31:38 Asia/Taipei
- stock_id: 1416
- stock_name: 廣豐
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1416_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1416_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1416_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1416_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1416_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1416.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1416.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1416.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1416.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1416_latest.md?ref=main

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
- open: 11.05
- high: 11.15
- low: 11.05
- close: 11.1
- volume: 228604
- ma5: 11.11
- ema23_primary: 11.21
- distance_to_ema23_pct: -1.02
- ma20: 11.19
- ma60: 11.43
- ma120: 11.6
- return_5d: -0.45
- return_20d: -2.63
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -0.78
- distance_to_high_60_pct: -5.53

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,11.45,11.45,11.35,11.35,139509,11.51,-1.39,11.52,11.61,0.77
20260505,11.35,11.4,11.3,11.35,120261,11.5,-1.27,11.52,11.6,0.66
20260506,11.3,11.4,11.3,11.35,169225,11.48,-1.17,11.52,11.59,0.92
20260507,11.35,11.4,11.3,11.3,232094,11.47,-1.47,11.51,11.59,1.27
20260508,11.4,11.4,11.25,11.3,169570,11.45,-1.35,11.49,11.58,0.9
20260511,11.35,11.35,11.25,11.3,132694,11.44,-1.24,11.48,11.57,0.71
20260512,11.3,11.35,11.2,11.2,153053,11.42,-1.94,11.46,11.56,0.85
20260513,11.25,11.3,11.15,11.25,243409,11.41,-1.38,11.44,11.55,1.36
20260514,11.3,11.35,11.2,11.25,370156,11.39,-1.27,11.42,11.54,1.99
20260515,11.25,11.25,11.05,11.1,420735,11.37,-2.37,11.39,11.53,2.13
20260518,11.1,11.1,11,11.05,199791,11.34,-2.58,11.36,11.52,0.98
20260519,11.1,11.1,10.95,11.05,293739,11.32,-2.37,11.33,11.51,1.38
20260520,11,11.1,11,11.1,143485,11.3,-1.77,11.31,11.5,0.68
20260521,11.15,11.15,11.05,11.1,187723,11.28,-1.63,11.29,11.49,0.93
20260522,11.15,11.15,11,11.15,265409,11.27,-1.09,11.27,11.48,1.28
20260525,11.15,11.2,11.05,11.15,336530,11.26,-1,11.26,11.47,1.56
20260526,11.15,11.15,11.05,11.15,421327,11.25,-0.92,11.24,11.46,1.85
20260527,11.1,11.15,11,11.1,361560,11.24,-1.25,11.22,11.45,1.53
20260528,11.1,11.15,11,11.05,199411,11.22,-1.55,11.2,11.44,0.84
20260529,11.05,11.15,11.05,11.1,228604,11.21,-1.02,11.19,11.43,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.9
- over_600_ratio: 52.24
- over_800_ratio: 50.11
- over_1000_ratio: 48.67
- over_400_change_1w: -0.33
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.6,,50.15,,48.75,,0,False,False
20260508,55.55,-0.05,50.15,0,48.75,0,0,False,False
20260515,55.23,-0.32,50.14,-0.01,48.73,-0.02,0,False,False
20260522,54.9,-0.33,50.11,-0.03,48.67,-0.06,0,False,False
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
