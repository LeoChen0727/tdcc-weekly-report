# INDIVIDUAL STOCK CHATGPT PACKET - 4119 旭富

## Metadata
- generated_at: 2026-05-27 21:27:18 Asia/Taipei
- stock_id: 4119
- stock_name: 旭富
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4119_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4119_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4119_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4119_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4119_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4119_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4119_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4119_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4119_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4119_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4119_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4119_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4119_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4119.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4119.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4119.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4119.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4119.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4119.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4119_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4119_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4119_latest.md?ref=main

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
- open: 41.5
- high: 41.5
- low: 40.7
- close: 41
- volume: 220386
- ma5: 41.78
- ema23_primary: 44
- distance_to_ema23_pct: -6.82
- ma20: 43.8
- ma60: 48.81
- ma120: 49.66
- return_5d: -3.53
- return_20d: -13.68
- volume_ratio: 0.84
- distance_to_ma20_pct_auxiliary: -6.4
- distance_to_high_60_pct: -26.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,48.05,48.2,47.5,48.2,106356,49.59,-2.81,49.66,51.74,0.51
20260430,48.2,48.2,47.7,47.8,149206,49.44,-3.32,49.51,51.64,0.73
20260504,47.3,48.95,47.1,47.15,198060,49.25,-4.27,49.27,51.53,0.94
20260505,47.15,47.2,46.9,47.1,168555,49.07,-4.02,49.05,51.42,0.78
20260506,47.1,47.7,46.9,47.1,193587,48.91,-3.7,48.8,51.31,0.88
20260507,47.05,47.4,46.55,47.3,200870,48.77,-3.02,48.55,51.2,0.89
20260508,47.5,47.7,46.55,46.65,183993,48.6,-4.01,48.33,51.09,0.82
20260511,46.05,46.05,44.15,44.3,661393,48.24,-8.17,48.02,50.96,2.68
20260512,44.3,44.3,41.8,42.1,656097,47.73,-11.79,47.59,50.8,2.4
20260513,41.95,41.95,41.15,41.6,334218,47.22,-11.9,47.15,50.64,1.18
20260514,41.6,41.8,40.55,40.95,360948,46.69,-12.3,46.69,50.45,1.24
20260515,40.7,41.4,40.3,40.4,282940,46.17,-12.5,46.21,50.26,0.97
20260518,40.4,41.7,40.05,41.6,261338,45.79,-9.15,45.87,50.08,0.94
20260519,41.9,42.8,41.9,42.4,320699,45.51,-6.83,45.56,49.92,1.13
20260520,43.05,43.05,41.9,42.5,151271,45.26,-6.09,45.29,49.75,0.55
20260521,42.5,43.3,42.5,43.05,137261,45.07,-4.49,45.04,49.6,0.51
20260522,43,43,42.2,42.25,194671,44.84,-5.77,44.8,49.42,0.74
20260525,42.25,42.25,41,41.3,278345,44.54,-7.28,44.45,49.21,1.07
20260526,41,41.45,40.6,41.3,161538,44.27,-6.71,44.13,49.02,0.63
20260527,41.5,41.5,40.7,41,220386,44,-6.82,43.8,48.81,0.84
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.44
- over_600_ratio: 44.22
- over_800_ratio: 42.53
- over_1000_ratio: 42.53
- over_400_change_1w: 0.13
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.27,,42.36,,41.53,,0,False,False
20260508,45.3,0.03,42.38,0.02,42.38,0.85,1,True,True
20260515,45.31,0.01,42.38,0,42.38,0,2,False,False
20260522,45.44,0.13,42.53,0.15,42.53,0.15,3,True,True
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
