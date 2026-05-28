# INDIVIDUAL STOCK CHATGPT PACKET - 1720 生達

## Metadata
- generated_at: 2026-05-28 19:31:40 Asia/Taipei
- stock_id: 1720
- stock_name: 生達
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1720_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1720_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1720_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1720_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1720_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1720_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1720_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1720_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1720_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1720_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1720_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1720_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1720_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1720.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1720.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1720.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1720.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1720.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1720.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1720_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1720_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1720_latest.md?ref=main

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
- open: 61.2
- high: 61.4
- low: 60.8
- close: 61.4
- volume: 302505
- ma5: 61.54
- ema23_primary: 61.65
- distance_to_ema23_pct: -0.41
- ma20: 61.41
- ma60: 62.47
- ma120: 61.86
- return_5d: -1.6
- return_20d: 0
- volume_ratio: 1.15
- distance_to_ma20_pct_auxiliary: -0.02
- distance_to_high_60_pct: -6.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,61.4,62,61,61,170765,62.2,-1.94,62.56,62.57,0.59
20260504,61,61.4,60.5,60.7,400657,62.08,-2.22,62.4,62.56,1.39
20260505,60.9,61.2,60.5,61,140924,61.99,-1.6,62.25,62.55,0.5
20260506,61.5,61.5,60.9,61.3,184036,61.93,-1.02,62.12,62.53,0.66
20260507,61,61.4,60.9,61.2,236313,61.87,-1.08,61.99,62.52,0.85
20260508,61,61.5,60.8,61.1,241638,61.81,-1.14,61.87,62.51,0.87
20260511,61.2,61.4,60.9,61.1,213948,61.75,-1.05,61.77,62.51,0.77
20260512,61.2,61.2,60.8,60.8,223917,61.67,-1.41,61.65,62.51,0.8
20260513,61.8,62.1,61.3,61.6,406934,61.66,-0.1,61.56,62.53,1.41
20260514,61.6,62.5,61.4,61.8,389890,61.67,0.2,61.48,62.56,1.3
20260515,62.1,62.1,61.2,61.6,244840,61.67,-0.11,61.38,62.58,0.81
20260518,61.6,61.6,61,61.3,266248,61.64,-0.55,61.29,62.58,0.9
20260519,61.7,62.7,61.7,61.8,293343,61.65,0.24,61.28,62.6,1.06
20260520,61.8,62,61.6,61.8,144026,61.66,0.22,61.28,62.62,0.54
20260521,62.2,62.4,62,62.4,181414,61.72,1.09,61.3,62.65,0.7
20260522,62.2,62.2,61.8,62.1,195218,61.76,0.56,61.36,62.66,0.83
20260525,62.1,62.1,61.2,61.4,403869,61.73,-0.53,61.38,62.66,1.66
20260526,61.4,61.6,61,61.6,227896,61.72,-0.19,61.41,62.61,0.95
20260527,61.2,61.3,60.8,61.2,396745,61.67,-0.77,61.41,62.54,1.56
20260528,61.2,61.4,60.8,61.4,302505,61.65,-0.41,61.41,62.47,1.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.24
- over_600_ratio: 62.77
- over_800_ratio: 62.42
- over_1000_ratio: 59.79
- over_400_change_1w: -0.02
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.49,,62.62,,59.99,,0,False,False
20260508,65.34,-0.15,62.51,-0.11,59.88,-0.11,0,False,False
20260515,65.26,-0.08,62.44,-0.07,59.81,-0.07,0,False,False
20260522,65.24,-0.02,62.42,-0.02,59.79,-0.02,0,False,False
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
