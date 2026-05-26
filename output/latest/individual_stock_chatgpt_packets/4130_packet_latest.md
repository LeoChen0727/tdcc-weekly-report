# INDIVIDUAL STOCK CHATGPT PACKET - 4130 健亞

## Metadata
- generated_at: 2026-05-26 21:25:44 Asia/Taipei
- stock_id: 4130
- stock_name: 健亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4130_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4130_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4130_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4130_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4130_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4130_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4130_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4130_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4130_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4130_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4130_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4130_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4130_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4130.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4130.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4130.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4130.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4130.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4130.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4130_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4130_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4130_latest.md?ref=main

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
- open: 26.2
- high: 26.4
- low: 25.45
- close: 25.8
- volume: 26000
- ma5: 26.92
- ema23_primary: 28.12
- distance_to_ema23_pct: -8.25
- ma20: 27.45
- ma60: 30.8
- ma120: 29.69
- return_5d: -7.36
- return_20d: -7.86
- volume_ratio: 0.19
- distance_to_ma20_pct_auxiliary: -6.02
- distance_to_high_60_pct: -28.33

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,28,28.1,27.45,27.9,215000,31.5,-11.42,32.34,32.18,0.18
20260429,27.55,28.35,27.55,27.8,165000,31.19,-10.86,31.98,32.09,0.14
20260430,27.8,27.85,27.45,27.45,165000,30.88,-11.1,31.73,31.98,0.15
20260504,27.4,27.4,26.4,26.85,300000,30.54,-12.09,31.41,31.87,0.28
20260505,26.8,27.5,26.75,27.4,204000,30.28,-9.51,31.08,31.8,0.19
20260506,27.1,27.3,26.65,27,146000,30.01,-10.02,30.7,31.72,0.14
20260507,27.05,27.85,26.8,27.35,211000,29.78,-8.17,30.36,31.65,0.22
20260508,27.35,27.4,27,27.2,115000,29.57,-8.01,30.02,31.58,0.12
20260511,27.95,27.95,27.35,27.65,115000,29.41,-5.98,29.7,31.54,0.13
20260512,27.95,28.5,27.9,28.25,283000,29.31,-3.63,29.43,31.5,0.4
20260513,28.45,28.5,28.15,28.25,160000,29.22,-3.33,29.19,31.45,0.24
20260514,28.35,28.35,27.9,28.2,135000,29.14,-3.22,28.92,31.4,0.23
20260515,28.2,28.2,27.5,27.6,120000,29.01,-4.86,28.67,31.32,0.22
20260518,27.1,27.75,27.1,27.7,28000,28.9,-4.16,28.43,31.25,0.05
20260519,27.7,28.2,27.7,27.85,77000,28.81,-3.34,28.2,31.19,0.15
20260520,27.25,27.8,27.1,27.3,95000,28.69,-4.84,27.96,31.11,0.23
20260521,27.3,27.85,27.3,27.6,121000,28.6,-3.49,27.84,31.03,0.46
20260522,27.4,27.75,27.35,27.5,27000,28.51,-3.53,27.71,30.95,0.14
20260525,27.35,27.4,26.3,26.4,27000,28.33,-6.81,27.56,30.89,0.16
20260526,26.2,26.4,25.45,25.8,26000,28.12,-8.25,27.45,30.8,0.19
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.12
- over_600_ratio: 62.37
- over_800_ratio: 61.81
- over_1000_ratio: 61.81
- over_400_change_1w: -0.01
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.59,,61.62,,61.62,,0,False,False
20260508,64.04,0.45,61.69,0.07,61.69,0.07,1,True,True
20260515,64.13,0.09,61.78,0.09,61.78,0.09,2,False,True
20260522,64.12,-0.01,61.81,0.03,61.81,0.03,3,False,True
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
