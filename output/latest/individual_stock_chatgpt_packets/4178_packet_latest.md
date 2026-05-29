# INDIVIDUAL STOCK CHATGPT PACKET - 4178 永笙-KY

## Metadata
- generated_at: 2026-05-29 19:32:48 Asia/Taipei
- stock_id: 4178
- stock_name: 永笙-KY
- packet_status: partial_rawdata_packet
- latest_price_date: 20260529
- price_rows: 21
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4178_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4178_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4178_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4178_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4178_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4178_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4178_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4178_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4178_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4178_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4178_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4178_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4178_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4178.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4178.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4178.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4178.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4178.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4178.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4178_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4178_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4178_latest.md?ref=main

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
- open: 18.7
- high: 18.7
- low: 18.55
- close: 18.65
- volume: 347530
- ma5: 18.77
- ema23_primary: 18.93
- distance_to_ema23_pct: -1.49
- ma20: 18.95
- ma60: 18.96
- ma120: 18.96
- return_5d: -1.58
- return_20d: -2.36
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: -1.58
- distance_to_high_60_pct: -3.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,18.95,19.2,18.65,19.1,2152179,,,,,
20260505,19.1,19.1,18.8,19.05,1030659,,,,,
20260506,19.15,19.15,18.75,19,1167523,,,,,
20260507,19.1,19.1,18.8,19,867525,19.08,-0.42,19.05,19.05,0.32
20260508,19,19.1,18.7,19,1492221,19.07,-0.39,19.04,19.04,0.6
20260511,19,19.05,18.9,19,695168,19.07,-0.35,19.04,19.04,0.31
20260512,19,19.1,18.95,19.05,565464,19.07,-0.08,19.04,19.04,0.28
20260513,19,19.1,18.95,19.05,553368,19.06,-0.08,19.04,19.04,0.3
20260514,19,19.1,18.8,19,593525,19.06,-0.31,19.04,19.04,0.34
20260515,19,19,18.8,19,429546,19.05,-0.29,19.03,19.03,0.27
20260518,18.8,19,18.8,18.95,383470,19.05,-0.5,19.02,19.02,0.25
20260519,19,19,18.85,19,490811,19.04,-0.22,19.02,19.02,0.34
20260520,18.95,19.05,18.9,19,387286,19.04,-0.2,19.02,19.02,0.28
20260521,19,19.15,18.95,19,432922,19.04,-0.19,19.02,19.02,0.33
20260522,19,19,18.8,18.95,354843,19.03,-0.41,19.02,19.02,0.29
20260525,18.95,18.95,18.6,18.9,1348005,19.02,-0.62,19.01,19.01,1.08
20260526,18.8,18.9,18.65,18.9,728525,19.01,-0.57,19,19,0.6
20260527,18.9,18.9,18.6,18.85,555989,18.99,-0.76,18.99,18.99,0.47
20260528,18.85,18.85,18.55,18.55,280033,18.96,-2.15,18.97,18.97,0.25
20260529,18.7,18.7,18.55,18.65,347530,18.93,-1.49,18.95,18.96,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 77.03
- over_600_ratio: 74.72
- over_800_ratio: 71.77
- over_1000_ratio: 71.37
- over_400_change_1w: 0.15
- over_800_change_1w: 0.36
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.62,,69.29,,68.89,,0,False,False
20260508,76.38,0.76,70.85,1.56,70.45,1.56,1,True,True
20260515,76.88,0.5,71.41,0.56,71.01,0.56,2,True,True
20260522,77.03,0.15,71.77,0.36,71.37,0.36,3,True,True
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
