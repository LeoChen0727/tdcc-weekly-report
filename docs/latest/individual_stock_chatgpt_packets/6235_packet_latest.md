# INDIVIDUAL STOCK CHATGPT PACKET - 6235 華孚

## Metadata
- generated_at: 2026-05-26 23:02:13 Asia/Taipei
- stock_id: 6235
- stock_name: 華孚
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6235_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6235_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6235_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6235_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6235_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6235_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6235_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6235_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6235_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6235_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6235_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6235_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6235_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6235.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6235.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6235.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6235.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6235.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6235.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6235_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6235_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6235_latest.md?ref=main

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
- open: 41.75
- high: 42.15
- low: 40.4
- close: 40.85
- volume: 920690
- ma5: 41.02
- ema23_primary: 42.38
- distance_to_ema23_pct: -3.61
- ma20: 42
- ma60: 45.97
- ma120: 53.22
- return_5d: 2.9
- return_20d: -6.63
- volume_ratio: 1.08
- distance_to_ma20_pct_auxiliary: -2.73
- distance_to_high_60_pct: -30.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,44,44.75,43.4,44.75,503223,46.4,-3.55,45.7,51.55,0.64
20260429,44.2,44.9,43.8,43.85,366555,46.19,-5.06,45.47,51.25,0.51
20260430,43.9,44.1,43.15,43.2,506340,45.94,-5.96,45.33,50.94,0.73
20260504,42.8,42.95,42.35,42.5,934373,45.65,-6.9,45.09,50.62,1.3
20260505,42.6,43.15,42.6,43.1,621683,45.44,-5.15,44.95,50.29,0.85
20260506,43.25,43.4,42.05,42.8,820751,45.22,-5.35,44.88,49.99,1.17
20260507,42.6,43.45,42.6,43.4,738950,45.07,-3.7,44.78,49.69,1.05
20260508,43.65,44.3,42.9,43,939003,44.89,-4.22,44.64,49.41,1.3
20260511,42.95,43.65,42.5,43.6,777089,44.79,-2.65,44.56,49.18,1.05
20260512,43.6,43.65,42.65,42.7,724591,44.61,-4.29,44.47,48.95,0.97
20260513,42,42.1,40.3,41.25,1514078,44.33,-6.95,44.27,48.66,1.92
20260514,41.5,42.05,40.1,40.35,1361737,44,-8.3,44.03,48.32,1.66
20260515,40.55,41.9,39.95,40.15,1354234,43.68,-8.08,43.74,48.02,1.57
20260518,40,40.5,39.5,40.5,546226,43.41,-6.71,43.48,47.74,0.64
20260519,40.5,40.95,39.7,39.7,946388,43.11,-7.9,43.15,47.43,1.08
20260520,40.15,40.15,39.55,39.75,409039,42.83,-7.18,42.77,47.12,0.48
20260521,40.1,41.4,40.1,41.3,963215,42.7,-3.28,42.48,46.84,1.13
20260522,41.4,42.15,41.25,41.9,867540,42.63,-1.72,42.28,46.55,1.04
20260525,41.9,42.25,41.05,41.3,1170672,42.52,-2.87,42.14,46.26,1.39
20260526,41.75,42.15,40.4,40.85,920690,42.38,-3.61,42,45.97,1.08
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.7
- over_600_ratio: 39.98
- over_800_ratio: 37.9
- over_1000_ratio: 36.54
- over_400_change_1w: 0.12
- over_800_change_1w: 0.89
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.49,,38.65,,36.86,,0,False,False
20260508,42.65,0.16,37.61,-1.04,36.29,-0.57,1,False,False
20260515,42.58,-0.07,37.01,-0.6,36.56,0.27,2,False,True
20260522,42.7,0.12,37.9,0.89,36.54,-0.02,3,False,True
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6235 | 華孚 | 13 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
