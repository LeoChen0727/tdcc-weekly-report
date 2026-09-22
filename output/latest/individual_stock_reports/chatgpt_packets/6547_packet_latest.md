# INDIVIDUAL STOCK CHATGPT PACKET - 6547 高端疫苗

## Metadata
- generated_at: 2026-09-20 22:17:59 Asia/Taipei
- stock_id: 6547
- stock_name: 高端疫苗
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6547_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6547_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6547_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6547_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6547_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6547_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6547_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6547.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6547.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6547.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6547.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6547_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6547_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6547_latest.md?ref=main

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
- date: 20260918
- open: 60.5
- high: 61
- low: 58.5
- close: 59.7
- volume: 4709000
- ma5: 59.74
- ema23_primary: 59.27
- distance_to_ema23_pct: 0.73
- ma20: 61.31
- ma60: 52.63
- ma120: 50.89
- return_5d: 1.53
- return_20d: 7.18
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: -2.63
- distance_to_high_60_pct: -17.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,55.5,57.5,55.1,55.5,5174000,50.77,9.31,50.35,47.77,1.47
20260825,55.5,56.7,54.9,56.3,4032000,51.23,9.89,50.84,47.96,1.12
20260826,59.1,61.9,59.1,61.9,10171000,52.12,18.76,51.65,48.22,2.54
20260827,61.9,66.7,60.5,63.1,22608000,53.04,18.97,52.53,48.52,4.47
20260828,64.7,67.9,64.2,65,11885000,54.03,20.3,53.49,48.85,2.13
20260831,65,65.9,62.8,63.9,6832000,54.86,16.49,54.34,49.08,1.17
20260901,63.9,63.9,60.6,61.3,7875000,55.39,10.66,55.03,49.29,1.28
20260902,61.7,62.3,60.7,61.5,3293000,55.9,10.01,55.51,49.51,0.55
20260903,61.9,62.7,61.3,61.8,2906000,56.39,9.59,56.15,49.75,0.52
20260904,61.9,63.4,61.2,61.5,3208000,56.82,8.24,56.65,49.99,0.58
20260907,62,63.9,61.2,63.4,3575000,57.37,10.52,57.22,50.29,0.65
20260908,63.4,64.7,62.5,64,3048000,57.92,10.5,57.82,50.59,0.55
20260909,64.1,68.3,63.6,68.1,6563000,58.77,15.88,58.7,50.96,1.13
20260910,71,72.2,61.3,61.4,19245000,58.99,4.09,59.16,51.23,2.92
20260911,61.6,62.4,58.7,58.8,7604000,58.97,-0.29,59.52,51.45,1.11
20260914,58.4,59.3,56.5,58.1,5796000,58.9,-1.36,59.91,51.66,0.82
20260915,58.7,60.7,58,59.7,2531000,58.97,1.24,60.28,51.91,0.36
20260916,59.7,60.8,59.1,60.5,2486000,59.09,2.38,60.72,52.16,0.36
20260917,60.9,61.7,60.3,60.7,2311000,59.23,2.49,61.11,52.4,0.34
20260918,60.5,61,58.5,59.7,4709000,59.27,0.73,61.31,52.63,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 35.8
- over_600_ratio: 32.19
- over_800_ratio: 30
- over_1000_ratio: 28.74
- over_400_change_1w: 0.24
- over_800_change_1w: 1.03
- over_1000_change_1w: 0.84
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,35.24,0.05,29.36,0.13,28.28,-0.12,2,False,True
20260709,35.48,0.24,29.99,0.63,28.33,0.05,3,True,True
20260717,35.43,-0.05,29.95,-0.04,28.33,0,0,False,False
20260724,35.01,-0.42,29.42,-0.53,28.03,-0.3,0,False,False
20260731,34.8,-0.21,29.12,-0.3,28.3,0.27,1,False,True
20260807,34.63,-0.17,29.36,0.24,28.05,-0.25,2,False,True
20260814,35.76,1.13,29.74,0.38,28.7,0.65,3,True,True
20260821,35.69,-0.07,29.77,0.03,28.14,-0.56,4,False,True
20260828,36.61,0.92,30.48,0.71,29.42,1.28,5,True,True
20260904,36.35,-0.26,30.54,0.06,29.25,-0.17,6,False,True
20260911,35.56,-0.79,28.97,-1.57,27.9,-1.35,0,False,False
20260918,35.8,0.24,30,1.03,28.74,0.84,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6547 | 高端疫苗 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | stale_signal | 內容：依高端疫苗二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月08日至115年11月06日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)依本公司「國內第二次有擔保轉換公司債發行及轉換辦法」第十八條第一項規定，該轉換公司債發行滿三個月後翌日起(民國115年6月20日)至發&#64008;期間屆滿前四十日止(民國118年2月7日)，本公司普通股收盤價連續三十個營業日超過當時轉換價格百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本轉換公司債之面額，以現&#63754;收回其全部債券，並函請櫃檯買賣中心公告。本公司執&#64008;收回請求，應於債券收回基準日後七個營業日內以現&#63754;贖回本轉換公司債。 (二)通知及受理轉換公司債收回期間：115年10月8日至115年11月6日。 (三)掛號寄發債券收回通知書日期：115年10月8日。 (四)轉換公司債收回基準日：115年11月6日。 (五)轉換公司債終止櫃檯買賣日期：115年11月9日。 (六)收回價款發放日：115年11月17日。 (七)每張債券收回價款：新台幣壹拾萬元整。 (八)債券收回手續 1.因本轉換公司債為無實體發行，債券持有人請攜帶1.證券存摺2.集保帳戶印鑑，至原交易證券商填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』127表單（註明贖回）辦理債券收回手續即可；交易證券商於收件後會向臺灣集中保管結算所提出申請，臺灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生收回之效力，且不得申請撤銷。 2.若債券持有人於「債券收回通知書」所載債權收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效力，採郵寄者已郵戳日為憑)者，本公司於債券收回基準日後七個營業日內(預計於115年11月17日)按債券面額以現&#63754;贖回。 3.債券持有人得自債券收回通知之始日(115年10月8日)起至屆滿日(115年11月6日)之前一營業日(115年11月5日)止，向往來券商辦理贖回手續。 4.如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年11月10日前至往來證券商辦理轉換手續。 (九)、本公司股務代理機構： 永豐金證券股份有限公司股務代理部 地址：100台北市博愛路17號3樓 電話:02-2381-6288 警語：請投資人注意，具有請求轉換資格者，如未於115年11月10日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6547 | 高端疫苗 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 內容：依高端疫苗二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月08日至115年11月06日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)依本公司「國內第二次有擔保轉換公司債發行及轉換辦法」第十八條第一項規定，該轉換公司債發行滿三個月後翌日起(民國115年6月20日)至發&#64008;期間屆滿前四十日止(民國118年2月7日)，本公司普通股收盤價連續三十個營業日超過當時轉換價格百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本轉換公司債之面額，以現&#63754;收回其全部債券，並函請櫃檯買賣中心公告。本公司執&#64008;收回請求，應於債券收回基準日後七個營業日內以現&#63754;贖回本轉換公司債。 (二)通知及受理轉換公司債收回期間：115年10月8日至115年11月6日。 (三)掛號寄發債券收回通知書日期：115年10月8日。 (四)轉換公司債收回基準日：115年11月6日。 (五)轉換公司債終止櫃檯買賣日期：115年11月9日。 (六)收回價款發放日：115年11月17日。 (七)每張債券收回價款：新台幣壹拾萬元整。 (八)債券收回手續 1.因本轉換公司債為無實體發行，債券持有人請攜帶1.證券存摺2.集保帳戶印鑑，至原交易證券商填具『轉換公司債帳簿劃撥轉換/贖回/賣回申請書』127表單（註明贖回）辦理債券收回手續即可；交易證券商於收件後會向臺灣集中保管結算所提出申請，臺灣集中保管結算所於接受申請後送交本公司股務代理機構，於送達時即生收回之效力，且不得申請撤銷。 2.若債券持有人於「債券收回通知書」所載債權收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效力，採郵寄者已郵戳日為憑)者，本公司於債券收回基準日後七個營業日內(預計於115年11月17日)按債券面額以現&#63754;贖回。 3.債券持有人得自債券收回通知之始日(115年10月8日)起至屆滿日(115年11月6日)之前一營業日(115年11月5日)止，向往來券商辦理贖回手續。 4.如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年11月10日前至往來證券商辦理轉換手續。 (九)、本公司股務代理機構： 永豐金證券股份有限公司股務代理部 地址：100台北市博愛路17號3樓 電話:02-2381-6288 警語：請投資人注意，具有請求轉換資格者，如未於115年11月10日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6547 | 高端疫苗 | 5 | 5 | 5 | 7 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
