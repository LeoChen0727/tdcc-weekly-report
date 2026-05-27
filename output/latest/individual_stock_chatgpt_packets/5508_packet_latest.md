# INDIVIDUAL STOCK CHATGPT PACKET - 5508 永信建

## Metadata
- generated_at: 2026-05-27 21:27:42 Asia/Taipei
- stock_id: 5508
- stock_name: 永信建
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5508_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5508_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5508_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5508_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5508_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5508_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5508_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5508_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5508_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5508_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5508_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5508_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5508_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5508.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5508.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5508.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5508.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5508.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5508.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5508_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5508_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5508_latest.md?ref=main

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
- open: 47.55
- high: 47.8
- low: 46.8
- close: 46.8
- volume: 47000
- ma5: 47.58
- ema23_primary: 48.73
- distance_to_ema23_pct: -3.97
- ma20: 48.57
- ma60: 50.78
- ma120: 57.94
- return_5d: -3.41
- return_20d: -5.45
- volume_ratio: 0.15
- distance_to_ma20_pct_auxiliary: -3.65
- distance_to_high_60_pct: -20.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,49.25,49.6,48,48.5,912000,50.89,-4.7,50.51,54.06,1.84
20260430,48.5,48.85,48.05,48.05,435000,50.66,-5.14,50.38,53.84,0.88
20260504,48.05,50.1,48,50,500000,50.6,-1.19,50.3,53.65,0.99
20260505,50,50.5,49.2,49.45,314000,50.51,-2.09,50.24,53.45,0.63
20260506,49.5,49.75,49.1,49.3,315000,50.4,-2.19,50.17,53.27,0.65
20260507,49.65,50.2,49.35,50.1,340000,50.38,-0.55,50.13,53.1,0.7
20260508,49.85,50.2,48.95,49.1,432000,50.27,-2.33,50.07,52.9,0.89
20260511,49.1,49.95,48.75,49.75,309000,50.23,-0.95,50.04,52.74,0.64
20260512,49.65,49.75,49.2,49.35,213000,50.16,-1.61,49.98,52.56,0.45
20260513,49.15,49.3,48.75,48.8,226000,50.04,-2.48,49.9,52.39,0.48
20260514,48.8,49.05,48.3,48.4,269000,49.91,-3.02,49.79,52.21,0.58
20260515,48.4,48.65,47.6,47.75,569000,49.73,-3.97,49.63,52.01,1.2
20260518,47.6,49.2,47.1,48.55,469000,49.63,-2.17,49.48,51.84,0.99
20260519,48.95,49.45,48,48,302000,49.49,-3.02,49.35,51.69,0.65
20260520,48,48.5,47.8,48.45,208000,49.41,-1.93,49.24,51.52,0.46
20260521,48.5,48.9,48.25,48.6,281000,49.34,-1.5,49.13,51.36,0.64
20260522,48.6,48.6,48,48.15,48000,49.24,-2.21,49,51.2,0.12
20260525,48.15,48.3,47.1,47.25,47000,49.07,-3.72,48.84,51.04,0.12
20260526,47.4,47.45,47,47.1,47000,48.91,-3.7,48.71,50.91,0.14
20260527,47.55,47.8,46.8,46.8,47000,48.73,-3.97,48.57,50.78,0.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.06
- over_600_ratio: 68.25
- over_800_ratio: 66.72
- over_1000_ratio: 65.9
- over_400_change_1w: 0.08
- over_800_change_1w: -0.1
- over_1000_change_1w: -0.55
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.97,,66.74,,66.37,,0,False,False
20260508,69.11,0.14,66.69,-0.05,65.88,-0.49,1,False,False
20260515,68.98,-0.13,66.82,0.13,66.45,0.57,2,False,True
20260522,69.06,0.08,66.72,-0.1,65.9,-0.55,3,False,False
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
