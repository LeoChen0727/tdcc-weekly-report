# INDIVIDUAL STOCK CHATGPT PACKET - 3003 健和興

## Metadata
- generated_at: 2026-05-28 19:32:11 Asia/Taipei
- stock_id: 3003
- stock_name: 健和興
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3003_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3003_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3003_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3003_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3003_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3003_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3003.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3003.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3003.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3003.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3003.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3003.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3003_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3003_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3003_latest.md?ref=main

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
- open: 62.9
- high: 64.7
- low: 61.8
- close: 62.2
- volume: 1965070
- ma5: 62.14
- ema23_primary: 58.75
- distance_to_ema23_pct: 5.87
- ma20: 58.85
- ma60: 53.9
- ma120: 51.05
- return_5d: 2.81
- return_20d: 12.07
- volume_ratio: 1.37
- distance_to_ma20_pct_auxiliary: 5.68
- distance_to_high_60_pct: -6.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,56.4,56.6,54.1,54.7,625988,53.14,2.94,53.07,50.66,0.8
20260504,55.6,56,54.6,55.5,733927,53.34,4.06,53.35,50.75,0.91
20260505,56.1,56.3,54.5,55.5,609812,53.52,3.71,53.66,50.84,0.74
20260506,56,56.4,54.5,56,740218,53.72,4.24,54.01,50.95,0.86
20260507,56,56.6,55.5,55.7,613665,53.89,3.36,54.3,51.06,0.7
20260508,55.7,56.8,55.3,55.8,863154,54.05,3.24,54.57,51.18,0.95
20260511,56.4,59.3,56,59.1,2446931,54.47,8.5,55.03,51.38,2.41
20260512,58.6,60.8,57.5,59.8,2186000,54.91,8.9,55.34,51.6,2.16
20260513,58.6,59.8,57.5,57.9,1259771,55.16,4.96,55.51,51.78,1.25
20260514,58.3,62.5,58.3,61,2863192,55.65,9.62,55.88,52,2.61
20260515,61.6,62,57.7,58.6,1769660,55.89,4.84,56.09,52.17,1.57
20260518,57.7,60,56.3,59,1020092,56.15,5.07,56.3,52.37,0.9
20260519,58.5,59.2,58,58.3,604675,56.33,3.49,56.45,52.55,0.55
20260520,58.3,59.1,57.7,59,709662,56.55,4.33,56.66,52.73,0.64
20260521,59.7,60.8,59.3,60.5,969804,56.88,6.36,56.88,52.92,0.89
20260522,60.9,62.2,59.4,61.9,1655637,57.3,8.03,57.27,53.13,1.49
20260525,62.9,63.5,60.8,61,1738481,57.61,5.89,57.62,53.31,1.51
20260526,61.6,62.8,59.2,62.7,1591485,58.03,8.04,58.06,53.51,1.32
20260527,65.5,66.7,61.8,62.9,3753256,58.44,7.63,58.52,53.72,2.74
20260528,62.9,64.7,61.8,62.2,1965070,58.75,5.87,58.85,53.9,1.37
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.65
- over_600_ratio: 55.48
- over_800_ratio: 51.91
- over_1000_ratio: 50.85
- over_400_change_1w: 0.19
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.12
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.01,,51.64,,50.57,,0,False,False
20260508,57.48,0.47,51.68,0.04,50.6,0.03,1,True,True
20260515,57.46,-0.02,51.87,0.19,50.73,0.13,2,False,True
20260522,57.65,0.19,51.91,0.04,50.85,0.12,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3003 | 健和興 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 3003 | 健和興 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3003 | 健和興 | 4 | 1 | 4 | 4 | 4 | repeated_but_no_breakout | 近 10 日上榜 4 日、近 20 日上榜 4 日，尚未突破，需分辨醞釀或鈍化。 |

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
