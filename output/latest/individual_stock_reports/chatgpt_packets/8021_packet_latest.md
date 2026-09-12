# INDIVIDUAL STOCK CHATGPT PACKET - 8021 尖點

## Metadata
- generated_at: 2026-09-12 22:17:56 Asia/Taipei
- stock_id: 8021
- stock_name: 尖點
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8021_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8021_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8021.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8021.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8021.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8021.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8021_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8021_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8021_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260911
- open: 430
- high: 430
- low: 418
- close: 418.5
- volume: 1115991
- ma5: 442.2
- ema23_primary: 429.03
- distance_to_ema23_pct: -2.45
- ma20: 425.57
- ma60: 449.26
- ma120: 424.65
- return_5d: -0.36
- return_20d: -3.57
- volume_ratio: 0.16
- distance_to_ma20_pct_auxiliary: -1.66
- distance_to_high_60_pct: -32.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,423.5,431,395,428,1631315,419.93,1.92,389.82,466.41,0.32
20260818,437,452,400,408.5,10703530,418.98,-2.5,391.23,466.18,2.1
20260819,392,413,391,393.5,5308156,416.86,-5.6,389.98,465.01,1.03
20260820,402.5,418.5,401,408.5,4979209,416.16,-1.84,390.07,464.07,1
20260821,407,410.5,394,397,3418276,414.56,-4.24,391.43,463.43,0.72
20260824,397,411,388,388.5,3247872,412.39,-5.79,391.32,462.93,0.71
20260825,384,404,373.5,404,3896338,411.69,-1.87,393.95,462.17,0.85
20260826,404,437.5,398.5,418.5,8167498,412.26,1.51,399.05,461.41,1.67
20260827,429,430,415,422.5,5113803,413.11,2.27,405.48,461.03,1.08
20260828,433.5,463.5,426,454,16137795,416.52,9,412.02,460.77,2.94
20260831,442.5,461,423.5,435,9134188,418.06,4.05,416.02,460.67,1.58
20260901,435,465,430,450,8753655,420.72,6.96,419,460.53,1.47
20260902,445,461,438.5,459,7186775,423.91,8.28,422.15,460.52,1.25
20260903,461,462,413.5,413.5,14442146,423.04,-2.26,421.95,458.98,2.41
20260904,425,426,413,420,6332673,422.79,-0.66,423.2,456.71,1.06
20260907,445,462,444,462,13046649,426.06,8.44,424.57,454.91,2.07
20260908,441,461,431,450,15127276,428.05,5.13,425.12,453.71,2.16
20260909,448,451.5,439.5,442.5,1319886,429.26,3.09,425.9,452.65,0.19
20260910,445.5,449.5,431,438,995636,429.99,1.86,426.35,451.32,0.14
20260911,430,430,418,418.5,1115991,429.03,-2.45,425.57,449.26,0.16
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 47.53
- over_600_ratio: 43.07
- over_800_ratio: 39.81
- over_1000_ratio: 34.82
- over_400_change_1w: 4.09
- over_800_change_1w: 4.06
- over_1000_change_1w: 3.92
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,47.84,1.27,40.38,2.4,37.38,2.33,1,True,True
20260703,47.91,0.07,40.61,0.23,37.17,-0.21,2,False,True
20260709,48.03,0.12,40.86,0.25,37.85,0.68,3,False,True
20260717,47.46,-0.57,40.91,0.05,37.93,0.08,4,False,True
20260724,46.23,-1.23,39.9,-1.01,36.93,-1,0,False,False
20260731,46.38,0.15,38.67,-1.23,33.85,-3.08,1,False,False
20260807,46.88,0.5,38.32,-0.35,35.82,1.97,2,False,True
20260814,47.1,0.22,40.13,1.81,38.29,2.47,3,True,True
20260821,45.88,-1.22,38.87,-1.26,35.75,-2.54,0,False,False
20260828,46.17,0.29,37.33,-1.54,34.34,-1.41,1,False,False
20260904,43.44,-2.73,35.75,-1.58,30.9,-3.44,0,False,False
20260911,47.53,4.09,39.81,4.06,34.82,3.92,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8021 | 尖點 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.董事會決議或公司決定增資基準日期:115/09/08 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/09/04 4.董事會決議(追補)發行日期:115/08/14 5.發行總金額及股數: 發行總面額新台幣40,000,000元 發行股數:4,000,000股。 6.採總括申報發行新股案件，本次發行金額及股數:不適用。 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用。 8.每股面額:新台幣 10 元。 9.發行價格:俟定價後另行公告。 10.員工認股股數: 依公司法第267條規定，保留發行新股總數10%，計400千股 供員工認購。 11.原股東認購比率:本次發行新股總額之80%計3,200千股，由原股東按 增資認股基準日股東名簿記載之股東及其持股比例分別認購，依本公司 目前流通在外股數 147,320,109股計算，原股東每仟股得認購 21.72140668股。如嗣後因本公司普通股發生變動影響流通在外股份數量， 致原股東認股比率因此發生變動時，由董事長辦理相關調整事宜。 12.公開銷售方式及股數:依證券交易法28條之1規定，提撥發行新股總數10%， 計400千股採公開申購方式對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止 過戶日起五日內由股東自行向本公司股務代理機構辦理拼湊整股認購，其拼湊不 足一股之畸零股及原股東、員工放棄認購或認購不足及逾期未拼湊之部分，擬授 權董事長洽特定人按發行價格認購之。 14.本次發行新股之權利義務: 本次現金增資發行新股之權利義務與原發行 之普通股份相同。 15.本次增資資金用途:購置機器設備/廠務工程/員工宿舍。 16.現金增資認股基準日:115/10/12 17.最後過戶日:115/10/07 18.停止過戶起始日期:115/10/08 19.停止過戶截止日期:115/10/12 20.股款繳納期間: (1)原股東及員工繳款期間:115/10/20 ~ 115/10/27 (2)特定人認股繳款期間:115/10/28-115/10/30 21.與代收及專戶存儲價款行庫訂約日期:俟正式簽約後另行公告。 22.委託代收存款機構:俟正式簽約後另行公告。 23.委託存儲款項機構:俟正式簽約後另行公告。 24.其他應敘明事項: (1)本公司辦理115年現金增資發行普通股4,000,000股乙案， 業經金融監督管理委員會115年9月4日金管證發字第1150353873號函 申報生效在案。 (2)本公司國內第二次無擔保轉換公司債，停止轉換普通股期間為 115年09月15日至115年10月12日；請債券持有人如擬申請轉換， 最遲應於115年9月11日向往來證券商辦理轉換手續。 (3)嗣後如因本公司可轉換公司債轉換，致影響流通在外股數， 使每仟股可認購股數因此發生變動者，授權董事長全權處理認股率調整事宜， 並另行公告之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 8021 | 尖點 | revenue_breakout_low_response | 營收爆發低反應股 | 14 | 40 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.董事會決議或公司決定增資基準日期:115/09/08 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/09/04 4.董事會決議(追補)發行日期:115/08/14 5.發行總金額及股數: 發行總面額新台幣40,000,000元 發行股數:4,000,000股。 6.採總括申報發行新股案件，本次發行金額及股數:不適用。 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用。 8.每股面額:新台幣 10 元。 9.發行價格:俟定價後另行公告。 10.員工認股股數: 依公司法第267條規定，保留發行新股總數10%，計400千股 供員工認購。 11.原股東認購比率:本次發行新股總額之80%計3,200千股，由原股東按 增資認股基準日股東名簿記載之股東及其持股比例分別認購，依本公司 目前流通在外股數 147,320,109股計算，原股東每仟股得認購 21.72140668股。如嗣後因本公司普通股發生變動影響流通在外股份數量， 致原股東認股比率因此發生變動時，由董事長辦理相關調整事宜。 12.公開銷售方式及股數:依證券交易法28條之1規定，提撥發行新股總數10%， 計400千股採公開申購方式對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止 過戶日起五日內由股東自行向本公司股務代理機構辦理拼湊整股認購，其拼湊不 足一股之畸零股及原股東、員工放棄認購或認購不足及逾期未拼湊之部分，擬授 權董事長洽特定人按發行價格認購之。 14.本次發行新股之權利義務: 本次現金增資發行新股之權利義務與原發行 之普通股份相同。 15.本次增資資金用途:購置機器設備/廠務工程/員工宿舍。 16.現金增資認股基準日:115/10/12 17.最後過戶日:115/10/07 18.停止過戶起始日期:115/10/08 19.停止過戶截止日期:115/10/12 20.股款繳納期間: (1)原股東及員工繳款期間:115/10/20 ~ 115/10/27 (2)特定人認股繳款期間:115/10/28-115/10/30 21.與代收及專戶存儲價款行庫訂約日期:俟正式簽約後另行公告。 22.委託代收存款機構:俟正式簽約後另行公告。 23.委託存儲款項機構:俟正式簽約後另行公告。 24.其他應敘明事項: (1)本公司辦理115年現金增資發行普通股4,000,000股乙案， 業經金融監督管理委員會115年9月4日金管證發字第1150353873號函 申報生效在案。 (2)本公司國內第二次無擔保轉換公司債，停止轉換普通股期間為 115年09月15日至115年10月12日；請債券持有人如擬申請轉換， 最遲應於115年9月11日向往來證券商辦理轉換手續。 (3)嗣後如因本公司可轉換公司債轉換，致影響流通在外股數， 使每仟股可認購股數因此發生變動者，授權董事長全權處理認股率調整事宜， 並另行公告之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8021 | 尖點 | 1 | 1 | 4 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
