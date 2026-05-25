# INDIVIDUAL STOCK CHATGPT PACKET - 2020 美亞

## Metadata
- generated_at: 2026-05-26 06:39:29 Asia/Taipei
- stock_id: 2020
- stock_name: 美亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2020_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2020_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2020_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2020_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2020_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2020_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2020_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2020_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2020_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2020_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2020_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2020_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2020_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2020.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2020.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2020.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2020.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2020.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2020.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2020_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2020_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2020_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 21.5
- high: 21.9
- low: 21.45
- close: 21.75
- volume: 993511
- ma5: 21.48
- ma20: 21.67
- ma60: 23.22
- ma120: 23.43
- ema23: 21.91
- return_5d: 1.4
- return_20d: -2.47
- volume_ratio: 1.98
- distance_to_ma20_pct: 0.37
- distance_to_high_60_pct: -15.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ema23,volume_ratio
20260430,22.45,22.45,22,22.15,387528,22.19,23.78,24.01,23.37,0.48
20260504,22.15,22.15,21.8,21.85,638048,22.11,23.63,23.98,23.24,0.8
20260505,21.85,21.95,21.75,21.8,302183,22.07,23.48,23.94,23.12,0.38
20260506,21.8,21.85,21.65,21.8,686141,21.98,23.3,23.91,23.01,0.88
20260507,21.8,21.9,21.65,21.85,609599,21.89,23.13,23.88,22.91,0.8
20260508,21.85,22.05,21.85,21.95,491126,21.85,22.95,23.84,22.83,0.66
20260511,21.95,22.3,21.9,22.15,354250,21.91,22.79,23.8,22.78,0.49
20260512,22.3,22.3,22,22.05,394364,21.96,22.63,23.77,22.72,0.57
20260513,22,22.15,21.95,22.1,556069,22.02,22.48,23.74,22.66,0.84
20260514,21.95,22.15,21.8,21.8,429912,22.01,22.31,23.7,22.59,0.74
20260515,21.8,21.95,21.35,21.4,874382,21.9,22.21,23.65,22.49,1.56
20260518,21.4,21.4,21.1,21.1,321875,21.69,22.11,23.61,22.38,0.6
20260519,21.15,21.4,21.15,21.2,257891,21.52,22.02,23.56,22.28,0.51
20260520,21.2,21.4,21.2,21.35,235334,21.37,21.93,23.52,22.2,0.48
20260521,21.35,21.5,21.35,21.45,166281,21.3,21.86,23.47,22.14,0.35
20260522,21.45,21.6,21.25,21.3,443729,21.28,21.8,23.42,22.07,0.98
20260523,21.45,21.6,21.25,21.3,443729,21.32,21.76,23.37,22,0.99
20260524,21.45,21.6,21.25,21.3,443729,21.34,21.72,23.31,21.95,1.01
20260525,21.5,21.9,21.45,21.75,993511,21.42,21.7,23.27,21.93,2.13
20260526,21.5,21.9,21.45,21.75,993511,21.48,21.67,23.22,21.91,1.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.92
- over_600_ratio: 48.23
- over_800_ratio: 46.68
- over_1000_ratio: 44.65
- over_400_change_1w: -0.01
- over_800_change_1w: -0.27
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.52,,46.7,,44.66,,0,False,False
20260508,49.82,0.3,47,0.3,44.65,-0.01,1,False,True
20260515,49.93,0.11,46.95,-0.05,44.65,0,2,False,False
20260522,49.92,-0.01,46.68,-0.27,44.65,0,0,False,False
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
