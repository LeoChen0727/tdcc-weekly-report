# INDIVIDUAL STOCK CHATGPT PACKET - 2488 漢平

## Metadata
- generated_at: 2026-05-28 19:32:00 Asia/Taipei
- stock_id: 2488
- stock_name: 漢平
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2488_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2488_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2488_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2488_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2488_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2488_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2488_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2488_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2488_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2488_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2488_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2488_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2488_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2488.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2488.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2488.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2488.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2488.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2488.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2488_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2488_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2488_latest.md?ref=main

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
- open: 53.2
- high: 53.4
- low: 52.8
- close: 53
- volume: 269579
- ma5: 53.48
- ema23_primary: 52.09
- distance_to_ema23_pct: 1.74
- ma20: 52.14
- ma60: 50.04
- ma120: 48.01
- return_5d: 1.15
- return_20d: 3.11
- volume_ratio: 1.27
- distance_to_ma20_pct_auxiliary: 1.65
- distance_to_high_60_pct: -2.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,51.4,52.5,51.4,51.8,292644,50.41,2.75,50.65,48.33,0.94
20260504,51.8,51.8,50.7,50.8,217695,50.45,0.7,50.74,48.4,0.71
20260505,51.2,51.3,50.4,51.3,180399,50.52,1.55,50.84,48.48,0.6
20260506,51.7,51.7,50.4,51,230461,50.56,0.88,50.92,48.55,0.77
20260507,51,51.8,50.9,51.7,261424,50.65,2.07,51.03,48.63,0.9
20260508,52.3,52.3,51.6,51.9,160494,50.76,2.25,51.13,48.72,0.57
20260511,51.9,52.6,51.8,52.5,180885,50.9,3.14,51.26,48.83,0.66
20260512,52.7,52.7,51.9,51.9,167539,50.98,1.8,51.38,48.94,0.65
20260513,51.7,51.9,51.2,51.7,169095,51.04,1.28,51.47,49.04,0.68
20260514,51.7,51.8,51.6,51.8,108517,51.11,1.36,51.53,49.14,0.46
20260515,52,52.5,51.3,51.3,216597,51.12,0.35,51.48,49.23,0.95
20260518,51.1,51.6,51.1,51.4,87330,51.15,0.5,51.51,49.32,0.43
20260519,51.5,52,50.9,51.8,119542,51.2,1.17,51.48,49.41,0.63
20260520,52.3,52.3,51.9,52.1,87626,51.28,1.61,51.48,49.5,0.48
20260521,52.3,52.5,52.2,52.4,201333,51.37,2.01,51.54,49.59,1.09
20260522,52.9,54.5,52.6,54.4,593877,51.62,5.38,51.73,49.69,2.98
20260525,54.5,54.5,53.3,53.7,302527,51.8,3.68,51.89,49.79,1.46
20260526,54,54,53,53.2,223249,51.91,2.48,51.98,49.87,1.08
20260527,53.5,53.5,52.8,53.1,167930,52.01,2.09,52.06,49.96,0.8
20260528,53.2,53.4,52.8,53,269579,52.09,1.74,52.14,50.04,1.27
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 53.04
- over_600_ratio: 46.88
- over_800_ratio: 46.88
- over_1000_ratio: 45.8
- over_400_change_1w: -0.03
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.88,,46.72,,45.65,,0,False,False
20260508,52.46,-0.42,46.8,0.08,45.73,0.08,1,False,True
20260515,53.07,0.61,46.86,0.06,45.79,0.06,2,True,True
20260522,53.04,-0.03,46.88,0.02,45.8,0.01,3,False,True
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
