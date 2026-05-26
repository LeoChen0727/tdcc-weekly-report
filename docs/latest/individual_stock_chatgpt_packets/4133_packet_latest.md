# INDIVIDUAL STOCK CHATGPT PACKET - 4133 亞諾法

## Metadata
- generated_at: 2026-05-26 23:01:31 Asia/Taipei
- stock_id: 4133
- stock_name: 亞諾法
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4133_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4133_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4133_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4133_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4133_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4133_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4133_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4133_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4133_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4133_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4133_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4133_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4133_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4133.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4133.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4133.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4133.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4133.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4133.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4133_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4133_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4133_latest.md?ref=main

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
- open: 21
- high: 21.25
- low: 20.8
- close: 20.85
- volume: 154073
- ma5: 21.1
- ema23_primary: 21.53
- distance_to_ema23_pct: -3.17
- ma20: 21.42
- ma60: 22.51
- ma120: 23.15
- return_5d: -1.42
- return_20d: -3.7
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: -2.65
- distance_to_high_60_pct: -18.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,21.75,21.75,21.55,21.6,101569,22.55,-4.2,22.44,23.85,1.06
20260429,21.85,21.85,21.55,21.75,70934,22.48,-3.25,22.39,23.81,0.73
20260430,21.8,22.05,21.45,21.6,171554,22.41,-3.6,22.34,23.77,1.76
20260504,21.65,21.65,21.3,21.4,248914,22.32,-4.13,22.27,23.73,2.34
20260505,21.4,21.85,21.3,21.55,141921,22.26,-3.18,22.2,23.69,1.33
20260506,21.95,21.95,21.6,21.9,149659,22.23,-1.48,22.17,23.62,1.33
20260507,22.1,22.25,21.9,21.95,141950,22.21,-1.15,22.14,23.5,1.25
20260508,22.5,22.85,21.95,21.95,211680,22.18,-1.05,22.13,23.4,1.74
20260511,21.8,22,21.65,21.75,94188,22.15,-1.8,22.1,23.32,0.76
20260512,21.75,21.75,21.05,21.4,278085,22.09,-3.1,22.04,23.24,2.06
20260513,21.4,21.7,21.25,21.4,175669,22.03,-2.85,21.98,23.17,1.24
20260514,21.4,21.4,20.95,21.2,376885,21.96,-3.46,21.91,23.09,2.44
20260515,21.35,21.35,20.7,20.8,372720,21.86,-4.86,21.81,23,2.21
20260518,20.5,21.55,20.5,21.45,322246,21.83,-1.73,21.76,22.93,1.79
20260519,21.6,21.8,21.15,21.15,128852,21.77,-2.86,21.7,22.86,0.71
20260520,21.25,21.25,21,21.05,69643,21.71,-3.05,21.63,22.79,0.39
20260521,21.1,21.3,20.85,21.15,261182,21.66,-2.38,21.57,22.72,1.4
20260522,21.3,21.3,21,21.3,145560,21.63,-1.55,21.51,22.65,0.77
20260525,21.3,21.4,21.05,21.15,154388,21.59,-2.06,21.46,22.58,0.8
20260526,21,21.25,20.8,20.85,154073,21.53,-3.17,21.42,22.51,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 22.84
- over_600_ratio: 19.65
- over_800_ratio: 18.53
- over_1000_ratio: 18.53
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
20260430,23.67,,18.53,,18.53,,0,False,False
20260508,23.67,0,18.53,0,18.53,0,0,False,False
20260515,22.84,-0.83,18.53,0,18.53,0,0,False,False
20260522,22.84,0,18.53,0,18.53,0,0,False,False
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
