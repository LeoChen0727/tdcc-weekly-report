# INDIVIDUAL STOCK CHATGPT PACKET - 4123 晟德

## Metadata
- generated_at: 2026-06-25 22:23:45 Asia/Taipei
- stock_id: 4123
- stock_name: 晟德
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 155
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4123_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4123_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4123_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4123_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4123_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4123_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4123_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4123.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4123.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4123.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4123.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4123_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4123_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4123_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260624
- open: 37.1
- high: 38.3
- low: 37.1
- close: 38.25
- volume: 3423000
- ma5: 37.37
- ema23_primary: 37.85
- distance_to_ema23_pct: 1.06
- ma20: 37.79
- ma60: 38.88
- ma120: 40.34
- return_5d: 3.24
- return_20d: 1.46
- volume_ratio: 2.69
- distance_to_ma20_pct_auxiliary: 1.21
- distance_to_high_60_pct: -11.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,37.7,37.8,37.25,37.25,38000,38.61,-3.52,38.33,40.94,0.02
20260528,37.2,38.15,37.15,37.8,38000,38.54,-1.92,38.27,40.81,0.02
20260529,38,38.3,37.85,38.25,38000,38.52,-0.69,38.23,40.7,0.02
20260601,38.55,38.55,37.9,38.4,38000,38.51,-0.28,38.21,40.52,0.02
20260602,38.35,38.35,38.05,38.35,38,38.49,-0.37,38.2,40.36,0
20260603,38.4,38.4,38.1,38.35,38000,38.48,-0.34,38.22,40.18,0.02
20260604,38.45,38.8,38.4,38.45,39000,38.48,-0.08,38.23,40.08,0.03
20260605,38.5,39.4,38.5,38.8,39000,38.51,0.76,38.27,40,0.03
20260608,37.35,38.15,36.85,37.9,2544000,38.46,-1.45,38.26,39.89,1.91
20260609,38.15,38.65,37.75,37.8,2378000,38.4,-1.57,38.23,39.78,1.75
20260610,37.85,38.3,37.65,37.95,2136000,38.36,-1.08,38.21,39.68,1.55
20260611,38,38,37.1,37.35,2204000,38.28,-2.43,38.1,39.56,2.14
20260612,37.7,37.85,37.5,37.65,1334000,38.23,-1.51,38.07,39.45,1.49
20260615,37.85,37.9,37.6,37.65,1266000,38.18,-1.38,38.06,39.33,1.48
20260616,37.7,37.7,37,37.05,2730000,38.08,-2.72,38.01,39.24,3.05
20260617,37.1,37.45,36.9,37.15,1327000,38.01,-2.25,37.96,39.15,1.47
20260618,37.2,37.35,37,37.2,1686000,37.94,-1.95,37.88,39.09,1.87
20260622,37.15,37.15,36.8,36.95,2511000,37.86,-2.4,37.8,39.01,2.45
20260623,37,37.3,36.85,37.3,1627000,37.81,-1.35,37.77,38.93,1.48
20260624,37.1,38.3,37.1,38.25,3423000,37.85,1.06,37.79,38.88,2.69
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 57.17
- over_600_ratio: 54.51
- over_800_ratio: 52.33
- over_1000_ratio: 50.44
- over_400_change_1w: -0.31
- over_800_change_1w: 0
- over_1000_change_1w: -0.11
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.41,,53.15,,51.27,,0,False,False
20260508,58.29,-0.12,53.17,0.02,51.19,-0.08,1,False,True
20260515,57.84,-0.45,53.03,-0.14,51.27,0.08,2,False,True
20260522,57.76,-0.08,52.83,-0.2,51.08,-0.19,3,False,False
20260529,57.68,-0.08,52.64,-0.19,50.77,-0.31,0,False,False
20260605,57.58,-0.1,52.52,-0.12,50.63,-0.14,1,False,False
20260612,57.48,-0.1,52.33,-0.19,50.55,-0.08,0,False,False
20260618,57.17,-0.31,52.33,0,50.44,-0.11,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 4123 | 晟德 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | 1.董事會決議日期:115/06/23 2.發行期間:於主管機關申報生效通知到達之日起二年內，得視實際需要， 一次或分次發行，實際發行日期授權董事長訂定之。 3.認股權人資格條件: (一)以認股資格基準日當日之本公司及國內外子公司(所稱「子公司」係依金融監督 管理委員會民國107年12月27日金管證發字第1070121068號令規定)正式編制內全職 員工為限(所稱「全職員工」係指受雇從事工作每月達公司規定時數，獲致工資之員工 而言。)，認股資格基準日授權董事長決定。 (二)實際得為認股權人之員工及得認股之數量，將參酌年資、職級、工作績效、過去及 預期整體貢獻或特殊功績及發展潛力等因素擬定分配標準，由董事長核定後依下列程序 辦理： 1.本公司經理人或兼任本公司董事之員工，應先經本公司薪資報酬委員會同意後，再提 本公司董事會決議；子公司員工若兼具本公司經理人或本公司董事身分者，亦須比照 前述程序，經本公司薪資報酬委員會同意及本公司董事會決議。 2.第1款所述以外之本公司及子公司員工，應先經本公司審計委員會同意，再提本公司 董事會決議。 (三)依「發行人募集與發行有價證券處理準則」第五十六條之一第一項規定，發行員工 認股權憑證累計給予單一認股權人得認購股數，加計認股權人累計取得限制員工權利 新股之合計數，不得超過本公司已發行股份總數之千分之三，且加計本公司依第五十六 條第一項規定發行員工認股權憑證累計給予單一認股權人得認購股數，不得超過已發行 股份總數之百分之一。 4.員工認股權憑證之發行單位總數:6,300單位。 5.每單位認股權憑證得認購之股數:1,000股。 6.因認股權行使而須發行之新股總數或依證券交易法第二十八條之二 規定須買回之股數:6,300,000股。 7.認股價格:以發行當日本公司普通股收盤價格為認股價格。 若當日收盤價格低於面額時，則以普通股股票面額為認股價格。 8.認股權利期間: (1)本認股權憑證之存續期間自發行日起四年，此一期間內不得轉讓、質押、贈予他人 或作其他方式之處分，但遇認股權人死亡其繼承者不在此限。屆滿後，未行使之員工 認股權憑證視同放棄，認股權人不得再行主張其認股權利。 (2)認股權人自被授予員工認股權憑證屆滿二年後，可依下列認股權憑證授予期間及比例 行使認股權： 認股權憑證授予期間   可行使認股比例(累計)      屆滿 2 年              50%      屆滿 3 年             100% (3)認股權人自公司授予員工認股權憑證後，遇有違反勞動契約或工作規則等重大過失 ，或違反本辦法規定，或績效未達約定之目標者，本公司得依情節之輕重撤銷其全部或 部分尚未具行使權之員工認股權憑證，並予以收回註銷。 9.認購股份之種類:本公司普通股股票。 10.員工離職或發生繼承時之處理方式: 1.離職(含自願離職、解聘、免職及資遣)： (1)已具行使權之認股權憑證，應自離職日起一個月內行使認股權利，並以認股權憑證 存續期間為限，逾期未行使則視同放棄認股權利。但若遇有本辦法所定不得行使認股 權利者，其行使期間自得行使日起，按無法行使之日數順延之，惟不得逾本認股權憑證 之存續期間。 (2)未具行使權之認股權憑證，於離職當日起即視為放棄認股權利。 2.調職： 因營運所需，經由公司核定指派轉任為集團關係企業或其他公司之認股權人，其已授予 認股權憑證之權利不受轉任之影響。 3.留職停薪： (1)已具行使權之認股權憑證，得自留職停薪生效日起一個月內行使認股權利，並以 認股權憑證存續期間為限，逾期未行使則視同放棄認股權利。但若遇有本辦法所定不得 行使認股權利者，其行使期間自得行使日起，按無法行使之日數順延之，惟不得逾 本認股權憑證之存續期間。 (2)未具行使權利之認股權憑證，自復職日起依停職時間往後遞延回復其權利， 惟認股權行使期間仍以本認股權憑證存續期間為限，若逾本認股權憑證存續期間者， 視同放棄其認股權利。 4.退休： (1)已具行使權之認股權憑證，應自退休日起一個月內行使認股權利，並以認股權憑證 存續期間為限，逾期未行使則視同放棄認股權利。但若遇有本辦法所定不得行使認股 權利者，其行使期間自得行使日起，按無法行使之日數順延之，惟不得逾本認股權憑證 之存續期間。 (2)未具行使權之認股權憑證，於退休日起即視為放棄認股權利。 5.一般死亡： (1)已具行使權之認股權憑證，由繼承人自認股權人死亡日起一年內行使之， 並以認股權憑證存續期間為限，逾期未行使則視同放棄認股權利。 (2)未具行使權之認股權憑證，於死亡當日即失效。 6.因受職業災害殘疾或死亡： (1)因受職業災害致身體殘疾而無法繼續任職者 已授予之認股權憑證，於離職時，可以行使全部之認股權利，除仍應於被授予認股權 憑證屆滿二年後方得行使外，不受本條第二項有關時程屆滿可行使認股比例之限制。 惟該認股權利，應自離職日起或被授予認股權憑證屆滿二年之日起（以日期較晚者為主 ）一年內行使之，但仍不得逾本認股權憑證之存續期間。 (2)因受職業災害或因公出差致死亡者 已授予之認股權憑證，於死亡時，繼承人可以行使全部之認股權利，除仍應於被授予 認股權憑證屆滿二年後方得行使外，不受本條第二項有關時程屆滿可行使認股比例之 限制。惟該認股權利，應自死亡日起或被授予認股權憑證屆滿二年之日起（以日期較晚 者為主）一年內行使之，但仍不得逾本認股權憑證之存續期間。 7.其他： 非屬上列原因之僱傭關係終止/調整，或實際依照前揭各款規定執行時，需依照相關法令 進行調整時，授權董事長依實際狀況個別訂定或調整之。 8.認股權人或其繼承人若未能於上述期限內行使認股權者，即視為放棄認股權利。 11.其他認股條件: 對於放棄認股權利或經本公司撤銷之本員工認股權憑證，本公司將予以註銷不再發行。 12.履約方式:以本公司發行新股交付。 13.認股價格之調整: (一)本認股權憑證發行後，除本公司所發行具有普通股轉換權或認股權之各種有價證券 換發普通股股份或因員工酬勞發行新股者外，遇有本公司普通股股份發生變動時(包含 但不限於辦理私募、現金增資、盈餘轉增資、資本公積轉增資、公司合併或受讓他公司 股份發行新股、股票分割及現金增資參與發行海外存託憑證等)，認股價格應依下列 公式，於新股發行除權基準日調整之（計算至新台幣角為止，分以下四捨五入）。 如係因股票面額變更致已發行普通股股份增加，於新股換發基準日調整之，但有實際 繳款作業者於股款繳足日調整之： 調整後認股價格 ＝ 調整前認股價格 ×〔已發行股數＋(每股繳款額×新股發行股數） ／每股時價〕／（已發行股數＋新股發行股數）。 股票面額變更時： 調整後之認股價格 ＝ 調整前認股價格 ×（股票面額變更前已發行普通股股數/ 股票面額變更後已發行普通股股數） 註1.如為股票分割則為分割基準日調整；如為合併或受讓增資則於合併或受讓基準日 調整；如係採詢價圈購辦理之現金增資或現金增資參與發行海外存託憑證，因無除權 基準日，則於股款繳足日調整；如係採私募方式辦理之現金增資，則於私募有價證券 交付日調整。 註2.「已發行股數」係指普通股已發行股份總數(含已私募股份)，並應減除本公司買回 惟尚未註銷或轉讓之庫藏股股數。 註3.「每股繳款額」如係無償配股或股票分割，則其繳款額為零。 註4.與他公司合併或受讓時，增資新股每股繳款金額為合併或受讓基準日前第四十五個 營業日起，連續三十個營業日本公司普通股平均收盤價。 註5.「每股時價」之訂定，應以除權基準日、訂價基準日、股票合併及分割基準日或 私募有價證券交付日前一、三、五個營業日擇一計算之本公司普通股收盤價之簡單算術 平均數為準。 註6.遇有調整後認股價格高於調整前認股價格時，則不予調整。 (二)本認股權憑證發行後，如遇本公司配發普通股現金股利時，認股價格應於除息 基準日按下列公式調整之(計算至新台幣角為止，分以下四捨五入，向下調整，向上則 不予調整)： 調整後之認股價格 ＝ 調整前認股價格 × (1-發放普通股現金股利占每股時價之比率) 註：上述每股時價之訂定，應以現金股息停止過戶除息公告日之前一、三、五個營業日 擇一計算本公司普通股收盤價之簡單算術平均數為準。 (三)本認股權憑證發行後，如遇非因庫藏股註銷之減資致普通股股份減少，則依下列 公式計算調整認股價格(計算至新台幣角為止，分以下四捨五入，向下調整，向上則 不予調整)，於減資基準日調整之。如係因股票面額變更致普通股股份減少，於新股 換發基準日調整之。 1.減資彌補虧損時： 調整後之認股價格 ＝ 調整前認股價格 × (減資前已發行普通股股數/減資後已發行 普通股股數)。 2.現金減資時： 調整後之認股價格 ＝ 〔調整前認股價格 ×（1-每股退還現金金額占換發新股票前 最後交易日收盤價之比率）〕 × (減資前已發行普通股股數/減資後已發行普通股 股數)。 3.股票面額變更時： 調整後之認股價格 ＝ 調整前認股價格 ×（股票面額變更前已發行普通股股數／ 股票面額變更後已發行普通股股數）。 註：已發行股數係指普通股已發行股份總數(包括募集發行與私募股份)，並減除本公司 買回惟尚未註銷或轉讓之庫藏股股數。 (四)調整後之認股價格如低於普通股股票面額時，以普通股股票面額為認股價格。 (五)遇有同時發放現金股利及股票股利(含盈餘轉增資及資本公積轉增資)時，則先調整 現金股利後，再依股票股利金額調整認購價格。 (六)遇有須調整認股價格之情事，授權董事長依上述公式調整之。 14.行使認股權之程序: (一)認股權人除於下列期間不得行使認股權外，得依本辦法所訂之權利期間行使認股 權利，並填具「認股請求書」向本公司提出申請。 1.當年度股東會召開前之法定停止過戶期間。 2.發行無償配股停止過戶日、現金股息停止過戶日或現金增資認股停止過戶日前十五個 營業日起，至權利分派基準日止。 3.辦理減資之減資基準日起至減資換發股票開始交易日前一日止。 4.決定合併基準日之董事會召開後至合併基準日止之期間；或決定分割基準日之董事會 召開後至分割基準日止之期間。 5.其他依事實發生之法定停止過戶期間。 (二)本公司受理認股申請之請求後，通知認股權人於期限內繳納股款至指定銀行帳戶， 認股權人一經繳款後，即不得撤銷認股繳款，逾期未繳款者，則視為未認購。 (三)繳款後，認股權人需於當天將繳款證明文件交付本公司，本公司確認認股權人繳足 股款後，將相關資料交付股務代理機構。 (四)本公司股務代理機構於確認相關資料後，將員工認購之股數及員工姓名登載於 本公司股東名簿，並於五個營業日內以集保劃撥方式發給本公司新發行之普通股股票。 上述新發行之普通股股票自向認股權人交付之日起上櫃買賣。 (五)本公司依本辦法發行新股交付予認股權人，將每季至少一次向主管機關申請資本額 變更登記。惟如遇無償配股基準日或現金增資認股除權基準日時，得調整變更登記時間 。 15.認股後之權利義務: 本公司因認股權行使所發行之普通股，其權利義務與本公司已發行普通股相同。 16.附有轉換、交換或認股者，其換股基準日:NA 17.附有轉換、交換或認股者，對股權可能稀釋情形:不適用。 18.其他重要約定事項: (1)稅賦：認股權人依本辦法所認購之股票及其相關稅賦，均按當時中華民國之稅法 規定辦理。 (2)保密規定：認股權人經授予認股權憑證後，應恪遵本公司保密規定，除法令或 主管機關要求外，不得探詢他人或洩露被授予之認股權憑證相關內容及數量。若有違反 之情事，本公司有權就其尚未具行使權之認股權憑證予以收回並註銷。 (3)實施細則：個別認股權人被授予之認股權憑證數量、認股權行使條件、實際得行使 認股權數量、認股繳款、撥付股票等事宜之相關程序及作業事項，將由本公司另行通知 認股權人。 19.其他應敘明事項: (一)本辦法經董事會三分之二以上董事出席及出席董事過半數同意，並報經主管機關 核准後生效，發行前修正時亦同。若於送件審核過程中，因主管機關之要求而須修改時 ，授權董事長先行修正，嗣後再提報董事會追認後始得發行。 (二)本辦法如有未盡事宜，悉依相關法令規定辦理。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 4123 | 晟德 | 1 | 1 | 1 | 1 | 3 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
