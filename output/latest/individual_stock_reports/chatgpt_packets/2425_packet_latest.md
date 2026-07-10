# INDIVIDUAL STOCK CHATGPT PACKET - 2425 承啟

## Metadata
- generated_at: 2026-07-10 22:26:51 Asia/Taipei
- stock_id: 2425
- stock_name: 承啟
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2425_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2425_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2425_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2425_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2425_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2425_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2425_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2425.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2425.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2425.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2425.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2425_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2425_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2425_latest.md?ref=main

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

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure
- acceptable_risk_reward

### post_entry_watch_items
- next_monthly_revenue
- next_tdcc_update
- 23ema_hold_or_reclaim
- volume_price_confirmation
- prior_high_breakout_quality
- sector_benchmark_strength
- event_follow_through
- warrant_overheat_check

### downgrade_reason
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260709
- open: 40.5
- high: 41.55
- low: 39.35
- close: 40.05
- volume: 1372182
- ma5: 40.71
- ema23_primary: 39.58
- distance_to_ema23_pct: 1.2
- ma20: 40.27
- ma60: 35.36
- ma120: 32.18
- return_5d: -4.98
- return_20d: 20.81
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: -0.55
- distance_to_high_60_pct: -13.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,34.9,36.45,34.9,36.45,1445426,34.33,6.19,34.85,31.56,1.54
20260612,40.05,40.05,35.9,35.95,8040355,34.46,4.32,34.91,31.64,6.46
20260615,36.3,38.7,36.2,38.35,3564003,34.79,10.25,35.12,31.76,2.58
20260616,38.8,42.15,38,39.5,8114548,35.18,12.29,35.47,31.9,4.64
20260617,40.5,43.45,39.8,41.25,11249764,35.68,15.6,35.9,32.08,4.9
20260618,41.2,41.2,39.15,39.4,3564426,35.99,9.46,36.16,32.25,1.46
20260622,40.1,40.55,39.35,39.35,2601268,36.27,8.48,36.4,32.41,1.02
20260623,39.3,39.7,37.8,39.35,2018359,36.53,7.72,36.61,32.58,0.78
20260624,39.05,40.25,38.35,38.5,1480798,36.69,4.92,36.79,32.75,0.56
20260625,38.95,42.35,38.75,42.35,6492729,37.17,13.95,37.09,32.99,2.26
20260626,42.75,43.25,39.05,39.45,7498184,37.36,5.61,37.33,33.19,2.37
20260629,39.95,42.4,39.2,41.1,7224384,37.67,9.11,37.6,33.44,2.07
20260630,42.7,45.2,41.2,45.2,12007000,38.3,18.03,38.03,33.75,2.98
20260701,46,46.5,43.2,43.55,6564000,38.73,12.44,38.4,34.04,1.53
20260702,42.5,44.3,41.55,42.15,3311000,39.02,8.03,38.69,34.3,0.75
20260703,42,42.45,41.2,42.35,1796534,39.3,7.77,39.02,34.56,0.4
20260706,43.05,43.05,41.2,41.6,1490000,39.49,5.35,39.33,34.81,0.33
20260707,42,42.25,39.7,39.9,1538086,39.52,0.96,39.66,35.03,0.34
20260708,39.9,40.8,38.8,39.65,1353290,39.53,0.3,39.93,35.2,0.29
20260709,40.5,41.55,39.35,40.05,1372182,39.58,1.2,40.27,35.36,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 49.98
- over_600_ratio: 45.89
- over_800_ratio: 41.2
- over_1000_ratio: 38.44
- over_400_change_1w: -2.05
- over_800_change_1w: -3.05
- over_1000_change_1w: -4.86
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.71,,39.98,,39.03,,0,False,False
20260508,46.73,0.02,39.13,-0.85,38.18,-0.85,1,False,False
20260515,47.45,0.72,38.71,-0.42,37.76,-0.42,2,False,False
20260522,47.89,0.44,39.73,1.02,37.91,0.15,3,True,True
20260529,47.67,-0.22,39.76,0.03,38.81,0.9,4,False,True
20260605,47.48,-0.19,39.65,-0.11,38.7,-0.11,0,False,False
20260612,48.69,1.21,40.48,0.83,38.7,0,1,False,True
20260618,50.11,1.42,41.2,0.72,39.31,0.61,2,True,True
20260626,52.03,1.92,44.25,3.05,43.3,3.99,3,True,True
20260703,49.98,-2.05,41.2,-3.05,38.44,-4.86,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2425 | 承啟 | pattern | 型態觀察 | 48.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額::股東現金股利新台幣9,649,883元(每股配發0.1元) 4.除權（息）交易日:115/07/03 5.最後過戶日:115/07/06 6.停止過戶起始日期:115/07/07 7.停止過戶截止日期:115/07/11 8.除權（息）基準日:115/07/11 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/07/31 13.其他應敘明事項: 本次現金股利依除息基準日股東名簿記載之股東持有股份計算，並按分配比例 計算至元為止，元以下捨去，不足一元之畸零款合計數，列入公司之其他收入。；degraded calendar context only: ex_dividend on 20260703; status=source_stale_cached; proximity=recent; model_effect_allowed=False; pdf_effect_allowed=False |
| 20260709 | 2425 | 承啟 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額::股東現金股利新台幣9,649,883元(每股配發0.1元) 4.除權（息）交易日:115/07/03 5.最後過戶日:115/07/06 6.停止過戶起始日期:115/07/07 7.停止過戶截止日期:115/07/11 8.除權（息）基準日:115/07/11 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/07/31 13.其他應敘明事項: 本次現金股利依除息基準日股東名簿記載之股東持有股份計算，並按分配比例 計算至元為止，元以下捨去，不足一元之畸零款合計數，列入公司之其他收入。；degraded calendar context only: ex_dividend on 20260703; status=source_stale_cached; proximity=recent; model_effect_allowed=False; pdf_effect_allowed=False；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 2425 | 承啟 | revenue_breakout_low_response | 營收爆發低反應股 | 19.0 | 5.0 | A_優先追蹤 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額::股東現金股利新台幣9,649,883元(每股配發0.1元) 4.除權（息）交易日:115/07/03 5.最後過戶日:115/07/06 6.停止過戶起始日期:115/07/07 7.停止過戶截止日期:115/07/11 8.除權（息）基準日:115/07/11 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/07/31 13.其他應敘明事項: 本次現金股利依除息基準日股東名簿記載之股東持有股份計算，並按分配比例 計算至元為止，元以下捨去，不足一元之畸零款合計數，列入公司之其他收入。；degraded calendar context only: ex_dividend on 20260703; status=source_stale_cached; proximity=recent; model_effect_allowed=False; pdf_effect_allowed=False；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2425 | 承啟 | 13 | 6 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
