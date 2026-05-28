# INDIVIDUAL STOCK CHATGPT PACKET - 2706 第一店

## Metadata
- generated_at: 2026-05-28 19:32:05 Asia/Taipei
- stock_id: 2706
- stock_name: 第一店
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2706_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2706_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2706_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2706_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2706_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2706_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2706_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2706_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2706_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2706_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2706_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2706_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2706_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2706.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2706.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2706.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2706.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2706.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2706.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2706_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2706_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2706_latest.md?ref=main

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
- open: 11.95
- high: 12
- low: 11.85
- close: 11.9
- volume: 226243
- ma5: 11.93
- ema23_primary: 12.14
- distance_to_ema23_pct: -1.99
- ma20: 12.16
- ma60: 12.39
- ma120: 12.66
- return_5d: -0.83
- return_20d: -4.03
- volume_ratio: 1.51
- distance_to_ma20_pct_auxiliary: -2.18
- distance_to_high_60_pct: -7.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,12.5,12.5,12.3,12.4,81858,12.48,-0.62,12.49,12.61,0.62
20260504,12.4,12.55,12.35,12.45,171260,12.48,-0.2,12.49,12.61,1.27
20260505,12.45,12.5,12.4,12.45,68042,12.47,-0.19,12.5,12.6,0.5
20260506,12.5,12.6,12.4,12.5,206535,12.48,0.2,12.51,12.6,1.42
20260507,12.55,12.55,12.4,12.4,141014,12.47,-0.55,12.51,12.59,0.98
20260508,12.5,12.55,12.4,12.5,119718,12.47,0.23,12.51,12.58,0.83
20260511,12.5,12.5,12.35,12.35,110853,12.46,-0.9,12.5,12.57,0.75
20260512,12.4,12.4,12.2,12.25,107378,12.44,-1.56,12.48,12.56,0.82
20260513,12.3,12.3,12.2,12.25,208693,12.43,-1.43,12.46,12.55,1.57
20260514,12.3,12.3,12.15,12.15,174547,12.4,-2.05,12.43,12.54,1.34
20260515,12.2,12.2,11.95,12.05,222219,12.38,-2.63,12.39,12.53,1.68
20260518,12.2,12.2,11.9,11.95,226841,12.34,-3.16,12.36,12.51,1.63
20260519,11.95,12,11.9,11.95,98157,12.31,-2.9,12.32,12.5,0.71
20260520,11.95,12,11.9,12,40226,12.28,-2.29,12.29,12.48,0.3
20260521,12,12.05,11.95,12,68794,12.26,-2.11,12.27,12.47,0.52
20260522,12,12.05,11.95,11.95,193679,12.23,-2.31,12.25,12.45,1.48
20260525,12.05,12.05,11.9,11.9,179006,12.2,-2.5,12.23,12.44,1.37
20260526,11.95,11.95,11.9,11.95,93787,12.18,-1.92,12.21,12.42,0.72
20260527,11.95,12,11.85,11.95,262511,12.16,-1.76,12.19,12.41,1.86
20260528,11.95,12,11.85,11.9,226243,12.14,-1.99,12.16,12.39,1.51
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.85
- over_600_ratio: 83.45
- over_800_ratio: 82.3
- over_1000_ratio: 81.56
- over_400_change_1w: 0.03
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.8,,82.28,,81.54,,0,False,False
20260508,84.88,0.08,82.28,0,81.54,0,1,False,False
20260515,84.82,-0.06,82.29,0.01,81.55,0.01,2,False,True
20260522,84.85,0.03,82.3,0.01,81.56,0.01,3,True,True
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
