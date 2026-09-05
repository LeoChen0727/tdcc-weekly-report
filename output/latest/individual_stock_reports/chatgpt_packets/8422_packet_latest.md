# INDIVIDUAL STOCK CHATGPT PACKET - 8422 可寧衛*

## Metadata
- generated_at: 2026-09-05 15:54:50 Asia/Taipei
- stock_id: 8422
- stock_name: 可寧衛*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 341
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8422_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8422_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8422.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8422.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8422.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8422.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8422_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8422_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8422_latest.md?ref=main

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
- date: 20260904
- open: 26.2
- high: 26.35
- low: 26
- close: 26.1
- volume: 2983275
- ma5: 26.49
- ema23_primary: 26.65
- distance_to_ema23_pct: -2.05
- ma20: 26.78
- ma60: 26.95
- ma120: 27.68
- return_5d: -3.69
- return_20d: -0.76
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: -2.54
- distance_to_high_60_pct: -14.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,26.3,26.85,26.2,26.8,6104188,26.27,2,25.93,27.11,0.87
20260811,26.8,26.95,26.55,26.65,3484684,26.31,1.31,25.96,27.11,0.53
20260812,26.85,27.15,26.6,26.9,4903645,26.35,2.07,25.98,27.14,0.74
20260813,27.1,27.2,26.4,26.45,3505123,26.36,0.33,25.96,27.15,0.53
20260814,26.4,26.5,26.2,26.4,2899071,26.37,0.13,25.98,27.16,0.46
20260817,26.3,26.5,26.15,26.45,2577106,26.37,0.29,26.02,27.16,0.42
20260818,26.55,27.15,26.4,27.1,9577639,26.43,2.52,26.05,27.17,1.52
20260819,27.2,27.25,26.7,26.7,4460715,26.46,0.92,26.09,27.16,0.71
20260820,27,27.2,26.5,27.1,6360439,26.51,2.23,26.13,27.15,1
20260821,27,27.4,26.7,26.85,5906218,26.54,1.18,26.17,27.15,0.91
20260824,27,27.4,26.9,27.2,5444895,26.59,2.28,26.25,27.16,0.85
20260825,27.2,27.3,26.85,27.2,3543910,26.64,2.09,26.36,27.16,0.58
20260826,27.2,27.5,27.15,27.25,3728937,26.69,2.08,26.48,27.15,0.66
20260827,27.35,27.6,26.9,27,4251584,26.72,1.05,26.61,27.15,0.76
20260828,27.05,27.35,27,27.1,4376283,26.75,1.3,26.73,27.13,0.85
20260831,27,27.35,26.8,26.8,7483477,26.76,0.17,26.73,27.11,1.51
20260901,26.8,27,26.75,26.75,3772736,26.75,-0.02,26.76,27.08,0.78
20260902,26.75,26.95,26.6,26.65,2432371,26.75,-0.36,26.79,27.08,0.51
20260903,26.7,26.85,26.15,26.15,3790114,26.7,-2.05,26.79,27.02,0.8
20260904,26.2,26.35,26,26.1,2983275,26.65,-2.05,26.78,26.95,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 38.35
- over_600_ratio: 36.93
- over_800_ratio: 35.51
- over_1000_ratio: 34.55
- over_400_change_1w: 0.19
- over_800_change_1w: 0.12
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,38.08,-0.33,35.34,-0.36,34.72,-0.18,0,False,False
20260626,37.64,-0.44,34.86,-0.48,34.18,-0.54,0,False,False
20260703,37.35,-0.29,34.72,-0.14,33.7,-0.48,0,False,False
20260709,37.44,0.09,34.89,0.17,34.07,0.37,1,True,True
20260717,36.9,-0.54,34.34,-0.55,33.58,-0.49,0,False,False
20260724,37.02,0.12,34.34,0,33.59,0.01,1,False,True
20260731,36.92,-0.1,34.06,-0.28,33.36,-0.23,0,False,False
20260807,37.27,0.35,34.39,0.33,33.77,0.41,1,True,True
20260814,37.71,0.44,34.71,0.32,34.09,0.32,2,True,True
20260821,38.01,0.3,35.04,0.33,34.28,0.19,3,True,True
20260828,38.16,0.15,35.39,0.35,34.63,0.35,4,True,True
20260904,38.35,0.19,35.51,0.12,34.55,-0.08,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 8422 | 可寧衛* | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議日期:115/08/26 2.發行期間:  本公司辦理股票公開發行前，視實際需要發行之，實際發行及認購基準日期授權由董事  長訂定之。 3.認股權人資格條件:  (一)本公司及本公司國內外控制或從屬公司之正式編制員工及兼職員工。  (二)實際得為認股權人之員工及其得認股之數量，將參酌職級、工作績效、年資、過去      及預期整體貢獻或特殊功績及其他等因素，由總經理擬定，呈董事長核定後辦理。 4.員工認股權憑證之發行單位總數:10,000單位 5.每單位認股權憑證得認購之股數:1,000股 6.因認股權行使而須發行之新股總數或依證券交易法第二十八條之二 規定須買回之股數:10,000,000股 7.認股價格:每股新台幣25元 8.認股權利期間:  (1)認股權憑證之存續期間為三年，屆滿後未行使之認股權視同放棄認股權利，認股權     人不得再行主張其認股權。該認股權憑證不得轉讓，但遇認股權人死亡其繼承者不     在此限。  (2)認股權憑證不得質押、贈予他人或作其他方式之處分。  (3)憑證授予期間與可行使比例如下所述：      認股權憑證授予期間         累積可行使認股比例      ------------------         ------------------          屆滿15個月                     50%          屆滿30個月                    100%  (4)認股權人自公司授予員工認股權憑證後，遇有違反勞動契約或工作規則等重大過失     者，公司有權就其尚未具行使權之認股權憑證予以收回並註銷。 9.認購股份之種類:本公司普通股股票。 10.員工離職或發生繼承時之處理方式:   (1)離職（含自願離職、資遣、開除）：      已具行使權之認股權憑證，得自離職日起於30日內行使認股權利；未具行使權之認      股權憑證，於離職當日即視為放棄認股權利。   (2)退休：      已具行使權之認股權憑證，於退休時，必須自退休日起30日內行使之，但仍以認股      權憑證存續期間為限。未行使認股的部份，於退休日起失效。   (3)留職停薪：      依政府法令規定及個人重大疾病、家庭重大變故、赴國外進修等原因經由公司特別      核准之留職停薪員工，已具行使權之認股權憑證，得自留職停薪起始日起30日內ㄧ      次行使完認股權利，逾期未行使則視同放棄其認股權利。      未具行使權利之認股權憑證得於復職後恢復權益，惟認股權行使時程應依留職停薪      期間往後遞延，但仍不得逾認股權憑證存續期間。   (4)一般死亡：      已具行使權之認股權憑證，由繼承人自死亡日起30日內行使認股權，未具行使權之      認股權憑證，於死亡當日即視為放棄認股權利。   (5)因受職業災害殘疾者：      (a)受職業災害致身體殘疾而無法繼續任職者         已具行使權之認股權憑證，認股權人需於離職日起30日內行使之，逾期未行使         即失效；未具行使權之認股權憑證，於認股權人離職當日即失效。      (b)因受職業災害或因公出差致死亡者         已具行使權之認股權憑證，於死亡時，繼承人可以行使全部之認股權利。惟該         認股權利，必須自死亡日起30日內行使之，但仍以認股權憑證存續期間為限，         未行使認股的部份，視同放棄。   (6)轉任集團關係企業：      若認股權人因個人因素請調至集團關係企業或其他公司時，其認股權憑證應比照離      職人員方式處理；認股權人係因公司業務需要，經本公司指派轉任關係企業或其他      公司時，其已授予認股權憑證之權利義務不受影響。   (7)認股權人或其繼承人若未能於上述期限內行使認股權者，即視為放棄認股權利。 11.其他認股條件:   放棄認股權利之認股權憑證，本公司將予註銷不再發行。 12.履約方式:以本公司發行新股方式交付。 13.認股價格之調整:   (一)本認股權憑證發行後，遇有本公司普通股股份發生變動時（即辦理現金增資、盈       餘轉增資、資本公積轉增資、公司合併、公司分割、股票分割及辦理現金增資參       與發行海外存託憑證等），認股價格依下列公式調整之（計算至新台幣角為止，       分以下四捨五入）；惟公司合併或公司分割時，認股價格不予調整。       除法令另有規定或需經主管機關核可外，對於登載於股東名薄之認股權股款繳納       憑證持有人，本公司將按認股價格調整之差異，加發認股權股款繳納憑證，實際       發行日期由董事長訂之。加發認股權股款繳納憑證時，若有不足壹股之股份金額       ，本公司以現金償付。   (二)調整後認股價格＝        調整前認股價格 × ｛〔已發行股數 + （每股繳款金額 × 新股發行股數）/ 調       整前認股價格〕/（已發行股數 + 新股發行股數）｝        (1)發行股數係指普通股已發行股份總數，不含已繳款之股款繳納憑證及債券換          股權利證書之股數。       (2)每股繳款金額如係屬無償配股或股票分割，則其繳款金額為零。       (3)遇有調整後認股價格高於調整前認股價格時，則不予調整。   (三)本認股權憑證發行後，遇有本公司發放普通股現金股利，每股發放金額占每股時       價之比率超過百分之ㄧ點五者，認股價格依下列公式調整之（調整後認股價格計       算至新台幣角為止，分以下四捨五入）：       調整後認股價格 ＝ 調整前認股價格 × （1－發放普通股現金股利/每股時價）   (四)本認股權憑證發行後，遇有非因庫藏股註銷之減資致普通股股份減少時，應依下       列公式計算調整後認股價格：       調整後認股價格=調整前認股價格 × （減資前已發行股份/減資後已發行股份） 14.行使認股權之程序:   (一)認股權人除依法暫停過戶期間外，得依發行及認股辦法第六條第二項所訂之時程       行使認股權利，並填具認股請求書，向本公司或股務代理機構提出申請，於送遞       時即生認股之效力，且不得申請撤銷。   (二)本公司或股務代理機構於受理認股之請求後，通知認股權人繳納股款至指定銀       行。   (三)本公司或股務代理機構於確認收足股款後，將其認購之股數登載於本公司股東名       簿，並於取得經濟部核准函後發給本公司新發行之普通股。   (四)本公司普通股若依法得於台灣證券交易所或櫃買中心買賣時，本公司新發行之普       通股自向認股權人交付之日起即得上市(櫃)買賣。   (五)本公司依發行及認股辦法發行新股交付予認股權人，將於每季結束後向公司登記       主管機關申請資本額變更登記及新股發行之申請；惟當年度若遇無償配股基準日       或現金增資認股除權基準日時，得調整變更登記時間。 15.認股後之權利義務:   本公司因認股權行使所發行之普通股，其權利義務與本公司已發行且流通在外之普通   股股票相同。 16.附有轉換、交換或認股者，其換股基準日:不適用 17.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 18.其他重要約定事項:   (一)本公司完成法定發行程序後，即由承辦部門通知認股權人簽署「員工認股權憑證       受領同意書」，經認股權人完成「員工認股權憑證受領同意書」簽署完成後，即       視為取得受領權利；未依規定完成簽署者，即視同放棄受領權利。   (二)凡經通知簽署後，均應遵守保密規定，不得將本案相關內容及個人權益告知他人       ，若有違反，依發行及認股辦法第六條第二項第四款辦理。 19.其他應敘明事項:   (一)本公司因發行及認股辦法第八條調整認股價格致調整後認股價格低於普通股股票       面額時，以普通股股票面額為認股價格。   (二)發行及認股辦法經董事會三分之二以上董事出席及出席董事超過二分之一同意。       日後如基於法令變更、主管機關核定變更或客觀環境變動時，得經董事會三分之       二以上董事出席及出席董事超過二分之一同意修訂之。   (三)發行及認股辦法如有未盡事宜，悉依相關法令規定辦理。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 8422 | 可寧衛* | revenue_breakout_low_response | 營收爆發低反應股 | 15 | 31 | B_可觀察 |  |  | no_signal | stale_signal | 1.董事會決議日期:115/08/26 2.發行期間:  本公司辦理股票公開發行前，視實際需要發行之，實際發行及認購基準日期授權由董事  長訂定之。 3.認股權人資格條件:  (一)本公司及本公司國內外控制或從屬公司之正式編制員工及兼職員工。  (二)實際得為認股權人之員工及其得認股之數量，將參酌職級、工作績效、年資、過去      及預期整體貢獻或特殊功績及其他等因素，由總經理擬定，呈董事長核定後辦理。 4.員工認股權憑證之發行單位總數:10,000單位 5.每單位認股權憑證得認購之股數:1,000股 6.因認股權行使而須發行之新股總數或依證券交易法第二十八條之二 規定須買回之股數:10,000,000股 7.認股價格:每股新台幣25元 8.認股權利期間:  (1)認股權憑證之存續期間為三年，屆滿後未行使之認股權視同放棄認股權利，認股權     人不得再行主張其認股權。該認股權憑證不得轉讓，但遇認股權人死亡其繼承者不     在此限。  (2)認股權憑證不得質押、贈予他人或作其他方式之處分。  (3)憑證授予期間與可行使比例如下所述：      認股權憑證授予期間         累積可行使認股比例      ------------------         ------------------          屆滿15個月                     50%          屆滿30個月                    100%  (4)認股權人自公司授予員工認股權憑證後，遇有違反勞動契約或工作規則等重大過失     者，公司有權就其尚未具行使權之認股權憑證予以收回並註銷。 9.認購股份之種類:本公司普通股股票。 10.員工離職或發生繼承時之處理方式:   (1)離職（含自願離職、資遣、開除）：      已具行使權之認股權憑證，得自離職日起於30日內行使認股權利；未具行使權之認      股權憑證，於離職當日即視為放棄認股權利。   (2)退休：      已具行使權之認股權憑證，於退休時，必須自退休日起30日內行使之，但仍以認股      權憑證存續期間為限。未行使認股的部份，於退休日起失效。   (3)留職停薪：      依政府法令規定及個人重大疾病、家庭重大變故、赴國外進修等原因經由公司特別      核准之留職停薪員工，已具行使權之認股權憑證，得自留職停薪起始日起30日內ㄧ      次行使完認股權利，逾期未行使則視同放棄其認股權利。      未具行使權利之認股權憑證得於復職後恢復權益，惟認股權行使時程應依留職停薪      期間往後遞延，但仍不得逾認股權憑證存續期間。   (4)一般死亡：      已具行使權之認股權憑證，由繼承人自死亡日起30日內行使認股權，未具行使權之      認股權憑證，於死亡當日即視為放棄認股權利。   (5)因受職業災害殘疾者：      (a)受職業災害致身體殘疾而無法繼續任職者         已具行使權之認股權憑證，認股權人需於離職日起30日內行使之，逾期未行使         即失效；未具行使權之認股權憑證，於認股權人離職當日即失效。      (b)因受職業災害或因公出差致死亡者         已具行使權之認股權憑證，於死亡時，繼承人可以行使全部之認股權利。惟該         認股權利，必須自死亡日起30日內行使之，但仍以認股權憑證存續期間為限，         未行使認股的部份，視同放棄。   (6)轉任集團關係企業：      若認股權人因個人因素請調至集團關係企業或其他公司時，其認股權憑證應比照離      職人員方式處理；認股權人係因公司業務需要，經本公司指派轉任關係企業或其他      公司時，其已授予認股權憑證之權利義務不受影響。   (7)認股權人或其繼承人若未能於上述期限內行使認股權者，即視為放棄認股權利。 11.其他認股條件:   放棄認股權利之認股權憑證，本公司將予註銷不再發行。 12.履約方式:以本公司發行新股方式交付。 13.認股價格之調整:   (一)本認股權憑證發行後，遇有本公司普通股股份發生變動時（即辦理現金增資、盈       餘轉增資、資本公積轉增資、公司合併、公司分割、股票分割及辦理現金增資參       與發行海外存託憑證等），認股價格依下列公式調整之（計算至新台幣角為止，       分以下四捨五入）；惟公司合併或公司分割時，認股價格不予調整。       除法令另有規定或需經主管機關核可外，對於登載於股東名薄之認股權股款繳納       憑證持有人，本公司將按認股價格調整之差異，加發認股權股款繳納憑證，實際       發行日期由董事長訂之。加發認股權股款繳納憑證時，若有不足壹股之股份金額       ，本公司以現金償付。   (二)調整後認股價格＝        調整前認股價格 × ｛〔已發行股數 + （每股繳款金額 × 新股發行股數）/ 調       整前認股價格〕/（已發行股數 + 新股發行股數）｝        (1)發行股數係指普通股已發行股份總數，不含已繳款之股款繳納憑證及債券換          股權利證書之股數。       (2)每股繳款金額如係屬無償配股或股票分割，則其繳款金額為零。       (3)遇有調整後認股價格高於調整前認股價格時，則不予調整。   (三)本認股權憑證發行後，遇有本公司發放普通股現金股利，每股發放金額占每股時       價之比率超過百分之ㄧ點五者，認股價格依下列公式調整之（調整後認股價格計       算至新台幣角為止，分以下四捨五入）：       調整後認股價格 ＝ 調整前認股價格 × （1－發放普通股現金股利/每股時價）   (四)本認股權憑證發行後，遇有非因庫藏股註銷之減資致普通股股份減少時，應依下       列公式計算調整後認股價格：       調整後認股價格=調整前認股價格 × （減資前已發行股份/減資後已發行股份） 14.行使認股權之程序:   (一)認股權人除依法暫停過戶期間外，得依發行及認股辦法第六條第二項所訂之時程       行使認股權利，並填具認股請求書，向本公司或股務代理機構提出申請，於送遞       時即生認股之效力，且不得申請撤銷。   (二)本公司或股務代理機構於受理認股之請求後，通知認股權人繳納股款至指定銀       行。   (三)本公司或股務代理機構於確認收足股款後，將其認購之股數登載於本公司股東名       簿，並於取得經濟部核准函後發給本公司新發行之普通股。   (四)本公司普通股若依法得於台灣證券交易所或櫃買中心買賣時，本公司新發行之普       通股自向認股權人交付之日起即得上市(櫃)買賣。   (五)本公司依發行及認股辦法發行新股交付予認股權人，將於每季結束後向公司登記       主管機關申請資本額變更登記及新股發行之申請；惟當年度若遇無償配股基準日       或現金增資認股除權基準日時，得調整變更登記時間。 15.認股後之權利義務:   本公司因認股權行使所發行之普通股，其權利義務與本公司已發行且流通在外之普通   股股票相同。 16.附有轉換、交換或認股者，其換股基準日:不適用 17.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 18.其他重要約定事項:   (一)本公司完成法定發行程序後，即由承辦部門通知認股權人簽署「員工認股權憑證       受領同意書」，經認股權人完成「員工認股權憑證受領同意書」簽署完成後，即       視為取得受領權利；未依規定完成簽署者，即視同放棄受領權利。   (二)凡經通知簽署後，均應遵守保密規定，不得將本案相關內容及個人權益告知他人       ，若有違反，依發行及認股辦法第六條第二項第四款辦理。 19.其他應敘明事項:   (一)本公司因發行及認股辦法第八條調整認股價格致調整後認股價格低於普通股股票       面額時，以普通股股票面額為認股價格。   (二)發行及認股辦法經董事會三分之二以上董事出席及出席董事超過二分之一同意。       日後如基於法令變更、主管機關核定變更或客觀環境變動時，得經董事會三分之       二以上董事出席及出席董事超過二分之一同意修訂之。   (三)發行及認股辦法如有未盡事宜，悉依相關法令規定辦理。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 8422 | 可寧衛* | 15 | 13 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 8422 | 可寧衛* | 43 | 2 | 422020.0 | 21000.0 | 20.1 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
