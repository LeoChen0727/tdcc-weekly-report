# INDIVIDUAL STOCK CHATGPT PACKET - 3702 大聯大

## Metadata
- generated_at: 2026-06-30 22:27:18 Asia/Taipei
- stock_id: 3702
- stock_name: 大聯大
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 294
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3702.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3702.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3702.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3702.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3702_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3702_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3702_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
- decision_score_high
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
- date: 20260630
- open: 105.5
- high: 108.5
- low: 105
- close: 107
- volume: 16810000
- ma5: 106.3
- ema23_primary: 109.31
- distance_to_ema23_pct: -2.11
- ma20: 109.83
- ma60: 107.03
- ma120: 88.8
- return_5d: -0.93
- return_20d: -9.7
- volume_ratio: 1.23
- distance_to_ma20_pct_auxiliary: -2.57
- distance_to_high_60_pct: -16.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,118.5,119.5,115.5,119,15652534,113.51,4.83,115.1,99.35,1.04
20260603,120,120,116.5,118,15454822,113.89,3.61,115.8,100.12,0.99
20260604,119,119.5,115,116.5,16158984,114.1,2.1,116.45,100.89,1
20260605,116.5,116.5,113,114.5,16516439,114.14,0.32,116.5,101.6,1.05
20260608,108,109.5,105.5,108,27570429,113.63,-4.95,116.2,102.19,1.8
20260609,109.5,112.5,107.5,110.5,14917517,113.37,-2.53,116.03,102.8,0.97
20260610,110,113.5,109,109,12426606,113,-3.54,115.95,103.38,0.82
20260611,111,111.5,105.5,108.5,18045469,112.63,-3.66,115.83,103.82,1.18
20260612,111.5,111.5,104,105,20657601,111.99,-6.24,115.58,104.07,1.3
20260615,107,108.5,103.5,107.5,12127021,111.62,-3.69,115.42,104.31,0.76
20260616,109,109.5,106.5,109,10028040,111.4,-2.15,115.45,104.58,0.63
20260617,107,107.5,104.5,107,10172545,111.03,-3.63,114.85,104.84,0.65
20260618,107.5,113,106.5,112,20036329,111.11,0.8,114.28,105.19,1.38
20260622,113.5,114,110.5,112.5,8555913,111.23,1.14,114,105.56,0.61
20260623,112.5,113,108,108,6484321,110.96,-2.67,113.22,105.76,0.47
20260624,107,108,105.5,106.5,3749385,110.59,-3.7,112.47,105.95,0.28
20260625,107,109.5,106,107,10429116,110.29,-2.98,111.8,106.2,0.77
20260626,106,109,105,106.5,9602233,109.97,-3.16,111.05,106.47,0.71
20260629,108,108,103.5,104.5,7796543,109.52,-4.58,110.4,106.74,0.59
20260630,105.5,108.5,105,107,16810000,109.31,-2.11,109.83,107.03,1.23
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 84.2
- over_600_ratio: 82.2
- over_800_ratio: 80.34
- over_1000_ratio: 79.22
- over_400_change_1w: -0.17
- over_800_change_1w: -0.16
- over_1000_change_1w: -0.35
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.31,,82,,80.66,,0,False,False
20260508,85.45,0.14,82.15,0.15,80.98,0.32,1,True,True
20260515,85.47,0.02,82,-0.15,80.83,-0.15,2,False,False
20260522,85.52,0.05,81.86,-0.14,80.8,-0.03,3,False,False
20260529,85.24,-0.28,81.85,-0.01,80.63,-0.17,0,False,False
20260605,84.99,-0.25,81.56,-0.29,80.31,-0.32,0,False,False
20260612,84.76,-0.23,81.28,-0.28,80.14,-0.17,0,False,False
20260618,84.37,-0.39,80.5,-0.78,79.57,-0.57,0,False,False
20260626,84.2,-0.17,80.34,-0.16,79.22,-0.35,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 3702 | 大聯大 | pullback_rebound | 回檔後短線轉強 | 82.0 |  |  |  |  | no_signal | stale_signal | 內容：依大聯大E1發行及交換辦法第十七條規定辦理。 發行公司於115年07月10日至115年08月08日行使債券贖回權，贖回權價格為債券面額之100.0000% 一、依據本公司國內第一次無擔保交換公司債(以下簡稱：本交換公司債)發行及交換辦法第17條第(一)項規定:本交換公司債於發行屆滿三個月之翌日(民國115年4月15日)起至發行期間屆滿前四十日(民國117年12月5日)止，若文曄普通股收盤價連續三十個營業日超過當時交換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司寄發之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為本交換公司債之停止交換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本交換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本交換公司債之面額新台幣壹拾萬元整，以現金收回其全部債券，並函請櫃買中心公告。本公司執行收回請求，應於債券收回基準日後七個營業日內，按債券面額以現金發放贖回價款。 二、本轉換公司債收回相關事宜如下： (一)掛號寄發債券收回通知書日期：115年7月10日 (二)通知及受理交換公司債收回期間：115年7月10日至115年8月8日 (三)交換公司債收回基準日：115年8月8日 (四)交換公司債終止櫃檯買賣日期：115年8月10日 (五)收回價款發放日：115年8月18日 三、收回手續： (一)本交換債為無實體發行，債券持有人請攜帶(1)證券存摺、(2)集保帳戶印鑑，至原交易證券商提具『轉(交)換公司債帳簿劃撥轉(交)換/贖回/賣回申請書』（127表單，並註明『贖回』）辦理債券收回手續。交易證券商收件後，將向臺灣集中保管結算所提出申請；臺灣集中保管結算所接受申請後送交本公司股務代理機構，於送達時即發生收回效力，且不得申請撤銷。 (二)債權人得自債券收回之前一營業日至屆滿之前一營業日止(即自民國115年7月9日起至民國115年8月7日止)，由債券持有人向往來券商辦理贖回手續。 (三)若債券持有人於「債券收回通知書」所載債券收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效&#63882;，採郵寄者以郵戳日為憑)者，本公司於債券收回基準日後七個營業日(115年8月18日)以匯款方式給付至債權人留存於交易證券商之款項劃撥帳號，匯費自贖回價金中直接扣除。如因帳號錯誤(或不完全)致金融機構退匯者，將改以郵寄支票至股東登記之通訊地址，相關郵資將由贖回價金中逕予扣除。 (四)如債券持有人不欲公司行使贖回權，擬請求將本交換公司債交換為文曄普通股，最遲應於115年8月11日前至往來證券商辦理交換手續。 四、本公司股務代理機構：群益金鼎證券股份有限公司股務代理部 地址：台北市大安區敦化南路二段97號地下二樓 電話：（02）2702-3999 警語：請投資人注意，具有請求交換資格者，如未於115年8月11日前以書面請求交換，本公司將按面額計算以現金收回其全部債券。；calendar event: shareholder_meeting on 20260630; status=confirmed; proximity=within_3d |
| 20260630 | 3702 | 大聯大 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  | no_signal | stale_signal | 內容：依大聯大E1發行及交換辦法第十七條規定辦理。 發行公司於115年07月10日至115年08月08日行使債券贖回權，贖回權價格為債券面額之100.0000% 一、依據本公司國內第一次無擔保交換公司債(以下簡稱：本交換公司債)發行及交換辦法第17條第(一)項規定:本交換公司債於發行屆滿三個月之翌日(民國115年4月15日)起至發行期間屆滿前四十日(民國117年12月5日)止，若文曄普通股收盤價連續三十個營業日超過當時交換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司寄發之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為本交換公司債之停止交換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本交換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本交換公司債之面額新台幣壹拾萬元整，以現金收回其全部債券，並函請櫃買中心公告。本公司執行收回請求，應於債券收回基準日後七個營業日內，按債券面額以現金發放贖回價款。 二、本轉換公司債收回相關事宜如下： (一)掛號寄發債券收回通知書日期：115年7月10日 (二)通知及受理交換公司債收回期間：115年7月10日至115年8月8日 (三)交換公司債收回基準日：115年8月8日 (四)交換公司債終止櫃檯買賣日期：115年8月10日 (五)收回價款發放日：115年8月18日 三、收回手續： (一)本交換債為無實體發行，債券持有人請攜帶(1)證券存摺、(2)集保帳戶印鑑，至原交易證券商提具『轉(交)換公司債帳簿劃撥轉(交)換/贖回/賣回申請書』（127表單，並註明『贖回』）辦理債券收回手續。交易證券商收件後，將向臺灣集中保管結算所提出申請；臺灣集中保管結算所接受申請後送交本公司股務代理機構，於送達時即發生收回效力，且不得申請撤銷。 (二)債權人得自債券收回之前一營業日至屆滿之前一營業日止(即自民國115年7月9日起至民國115年8月7日止)，由債券持有人向往來券商辦理贖回手續。 (三)若債券持有人於「債券收回通知書」所載債券收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效&#63882;，採郵寄者以郵戳日為憑)者，本公司於債券收回基準日後七個營業日(115年8月18日)以匯款方式給付至債權人留存於交易證券商之款項劃撥帳號，匯費自贖回價金中直接扣除。如因帳號錯誤(或不完全)致金融機構退匯者，將改以郵寄支票至股東登記之通訊地址，相關郵資將由贖回價金中逕予扣除。 (四)如債券持有人不欲公司行使贖回權，擬請求將本交換公司債交換為文曄普通股，最遲應於115年8月11日前至往來證券商辦理交換手續。 四、本公司股務代理機構：群益金鼎證券股份有限公司股務代理部 地址：台北市大安區敦化南路二段97號地下二樓 電話：（02）2702-3999 警語：請投資人注意，具有請求交換資格者，如未於115年8月11日前以書面請求交換，本公司將按面額計算以現金收回其全部債券。；calendar event: shareholder_meeting on 20260630; status=confirmed; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 3702 | 大聯大 | 20 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 3702 | 大聯大 | 29 | 0 | 1808170.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
