# INDIVIDUAL STOCK CHATGPT PACKET - 6666 羅麗芬-KY

## Metadata
- generated_at: 2026-05-26 23:02:27 Asia/Taipei
- stock_id: 6666
- stock_name: 羅麗芬-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6666_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6666_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6666_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6666_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6666_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6666_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6666_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6666_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6666_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6666_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6666_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6666_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6666_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6666.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6666.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6666.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6666.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6666.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6666.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6666_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6666_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6666_latest.md?ref=main

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
- date: 20260526
- open: 39.8
- high: 39.95
- low: 39.2
- close: 39.6
- volume: 33159
- ma5: 40.45
- ema23_primary: 40.75
- distance_to_ema23_pct: -2.81
- ma20: 40.64
- ma60: 41.22
- ma120: 42.99
- return_5d: -3.41
- return_20d: -3.53
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: -2.55
- distance_to_high_60_pct: -11.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,41.05,41.45,40.7,40.7,17455,41.53,-1.99,41.23,42.4,0.96
20260429,41.1,41.15,40.75,40.9,7522,41.47,-1.38,41.28,42.35,0.43
20260430,41.35,41.35,40,40.15,25309,41.36,-2.93,41.29,42.29,1.43
20260504,40.7,40.95,39.75,40.2,57055,41.27,-2.59,41.29,42.23,2.89
20260505,40.75,40.75,39.95,40.1,12602,41.17,-2.6,41.28,42.16,0.63
20260506,41.2,42,40.75,41.1,37020,41.16,-0.16,41.33,42.08,1.72
20260507,41.4,42.5,41.15,41.35,24857,41.18,0.41,41.38,42.02,1.13
20260508,41.9,41.9,41,41.4,17023,41.2,0.49,41.37,41.96,0.79
20260511,42.2,42.2,41.05,41.55,31259,41.23,0.78,41.36,41.91,1.37
20260512,41.2,41.45,40.5,40.75,27446,41.19,-1.06,41.31,41.85,1.19
20260513,40.75,40.75,40.15,40.35,17002,41.12,-1.87,41.23,41.79,0.73
20260514,41.4,41.4,40.45,40.45,10312,41.06,-1.49,41.16,41.72,0.45
20260515,40,40.95,39.9,40.3,22223,41,-1.7,41.11,41.66,0.95
20260518,41.25,41.25,40.1,40.2,3675,40.93,-1.79,41.04,41.59,0.16
20260519,40.8,41.35,40.3,41,76580,40.94,0.15,41.01,41.53,2.97
20260520,41.3,41.3,40.3,40.35,16289,40.89,-1.32,40.92,41.47,0.68
20260521,40.15,42.6,40.15,41.65,40895,40.95,1.7,40.88,41.44,1.65
20260522,41.55,41.6,40.6,40.6,14113,40.92,-0.79,40.84,41.37,0.57
20260525,40.1,40.15,39.95,40.05,41018,40.85,-1.96,40.71,41.3,1.59
20260526,39.8,39.95,39.2,39.6,33159,40.75,-2.81,40.64,41.22,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.06
- over_600_ratio: 78.06
- over_800_ratio: 78.06
- over_1000_ratio: 78.06
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.06,,78.06,,78.06,,0,False,False
20260508,78.06,0,78.06,0,78.06,0,0,False,False
20260515,78.06,0,78.06,0,78.06,0,0,False,False
20260522,78.06,0,78.06,0,78.06,0,0,False,False
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
