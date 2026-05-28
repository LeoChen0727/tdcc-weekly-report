# INDIVIDUAL STOCK CHATGPT PACKET - 3680 家登

## Metadata
- generated_at: 2026-05-28 19:32:34 Asia/Taipei
- stock_id: 3680
- stock_name: 家登
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3680_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3680_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3680_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3680_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3680_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3680_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3680_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3680_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3680_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3680_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3680_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3680_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3680_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3680.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3680.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3680.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3680.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3680.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3680.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3680_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3680_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3680_latest.md?ref=main

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
- open: 562
- high: 568
- low: 530
- close: 535
- volume: 2318721
- ma5: 568.8
- ema23_primary: 540.91
- distance_to_ema23_pct: -1.09
- ma20: 565.75
- ma60: 462.57
- ma120: 422.64
- return_5d: -1.65
- return_20d: 6.79
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: -5.44
- distance_to_high_60_pct: -14.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,513,551,511,537,8010000,448.39,19.76,438.43,414.68,2.1
20260504,549,582,545,564,7139000,458.03,23.14,447.77,416.73,1.74
20260505,579,602,572,582,5181000,468.36,24.26,458.12,419.15,1.2
20260506,587,604,554,581,5352000,477.74,21.61,468.32,421.47,1.18
20260507,584,608,570,585,4192000,486.68,20.2,477.35,423.62,0.9
20260508,590,614,557,560,5499000,492.79,13.64,484.48,426.05,1.13
20260511,580,616,579,616,3908000,503.06,22.45,495.75,429.61,0.8
20260512,617,623,600,602,3492000,511.3,17.74,506.77,432.89,0.7
20260513,592,602,563,588,3151000,517.7,13.58,515.95,435.92,0.65
20260514,593,603,573,580,3513000,522.89,10.92,524.85,438.69,0.71
20260515,592,592,557,568,3139000,526.65,7.85,531.5,441.48,0.66
20260518,552,552,518,544,3486000,528.09,3.01,537.2,444,0.73
20260519,540,540,503,514,3667000,526.92,-2.45,539.25,445.77,0.78
20260520,513,519,498.5,506,2608000,525.18,-3.65,539.4,447.47,0.59
20260521,529,555,525,544,2412000,526.74,3.28,541.85,449.99,0.56
20260522,550,581,541,568,565000,530.18,7.13,546.83,452.63,0.14
20260525,590,615,580,595,601000,535.58,11.09,553.62,455.61,0.15
20260526,603,610,583,589,594000,540.04,9.07,560.62,458.38,0.16
20260527,600,601,548,557,568000,541.45,2.87,564.05,460.57,0.16
20260528,562,568,530,535,2318721,540.91,-1.09,565.75,462.57,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.34
- over_600_ratio: 55.83
- over_800_ratio: 50
- over_1000_ratio: 48.05
- over_400_change_1w: 0.27
- over_800_change_1w: -0.97
- over_1000_change_1w: -0.25
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.27,,46.21,,41.45,,0,False,False
20260508,60.17,4.9,49.56,3.35,45.76,4.31,1,True,True
20260515,61.07,0.9,50.97,1.41,48.3,2.54,2,False,True
20260522,61.34,0.27,50,-0.97,48.05,-0.25,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3680 | 家登 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 3680 | 家登 | revenue_pullback | 營收成長股價回檔 | 56.0 |  |  |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260521 | 3680 | 家登 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3680 | 家登 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
