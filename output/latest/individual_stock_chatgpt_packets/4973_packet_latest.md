# INDIVIDUAL STOCK CHATGPT PACKET - 4973 廣穎

## Metadata
- generated_at: 2026-05-28 19:32:52 Asia/Taipei
- stock_id: 4973
- stock_name: 廣穎
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4973_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4973_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4973_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4973_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4973_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4973_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4973_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4973_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4973_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4973_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4973_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4973_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4973_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4973.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4973.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4973.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4973.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4973.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4973.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4973_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4973_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4973_latest.md?ref=main

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
- open: 152.5
- high: 152.5
- low: 146.5
- close: 152.5
- volume: 8787744
- ma5: 130.2
- ema23_primary: 111.34
- distance_to_ema23_pct: 36.97
- ma20: 111.15
- ma60: 84.82
- ma120: 63.56
- return_5d: 41.2
- return_20d: 74.69
- volume_ratio: 1.42
- distance_to_ma20_pct_auxiliary: 37.2
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,88.1,88.9,82.1,83.1,5283000,79.22,4.9,79.63,64.06,0.74
20260504,84.8,86.5,83.3,85.4,3420000,79.73,7.11,80.5,64.65,0.47
20260505,86.3,88.4,84.3,87.7,3571000,80.4,9.09,81.49,65.25,0.48
20260506,92.5,96.4,91.7,91.7,12173000,81.34,12.74,82.61,65.96,1.58
20260507,94,100.5,90.5,95.5,9600000,82.52,15.73,83.58,66.71,1.23
20260508,94.2,105,93,99.6,15712000,83.94,18.65,84.99,67.52,1.92
20260511,106,109.5,106,109.5,5348000,86.07,27.22,86.55,68.49,0.68
20260512,115.5,120,114.5,120,12603000,88.9,34.99,88.56,69.71,1.56
20260513,119.5,121.5,112,118.5,9396000,91.37,29.7,90.5,70.93,1.14
20260514,122,129,116,116.5,11123000,93.46,24.65,92.42,72.12,1.29
20260515,119,121.5,114,117,7470000,95.42,22.61,94.42,73.34,0.85
20260518,115,120.5,111.5,120.5,4788000,97.51,23.58,96.57,74.66,0.54
20260519,118,118,109.5,110,5945000,98.55,11.62,98.1,75.73,0.66
20260520,110,111,104,109,3890000,99.42,9.63,99.19,76.81,0.45
20260521,114,114.5,107.5,108,3932000,100.14,7.85,100.08,77.85,0.48
20260522,109.5,118,108.5,115,114000,101.38,13.44,101.7,78.99,0.01
20260525,118,119.5,113.5,118,117000,102.76,14.83,103.6,80.16,0.02
20260526,119.5,129.5,117.5,126.5,125000,104.74,20.78,105.52,81.5,0.02
20260527,139,139,138.5,139,139000,107.59,29.19,107.89,83.05,0.02
20260528,152.5,152.5,146.5,152.5,8787744,111.34,36.97,111.15,84.82,1.42
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 33.51
- over_600_ratio: 26.22
- over_800_ratio: 24.11
- over_1000_ratio: 21.34
- over_400_change_1w: 1.42
- over_800_change_1w: -0.78
- over_1000_change_1w: 2.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.65,,23.5,,19.27,,0,False,False
20260508,33.54,2.89,22.2,-1.3,19.27,0,1,False,False
20260515,32.09,-1.45,24.89,2.69,19.27,0,2,False,True
20260522,33.51,1.42,24.11,-0.78,21.34,2.07,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 4973 | 廣穎 | true_breakout | 嚴格突破 | 82.0 |  |  | breakout_confirmed |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 4973 | 廣穎 | 1 | 1 | 2 | 2 | 2 | first_seen | 歷史上榜資料仍少，先當新訊號觀察。 |

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
