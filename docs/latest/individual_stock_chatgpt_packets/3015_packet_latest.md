# INDIVIDUAL STOCK CHATGPT PACKET - 3015 全漢

## Metadata
- generated_at: 2026-05-29 19:32:20 Asia/Taipei
- stock_id: 3015
- stock_name: 全漢
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3015_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3015_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3015_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3015_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3015_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3015_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3015_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3015_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3015_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3015_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3015_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3015_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3015_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3015.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3015.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3015.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3015.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3015.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3015.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3015_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3015_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3015_latest.md?ref=main

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
- open: 51.6
- high: 52.2
- low: 50.2
- close: 50.2
- volume: 1386150
- ma5: 51.38
- ema23_primary: 50.86
- distance_to_ema23_pct: -1.3
- ma20: 50.86
- ma60: 50.86
- ma120: 52.3
- return_5d: -2.52
- return_20d: 1.21
- volume_ratio: 2.69
- distance_to_ma20_pct_auxiliary: -1.3
- distance_to_high_60_pct: -6.52

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,49.7,51.5,49.7,51.1,478658,50.63,0.93,50.48,51.68,1.64
20260505,51.2,51.6,51,51.6,514088,50.71,1.75,50.58,51.62,1.67
20260506,51.6,52.1,50.3,50.8,579620,50.72,0.16,50.67,51.57,1.79
20260507,51.1,51.5,50.8,51.3,309287,50.77,1.05,50.73,51.52,0.95
20260508,51.6,52,50.2,50.7,370240,50.76,-0.12,50.7,51.48,1.14
20260511,50.8,51.1,50,51.1,296428,50.79,0.61,50.72,51.48,0.9
20260512,51.1,51.1,50.2,50.2,253277,50.74,-1.07,50.7,51.47,0.76
20260513,50.2,51,49.6,51,456043,50.76,0.47,50.7,51.46,1.31
20260514,51,51.1,50,50.1,289691,50.71,-1.2,50.69,51.42,0.83
20260515,50.5,50.6,49.45,49.45,393727,50.6,-2.28,50.59,51.38,1.1
20260518,49.65,49.65,48.7,49.05,496004,50.47,-2.82,50.51,51.35,1.36
20260519,49.1,50.7,49,50.7,497711,50.49,0.41,50.49,51.33,1.36
20260520,51,51.2,49.8,50.7,518990,50.51,0.38,50.48,51.28,1.37
20260521,51.4,51.5,50.6,51,476717,50.55,0.89,50.45,51.23,1.25
20260522,51,51.6,50.7,51.5,509489,50.63,1.72,50.52,51.15,1.31
20260525,51.8,52.2,51.4,52,699144,50.74,2.48,50.59,51.09,1.7
20260526,52.3,53.3,51.7,52.2,694362,50.87,2.62,50.7,51.05,1.62
20260527,52.6,53.3,51.5,51.6,441606,50.93,1.32,50.78,50.99,1
20260528,51.6,52.6,50.8,50.9,650972,50.92,-0.05,50.83,50.91,1.41
20260529,51.6,52.2,50.2,50.2,1386150,50.86,-1.3,50.86,50.86,2.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.92
- over_600_ratio: 61.63
- over_800_ratio: 59.08
- over_1000_ratio: 56.54
- over_400_change_1w: 0.36
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.69,,58.54,,55.99,,0,False,False
20260508,63.65,-0.04,59.08,0.54,57.03,1.04,1,False,True
20260515,63.56,-0.09,59.15,0.07,56.62,-0.41,2,False,True
20260522,63.92,0.36,59.08,-0.07,56.54,-0.08,3,False,False
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
| 20260529 | 3015 | 全漢 | 4 | 0 | 34960.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
