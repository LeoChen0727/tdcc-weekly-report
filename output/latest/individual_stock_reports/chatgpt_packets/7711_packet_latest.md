# INDIVIDUAL STOCK CHATGPT PACKET - 7711 永擎

## Metadata
- generated_at: 2026-09-20 22:18:26 Asia/Taipei
- stock_id: 7711
- stock_name: 永擎
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 203
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/7711_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/7711_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7711_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7711_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7711_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7711_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7711_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7711.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7711.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7711.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7711.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7711_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7711_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7711_latest.md?ref=main

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
- open: 566
- high: 584
- low: 561
- close: 570
- volume: 1904132
- ma5: 519
- ema23_primary: 525.17
- distance_to_ema23_pct: 8.54
- ma20: 549.62
- ma60: 415.57
- ma120: 389.16
- return_5d: 7.34
- return_20d: 23.51
- volume_ratio: 1.1
- distance_to_ma20_pct_auxiliary: 3.71
- distance_to_high_60_pct: -15.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,462,506,458.5,497.5,1969834,410.33,21.24,394.43,357.99,1.95
20260825,492,516,481,515,1678949,419.05,22.9,405.93,359.87,1.55
20260826,510,510,489,493,1451678,425.21,15.94,416.48,361.2,1.28
20260827,493,502,485,493,899277,430.86,14.42,427.25,362.69,0.77
20260828,498,503,472,487,1443345,435.54,11.82,436.98,364.22,1.17
20260831,486,535,483,535,1893081,443.83,20.54,449.05,366.8,1.43
20260901,535,580,533,575,2373303,454.76,26.44,462.82,369.83,1.65
20260902,570,625,567,610,2332752,467.7,30.43,476.88,373.82,1.51
20260903,617,617,575,575,1693857,476.64,20.64,487.55,377.19,1.04
20260904,597,632,575,632,2356476,489.58,29.09,500.4,381.84,1.46
20260907,645,675,621,660,2867311,503.79,31.01,513.15,386.88,1.7
20260908,650,650,594,594,2433484,511.3,16.17,522.5,390.8,1.43
20260909,594,617,575,610,1865679,519.53,17.41,530.62,394.86,1.1
20260910,598,615,583,590,1268789,525.4,12.3,535.55,398.61,0.76
20260911,531,531,531,531,318431,525.87,0.98,538.5,401.45,0.2
20260914,478,478,478,478,411129,521.88,-8.41,538.65,403.34,0.25
20260915,461,473,438,468,3570247,517.39,-9.55,537.45,405.21,2.03
20260916,472,514,472,514,1415029,517.11,-0.6,538.65,408.11,0.79
20260917,560,565,556,565,613102,521.1,8.43,544.2,411.72,0.36
20260918,566,584,561,570,1904132,525.17,8.54,549.62,415.57,1.1
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 61.18
- over_600_ratio: 60.36
- over_800_ratio: 55.31
- over_1000_ratio: 52.68
- over_400_change_1w: -0.41
- over_800_change_1w: -1.41
- over_1000_change_1w: -1.42
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,61.81,-0.02,57.22,0.01,54.67,0,3,False,True
20260709,61.79,-0.02,57.21,-0.01,54.67,0,0,False,False
20260717,61.81,0.02,57.24,0.03,54.67,0,1,False,True
20260724,61.79,-0.02,57.23,-0.01,54.67,0,0,False,False
20260731,61.77,-0.02,57.22,-0.01,54.67,0,0,False,False
20260807,61.3,-0.47,57.31,0.09,54.67,0,1,False,True
20260814,61.64,0.34,57.65,0.34,56.4,1.73,2,True,True
20260821,61.54,-0.1,57.55,-0.1,56.29,-0.11,0,False,False
20260828,61.8,0.26,57.01,-0.54,54.39,-1.9,1,False,False
20260904,62.93,1.13,57.36,0.35,54.74,0.35,2,True,True
20260911,61.59,-1.34,56.72,-0.64,54.1,-0.64,0,False,False
20260918,61.18,-0.41,55.31,-1.41,52.68,-1.42,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 7711 | 永擎 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_strong_inflow | repeated_but_no_breakout | 1.董事會決議日期:115/09/17 2.名稱﹝XX公司第X次（有、無）擔保公司債﹞: 永擎電子股份有限公司國內第一次無擔保轉換公司債 3.是否採總括申報發行公司債(是/否):否 4.發行總額:發行總面額上限為新臺幣4,200,000仟元整。 5.每張面額:新臺幣100,000元整。 6.發行價格:採競價拍賣方式辦理公開承銷，底標暫定以面額之100%~103%發行， 實際總發行金額依競價拍賣結果而定。 7.發行期間:五年 8.發行利率:票面利率0% 9.擔保品之種類、名稱、金額及約定事項:不適用 10.募得價款之用途及運用計畫:充實營運資金、償還銀行借款 11.承銷方式:採競價拍賣方式辦理公開承銷 12.公司債受託人:董事會授權董事長全權處理之 13.承銷或代銷機構:元大證券股份有限公司 14.發行保證人:不適用 15.代理還本付息機構:凱基證券股份有限公司股務代理部 16.簽證機構:不適用 17.能轉換股份者，其轉換辦法: 相關辦法將依有關法令規定辦理，並報奉相關主管機關核准後另行公告。 18.賣回條件: 相關辦法將依有關法令規定辦理，並報奉相關主管機關核准後另行公告。 19.買回條件: 相關辦法將依有關法令規定辦理，並報奉相關主管機關核准後另行公告。 20.附有轉換、交換或認股者，其換股基準日: 相關辦法將依有關法令規定辦理，並報奉相關主管機關核准後另行公告。 21.附有轉換、交換或認股者，對股權可能稀釋情形: 相關辦法將依有關法令規定辦理，並報奉相關主管機關核准後另行公告。 22.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 23.其他應敘明事項: (1)配合本次發行國內第一次無擔保轉換公司債籌資計畫之發行作業， 授權董事長核可並代表本公司簽署一切有關本次發行國內第一次 無擔保轉換公司債之契約及文件，並代表本公司辦理相關發行事宜。 (2)因資本市場籌資環境變化快速，為掌握訂定發行條件及實際發行作業 之時效，本次發行國內第一次無擔保轉換公司債籌資計畫有關之預計及實際 發行金額(張數)、募集金額、發行條件、發行及轉換辦法之訂定，以及計畫 所需資金總額、資金來源、計畫項目、資金運用進度、預計可能產生效益、 募集時點、公開承銷方式、本案展延、撤銷及其他相關事宜，如經主管機關指示 ，相關法令規則修正，或因應客觀環境需修訂或修正時，授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 7711 | 永擎 | 1 | 1 | 3 | 6 | 14 | repeated_but_no_breakout | 近 10 日上榜 6 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 7711 | 永擎 | 9 | 0 | 8176480.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
