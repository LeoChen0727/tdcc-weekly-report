# INDIVIDUAL STOCK CHATGPT PACKET - 1101 台泥

## Metadata
- generated_at: 2026-09-26 22:15:56 Asia/Taipei
- stock_id: 1101
- stock_name: 台泥
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 361
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1101_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1101_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1101.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1101.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1101.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1101.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1101_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1101_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1101_latest.md?ref=main

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
- open: 25.7
- high: 25.7
- low: 25.1
- close: 25.25
- volume: 39328798
- ma5: 24.79
- ema23_primary: 24.53
- distance_to_ema23_pct: 2.94
- ma20: 24.53
- ma60: 24.17
- ma120: 24.33
- return_5d: 3.27
- return_20d: 4.77
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: 2.92
- distance_to_high_60_pct: -3.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,24.1,24.4,24.1,24.3,16839498,24.29,0.06,24.3,24.07,0.63
20260831,24.3,24.45,24.05,24.4,557094159,24.29,0.43,24.33,24.07,10.6
20260901,24.6,26.1,24.6,25.3,108834320,24.38,3.78,24.42,24.08,1.92
20260902,25.3,25.4,24.65,24.8,43527079,24.41,1.58,24.46,24.1,0.75
20260903,24.85,24.95,24.4,24.45,24047477,24.42,0.14,24.46,24.11,0.42
20260904,24.6,24.7,24.35,24.6,18895624,24.43,0.69,24.48,24.12,0.33
20260907,24.65,24.65,24.3,24.3,19462259,24.42,-0.5,24.46,24.12,0.34
20260908,24.3,24.5,24.2,24.3,16729814,24.41,-0.45,24.45,24.11,0.29
20260909,24.25,25,24.25,24.75,33714369,24.44,1.27,24.46,24.11,0.57
20260910,24.7,24.95,24.6,24.8,20276057,24.47,1.35,24.5,24.12,0.35
20260911,24.65,24.75,24.5,24.5,14583409,24.47,0.12,24.51,24.12,0.25
20260914,24.4,24.4,23.9,23.9,35778533,24.42,-2.15,24.5,24.11,0.61
20260915,24,24.05,23.8,23.8,20277886,24.37,-2.35,24.48,24.1,0.35
20260916,23.85,24.05,23.75,24.05,18247875,24.35,-1.21,24.48,24.1,0.31
20260917,24.1,24.6,24.05,24.45,23063655,24.35,0.39,24.46,24.1,0.4
20260918,24.5,24.55,24.15,24.35,22255754,24.35,-0.02,24.44,24.1,0.39
20260921,24.3,24.3,24.05,24.15,12445836,24.34,-0.77,24.41,24.1,0.23
20260922,24.35,24.8,24.15,24.55,29414044,24.35,0.8,24.41,24.1,0.54
20260923,24.85,26.1,24.65,25.65,130648955,24.46,4.85,24.48,24.13,2.19
20260924,25.7,25.7,25.1,25.25,39328798,24.53,2.94,24.53,24.17,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 55.1
- over_600_ratio: 53.23
- over_800_ratio: 52.06
- over_1000_ratio: 51.11
- over_400_change_1w: 0.32
- over_800_change_1w: 0.34
- over_1000_change_1w: 0.37
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,54.98,0.2,51.94,0.19,50.83,0.21,1,True,True
20260717,54.93,-0.05,51.92,-0.02,50.88,0.05,2,False,True
20260724,55.42,0.49,52.37,0.45,51.34,0.46,3,True,True
20260731,55.95,0.53,52.89,0.52,51.9,0.56,4,True,True
20260807,56.09,0.14,53.04,0.15,52.06,0.16,5,True,True
20260814,56.34,0.25,53.37,0.33,52.35,0.29,6,True,True
20260821,56.54,0.2,53.68,0.31,52.69,0.34,7,True,True
20260828,56.29,-0.25,53.4,-0.28,52.39,-0.3,0,False,False
20260904,55.47,-0.82,52.53,-0.87,51.55,-0.84,0,False,False
20260911,55.25,-0.22,52.36,-0.17,51.36,-0.19,0,False,False
20260918,54.78,-0.47,51.72,-0.64,50.74,-0.62,0,False,False
20260924,55.1,0.32,52.06,0.34,51.11,0.37,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1101 | 台泥 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | no_signal | stale_signal | 1.併購種類(如合併、分割、收購或股份受讓): 收購 2.事實發生日:115/9/22 3.參與併購公司名稱(如合併另一方公司、分割新設公司、收購或受讓股份標的公司之 名稱: Private Joint-Stock Company "Ivano-Frankivskcement"、 "Ivano-Frankivsk-Dakh" LLC、"KRU Gips" LLC 及 "KRU Mix" LLC 及其等之子公司（以下合稱「標的公司」或「BLUE」） 4.交易相對人(如合併另一方公司、分割讓與他公司、收購或受讓股份之交易對象): CEMINWEST SA、PRENTERS ENGINEERING LIMITED、LARSTONE LIMITED、 LIEBSTEN HOLDINGS LIMITED 及 PERMIXO LIMITED 5.交易相對人為關係人:否 6.交易相對人與公司之關係(本公司轉投資持股達XX%之被投資公司)，並說明選定 收購、受讓他公司股份之對象為關係企業或關係人之原因及是否不影響股東權益: 不適用 7.併購目的及條件，包括併購理由、對價條件及支付時點(註七): 為加速本集團於歐洲市場之戰略佈局，並提升全球競爭力。 8.併購後預計產生之效益: 鞏固歐洲市場地位，為集團創造長期價值。 9.併購對每股淨值及每股盈餘之影響: 如達成併購目的，合理預期對本公司每股淨值及每股盈餘將有正面之助益。 10.併購之對價種類及資金來源: 由本公司或子公司TCC Dutch評估，以股東借款或增資方式， 提供TCC EMEA收購 BLUE全部或部分股權所需資金。 11.換股比例及其計算依據: 本公司預計透過 TCC Dutch Holdings B.V.（以下稱「TCC Dutch」）之 全資子公司 TCC Group  EMEA Holdings B.V.（以下稱「TCC EMEA」） 以其企業價值(Enterprise Value)不超過歐元7.5億元（下同）額度內 取得BLUE 100%之股權。實際支付之交易金額，將於交割時依據最近期 財務報表，視其淨營運資金（Net Working Capital）及淨負債 (Net Debt)等項目進行常規之結算調整（以下稱「本股份收購案」）。 12.本次交易會計師、律師或證券承銷商出具非合理性意見:否 13.會計師或律師事務所名稱或證券承銷商公司名稱: 國富浩華聯合會計師事務所 14.會計師或律師姓名: 吳孟達會計師 15.會計師或律師開業證書字號: 台財證登(六)第三六二二號 16.獨立專家就本次併購換股比例、配發股東之現金或其他財產之合理性意見書內容 (一、包含公開收購價格訂定所採用之方法、原則或計算方式及與國際慣用之市價法 、成本法及現金流量折現法之比較。二、被收購公司與已上市櫃同業之財務狀況 、獲利情形及本益比之比較情形。三、公開收購價格若參考鑑價機構之鑑價報告者 ，應說明該鑑價報告內容及結論。四、收購人融資償還計畫若係以被收購公司或合 併後存續公司之資產或股份為擔保者，應說明對被收購公司或合併後存續公司財務 業務健全性之影響評估)(註七): 經本會計師考量可&#63870;化之財務&#63849;字及市場客觀資料，獨立財務專家採收益法 為評價主要方法，並將收益法之隱含乘數對比市場法之可類比公司法之乘數 ，作為本案支持收益法運算之結果。本會計師經複核其價值評估結果及執行 必要之調整後認為，BLUE 100%具控制權但不具市場流動性之整體企業價值 約介於歐元697,878仟元至804,836仟元間，本案擬以不超過歐元7.5億元之 企業價值為基準，並依最終股權買賣合約所約定基準日有關淨負債及營運資金 進行調整後之價格取得BLUE 全部股權，其價格應無不合理之處。 17.預定完成日程(註七): 擬議交易的完成仍需相關機關批准，包括但不限於台灣及烏克蘭。 18.既存或新設公司承受消滅(或分割)公司權利義務相關事項(註二): 不適用 19.參與合併公司之基本資料(註三): BLUE是烏克蘭第二大水泥公司，營運狀況良好且具備地利優勢。 20.分割之相關事項(含預定讓與既存公司或新設公司之營業、資產之評價價值；被 分割公司或其股東所取得股份之總數、種類及數量；被分割公司資本減少時，其資 本減少有關事項)(註：若非分割公告時，則不適用): 不適用 21.併購股份未來移轉之條件及限制: 無 22.併購完成後之計畫(包含一、繼續經營公司業務之意願及計畫內容。二、是否發生 解散、下市(櫃)、重大變更組織、資本、業務計畫、財務及生產、對公司重要人員 、資產之安排或運用，或其他任何影響公司股東權益之重大事項): 維持BLUE原有業務並繼續經營。 23.其他重要約定事項: 無 24.其他與併購相關之重大事項: 維持BLUE原有業務並繼續經營。 25.本次交易，董事有無異議:否 26.併購交易中涉及利害關係董事資訊(自然人董事姓名或法人董事名稱暨其代表人姓名 、其自身或其代表之法人有利害關係之重要內容(包括但不限於實際或預計投資其他 參加併購公司之方式、持股比率、交易價格、是否參與併購公司之經營及其他投資條件 等情形)、其應迴避或不迴避理由、迴避情形、贊成或反對併購決議之理由)(註七): 無 27.是否涉及營運模式變更:否 28.營運模式變更說明(註四): 不適用 29.過去一年及預計未來一年內與交易相對人交易情形(註五): 不適用 30.資金來源(註五): 由本公司或子公司TCC Dutch評估，以股東借款或增資方式， 提供其子公司TCC EMEA收購 BLUE全部或部分股權所需資金。 相關程序將依當地應適用法律程序辦理。 31.其他敘明事項(註六): 本公司保留引入超國家金融基金作為共同投資者的靈活性，以直接或間接收購 目標公司部分已發行股本。 TCC 將維持最終控制權。 註二、既存或新設公司承受消滅公司權利義務相關事項，包括庫藏股及已發行具有股權性質有 　　　價證券之處理原則。 註三：參與合併公司之基本資料包括公司名稱及所營業務之主要內容。 註四：倘涉營運模式變更，請於欄位敘明包括營業範圍變更、產品線擴充/縮減、製程調整、產業 　　　水平/垂直整合，或其他涉及營運架構調整事項。 註五：非屬私募資金用以併購案件者，得填寫不適用。 註六：若本案成就前，尚需經國內、外主管機關(如:投審會、公平交易委員會、反壟斷局或其他單位)核准或許可者，應予敘明相關事項。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1101 | 台泥 | 3 | 1 | 3 | 5 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1101 | 台泥 | 27 | 0 | 6704130.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
