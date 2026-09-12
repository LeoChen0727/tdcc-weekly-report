# INDIVIDUAL STOCK CHATGPT PACKET - 2392 正崴

## Metadata
- generated_at: 2026-09-12 15:42:43 Asia/Taipei
- stock_id: 2392
- stock_name: 正崴
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 351
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2392_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2392_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2392_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2392_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2392_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2392_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2392_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2392.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2392.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2392.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2392.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2392_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2392_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2392_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260911
- open: 42.3
- high: 43.15
- low: 41
- close: 42.3
- volume: 2532212
- ma5: 43.13
- ema23_primary: 42.78
- distance_to_ema23_pct: -1.12
- ma20: 43.77
- ma60: 39.36
- ma120: 38.4
- return_5d: -7.24
- return_20d: -1.74
- volume_ratio: 0.45
- distance_to_ma20_pct_auxiliary: -3.37
- distance_to_high_60_pct: -12.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,43.25,44.75,42.25,43.3,20622343,37.95,14.11,36.86,38.06,5.82
20260818,43,43.6,40.2,40.3,7050849,38.14,5.65,37.1,38.1,1.83
20260819,39.7,41.65,39.05,41.05,3782138,38.39,6.94,37.36,38.14,0.95
20260820,40.35,41.5,40.2,40.6,2407598,38.57,5.26,37.58,38.17,0.6
20260821,40.4,41.9,40.1,41.6,2545941,38.82,7.15,37.88,38.24,0.62
20260824,41.45,45.2,41.45,44.25,7794623,39.27,12.67,38.3,38.35,1.76
20260825,43.7,45.95,43.2,45.1,5584666,39.76,13.43,38.82,38.45,1.21
20260826,44.8,45.3,43.8,45.15,5149062,40.21,12.29,39.4,38.5,1.1
20260827,45.15,48.6,44.85,46.65,8847109,40.75,14.49,40.09,38.58,1.76
20260828,47.05,47.2,44.1,44.5,7275128,41.06,8.38,40.63,38.59,1.37
20260831,44.35,45.85,43.7,45,14226070,41.39,8.73,41.16,38.64,2.38
20260901,45.8,47.95,45.2,45.9,5269563,41.76,9.9,41.72,38.73,0.85
20260902,45.5,46.3,45.05,45.5,2780697,42.07,8.14,42.14,38.83,0.45
20260903,46.25,47.65,45.35,45.35,4625829,42.35,7.09,42.54,38.94,0.73
20260904,45.6,46,44.55,45.6,3267943,42.62,7,42.97,39.07,0.51
20260907,46.2,46.3,44.3,44.35,3278504,42.76,3.71,43.29,39.17,0.5
20260908,44.4,45,42.6,42.8,3507000,42.77,0.08,43.45,39.23,0.54
20260909,43.1,43.1,42.3,42.8,1690380,42.77,0.07,43.6,39.27,0.26
20260910,42.5,43.75,42.5,43.4,1572885,42.82,1.35,43.81,39.33,0.25
20260911,42.3,43.15,41,42.3,2532212,42.78,-1.12,43.77,39.36,0.45
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 50.77
- over_600_ratio: 48.43
- over_800_ratio: 47.48
- over_1000_ratio: 46.44
- over_400_change_1w: -0.11
- over_800_change_1w: -0.69
- over_1000_change_1w: -0.52
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,48.68,0.21,45.24,0.01,44.22,0.34,6,False,True
20260703,48.49,-0.19,45.12,-0.12,44.13,-0.09,0,False,False
20260709,48.16,-0.33,44.95,-0.17,43.96,-0.17,0,False,False
20260717,48.24,0.08,45.02,0.07,44.19,0.23,1,True,True
20260724,47.97,-0.27,44.9,-0.12,43.89,-0.3,0,False,False
20260731,47.65,-0.32,44.4,-0.5,43.2,-0.69,0,False,False
20260807,48.2,0.55,44.83,0.43,43.63,0.43,1,True,True
20260814,49.18,0.98,45.98,1.15,44.41,0.78,2,True,True
20260821,49.96,0.78,47.19,1.21,45.66,1.25,3,True,True
20260828,51.2,1.24,48.4,1.21,47.05,1.39,4,True,True
20260904,50.88,-0.32,48.17,-0.23,46.96,-0.09,0,False,False
20260911,50.77,-0.11,47.48,-0.69,46.44,-0.52,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2392 | 正崴 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.重要子公司、第七條第三項視同上市公司之子公司或擬於海外證券市場申請掛牌之子 公司名稱:森崴能源股份有限公司、富崴能源股份有限公司、 SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION 2.發生緣由(降低持股(或出資額)比例或喪失控制力): 降低持股及喪失控制力 3.降低持股(或出資額)比例之方式(請分別列示各次發生日期、發生原因、方式、降低持 股比例、交易數量、每單位價格及交易總金額): 一、森崴能源股份有限公司(下稱森崴公司) (1)於民國113年3月至9月間，持有森崴公司發行之可轉換公司債的 債券投資人請求轉換森崴公司普通股，致富崴國際投資股份有限公司 (下稱富崴投資公司)及勁永國際股份有限公司(下稱勁永公司) 持股比例分別減少0.33%及1.80%。 (2)富崴投資公司及崴強科技股份有限公司(下稱崴強公司) 於民國114年3月參與森崴公司現金增資，因森崴公司保留10% 供員工認股及保留10%供公開承銷，致富崴投資公司、勁永公司 及崴強公司持股比例分別減少0.30%、減少8.34%及增加6.67%。 (3)本公司於民國115年8月31日董事會決議通過參與公開收購應賣方式， 富崴投資、勁永公司及崴強公司以每股新台幣0.05元分別出售持有之 森崴公司普通股18,647,921股、102,951,145股及18,331,519股， 持股比例分別減少6.79%、37.49%及6.67%， 交易總金額為新台幣6,997仟元(不考慮相關稅負)。 二、本公司透過前述第一項第3點之交易喪失對森崴公司之控制力， 亦間接喪失對森崴公司之子公司富崴能源股份有限公司及 SHINFOX FAR EAST COMPANY PTE LTD暨孫公司 SFE HERCULES COMPANY CORPORATION之控制力， 持股比例分別減少100%、67%及100%。 4.喪失控制力之方式(請列示發生日期、發生原因及方式): 本公司董事會於民國115年8月31日決議透過參與公開收購應賣方式 處分森崴能源股份有限公司普通股，出售股數合計139,930,585股。 5.股權(或出資額)受讓對象或所洽特定對象(請分別列示各次交易對象): 一、森崴能源股份有限公司(下稱森崴公司) (1)係債券投資人請求轉換森崴公司普通股，無特定受讓對象 (2)係森崴公司現金增資，無特定受讓對象 (3)股權受讓對象為公開收購人為胡正杰先生 二、富崴能源股份有限公司、SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION 係透過上述第一項第3點交易方式喪失控制力，故不適用。 6.與交易對象之關係(請分別列示各次交易對象與公司之關係): 一、森崴能源股份有限公司(下稱森崴公司) (1)係債券投資人請求轉換森崴公司普通股，無特定受讓對象且非關係人 (2)係森崴公司現金增資，無特定受讓對象且非關係人 (3)股權受讓對象為公開收購人為胡正杰先生且非關係人 二、富崴能源股份有限公司、SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION係透過上述 第一項第3點交易方式喪失控制力，故不適用。 7.處分利益(或損失)(請分別列示各次處分損益)(若無處分損益請填寫不適用): 一、森崴能源股份有限公司(下稱森崴公司) (1)係債券投資人請求轉換森崴公司普通股，故不適用 (2)係森崴公司現金增資，故不適用 (3)依本公司民國115年6月30日經會計師核閱後合併報表為基礎， 本公司合併處分損益為新台幣2,057,542仟元(不考慮稅負影響)， 實際處分損益依民國115年9月30日經會計師核閱後合併報表為主。 二、富崴能源股份有限公司、SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION係透過上述 第一項第3點交易方式喪失控制力，故不適用。 8.迄目前為止(含本次交易)，對重要子公司、第七條第三項視同上市公司之子公司或擬 於海外證券市場申請掛牌之子公司累積降低持股比例: 一、森崴能源股份有限公司：本公司合併累積降低持股比例為55.05% 二、富崴能源股份有限公司、SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION 累積持股比例分別減少100%、67%及100% 9.迄目前為止(含本次交易)，對重要子公司、第七條第三項視同上市公司之子公司或擬 於海外證券市場申請掛牌之子公司持股比例: 一、森崴能源股份有限公司：本公司合併持股比例為1.22% 二、富崴能源股份有限公司、SHINFOX FAR EAST COMPANY PTE LTD 及SFE HERCULES COMPANY CORPORATION持股比例皆為0% 10.獨立專家姓名及其就歷次價格合理性之意見: 吳宏一會計師，以每股新台幣0.05元應賣之交易價格尚屬合理 11.獨立專家姓名及其就降低持股或喪失控制力對上市公司股東權益影響之意見: 吳宏一會計師， 本次交易對本公司股東權益屬正面影響，尚不致造成重大不利影響。 12.是否影響母公司繼續上市:否 13.審計委員會決議日期:115/08/31 14.審計委員會決議內容:全體出席委員一致同意照案通過。 15.董事會決議日期:115/08/31 16.董事會決議內容:全體出席董事一致同意照案通過。 17.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2392 | 正崴 | 5 | 5 | 5 | 7 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2392 | 正崴 | 25 | 0 | 1051170.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
