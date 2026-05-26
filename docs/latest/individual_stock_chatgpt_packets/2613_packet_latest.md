# INDIVIDUAL STOCK CHATGPT PACKET - 2613 中櫃

## Metadata
- generated_at: 2026-05-26 23:53:26 Asia/Taipei
- stock_id: 2613
- stock_name: 中櫃
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2613_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2613_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2613_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2613_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2613_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2613_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2613_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2613_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2613_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2613_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2613_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2613_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2613_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2613.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2613.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2613.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2613.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2613.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2613.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2613_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2613_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2613_latest.md?ref=main

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
- open: 22
- high: 22
- low: 21.7
- close: 21.85
- volume: 336602
- ma5: 21.82
- ema23_primary: 22.15
- distance_to_ema23_pct: -1.37
- ma20: 22.06
- ma60: 23.46
- ma120: 23.8
- return_5d: 1.16
- return_20d: -2.02
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: -0.94
- distance_to_high_60_pct: -27.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.5,22.65,22.2,22.5,270209,23.17,-2.9,23.02,24.2,0.71
20260429,22.75,22.75,22.45,22.5,159267,23.12,-2.67,22.96,24.18,0.44
20260430,22.6,22.6,22.4,22.4,163586,23.06,-2.85,22.93,24.14,0.46
20260504,22.8,22.85,22.35,22.55,239480,23.01,-2.02,22.88,24.11,0.68
20260505,22.55,22.65,22.4,22.5,171090,22.97,-2.05,22.85,24.09,0.49
20260506,22.45,22.6,22.25,22.4,341090,22.92,-2.29,22.8,24.06,0.97
20260507,22.55,22.7,22.3,22.65,376080,22.9,-1.1,22.75,24.02,1.06
20260508,22.65,22.9,22.1,22.3,312848,22.85,-2.41,22.71,23.98,0.88
20260511,22.35,22.4,22.2,22.35,222285,22.81,-2.01,22.68,23.95,0.63
20260512,22.35,22.35,21.9,22,550263,22.74,-3.26,22.63,23.91,1.52
20260513,22,22,21.8,21.8,438715,22.66,-3.81,22.57,23.87,1.19
20260514,21.8,21.95,21.4,21.5,522317,22.57,-4.73,22.5,23.81,1.51
20260515,21.85,22,21.45,21.45,424582,22.47,-4.55,22.41,23.76,1.21
20260518,21.4,21.8,21.2,21.55,204191,22.4,-3.78,22.34,23.72,0.6
20260519,21.6,22,21.55,21.6,190919,22.33,-3.27,22.27,23.68,0.57
20260520,21.6,22.45,21.55,21.55,416478,22.27,-3.21,22.2,23.63,1.23
20260521,21.6,22.05,21.45,21.9,383179,22.23,-1.5,22.14,23.59,1.11
20260522,22.05,22.45,21.85,21.95,344291,22.21,-1.17,22.11,23.55,1.04
20260525,22.3,22.55,21.75,21.85,536874,22.18,-1.49,22.08,23.5,1.6
20260526,22,22,21.7,21.85,336602,22.15,-1.37,22.06,23.46,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.5
- over_600_ratio: 51.88
- over_800_ratio: 50.02
- over_1000_ratio: 49.44
- over_400_change_1w: -0.3
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.42,,49.41,,49.41,,0,False,False
20260508,55.55,0.13,50,0.59,49.42,0.01,1,True,True
20260515,55.8,0.25,50.02,0.02,49.44,0.02,2,False,True
20260522,55.5,-0.3,50.02,0,49.44,0,3,False,False
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
