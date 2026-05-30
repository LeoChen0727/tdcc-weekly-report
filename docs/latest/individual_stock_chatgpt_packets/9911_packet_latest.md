# INDIVIDUAL STOCK CHATGPT PACKET - 9911 櫻花

## Metadata
- generated_at: 2026-05-30 23:44:03 Asia/Taipei
- stock_id: 9911
- stock_name: 櫻花
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9911_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9911_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9911_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9911_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9911_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9911_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9911_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9911_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9911_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9911_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9911_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9911_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9911_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9911.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9911.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9911.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9911.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9911.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9911.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9911_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9911_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9911_latest.md?ref=main

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
- open: 82.5
- high: 82.5
- low: 81.6
- close: 82
- volume: 203873
- ma5: 81.92
- ema23_primary: 82.73
- distance_to_ema23_pct: -0.88
- ma20: 82.63
- ma60: 85.41
- ma120: 84.83
- return_5d: -0.85
- return_20d: -1.44
- volume_ratio: 0.71
- distance_to_ma20_pct_auxiliary: -0.76
- distance_to_high_60_pct: -11.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,83.2,83.4,82.2,82.6,305434,84.07,-1.75,83.57,86.21,0.87
20260505,82.6,83,82.4,82.8,191191,83.96,-1.38,83.48,86.19,0.56
20260506,83.1,83.6,82.9,83.3,347109,83.91,-0.72,83.38,86.17,1.04
20260507,83.1,83.6,83,83.6,385345,83.88,-0.34,83.33,86.17,1.17
20260508,83.6,83.7,83,83.2,264735,83.82,-0.75,83.26,86.16,0.8
20260511,83.9,84.3,83,84.2,410515,83.86,0.41,83.23,86.17,1.19
20260512,84.2,84.3,82.5,82.5,406843,83.74,-1.48,83.11,86.16,1.15
20260513,83.4,83.4,82.6,83,257984,83.68,-0.81,83.02,86.16,0.73
20260514,83,83.1,82.5,82.5,192167,83.58,-1.3,82.91,86.13,0.55
20260515,82.8,83.1,82.4,82.4,164761,83.48,-1.3,82.82,86.08,0.47
20260518,82.4,82.8,82,82.2,181131,83.38,-1.41,82.74,86.04,0.54
20260519,82.6,83.1,82.3,82.3,167641,83.29,-1.19,82.7,86,0.51
20260520,83,83,82.1,82.8,185098,83.25,-0.54,82.68,85.96,0.58
20260521,82.9,83.2,82.6,82.9,234083,83.22,-0.38,82.68,85.91,0.77
20260522,82.5,82.9,82.4,82.7,207788,83.17,-0.57,82.7,85.84,0.75
20260525,82.7,83,82,82.2,410897,83.09,-1.08,82.71,85.77,1.47
20260526,82.2,82.3,81.8,81.9,292429,82.99,-1.32,82.72,85.7,1.08
20260527,82.2,82.5,81.8,82,413906,82.91,-1.1,82.72,85.63,1.47
20260528,82.5,82.5,81.3,81.5,489946,82.79,-1.56,82.69,85.53,1.68
20260529,82.5,82.5,81.6,82,203873,82.73,-0.88,82.63,85.41,0.71
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 68.12
- over_600_ratio: 66.18
- over_800_ratio: 64.88
- over_1000_ratio: 62.4
- over_400_change_1w: -0.22
- over_800_change_1w: -0.86
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.36,,64.88,,61.93,,0,False,False
20260508,68.29,-0.07,65.67,0.79,62.41,0.48,1,False,True
20260515,68.28,-0.01,65.66,-0.01,62.38,-0.03,0,False,False
20260522,68.34,0.06,65.74,0.08,62.47,0.09,1,True,True
20260529,68.12,-0.22,64.88,-0.86,62.4,-0.07,0,False,False
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
