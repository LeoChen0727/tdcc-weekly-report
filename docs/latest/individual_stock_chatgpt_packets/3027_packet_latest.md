# INDIVIDUAL STOCK CHATGPT PACKET - 3027 盛達

## Metadata
- generated_at: 2026-05-26 21:25:19 Asia/Taipei
- stock_id: 3027
- stock_name: 盛達
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3027_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3027_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3027_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3027_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3027_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3027_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3027_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3027_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3027_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3027_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3027_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3027_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3027_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3027.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3027.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3027.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3027.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3027.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3027.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3027_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3027_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3027_latest.md?ref=main

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
- open: 19.4
- high: 19.4
- low: 18.55
- close: 19
- volume: 511217
- ma5: 18.18
- ema23_primary: 18.43
- distance_to_ema23_pct: 3.07
- ma20: 18.25
- ma60: 19.68
- ma120: 21.87
- return_5d: 8.26
- return_20d: 6.44
- volume_ratio: 1.31
- distance_to_ma20_pct_auxiliary: 4.11
- distance_to_high_60_pct: -21.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,17.85,17.95,17.65,17.9,308939,19.45,-7.96,19.16,21.7,0.79
20260429,17.9,18.75,17.85,18.5,349137,19.37,-4.49,19.11,21.56,0.88
20260430,18.5,18.7,18.35,18.6,261074,19.31,-3.65,19.09,21.43,0.67
20260504,18.65,19.05,18.45,18.5,259367,19.24,-3.84,19.04,21.29,0.67
20260505,18.25,19.2,18.25,19.1,449083,19.23,-0.66,19.04,21.17,1.12
20260506,19.2,19.2,18.5,18.5,310473,19.17,-3.48,19,21.05,0.76
20260507,18.5,19.15,18.5,19.1,461260,19.16,-0.32,18.99,20.94,1.12
20260508,19.3,19.5,19.05,19.2,568504,19.16,0.19,18.98,20.84,1.34
20260511,18.8,18.8,18.2,18.3,455162,19.09,-4.15,18.95,20.74,1.06
20260512,18.3,18.4,18.1,18.25,279123,19.02,-4.06,18.91,20.64,0.64
20260513,18.05,18.3,17.9,18,275104,18.94,-4.95,18.84,20.54,0.63
20260514,18.05,18.45,17.5,17.55,477327,18.82,-6.75,18.75,20.42,1.09
20260515,17.6,18.1,17.5,17.5,276745,18.71,-6.47,18.66,20.3,0.63
20260518,17.5,17.65,17.2,17.55,231923,18.61,-5.72,18.56,20.21,0.54
20260519,17.7,17.85,17.5,17.55,160276,18.53,-5.27,18.46,20.12,0.38
20260520,17.8,17.8,17.2,17.2,244040,18.41,-6.6,18.34,20.02,0.59
20260521,17.1,17.9,17.1,17.6,390714,18.35,-4.07,18.21,19.93,1
20260522,17.6,18.2,17.4,18.15,546462,18.33,-0.99,18.16,19.84,1.42
20260525,18.3,19.35,18.2,18.95,961564,18.38,3.09,18.19,19.76,2.44
20260526,19.4,19.4,18.55,19,511217,18.43,3.07,18.25,19.68,1.31
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.32
- over_600_ratio: 40.66
- over_800_ratio: 36.34
- over_1000_ratio: 34.89
- over_400_change_1w: 0.38
- over_800_change_1w: -0.12
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.51,,35.72,,34.27,,0,False,False
20260508,45.25,0.74,36.52,0.8,35.07,0.8,1,True,True
20260515,44.94,-0.31,36.46,-0.06,35.01,-0.06,0,False,False
20260522,45.32,0.38,36.34,-0.12,34.89,-0.12,1,False,False
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
