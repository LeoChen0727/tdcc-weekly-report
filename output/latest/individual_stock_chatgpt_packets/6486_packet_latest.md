# INDIVIDUAL STOCK CHATGPT PACKET - 6486 互動

## Metadata
- generated_at: 2026-05-28 19:33:19 Asia/Taipei
- stock_id: 6486
- stock_name: 互動
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6486_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6486_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6486_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6486_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6486_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6486_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6486_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6486_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6486_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6486_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6486_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6486_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6486_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6486.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6486.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6486.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6486.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6486.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6486.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6486_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6486_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6486_latest.md?ref=main

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
- open: 80.8
- high: 81.5
- low: 80.3
- close: 81
- volume: 83965
- ma5: 81.42
- ema23_primary: 82.85
- distance_to_ema23_pct: -2.24
- ma20: 82.61
- ma60: 84.97
- ma120: 83.31
- return_5d: -0.74
- return_20d: -4.93
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: -1.94
- distance_to_high_60_pct: -10.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,86,86,84.6,84.7,228000,86.56,-2.14,87.08,84.66,0.76
20260504,84.8,85.4,84.5,84.6,151000,86.39,-2.08,87,84.69,0.5
20260505,84.1,85.2,84,85.1,81000,86.29,-1.37,87,84.7,0.29
20260506,84.8,85,84.2,84.8,208000,86.16,-1.58,86.94,84.72,0.72
20260507,84.8,84.8,84.1,84.1,225000,85.99,-2.2,86.79,84.75,0.78
20260508,84,84.2,83.3,83.3,209000,85.77,-2.87,86.62,84.8,0.72
20260511,83.4,84.3,82.9,83.3,118000,85.56,-2.64,86.42,84.87,0.41
20260512,83.2,83.3,82.1,82.6,228000,85.31,-3.18,86.1,84.93,0.84
20260513,82.6,82.6,81.8,82.4,109000,85.07,-3.14,85.89,84.98,0.43
20260514,82.5,83.4,82.3,83.1,105000,84.91,-2.13,85.69,85.05,0.41
20260515,82.9,83.1,82,82,165000,84.66,-3.15,85.37,85.08,0.66
20260518,80.5,81.7,80.1,81.2,360000,84.38,-3.76,85.02,85.1,1.38
20260519,81.3,81.9,81,81,79000,84.09,-3.68,84.67,85.14,0.31
20260520,81,81.5,81,81.2,26000,83.85,-3.16,84.33,85.17,0.1
20260521,81.2,81.9,81.2,81.6,92000,83.67,-2.47,83.98,85.22,0.38
20260522,82.3,82.4,81.6,82.1,82000,83.53,-1.72,83.73,85.21,0.35
20260525,82.1,82.2,81.3,81.9,82000,83.4,-1.8,83.31,85.18,0.42
20260526,81.6,81.7,81,81.3,81000,83.22,-2.31,83.06,85.13,0.55
20260527,81.4,81.4,80.6,80.8,81000,83.02,-2.68,82.81,85.06,0.57
20260528,80.8,81.5,80.3,81,83965,82.85,-2.24,82.61,84.97,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.9
- over_600_ratio: 42.9
- over_800_ratio: 40.28
- over_1000_ratio: 40.28
- over_400_change_1w: 0.02
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.88,,40.28,,40.28,,0,False,False
20260508,42.88,0,40.28,0,40.28,0,0,False,False
20260515,42.88,0,40.28,0,40.28,0,0,False,False
20260522,42.9,0.02,40.28,0,40.28,0,1,False,False
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
