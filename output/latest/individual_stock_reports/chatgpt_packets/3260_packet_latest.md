# INDIVIDUAL STOCK CHATGPT PACKET - 3260 威剛

## Metadata
- generated_at: 2026-07-08 22:27:11 Asia/Taipei
- stock_id: 3260
- stock_name: 威剛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 165
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3260_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3260_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3260.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3260.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3260.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3260.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3260_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3260_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3260_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
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
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260708
- open: 408
- high: 413
- low: 397
- close: 404
- volume: 5808000
- ma5: 407.6
- ema23_primary: 411.19
- distance_to_ema23_pct: -1.75
- ma20: 409
- ma60: 417.73
- ma120: 376.73
- return_5d: 1.38
- return_20d: -4.04
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: -1.22
- distance_to_high_60_pct: -18.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,412,420.5,390,390,11259000,422.15,-7.61,420.88,413.64,1.74
20260611,388,399.5,378,394.5,13824000,419.84,-6.04,418.25,413.63,2.23
20260612,416,422,405.5,405.5,11982000,418.65,-3.14,417.27,413.15,2
20260615,414.5,435,413,423,16112000,419.01,0.95,417.52,412.24,2.59
20260616,430,434,417,417,13924000,418.84,-0.44,418.88,410.44,2.24
20260617,412,417,405.5,416,8232000,418.61,-0.62,419.4,409.75,1.4
20260618,420,425,412,423,12103000,418.97,0.96,419.9,409.93,2.07
20260622,434,443,427.5,434,15594000,420.22,3.28,420.73,410.73,2.36
20260623,436,436,410,412,13449000,419.54,-1.8,420.95,410.84,1.86
20260624,402,410,399,408.5,8268000,418.62,-2.42,420.88,411.47,1.08
20260625,421,423,407.5,409.5,9000000,417.86,-2,420.73,411.78,1.11
20260626,409.5,421,396,397.5,10709000,416.16,-4.48,420.38,412.24,1.25
20260629,399,406.5,394.5,404,5433000,415.15,-2.69,419.82,413.39,0.61
20260630,407.5,415,396,409,11091000,414.64,-1.36,418.93,414.07,1.18
20260701,411.5,412,392,398.5,14202000,413.29,-3.58,415.38,414.68,1.41
20260702,384,408,382.5,408,7750000,412.85,-1.17,412.68,415.43,0.74
20260703,404,411.5,403,411.5,5835000,412.74,-0.3,410.35,415.81,0.54
20260706,416,420,408,410.5,7015000,412.55,-0.5,409.8,416.55,0.64
20260707,417,418,404,404,8455000,411.84,-1.9,409.85,417.08,0.79
20260708,408,413,397,404,5808000,411.19,-1.75,409,417.73,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 29.03
- over_600_ratio: 26.7
- over_800_ratio: 25.82
- over_1000_ratio: 23.97
- over_400_change_1w: -1.8
- over_800_change_1w: -0.78
- over_1000_change_1w: -1.27
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,41.44,,35.94,,33.78,,0,False,False
20260508,38.64,-2.8,34.19,-1.75,31.68,-2.1,0,False,False
20260515,36.47,-2.17,32.61,-1.58,31.51,-0.17,0,False,False
20260522,34.99,-1.48,31.22,-1.39,28.74,-2.77,0,False,False
20260529,32.95,-2.04,28.62,-2.6,26.41,-2.33,0,False,False
20260605,35.16,2.21,31.23,2.61,29.87,3.46,1,True,True
20260612,32.51,-2.65,28.13,-3.1,26.49,-3.38,0,False,False
20260618,32.63,0.12,28.49,0.36,26.31,-0.18,1,False,True
20260626,30.83,-1.8,26.6,-1.89,25.24,-1.07,0,False,False
20260703,29.03,-1.8,25.82,-0.78,23.97,-1.27,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 3260 | 威剛 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.併購種類(如合併、分割、收購或股份受讓): 公開收購 2.事實發生日:115/7/7 3.參與併購公司名稱(如合併另一方公司、分割新設公司、收購或受讓股份標的公司之 名稱: 琉園股份有限公司(以下簡稱「琉園」或「被收購公司」) 4.交易相對人(如合併另一方公司、分割讓與他公司、收購或受讓股份之交易對象): 琉園參與應賣股東 5.交易相對人為關係人:否 6.交易相對人與公司之關係(本公司轉投資持股達XX%之被投資公司)，並說明選定 收購、受讓他公司股份之對象為關係企業或關係人之原因及是否不影響股東權益: 本次收購採公開收購方式進行，價格與條件均屬一律，倘有本公司關係人參與應賣 ，本公司依法不得拒絕或排除，故交易相對人可能為關係人。 7.併購目的及條件，包括併購理由、對價條件及支付時點(註七): (1)本公司公開收購取得琉園普通股股份之目的：本公司以公開收購方式取得被收購 公司普通股股份，主要係基於策略性投資目的，結合被收購公司所具備高端藝術設計 與文化價值，提升公開收購人之品牌形象與差異化，增加公開收購人合理之投資收益 、提升被收購 公司資產及股東權益報酬率，維護公司永續發展經營。  (2)本次公開收購對價為每股現金新臺幣24元整。  (3)在本次公開收購之條件已成就且受委任機構福邦證券於收受公開收購人或出具履約 保證文件之金融機構如期完成匯款義務之情況下，公開收購對價將由受委任機構福邦 證券於公開收購期間屆滿日（如經延長則為延長期間屆滿日）次日起算五個營業日 （含第五個營業日）以內，優先以銀行匯款方式支付至臺灣集中保管結算所提供予福邦 證券之應賣人銀行帳號，倘應賣人銀行帳號有誤或因其他原因致無法完成匯款時，以 支票(抬頭劃線並禁止背書轉讓）掛號郵寄至臺灣集中保管結算所所提供之應賣人地址。 匯款金額/支票金額之計算，係以應賣人成交股份收購對價扣除應賣人依法應繳納之 證券交易稅、臺灣集中保管結算所及證券經紀商手續費、銀行匯款費用或掛號郵寄支票 之郵資，及其他支付收購對價所必要之合理費用，並計算至「元」為止 （不足一元之部分捨棄）。  (4) 其他公開收購條件請詳閱公開收購說明 8.併購後預計產生之效益: 本次以公開收購方式取得被收購公司普通股股份，主要係基於策略性投資目的，以增加 公開收購人合理之投資收益、並提升被收購公司資產及股東權益報酬率。 9.併購對每股淨值及每股盈餘之影響: 公開收購完成後，透過認列合理之投資收益，對日後每股淨值與每股盈餘應有正面 之助益。 10.併購之對價種類及資金來源: 本次公開收購對價為每股現金新臺幣24元，所需現金對價總計為新臺幣600,000,000元 ，全數由本公司以自有資金支應。 11.換股比例及其計算依據: 一、換股比例：不適用。  二、計算依據：不適用。 12.本次交易會計師、律師或證券承銷商出具非合理性意見:否 13.會計師或律師事務所名稱或證券承銷商公司名稱: 大昌聯合會計師事務所 14.會計師或律師姓名: 曾柏堯會計師 15.會計師或律師開業證書字號: 北市會籍編號4519 16.獨立專家就本次併購換股比例、配發股東之現金或其他財產之合理性意見書內容 (一、包含公開收購價格訂定所採用之方法、原則或計算方式及與國際慣用之市價法 、成本法及現金流量折現法之比較。二、被收購公司與已上市櫃同業之財務狀況 、獲利情形及本益比之比較情形。三、公開收購價格若參考鑑價機構之鑑價報告者 ，應說明該鑑價報告內容及結論。四、收購人融資償還計畫若係以被收購公司或合 併後存續公司之資產或股份為擔保者，應說明對被收購公司或合併後存續公司財務 業務健全性之影響評估)(註七): 一)本案獨立專家依據評價公報之評價技術採用市場法之市價法及可類比公司法 之股價淨值比法及本益比法作為計算價值之乘數，據以推算琉園股份有限公司被 公開收購普通股之理論價格，並推算其每股普通股合理收購價格區間。經本案獨 立專家評估琉園股份有限公司普通股股票之公開收購價格合理區間 為新台幣18.40至43.39元。  (二)被收購公司與已上市櫃同業之財務狀況、獲利情形及本益比之比較情形：  被收購公司與已上市櫃同業之財務狀況、獲利情形及本益比之比較情形請詳閱 公開收購說明書之附件二公開收購對價合理性意見書。  (三)公開收購價格若參考鑑價機構之鑑價報告者，應說明該鑑價報告內容及結論：  不適用。  (四)收購人融資償還計畫若係以被收購公司或合併後存續公司之資產或股份為擔保者 ，應說明對被收購公司或合併後存續公司財務業務健全性之影響評估：不適用。 17.預定完成日程(註七): 本公開收購案依據法令規定必須向金融監督管理委員會申報並公告，申報日預計於 民國115年7月7日，公開收購開始日預計於民國115年7月8日。   在本次公開收購之條件成就下，且公開收購人或出具履約保證之金融機構已如期完 成匯款義務之情況下，公開收購對價將由受委任機構福邦證券於公開收購期間屆滿 日（如經延長則為延長期間屆滿日）次日起算五個營業日（含第五個營業日）以內 撥付。 18.既存或新設公司承受消滅(或分割)公司權利義務相關事項(註二): 不適用 19.參與合併公司之基本資料(註三): 不適用 20.分割之相關事項(含預定讓與既存公司或新設公司之營業、資產之評價價值；被 分割公司或其股東所取得股份之總數、種類及數量；被分割公司資本減少時，其資 本減少有關事項)(註：若非分割公告時，則不適用): 不適用 21.併購股份未來移轉之條件及限制: 無 22.併購完成後之計畫(包含一、繼續經營公司業務之意願及計畫內容。二、是否發生 解散、下市(櫃)、重大變更組織、資本、業務計畫、財務及生產、對公司重要人員 、資產之安排或運用，或其他任何影響公司股東權益之重大事項): (1)繼續經營公司業務之意願及計畫內容  公開收購人本次以公開收購方式取得被收購公司普通股股份，主要係基於 策略性投資目的，結合被收購公司所具備高端藝術設計與文化價值，提升 公開收購人之品牌形象與差異化，增加公開收購人合理之投資收益、提升 被收購公司資產及股東權益報酬率，維護公司永續發展經營。  (2)是否發生解散、下市(櫃)、重大變更組織、資本、業務計畫、財務及生 產，或其他任何影響公司股東權益之重大事項。  本公司並無影響被收購公司股東權益之重大事項，請詳閱公開收購說明書。 23.其他重要約定事項: 無 24.其他與併購相關之重大事項: (1)公開收購期間  自民國115年7月8日（下稱「收購期間開始日」）上午9時00分起至 民國115年7月27日（下稱「收購期間屆滿日」）下午3時30分止 ，惟公開收購人得依相關法令向金融監督管理委員會 （下稱「金管會」）申報並公告延長公開收購期間，但延長公開收購 期間不得超過五十日，且以一次為限。每個營業日接受申請應賣時間 及方式，請詳閱公開收購說明書。   (2)預定收購數量及最低收購數量  本次預定收購數量為25,000,000股（下稱「預定收購數量」）， 即被收購公司於經濟部商業司商工登記資料公示查詢系統顯示 民國115年4月10日最後異動日所載之已發行股份總數44,860,763股 （下稱「已發行股份總數」）之55.73% （25,000,000股/44,860,763股=55.73%）；惟若最終有效應賣之數 量未達預定收購數量，但已達10,000,000股（約當被收購公司已發行 股份總數之22.29%，下稱「最低收購數量」）時，則本公開收購之數量 條件即告成就。在本次公開收購之條件成就（係指有效應賣股份&#63849;&#63870; 已達最低收購&#63849;&#63870;時），且本次公開收購未依法停止進行之情況下， 公開收購人最多收購預定收購數量之股數。  若應賣有價證券數量超過預定收購數量時，公開收購人將依同一比&#63925;分配 至股為止向所有應賣人購買（計算方式請詳閱公開收購說明書）。  (3)其餘注意事項請詳公開收購說明書 25.本次交易，董事有無異議:否 26.併購交易中涉及利害關係董事資訊(自然人董事姓名或法人董事名稱暨其代表人姓名 、其自身或其代表之法人有利害關係之重要內容(包括但不限於實際或預計投資其他 參加併購公司之方式、持股比率、交易價格、是否參與併購公司之經營及其他投資條件 等情形)、其應迴避或不迴避理由、迴避情形、贊成或反對併購決議之理由)(註七): 本公司法人董事保達投資股份有限公司之代表人周康記 a.自身或其代表之法人有利害關係之重要內容： 本公司法人董事代表人周康記同時擔任琉園法人董事之代表人， 就本案有利害關係。 b.迴避情形及理由： 考量本案已由審計委員會先進行審議，且本次公開收購對價之合理性已依規定 取得獨立專家出具意見書確認，法人董事代表人周康記參與本案討論及表決應 無致損害本公司利益之虞，但為確保決議作成之客觀性，仍自請迴避參與本案 討論與表決。 c.贊成或反對公開收購案決議之理由： 考量本案完成後可形成「文化藝術×科技品牌」的跨界優勢並提升本公司品牌形象 與差異化，故贊成本案。 27.是否涉及營運模式變更:否 28.營運模式變更說明(註四): 不適用 29.過去一年及預計未來一年內與交易相對人交易情形(註五): 過去一年：本公司無此情事。 未來一年：本公司將視本次最終收購結果、被收購公司未來營運實 際需求及整體利益、及/或未來市場狀況，另行評估於公開收購期間 屆滿日起一年內是否再次取得被收購公司股權，惟目前尚無具體計畫。 30.資金來源(註五): 本公司自有資金 31.其他敘明事項(註六): 一、為進行本公開收購案，擬請董事會授權董事長及/或其指定之人代表 本公司處理與本公開收購有關之一切必要程序並採取相關必要之行為，包 括但不限於完成並簽署公開收購說明書、公開收購申報書及承諾書、協商 、簽署及交付所有相關文件及合約，以及向主管機關提出申請或申報等相 關事項。如因主管機關指示或因應市場狀況、客觀環境變動，或有其他正當 理由等而致本公開收購程序、申報文件或條件須予修正（包括但不限於延長 公開收購期間等）或其他未盡事宜，擬授權董事長及/或其指定之人全權處 理之。 二、本公開收購案依據法令規定必須向金融監督管理委員會申報並公告， 申報日預計於民國115年7月7日，公開收購開始日預計於民國115年7月8日。 三、其他公開收購條件請詳公開收購說明書。 公開收購說明書查詢網址： 公開資訊觀測站：http://mops.twse.com.tw (公開資訊觀測站/投資專區/公開收購專區) 註二、既存或新設公司承受消滅公司權利義務相關事項，包括庫藏股及已發行具有股權性質有 　　　價證券之處理原則。 註三：參與合併公司之基本資料包括公司名稱及所營業務之主要內容。 註四：倘涉營運模式變更，請於欄位敘明包括營業範圍變更、產品線擴充/縮減、製程調整、產業 　　　水平/垂直整合，或其他涉及營運架構調整事項。 註五：非屬私募資金用以併購案件者，得填寫不適用。 註六：若本案成就前，尚需經國內、外主管機關(如:投審會、公平交易委員會、反壟斷局或其他單位)核准或許可者，應予敘明相關事項。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260708 | 3260 | 威剛 | revenue_breakout_low_response | 營收爆發低反應股 | 17.0 | 22.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.併購種類(如合併、分割、收購或股份受讓): 公開收購 2.事實發生日:115/7/7 3.參與併購公司名稱(如合併另一方公司、分割新設公司、收購或受讓股份標的公司之 名稱: 琉園股份有限公司(以下簡稱「琉園」或「被收購公司」) 4.交易相對人(如合併另一方公司、分割讓與他公司、收購或受讓股份之交易對象): 琉園參與應賣股東 5.交易相對人為關係人:否 6.交易相對人與公司之關係(本公司轉投資持股達XX%之被投資公司)，並說明選定 收購、受讓他公司股份之對象為關係企業或關係人之原因及是否不影響股東權益: 本次收購採公開收購方式進行，價格與條件均屬一律，倘有本公司關係人參與應賣 ，本公司依法不得拒絕或排除，故交易相對人可能為關係人。 7.併購目的及條件，包括併購理由、對價條件及支付時點(註七): (1)本公司公開收購取得琉園普通股股份之目的：本公司以公開收購方式取得被收購 公司普通股股份，主要係基於策略性投資目的，結合被收購公司所具備高端藝術設計 與文化價值，提升公開收購人之品牌形象與差異化，增加公開收購人合理之投資收益 、提升被收購 公司資產及股東權益報酬率，維護公司永續發展經營。  (2)本次公開收購對價為每股現金新臺幣24元整。  (3)在本次公開收購之條件已成就且受委任機構福邦證券於收受公開收購人或出具履約 保證文件之金融機構如期完成匯款義務之情況下，公開收購對價將由受委任機構福邦 證券於公開收購期間屆滿日（如經延長則為延長期間屆滿日）次日起算五個營業日 （含第五個營業日）以內，優先以銀行匯款方式支付至臺灣集中保管結算所提供予福邦 證券之應賣人銀行帳號，倘應賣人銀行帳號有誤或因其他原因致無法完成匯款時，以 支票(抬頭劃線並禁止背書轉讓）掛號郵寄至臺灣集中保管結算所所提供之應賣人地址。 匯款金額/支票金額之計算，係以應賣人成交股份收購對價扣除應賣人依法應繳納之 證券交易稅、臺灣集中保管結算所及證券經紀商手續費、銀行匯款費用或掛號郵寄支票 之郵資，及其他支付收購對價所必要之合理費用，並計算至「元」為止 （不足一元之部分捨棄）。  (4) 其他公開收購條件請詳閱公開收購說明 8.併購後預計產生之效益: 本次以公開收購方式取得被收購公司普通股股份，主要係基於策略性投資目的，以增加 公開收購人合理之投資收益、並提升被收購公司資產及股東權益報酬率。 9.併購對每股淨值及每股盈餘之影響: 公開收購完成後，透過認列合理之投資收益，對日後每股淨值與每股盈餘應有正面 之助益。 10.併購之對價種類及資金來源: 本次公開收購對價為每股現金新臺幣24元，所需現金對價總計為新臺幣600,000,000元 ，全數由本公司以自有資金支應。 11.換股比例及其計算依據: 一、換股比例：不適用。  二、計算依據：不適用。 12.本次交易會計師、律師或證券承銷商出具非合理性意見:否 13.會計師或律師事務所名稱或證券承銷商公司名稱: 大昌聯合會計師事務所 14.會計師或律師姓名: 曾柏堯會計師 15.會計師或律師開業證書字號: 北市會籍編號4519 16.獨立專家就本次併購換股比例、配發股東之現金或其他財產之合理性意見書內容 (一、包含公開收購價格訂定所採用之方法、原則或計算方式及與國際慣用之市價法 、成本法及現金流量折現法之比較。二、被收購公司與已上市櫃同業之財務狀況 、獲利情形及本益比之比較情形。三、公開收購價格若參考鑑價機構之鑑價報告者 ，應說明該鑑價報告內容及結論。四、收購人融資償還計畫若係以被收購公司或合 併後存續公司之資產或股份為擔保者，應說明對被收購公司或合併後存續公司財務 業務健全性之影響評估)(註七): 一)本案獨立專家依據評價公報之評價技術採用市場法之市價法及可類比公司法 之股價淨值比法及本益比法作為計算價值之乘數，據以推算琉園股份有限公司被 公開收購普通股之理論價格，並推算其每股普通股合理收購價格區間。經本案獨 立專家評估琉園股份有限公司普通股股票之公開收購價格合理區間 為新台幣18.40至43.39元。  (二)被收購公司與已上市櫃同業之財務狀況、獲利情形及本益比之比較情形：  被收購公司與已上市櫃同業之財務狀況、獲利情形及本益比之比較情形請詳閱 公開收購說明書之附件二公開收購對價合理性意見書。  (三)公開收購價格若參考鑑價機構之鑑價報告者，應說明該鑑價報告內容及結論：  不適用。  (四)收購人融資償還計畫若係以被收購公司或合併後存續公司之資產或股份為擔保者 ，應說明對被收購公司或合併後存續公司財務業務健全性之影響評估：不適用。 17.預定完成日程(註七): 本公開收購案依據法令規定必須向金融監督管理委員會申報並公告，申報日預計於 民國115年7月7日，公開收購開始日預計於民國115年7月8日。   在本次公開收購之條件成就下，且公開收購人或出具履約保證之金融機構已如期完 成匯款義務之情況下，公開收購對價將由受委任機構福邦證券於公開收購期間屆滿 日（如經延長則為延長期間屆滿日）次日起算五個營業日（含第五個營業日）以內 撥付。 18.既存或新設公司承受消滅(或分割)公司權利義務相關事項(註二): 不適用 19.參與合併公司之基本資料(註三): 不適用 20.分割之相關事項(含預定讓與既存公司或新設公司之營業、資產之評價價值；被 分割公司或其股東所取得股份之總數、種類及數量；被分割公司資本減少時，其資 本減少有關事項)(註：若非分割公告時，則不適用): 不適用 21.併購股份未來移轉之條件及限制: 無 22.併購完成後之計畫(包含一、繼續經營公司業務之意願及計畫內容。二、是否發生 解散、下市(櫃)、重大變更組織、資本、業務計畫、財務及生產、對公司重要人員 、資產之安排或運用，或其他任何影響公司股東權益之重大事項): (1)繼續經營公司業務之意願及計畫內容  公開收購人本次以公開收購方式取得被收購公司普通股股份，主要係基於 策略性投資目的，結合被收購公司所具備高端藝術設計與文化價值，提升 公開收購人之品牌形象與差異化，增加公開收購人合理之投資收益、提升 被收購公司資產及股東權益報酬率，維護公司永續發展經營。  (2)是否發生解散、下市(櫃)、重大變更組織、資本、業務計畫、財務及生 產，或其他任何影響公司股東權益之重大事項。  本公司並無影響被收購公司股東權益之重大事項，請詳閱公開收購說明書。 23.其他重要約定事項: 無 24.其他與併購相關之重大事項: (1)公開收購期間  自民國115年7月8日（下稱「收購期間開始日」）上午9時00分起至 民國115年7月27日（下稱「收購期間屆滿日」）下午3時30分止 ，惟公開收購人得依相關法令向金融監督管理委員會 （下稱「金管會」）申報並公告延長公開收購期間，但延長公開收購 期間不得超過五十日，且以一次為限。每個營業日接受申請應賣時間 及方式，請詳閱公開收購說明書。   (2)預定收購數量及最低收購數量  本次預定收購數量為25,000,000股（下稱「預定收購數量」）， 即被收購公司於經濟部商業司商工登記資料公示查詢系統顯示 民國115年4月10日最後異動日所載之已發行股份總數44,860,763股 （下稱「已發行股份總數」）之55.73% （25,000,000股/44,860,763股=55.73%）；惟若最終有效應賣之數 量未達預定收購數量，但已達10,000,000股（約當被收購公司已發行 股份總數之22.29%，下稱「最低收購數量」）時，則本公開收購之數量 條件即告成就。在本次公開收購之條件成就（係指有效應賣股份&#63849;&#63870; 已達最低收購&#63849;&#63870;時），且本次公開收購未依法停止進行之情況下， 公開收購人最多收購預定收購數量之股數。  若應賣有價證券數量超過預定收購數量時，公開收購人將依同一比&#63925;分配 至股為止向所有應賣人購買（計算方式請詳閱公開收購說明書）。  (3)其餘注意事項請詳公開收購說明書 25.本次交易，董事有無異議:否 26.併購交易中涉及利害關係董事資訊(自然人董事姓名或法人董事名稱暨其代表人姓名 、其自身或其代表之法人有利害關係之重要內容(包括但不限於實際或預計投資其他 參加併購公司之方式、持股比率、交易價格、是否參與併購公司之經營及其他投資條件 等情形)、其應迴避或不迴避理由、迴避情形、贊成或反對併購決議之理由)(註七): 本公司法人董事保達投資股份有限公司之代表人周康記 a.自身或其代表之法人有利害關係之重要內容： 本公司法人董事代表人周康記同時擔任琉園法人董事之代表人， 就本案有利害關係。 b.迴避情形及理由： 考量本案已由審計委員會先進行審議，且本次公開收購對價之合理性已依規定 取得獨立專家出具意見書確認，法人董事代表人周康記參與本案討論及表決應 無致損害本公司利益之虞，但為確保決議作成之客觀性，仍自請迴避參與本案 討論與表決。 c.贊成或反對公開收購案決議之理由： 考量本案完成後可形成「文化藝術×科技品牌」的跨界優勢並提升本公司品牌形象 與差異化，故贊成本案。 27.是否涉及營運模式變更:否 28.營運模式變更說明(註四): 不適用 29.過去一年及預計未來一年內與交易相對人交易情形(註五): 過去一年：本公司無此情事。 未來一年：本公司將視本次最終收購結果、被收購公司未來營運實 際需求及整體利益、及/或未來市場狀況，另行評估於公開收購期間 屆滿日起一年內是否再次取得被收購公司股權，惟目前尚無具體計畫。 30.資金來源(註五): 本公司自有資金 31.其他敘明事項(註六): 一、為進行本公開收購案，擬請董事會授權董事長及/或其指定之人代表 本公司處理與本公開收購有關之一切必要程序並採取相關必要之行為，包 括但不限於完成並簽署公開收購說明書、公開收購申報書及承諾書、協商 、簽署及交付所有相關文件及合約，以及向主管機關提出申請或申報等相 關事項。如因主管機關指示或因應市場狀況、客觀環境變動，或有其他正當 理由等而致本公開收購程序、申報文件或條件須予修正（包括但不限於延長 公開收購期間等）或其他未盡事宜，擬授權董事長及/或其指定之人全權處 理之。 二、本公開收購案依據法令規定必須向金融監督管理委員會申報並公告， 申報日預計於民國115年7月7日，公開收購開始日預計於民國115年7月8日。 三、其他公開收購條件請詳公開收購說明書。 公開收購說明書查詢網址： 公開資訊觀測站：http://mops.twse.com.tw (公開資訊觀測站/投資專區/公開收購專區) 註二、既存或新設公司承受消滅公司權利義務相關事項，包括庫藏股及已發行具有股權性質有 　　　價證券之處理原則。 註三：參與合併公司之基本資料包括公司名稱及所營業務之主要內容。 註四：倘涉營運模式變更，請於欄位敘明包括營業範圍變更、產品線擴充/縮減、製程調整、產業 　　　水平/垂直整合，或其他涉及營運架構調整事項。 註五：非屬私募資金用以併購案件者，得填寫不適用。 註六：若本案成就前，尚需經國內、外主管機關(如:投審會、公平交易委員會、反壟斷局或其他單位)核准或許可者，應予敘明相關事項。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 3260 | 威剛 | 13 | 12 | 5 | 10 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
