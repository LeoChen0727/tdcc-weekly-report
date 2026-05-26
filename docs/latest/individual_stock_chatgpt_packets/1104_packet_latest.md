# INDIVIDUAL STOCK CHATGPT PACKET - 1104 環泥

## Metadata
- generated_at: 2026-05-26 22:17:57 Asia/Taipei
- stock_id: 1104
- stock_name: 環泥
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1104_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1104_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1104_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1104_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1104_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1104_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1104_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1104_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1104_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1104_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1104_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1104_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1104_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1104.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1104.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1104.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1104.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1104.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1104.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1104_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1104_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1104_latest.md?ref=main

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
- open: 27.55
- high: 27.8
- low: 27.35
- close: 27.35
- volume: 872295
- ma5: 27.47
- ema23_primary: 28
- distance_to_ema23_pct: -2.32
- ma20: 27.94
- ma60: 28.86
- ma120: 29.61
- return_5d: -0.36
- return_20d: -3.7
- volume_ratio: 1.23
- distance_to_ma20_pct_auxiliary: -2.11
- distance_to_high_60_pct: -9.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,28.5,28.65,28.5,28.5,418518,29.11,-2.1,29.18,29.46,0.59
20260429,28.5,28.8,28.3,28.6,311862,29.07,-1.62,29.12,29.44,0.46
20260430,28.5,28.7,28.3,28.35,530424,29.01,-2.27,29.07,29.41,0.77
20260504,28.35,28.35,28.2,28.25,871367,28.95,-2.41,29,29.38,1.2
20260505,28.25,28.45,28.1,28.25,307727,28.89,-2.21,28.95,29.35,0.42
20260506,28.25,28.45,28.15,28.3,427061,28.84,-1.87,28.89,29.32,0.58
20260507,28.35,28.45,27.9,28.3,1523197,28.79,-1.72,28.84,29.29,2.07
20260508,28.5,28.5,28.15,28.3,571469,28.75,-1.58,28.8,29.27,0.77
20260511,28.3,28.45,28.25,28.3,610558,28.72,-1.45,28.74,29.24,0.81
20260512,28.2,28.55,28.05,28.2,986410,28.67,-1.65,28.68,29.22,1.26
20260513,28.05,28.45,27.9,28.05,1113436,28.62,-1.99,28.63,29.2,1.43
20260514,28,28.15,27.9,27.9,634461,28.56,-2.31,28.56,29.16,0.83
20260515,28,28,27.35,27.35,1742453,28.46,-3.9,28.46,29.12,2.08
20260518,27.35,27.5,27.1,27.35,516594,28.37,-3.59,28.36,29.09,0.65
20260519,27.35,27.65,27.35,27.45,313059,28.29,-2.97,28.27,29.05,0.41
20260520,27.45,27.5,27.3,27.4,610586,28.22,-2.89,28.18,29.02,0.79
20260521,27.5,27.75,27.4,27.5,558105,28.16,-2.33,28.11,28.99,0.72
20260522,27.5,27.6,27.45,27.55,410128,28.11,-1.98,28.05,28.95,0.55
20260525,27.85,27.85,27.5,27.55,820540,28.06,-1.82,27.99,28.91,1.13
20260526,27.55,27.8,27.35,27.35,872295,28,-2.32,27.94,28.86,1.23
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.06
- over_600_ratio: 70.56
- over_800_ratio: 69.14
- over_1000_ratio: 68
- over_400_change_1w: -0.11
- over_800_change_1w: 0.17
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.38,,69.24,,68.09,,0,False,False
20260508,74.28,-0.1,69.26,0.02,68.27,0.18,1,False,True
20260515,74.17,-0.11,68.97,-0.29,68.09,-0.18,0,False,False
20260522,74.06,-0.11,69.14,0.17,68,-0.09,1,False,True
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
