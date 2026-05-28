# INDIVIDUAL STOCK CHATGPT PACKET - 9908 大台北

## Metadata
- generated_at: 2026-05-28 20:20:43 Asia/Taipei
- stock_id: 9908
- stock_name: 大台北
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9908_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9908_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9908_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9908_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9908_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9908_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9908_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9908_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9908_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9908_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9908_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9908_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9908_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9908.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9908.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9908.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9908.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9908.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9908.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9908_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9908_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9908_latest.md?ref=main

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
- date: 20260528
- open: 29.2
- high: 29.2
- low: 29
- close: 29.05
- volume: 268977
- ma5: 29.11
- ema23_primary: 29.32
- distance_to_ema23_pct: -0.91
- ma20: 29.28
- ma60: 29.88
- ma120: 29.91
- return_5d: -0.51
- return_20d: -2.52
- volume_ratio: 0.77
- distance_to_ma20_pct_auxiliary: -0.79
- distance_to_high_60_pct: -17.24

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,29.65,29.7,29.55,29.6,228266,29.79,-0.65,29.75,30.08,0.5
20260504,29.6,29.65,29.4,29.45,602740,29.77,-1.06,29.73,30.07,1.27
20260505,29.5,29.6,29.45,29.55,168649,29.75,-0.66,29.71,30.07,0.36
20260506,29.7,29.7,29.3,29.5,486241,29.73,-0.76,29.69,30.06,1.01
20260507,29.5,29.6,29.45,29.45,280385,29.7,-0.85,29.67,30.06,0.63
20260508,29.6,29.6,29.4,29.45,268071,29.68,-0.78,29.66,30.05,0.61
20260511,29.5,29.5,29.3,29.35,657423,29.65,-1.03,29.64,30.04,1.44
20260512,29.5,29.5,29.3,29.3,561213,29.63,-1.1,29.61,30.03,1.19
20260513,29.35,29.4,29.2,29.4,592387,29.61,-0.7,29.59,30.03,1.27
20260514,29.4,29.5,29.25,29.25,458624,29.58,-1.1,29.56,30.02,1.04
20260515,29.4,29.4,29.1,29.1,426858,29.54,-1.48,29.52,30.01,0.96
20260518,29.15,29.2,29.05,29.1,282486,29.5,-1.36,29.48,30,0.64
20260519,29.1,29.3,29.1,29.25,284558,29.48,-0.78,29.45,29.99,0.67
20260520,29.3,29.3,29.1,29.15,183456,29.45,-1.03,29.43,29.97,0.44
20260521,29.2,29.3,29.15,29.2,198110,29.43,-0.79,29.4,29.96,0.48
20260522,29.2,29.3,29.15,29.2,205559,29.41,-0.72,29.38,29.95,0.57
20260525,29.25,29.3,29.05,29.05,318560,29.38,-1.13,29.36,29.93,0.89
20260526,29.1,29.15,29.05,29.1,262188,29.36,-0.88,29.34,29.92,0.75
20260527,29.1,29.15,29.05,29.15,282758,29.34,-0.65,29.32,29.9,0.8
20260528,29.2,29.2,29,29.05,268977,29.32,-0.91,29.28,29.88,0.77
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.44
- over_600_ratio: 77.97
- over_800_ratio: 76.39
- over_1000_ratio: 74.13
- over_400_change_1w: 0.18
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.16,,76.36,,74.3,,0,False,False
20260508,80.25,0.09,76.36,0,74.3,0,1,False,False
20260515,80.26,0.01,76.38,0.02,74.12,-0.18,2,False,True
20260522,80.44,0.18,76.39,0.01,74.13,0.01,3,True,True
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
