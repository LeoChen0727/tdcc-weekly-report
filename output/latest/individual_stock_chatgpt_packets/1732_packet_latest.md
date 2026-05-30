# INDIVIDUAL STOCK CHATGPT PACKET - 1732 毛寶

## Metadata
- generated_at: 2026-05-30 23:41:08 Asia/Taipei
- stock_id: 1732
- stock_name: 毛寶
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1732_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1732_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1732_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1732_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1732_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1732_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1732_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1732_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1732_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1732_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1732_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1732_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1732_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1732.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1732.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1732.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1732.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1732.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1732.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1732_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1732_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1732_latest.md?ref=main

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
- date: 20260529
- open: 26.75
- high: 26.75
- low: 26.35
- close: 26.35
- volume: 170692
- ma5: 26.43
- ema23_primary: 26.4
- distance_to_ema23_pct: -0.18
- ma20: 26.48
- ma60: 26.24
- ma120: 27.28
- return_5d: -0.75
- return_20d: 2.13
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -0.47
- distance_to_high_60_pct: -6.23

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,26.5,26.6,26,26.35,312484,26.02,1.28,25.96,26.81,2.42
20260505,27,27.4,26.35,26.4,411682,26.05,1.35,25.96,26.79,2.81
20260506,27,27,26,26.25,203425,26.06,0.71,25.96,26.72,1.32
20260507,26.4,26.4,25.8,26.4,151784,26.09,1.18,25.97,26.61,1.12
20260508,26.9,27.65,26.5,26.5,747810,26.13,1.43,26,26.55,4.52
20260511,27.1,27.9,26.6,26.75,678901,26.18,2.18,26.04,26.53,3.5
20260512,26.95,26.95,26.5,26.6,207824,26.21,1.47,26.07,26.5,1.04
20260513,26.8,26.8,26.1,26.15,155757,26.21,-0.22,26.08,26.46,0.77
20260514,26.25,26.65,26.1,26.3,119917,26.22,0.32,26.09,26.43,0.59
20260515,26.1,26.35,25.8,26.15,157678,26.21,-0.23,26.08,26.4,0.76
20260518,27.05,28,26.5,26.5,645007,26.23,1.01,26.1,26.38,2.72
20260519,27.1,27.75,26.7,27.15,1010945,26.31,3.19,26.16,26.38,3.58
20260520,27.6,27.7,26.5,26.7,348214,26.34,1.35,26.2,26.36,1.17
20260521,26.75,26.75,26.3,26.6,266040,26.36,0.89,26.23,26.35,0.87
20260522,26.85,26.9,26.05,26.55,372093,26.38,0.64,26.28,26.33,1.18
20260525,26.6,26.8,26.3,26.4,197884,26.38,0.07,26.32,26.31,0.62
20260526,26.2,26.4,26.1,26.4,111263,26.38,0.06,26.37,26.29,0.35
20260527,26.75,27,26.35,26.4,231136,26.38,0.06,26.42,26.27,0.7
20260528,26.4,26.8,26.3,26.6,359793,26.4,0.75,26.45,26.26,1.06
20260529,26.75,26.75,26.35,26.35,170692,26.4,-0.18,26.48,26.24,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 46.4
- over_600_ratio: 46.4
- over_800_ratio: 46.4
- over_1000_ratio: 44.13
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.4,,46.4,,44.13,,0,False,False
20260508,46.4,0,46.4,0,44.13,0,0,False,False
20260515,46.4,0,46.4,0,44.13,0,0,False,False
20260522,46.4,0,46.4,0,44.13,0,0,False,False
20260529,46.4,0,46.4,0,44.13,0,0,False,False
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
