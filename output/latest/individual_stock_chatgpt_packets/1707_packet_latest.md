# INDIVIDUAL STOCK CHATGPT PACKET - 1707 葡萄王

## Metadata
- generated_at: 2026-05-26 23:00:22 Asia/Taipei
- stock_id: 1707
- stock_name: 葡萄王
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1707_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1707_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1707_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1707_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1707_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1707_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1707_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1707_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1707_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1707_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1707_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1707_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1707_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1707.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1707.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1707.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1707.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1707.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1707.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1707_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1707_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1707_latest.md?ref=main

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
- open: 101.5
- high: 102.5
- low: 100
- close: 100.5
- volume: 589616
- ma5: 102.5
- ema23_primary: 108.78
- distance_to_ema23_pct: -7.61
- ma20: 108.8
- ma60: 116.12
- ma120: 120.67
- return_5d: -4.74
- return_20d: -11.84
- volume_ratio: 1.96
- distance_to_ma20_pct_auxiliary: -7.63
- distance_to_high_60_pct: -18.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,115,115,113,114,167950,118.21,-3.56,118.8,120.4,0.8
20260429,114.5,114.5,113,114,82304,117.86,-3.27,118.38,120.28,0.41
20260430,113.5,114,112.5,112.5,241208,117.41,-4.18,117.95,120.11,1.17
20260504,112.5,113,112,112,192259,116.96,-4.24,117.42,119.93,0.91
20260505,112,113,112,112.5,99008,116.59,-3.51,117.03,119.78,0.46
20260506,112.5,112.5,112,112.5,149323,116.25,-3.22,116.62,119.62,0.68
20260507,112.5,113,112,112.5,172128,115.93,-2.96,116.15,119.46,0.77
20260508,112.5,114,112.5,113,142141,115.69,-2.32,115.75,119.3,0.62
20260511,113,113.5,112.5,113,122936,115.47,-2.13,115.4,119.17,0.56
20260512,111.5,111.5,110,110.5,529611,115.05,-3.96,115.03,118.99,2.43
20260513,110,110,108.5,109.5,341186,114.59,-4.44,114.55,118.78,1.5
20260514,108.5,109,108,108.5,282665,114.08,-4.89,114.08,118.58,1.21
20260515,108.5,108.5,107,107.5,313780,113.53,-5.31,113.55,118.33,1.3
20260518,108,108,106,106,239236,112.91,-6.12,112.92,118.08,0.97
20260519,105.5,106,105,105.5,251374,112.29,-6.05,112.3,117.82,1.03
20260520,105.5,105.5,103,103.5,523148,111.56,-7.22,111.58,117.5,2
20260521,104,104,102,104,530769,110.93,-6.24,110.9,117.2,1.88
20260522,104,104,102,103,529532,110.27,-6.59,110.22,116.87,1.85
20260525,103,103.5,101.5,101.5,512449,109.54,-7.34,109.47,116.5,1.69
20260526,101.5,102.5,100,100.5,589616,108.78,-7.61,108.8,116.12,1.96
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.42
- over_600_ratio: 54.49
- over_800_ratio: 50.92
- over_1000_ratio: 46.07
- over_400_change_1w: -0.31
- over_800_change_1w: -0.09
- over_1000_change_1w: -1.25
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.89,,51.18,,47.47,,0,False,False
20260508,57.82,-0.07,51.11,-0.07,47.4,-0.07,0,False,False
20260515,57.73,-0.09,51.01,-0.1,47.32,-0.08,0,False,False
20260522,57.42,-0.31,50.92,-0.09,46.07,-1.25,0,False,False
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
