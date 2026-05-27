# INDIVIDUAL STOCK CHATGPT PACKET - 3712 永崴投控

## Metadata
- generated_at: 2026-05-27 21:27:16 Asia/Taipei
- stock_id: 3712
- stock_name: 永崴投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3712_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3712_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3712_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3712_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3712_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3712_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3712_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3712_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3712_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3712_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3712_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3712_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3712_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3712.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3712.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3712.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3712.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3712.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3712.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3712_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3712_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3712_latest.md?ref=main

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
- date: 20260527
- open: 16.3
- high: 16.5
- low: 15.85
- close: 16.05
- volume: 1027593
- ma5: 16.01
- ema23_primary: 17.84
- distance_to_ema23_pct: -10.04
- ma20: 18.14
- ma60: 20.46
- ma120: 23.12
- return_5d: 7.36
- return_20d: -21.71
- volume_ratio: 0.7
- distance_to_ma20_pct_auxiliary: -11.52
- distance_to_high_60_pct: -36.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,20.5,20.5,19.8,20.2,775717,20.57,-1.82,19.71,23,0.56
20260429,20.2,20.7,20,20.65,675808,20.58,0.33,19.62,22.91,0.49
20260430,20.6,20.6,19.7,19.85,753814,20.52,-3.27,19.53,22.78,0.54
20260504,20.05,20.1,19.6,19.7,2453014,20.45,-3.68,19.43,22.64,1.64
20260505,19.8,20.3,19.8,20.05,518232,20.42,-1.8,19.44,22.51,0.36
20260506,20.3,20.45,19.95,20.1,636691,20.39,-1.43,19.56,22.39,0.45
20260507,20.3,21.2,20,21.05,2609458,20.45,2.95,19.71,22.3,1.91
20260508,21.05,21.3,20.35,20.65,604701,20.46,0.91,19.88,22.2,0.46
20260511,20.7,20.75,20.2,20.3,467907,20.45,-0.73,20.03,22.11,0.36
20260512,20.3,20.35,19.85,19.9,684082,20.4,-2.47,20.18,22.02,0.54
20260514,17.95,17.95,17.95,17.95,250760,20.2,-11.14,20.19,21.89,0.2
20260515,16.2,16.2,16.2,16.2,401564,19.87,-18.46,20.09,21.73,0.35
20260518,14.65,16.65,14.65,15.5,8161868,19.5,-20.52,19.91,21.55,5.52
20260519,15.35,15.7,14.85,15.7,2106931,19.19,-18.17,19.73,21.39,1.38
20260520,15.55,15.55,14.7,14.95,2074798,18.83,-20.62,19.41,21.22,1.29
20260521,15.15,15.8,15.15,15.7,1445496,18.57,-15.46,19.04,21.06,0.88
20260522,15.8,16.45,15.3,16.15,1609275,18.37,-12.08,18.78,20.92,1.04
20260525,16.35,16.9,15.65,16,1231762,18.17,-11.95,18.55,20.76,0.8
20260526,16.1,16.5,15.8,16.15,940586,18,-10.3,18.36,20.61,0.61
20260527,16.3,16.5,15.85,16.05,1027593,17.84,-10.04,18.14,20.46,0.7
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.59
- over_600_ratio: 53.51
- over_800_ratio: 52.35
- over_1000_ratio: 51.59
- over_400_change_1w: 1.22
- over_800_change_1w: 0.49
- over_1000_change_1w: 0.49
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.37,,51.92,,51.16,,0,False,False
20260508,53.52,0.15,51.86,-0.06,51.1,-0.06,1,False,False
20260515,53.37,-0.15,51.86,0,51.1,0,0,False,False
20260522,54.59,1.22,52.35,0.49,51.59,0.49,1,True,True
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
| 20260527 | 3712 | 永崴投控 | 2 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
