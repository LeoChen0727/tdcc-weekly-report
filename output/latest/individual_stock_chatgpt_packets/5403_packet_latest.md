# INDIVIDUAL STOCK CHATGPT PACKET - 5403 中菲

## Metadata
- generated_at: 2026-05-26 22:19:48 Asia/Taipei
- stock_id: 5403
- stock_name: 中菲
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5403_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5403_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5403_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5403_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5403_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5403_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5403_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5403_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5403_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5403_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5403_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5403_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5403_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5403.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5403.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5403.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5403.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5403.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5403.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5403_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5403_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5403_latest.md?ref=main

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
- open: 85.5
- high: 85.5
- low: 84.5
- close: 84.9
- volume: 85000
- ma5: 85.7
- ema23_primary: 89.89
- distance_to_ema23_pct: -5.55
- ma20: 90.03
- ma60: 98.51
- ma120: 106.41
- return_5d: -0.12
- return_20d: -8.12
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: -5.69
- distance_to_high_60_pct: -23.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,92,92.6,91.7,92.5,145000,96.98,-4.61,95.64,105.32,0.97
20260429,92.1,93.8,92,93.7,107000,96.7,-3.1,95.33,104.99,0.71
20260430,93.1,93.8,93.1,93.8,143000,96.46,-2.76,95.09,104.65,0.93
20260504,93.8,93.8,93,93.8,111000,96.24,-2.53,94.86,104.3,0.72
20260505,93.8,96.5,93.8,96.5,141000,96.26,0.25,94.78,104.03,0.89
20260506,96.6,96.6,95.4,95.5,71000,96.2,-0.72,94.64,103.75,0.44
20260507,95.3,95.3,94.1,94.4,69000,96.05,-1.72,94.39,103.45,0.43
20260508,91.2,93.5,91.2,92.9,240000,95.79,-3.01,94.05,103.13,1.4
20260511,92.9,93,92.4,92.6,162000,95.52,-3.06,93.72,102.83,0.91
20260512,92.6,92.7,90.8,91,233000,95.14,-4.35,93.51,102.49,1.42
20260513,90.7,91,90.6,90.8,105000,94.78,-4.2,93.45,102.17,0.73
20260514,90.8,90.8,88,88.3,451000,94.24,-6.3,93.17,101.78,2.93
20260515,88,88.3,85.5,85.5,450000,93.51,-8.57,92.72,101.35,2.61
20260518,85.4,86.3,85.3,85.7,207000,92.86,-7.71,92.29,100.95,1.16
20260519,85.8,86.1,85,85,110000,92.21,-7.82,91.89,100.53,0.62
20260520,85.2,87,85.2,86,126000,91.69,-6.2,91.51,100.13,0.7
20260521,87.4,87.4,85.9,86.2,87000,91.23,-5.52,91.14,99.72,0.49
20260522,86.2,86.2,85.5,85.9,86000,90.79,-5.38,90.78,99.32,0.49
20260525,85.9,86.5,85.5,85.5,86000,90.35,-5.36,90.4,98.91,0.5
20260526,85.5,85.5,84.5,84.9,85000,89.89,-5.55,90.03,98.51,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.76
- over_600_ratio: 37.55
- over_800_ratio: 33.16
- over_1000_ratio: 29.77
- over_400_change_1w: 0.22
- over_800_change_1w: 0.12
- over_1000_change_1w: 0.12
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.99,,32.48,,28.92,,0,False,False
20260508,45.18,0.19,31.74,-0.74,29.38,0.46,1,False,True
20260515,45.54,0.36,33.04,1.3,29.65,0.27,2,True,True
20260522,45.76,0.22,33.16,0.12,29.77,0.12,3,True,True
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
