# INDIVIDUAL STOCK CHATGPT PACKET - 1218 泰山

## Metadata
- generated_at: 2026-05-30 23:40:51 Asia/Taipei
- stock_id: 1218
- stock_name: 泰山
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1218_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1218_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1218_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1218_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1218_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1218_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1218_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1218_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1218_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1218_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1218_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1218_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1218_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1218.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1218.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1218.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1218.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1218.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1218.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1218_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1218_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1218_latest.md?ref=main

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
- open: 18.65
- high: 18.85
- low: 18.6
- close: 18.75
- volume: 914125
- ma5: 18.53
- ema23_primary: 18.7
- distance_to_ema23_pct: 0.26
- ma20: 18.7
- ma60: 18.9
- ma120: 18.56
- return_5d: 0.54
- return_20d: -1.06
- volume_ratio: 1.4
- distance_to_ma20_pct_auxiliary: 0.27
- distance_to_high_60_pct: -4.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,18.95,19,18.65,18.75,1179269,19,-1.34,19.11,18.76,1.48
20260505,18.75,18.8,18.7,18.8,384842,18.99,-0.99,19.08,18.77,0.49
20260506,18.8,18.85,18.7,18.85,514458,18.98,-0.66,19.05,18.77,0.66
20260507,18.75,19.15,18.75,19.05,789302,18.98,0.36,19.03,18.78,1.03
20260508,19.1,19.2,19,19.1,794440,18.99,0.57,19.02,18.79,1.03
20260511,19.2,19.2,19.05,19.15,558664,19,0.76,19.01,18.8,0.72
20260512,19.1,19.1,18.85,18.9,873355,19,-0.51,18.98,18.82,1.12
20260513,18.9,18.9,18.8,18.9,369022,18.99,-0.46,18.96,18.83,0.49
20260514,18.85,18.95,18.75,18.75,404717,18.97,-1.15,18.94,18.84,0.57
20260515,18.9,18.9,18.4,18.45,1117502,18.93,-2.51,18.9,18.84,1.53
20260518,18.5,18.5,18.35,18.4,464547,18.88,-2.55,18.87,18.85,0.66
20260519,18.45,18.6,18.45,18.55,411718,18.85,-1.61,18.85,18.86,0.62
20260520,18.6,18.6,18.45,18.45,309851,18.82,-1.97,18.82,18.86,0.47
20260521,18.5,18.6,18.5,18.6,346914,18.8,-1.07,18.8,18.87,0.53
20260522,18.55,18.65,18.45,18.65,470627,18.79,-0.74,18.8,18.88,0.78
20260525,18.6,18.6,18.35,18.45,1238908,18.76,-1.66,18.78,18.88,1.93
20260526,18.45,18.5,18.35,18.5,482215,18.74,-1.28,18.77,18.88,0.77
20260527,18.5,18.55,18.4,18.45,444466,18.71,-1.42,18.73,18.88,0.72
20260528,18.45,18.6,18.45,18.5,952170,18.7,-1.05,18.71,18.89,1.52
20260529,18.65,18.85,18.6,18.75,914125,18.7,0.26,18.7,18.9,1.4
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 68.57
- over_600_ratio: 66.67
- over_800_ratio: 64.89
- over_1000_ratio: 63.79
- over_400_change_1w: -0.17
- over_800_change_1w: -0.26
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.9,,65.88,,64.77,,0,False,False
20260508,68.92,0.02,65.33,-0.55,64.04,-0.73,1,False,False
20260515,68.82,-0.1,65.27,-0.06,64,-0.04,0,False,False
20260522,68.74,-0.08,65.15,-0.12,63.85,-0.15,0,False,False
20260529,68.57,-0.17,64.89,-0.26,63.79,-0.06,0,False,False
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
