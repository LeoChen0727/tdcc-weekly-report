# INDIVIDUAL STOCK CHATGPT PACKET - 2072 世紀風電

## Metadata
- generated_at: 2026-05-29 19:31:54 Asia/Taipei
- stock_id: 2072
- stock_name: 世紀風電
- packet_status: partial_rawdata_packet
- latest_price_date: 20260529
- price_rows: 44
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2072_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2072_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2072_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2072_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2072_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2072_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2072_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2072_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2072_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2072_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2072_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2072_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2072_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2072.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2072.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2072.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2072.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2072.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2072.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2072_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2072_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2072_latest.md?ref=main

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
- open: 166.5
- high: 172
- low: 166
- close: 170.5
- volume: 619939
- ma5: 167.3
- ema23_primary: 173.28
- distance_to_ema23_pct: -1.6
- ma20: 173.78
- ma60: 177.66
- ma120: 177.66
- return_5d: 0.89
- return_20d: -7.84
- volume_ratio: 1.07
- distance_to_ma20_pct_auxiliary: -1.88
- distance_to_high_60_pct: -14.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,187,188,179.5,181,684357,181.07,-0.04,179.93,180.9,0.99
20260505,181,181.5,178.5,178.5,382172,180.85,-1.3,180.32,180.81,0.59
20260506,181.5,181.5,175,176,396294,180.45,-2.47,180.28,180.63,0.62
20260507,180,181.5,176.5,179,527916,180.33,-0.74,179.97,180.57,0.84
20260508,180,183.5,177.5,180.5,478389,180.34,0.09,179.5,180.57,0.8
20260511,182,185,179,179.5,601845,180.27,-0.43,179.35,180.53,1.02
20260512,180,181,178.5,178.5,357990,180.13,-0.9,179.3,180.47,0.63
20260513,178.5,178.5,173.5,175,523656,179.7,-2.61,179.38,180.3,0.93
20260514,173,173.5,162.5,171.5,1178767,179.02,-4.2,179.2,180.03,1.97
20260515,172,186,170,180,1623924,179.1,0.5,178.95,180.03,2.55
20260518,180,180,173.5,174.5,590882,178.71,-2.36,178.62,179.87,0.92
20260519,177.5,179.5,174.5,174.5,333041,178.36,-2.17,178.12,179.72,0.55
20260520,174.5,174.5,168.5,169,509179,177.58,-4.83,177.47,179.43,0.86
20260521,171,174.5,169.5,172.5,358246,177.16,-2.63,176.85,179.25,0.61
20260522,172.5,172.5,168.5,169,443434,176.48,-4.24,176.4,178.99,0.77
20260525,171,171,165,167.5,595215,175.73,-4.68,176.03,178.7,1.02
20260526,167.5,169.5,165.5,166.5,360917,174.96,-4.84,175.68,178.4,0.62
20260527,167,170,163.5,165.5,546642,174.17,-4.98,175.22,178.1,0.92
20260528,165.5,169,163.5,166.5,461439,173.53,-4.05,174.5,177.83,0.78
20260529,166.5,172,166,170.5,619939,173.28,-1.6,173.78,177.66,1.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.28
- over_600_ratio: 73.06
- over_800_ratio: 72.31
- over_1000_ratio: 71.38
- over_400_change_1w: -0.14
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.56,,72.39,,71.46,,0,False,False
20260508,75.58,0.02,72.46,0.07,71.53,0.07,1,True,True
20260515,75.42,-0.16,72.46,0,71.53,0,0,False,False
20260522,75.28,-0.14,72.31,-0.15,71.38,-0.15,0,False,False
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
