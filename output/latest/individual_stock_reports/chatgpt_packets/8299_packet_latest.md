# INDIVIDUAL STOCK CHATGPT PACKET - 8299 群聯

## Metadata
- generated_at: 2026-08-22 22:29:15 Asia/Taipei
- stock_id: 8299
- stock_name: 群聯
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
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
- individual_report_md_exists: True
- sell_strategy_summary_exists: True
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8299_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8299_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8299.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8299.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8299.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8299.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8299_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8299_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8299_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 2005
- high: 2075
- low: 1995
- close: 2075
- volume: 3154000
- ma5: 2024
- ema23_primary: 2005.51
- distance_to_ema23_pct: 3.46
- ma20: 1920.5
- ma60: 2158.83
- ma120: 2062.67
- return_5d: -0.24
- return_20d: 13.7
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: 8.04
- distance_to_high_60_pct: -26.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,1805,1820,1730,1820,4004000,2061.89,-11.73,2074.25,2322.5,0.98
20260728,1680,1685,1640,1650,4246000,2027.57,-18.62,2039.75,2318.33,1.02
20260729,1620,1620,1485,1515,8133000,1984.86,-23.67,1996.25,2310.08,1.84
20260730,1485,1640,1445,1495,6936000,1944.03,-23.1,1957.5,2299.75,1.53
20260731,1640,1640,1640,1640,1236000,1918.7,-14.53,1927.5,2288.33,0.28
20260803,1675,1800,1670,1760,5723000,1905.47,-7.63,1900.75,2277.83,1.26
20260804,1750,1850,1725,1820,4344000,1898.35,-4.13,1877.25,2267.67,0.96
20260805,1900,1910,1845,1845,3551000,1893.9,-2.58,1862.25,2253.92,0.8
20260806,1815,2025,1815,2025,5289000,1904.83,6.31,1856.5,2242.25,1.17
20260807,2060,2075,1970,2020,6639000,1914.43,5.51,1846.5,2232.25,1.42
20260810,2060,2080,2030,2040,4195000,1924.89,5.98,1840,2218.25,0.88
20260811,2035,2100,2015,2090,2872000,1938.65,7.81,1842,2208.92,0.62
20260812,2110,2245,2110,2210,5656000,1961.26,12.68,1847.25,2200.17,1.22
20260813,2260,2280,2175,2280,6892000,1987.82,14.7,1862.25,2197.08,1.45
20260814,2325,2325,2065,2080,14997000,1995.51,4.23,1877,2194,2.89
20260817,2110,2125,2085,2085,4262000,2002.96,4.1,1894.5,2189.83,0.82
20260818,2105,2120,2000,2000,4517000,2002.72,-0.14,1901.75,2182.67,0.86
20260819,1920,1970,1905,1965,4356000,1999.57,-1.73,1904.25,2174.08,0.83
20260820,2010,2080,1965,1995,3715000,1999.19,-0.21,1908,2165.58,0.7
20260821,2005,2075,1995,2075,3154000,2005.51,3.46,1920.5,2158.83,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 41.53
- over_600_ratio: 38
- over_800_ratio: 35.67
- over_1000_ratio: 32.44
- over_400_change_1w: -1.85
- over_800_change_1w: -1.1
- over_1000_change_1w: -2.32
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,48.31,-1.13,39.95,-2.4,37.91,-0.77,0,False,False
20260612,46.18,-2.13,39.11,-0.84,35.9,-2.01,0,False,False
20260618,45.76,-0.42,38.36,-0.75,35.11,-0.79,0,False,False
20260626,46.29,0.53,37.29,-1.07,36.09,0.98,1,False,True
20260703,45.53,-0.76,37.92,0.63,34.66,-1.43,2,False,True
20260709,45.05,-0.48,35.99,-1.93,33.98,-0.68,0,False,False
20260717,44.14,-0.91,36.55,0.56,34.96,0.98,1,False,True
20260724,43.59,-0.55,36.89,0.34,33.16,-1.8,2,False,True
20260731,42.31,-1.28,35.63,-1.26,33.18,0.02,3,False,True
20260807,43.36,1.05,35.8,0.17,34.62,1.44,4,True,True
20260814,43.38,0.02,36.77,0.97,34.76,0.14,5,True,True
20260821,41.53,-1.85,35.67,-1.1,32.44,-2.32,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8299 | 群聯 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期:115/07/14 2.發行期間: 於主管機關申報生效通知到達之日起二年內發行，得視實際需要，一次或分次發 行，實際發行日期授權由董事長訂定之。  3.認股權人資格條件: (一)認股權人以本公司及國內外從屬公司編制內全職、非全職員工為限(所稱「從 屬公司」，係指符合金融監督管理委員會107年12月27日金管證發字第1070121068 號函釋規定)。 本辦法所稱之員工包含全職及非全職，定義如下： 1.全職人員：受僱用繼續性工作，並定期支領薪資者。 2.非全職人員：受僱從事臨時性、短期性及特定性工作，而簽訂定期勞動契約或                顧問合約之人員。 (二)實際得為認股權人之員工及所得認股權之數量，將參酌員工之年資、職等、工     作績效考核、整體貢獻及特殊功績等因素擬定分配標準，由董事長或其指定之     人核定後，提報董事會同意。如認股權人具本公司經理人或兼任本公司董事之     員工身分者，應先提報薪資報酬委員會同意，再提報董事會決議；認股權人非     具本公司經理人或未兼任本公司董事之員工身分者，應先提報審計委員會同意     ，再提報董事會決議。 (三)依發行人募集與發行有價證券處理準則第60條之9規定，發行人依募集與發行     有價證券處理準則第五十六條之一第一項規定發行員工認股權憑證累計給予單     一認股權人得認購股數加計認股權人累計取得限制員工權利新股之合計數，不     得超過已發行股份總數之千分之三，且加計本公司依發行人募集與發行有價證     券處理準則第五十六條第一項規定發行員工認股權憑證累計給予單一認股權人     得認購股數，不得超過已發行股份總數之百分之一。但經各中央目的事業主管     機關專案核准者，單一員工取得員工認股權憑證與限制員工權利新股之合計數     ，得不受前開比例之限制。  4.員工認股權憑證之發行單位總數:發行總額為10,000,000單位。  5.每單位認股權憑證得認購之股數:每單位認股權憑證得認購股數為1股。  6.因認股權行使而須發行之新股總數或依證券交易法第二十八條之二 規定須買回之股數:因認股權行使而須發行之普通股新股總數為10,000,000股。  7.認股價格:認股價格以不低於發行日公司普通股股票之收盤價訂定之。  8.認股權利期間: (一)除本條或本辦法另有規定外，認股權人自被授予員工認股權憑證起持續任職於     本公司滿二年後可按下列時程行使認股。認股權憑證之存續期間為四年，不得     轉讓、質押、贈予他人或作其他方式之處分，但因繼承者不在此限。      認股權憑證授予後持續任職於本公司期間        可行使認股權比例(累計)                 滿2年	                                   50%                 滿3年	                                  100% (二)認股權人自公司授予員工認股權憑證後，遇有重大違反勞動契約、聘僱合約     或本公司管理規章等事由時，本公司有權就其尚未具行使權之認股權憑證予     以收回註銷。  9.認購股份之種類:本公司普通股股票。  10.員工離職或發生繼承時之處理方式:   認股權人如因自願離職、留職停薪、退休、死亡、受職業災害殘疾或死亡者、   資遣或解雇、調職時，應於認股權憑證存續期間內依下列方式處理： (一)自願離職：     依本條第(二)項規定已具認股行使權之認股權憑證，得自離職日起一個月內     行使認股權利，未於前述期間內行使權利者，視同放棄認股權利；未具行使     權之認股權憑證，於離職當日即視為放棄認股權利。 (二)留職停薪(不包含彈性育嬰留停)：     依本條第(二)項規定已具認股行使權之認股權憑證，得自留職停薪日起一個     月內行使認股權利，未於前述期間內行使權利者，視同放棄認股權利；未具     行使權之認股權憑證得於復職後恢復權益，惟認股權人於留職停薪前及復職後     於本公司任職期間合計達本條第（二）項所定期間後方可行使認股權利，行使     期間仍以本條第(二)項所定認股權憑證之存續期間為限。 (三)退休：     已授予之認股權憑證，於退休時，可以行使全部之認股權利。惟該認股權利，     應自退休日起或被授予認股權憑證屆滿二年之日起（以日期較晚者為主）六個     月內行使之，至遲不得晚於認股權憑證之存續期間。 (四)死亡：     已具認股行使權之認股權憑證，由繼承人自認股權人死亡日起六個月內行使認     股權，至遲不得晚於認股權憑證之存續期間。未具行使權之認股權憑證，於死     亡當日即視為放棄認股權利。 (五)受職業災害致殘疾或死亡： (1)因受職業災害致身體殘疾而無法繼續任職者，已授予之認股權憑證，於離職時，    可以行使全部之認股權利。惟該認股權利，應自離職日起或被授予認股權憑證    屆滿二年之日起（以日期較晚者為主）六個月內行使之，至遲不得晚於認股權    憑證之存續期間。 (2)因受職業災害致死亡者，已授予之認股權憑證，於死亡時，繼承人可以行使全    部之認股權利。惟該認股權利，應自死亡日起或被授予認股權憑證屆滿二年之    日起（以日期較晚者為主）六個月內行使之，至遲不得晚於認股權憑證之存續    期間。 (六)資遣或解雇：     已具認股行使權之認股權憑證，得自資遣生效日或解雇日起一個月內行使認股     權利，惟至遲不得晚於認股權憑證之存續期間。未於前述期間內行使權利者，     視同放棄認股權利。未具行使權之認股權憑證，自資遣生效日或解雇日起即視     為放棄認股權利。 (七)調職：     如認股權人主動申請調職至本公司之子公司或關係企業公司時，其認股權憑證     應比照離職方式處理。如應本公司要求而調職者，經本公司董事長或其授權之     人核定須轉任本公司國內外從屬公司之認股權人，其已授予認股權憑證之權利     義務均不受轉任之影響。 (八)認股權人或其繼承人若未能於上述期限內行使認股權者，即視為放棄認股權利。 (九)其它終止僱傭關係：     上述原因外，其它未約定之終止僱傭關係或僱傭關係調整，依本條第二項所規     定之權利期間及權利行使時程行使認股權利。 (十)其他非屬上列原因或實際依照前揭各款規定執行時必須依相關法令進行調整時，     授權董事長依實際狀況個別訂定或調整之。 (十一)放棄認股權利之認股權憑證處理方式：       對於放棄認股權利之認股權憑證，本公司將予以收回註銷不再發行。  11.其他認股條件:無。  12.履約方式:本公司以發行新股方式交付。  13.認股價格之調整: (一)本認股權憑證發行後，除本公司所發行具有普通股轉換權或認股權之各種有     價證券換發普通股股份或因員工酬勞發行新股者外，遇有本公司普通股股份     發生變動時（即包含以募集發行或以私募方式辦理現金增資、盈餘轉增資、     資本公積轉增資、公司合併或受讓他公司股份發行新股、股票分割及辦理現     金增資參與發行海外存託憑證等），認股價格依下列公式調整之（計算至新     台幣角為止，分以下四拾五入），如係因股票面額變更致已發行普通股股份     增加，於新股換發基準日調整之，但有實際繳款作業者於股款繳足日調整之     。     調整後之認股價格＝調整前認股價格×    〔已發行股數＋(每股繳款金額×新股發行股數) ÷每股時價〕÷    〔已發行股數＋新股發行股數〕     股票面額變更時     調整後之認股價格＝調整前認股價格×(股票面額變更前已發行普通股股數     ÷股票面額變更後已發行普通股股數) (1)「已發行股數」係指普通股已發行股份總數(含已辦理完成之私募普通股)，     不含已繳納之股款繳納憑證及債券換股權利證書之股數，但應扣除本公司買     回惟尚未註銷或轉讓之庫藏股股數。 (2)「每股繳款金額」如係屬無償配股或股票分割，則其繳款金額為零。 (3)本公司與他公司合併時，增資新股每股繳款金額為合併基準日前第四十五個    營業日起連續三十個營業日之本公司普通股平均收盤價。 (4)遇有調整後認股價格高於調整前認股價格時，則不予調整。 (5)調整後認股價格如低於普通股股票面額時，以普通股股票面額為認股價格。 (6)上述每股時價之訂定，應以除權基準日、訂價基準日或股票分割基準日之前    一、三、五個營業日擇一計算之普通股收盤價之簡單算術平均數為準。 (7)倘非前述所列舉之股份變動情形時，則授權董事會(長)決議調整與否。 (8)遇有須調整認股價格之情事，依上述公式調整，並經董事長核定，無須再送    董事會決議。 (二)認股權憑證發行後，本公司發放普通股現金股利時，認股價格應於除息基     準日依下列公式調整之（計算至新台幣角為止，分以下四捨五入）。     調整後之認股價格＝調整前認股價格×(1-發放普通股現金股利占每股時價之     比率) (1)上述每股時價之訂定，應以現金股息停止過戶除息公告日之前一、三、五個    營業日擇一計算本公司普通股收盤價之簡單算術平均數為準。 (2)遇有同時發放現金股利及股票股利（含盈餘轉增資及資本公積轉增資）時，則    先依現金股利金額調整認股價格後，再依股票股利金額調整認股價格。 (三)認股權憑證發行後，如遇非因庫藏股註銷之減資致普通股股份減少，於減資     基準日依下列公式計算其調整後認股價格（計算至新台幣角為止，分以下四     拾五入），如係因股票面額變更致普通股股份減少，於新股換發基準日調整     之。 (1)減資彌補虧損時    調整後認股價格＝調整前認股價格 × (減資前已發行普通股股數(註) ÷    減資後已發行普通股股數) (2)現金減資時    調整後認股價格＝〔調整前認股價格×（1-每股退還現金金額占換發新股票前最    後交易日收盤價之比率）〕×（減資前已發行普通股股數 ÷ 減資後已發行普通    股股數） (3)股票面額變更時    調整後之認股價格= 調整前認股價格×（股票面額變更前已發行普通股股數(註)    ÷股票面額變更後已發行普通股股數）    註：已發行普通股股數包括已發行普通股及私募股份之總數，並減除本公司買回    但尚未註銷或轉讓之庫藏股普通股股數。  14.行使認股權之程序: (一)認股權人除遇第九條對認股權行使之限制及依法暫停過戶期間外，得依本辦法     行使認股權利，並填具「認股請求書」，向本公司股務代理機構提出認股申請     ，於遞送時即生認股之效力，且不得申請撤銷。 (二)本公司股務代理機構受理認股之請求後，通知認股權人於期限內繳納股款至指     定銀行，認股權人未於繳納期限內繳足股款，則視同放棄認股權利。 (三)本公司股務代理機構於確認收足股款後，將員工認購之股數及員工姓名登載於     本公司股東名簿，且經認股權人出具集保帳號，並於五個營業日內以集保劃撥     方式發放之。 (四)上述普通股股票自向認股權人交付新股之日起即得上櫃(市)買賣。 (五)本公司每季至少向公司登記之主管機關申請資本額變更登記一次。  15.認股後之權利義務: 依本辦法交付之普通股新股之權利義務與本公司普通股股票相同，認股權人依本辦 法所認購之股票其相關之稅賦按當時中華民國之稅法規定辦理。  16.附有轉換、交換或認股者，其換股基準日:NA 17.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 18.其他重要約定事項: (一)認股權行使之限制     本公司所發放予員工之認股權憑證，每年度於以下期間不得行使認股權： (1)當年度股東會召開前之法定停止過戶期間。 (2)本公司無償配股停止過戶日、現金股息停止過戶日或現金增資認股停止過戶日    前十五個營業日起，至權利分派基準日止，辦理減資之減資基準日起至減資換發    股票開始交易日前一日止。 (3)「決定當年度之合併基準日之董事會」召開後至當年度合併基準日前之期間；或    「決定當年度之分割基準日之董事會」召開後至當年度分割基準日前之期間；或    「決定當年度之有償配股基準日之董事會」召開後至當年度有償配股基準日前之    期間。 (4)其它依事實發生之法定停止過戶期間。 (二)保密規定     認股權人經授予認股權憑證後，應遵守保密規定，除法令或主管機關要求外，     不得洩露被授予之認股權憑證相關內容及數量，若有違反之情事，依本辦法第　     五條第二項第二款辦理。 (三)實施細則     個別認股權人被授予認股權憑證之數量、認股權憑證之行使、認股繳款、換發     股票等事宜之相關作業及各該作業時間，將由本公司另行通知認股權人。 (四)其他重要約定事項 (1)本辦法應經董事會三分之二以上董事出席及出席董事超過二分之一之同意後通過    ，並報經主管機關申報後生效，實際發行前修改時亦同。本公司並授權董事長於    案件審查期間因應主管機關要求可修訂本發行及認股辦法，惟嗣後仍須提董事會    追認後始得發行。 (2)本辦法如有未盡事宜，悉依相關法令規定或主管機關之要求辦理。  19.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 8299 | 群聯 | revenue_breakout_low_response | 營收爆發低反應股 | 23 | 2 | A_優先追蹤 |  |  |  | stale_signal | 1.董事會決議日期:115/07/14 2.發行期間: 於主管機關申報生效通知到達之日起二年內發行，得視實際需要，一次或分次發 行，實際發行日期授權由董事長訂定之。  3.認股權人資格條件: (一)認股權人以本公司及國內外從屬公司編制內全職、非全職員工為限(所稱「從 屬公司」，係指符合金融監督管理委員會107年12月27日金管證發字第1070121068 號函釋規定)。 本辦法所稱之員工包含全職及非全職，定義如下： 1.全職人員：受僱用繼續性工作，並定期支領薪資者。 2.非全職人員：受僱從事臨時性、短期性及特定性工作，而簽訂定期勞動契約或                顧問合約之人員。 (二)實際得為認股權人之員工及所得認股權之數量，將參酌員工之年資、職等、工     作績效考核、整體貢獻及特殊功績等因素擬定分配標準，由董事長或其指定之     人核定後，提報董事會同意。如認股權人具本公司經理人或兼任本公司董事之     員工身分者，應先提報薪資報酬委員會同意，再提報董事會決議；認股權人非     具本公司經理人或未兼任本公司董事之員工身分者，應先提報審計委員會同意     ，再提報董事會決議。 (三)依發行人募集與發行有價證券處理準則第60條之9規定，發行人依募集與發行     有價證券處理準則第五十六條之一第一項規定發行員工認股權憑證累計給予單     一認股權人得認購股數加計認股權人累計取得限制員工權利新股之合計數，不     得超過已發行股份總數之千分之三，且加計本公司依發行人募集與發行有價證     券處理準則第五十六條第一項規定發行員工認股權憑證累計給予單一認股權人     得認購股數，不得超過已發行股份總數之百分之一。但經各中央目的事業主管     機關專案核准者，單一員工取得員工認股權憑證與限制員工權利新股之合計數     ，得不受前開比例之限制。  4.員工認股權憑證之發行單位總數:發行總額為10,000,000單位。  5.每單位認股權憑證得認購之股數:每單位認股權憑證得認購股數為1股。  6.因認股權行使而須發行之新股總數或依證券交易法第二十八條之二 規定須買回之股數:因認股權行使而須發行之普通股新股總數為10,000,000股。  7.認股價格:認股價格以不低於發行日公司普通股股票之收盤價訂定之。  8.認股權利期間: (一)除本條或本辦法另有規定外，認股權人自被授予員工認股權憑證起持續任職於     本公司滿二年後可按下列時程行使認股。認股權憑證之存續期間為四年，不得     轉讓、質押、贈予他人或作其他方式之處分，但因繼承者不在此限。      認股權憑證授予後持續任職於本公司期間        可行使認股權比例(累計)                 滿2年	                                   50%                 滿3年	                                  100% (二)認股權人自公司授予員工認股權憑證後，遇有重大違反勞動契約、聘僱合約     或本公司管理規章等事由時，本公司有權就其尚未具行使權之認股權憑證予     以收回註銷。  9.認購股份之種類:本公司普通股股票。  10.員工離職或發生繼承時之處理方式:   認股權人如因自願離職、留職停薪、退休、死亡、受職業災害殘疾或死亡者、   資遣或解雇、調職時，應於認股權憑證存續期間內依下列方式處理： (一)自願離職：     依本條第(二)項規定已具認股行使權之認股權憑證，得自離職日起一個月內     行使認股權利，未於前述期間內行使權利者，視同放棄認股權利；未具行使     權之認股權憑證，於離職當日即視為放棄認股權利。 (二)留職停薪(不包含彈性育嬰留停)：     依本條第(二)項規定已具認股行使權之認股權憑證，得自留職停薪日起一個     月內行使認股權利，未於前述期間內行使權利者，視同放棄認股權利；未具     行使權之認股權憑證得於復職後恢復權益，惟認股權人於留職停薪前及復職後     於本公司任職期間合計達本條第（二）項所定期間後方可行使認股權利，行使     期間仍以本條第(二)項所定認股權憑證之存續期間為限。 (三)退休：     已授予之認股權憑證，於退休時，可以行使全部之認股權利。惟該認股權利，     應自退休日起或被授予認股權憑證屆滿二年之日起（以日期較晚者為主）六個     月內行使之，至遲不得晚於認股權憑證之存續期間。 (四)死亡：     已具認股行使權之認股權憑證，由繼承人自認股權人死亡日起六個月內行使認     股權，至遲不得晚於認股權憑證之存續期間。未具行使權之認股權憑證，於死     亡當日即視為放棄認股權利。 (五)受職業災害致殘疾或死亡： (1)因受職業災害致身體殘疾而無法繼續任職者，已授予之認股權憑證，於離職時，    可以行使全部之認股權利。惟該認股權利，應自離職日起或被授予認股權憑證    屆滿二年之日起（以日期較晚者為主）六個月內行使之，至遲不得晚於認股權    憑證之存續期間。 (2)因受職業災害致死亡者，已授予之認股權憑證，於死亡時，繼承人可以行使全    部之認股權利。惟該認股權利，應自死亡日起或被授予認股權憑證屆滿二年之    日起（以日期較晚者為主）六個月內行使之，至遲不得晚於認股權憑證之存續    期間。 (六)資遣或解雇：     已具認股行使權之認股權憑證，得自資遣生效日或解雇日起一個月內行使認股     權利，惟至遲不得晚於認股權憑證之存續期間。未於前述期間內行使權利者，     視同放棄認股權利。未具行使權之認股權憑證，自資遣生效日或解雇日起即視     為放棄認股權利。 (七)調職：     如認股權人主動申請調職至本公司之子公司或關係企業公司時，其認股權憑證     應比照離職方式處理。如應本公司要求而調職者，經本公司董事長或其授權之     人核定須轉任本公司國內外從屬公司之認股權人，其已授予認股權憑證之權利     義務均不受轉任之影響。 (八)認股權人或其繼承人若未能於上述期限內行使認股權者，即視為放棄認股權利。 (九)其它終止僱傭關係：     上述原因外，其它未約定之終止僱傭關係或僱傭關係調整，依本條第二項所規     定之權利期間及權利行使時程行使認股權利。 (十)其他非屬上列原因或實際依照前揭各款規定執行時必須依相關法令進行調整時，     授權董事長依實際狀況個別訂定或調整之。 (十一)放棄認股權利之認股權憑證處理方式：       對於放棄認股權利之認股權憑證，本公司將予以收回註銷不再發行。  11.其他認股條件:無。  12.履約方式:本公司以發行新股方式交付。  13.認股價格之調整: (一)本認股權憑證發行後，除本公司所發行具有普通股轉換權或認股權之各種有     價證券換發普通股股份或因員工酬勞發行新股者外，遇有本公司普通股股份     發生變動時（即包含以募集發行或以私募方式辦理現金增資、盈餘轉增資、     資本公積轉增資、公司合併或受讓他公司股份發行新股、股票分割及辦理現     金增資參與發行海外存託憑證等），認股價格依下列公式調整之（計算至新     台幣角為止，分以下四拾五入），如係因股票面額變更致已發行普通股股份     增加，於新股換發基準日調整之，但有實際繳款作業者於股款繳足日調整之     。     調整後之認股價格＝調整前認股價格×    〔已發行股數＋(每股繳款金額×新股發行股數) ÷每股時價〕÷    〔已發行股數＋新股發行股數〕     股票面額變更時     調整後之認股價格＝調整前認股價格×(股票面額變更前已發行普通股股數     ÷股票面額變更後已發行普通股股數) (1)「已發行股數」係指普通股已發行股份總數(含已辦理完成之私募普通股)，     不含已繳納之股款繳納憑證及債券換股權利證書之股數，但應扣除本公司買     回惟尚未註銷或轉讓之庫藏股股數。 (2)「每股繳款金額」如係屬無償配股或股票分割，則其繳款金額為零。 (3)本公司與他公司合併時，增資新股每股繳款金額為合併基準日前第四十五個    營業日起連續三十個營業日之本公司普通股平均收盤價。 (4)遇有調整後認股價格高於調整前認股價格時，則不予調整。 (5)調整後認股價格如低於普通股股票面額時，以普通股股票面額為認股價格。 (6)上述每股時價之訂定，應以除權基準日、訂價基準日或股票分割基準日之前    一、三、五個營業日擇一計算之普通股收盤價之簡單算術平均數為準。 (7)倘非前述所列舉之股份變動情形時，則授權董事會(長)決議調整與否。 (8)遇有須調整認股價格之情事，依上述公式調整，並經董事長核定，無須再送    董事會決議。 (二)認股權憑證發行後，本公司發放普通股現金股利時，認股價格應於除息基     準日依下列公式調整之（計算至新台幣角為止，分以下四捨五入）。     調整後之認股價格＝調整前認股價格×(1-發放普通股現金股利占每股時價之     比率) (1)上述每股時價之訂定，應以現金股息停止過戶除息公告日之前一、三、五個    營業日擇一計算本公司普通股收盤價之簡單算術平均數為準。 (2)遇有同時發放現金股利及股票股利（含盈餘轉增資及資本公積轉增資）時，則    先依現金股利金額調整認股價格後，再依股票股利金額調整認股價格。 (三)認股權憑證發行後，如遇非因庫藏股註銷之減資致普通股股份減少，於減資     基準日依下列公式計算其調整後認股價格（計算至新台幣角為止，分以下四     拾五入），如係因股票面額變更致普通股股份減少，於新股換發基準日調整     之。 (1)減資彌補虧損時    調整後認股價格＝調整前認股價格 × (減資前已發行普通股股數(註) ÷    減資後已發行普通股股數) (2)現金減資時    調整後認股價格＝〔調整前認股價格×（1-每股退還現金金額占換發新股票前最    後交易日收盤價之比率）〕×（減資前已發行普通股股數 ÷ 減資後已發行普通    股股數） (3)股票面額變更時    調整後之認股價格= 調整前認股價格×（股票面額變更前已發行普通股股數(註)    ÷股票面額變更後已發行普通股股數）    註：已發行普通股股數包括已發行普通股及私募股份之總數，並減除本公司買回    但尚未註銷或轉讓之庫藏股普通股股數。  14.行使認股權之程序: (一)認股權人除遇第九條對認股權行使之限制及依法暫停過戶期間外，得依本辦法     行使認股權利，並填具「認股請求書」，向本公司股務代理機構提出認股申請     ，於遞送時即生認股之效力，且不得申請撤銷。 (二)本公司股務代理機構受理認股之請求後，通知認股權人於期限內繳納股款至指     定銀行，認股權人未於繳納期限內繳足股款，則視同放棄認股權利。 (三)本公司股務代理機構於確認收足股款後，將員工認購之股數及員工姓名登載於     本公司股東名簿，且經認股權人出具集保帳號，並於五個營業日內以集保劃撥     方式發放之。 (四)上述普通股股票自向認股權人交付新股之日起即得上櫃(市)買賣。 (五)本公司每季至少向公司登記之主管機關申請資本額變更登記一次。  15.認股後之權利義務: 依本辦法交付之普通股新股之權利義務與本公司普通股股票相同，認股權人依本辦 法所認購之股票其相關之稅賦按當時中華民國之稅法規定辦理。  16.附有轉換、交換或認股者，其換股基準日:NA 17.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 18.其他重要約定事項: (一)認股權行使之限制     本公司所發放予員工之認股權憑證，每年度於以下期間不得行使認股權： (1)當年度股東會召開前之法定停止過戶期間。 (2)本公司無償配股停止過戶日、現金股息停止過戶日或現金增資認股停止過戶日    前十五個營業日起，至權利分派基準日止，辦理減資之減資基準日起至減資換發    股票開始交易日前一日止。 (3)「決定當年度之合併基準日之董事會」召開後至當年度合併基準日前之期間；或    「決定當年度之分割基準日之董事會」召開後至當年度分割基準日前之期間；或    「決定當年度之有償配股基準日之董事會」召開後至當年度有償配股基準日前之    期間。 (4)其它依事實發生之法定停止過戶期間。 (二)保密規定     認股權人經授予認股權憑證後，應遵守保密規定，除法令或主管機關要求外，     不得洩露被授予之認股權憑證相關內容及數量，若有違反之情事，依本辦法第　     五條第二項第二款辦理。 (三)實施細則     個別認股權人被授予認股權憑證之數量、認股權憑證之行使、認股繳款、換發     股票等事宜之相關作業及各該作業時間，將由本公司另行通知認股權人。 (四)其他重要約定事項 (1)本辦法應經董事會三分之二以上董事出席及出席董事超過二分之一之同意後通過    ，並報經主管機關申報後生效，實際發行前修改時亦同。本公司並授權董事長於    案件審查期間因應主管機關要求可修訂本發行及認股辦法，惟嗣後仍須提董事會    追認後始得發行。 (2)本辦法如有未盡事宜，悉依相關法令規定或主管機關之要求辦理。  19.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8299 | 群聯 | 6 | 6 | 5 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
