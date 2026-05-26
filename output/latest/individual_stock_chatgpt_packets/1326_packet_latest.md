# INDIVIDUAL STOCK CHATGPT PACKET - 1326 台化

## Metadata
- generated_at: 2026-05-26 23:00:11 Asia/Taipei
- stock_id: 1326
- stock_name: 台化
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1326_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1326_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1326_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1326_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1326_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1326_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1326_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1326_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1326_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1326_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1326_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1326_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1326_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1326.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1326.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1326.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1326.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1326.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1326.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1326_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1326_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1326_latest.md?ref=main

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
- open: 44.75
- high: 45.75
- low: 44.2
- close: 44.5
- volume: 15263951
- ma5: 45
- ema23_primary: 46.73
- distance_to_ema23_pct: -4.78
- ma20: 47.59
- ma60: 46.95
- ma120: 41.1
- return_5d: -0.89
- return_20d: -11.71
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: -6.48
- distance_to_high_60_pct: -19.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,51.2,52.5,50.7,51.4,24399696,48.59,5.79,48.79,44.87,0.5
20260429,52.1,54.5,51.7,52.5,49498087,48.91,7.33,48.98,45.18,1.1
20260430,53,53.3,51.2,52.3,29865338,49.2,6.31,49.35,45.47,0.75
20260504,52,52,50.7,50.8,21143460,49.33,2.98,49.62,45.72,0.54
20260505,51,52.4,50.8,51.8,21769575,49.54,4.57,49.97,45.94,0.56
20260506,52.3,52.9,50.8,51,21291741,49.66,2.7,50.24,46.11,0.56
20260507,51,51.1,49.4,49.45,28788176,49.64,-0.38,50.45,46.2,0.76
20260508,50,50.1,46.6,46.95,42319894,49.42,-4.99,50.52,46.25,1.11
20260511,46.3,48.75,46.3,47.8,23048519,49.28,-3.01,50.64,46.34,0.6
20260512,48.1,48.2,46.7,47.05,13453186,49.1,-4.17,50.49,46.48,0.39
20260513,47,47.4,46.1,46.1,13784781,48.85,-5.62,50.07,46.59,0.47
20260514,46.05,46.1,44.8,44.95,19735831,48.52,-7.36,49.8,46.66,0.76
20260515,45.35,45.35,44.3,44.45,11530955,48.18,-7.75,49.41,46.73,0.46
20260518,44.45,45.3,43.65,45.25,19494877,47.94,-5.61,49.13,46.83,0.79
20260519,45.2,45.95,44.9,44.9,15639593,47.68,-5.84,48.85,46.87,0.64
20260520,45,45.25,44.25,44.55,12830593,47.42,-6.06,48.55,46.93,0.54
20260521,44.8,45.7,44.8,45.45,10223386,47.26,-3.83,48.29,46.98,0.44
20260522,45.5,45.75,45.15,45.55,11219996,47.12,-3.32,48.1,47.02,0.51
20260525,45.55,45.55,44.25,44.95,17590321,46.94,-4.23,47.88,47.02,0.81
20260526,44.75,45.75,44.2,44.5,15263951,46.73,-4.78,47.59,46.95,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.52
- over_600_ratio: 80.41
- over_800_ratio: 79.56
- over_1000_ratio: 78.91
- over_400_change_1w: -0.29
- over_800_change_1w: -0.32
- over_1000_change_1w: -0.34
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.26,,80.49,,79.74,,0,False,False
20260508,82.26,0,80.43,-0.06,79.78,0.04,1,False,True
20260515,81.81,-0.45,79.88,-0.55,79.25,-0.53,0,False,False
20260522,81.52,-0.29,79.56,-0.32,78.91,-0.34,0,False,False
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
| 20260526 | 1326 | 台化 | 108 | 6 | 5848320.0 | 32800.0 | 178.3 | call_put_bullish | 3 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
