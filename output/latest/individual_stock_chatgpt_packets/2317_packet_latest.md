# INDIVIDUAL STOCK CHATGPT PACKET - 2317 鴻海

## Metadata
- generated_at: 2026-05-30 23:41:19 Asia/Taipei
- stock_id: 2317
- stock_name: 鴻海
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 272
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2317_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2317_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2317_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2317_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2317_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2317_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2317_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2317_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2317_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2317_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2317_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2317_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2317_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2317.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2317.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2317.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2317.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2317.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2317.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2317_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2317_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2317_latest.md?ref=main

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
- open: 269
- high: 289
- low: 268
- close: 289
- volume: 289511198
- ma5: 267.2
- ema23_primary: 248.63
- distance_to_ema23_pct: 16.24
- ma20: 251.78
- ma60: 223.04
- ma120: 224.92
- return_5d: 15.6
- return_20d: 31.66
- volume_ratio: 2.83
- distance_to_ma20_pct_auxiliary: 14.79
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,224,229.5,223.5,227.5,57506042,214.71,5.96,211.32,214.32,0.83
20260505,227.5,240,227,239.5,162873566,216.78,10.48,213.65,214.57,2.16
20260506,246.5,253,245,252,240330399,219.71,14.69,216.65,215.02,2.8
20260507,255,258,250,253.5,128767846,222.53,13.92,219.25,215.48,1.45
20260508,254,256,245.5,250,102375417,224.82,11.2,221.75,215.92,1.12
20260511,256.5,258,251,252,63063740,227.08,10.97,224.32,216.44,0.69
20260512,254,254,246,250,84325367,228.99,9.17,226.82,217.03,0.9
20260513,246.5,251,242.5,251,72415109,230.83,8.74,229,217.61,0.76
20260514,255,255,244,244.5,73360409,231.97,5.4,230.85,218.03,0.77
20260515,249,260,247,248.5,138413483,233.34,6.5,232.93,218.58,1.39
20260518,251,251,241,248.5,63512356,234.61,5.92,235.05,219.14,0.63
20260519,251,254,244,245,70223341,235.47,4.05,236.93,219.58,0.69
20260520,246.5,246.5,239.5,240,62650287,235.85,1.76,238.38,219.9,0.61
20260521,245,249,244,247.5,51483466,236.82,4.51,239.7,220.24,0.53
20260522,249,251.5,245,250,56310552,237.92,5.08,240.95,220.6,0.61
20260525,255,263.5,255,261,122990174,239.84,8.82,242.93,221.08,1.31
20260526,262.5,263.5,257,259,55665305,241.44,7.27,244.47,221.29,0.61
20260527,263,269,261,264,78352856,243.32,8.5,246.4,221.64,0.87
20260528,265,269.5,259.5,263,73792269,244.96,7.36,248.3,222.04,0.81
20260529,269,289,268,289,289511198,248.63,16.24,251.78,223.04,2.83
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 70.43
- over_600_ratio: 69.24
- over_800_ratio: 68.48
- over_1000_ratio: 67.79
- over_400_change_1w: 0.67
- over_800_change_1w: 0.67
- over_1000_change_1w: 0.72
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.6,,65.63,,64.91,,0,False,False
20260508,69.22,1.62,67.22,1.59,66.52,1.61,1,True,True
20260515,69.39,0.17,67.41,0.19,66.71,0.19,2,True,True
20260522,69.76,0.37,67.81,0.4,67.07,0.36,3,True,True
20260529,70.43,0.67,68.48,0.67,67.79,0.72,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 2317 | 鴻海 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | call_put_bullish | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 2317 | 鴻海 | 8 | 8 | 5 | 8 | 8 | repeated_but_no_breakout | 近 10 日上榜 8 日、近 20 日上榜 8 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 2317 | 鴻海 | 527 | 47 | 298877460.0 | 920810.0 | 324.58 | call_put_bullish | 3 | 認購權證成交金額很大且認購/認售比偏高，需檢查標的是否高位追價或獲利結清；認購權證成交量與成交金額同步偏大，短線資金關注度高 |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
