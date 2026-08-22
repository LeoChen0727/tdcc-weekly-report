# INDIVIDUAL STOCK CHATGPT PACKET - 2327 國巨*

## Metadata
- generated_at: 2026-08-22 22:26:49 Asia/Taipei
- stock_id: 2327
- stock_name: 國巨*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 331
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2327_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2327_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2327_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2327_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2327_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2327_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2327_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2327.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2327.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2327.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2327.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2327_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2327_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2327_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260821
- open: 561
- high: 567
- low: 553
- close: 554
- volume: 20632149
- ma5: 575.2
- ema23_primary: 617.68
- distance_to_ema23_pct: -10.31
- ma20: 570.58
- ma60: 775.17
- ma120: 558.47
- return_5d: -10.93
- return_20d: -13.71
- volume_ratio: 0.4
- distance_to_ma20_pct_auxiliary: -2.9
- distance_to_high_60_pct: -54.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,650,655,590,625,56857378,790.88,-20.97,847.7,745.85,0.98
20260728,575,582,563,563,35712662,771.89,-27.06,823.85,749.95,0.62
20260729,539,545,507,507,51708941,749.81,-32.38,792.2,752.69,0.9
20260730,479.5,527,456.5,456.5,106828585,725.37,-37.07,758.02,754.49,1.81
20260731,502,502,502,502,6398641,706.76,-28.97,730.38,757.23,0.11
20260803,534,552,526,552,22438342,693.86,-20.45,705.73,760.23,0.4
20260804,581,583,545,566,97625584,683.21,-17.16,683.77,763.18,1.66
20260805,608,618,568,578,63678413,674.44,-14.3,667.42,766.29,1.09
20260806,563,578,536,570,53296450,665.74,-14.38,651.38,768.8,0.92
20260807,560,578,531,540,44277453,655.26,-17.59,633.38,770.8,0.77
20260810,558,578,557,573,36354305,648.4,-11.63,621.23,772.65,0.65
20260811,568,623,567,617,81650622,645.79,-4.46,613.17,775.34,1.47
20260812,607,625,600,602,56066841,642.14,-6.25,603.38,777.02,1
20260813,631,662,626,662,46850905,643.79,2.83,597.67,779.77,0.84
20260814,668,668,617,622,73827926,641.98,-3.11,593.83,781.48,1.29
20260817,620,622,596,608,36648051,639.14,-4.87,592.73,782.08,0.64
20260818,614,615,574,576,37659843,633.88,-9.13,588.02,781.19,0.69
20260819,547,590,547,576,56295383,629.06,-8.43,581.67,779.27,1.06
20260820,583,583,550,562,43070768,623.47,-9.86,574.98,777.62,0.82
20260821,561,567,553,554,20632149,617.68,-10.31,570.58,775.17,0.4
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 68.69
- over_600_ratio: 66.74
- over_800_ratio: 65.01
- over_1000_ratio: 63.94
- over_400_change_1w: -1.97
- over_800_change_1w: -2.05
- over_1000_change_1w: -2.04
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,74.05,-0.73,70.49,-0.66,69.06,-0.54,0,False,False
20260612,73.47,-0.58,69.8,-0.69,68.55,-0.51,0,False,False
20260618,73.87,0.4,70.2,0.4,68.78,0.23,1,True,True
20260626,74.34,0.47,70.82,0.62,69.45,0.67,2,True,True
20260703,73.9,-0.44,70.47,-0.35,68.96,-0.49,0,False,False
20260709,73.38,-0.52,69.95,-0.52,68.63,-0.33,0,False,False
20260717,72.87,-0.51,69.46,-0.49,68.1,-0.53,0,False,False
20260724,72.27,-0.6,69.06,-0.4,67.7,-0.4,0,False,False
20260731,71.11,-1.16,68.06,-1,66.64,-1.06,0,False,False
20260807,70.4,-0.71,67.03,-1.03,65.68,-0.96,0,False,False
20260814,70.66,0.26,67.06,0.03,65.98,0.3,1,True,True
20260821,68.69,-1.97,65.01,-2.05,63.94,-2.04,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2327 | 國巨* | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:國巨股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由: 國巨公司今日公布 2026 年 7 月份自結合併營收為 NT$ 161.31 億元， 單月營收較上月增加 5.0%，較去年同期增加 51.5%，再創下單月營收歷史新高(若以 美元換算，單月營收較上月增加 3.3%，較去年同期增加 39.0% )；累計1-7 月自結合 併營收為NT$ 987.53 億元，較去年同期增加 32.5% (若以美元換算，較去年同期增加 31.7% )。  7 月份合併營收較上月增加，主要受惠於AI相關應用需求持續強勁，標準品及特殊品 亦呈現穩定成長，各個產品應用也溫和成長。  展望未來，隨著 AI 應用需求持續成長，電子元件產業正迎來結構性轉變，公司將持 續密切關注相關發展。儘管地緣政治情勢仍存在不確定性，但客戶庫存水位目前仍維 持健康，公司將審慎因應經濟環境變化，並彈性調整以降低關稅政策及匯率波動帶來 的影響。  6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2327 | 國巨* | 6 | 6 | 5 | 9 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2327 | 國巨* | 216 | 30 | 20401550.0 | 1675780.0 | 12.17 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
