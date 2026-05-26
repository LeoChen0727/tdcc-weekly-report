# INDIVIDUAL STOCK CHATGPT PACKET - 5601 台聯櫃

## Metadata
- generated_at: 2026-05-26 22:19:53 Asia/Taipei
- stock_id: 5601
- stock_name: 台聯櫃
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 109
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5601_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5601_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5601_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5601_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5601_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5601_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5601_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5601_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5601_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5601_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5601_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5601_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5601_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5601.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5601.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5601.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5601.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5601.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5601.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5601_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5601_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5601_latest.md?ref=main

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
- open: 34.75
- high: 34.75
- low: 34.7
- close: 34.75
- volume: 35000
- ma5: 34.88
- ema23_primary: 35.44
- distance_to_ema23_pct: -1.93
- ma20: 35.35
- ma60: 36.22
- ma120: 36.54
- return_5d: -1.97
- return_20d: -2.8
- volume_ratio: 2.77
- distance_to_ma20_pct_auxiliary: -1.7
- distance_to_high_60_pct: -8.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260423,35.55,35.55,35.55,35.55,10000,36.38,-2.27,36.36,36.59,1.68
20260424,35.3,35.35,35.3,35.35,24000,36.29,-2.59,36.31,36.58,3.38
20260427,35.5,35.85,35.5,35.5,18000,36.22,-2,36.26,36.58,2.26
20260428,35.6,35.65,35.3,35.65,16000,36.18,-1.45,36.2,36.56,1.92
20260429,35.6,35.6,35.6,35.6,6000,36.13,-1.46,36.18,36.55,0.74
20260430,35.4,36,35.4,36,3000,36.12,-0.33,36.14,36.53,0.37
20260504,35.6,35.6,35.6,35.6,6000,36.07,-1.31,36.09,36.51,0.72
20260505,35.6,35.6,35.6,35.6,12000,36.03,-1.21,36.06,36.51,1.38
20260506,35.4,35.4,35.4,35.4,10000,35.98,-1.62,36.05,36.49,1.12
20260508,34.8,35.5,34.8,35.35,3000,35.93,-1.61,35.98,36.48,0.34
20260511,35.3,35.3,35.3,35.3,1000,35.88,-1.61,35.92,36.45,0.12
20260512,35.3,35.3,35.3,35.3,1000,35.83,-1.48,35.86,36.43,0.12
20260513,35.5,35.55,35.5,35.55,2000,35.81,-0.71,35.84,36.4,0.24
20260514,35.75,35.75,35.3,35.45,8000,35.78,-0.91,35.76,36.37,1.03
20260515,35.6,35.6,35.45,35.45,6000,35.75,-0.84,35.7,36.35,0.81
20260518,35.1,35.1,35.1,35.1,5000,35.69,-1.67,35.61,36.34,0.67
20260519,35.1,35.3,35.05,35.1,17000,35.65,-1.53,35.54,36.31,2.05
20260522,35.1,35.4,34.75,34.75,35000,35.57,-2.31,35.47,36.28,3.5
20260525,34.7,34.7,34.7,34.7,35000,35.5,-2.25,35.4,36.25,3.11
20260526,34.75,34.75,34.7,34.75,35000,35.44,-1.93,35.35,36.22,2.77
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.87
- over_600_ratio: 66.01
- over_800_ratio: 54.45
- over_1000_ratio: 48.9
- over_400_change_1w: -0.02
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.94,,54.53,,48.98,,0,False,False
20260508,78.88,-0.06,54.48,-0.05,48.93,-0.05,0,False,False
20260515,78.89,0.01,54.48,0,48.93,0,1,False,False
20260522,78.87,-0.02,54.45,-0.03,48.9,-0.03,0,False,False
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
