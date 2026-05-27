# INDIVIDUAL STOCK CHATGPT PACKET - 3052 夆典

## Metadata
- generated_at: 2026-05-27 21:26:55 Asia/Taipei
- stock_id: 3052
- stock_name: 夆典
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3052_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3052_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3052_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3052_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3052_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3052_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3052_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3052_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3052_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3052_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3052_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3052_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3052_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3052.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3052.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3052.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3052.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3052.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3052.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3052_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3052_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3052_latest.md?ref=main

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
- date: 20260527
- open: 10.45
- high: 10.45
- low: 10.3
- close: 10.3
- volume: 926780
- ma5: 10.48
- ema23_primary: 10.63
- distance_to_ema23_pct: -3.09
- ma20: 10.61
- ma60: 10.93
- ma120: 11.29
- return_5d: -1.44
- return_20d: -3.74
- volume_ratio: 1.64
- distance_to_ma20_pct_auxiliary: -2.94
- distance_to_high_60_pct: -10.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,10.6,10.7,10.5,10.7,699550,10.94,-2.18,10.94,11.23,1.04
20260430,10.65,10.65,10.6,10.65,397233,10.91,-2.42,10.92,11.21,0.58
20260504,10.6,10.65,10.55,10.65,624819,10.89,-2.22,10.9,11.19,0.91
20260505,10.6,11.05,10.6,11,1424175,10.9,0.91,10.91,11.18,1.91
20260506,11,11,10.7,10.75,624144,10.89,-1.27,10.89,11.17,0.83
20260507,10.75,10.8,10.7,10.75,322571,10.88,-1.17,10.88,11.15,0.44
20260508,10.75,10.75,10.6,10.65,527693,10.86,-1.92,10.86,11.14,0.76
20260511,10.8,10.8,10.7,10.7,326077,10.84,-1.34,10.84,11.13,0.49
20260512,10.75,10.85,10.65,10.75,423627,10.84,-0.8,10.83,11.12,0.63
20260513,10.8,10.8,10.6,10.65,422635,10.82,-1.58,10.81,11.1,0.64
20260514,10.65,10.7,10.55,10.55,698474,10.8,-2.3,10.79,11.09,1.06
20260515,10.65,10.65,10.5,10.55,507216,10.78,-2.12,10.76,11.07,0.78
20260518,10.5,10.65,10.4,10.55,723537,10.76,-1.94,10.73,11.06,1.1
20260519,10.55,10.6,10.45,10.5,326092,10.74,-2.21,10.71,11.04,0.5
20260520,10.5,10.5,10.4,10.45,298836,10.71,-2.46,10.69,11.02,0.48
20260521,10.45,10.55,10.45,10.5,230321,10.7,-1.83,10.66,11,0.4
20260522,10.55,10.55,10.45,10.55,266947,10.68,-1.25,10.64,10.99,0.49
20260525,10.6,10.6,10.5,10.6,572964,10.68,-0.72,10.64,10.97,1.07
20260526,10.6,10.6,10.4,10.45,929934,10.66,-1.95,10.63,10.95,1.75
20260527,10.45,10.45,10.3,10.3,926780,10.63,-3.09,10.61,10.93,1.64
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.22
- over_600_ratio: 52.76
- over_800_ratio: 50.4
- over_1000_ratio: 48.1
- over_400_change_1w: -0.03
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.28,,50.36,,48.04,,0,False,False
20260508,56.37,0.09,50.91,0.55,48.64,0.6,1,True,True
20260515,56.25,-0.12,50.44,-0.47,48.15,-0.49,0,False,False
20260522,56.22,-0.03,50.4,-0.04,48.1,-0.05,0,False,False
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
