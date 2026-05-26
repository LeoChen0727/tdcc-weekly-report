# INDIVIDUAL STOCK CHATGPT PACKET - 5530 龍巖

## Metadata
- generated_at: 2026-05-26 23:54:23 Asia/Taipei
- stock_id: 5530
- stock_name: 龍巖
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5530_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5530_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5530_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5530_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5530_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5530_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5530_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5530_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5530_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5530_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5530_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5530_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5530_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5530.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5530.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5530.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5530.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5530.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5530.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5530_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5530_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5530_latest.md?ref=main

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
- open: 48.55
- high: 49.5
- low: 46.9
- close: 47
- volume: 48000
- ma5: 47.04
- ema23_primary: 46.68
- distance_to_ema23_pct: 0.68
- ma20: 46.37
- ma60: 47.08
- ma120: 48.41
- return_5d: -0.63
- return_20d: 2.62
- volume_ratio: 0.07
- distance_to_ma20_pct_auxiliary: 1.36
- distance_to_high_60_pct: -12.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,45.9,46.2,45,45,537000,45.78,-1.71,45.55,48.89,1.1
20260429,45.6,45.6,44.6,44.6,403000,45.68,-2.37,45.38,48.72,0.81
20260430,44.6,44.7,44.05,44.05,403000,45.55,-3.29,45.23,48.55,0.8
20260504,44.35,44.4,43.85,44,401000,45.42,-3.12,45.09,48.38,0.79
20260505,44,44.4,43.8,44.2,285000,45.32,-2.46,44.97,48.23,0.56
20260506,44.25,44.9,44.05,44.5,313000,45.25,-1.65,44.85,48.06,0.61
20260507,45.4,47.6,45.25,46.2,1251000,45.33,1.92,44.82,47.94,2.21
20260508,46.2,46.85,45,45.25,479000,45.32,-0.16,44.75,47.83,0.83
20260511,45.35,45.85,45.05,45.1,506000,45.3,-0.45,44.72,47.74,0.91
20260512,47.4,48.95,47.05,48.2,1916000,45.54,5.83,44.9,47.73,3.13
20260513,49.25,49.45,47.7,47.8,1800000,45.73,4.52,45.04,47.71,2.61
20260514,48.2,52.4,48.2,50.1,2062000,46.1,8.69,45.31,47.72,2.68
20260515,50.2,50.8,48.1,48.1,1089000,46.26,3.97,45.47,47.66,1.33
20260518,48.2,48.2,47.3,47.75,506000,46.39,2.94,45.61,47.61,0.61
20260519,47.5,48.3,46.85,47.3,472000,46.46,1.8,45.74,47.55,0.57
20260520,47.3,47.3,45.75,46.7,633000,46.48,0.47,45.87,47.49,0.77
20260521,46.9,47.1,46.25,46.6,488000,46.49,0.23,45.98,47.41,0.6
20260522,46.6,46.7,45.75,46.45,46000,46.49,-0.08,46.09,47.27,0.06
20260525,46.9,48.85,46.9,48.45,48000,46.65,3.85,46.31,47.19,0.06
20260526,48.55,49.5,46.9,47,48000,46.68,0.68,46.37,47.08,0.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.18
- over_600_ratio: 80.66
- over_800_ratio: 79.36
- over_1000_ratio: 78.74
- over_400_change_1w: 0.01
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.22,,78.96,,78.53,,0,False,False
20260508,82.16,-0.06,79.16,0.2,78.52,-0.01,1,False,True
20260515,82.17,0.01,79.34,0.18,78.71,0.19,2,False,True
20260522,82.18,0.01,79.36,0.02,78.74,0.03,3,True,True
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
