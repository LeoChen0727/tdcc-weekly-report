# INDIVIDUAL STOCK CHATGPT PACKET - 8183 精星

## Metadata
- generated_at: 2026-05-29 19:33:57 Asia/Taipei
- stock_id: 8183
- stock_name: 精星
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8183_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8183_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8183_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8183_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8183_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8183_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8183_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8183_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8183_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8183_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8183_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8183_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8183_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8183.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8183.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8183.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8183.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8183.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8183.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8183_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8183_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8183_latest.md?ref=main

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
- open: 32.35
- high: 32.45
- low: 31.9
- close: 32.15
- volume: 32000
- ma5: 32.17
- ema23_primary: 32.32
- distance_to_ema23_pct: -0.53
- ma20: 31.85
- ma60: 34.04
- ma120: 33.8
- return_5d: 1.58
- return_20d: -3.31
- volume_ratio: 0.08
- distance_to_ma20_pct_auxiliary: 0.95
- distance_to_high_60_pct: -19.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.55,33.8,33.3,33.4,340000,35.11,-4.87,35.08,34.69,0.52
20260505,33.5,34.85,33.2,34.35,627000,35.05,-1.98,35.2,34.7,0.93
20260506,34.85,34.9,33.55,33.8,400000,34.94,-3.27,35.29,34.69,0.58
20260507,34.2,34.35,33.85,33.95,351000,34.86,-2.61,35.33,34.7,0.5
20260508,34.95,35,32.15,32.25,1628000,34.64,-6.9,35.24,34.68,2.13
20260511,32.8,32.8,31,31.7,1251000,34.4,-7.84,35.09,34.67,1.55
20260512,32.05,32.05,31.6,32,508000,34.2,-6.42,34.94,34.69,0.62
20260513,32,32,31.05,31.15,494000,33.94,-8.23,34.73,34.69,0.61
20260514,31.25,31.45,30.75,30.75,461000,33.68,-8.69,34.51,34.67,0.56
20260515,30.8,31.25,29.95,30.1,456000,33.38,-9.82,34.23,34.65,0.57
20260518,29.8,30.4,29.6,29.85,460000,33.08,-9.78,33.88,34.63,0.62
20260519,30.15,30.75,30,30.15,323000,32.84,-8.19,33.54,34.62,0.46
20260520,30.15,30.5,30.15,30.2,244000,32.62,-7.42,33.21,34.58,0.36
20260521,30.75,31.4,30.75,30.8,384000,32.47,-5.14,32.87,34.55,0.6
20260522,31,31.8,31,31.65,31000,32.4,-2.32,32.65,34.52,0.05
20260525,32,32.25,31.7,32,32000,32.37,-1.13,32.47,34.48,0.06
20260526,32.4,32.8,31.65,32,32000,32.34,-1.04,32.22,34.39,0.06
20260527,32.1,32.95,32.1,32.55,33000,32.35,0.61,31.99,34.25,0.07
20260528,32.75,33.3,31.8,32.15,33000,32.34,-0.58,31.9,34.15,0.08
20260529,32.35,32.45,31.9,32.15,32000,32.32,-0.53,31.85,34.04,0.08
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.29
- over_600_ratio: 45.32
- over_800_ratio: 43.55
- over_1000_ratio: 43.55
- over_400_change_1w: 0.6
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.04,,44.14,,43.48,,0,False,False
20260508,47.7,0.66,43.41,-0.73,43.41,-0.07,1,False,False
20260515,47.69,-0.01,43.38,-0.03,43.38,-0.03,0,False,False
20260522,48.29,0.6,43.55,0.17,43.55,0.17,1,True,True
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
