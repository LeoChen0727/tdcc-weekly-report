# INDIVIDUAL STOCK CHATGPT PACKET - 5272 笙科

## Metadata
- generated_at: 2026-05-28 19:32:55 Asia/Taipei
- stock_id: 5272
- stock_name: 笙科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5272_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5272_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5272_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5272_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5272_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5272_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5272_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5272_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5272_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5272_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5272_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5272_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5272_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5272.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5272.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5272.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5272.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5272.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5272.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5272_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5272_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5272_latest.md?ref=main

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
- open: 22.85
- high: 23.1
- low: 22
- close: 22
- volume: 332554
- ma5: 22.77
- ema23_primary: 23.08
- distance_to_ema23_pct: -4.69
- ma20: 23.27
- ma60: 23.05
- ma120: 21.66
- return_5d: -4.97
- return_20d: -9.46
- volume_ratio: 1.09
- distance_to_ma20_pct_auxiliary: -5.45
- distance_to_high_60_pct: -21.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,24.4,25.7,24.3,24.45,467000,23.77,2.88,23.52,22.33,0.67
20260504,24.7,25.3,24.5,24.75,416000,23.85,3.78,23.63,22.39,0.59
20260505,24.75,25.65,24.6,24.9,502000,23.94,4.03,23.77,22.45,0.69
20260506,25.3,25.3,23.9,24.4,486000,23.97,1.77,23.91,22.49,0.66
20260507,24.55,25,24.2,24.45,487000,24.01,1.82,24.02,22.53,0.64
20260508,24.4,25.4,24,24.2,535000,24.03,0.71,24.14,22.58,0.69
20260511,24.2,24.2,23.1,23.45,524000,23.98,-2.22,24.25,22.63,0.66
20260512,24.1,24.1,23.05,23.45,279000,23.94,-2.03,24.32,22.68,0.35
20260513,23.5,23.5,22.75,22.75,334000,23.84,-4.56,24.36,22.73,0.41
20260514,23,23.05,22.75,22.75,194000,23.75,-4.2,24.39,22.75,0.24
20260515,22.85,23.45,22.25,22.3,348000,23.63,-5.62,24.39,22.77,0.43
20260518,22.5,22.5,21.4,22.05,382000,23.5,-6.15,24.32,22.79,0.48
20260519,22.05,22.35,21.95,22.1,182000,23.38,-5.47,24.15,22.82,0.26
20260520,22.1,22.9,22.1,22.35,196000,23.29,-4.05,23.91,22.86,0.42
20260521,22.8,23.5,22.75,23.15,332000,23.28,-0.56,23.75,22.92,0.8
20260522,23.2,23.45,23.15,23.2,23000,23.27,-0.32,23.67,22.97,0.06
20260525,23.3,23.8,22.7,23.3,23000,23.28,0.1,23.57,23,0.07
20260526,23.3,23.5,22.3,22.55,23000,23.22,-2.87,23.47,23.03,0.07
20260527,22.6,23.2,22.15,22.8,23000,23.18,-1.65,23.38,23.07,0.08
20260528,22.85,23.1,22,22,332554,23.08,-4.69,23.27,23.05,1.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 23.1
- over_600_ratio: 18.76
- over_800_ratio: 14.93
- over_1000_ratio: 10.26
- over_400_change_1w: -0.75
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,23.81,,14.92,,10.26,,0,False,False
20260508,23.09,-0.72,14.92,0,10.26,0,0,False,False
20260515,23.85,0.76,14.93,0.01,10.26,0,1,False,True
20260522,23.1,-0.75,14.93,0,10.26,0,0,False,False
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
