# INDIVIDUAL STOCK CHATGPT PACKET - 2537 聯上發

## Metadata
- generated_at: 2026-05-26 21:25:08 Asia/Taipei
- stock_id: 2537
- stock_name: 聯上發
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2537_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2537_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2537_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2537_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2537_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2537_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2537_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2537_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2537_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2537_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2537_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2537_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2537_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2537.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2537.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2537.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2537.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2537.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2537.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2537_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2537_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2537_latest.md?ref=main

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
- open: 9.57
- high: 9.63
- low: 9.52
- close: 9.58
- volume: 1313073
- ma5: 9.64
- ema23_primary: 9.97
- distance_to_ema23_pct: -3.88
- ma20: 10.01
- ma60: 10.21
- ma120: 10.59
- return_5d: -0.93
- return_20d: -7.88
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: -4.29
- distance_to_high_60_pct: -12.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,10.45,10.45,10.3,10.35,504048,10.42,-0.64,10.41,10.4,0.66
20260429,10.45,10.45,10.35,10.45,656354,10.42,0.29,10.42,10.39,0.85
20260430,10.45,10.55,10.2,10.2,1453368,10.4,-1.93,10.42,10.38,1.81
20260504,10.3,10.3,10.2,10.25,929840,10.39,-1.33,10.41,10.38,1.14
20260505,10.25,10.3,10.2,10.25,580600,10.38,-1.22,10.41,10.37,0.71
20260506,10.25,10.45,10.25,10.3,819400,10.37,-0.68,10.41,10.36,0.97
20260507,10.35,10.5,10.3,10.5,973551,10.38,1.14,10.41,10.36,1.13
20260508,10.55,10.55,10.25,10.25,621814,10.37,-1.16,10.41,10.36,0.71
20260511,10.3,10.35,10.2,10.25,698130,10.36,-1.07,10.4,10.35,0.8
20260512,10.25,10.25,10.05,10.1,1403332,10.34,-2.31,10.38,10.35,1.56
20260513,10.05,10.15,10,10,1280440,10.31,-3.01,10.36,10.34,1.36
20260514,10.1,10.1,9.98,9.99,1128181,10.28,-2.86,10.33,10.33,1.16
20260515,10.05,10.05,9.5,9.66,2402270,10.23,-5.59,10.3,10.31,2.24
20260518,9.75,9.86,9.62,9.76,778193,10.19,-4.24,10.27,10.31,0.72
20260519,9.71,9.87,9.65,9.67,750635,10.15,-4.72,10.23,10.29,0.69
20260520,9.75,9.75,9.58,9.67,819712,10.11,-4.34,10.19,10.28,0.76
20260521,9.76,9.84,9.74,9.83,573027,10.09,-2.54,10.15,10.27,0.58
20260522,9.89,9.89,9.5,9.57,2015643,10.04,-4.71,10.1,10.25,2
20260525,9.57,9.6,9.38,9.55,1412427,10,-4.52,10.05,10.23,1.36
20260526,9.57,9.63,9.52,9.58,1313073,9.97,-3.88,10.01,10.21,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.39
- over_600_ratio: 55.77
- over_800_ratio: 52.82
- over_1000_ratio: 51.63
- over_400_change_1w: -0.17
- over_800_change_1w: -0.1
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.02,,51.33,,49.58,,0,False,False
20260508,57.79,0.77,52.72,1.39,51.3,1.72,1,True,True
20260515,58.56,0.77,52.92,0.2,51.78,0.48,2,True,True
20260522,58.39,-0.17,52.82,-0.1,51.63,-0.15,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2537 | 聯上發 | revenue_pullback | 營收成長股價回檔 | 82.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260526 | 2537 | 聯上發 | revenue_breakout_low_response | 營收爆發低反應股 | 22.0 | 6.0 | B_可觀察 |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2537 | 聯上發 | 4 | 4 | 4 | 4 | 4 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
