# INDIVIDUAL STOCK CHATGPT PACKET - 2506 太設

## Metadata
- generated_at: 2026-05-26 23:53:24 Asia/Taipei
- stock_id: 2506
- stock_name: 太設
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2506_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2506_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2506_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2506_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2506_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2506_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2506_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2506_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2506_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2506_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2506_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2506_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2506_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2506.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2506.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2506.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2506.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2506.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2506.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2506_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2506_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2506_latest.md?ref=main

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
- open: 8.6
- high: 8.63
- low: 8.58
- close: 8.62
- volume: 157296
- ma5: 8.65
- ema23_primary: 8.71
- distance_to_ema23_pct: -1.01
- ma20: 8.69
- ma60: 8.85
- ma120: 9.04
- return_5d: -0.46
- return_20d: -1.15
- volume_ratio: 0.92
- distance_to_ma20_pct_auxiliary: -0.78
- distance_to_high_60_pct: -5.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,8.79,8.84,8.66,8.74,139775,8.9,-1.79,8.92,8.95,1.07
20260429,8.83,8.85,8.7,8.8,65089,8.89,-1.02,8.91,8.95,0.51
20260430,8.75,8.89,8.72,8.89,149539,8.89,-0.01,8.91,8.95,1.16
20260504,8.92,8.92,8.82,8.84,134040,8.89,-0.52,8.9,8.94,1.04
20260505,8.8,8.84,8.73,8.74,120622,8.87,-1.51,8.89,8.94,0.93
20260506,8.75,8.84,8.72,8.72,95498,8.86,-1.6,8.88,8.94,0.72
20260507,8.73,8.79,8.7,8.7,87239,8.85,-1.67,8.87,8.93,0.68
20260508,8.8,8.8,8.66,8.75,80570,8.84,-1.02,8.86,8.93,0.62
20260511,8.75,8.79,8.66,8.66,193547,8.82,-1.87,8.84,8.92,1.5
20260512,8.67,8.68,8.5,8.6,445408,8.81,-2.34,8.82,8.92,3.06
20260513,8.53,8.62,8.41,8.6,287530,8.79,-2.15,8.8,8.91,1.9
20260514,8.53,8.64,8.53,8.58,167965,8.77,-2.18,8.78,8.9,1.11
20260515,8.59,8.6,8.5,8.6,334335,8.76,-1.8,8.76,8.89,2.08
20260518,8.59,8.62,8.55,8.62,142217,8.75,-1.44,8.74,8.89,0.88
20260519,8.65,8.7,8.52,8.66,190578,8.74,-0.9,8.73,8.88,1.14
20260520,8.63,8.68,8.59,8.64,166138,8.73,-1.04,8.72,8.87,0.98
20260521,8.69,8.69,8.64,8.68,145442,8.73,-0.53,8.71,8.87,0.84
20260522,8.7,8.71,8.62,8.67,126724,8.72,-0.59,8.7,8.86,0.76
20260525,8.71,8.71,8.6,8.65,174591,8.72,-0.75,8.69,8.86,1.04
20260526,8.6,8.63,8.58,8.62,157296,8.71,-1.01,8.69,8.85,0.92
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 76.68
- over_600_ratio: 74.12
- over_800_ratio: 72.66
- over_1000_ratio: 71.95
- over_400_change_1w: 0.22
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,76.32,,72.56,,71.85,,0,False,False
20260508,76.34,0.02,72.57,0.01,71.86,0.01,1,True,True
20260515,76.46,0.12,72.62,0.05,71.91,0.05,2,False,True
20260522,76.68,0.22,72.66,0.04,71.95,0.04,3,True,True
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
