# INDIVIDUAL STOCK CHATGPT PACKET - 2528 皇普

## Metadata
- generated_at: 2026-05-26 23:00:49 Asia/Taipei
- stock_id: 2528
- stock_name: 皇普
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2528_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2528_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2528_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2528_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2528_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2528_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2528_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2528_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2528_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2528_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2528_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2528_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2528_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2528.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2528.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2528.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2528.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2528.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2528.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2528_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2528_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2528_latest.md?ref=main

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
- open: 22.1
- high: 22.2
- low: 21.9
- close: 22
- volume: 876111
- ma5: 22.12
- ema23_primary: 22.56
- distance_to_ema23_pct: -2.5
- ma20: 22.29
- ma60: 24.48
- ma120: 26.95
- return_5d: -0.45
- return_20d: -2
- volume_ratio: 1.42
- distance_to_ma20_pct_auxiliary: -1.28
- distance_to_high_60_pct: -24.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.45,22.8,22.4,22.55,305603,24.04,-6.21,23.83,26.3,0.45
20260429,22.8,22.85,22.3,22.55,574448,23.92,-5.72,23.68,26.18,0.85
20260430,22.7,22.85,22.4,22.5,421732,23.8,-5.46,23.55,26.06,0.63
20260504,22.6,22.6,22.3,22.4,1066968,23.68,-5.42,23.44,25.94,1.54
20260505,22.6,22.6,22.1,22.45,918699,23.58,-4.79,23.31,25.83,1.3
20260506,22.55,22.55,22,22.25,1357327,23.47,-5.2,23.2,25.73,1.78
20260507,22.05,22.5,22,22.4,446828,23.38,-4.19,23.09,25.64,0.58
20260508,22.45,22.8,22.2,22.25,377530,23.29,-4.45,23,25.54,0.5
20260511,22.25,22.55,22.25,22.3,526491,23.2,-3.9,22.92,25.46,0.69
20260512,22.45,22.45,21.8,22.15,998998,23.12,-4.18,22.83,25.38,1.27
20260513,22.05,22.4,21.9,22.35,343264,23.05,-3.05,22.75,25.3,0.44
20260514,22.2,22.4,22.1,22.25,426825,22.99,-3.2,22.64,25.21,0.54
20260515,22.3,22.45,22,22.4,836572,22.94,-2.34,22.54,25.13,1.03
20260518,22.5,22.5,22.1,22.2,477259,22.88,-2.95,22.45,25.05,0.6
20260519,22.15,22.35,21.9,22.1,466014,22.81,-3.12,22.4,24.96,0.63
20260520,22.1,22.2,21.85,22.2,478302,22.76,-2.46,22.37,24.88,0.67
20260521,22.3,22.3,22,22.1,441214,22.7,-2.66,22.35,24.79,0.65
20260522,22,22.25,22,22.15,329871,22.66,-2.24,22.32,24.69,0.51
20260525,22.3,22.3,22,22.15,664311,22.62,-2.06,22.31,24.59,1.01
20260526,22.1,22.2,21.9,22,876111,22.56,-2.5,22.29,24.48,1.42
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 83.89
- over_600_ratio: 80.88
- over_800_ratio: 79.44
- over_1000_ratio: 78.25
- over_400_change_1w: -0.08
- over_800_change_1w: 0.16
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.67,,79.44,,78.02,,0,False,False
20260508,83.77,0.1,79.5,0.06,78.51,0.49,1,True,True
20260515,83.97,0.2,79.28,-0.22,78.1,-0.41,2,False,False
20260522,83.89,-0.08,79.44,0.16,78.25,0.15,3,False,True
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
