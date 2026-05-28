# INDIVIDUAL STOCK CHATGPT PACKET - 5274 信驊

## Metadata
- generated_at: 2026-05-28 20:19:42 Asia/Taipei
- stock_id: 5274
- stock_name: 信驊
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5274_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5274_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5274_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5274_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5274_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5274_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5274_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5274_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5274_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5274_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5274_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5274_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5274_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5274.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5274.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5274.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5274.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5274.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5274.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5274_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5274_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5274_latest.md?ref=main

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
- open: 17825
- high: 19000
- low: 17500
- close: 17835
- volume: 18137000
- ma5: 17762
- ema23_primary: 16744.22
- distance_to_ema23_pct: 6.51
- ma20: 17344.75
- ma60: 13940.67
- ma120: 10914.42
- return_5d: 8.49
- return_20d: 7.73
- volume_ratio: 3.87
- distance_to_ma20_pct_auxiliary: 2.83
- distance_to_high_60_pct: -7.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,16715,17140,16475,16475,284000,14203.1,16,14125,11384.5,0.94
20260504,17375,17545,16835,17545,247000,14481.59,21.15,14436.5,11529.08,0.82
20260505,17450,17905,16950,17790,297000,14757.29,20.55,14741.5,11677.58,0.99
20260506,18550,19195,17790,18700,391000,15085.85,23.96,15103,11843.25,1.26
20260507,18550,18750,17800,17890,488000,15319.53,16.78,15366.75,11994.08,1.5
20260508,17540,18150,16955,16955,384000,15455.82,9.7,15586.25,12121.42,1.17
20260511,17000,17980,17000,17825,289000,15653.25,13.87,15848.5,12270.5,0.89
20260512,17955,18385,17780,18005,276000,15849.23,13.6,16139.75,12419.92,0.84
20260513,17815,18100,17390,17820,298000,16013.46,11.28,16380.5,12553.75,0.91
20260514,18420,18535,17530,17810,280000,16163.17,10.19,16577.25,12689.92,0.84
20260515,18200,18450,17195,17195,220000,16249.16,5.82,16713,12824.33,0.67
20260518,17385,17385,15530,16150,479000,16240.9,-0.56,16830.25,12945.17,1.42
20260519,16020,16420,15140,15925,412000,16214.57,-1.79,16905.25,13052.25,1.2
20260520,16085,16100,15485,15560,258000,16160.02,-3.71,16921,13156.17,0.76
20260521,16370,16825,16140,16440,300000,16183.35,1.59,16938.75,13268.08,0.88
20260522,17235,17780,16285,17780,17020000,16316.41,8.97,17044.25,13401.83,14.53
20260525,17990,18380,17665,17725,17990000,16433.79,7.86,17112,13534.67,8.79
20260526,17905,18060,17190,17240,17527000,16500.98,4.48,17174,13660.08,6.04
20260527,18065,18450,17510,18230,18143000,16645.06,9.52,17280.75,13801.75,4.78
20260528,17825,19000,17500,17835,18137000,16744.22,6.51,17344.75,13940.67,3.87
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.85
- over_600_ratio: 26
- over_800_ratio: 21.97
- over_1000_ratio: 19.38
- over_400_change_1w: 2.29
- over_800_change_1w: -2.36
- over_1000_change_1w: -0.23
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.06,,24.77,,19.97,,0,False,False
20260508,32.68,-0.38,24.42,-0.35,19.62,-0.35,0,False,False
20260515,32.56,-0.12,24.33,-0.09,19.61,-0.01,0,False,False
20260522,34.85,2.29,21.97,-2.36,19.38,-0.23,1,False,False
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
