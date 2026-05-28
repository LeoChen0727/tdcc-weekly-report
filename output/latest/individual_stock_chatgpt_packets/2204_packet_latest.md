# INDIVIDUAL STOCK CHATGPT PACKET - 2204 中華

## Metadata
- generated_at: 2026-05-28 20:18:33 Asia/Taipei
- stock_id: 2204
- stock_name: 中華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2204_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2204_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2204_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2204_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2204_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2204_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2204_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2204_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2204_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2204_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2204_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2204_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2204_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2204.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2204.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2204.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2204.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2204.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2204.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2204_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2204_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2204_latest.md?ref=main

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
- open: 52.6
- high: 53.5
- low: 52.2
- close: 52.9
- volume: 1916150
- ma5: 53.02
- ema23_primary: 53.27
- distance_to_ema23_pct: -0.7
- ma20: 53.24
- ma60: 54.52
- ma120: 56.55
- return_5d: 0.19
- return_20d: -2.4
- volume_ratio: 1.21
- distance_to_ma20_pct_auxiliary: -0.65
- distance_to_high_60_pct: -11.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,54.2,54.4,53.8,54.1,906844,54.5,-0.73,54.4,55.74,0.75
20260504,53.9,54.8,53.8,54.5,1023675,54.5,0.01,54.3,55.71,0.86
20260505,54.2,54.8,53.3,53.7,2409347,54.43,-1.34,54.22,55.66,1.92
20260506,54.4,54.4,53.9,54,1044420,54.39,-0.72,54.2,55.63,0.85
20260507,54.5,55.2,54,55,1414862,54.44,1.02,54.2,55.62,1.15
20260508,55.3,55.5,54.4,54.4,951391,54.44,-0.08,54.21,55.59,0.78
20260511,54.5,54.5,53.9,54.1,1223826,54.41,-0.57,54.2,55.57,1.02
20260512,54,54.5,53.9,54,1157338,54.38,-0.7,54.16,55.55,0.95
20260513,53.9,53.9,52.5,52.9,3773584,54.25,-2.5,54.08,55.51,2.78
20260514,52.7,53.1,52,52.2,3028807,54.08,-3.48,53.95,55.45,2.07
20260515,52.5,52.6,51.9,52,1696823,53.91,-3.54,53.8,55.38,1.16
20260518,52.3,52.3,51.5,51.9,1100851,53.74,-3.43,53.67,55.31,0.75
20260519,51.6,52.5,51.6,52,891558,53.6,-2.98,53.56,55.24,0.61
20260520,52.1,52.5,51.7,52.2,1006925,53.48,-2.4,53.47,55.16,0.7
20260521,52.2,52.9,52,52.8,1312834,53.42,-1.17,53.41,55.05,0.9
20260522,52.8,53.2,52,53.1,1727576,53.4,-0.56,53.38,54.95,1.21
20260525,53,53.4,52.4,53.3,1616570,53.39,-0.17,53.38,54.85,1.11
20260526,53.3,53.3,52.5,53.2,1666390,53.37,-0.32,53.38,54.75,1.13
20260527,53.4,53.4,52.5,52.6,1695900,53.31,-1.33,53.31,54.63,1.12
20260528,52.6,53.5,52.2,52.9,1916150,53.27,-0.7,53.24,54.52,1.21
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.99
- over_600_ratio: 72.05
- over_800_ratio: 70.67
- over_1000_ratio: 70
- over_400_change_1w: 0.15
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.44
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.97,,70.49,,69,,0,False,False
20260508,73.11,0.14,70.63,0.14,68.78,-0.22,1,False,True
20260515,72.84,-0.27,70.4,-0.23,69.56,0.78,2,False,True
20260522,72.99,0.15,70.67,0.27,70,0.44,3,True,True
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
