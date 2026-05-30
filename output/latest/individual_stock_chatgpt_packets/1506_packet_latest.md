# INDIVIDUAL STOCK CHATGPT PACKET - 1506 正道

## Metadata
- generated_at: 2026-05-30 23:41:00 Asia/Taipei
- stock_id: 1506
- stock_name: 正道
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1506_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1506_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1506_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1506_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1506_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1506_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1506_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1506_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1506_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1506_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1506_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1506_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1506_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1506.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1506.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1506.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1506.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1506.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1506.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1506_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1506_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1506_latest.md?ref=main

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
- open: 10.7
- high: 10.7
- low: 10.15
- close: 10.3
- volume: 353330
- ma5: 10.3
- ema23_primary: 10.47
- distance_to_ema23_pct: -1.63
- ma20: 10.37
- ma60: 10.94
- ma120: 11.42
- return_5d: -5.94
- return_20d: -4.63
- volume_ratio: 1.19
- distance_to_ma20_pct_auxiliary: -0.68
- distance_to_high_60_pct: -11.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,10.8,10.95,10.6,10.65,220179,11.08,-3.9,11.05,11.45,1.07
20260505,10.65,10.65,10.45,10.5,304872,11.03,-4.84,11.03,11.42,1.43
20260506,10.7,10.7,10.5,10.5,228931,10.99,-4.45,11,11.38,1.03
20260507,10.5,10.6,10.4,10.5,286693,10.95,-4.1,10.97,11.35,1.27
20260508,10.5,10.6,10.45,10.5,130170,10.91,-3.77,10.94,11.31,0.58
20260511,10.5,10.8,10.5,10.75,172999,10.9,-1.36,10.93,11.28,0.76
20260512,10.7,10.7,10.6,10.65,62664,10.88,-2.09,10.91,11.26,0.27
20260513,10.55,10.65,10.35,10.35,344731,10.83,-4.46,10.86,11.23,1.45
20260514,10.35,10.4,10.05,10.2,315998,10.78,-5.38,10.8,11.21,1.31
20260515,10.3,10.3,10,10.15,278590,10.73,-5.39,10.76,11.18,1.13
20260518,10.05,10.1,9.95,10.1,179945,10.68,-5.39,10.71,11.15,0.72
20260519,10.2,10.2,9.99,10,92078,10.62,-5.83,10.65,11.12,0.39
20260520,10,10.2,9.98,10,138682,10.57,-5.37,10.6,11.09,0.59
20260521,10,10.15,9.98,10.1,208781,10.53,-4.07,10.55,11.07,0.9
20260522,10.1,11.1,10,10.95,904266,10.56,3.66,10.54,11.05,3.52
20260525,10.75,10.75,10.35,10.35,427858,10.55,-1.86,10.52,11.03,1.57
20260526,10.35,10.6,10,10.3,336687,10.53,-2.14,10.47,11,1.33
20260527,10.35,10.35,10,10.1,466796,10.49,-3.72,10.41,10.98,1.74
20260528,10.2,10.6,10.15,10.45,497525,10.49,-0.35,10.39,10.96,1.75
20260529,10.7,10.7,10.15,10.3,353330,10.47,-1.63,10.37,10.94,1.19
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 77.37
- over_600_ratio: 74.18
- over_800_ratio: 72.55
- over_1000_ratio: 71.99
- over_400_change_1w: -0.19
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,77.56,,72.6,,72.02,,0,False,False
20260508,77.61,0.05,72.62,0.02,72.04,0.02,1,True,True
20260515,77.58,-0.03,72.56,-0.06,72.01,-0.03,0,False,False
20260522,77.56,-0.02,72.55,-0.01,71.99,-0.02,0,False,False
20260529,77.37,-0.19,72.55,0,71.99,0,0,False,False
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
