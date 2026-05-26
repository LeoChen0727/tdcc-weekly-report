# INDIVIDUAL STOCK CHATGPT PACKET - 1517 利奇

## Metadata
- generated_at: 2026-05-26 23:00:17 Asia/Taipei
- stock_id: 1517
- stock_name: 利奇
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1517_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1517_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1517_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1517_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1517_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1517_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1517_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1517_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1517_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1517_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1517_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1517_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1517_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1517.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1517.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1517.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1517.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1517.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1517.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1517_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1517_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1517_latest.md?ref=main

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
- open: 10.1
- high: 10.1
- low: 10
- close: 10.05
- volume: 281223
- ma5: 10.03
- ema23_primary: 10.27
- distance_to_ema23_pct: -2.12
- ma20: 10.14
- ma60: 10.95
- ma120: 11.27
- return_5d: 0
- return_20d: -2.9
- volume_ratio: 1.15
- distance_to_ma20_pct_auxiliary: -0.94
- distance_to_high_60_pct: -21.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,10.35,10.5,10.3,10.35,136789,11.03,-6.13,11.03,11.59,0.52
20260429,10.45,10.5,10.4,10.45,76801,10.98,-4.81,10.98,11.55,0.3
20260430,10.45,10.45,10.35,10.4,84423,10.93,-4.84,10.95,11.51,0.33
20260504,10.3,10.35,10.25,10.25,265744,10.87,-5.73,10.9,11.48,1.07
20260505,10.25,10.35,10.2,10.2,159222,10.82,-5.7,10.85,11.43,0.65
20260506,10.35,10.35,10.2,10.25,322495,10.77,-4.82,10.81,11.39,1.28
20260507,10.25,10.3,10.15,10.2,241344,10.72,-4.87,10.76,11.36,0.94
20260508,10.4,10.4,10.1,10.1,191994,10.67,-5.34,10.71,11.32,0.74
20260511,10.1,10.3,10.05,10.2,286552,10.63,-4.05,10.66,11.29,1.08
20260512,10.2,10.2,10.05,10.05,223573,10.58,-5.03,10.6,11.26,0.83
20260513,10.05,10.2,10.05,10.1,313110,10.54,-4.2,10.54,11.23,1.15
20260514,10.25,10.25,10.1,10.1,238911,10.51,-3.86,10.49,11.19,0.91
20260515,10.1,10.25,10,10.05,381771,10.47,-3.99,10.43,11.16,1.41
20260518,10.05,10.05,10,10,231168,10.43,-4.11,10.37,11.13,0.86
20260519,10,10.1,10,10.05,184252,10.4,-3.34,10.32,11.11,0.7
20260520,10.05,10.05,10,10,138991,10.36,-3.51,10.28,11.08,0.56
20260521,10.05,10.15,10,10.05,151657,10.34,-2.78,10.23,11.05,0.66
20260522,10.05,10.1,10,10,423965,10.31,-3,10.19,11.01,1.85
20260525,10,10.15,10,10.05,575411,10.29,-2.31,10.16,10.98,2.32
20260526,10.1,10.1,10,10.05,281223,10.27,-2.12,10.14,10.95,1.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.58
- over_600_ratio: 46.72
- over_800_ratio: 46.05
- over_1000_ratio: 43.65
- over_400_change_1w: 0.06
- over_800_change_1w: 0.39
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.32,,45.62,,43.62,,0,False,False
20260508,48.44,0.12,45.63,0.01,43.62,0,1,False,True
20260515,48.52,0.08,45.66,0.03,43.65,0.03,2,True,True
20260522,48.58,0.06,46.05,0.39,43.65,0,3,False,True
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
