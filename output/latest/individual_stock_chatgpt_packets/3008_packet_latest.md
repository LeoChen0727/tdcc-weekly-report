# INDIVIDUAL STOCK CHATGPT PACKET - 3008 大立光

## Metadata
- generated_at: 2026-05-26 23:53:35 Asia/Taipei
- stock_id: 3008
- stock_name: 大立光
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3008_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3008_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3008_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3008_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3008_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3008_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3008.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3008.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3008.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3008.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3008.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3008.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3008_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3008_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3008_latest.md?ref=main

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
- open: 3875
- high: 3875
- low: 3665
- close: 3665
- volume: 1129814
- ma5: 3542
- ema23_primary: 3063.01
- distance_to_ema23_pct: 19.65
- ma20: 2980.5
- ma60: 2588.5
- ma120: 2449.71
- return_5d: 8.92
- return_20d: 40.15
- volume_ratio: 0.52
- distance_to_ma20_pct_auxiliary: 22.97
- distance_to_high_60_pct: -5.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,2650,2685,2575,2580,1455699,2492.13,3.53,2459.5,2393.25,0.82
20260429,2590,2650,2550,2595,1553127,2500.7,3.77,2480.25,2395.83,0.85
20260430,2580,2580,2515,2515,1185538,2501.89,0.52,2498.25,2397.17,0.65
20260504,2540,2580,2515,2575,1338198,2507.99,2.67,2517.5,2399.08,0.71
20260505,2575,2585,2520,2545,781570,2511.07,1.35,2537.75,2400.67,0.41
20260506,2550,2550,2490,2520,1403899,2511.82,0.33,2555.25,2402.08,0.72
20260507,2535,2575,2535,2575,1194265,2517.08,2.3,2570,2404.33,0.61
20260508,2585,2620,2530,2570,1447944,2521.49,1.92,2584.5,2406.75,0.73
20260511,2600,2600,2525,2545,865599,2523.45,0.85,2596.25,2409,0.43
20260512,2600,2795,2580,2795,3209668,2546.08,9.78,2614.5,2416.33,1.52
20260513,2870,2870,2735,2850,4369632,2571.41,10.83,2623.5,2424.67,2.03
20260514,2930,3135,2895,3135,4216926,2618.37,19.73,2639.25,2437.5,1.96
20260515,3290,3445,3290,3445,3089450,2687.26,28.2,2670.5,2456.58,1.43
20260518,3400,3400,3125,3290,4461026,2737.49,20.18,2704.75,2472.58,2.06
20260519,3445,3615,3325,3365,5982140,2789.78,20.62,2737.5,2490.5,2.57
20260520,3330,3410,3200,3200,1168759,2823.96,13.32,2765.25,2505.08,0.51
20260521,3285,3520,3280,3460,1745376,2876.97,20.27,2809,2524.58,0.76
20260522,3450,3595,3450,3540,1289200,2932.22,20.73,2861.75,2544.08,0.57
20260525,3635,3845,3635,3845,1446961,3008.28,27.81,2928,2567.67,0.64
20260526,3875,3875,3665,3665,1129814,3063.01,19.65,2980.5,2588.5,0.52
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.31
- over_600_ratio: 50.3
- over_800_ratio: 46.17
- over_1000_ratio: 40.8
- over_400_change_1w: -0.63
- over_800_change_1w: 0.1
- over_1000_change_1w: -2.64
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.04,,47.16,,45.89,,0,False,False
20260508,57.93,-1.11,45.77,-1.39,43.75,-2.14,0,False,False
20260515,57.94,0.01,46.07,0.3,43.44,-0.31,1,False,True
20260522,57.31,-0.63,46.17,0.1,40.8,-2.64,2,False,True
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
| 20260526 | 3008 | 大立光 | 241 | 12 | 40995970.0 | 336520.0 | 121.82 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
