# INDIVIDUAL STOCK CHATGPT PACKET - 2607 榮運

## Metadata
- generated_at: 2026-05-28 20:18:49 Asia/Taipei
- stock_id: 2607
- stock_name: 榮運
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2607_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2607_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2607_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2607_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2607_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2607_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2607_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2607_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2607_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2607_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2607_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2607_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2607_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2607.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2607.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2607.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2607.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2607.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2607.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2607_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2607_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2607_latest.md?ref=main

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
- open: 47.5
- high: 47.7
- low: 47.2
- close: 47.3
- volume: 995513
- ma5: 47.8
- ema23_primary: 48.05
- distance_to_ema23_pct: -1.55
- ma20: 47.54
- ma60: 50.43
- ma120: 53.92
- return_5d: -0.94
- return_20d: -2.17
- volume_ratio: 1.56
- distance_to_ma20_pct_auxiliary: -0.5
- distance_to_high_60_pct: -18.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,48.5,48.5,47.45,47.45,511349,50.06,-5.2,50.02,53.23,0.92
20260504,47.6,48,47,47,619131,49.8,-5.62,49.77,53.05,1.12
20260505,47,47.5,46.8,47.25,486107,49.59,-4.72,49.56,52.88,0.86
20260506,47.8,47.8,47.2,47.5,387978,49.41,-3.87,49.35,52.72,0.67
20260507,47.75,48.15,47.5,48,496872,49.3,-2.63,49.17,52.57,0.86
20260508,48.25,48.25,47.7,47.9,206116,49.18,-2.6,49.02,52.42,0.36
20260511,47.95,48.4,47.75,48.4,370048,49.11,-1.46,48.89,52.28,0.67
20260512,48.5,48.55,47.85,47.85,543589,49.01,-2.37,48.76,52.15,0.97
20260513,47.85,47.85,47,47.25,791714,48.86,-3.3,48.58,52,1.39
20260514,47.25,47.4,47,47,593633,48.71,-3.51,48.4,51.84,1.06
20260515,47,47.35,46.45,46.45,668520,48.52,-4.27,48.2,51.68,1.19
20260518,46.7,47.25,46,47.1,1240445,48.4,-2.69,48.04,51.53,2.07
20260519,47.05,47.75,47.05,47.5,962717,48.33,-1.71,47.91,51.39,1.57
20260520,47.9,48.1,47.15,47.35,618537,48.24,-1.85,47.77,51.24,1
20260521,47.55,47.8,47.2,47.75,449494,48.2,-0.94,47.67,51.11,0.74
20260522,47.8,48.2,47.45,47.9,537063,48.18,-0.58,47.62,50.98,0.93
20260525,48.15,48.9,47.9,48.5,704557,48.21,0.61,47.63,50.87,1.21
20260526,48.55,48.8,47.75,48,613029,48.19,-0.39,47.63,50.73,1.06
20260527,48.3,48.3,47.2,47.3,958151,48.11,-1.69,47.59,50.59,1.58
20260528,47.5,47.7,47.2,47.3,995513,48.05,-1.55,47.54,50.43,1.56
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 77.03
- over_600_ratio: 74.79
- over_800_ratio: 73.18
- over_1000_ratio: 70.61
- over_400_change_1w: 0.14
- over_800_change_1w: -0.22
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.96,,73.58,,71.19,,0,False,False
20260508,76.96,0,73.6,0.02,71.22,0.03,1,False,True
20260515,76.89,-0.07,73.4,-0.2,70.81,-0.41,0,False,False
20260522,77.03,0.14,73.18,-0.22,70.61,-0.2,1,False,False
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
