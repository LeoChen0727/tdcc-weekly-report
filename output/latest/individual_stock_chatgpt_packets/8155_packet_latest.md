# INDIVIDUAL STOCK CHATGPT PACKET - 8155 博智

## Metadata
- generated_at: 2026-05-28 19:33:47 Asia/Taipei
- stock_id: 8155
- stock_name: 博智
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8155_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8155_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8155_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8155_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8155_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8155_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8155_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8155_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8155_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8155_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8155_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8155_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8155_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8155.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8155.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8155.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8155.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8155.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8155.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8155_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8155_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8155_latest.md?ref=main

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
- open: 406.5
- high: 414
- low: 387
- close: 393.5
- volume: 1817779
- ma5: 409.3
- ema23_primary: 400.98
- distance_to_ema23_pct: -1.87
- ma20: 418.4
- ma60: 329.27
- ma120: 257.59
- return_5d: -4.72
- return_20d: -5.52
- volume_ratio: 0.71
- distance_to_ma20_pct_auxiliary: -5.95
- distance_to_high_60_pct: -18.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,426,438.5,412.5,416,6462000,349.89,18.9,350.82,264.18,1.46
20260504,420,425.5,403.5,415,3160000,355.31,16.8,359.35,268.02,0.69
20260505,417,456.5,415,456.5,4863000,363.74,25.5,369.52,272.25,1.03
20260506,474.5,475,412,444,7307000,370.43,19.86,377.82,276.1,1.45
20260507,460.5,480,441.5,449,4703000,376.98,19.1,385.48,279.88,0.91
20260508,440,450,420.5,444,3192000,382.56,16.06,392.43,283.39,0.64
20260511,434,437,418.5,420,3635000,385.68,8.9,397.32,286.72,0.75
20260512,417,431.5,417,420,1747000,388.54,8.1,402.6,290.13,0.37
20260513,417,427.5,408,424,1651000,391.5,8.3,407.5,293.62,0.36
20260514,434,438,418.5,418.5,2524000,393.75,6.29,410.5,296.88,0.57
20260515,423,424,393,399,2496000,394.19,1.22,412.62,300.02,0.58
20260518,387.5,416.5,380,411,2156000,395.59,3.9,414.3,303.36,0.52
20260519,404.5,414.5,395,399.5,1349000,395.91,0.91,414.2,306.38,0.34
20260520,393,401.5,387.5,392,931000,395.59,-0.91,414,309.34,0.24
20260521,403,416,402,413,1515000,397.04,4.02,415.2,312.76,0.4
20260522,417,426,404,413.5,414000,398.41,3.79,417.9,316.16,0.12
20260525,425,432.5,414,421,422000,400.29,5.17,420,319.53,0.13
20260526,427,430,415,418,421000,401.77,4.04,420.07,322.95,0.14
20260527,422.5,424.5,399,400.5,409000,401.66,-0.29,419.55,326.02,0.16
20260528,406.5,414,387,393.5,1817779,400.98,-1.87,418.4,329.27,0.71
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.12
- over_600_ratio: 50.69
- over_800_ratio: 44.39
- over_1000_ratio: 39.95
- over_400_change_1w: 1.92
- over_800_change_1w: 1.47
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.88,,52.35,,43.78,,0,False,False
20260508,55.4,-3.48,46.37,-5.98,40.6,-3.18,0,False,False
20260515,52.2,-3.2,42.92,-3.45,39.98,-0.62,0,False,False
20260522,54.12,1.92,44.39,1.47,39.95,-0.03,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8155 | 博智 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8155 | 博智 | 1 | 1 | 2 | 2 | 2 | first_seen | 歷史上榜資料仍少，先當新訊號觀察。 |

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
