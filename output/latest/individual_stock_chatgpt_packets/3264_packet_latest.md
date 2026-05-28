# INDIVIDUAL STOCK CHATGPT PACKET - 3264 欣銓

## Metadata
- generated_at: 2026-05-28 19:32:21 Asia/Taipei
- stock_id: 3264
- stock_name: 欣銓
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3264_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3264_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3264_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3264_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3264_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3264_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3264_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3264_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3264_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3264_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3264_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3264_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3264_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3264.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3264.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3264.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3264.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3264.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3264.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3264_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3264_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3264_latest.md?ref=main

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
- open: 231
- high: 249
- low: 227.5
- close: 235.5
- volume: 16614457
- ma5: 228.3
- ema23_primary: 218.16
- distance_to_ema23_pct: 7.95
- ma20: 224.7
- ma60: 186.13
- ma120: 155.09
- return_5d: 7.53
- return_20d: 18.05
- volume_ratio: 1.58
- distance_to_ma20_pct_auxiliary: 4.81
- distance_to_high_60_pct: -5.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,197.5,202.5,192,195,10284000,184.78,5.53,186.38,163.54,0.55
20260504,197,214.5,197,214.5,12305000,187.26,14.55,188.8,164.6,0.66
20260505,220,235.5,218,235.5,18479000,191.28,23.12,192.53,165.85,1
20260506,244,249,218.5,226,26935000,194.17,16.39,196.03,166.91,1.39
20260507,236,248.5,230,248.5,15151000,198.7,25.06,200.22,168.28,0.78
20260508,240,244.5,224,224,20591000,200.81,11.55,202.4,169.4,1.07
20260511,220,228.5,216.5,225.5,8182000,202.87,11.16,204.22,170.5,0.47
20260512,227.5,234,222,228.5,11008000,205,11.46,206.07,171.75,0.65
20260513,224,231,222,230,5615000,207.09,11.07,208.22,173.01,0.35
20260514,234,237,227,229,9426000,208.91,9.62,210.32,174.26,0.6
20260515,232,241,222,226,19092000,210.34,7.45,212.88,175.56,1.22
20260518,219,230,217.5,230,5719000,211.97,8.5,215.78,177.01,0.37
20260519,230,230,210,214.5,11515000,212.18,1.09,217.12,178.07,0.76
20260520,212,214,203.5,206.5,11803000,211.71,-2.46,217.15,178.84,0.79
20260521,212.5,221,212,219,6281000,212.32,3.15,217.6,179.95,0.47
20260522,221,229.5,218,221.5,225000,213.08,3.95,218.8,181.16,0.02
20260525,226,232,223,224,227000,213.99,4.68,219.5,182.26,0.02
20260526,228,233.5,221,231,229000,215.41,7.24,221.35,183.51,0.02
20260527,238.5,239,226.5,229.5,232000,216.58,5.96,222.9,184.71,0.02
20260528,231,249,227.5,235.5,16614457,218.16,7.95,224.7,186.13,1.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.76
- over_600_ratio: 69.14
- over_800_ratio: 66.13
- over_1000_ratio: 63.97
- over_400_change_1w: -0.18
- over_800_change_1w: -0.08
- over_1000_change_1w: 0.49
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.69,,66.36,,63.8,,0,False,False
20260508,72.4,0.71,67.28,0.92,64.53,0.73,1,True,True
20260515,70.94,-1.46,66.21,-1.07,63.48,-1.05,0,False,False
20260522,70.76,-0.18,66.13,-0.08,63.97,0.49,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3264 | 欣銓 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 3264 | 欣銓 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260528 | 3264 | 欣銓 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3264 | 欣銓 | 1 | 1 | 2 | 2 | 2 | first_seen | 歷史上榜資料仍少，先當新訊號觀察。 |

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
