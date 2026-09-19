# INDIVIDUAL STOCK CHATGPT PACKET - 3717 聯嘉投控

## Metadata
- generated_at: 2026-09-19 22:16:40 Asia/Taipei
- stock_id: 3717
- stock_name: 聯嘉投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 266
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3717_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3717_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3717.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3717.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3717.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3717.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3717_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3717_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3717_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
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
- date: 20260918
- open: 23.3
- high: 25.15
- low: 23.05
- close: 25.1
- volume: 16980049
- ma5: 22.41
- ema23_primary: 22.34
- distance_to_ema23_pct: 12.35
- ma20: 22.27
- ma60: 23.29
- ma120: 22.69
- return_5d: 19.24
- return_20d: 12.81
- volume_ratio: 8.15
- distance_to_ma20_pct_auxiliary: 12.68
- distance_to_high_60_pct: -20.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,22.5,22.75,22.15,22.45,1300568,22.68,-1.03,22.41,23.19,0.53
20260825,22.5,22.75,22.05,22.75,742783,22.69,0.27,22.48,23.2,0.31
20260826,22.7,23.1,22.7,22.85,945677,22.7,0.65,22.61,23.2,0.43
20260827,22.9,23.4,22.65,23,1356428,22.73,1.2,22.74,23.21,0.62
20260828,23.25,23.55,23,23.25,2126255,22.77,2.1,22.8,23.21,0.99
20260831,23.2,23.3,22.65,22.65,1230226,22.76,-0.49,22.79,23.21,0.59
20260901,22.7,22.8,22.15,22.3,1627170,22.72,-1.86,22.75,23.21,0.78
20260902,22.3,22.5,21.95,22.35,827774,22.69,-1.5,22.71,23.23,0.41
20260903,22.4,22.95,22.05,22.05,1404156,22.64,-2.6,22.67,23.24,0.71
20260904,22.6,22.6,22.05,22.3,907714,22.61,-1.37,22.58,23.27,0.6
20260907,22.35,22.4,21.75,21.85,2038372,22.55,-3.09,22.5,23.3,1.44
20260908,21.95,21.95,21.3,21.4,1473154,22.45,-4.68,22.43,23.32,1.07
20260909,21.1,22.3,21.1,21.75,1183682,22.39,-2.87,22.37,23.31,0.87
20260910,21.9,21.9,21.2,21.45,941489,22.31,-3.87,22.31,23.31,0.71
20260911,21.3,21.3,21,21.05,758063,22.21,-5.22,22.23,23.29,0.6
20260914,21.15,21.25,20.9,21.1,580182,22.12,-4.59,22.18,23.26,0.48
20260915,21.1,21.1,20.9,21,470577,22.02,-4.65,22.11,23.24,0.41
20260916,21,22.15,21,21.95,803152,22.02,-0.3,22.09,23.24,0.71
20260917,22,23.15,21.9,22.9,3951914,22.09,3.66,22.13,23.25,3.09
20260918,23.3,25.15,23.05,25.1,16980049,22.34,12.35,22.27,23.29,8.15
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 37.55
- over_600_ratio: 33.6
- over_800_ratio: 29.7
- over_1000_ratio: 27.95
- over_400_change_1w: 0.88
- over_800_change_1w: 1.09
- over_1000_change_1w: 1.1
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,43.16,-2.2,35.52,-1.27,33.75,-1.8,0,False,False
20260709,40.79,-2.37,33.36,-2.16,31.63,-2.12,0,False,False
20260717,39.35,-1.44,31.45,-1.91,29.28,-2.35,0,False,False
20260724,37.31,-2.04,30.98,-0.47,29.26,-0.02,0,False,False
20260731,36.84,-0.47,30.41,-0.57,28.22,-1.04,0,False,False
20260807,37.22,0.38,31.1,0.69,29.37,1.15,1,True,True
20260814,38.05,0.83,30.73,-0.37,27.8,-1.57,2,False,False
20260821,36.93,-1.12,29.89,-0.84,27.4,-0.4,0,False,False
20260828,37.42,0.49,30.37,0.48,27.49,0.09,1,True,True
20260904,36.71,-0.71,29.33,-1.04,27.24,-0.25,0,False,False
20260911,36.67,-0.04,28.61,-0.72,26.85,-0.39,1,False,False
20260918,37.55,0.88,29.7,1.09,27.95,1.1,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3717 | 聯嘉投控 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  |  | continued_overheated | 1.董事會決議變更日期:115/07/02 2.原計畫申報生效之日期:114/12/18 3.追補發行之日期:不適用 4.變動原因: a.本公司於114年11月13日董事會決議辦理114年度現金增資 發行新股暨國內第一次有擔保轉換公司債，原計畫所需資金 總額1,400,000仟元，全數用於轉投資子公司聯嘉光電股份有限 公司以償還其銀行借款。 b.本公司國內第一次有擔保轉換公司債，每張債券發行面額為 100千元整，發行總面額為700,000千元整，票面利率0%， 發行期間3年，採競價拍賣方式辦理公開承銷，每張實際發行價格 依面額之105.57%發行，實際募集總金額為738,998千元， 並於115年第一季執行完畢，其中700,000千元用於轉投資子公司 聯嘉光電股份有限公司以償還其銀行借款，餘38,998千用於充實 本公司營運資金。 c.本公司114年度現金增資發行新股因考量募集期間資本市場波 動劇烈、募資環境變化及維護公司股東權益，本公司董事長115年 06月12日依本公司114年11月13日董事會之授權，代表本公司 撤銷114年度現金增資發行新股案，向金融監督管理委員會申請 撤銷本次現金增資發行新股案，業經金融監督管理委員會 115年6月23日金管證發字第1150347329號同意在案， 並於115年07月02日董事會通過辦理計畫金額變更。 5.歷次變更前後募集資金計畫:                                          單位:新臺幣千元 計劃項目     原幕資計畫金額    變動金額   計畫變更後金額 轉投資子公司 聯嘉光電        1,400,000      (700,000)       700,000 充實營運資金       38,998             -         38,998 合計            1,438,998      (700,000)       738,998 6.預計執行進度:變更後之計畫已於115年第一季執行完畢 7.預計完成日期:變更後之計畫已於115年第一季執行完畢 8.預計可能產生效益: 本次募資計劃所需資金738,998仟元，已於115年01月20日募集 完成，其中700,000千元用於轉投資子公司聯嘉光電股份有限 公司以償還其銀行借款，餘38,998千用於充實本公司營運資金 ，皆於115年第一季執行完畢。本公司本次募集資金轉投資 子公司聯嘉光電以償還其銀行借款，可減少利息支出，並可提升 償債能力，若以聯嘉光電擬償還銀行借款之利率設算，預估115 年度可節省之利息支出約15,443千元，後續可節省之年度 利息支出約18,740千元。 9.與原預計效益產生之差異: 本公司計畫變更後用途仍為轉投資子公司聯嘉光電股份有限公司 以償還其銀行借款，故與原預計效益並無重大差異，然因計畫 變更後之金額減少，故可節省之利息支出亦同步減少，惟仍有 強化財務結構及提升償債能力，以及節省利息支出，減輕財務 負擔之效益。 10.本次變更對股東權益之影響: 本次辦理計畫金額變更，可避免股本過度擴張顧及股東權益， 後續再依營運資金需求情形評估辦理增資事宜，對股東權益 應無重大不利之影響。 11.原主辦承銷商評估意見摘要: 聯嘉光電投資控股股份有限公司辦理114年度現金增資發行　 新股暨發行國內第一次有擔保轉換公司債，其中國內第一次 有擔保轉換公司債已於115年第一季發行募集資金完成， 唯114年度現金增資發行新股因募集期間資本市場波動劇烈、 募資環境變化及維護公司股東權益，且該公司因依核准 資金之募集期間已不足以調整延後，而需申請撤銷現金增資 發行新股案並辦理計畫變更，經評估有其必要性及合理性。 該公司變更後計畫變更後資金用途仍為轉投資子公司 聯嘉光電股份有限公司以償還其銀行借款，故與原預計效益 並無重大差異，然因計畫變更後之金額減少，故可節省之利 息支出亦同步減少，惟仍有強化財務結構及提升償債能力， 以及節省利息支出，減輕財務負擔之效益，且已於115年 第一季執行完畢，經評估對該公司股東權益並無負面之影響。 12.其他應敘明事項:提報最近次股東會追認。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3717 | 聯嘉投控 | 2 | 2 | 2 | 2 | 5 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
