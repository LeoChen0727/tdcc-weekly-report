# INDIVIDUAL STOCK CHATGPT PACKET - 6672 騰輝電子-KY

## Metadata
- generated_at: 2026-08-21 22:28:05 Asia/Taipei
- stock_id: 6672
- stock_name: 騰輝電子-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6672_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6672_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6672_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6672_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6672_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6672_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6672_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6672.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6672.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6672.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6672.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6672_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6672_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6672_latest.md?ref=main

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
- date: 20260821
- open: 285
- high: 292
- low: 264
- close: 267.5
- volume: 6973935
- ma5: 282
- ema23_primary: 255.63
- distance_to_ema23_pct: 4.64
- ma20: 240.95
- ma60: 248
- ma120: 202.85
- return_5d: -0.93
- return_20d: 19.15
- volume_ratio: 1.57
- distance_to_ma20_pct_auxiliary: 11.02
- distance_to_high_60_pct: -18.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,225.5,228,217,221,1749271,251.15,-12.01,268.6,235.43,0.39
20260728,213,213,199,199.5,2262010,246.85,-19.18,264.5,235.1,0.53
20260729,204,204,180,185.5,3222466,241.74,-23.26,258.77,234.47,0.77
20260730,179.5,193,178,181,2854432,236.68,-23.52,253.3,233.82,0.77
20260731,195,199,191,198,2172683,233.45,-15.19,248.32,233.54,0.61
20260803,198,215,196.5,211.5,2828867,231.62,-8.69,243.15,233.3,0.83
20260804,211,221,210.5,218.5,2044862,230.53,-5.22,238.68,233.47,0.62
20260805,227,228,221.5,221.5,2656170,229.78,-3.6,234.75,233.68,0.87
20260806,220.5,233,216,232.5,3201994,230,1.09,231.07,234.12,1.08
20260807,232.5,233.5,225,229,2541547,229.92,-0.4,227.62,234.64,0.86
20260810,251.5,251.5,243,251.5,6389874,231.72,8.54,226.45,235.58,2.07
20260811,251.5,262,247,257,6965524,233.83,9.91,226.22,236.84,2.14
20260812,252.5,270,252,268,5359256,236.67,13.24,226.22,238.3,1.57
20260813,269.5,272.5,260,264.5,4550996,238.99,10.67,226.07,239.72,1.28
20260814,264.5,284.5,258.5,270,6294536,241.58,11.77,227.53,241.28,1.7
20260817,271,288,266,283,5150608,245.03,15.5,230.6,243.03,1.37
20260818,283,295,277.5,288,8355505,248.61,15.84,233.53,244.61,2.1
20260819,280,293,280,284,7856786,251.56,12.9,235.97,245.84,1.89
20260820,289,292,280,287.5,5170899,254.55,12.94,238.8,247.07,1.21
20260821,285,292,264,267.5,6973935,255.63,4.64,240.95,248,1.57
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 28.88
- over_600_ratio: 25.66
- over_800_ratio: 20.63
- over_1000_ratio: 17.49
- over_400_change_1w: -0.15
- over_800_change_1w: 1.48
- over_1000_change_1w: 1.79
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,26.33,-5.15,17.32,-2.16,17.32,1.17,1,False,True
20260605,24.26,-2.07,17.41,0.09,17.41,0.09,2,False,True
20260612,26.33,2.07,18.49,1.08,17.38,-0.03,3,False,True
20260618,28.49,2.16,19.73,1.24,16.2,-1.18,4,False,True
20260626,35.79,7.3,27.74,8.01,25.48,9.28,5,True,True
20260703,35.25,-0.54,23.54,-4.2,21.21,-4.27,0,False,False
20260709,34.04,-1.21,22.96,-0.58,20.63,-0.58,0,False,False
20260717,33.83,-0.21,23,0.04,20.67,0.04,1,False,True
20260724,30.46,-3.37,19.85,-3.15,18.7,-1.97,0,False,False
20260731,29.37,-1.09,18.59,-1.26,17.44,-1.26,0,False,False
20260807,29.03,-0.34,19.15,0.56,15.7,-1.74,1,False,True
20260814,28.88,-0.15,20.63,1.48,17.49,1.79,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6672 | 騰輝電子-KY | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | call_put_bullish | repeated_but_no_breakout | 內容：依騰輝電子二KY發行及轉換辦法第十八條規定辦理。 發行公司於115年08月03日至115年09月01日行使債券贖回權，贖回權價格為債券面額之100.0000% 一、依據本公司中華民國境內第二次無擔保轉換公司債(以下簡稱：本轉換債)發行及轉換辦法第 18 條第一項規定: 本轉換公司債發&#64008;滿三個月後翌日起(民國115年5月4日)至發&#64008;期間屆滿前四十日止(民國119年12月25日)，本公司普通股收盤價&#63898;續三十個營業日(115年5月29日~115年7月13日)超過當時轉換價格(90.50元)達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日(115年7月27 日)債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現&#63754;收回其全部債券，並函請櫃檯買賣中心公告。本公司執&#64008;收回請求，應於債券收回基準日後七個營業日內按債券面額以現&#63754;贖回其流通在外之本轉換公司債。 二、茲訂定本轉換債收回相關事宜如下：通知及受理轉換公司債收回期間：115年8月3日至115年9月1日(透過證券商申請收回者，配合集保公司作業115年8月31日為最後申請日)，逾期恕不受理。 三、轉換公司債收回基準日：115年9月1日 四、轉換公司債終止櫃檯買賣日期：115年9月2日 五、掛號寄發債券收回通知書日期：115年8月3日 六、若債券持有人於「債券收回通知書」所載債券收回基準日前，未至原交易券商辦理債券贖回手續者，本公司將按「債券面額」以現金收回流通在外之本轉換債。 七、每張債券收回價格：新台幣壹拾萬元整。 八、收回價款發放日：115 年 9 月10日(扣除處理費)以匯款或掛號方式郵寄禁止背書轉讓支票。 九、贖回權相關稅賦：因本次贖回權以債券面額收回，票面&#63965;&#63841;為0%，無債息相關稅賦之問題。 十、本公司執行收回請求，債券持有人請求轉換之最後期限為本轉換公司債終止櫃檯買賣日後第二個營業日(應於 115 年 9 月 3日前向往來券商提出申請)，未於前述期限前以書面向往來券商請求轉換者，本公司將按「債券面額」以現金收回其全部債券。 十一、本轉換債收回手續：因本轉換債為無實體發行，債券持有人請攜帶：1.證券存摺。 2.填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』127表單（註明贖回），並加蓋集保帳戶印鑑。3.身分證正反面影本，至原交易證券商辦理債券收回手續即可；交易證券商於收件後會向台灣集中保管結算所提出申請，台灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生收回之效力，且不得申請撤銷。 十二、本公司股務代理機構：元大證券股份有限公司股務代理部 地址：106       臺北市大安區敦化南路2段67號地下一樓 電話：（02）2586&#8208;5859 警語：請投資人注意，具有請求轉換資格者，如未於115年9月3日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 6672 | 騰輝電子-KY | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_put_bullish | repeated_but_no_breakout | 內容：依騰輝電子二KY發行及轉換辦法第十八條規定辦理。 發行公司於115年08月03日至115年09月01日行使債券贖回權，贖回權價格為債券面額之100.0000% 一、依據本公司中華民國境內第二次無擔保轉換公司債(以下簡稱：本轉換債)發行及轉換辦法第 18 條第一項規定: 本轉換公司債發&#64008;滿三個月後翌日起(民國115年5月4日)至發&#64008;期間屆滿前四十日止(民國119年12月25日)，本公司普通股收盤價&#63898;續三十個營業日(115年5月29日~115年7月13日)超過當時轉換價格(90.50元)達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日(115年7月27 日)債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現&#63754;收回其全部債券，並函請櫃檯買賣中心公告。本公司執&#64008;收回請求，應於債券收回基準日後七個營業日內按債券面額以現&#63754;贖回其流通在外之本轉換公司債。 二、茲訂定本轉換債收回相關事宜如下：通知及受理轉換公司債收回期間：115年8月3日至115年9月1日(透過證券商申請收回者，配合集保公司作業115年8月31日為最後申請日)，逾期恕不受理。 三、轉換公司債收回基準日：115年9月1日 四、轉換公司債終止櫃檯買賣日期：115年9月2日 五、掛號寄發債券收回通知書日期：115年8月3日 六、若債券持有人於「債券收回通知書」所載債券收回基準日前，未至原交易券商辦理債券贖回手續者，本公司將按「債券面額」以現金收回流通在外之本轉換債。 七、每張債券收回價格：新台幣壹拾萬元整。 八、收回價款發放日：115 年 9 月10日(扣除處理費)以匯款或掛號方式郵寄禁止背書轉讓支票。 九、贖回權相關稅賦：因本次贖回權以債券面額收回，票面&#63965;&#63841;為0%，無債息相關稅賦之問題。 十、本公司執行收回請求，債券持有人請求轉換之最後期限為本轉換公司債終止櫃檯買賣日後第二個營業日(應於 115 年 9 月 3日前向往來券商提出申請)，未於前述期限前以書面向往來券商請求轉換者，本公司將按「債券面額」以現金收回其全部債券。 十一、本轉換債收回手續：因本轉換債為無實體發行，債券持有人請攜帶：1.證券存摺。 2.填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』127表單（註明贖回），並加蓋集保帳戶印鑑。3.身分證正反面影本，至原交易證券商辦理債券收回手續即可；交易證券商於收件後會向台灣集中保管結算所提出申請，台灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生收回之效力，且不得申請撤銷。 十二、本公司股務代理機構：元大證券股份有限公司股務代理部 地址：106       臺北市大安區敦化南路2段67號地下一樓 電話：（02）2586&#8208;5859 警語：請投資人注意，具有請求轉換資格者，如未於115年9月3日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6672 | 騰輝電子-KY | 1 | 1 | 4 | 9 | 11 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 11 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6672 | 騰輝電子-KY | 68 | 1 | 18666390.0 | 38210.0 | 488.52 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
