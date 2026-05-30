# INDIVIDUAL STOCK CHATGPT PACKET - 2115 六暉-KY

## Metadata
- generated_at: 2026-05-30 23:41:16 Asia/Taipei
- stock_id: 2115
- stock_name: 六暉-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 270
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2115_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2115_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2115_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2115_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2115_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2115_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2115_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2115_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2115_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2115_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2115_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2115_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2115_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2115.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2115.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2115.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2115.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2115.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2115.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2115_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2115_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2115_latest.md?ref=main

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
- open: 22
- high: 22.3
- low: 21.5
- close: 21.6
- volume: 187260
- ma5: 21.13
- ema23_primary: 20.99
- distance_to_ema23_pct: 2.89
- ma20: 20.8
- ma60: 21.48
- ma120: 23.11
- return_5d: 4.35
- return_20d: 1.89
- volume_ratio: 1.03
- distance_to_ma20_pct_auxiliary: 3.83
- distance_to_high_60_pct: -10.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,21.2,21.2,20.8,21,148852,21.57,-2.66,21.48,22.68,1.86
20260505,21,21,20.8,20.8,107733,21.51,-3.3,21.45,22.6,1.32
20260506,20.8,20.95,20.65,20.9,124492,21.46,-2.6,21.42,22.53,1.43
20260507,21.15,22.9,21.15,21.45,251338,21.46,-0.03,21.42,22.46,2.63
20260508,21.75,21.75,21.25,21.3,66099,21.44,-0.67,21.41,22.4,0.68
20260511,21.35,21.35,20.8,20.9,216300,21.4,-2.33,21.38,22.33,2.02
20260512,21.1,21.1,20.55,20.75,317519,21.34,-2.79,21.34,22.27,2.63
20260513,20.7,20.8,20.65,20.75,119523,21.3,-2.56,21.31,22.21,0.97
20260514,20.75,20.75,20.4,20.45,250812,21.22,-3.65,21.25,22.14,1.87
20260515,20.35,20.4,19.9,20,296193,21.12,-5.32,21.17,22.07,2.18
20260518,19.9,19.9,19.7,19.9,249464,21.02,-5.33,21.08,22,1.74
20260519,20.05,20.4,19.8,20.25,206041,20.96,-3.37,21.01,21.93,1.36
20260520,20.35,20.5,20.35,20.4,154052,20.91,-2.44,20.95,21.87,1.01
20260521,20.55,20.9,20.4,20.85,32453,20.91,-0.26,20.91,21.81,0.22
20260522,20.65,20.85,20.65,20.7,29828,20.89,-0.9,20.86,21.75,0.21
20260525,20.7,20.7,20.55,20.6,99586,20.86,-1.27,20.82,21.68,0.68
20260526,20.8,20.8,20.55,20.75,78466,20.85,-0.5,20.78,21.62,0.54
20260527,20.7,20.75,20.45,20.75,218993,20.85,-0.46,20.75,21.56,1.41
20260528,21.4,22.4,21.35,21.95,481422,20.94,4.83,20.78,21.52,2.73
20260529,22,22.3,21.5,21.6,187260,20.99,2.89,20.8,21.48,1.03
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 69.4
- over_600_ratio: 65.18
- over_800_ratio: 60.54
- over_1000_ratio: 58.8
- over_400_change_1w: -0.49
- over_800_change_1w: -0.68
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.37,,61.62,,59.18,,0,False,False
20260508,69.41,0.04,61.66,0.04,59.22,0.04,1,True,True
20260515,69.52,0.11,61.77,0.11,58.4,-0.82,2,False,True
20260522,69.89,0.37,61.22,-0.55,58.72,0.32,3,False,True
20260529,69.4,-0.49,60.54,-0.68,58.8,0.08,4,False,True
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
