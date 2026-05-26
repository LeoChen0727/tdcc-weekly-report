# INDIVIDUAL STOCK CHATGPT PACKET - 3131 弘塑

## Metadata
- generated_at: 2026-05-26 21:25:23 Asia/Taipei
- stock_id: 3131
- stock_name: 弘塑
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3131_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3131_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3131_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3131_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3131_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3131_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3131_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3131_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3131_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3131_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3131_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3131_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3131_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3131.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3131.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3131.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3131.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3131.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3131.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3131_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3131_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3131_latest.md?ref=main

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
- open: 3045
- high: 3205
- low: 3000
- close: 3115
- volume: 3139000
- ma5: 2827
- ema23_primary: 2911.54
- distance_to_ema23_pct: 6.99
- ma20: 2923.75
- ma60: 2716.25
- ma120: 2152.88
- return_5d: 20.74
- return_20d: 8.35
- volume_ratio: 3.09
- distance_to_ma20_pct_auxiliary: 6.54
- distance_to_high_60_pct: -14.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,2880,2905,2775,2870,840000,2978.01,-3.63,3146.5,2316.08,0.79
20260429,2895,2895,2810,2870,513000,2969.01,-3.33,3149.25,2334.75,0.5
20260430,2895,3045,2895,2950,859000,2967.42,-0.59,3159.25,2354.17,0.88
20260504,3015,3100,2920,3065,779000,2975.55,3.01,3166,2376,0.83
20260505,2930,2960,2810,2910,1583000,2970.09,-2.02,3157,2395.08,1.64
20260506,2990,3200,2950,3200,1165000,2989.25,7.05,3159.5,2419,1.19
20260507,3200,3235,3050,3120,874000,3000.15,4,3148.5,2441,0.89
20260508,3120,3140,2900,2940,395000,2995.13,-1.84,3132,2459.58,0.41
20260511,2900,3110,2895,3090,732000,3003.04,2.9,3128,2483.25,0.78
20260512,3095,3215,3025,3140,754000,3014.45,4.16,3110.75,2508.83,0.81
20260513,3120,3120,2940,3025,373000,3015.33,0.32,3097.75,2532,0.41
20260514,3100,3110,2930,2935,448000,3008.64,-2.45,3083.5,2554,0.5
20260515,3060,3060,2870,2870,431000,2997.08,-4.24,3064.25,2575.58,0.49
20260518,2810,2845,2665,2775,280000,2978.58,-6.83,3040.25,2596.08,0.33
20260519,2730,2775,2565,2580,566000,2945.36,-12.4,3008.75,2612.92,0.67
20260520,2570,2640,2550,2580,368000,2914.92,-11.49,2973.75,2630.25,0.45
20260521,2655,2725,2605,2700,463000,2897.01,-6.8,2938.75,2649.75,0.59
20260522,2750,2910,2735,2820,2829000,2890.59,-2.44,2922.25,2670,3.31
20260525,2910,2985,2875,2920,2945000,2893.04,0.93,2911.75,2691.83,3.18
20260526,3045,3205,3000,3115,3139000,2911.54,6.99,2923.75,2716.25,3.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.24
- over_600_ratio: 41.44
- over_800_ratio: 38.93
- over_1000_ratio: 35.96
- over_400_change_1w: -1.4
- over_800_change_1w: 0.35
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.99,,35,,28.72,,0,False,False
20260508,45.95,-1.04,37.94,2.94,28.7,-0.02,1,False,True
20260515,46.64,0.69,38.58,0.64,35.6,6.9,2,True,True
20260522,45.24,-1.4,38.93,0.35,35.96,0.36,3,False,True
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
