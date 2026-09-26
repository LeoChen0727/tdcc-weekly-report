# INDIVIDUAL STOCK CHATGPT PACKET - 1560 中砂

## Metadata
- generated_at: 2026-09-26 22:16:05 Asia/Taipei
- stock_id: 1560
- stock_name: 中砂
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1560_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1560_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1560.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1560.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1560.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1560.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1560_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1560_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1560_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_consolidation
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260924
- open: 950
- high: 975
- low: 945
- close: 971
- volume: 2172367
- ma5: 937.2
- ema23_primary: 802.56
- distance_to_ema23_pct: 20.99
- ma20: 783.1
- ma60: 721.07
- ma120: 675.1
- return_5d: 19.14
- return_20d: 40.72
- volume_ratio: 1.01
- distance_to_ma20_pct_auxiliary: 23.99
- distance_to_high_60_pct: -2.12

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,697,707,694,695,584981,690.14,0.7,693.7,692.43,0.48
20260831,685,687,663,683,943741,689.55,-0.95,694.3,691.88,0.81
20260901,681,748,681,744,2090731,694.09,7.19,697.75,692.65,1.72
20260902,739,739,702,704,1081855,694.91,1.31,698.95,693.57,0.89
20260903,705,727,702,711,1273917,696.25,2.12,699.85,694.33,1.04
20260904,728,731,683,695,1570777,696.15,-0.17,701.5,695.77,1.24
20260907,702,736,702,730,1767148,698.97,4.44,703.6,697.47,1.34
20260908,730,736,713,717,665337,700.47,2.36,705.1,698.55,0.51
20260909,717,733,717,730,995480,702.93,3.85,705.2,699,0.83
20260910,727,735,718,733,456150,705.44,3.91,706.5,699.9,0.4
20260911,747,794,744,790,4096116,712.49,10.88,709.75,701.62,3.26
20260914,775,776,740,753,2027263,715.86,5.19,710.3,702.5,1.63
20260915,746,752,735,735,702383,717.46,2.45,711.65,702.87,0.59
20260916,740,754,739,741,672723,719.42,3,713.35,703.47,0.58
20260917,750,815,750,815,3169755,727.38,12.05,719.2,704.57,2.5
20260918,855,896,813,896,6133920,741.43,20.85,730.05,707.33,4
20260921,903,916,861,914,5320084,755.82,20.93,741.75,710.85,3.01
20260922,935,960,929,950,3983118,772,23.06,755.4,714.38,2.06
20260923,955,992,947,955,3373372,787.25,21.31,769.05,717.6,1.62
20260924,950,975,945,971,2172367,802.56,20.99,783.1,721.07,1.01
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 65.98
- over_600_ratio: 60.06
- over_800_ratio: 56.1
- over_1000_ratio: 48.91
- over_400_change_1w: -0.04
- over_800_change_1w: 1.55
- over_1000_change_1w: -1.4
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,66.19,-0.28,54.42,-0.46,48.78,0.21,5,False,True
20260717,66.57,0.38,55.76,1.34,50.72,1.94,6,True,True
20260724,65.68,-0.89,54.33,-1.43,49.94,-0.78,0,False,False
20260731,65.25,-0.43,53.61,-0.72,48.06,-1.88,0,False,False
20260807,64.68,-0.57,54.38,0.77,49.51,1.45,1,False,True
20260814,65.21,0.53,55.1,0.72,49.64,0.13,2,True,True
20260821,64.49,-0.72,54.25,-0.85,49.38,-0.26,0,False,False
20260828,64.45,-0.04,53.57,-0.68,48.12,-1.26,0,False,False
20260904,64.54,0.09,53.71,0.14,48.87,0.75,1,True,True
20260911,64.69,0.15,53.39,-0.32,49.14,0.27,2,False,True
20260918,66.02,1.33,54.55,1.16,50.31,1.17,3,True,True
20260924,65.98,-0.04,56.1,1.55,48.91,-1.4,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1560 | 中砂 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 63.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 內容：依中砂一發行及轉換辦法第十八條規定辦理。 發行公司於115年08月04日至115年09月02日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、依中砂國內第一次無擔保轉換公司債發行及轉換辦法第十八條第一項規定，(一) 本轉換公司債發&#64008;滿三個月後翌日 (113年9月25日) 起至發&#64008;期間屆滿前四十日 (118年5月15日) 止，若本公司普通股收盤價&#63898;續三十個營業日超過當時轉換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本轉換公司債面額，以現&#63754;收回其全部債券，並函請櫃買中心公告。本公司執&#64008;收回請求，應於債券收回基準日後五個營業日內按債券面額以現&#63754;贖回其流通在外之本轉換公司債。 (二)、轉換公司債停止過戶期間：不適用。 (三)、通知及受理轉換公司債贖回期間：115年08月04日至115年09月02日 (四)、轉換公司債收回基準日：115年09月02日 (五)、轉換公司債終止櫃檯買賣日期:115年09月03日 (六)、掛號寄發債券收回通知書日期:115年08月04日 (七)、債券收回手續 1、若　台端已將所持有之「中砂一」申請轉換或出售，則本通知書自動無效。 2、本轉換公司債採無實體發行，請　台端自債券收回權行使開始日之前一個營業日(民國115年8月3日)起至屆滿日之前一個營業日(民國115年9月1日)止，向原交易券商申請辦理收回手續，無須將債券領回。 3、請　台端檢附：(1)轉換公司債帳簿劃撥轉換/贖回/賣回申請書（表格請至各券商索取），並加蓋證券集保帳戶原留印鑑章(2)證券存摺，至原交易券商辦理債券收回手續。由往&#63789;券商向臺灣集中保管結算所股份有限公司（以下稱集保結算所）提出申請，集保公司於接受申請後送交本公司股務代&#63972;機構，於送達時即生效&#63882;，且&#63847;得申請撤回。  (八)、本次收回公司債還本金額統一於115年9月9日以匯款或掛號方式郵寄支票支付各債券持有人，匯費(郵資)自收回價金中直接扣除。  (九)、公司股務代理機構（包括地址及電話）: 凱基證券股份有限公司股務代&#63972;部，地址：100900台北市重慶南路一段2號5樓，電話：02-23892999。 警語：請投資人注意，具有請求轉換資格者，如未於115年 09月04日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1560 | 中砂 | 6 | 2 | 5 | 6 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1560 | 中砂 | 140 | 12 | 12224470.0 | 218910.0 | 55.84 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
