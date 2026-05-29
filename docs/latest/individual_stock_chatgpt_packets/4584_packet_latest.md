# INDIVIDUAL STOCK CHATGPT PACKET - 4584 君帆

## Metadata
- generated_at: 2026-05-29 19:32:54 Asia/Taipei
- stock_id: 4584
- stock_name: 君帆
- packet_status: standard_rawdata_packet
- latest_price_date: 20260529
- price_rows: 113
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4584_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4584_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4584_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4584_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4584_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4584_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4584_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4584_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4584_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4584_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4584_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4584_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4584_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4584.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4584.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4584.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4584.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4584.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4584.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4584_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4584_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4584_latest.md?ref=main

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
- open: 42.8
- high: 44.9
- low: 42.8
- close: 43.85
- volume: 44000
- ma5: 44.07
- ema23_primary: 42.97
- distance_to_ema23_pct: 2.04
- ma20: 42.49
- ma60: 42.91
- ma120: 45.36
- return_5d: -6.3
- return_20d: 5.66
- volume_ratio: 2
- distance_to_ma20_pct_auxiliary: 3.19
- distance_to_high_60_pct: -7.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,41,41.5,40.6,41,15000,41.98,-2.33,41.63,44.18,1.29
20260504,40.6,41.5,40.6,41.5,3000,41.94,-1.04,41.57,44.1,0.26
20260505,40.75,41,40.7,41,11000,41.86,-2.05,41.53,44.01,0.92
20260506,40.6,40.6,40.35,40.35,3000,41.73,-3.32,41.4,43.9,0.25
20260507,40.35,40.9,40.25,40.9,25000,41.66,-1.84,41.35,43.81,1.92
20260508,41.15,41.15,40.85,40.85,4000,41.6,-1.8,41.32,43.71,0.32
20260511,40.4,40.4,40,40.15,27000,41.48,-3.2,41.23,43.6,2.17
20260512,40.15,40.3,40.15,40.3,2000,41.38,-2.61,41.15,43.5,0.16
20260513,41,41.85,41,41.6,15000,41.4,0.49,41.1,43.42,1.2
20260514,41.2,41.2,40.95,40.95,19000,41.36,-0.99,41.1,43.33,1.65
20260515,40.75,42.6,40.75,41.95,8000,41.41,1.31,41.1,43.27,0.73
20260518,41,44.3,41,44.3,25000,41.65,6.36,41.25,43.23,2.08
20260519,42,42.1,41.95,41.95,11000,41.67,0.66,41.26,43.14,0.91
20260520,42.95,45.9,42.5,45.9,23000,42.03,9.22,41.48,43.12,1.79
20260521,47,47,43.2,46.8,29000,42.42,10.31,41.8,43.12,2.13
20260522,46.8,46.8,44.4,46,46000,42.72,7.67,42.07,43.1,2.95
20260525,44.5,44.5,44.2,44.2,44000,42.85,3.16,42.23,43.04,2.61
20260526,44.3,44.3,42.6,43.1,43000,42.87,0.54,42.3,42.99,2.38
20260528,43.1,43.2,43.1,43.2,43000,42.89,0.71,42.38,42.94,2.15
20260529,42.8,44.9,42.8,43.85,44000,42.97,2.04,42.49,42.91,2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.09
- over_600_ratio: 78.65
- over_800_ratio: 78.65
- over_1000_ratio: 69.26
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
20260430,80.09,,78.65,,69.26,,0,False,False
20260508,80.09,0,78.65,0,69.26,0,0,False,False
20260515,80.09,0,78.65,0,69.26,0,0,False,False
20260522,80.09,0,78.65,0,69.26,0,0,False,False
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
