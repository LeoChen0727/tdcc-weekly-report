# INDIVIDUAL STOCK CHATGPT PACKET - 3064 泰偉

## Metadata
- generated_at: 2026-05-26 21:25:22 Asia/Taipei
- stock_id: 3064
- stock_name: 泰偉
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 110
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3064_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3064_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3064_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3064_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3064_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3064_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3064_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3064_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3064_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3064_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3064_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3064_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3064_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3064.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3064.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3064.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3064.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3064.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3064.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3064_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3064_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3064_latest.md?ref=main

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
- open: 18.75
- high: 18.75
- low: 18
- close: 18.35
- volume: 18000
- ma5: 18.56
- ema23_primary: 20.85
- distance_to_ema23_pct: -11.97
- ma20: 19.65
- ma60: 29.88
- ma120: 38.44
- return_5d: 0.27
- return_20d: -10.92
- volume_ratio: 2.2
- distance_to_ma20_pct_auxiliary: -6.6
- distance_to_high_60_pct: -62.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260420,20.5,20.5,18.55,19.5,17000,27.01,-27.81,25.86,38.75,1.54
20260421,19.45,19.45,18.5,18.5,8000,26.3,-29.66,25.21,38.21,0.78
20260422,19.2,19.2,19.2,19.2,1000,25.71,-25.32,24.62,37.69,0.1
20260423,19.8,20.5,19.4,20,23000,25.23,-20.74,24.04,37.19,2.09
20260424,19.9,20,19.8,20,7000,24.8,-19.35,23.59,36.76,0.63
20260427,20.95,20.95,20.95,20.95,1000,24.48,-14.41,23.16,36.32,0.09
20260429,21,21,21,21,1000,24.19,-13.18,22.73,35.88,0.09
20260430,19.9,20.75,19.9,20.75,3000,23.9,-13.18,22.28,35.45,0.28
20260504,20.65,20.65,19,19.15,5000,23.51,-18.53,21.9,35.02,0.51
20260505,19.45,20,19.45,20,3000,23.21,-13.84,21.57,34.59,0.3
20260506,21,21,21,21,1000,23.03,-8.81,21.23,34.16,0.12
20260511,20.6,20.8,20.6,20.75,3000,22.84,-9.15,20.89,33.72,0.35
20260512,20.55,20.55,20.55,20.55,1000,22.65,-9.26,20.57,33.32,0.13
20260513,20.5,20.5,20.5,20.5,1000,22.47,-8.76,20.38,32.87,0.16
20260515,20.2,20.2,18.3,18.3,12000,22.12,-17.28,20.19,32.36,1.85
20260518,18.6,19.7,18.5,19.5,14000,21.9,-10.97,20.02,31.87,2.41
20260521,17.75,18.95,17.75,18.95,9000,21.66,-12.5,19.94,31.37,1.57
20260522,18.1,18.1,17.45,18,18000,21.35,-15.7,19.86,30.87,2.77
20260525,18.15,18.15,18,18,18000,21.07,-14.58,19.76,30.37,2.45
20260526,18.75,18.75,18,18.35,18000,20.85,-11.97,19.65,29.88,2.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.47
- over_600_ratio: 60.15
- over_800_ratio: 60.15
- over_1000_ratio: 60.15
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
20260430,63.47,,60.15,,60.15,,0,False,False
20260508,63.47,0,60.15,0,60.15,0,0,False,False
20260515,63.47,0,60.15,0,60.15,0,0,False,False
20260522,63.47,0,60.15,0,60.15,0,0,False,False
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
