# INDIVIDUAL STOCK CHATGPT PACKET - 6655 科定

## Metadata
- generated_at: 2026-05-30 23:43:12 Asia/Taipei
- stock_id: 6655
- stock_name: 科定
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 257
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6655_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6655_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6655_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6655_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6655_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6655_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6655_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6655_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6655_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6655_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6655_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6655_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6655_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6655.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6655.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6655.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6655.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6655.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6655.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6655_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6655_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6655_latest.md?ref=main

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
- open: 131.5
- high: 132
- low: 131
- close: 131.5
- volume: 8662
- ma5: 131.2
- ema23_primary: 133.63
- distance_to_ema23_pct: -1.59
- ma20: 134.62
- ma60: 133.03
- ma120: 125.85
- return_5d: -0.75
- return_20d: -4.01
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -2.32
- distance_to_high_60_pct: -6.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,136.5,137,136.5,137,4347,135.14,1.38,135.12,129.43,0.43
20260505,140,140,136,138,7034,135.38,1.94,135.6,129.72,0.68
20260506,138.5,138.5,135.5,137.5,15271,135.56,1.43,136.07,129.99,1.41
20260507,138,138,138,138,5007,135.76,1.65,136.53,130.28,0.49
20260508,138.5,138.5,138.5,138.5,2600,135.99,1.85,137,130.58,0.27
20260511,138,138.5,137,138.5,7280,136.2,1.69,137.43,130.88,0.79
20260512,139.5,139.5,136.5,138,8297,136.35,1.21,137.72,131.2,0.9
20260513,138,138,136.5,137.5,10305,136.44,0.77,137.93,131.48,1.11
20260514,137,137,136,136,6000,136.41,-0.3,137.97,131.76,0.65
20260515,135,135,134.5,135,5000,136.29,-0.95,137.95,131.98,0.56
20260518,137.5,137.5,132.5,133,10060,136.01,-2.22,137.78,132.18,1.13
20260519,131.5,135.5,131.5,132,16258,135.68,-2.71,137.47,132.38,1.76
20260520,133,133,133,133,7016,135.46,-1.81,137.12,132.57,0.77
20260521,132,132,131,132,8096,135.17,-2.34,136.72,132.76,0.87
20260522,130,132.5,130,132.5,10016,134.95,-1.81,136.45,132.94,1.08
20260525,135.5,135.5,131.5,131.5,12100,134.66,-2.35,136,132.99,1.33
20260526,131.5,134.5,130,131,12999,134.35,-2.5,135.68,133.02,1.37
20260527,133.5,133.5,129.5,131,15101,134.07,-2.29,135.25,133.03,1.69
20260528,131,131,130.5,131,7950,133.82,-2.11,134.9,133.03,0.87
20260529,131.5,132,131,131.5,8662,133.63,-1.59,134.62,133.03,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 86.07
- over_600_ratio: 83.1
- over_800_ratio: 79.75
- over_1000_ratio: 76.39
- over_400_change_1w: 0.09
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,86.01,,79.69,,77.58,,0,False,False
20260508,85.93,-0.08,79.61,-0.08,76.31,-1.27,0,False,False
20260515,85.95,0.02,79.63,0.02,76.33,0.02,1,True,True
20260522,85.98,0.03,79.66,0.03,76.36,0.03,2,True,True
20260529,86.07,0.09,79.75,0.09,76.39,0.03,3,True,True
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
