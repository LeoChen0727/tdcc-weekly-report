# INDIVIDUAL STOCK CHATGPT PACKET - 3081 聯亞

## Metadata
- generated_at: 2026-05-26 21:25:22 Asia/Taipei
- stock_id: 3081
- stock_name: 聯亞
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3081_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3081_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3081_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3081_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3081_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3081_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3081_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3081_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3081_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3081_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3081_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3081_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3081_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3081.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3081.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3081.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3081.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3081.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3081.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3081_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3081_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3081_latest.md?ref=main

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
- open: 2960
- high: 3180
- low: 2825
- close: 3160
- volume: 3001000
- ma5: 2786
- ema23_primary: 2678.21
- distance_to_ema23_pct: 17.99
- ma20: 2724.25
- ma60: 2161.92
- ma120: 1442.11
- return_5d: 26.91
- return_20d: 24.41
- volume_ratio: 1.05
- distance_to_ma20_pct_auxiliary: 16
- distance_to_high_60_pct: -4.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,2550,2675,2485,2505,3700000,2321.44,7.91,2338.25,1614.35,1.05
20260429,2480,2590,2430,2445,2443000,2331.74,4.86,2375,1642.27,0.71
20260430,2610,2685,2605,2640,3415000,2357.43,11.99,2428.25,1673.35,1.01
20260504,2795,2865,2615,2745,3328000,2389.72,14.87,2479,1706.07,0.97
20260505,2780,2885,2710,2815,2670000,2425.16,16.07,2528.5,1739.38,0.79
20260506,2880,2905,2565,2655,4382000,2444.32,8.62,2561,1769.98,1.28
20260507,2600,2690,2470,2660,3667000,2462.29,8.03,2592,1799.32,1.08
20260508,2565,2750,2555,2620,2484000,2475.43,5.84,2617.75,1826.48,0.74
20260511,2675,2820,2630,2780,2093000,2500.81,11.16,2641,1856.15,0.63
20260512,3055,3055,2955,3055,3824000,2547,19.95,2677.75,1890.42,1.13
20260513,2965,3050,2750,2835,2659000,2571,10.27,2710.75,1919.42,0.8
20260514,2960,2980,2815,2945,3013000,2602.16,13.18,2742.25,1949.58,0.93
20260515,3000,3000,2655,2655,2777000,2606.57,1.86,2756.75,1976.75,0.85
20260518,2550,2710,2500,2710,1878000,2615.19,3.63,2762.25,2005.25,0.57
20260519,2650,2705,2480,2490,2030000,2604.75,-4.41,2743.75,2028.5,0.61
20260520,2460,2670,2460,2580,2021000,2602.69,-0.87,2726,2052.83,0.63
20260521,2655,2660,2540,2555,2192000,2598.72,-1.68,2703.5,2077.33,0.68
20260522,2715,2790,2670,2710,2738000,2607.99,3.91,2688,2102.67,0.9
20260525,2790,2980,2730,2925,2900000,2634.41,11.03,2693.25,2130.33,0.99
20260526,2960,3180,2825,3160,3001000,2678.21,17.99,2724.25,2161.92,1.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.07
- over_600_ratio: 40.64
- over_800_ratio: 35.41
- over_1000_ratio: 30.68
- over_400_change_1w: 0.28
- over_800_change_1w: -0.91
- over_1000_change_1w: -2.93
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.59,,37.42,,33.74,,0,False,False
20260508,44.54,-2.05,35.67,-1.75,31.97,-1.77,0,False,False
20260515,44.79,0.25,36.32,0.65,33.61,1.64,1,False,True
20260522,45.07,0.28,35.41,-0.91,30.68,-2.93,2,False,False
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
