# INDIVIDUAL STOCK CHATGPT PACKET - 8085 福華

## Metadata
- generated_at: 2026-05-30 23:43:50 Asia/Taipei
- stock_id: 8085
- stock_name: 福華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8085_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8085_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8085_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8085_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8085_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8085_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8085_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8085_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8085_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8085_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8085_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8085_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8085_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8085.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8085.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8085.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8085.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8085.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8085.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8085_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8085_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8085_latest.md?ref=main

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
- open: 11
- high: 11.3
- low: 10.9
- close: 11.05
- volume: 11000
- ma5: 11.25
- ema23_primary: 12.07
- distance_to_ema23_pct: -8.49
- ma20: 11.8
- ma60: 14.28
- ma120: 15.68
- return_5d: -5.15
- return_20d: -11.95
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: -6.38
- distance_to_high_60_pct: -40.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.95,13.3,12.65,12.9,412000,14.32,-9.89,14.3,16.15,0.78
20260505,12.75,12.9,12.5,12.6,545000,14.17,-11.1,14.18,16.05,1.01
20260506,12.7,12.75,12.25,12.3,691000,14.02,-12.25,14.01,15.96,1.27
20260507,12.5,12.7,12.3,12.5,418000,13.89,-10.01,13.87,15.88,0.76
20260508,12.55,12.65,12,12.3,592000,13.76,-10.6,13.73,15.79,1.07
20260511,12.3,12.3,11.85,12.15,556000,13.62,-10.82,13.6,15.71,1.02
20260512,12.15,12.25,11.8,12.2,381000,13.51,-9.66,13.48,15.64,0.69
20260513,12.2,12.25,11.85,12.15,250000,13.39,-9.28,13.34,15.56,0.46
20260514,12.25,12.25,11.75,11.8,355000,13.26,-11.01,13.18,15.46,0.65
20260515,11.8,12,11.2,11.45,725000,13.11,-12.65,12.98,15.35,1.3
20260518,11.5,12,11.2,11.65,583000,12.99,-10.3,12.82,15.25,1.02
20260519,11.9,11.9,11,11.1,522000,12.83,-13.48,12.66,15.14,0.94
20260520,11.1,11.6,11.1,11.5,322000,12.72,-9.58,12.51,15.04,0.62
20260521,11.4,11.6,11.3,11.55,288000,12.62,-8.49,12.35,14.95,0.56
20260522,11.5,11.8,11.35,11.65,12000,12.54,-7.1,12.23,14.85,0.03
20260525,11.65,12.1,11.45,11.75,12000,12.47,-5.81,12.14,14.75,0.03
20260526,11.75,11.9,11.25,11.4,11000,12.39,-7.95,12.06,14.64,0.03
20260527,11.3,11.3,11,11.05,11000,12.27,-9.97,11.97,14.52,0.03
20260528,11.1,11.3,10.9,11,11000,12.17,-9.6,11.88,14.39,0.03
20260529,11,11.3,10.9,11.05,11000,12.07,-8.49,11.8,14.28,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 42.2
- over_600_ratio: 38.24
- over_800_ratio: 36.2
- over_1000_ratio: 32.49
- over_400_change_1w: -0.14
- over_800_change_1w: -0.1
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,41.61,,35.47,,31.66,,0,False,False
20260508,42.69,1.08,36.07,0.6,31.66,0,1,False,True
20260515,42.85,0.16,36.23,0.16,32.53,0.87,2,True,True
20260522,42.34,-0.51,36.3,0.07,32.54,0.01,3,False,True
20260529,42.2,-0.14,36.2,-0.1,32.49,-0.05,0,False,False
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
