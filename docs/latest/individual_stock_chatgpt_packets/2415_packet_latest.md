# INDIVIDUAL STOCK CHATGPT PACKET - 2415 錩新

## Metadata
- generated_at: 2026-05-26 22:18:33 Asia/Taipei
- stock_id: 2415
- stock_name: 錩新
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2415_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2415_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2415_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2415_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2415_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2415_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2415_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2415_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2415_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2415_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2415_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2415_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2415_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2415.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2415.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2415.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2415.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2415.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2415.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2415_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2415_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2415_latest.md?ref=main

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
- open: 27.05
- high: 27.05
- low: 26.7
- close: 26.75
- volume: 104516
- ma5: 26.99
- ema23_primary: 27.2
- distance_to_ema23_pct: -1.67
- ma20: 26.96
- ma60: 27.96
- ma120: 27.26
- return_5d: 1.71
- return_20d: 0.38
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: -0.78
- distance_to_high_60_pct: -14.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,27,27.25,26.55,26.85,163720,28.39,-5.43,28.79,28.03,0.58
20260429,26.9,27.15,26.7,27.15,116598,28.29,-4.03,28.69,28.02,0.42
20260430,27.25,27.25,26.6,26.6,182388,28.15,-5.5,28.58,28,0.65
20260504,26.6,27.4,26.6,26.8,74458,28.04,-4.41,28.41,27.98,0.29
20260505,26.7,27,26.7,27,133218,27.95,-3.4,28.27,27.97,0.53
20260506,27.15,27.35,26.6,27.2,134694,27.89,-2.46,28.09,27.97,0.6
20260507,27.3,27.8,27.25,27.6,124725,27.86,-0.94,27.98,27.98,0.62
20260508,27.8,28.45,27.7,28,204206,27.87,0.45,27.94,28.01,1.03
20260511,27.8,28.25,27.55,27.6,204539,27.85,-0.9,27.89,28.03,1.07
20260512,27.65,27.65,26.95,27,187742,27.78,-2.81,27.79,28.04,0.98
20260513,27.15,27.15,26.6,26.65,151864,27.69,-3.74,27.66,28.05,0.8
20260514,26.65,27.15,26.55,26.65,150522,27.6,-3.44,27.55,28.05,0.79
20260515,26.9,27.25,26.3,26.5,291100,27.51,-3.67,27.42,28.04,1.47
20260518,26.6,26.7,26.15,26.35,202895,27.41,-3.87,27.29,28.05,1.02
20260519,26.5,26.65,26.2,26.3,116359,27.32,-3.73,27.16,28.02,0.61
20260520,26.25,26.55,26.25,26.45,175404,27.25,-2.92,27.04,28.01,0.91
20260521,26.75,27.5,26.75,27.5,179048,27.27,0.85,26.98,28,0.94
20260522,27.5,27.5,27.25,27.25,150903,27.27,-0.06,26.95,27.99,0.84
20260525,27.5,27.5,26.95,27,159229,27.24,-0.9,26.95,27.98,0.97
20260526,27.05,27.05,26.7,26.75,104516,27.2,-1.67,26.96,27.96,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.73
- over_600_ratio: 61.65
- over_800_ratio: 60.17
- over_1000_ratio: 59.12
- over_400_change_1w: 0.28
- over_800_change_1w: -0.17
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.36,,60.25,,59.27,,0,False,False
20260508,64.49,0.13,60.38,0.13,60.38,1.11,1,True,True
20260515,64.45,-0.04,60.34,-0.04,59.24,-1.14,0,False,False
20260522,64.73,0.28,60.17,-0.17,59.12,-0.12,1,False,False
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
