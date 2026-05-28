# INDIVIDUAL STOCK CHATGPT PACKET - 2408 南亞科

## Metadata
- generated_at: 2026-05-28 20:18:40 Asia/Taipei
- stock_id: 2408
- stock_name: 南亞科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2408_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2408_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2408_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2408_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2408_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2408_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2408_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2408_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2408_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2408_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2408_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2408_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2408_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2408.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2408.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2408.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2408.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2408.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2408.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2408_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2408_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2408_latest.md?ref=main

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
- open: 310
- high: 339
- low: 306
- close: 324
- volume: 226715301
- ma5: 309.2
- ema23_primary: 285.94
- distance_to_ema23_pct: 13.31
- ma20: 292.05
- ma60: 248.8
- ma120: 235.2
- return_5d: 10.58
- return_20d: 37.87
- volume_ratio: 1.44
- distance_to_ma20_pct_auxiliary: 10.94
- distance_to_high_60_pct: -8.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,239.5,240,214.5,215.5,125666192,221.76,-2.82,215.78,245.53,1.18
20260504,223,237,217,237,144354307,223.03,6.26,217.07,244.96,1.34
20260505,243,259,242.5,256.5,207567196,225.82,13.59,219.88,244.47,1.85
20260506,282,282,270.5,282,149468917,230.5,22.34,223.68,244.55,1.29
20260507,293,296,278,287,197355586,235.21,22.02,226.88,244.38,1.63
20260508,282,289,260,274,130863185,238.44,14.91,230.32,244,1.06
20260511,300.5,301,296,301,108987498,243.65,23.54,234.62,243.57,0.88
20260512,312.5,325,301,321,217595653,250.1,28.35,239.4,244.03,1.67
20260513,311.5,322.5,303,321,106103420,256.01,25.39,244.45,244.75,0.83
20260514,342.5,353,335.5,341,181771498,263.09,29.61,250.93,245.52,1.39
20260515,330.5,334.5,308.5,311.5,160442326,267.12,16.61,255.82,246.12,1.18
20260518,300,309,287,305,117077708,270.28,12.85,260.57,246.81,0.84
20260519,291.5,295,274.5,274.5,118906988,270.63,1.43,263.95,246.81,0.84
20260520,279.5,285,265.5,275,123868197,271,1.48,266.7,246.88,0.87
20260521,291.5,295,280,293,149826596,272.83,7.39,270.4,247.12,1.03
20260522,299.5,321,296,310.5,157819181,275.97,12.51,275.52,247.48,1.08
20260525,295,303.5,288,296,155862832,277.64,6.61,280.02,247.45,1.04
20260526,300.5,314,295.5,303.5,152949355,279.79,8.47,283.88,247.71,1.02
20260527,333,333.5,306,312,206216639,282.48,10.45,287.6,248.15,1.37
20260528,310,339,306,324,226715301,285.94,13.31,292.05,248.8,1.44
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.05
- over_600_ratio: 80.25
- over_800_ratio: 79.66
- over_1000_ratio: 79.03
- over_400_change_1w: -2.09
- over_800_change_1w: -2.08
- over_1000_change_1w: -2.13
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.47,,79.2,,78.62,,0,False,False
20260508,82.16,1.69,80.79,1.59,80.23,1.61,1,True,True
20260515,83.14,0.98,81.74,0.95,81.16,0.93,2,True,True
20260522,81.05,-2.09,79.66,-2.08,79.03,-2.13,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2408 | 南亞科 | pullback_rebound | 回檔後短線轉強 | 63.0 |  |  |  |  | mixed_flow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 2408 | 南亞科 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | mixed_flow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260528 | 2408 | 南亞科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 60.0 |  |  | neckline_challenge |  | mixed_flow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 2408 | 南亞科 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | mixed_flow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2408 | 南亞科 | 6 | 6 | 5 | 6 | 6 | continued_overheated | 連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2408 | 南亞科 | 177 | 15 | 208818110.0 | 2410480.0 | 86.63 | mixed_flow | 0 | 認購權證成交金額很大且認購/認售比偏高，需檢查標的是否高位追價或獲利結清；認購權證成交量與成交金額同步偏大，短線資金關注度高 |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
