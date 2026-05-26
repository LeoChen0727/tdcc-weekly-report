# INDIVIDUAL STOCK CHATGPT PACKET - 3303 岱稜

## Metadata
- generated_at: 2026-05-26 23:53:45 Asia/Taipei
- stock_id: 3303
- stock_name: 岱稜
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3303_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3303_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3303_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3303_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3303_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3303_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3303_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3303_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3303_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3303_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3303_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3303_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3303_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3303.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3303.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3303.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3303.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3303.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3303.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3303_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3303_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3303_latest.md?ref=main

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
- open: 49.8
- high: 50
- low: 49
- close: 49.2
- volume: 49000
- ma5: 49.03
- ema23_primary: 49.12
- distance_to_ema23_pct: 0.16
- ma20: 49.91
- ma60: 47.74
- ma120: 46.69
- return_5d: 2.07
- return_20d: 1.86
- volume_ratio: 0.09
- distance_to_ma20_pct_auxiliary: -1.41
- distance_to_high_60_pct: -9.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,48.6,48.75,48.05,48.4,195000,46.82,3.38,46.31,46.55,0.85
20260429,48.75,49.4,48.45,48.75,663000,46.98,3.77,46.47,46.59,2.6
20260430,49.4,49.4,48.75,49,292000,47.15,3.93,46.68,46.62,1.13
20260504,49.8,49.95,48.7,49.8,638000,47.37,5.13,46.92,46.67,2.26
20260505,50.5,53.7,49.8,53.7,1694000,47.9,12.12,47.37,46.77,4.68
20260506,54.5,54.6,50.2,51.3,2073000,48.18,6.48,47.68,46.85,4.5
20260507,51.4,52,51.1,51.6,464000,48.46,6.47,47.99,46.94,0.97
20260508,52.7,53.2,51.5,52,702000,48.76,6.65,48.32,47.03,1.39
20260511,52.9,52.9,51.7,52,384000,49.03,6.06,48.59,47.14,0.75
20260512,50.5,50.5,48.95,49.8,1138000,49.09,1.44,48.78,47.22,2.03
20260513,49.5,51.1,49.5,50.1,453000,49.18,1.88,48.98,47.31,0.79
20260514,50.5,51.1,50,50.4,436000,49.28,2.27,49.21,47.39,0.74
20260515,50.5,50.5,49.1,49.15,396000,49.27,-0.24,49.34,47.45,0.66
20260518,48.65,49.15,48.35,48.75,294000,49.23,-0.97,49.45,47.52,0.49
20260519,48.75,48.95,47.75,48.2,278000,49.14,-1.91,49.55,47.58,0.46
20260520,48.3,48.45,47.85,47.9,178000,49.04,-2.32,49.59,47.61,0.3
20260521,48.15,49.2,48.15,48.9,272000,49.03,-0.26,49.64,47.66,0.47
20260522,49.3,49.5,48.8,49.35,49000,49.05,0.61,49.77,47.7,0.09
20260525,49.65,50.6,49.45,49.8,50000,49.11,1.4,49.86,47.73,0.09
20260526,49.8,50,49,49.2,49000,49.12,0.16,49.91,47.74,0.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.62
- over_600_ratio: 42.81
- over_800_ratio: 38.62
- over_1000_ratio: 36.54
- over_400_change_1w: -0.46
- over_800_change_1w: 0.35
- over_1000_change_1w: 0.35
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.95,,38.14,,36.06,,0,False,False
20260508,46.28,0.33,38.27,0.13,36.19,0.13,1,True,True
20260515,46.08,-0.2,38.27,0,36.19,0,2,False,False
20260522,45.62,-0.46,38.62,0.35,36.54,0.35,3,False,True
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
