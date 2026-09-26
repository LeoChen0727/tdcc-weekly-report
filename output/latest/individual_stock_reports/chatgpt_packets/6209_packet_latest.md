# INDIVIDUAL STOCK CHATGPT PACKET - 6209 今國光

## Metadata
- generated_at: 2026-09-26 22:17:20 Asia/Taipei
- stock_id: 6209
- stock_name: 今國光
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6209_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6209_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6209_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6209_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6209_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6209_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6209_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6209.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6209.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6209.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6209.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6209_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6209_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6209_latest.md?ref=main

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
- date: 20260924
- open: 78.7
- high: 80.3
- low: 78.3
- close: 79.9
- volume: 5832314
- ma5: 78.9
- ema23_primary: 77.67
- distance_to_ema23_pct: 2.87
- ma20: 79.31
- ma60: 74.43
- ma120: 74.35
- return_5d: 2.44
- return_20d: 4.44
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: 0.74
- distance_to_high_60_pct: -9.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,77,78.1,75.8,76.7,11986491,71.84,6.77,71.75,76.68,1.82
20260831,75.8,82.2,75.8,79.5,20751886,72.47,9.69,72.24,76.59,2.83
20260901,81,84.8,80.4,81.9,21793225,73.26,11.79,72.88,76.49,2.66
20260902,80.5,88.5,80.5,84.3,33317698,74.18,13.64,73.5,76.56,3.45
20260903,84.5,85.7,80.5,81.1,19919693,74.76,8.49,73.72,76.45,1.94
20260904,81.8,82.2,78.2,81.5,10548829,75.32,8.21,74.08,76.45,1.01
20260907,81.5,81.8,77.6,79.1,8030529,75.63,4.58,74.33,76.45,0.76
20260908,80.5,81.1,77.1,77.5,7464127,75.79,2.26,74.46,76.37,0.69
20260909,77.9,80.3,77.5,79.1,6297256,76.07,3.99,74.67,76.24,0.58
20260910,79.1,81,78.4,81,8089637,76.48,5.92,75.19,76,0.74
20260911,79,84.8,78.6,80,18994955,76.77,4.21,75.7,75.74,1.63
20260914,78.9,81.6,76.5,76.5,8971424,76.75,-0.32,75.97,75.4,0.76
20260915,75.9,78.5,75.3,75.6,5765279,76.65,-1.37,76.36,75.04,0.48
20260916,76.2,81,76.2,80,11325045,76.93,3.99,77.02,74.87,0.92
20260917,80,80.5,78,78,7575261,77.02,1.27,77.47,74.69,0.6
20260918,78.3,80.4,78.3,80.4,6170241,77.3,4.01,78.01,74.53,0.49
20260921,81,81.2,79.1,79.1,4049535,77.45,2.13,78.58,74.5,0.32
20260922,79.6,79.9,76.9,77.1,4731553,77.42,-0.42,78.98,74.46,0.37
20260923,78,81.5,77.5,78,6511348,77.47,0.68,79.14,74.42,0.52
20260924,78.7,80.3,78.3,79.9,5832314,77.67,2.87,79.31,74.43,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 37.69
- over_600_ratio: 36.06
- over_800_ratio: 32.9
- over_1000_ratio: 29.98
- over_400_change_1w: -0.16
- over_800_change_1w: -0.45
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,40.37,0.45,35.25,-0.41,33.33,-0.44,2,False,False
20260717,40.7,0.33,36.7,1.45,33.64,0.31,3,True,True
20260724,41.48,0.78,37.44,0.74,33.5,-0.14,4,False,True
20260731,40.56,-0.92,36.85,-0.59,32.95,-0.55,0,False,False
20260807,42.03,1.47,37.3,0.45,33.83,0.88,1,True,True
20260814,40.12,-1.91,35.27,-2.03,31.3,-2.53,0,False,False
20260821,39.62,-0.5,34.14,-1.13,30.7,-0.6,0,False,False
20260828,38.84,-0.78,33.87,-0.27,30.84,0.14,1,False,True
20260904,38.54,-0.3,32.53,-1.34,30.56,-0.28,0,False,False
20260911,38.38,-0.16,33.91,1.38,31.97,1.41,1,False,True
20260918,37.85,-0.53,33.35,-0.56,30.01,-1.96,0,False,False
20260924,37.69,-0.16,32.9,-0.45,29.98,-0.03,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6209 | 今國光 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  | call_strong_inflow | stale_signal | 內容：依今國光三發行及轉換辦法第十七條規定辦理。 發行公司於115年10月13日至115年11月11日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、本公司國內第三次有擔保轉換公司債發行及轉換辦法第十七條(一)規定，本轉換公司債發行滿三個月翌日(115年1月24日)起至到期日前四十日(117年9月13 日)止，若本公司普通股之收盤價格連續三十個營業日超過當時轉換價格達百分之三十者，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之投資人，則以公告方式為之)，且函知櫃買中心公告本公司贖回權之行使，並於債券收回基準日後五個營業日內按債券面額以現金收回其全部債券。 (二)、債券收回期間：自115年10月13日起至115年11月11日止 證券商受理期間：自115年10月12日起至115年11月10日止 (三)、債券收回基準日：115年11月11日 (四)、債券終止櫃檯買賣日：115年11月12日 (五)、每張債券收回價格：新台幣100,000元 (六)、收回價款發放日：115年11月18日採匯款或郵寄支票方式交付予債券持有人，匯費(郵資)自收回價款中直接扣除。 (七)、收回手續： 債券持有人請攜帶1.證券存摺 2.集保帳戶印鑑，至往來券商填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』（註明贖回）辦理債券收回手續；證券商於收件後會向台灣集中保管結算所提出申請，台灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生效力。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月13日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 6209 | 今國光 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_strong_inflow | stale_signal | 內容：依今國光三發行及轉換辦法第十七條規定辦理。 發行公司於115年10月13日至115年11月11日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、本公司國內第三次有擔保轉換公司債發行及轉換辦法第十七條(一)規定，本轉換公司債發行滿三個月翌日(115年1月24日)起至到期日前四十日(117年9月13 日)止，若本公司普通股之收盤價格連續三十個營業日超過當時轉換價格達百分之三十者，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之投資人，則以公告方式為之)，且函知櫃買中心公告本公司贖回權之行使，並於債券收回基準日後五個營業日內按債券面額以現金收回其全部債券。 (二)、債券收回期間：自115年10月13日起至115年11月11日止 證券商受理期間：自115年10月12日起至115年11月10日止 (三)、債券收回基準日：115年11月11日 (四)、債券終止櫃檯買賣日：115年11月12日 (五)、每張債券收回價格：新台幣100,000元 (六)、收回價款發放日：115年11月18日採匯款或郵寄支票方式交付予債券持有人，匯費(郵資)自收回價款中直接扣除。 (七)、收回手續： 債券持有人請攜帶1.證券存摺 2.集保帳戶印鑑，至往來券商填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』（註明贖回）辦理債券收回手續；證券商於收件後會向台灣集中保管結算所提出申請，台灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生效力。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月13日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 6209 | 今國光 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 23 | D_降級_TDCC轉弱 |  |  | call_strong_inflow | stale_signal | 內容：依今國光三發行及轉換辦法第十七條規定辦理。 發行公司於115年10月13日至115年11月11日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、本公司國內第三次有擔保轉換公司債發行及轉換辦法第十七條(一)規定，本轉換公司債發行滿三個月翌日(115年1月24日)起至到期日前四十日(117年9月13 日)止，若本公司普通股之收盤價格連續三十個營業日超過當時轉換價格達百分之三十者，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之投資人，則以公告方式為之)，且函知櫃買中心公告本公司贖回權之行使，並於債券收回基準日後五個營業日內按債券面額以現金收回其全部債券。 (二)、債券收回期間：自115年10月13日起至115年11月11日止 證券商受理期間：自115年10月12日起至115年11月10日止 (三)、債券收回基準日：115年11月11日 (四)、債券終止櫃檯買賣日：115年11月12日 (五)、每張債券收回價格：新台幣100,000元 (六)、收回價款發放日：115年11月18日採匯款或郵寄支票方式交付予債券持有人，匯費(郵資)自收回價款中直接扣除。 (七)、收回手續： 債券持有人請攜帶1.證券存摺 2.集保帳戶印鑑，至往來券商填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』（註明贖回）辦理債券收回手續；證券商於收件後會向台灣集中保管結算所提出申請，台灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生效力。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月13日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6209 | 今國光 | 27 | 14 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6209 | 今國光 | 85 | 0 | 4540000.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
