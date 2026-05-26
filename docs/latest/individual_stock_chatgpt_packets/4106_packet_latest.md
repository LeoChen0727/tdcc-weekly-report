# INDIVIDUAL STOCK CHATGPT PACKET - 4106 雃博

## Metadata
- generated_at: 2026-05-26 23:01:29 Asia/Taipei
- stock_id: 4106
- stock_name: 雃博
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4106_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4106_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4106_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4106_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4106_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4106_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4106_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4106_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4106_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4106_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4106_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4106_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4106_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4106.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4106.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4106.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4106.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4106.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4106.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4106_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4106_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4106_latest.md?ref=main

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
- open: 23.35
- high: 23.45
- low: 23.15
- close: 23.45
- volume: 125109
- ma5: 23.25
- ema23_primary: 22.8
- distance_to_ema23_pct: 2.84
- ma20: 22.68
- ma60: 22.51
- ma120: 22.49
- return_5d: 1.74
- return_20d: 6.35
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: 3.4
- distance_to_high_60_pct: -0.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.2,22.2,22,22.2,72856,22.37,-0.75,22.32,22.65,0.95
20260429,22.3,22.3,22.1,22.2,38112,22.35,-0.69,22.33,22.63,0.5
20260430,22.2,22.3,22,22.3,129731,22.35,-0.22,22.34,22.62,1.72
20260504,22.1,22.3,22.05,22.3,101700,22.35,-0.2,22.35,22.61,1.32
20260505,22.1,22.25,22.05,22.1,68176,22.33,-1.01,22.34,22.59,0.88
20260506,22.1,22.25,22.1,22.25,106328,22.32,-0.31,22.33,22.57,1.3
20260507,22.25,22.25,22.1,22.2,94152,22.31,-0.49,22.33,22.55,1.13
20260508,22.2,22.25,22.05,22.2,87999,22.3,-0.45,22.32,22.53,1.04
20260511,22.3,22.3,22.1,22.2,58351,22.29,-0.41,22.31,22.52,0.69
20260512,22.15,22.25,22.05,22.2,134973,22.28,-0.38,22.31,22.5,1.52
20260513,22.45,23.4,22.25,23.35,1039903,22.37,4.37,22.36,22.51,7.48
20260514,23.5,23.55,22.75,22.9,388263,22.42,2.16,22.39,22.5,2.53
20260515,22.85,22.9,22.7,22.9,132220,22.46,1.97,22.41,22.49,0.85
20260518,22.75,23.15,22.7,23,117761,22.5,2.21,22.43,22.49,0.75
20260519,23,23.1,22.8,23.05,79108,22.55,2.23,22.45,22.49,0.5
20260520,23.05,23.05,22.9,23.05,74264,22.59,2.04,22.48,22.49,0.47
20260521,23.05,23.3,23,23.1,92189,22.63,2.07,22.5,22.49,0.58
20260522,23.1,23.35,23.05,23.3,103265,22.69,2.7,22.56,22.5,0.67
20260525,23.1,23.35,23.05,23.35,155187,22.74,2.67,22.61,22.5,0.97
20260526,23.35,23.45,23.15,23.45,125109,22.8,2.84,22.68,22.51,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.29
- over_600_ratio: 46.93
- over_800_ratio: 46.93
- over_1000_ratio: 46.12
- over_400_change_1w: -0.01
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.25,,46.86,,46.05,,0,False,False
20260508,50.28,0.03,46.89,0.03,46.08,0.03,1,True,True
20260515,50.3,0.02,46.91,0.02,46.1,0.02,2,True,True
20260522,50.29,-0.01,46.93,0.02,46.12,0.02,3,False,True
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
