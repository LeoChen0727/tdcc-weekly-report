# INDIVIDUAL STOCK CHATGPT PACKET - 1227 佳格

## Metadata
- generated_at: 2026-05-28 20:18:12 Asia/Taipei
- stock_id: 1227
- stock_name: 佳格
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1227_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1227_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1227_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1227_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1227_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1227_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1227_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1227_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1227_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1227_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1227_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1227_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1227_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1227.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1227.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1227.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1227.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1227.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1227.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1227_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1227_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1227_latest.md?ref=main

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
- open: 28.1
- high: 28.1
- low: 27.9
- close: 27.9
- volume: 1345180
- ma5: 28.16
- ema23_primary: 28.67
- distance_to_ema23_pct: -2.68
- ma20: 28.57
- ma60: 29.5
- ma120: 29.74
- return_5d: -2.45
- return_20d: -4.45
- volume_ratio: 1.29
- distance_to_ma20_pct_auxiliary: -2.34
- distance_to_high_60_pct: -10.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,29.2,29.2,28.9,28.95,1248501,29.74,-2.67,29.93,29.75,1.21
20260504,29,29,28.75,28.95,1146529,29.68,-2.45,29.82,29.75,1.13
20260505,28.95,29,28.8,28.8,912987,29.6,-2.72,29.73,29.74,0.89
20260506,28.9,28.95,28.75,28.75,986091,29.53,-2.65,29.64,29.73,0.94
20260507,28.75,28.95,28.7,28.85,914854,29.48,-2.12,29.57,29.72,0.88
20260508,28.95,29.15,28.9,29.05,581438,29.44,-1.33,29.51,29.71,0.56
20260511,29.05,29.2,28.85,28.85,986493,29.39,-1.84,29.45,29.71,0.92
20260512,28.95,29.1,28.75,28.8,1196785,29.34,-1.85,29.39,29.71,1.09
20260513,28.85,28.85,28.7,28.8,1064312,29.3,-1.7,29.32,29.71,0.97
20260514,28.8,28.95,28.55,28.55,1327841,29.23,-2.34,29.26,29.71,1.18
20260515,28.6,28.65,28.45,28.5,899248,29.17,-2.31,29.19,29.7,0.79
20260518,28.5,28.55,28.3,28.3,882520,29.1,-2.75,29.07,29.69,0.83
20260519,28.35,28.6,28.35,28.5,472078,29.05,-1.9,28.98,29.69,0.47
20260520,28.5,28.5,28.1,28.3,1209899,28.99,-2.37,28.89,29.68,1.18
20260521,28.55,28.75,28.4,28.6,951268,28.96,-1.23,28.83,29.66,0.96
20260522,28.5,28.55,28.35,28.45,634178,28.91,-1.6,28.79,29.63,0.69
20260525,28.4,28.4,28.05,28.1,1416096,28.85,-2.59,28.73,29.6,1.51
20260526,28.1,28.45,28.05,28.25,927467,28.8,-1.9,28.69,29.57,1
20260527,28.25,28.25,28,28.1,1730442,28.74,-2.22,28.63,29.53,1.74
20260528,28.1,28.1,27.9,27.9,1345180,28.67,-2.68,28.57,29.5,1.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 67.45
- over_600_ratio: 65.97
- over_800_ratio: 65.37
- over_1000_ratio: 64.59
- over_400_change_1w: -0.05
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.6,,65.59,,64.9,,0,False,False
20260508,67.48,-0.12,65.49,-0.1,64.81,-0.09,0,False,False
20260515,67.5,0.02,65.45,-0.04,64.77,-0.04,1,False,False
20260522,67.45,-0.05,65.37,-0.08,64.59,-0.18,0,False,False
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
