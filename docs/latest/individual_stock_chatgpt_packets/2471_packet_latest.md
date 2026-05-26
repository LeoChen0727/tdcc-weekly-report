# INDIVIDUAL STOCK CHATGPT PACKET - 2471 資通

## Metadata
- generated_at: 2026-05-26 23:00:45 Asia/Taipei
- stock_id: 2471
- stock_name: 資通
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2471_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2471_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2471_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2471_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2471_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2471_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2471_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2471_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2471_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2471_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2471_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2471_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2471_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2471.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2471.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2471.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2471.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2471.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2471.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2471_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2471_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2471_latest.md?ref=main

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
- open: 50.2
- high: 51
- low: 50.2
- close: 50.9
- volume: 248777
- ma5: 50.48
- ema23_primary: 51.17
- distance_to_ema23_pct: -0.53
- ma20: 51.34
- ma60: 51.65
- ma120: 51.18
- return_5d: 2.11
- return_20d: -1.55
- volume_ratio: 1.04
- distance_to_ma20_pct_auxiliary: -0.85
- distance_to_high_60_pct: -7.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,51.7,52.1,51.1,51.9,198486,52.31,-0.78,52.19,51.68,0.89
20260429,52.1,53,51.9,52.3,273374,52.3,-0.01,52.25,51.67,1.19
20260430,52.4,53.8,52.2,52.6,160224,52.33,0.52,52.38,51.66,0.7
20260504,52.5,53.1,52.3,52.6,241331,52.35,0.47,52.41,51.64,1.05
20260505,52.6,53.3,52.6,52.7,253960,52.38,0.61,52.52,51.63,1.08
20260506,52.9,53.1,52.5,52.8,257485,52.42,0.73,52.6,51.64,1.05
20260507,53.1,53.5,52.7,52.9,237826,52.46,0.85,52.65,51.64,0.95
20260508,52.9,53.7,52.9,53.1,191080,52.51,1.12,52.69,51.66,0.75
20260511,53.1,53.1,51,51.7,553232,52.44,-1.42,52.66,51.67,2.01
20260512,51.8,51.8,50.9,51.3,245714,52.35,-2,52.67,51.69,0.89
20260513,51.3,51.3,50.8,50.9,123612,52.23,-2.54,52.63,51.69,0.45
20260514,50.9,50.9,50,50.2,479147,52.06,-3.57,52.55,51.68,1.64
20260515,50.3,50.5,49.5,49.6,479586,51.85,-4.34,52.28,51.67,1.75
20260518,49.6,50.2,49.1,49.85,120568,51.69,-3.55,52.08,51.67,0.46
20260519,50.1,50.6,49.8,49.85,101528,51.53,-3.27,51.91,51.63,0.4
20260520,49.85,50.3,49.7,50.2,87370,51.42,-2.38,51.72,51.62,0.35
20260521,50.2,50.7,50.2,50.4,116863,51.34,-1.82,51.55,51.61,0.49
20260522,50.4,50.6,50,50.5,180116,51.27,-1.5,51.46,51.62,0.78
20260525,50.5,50.5,50,50.4,224741,51.19,-1.55,51.38,51.63,0.96
20260526,50.2,51,50.2,50.9,248777,51.17,-0.53,51.34,51.65,1.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 23.93
- over_600_ratio: 13.46
- over_800_ratio: 10.44
- over_1000_ratio: 6.74
- over_400_change_1w: 0.68
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,23.45,,10.44,,6.74,,0,False,False
20260508,23.34,-0.11,10.44,0,6.74,0,0,False,False
20260515,23.25,-0.09,10.44,0,6.74,0,0,False,False
20260522,23.93,0.68,10.44,0,6.74,0,1,False,False
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
