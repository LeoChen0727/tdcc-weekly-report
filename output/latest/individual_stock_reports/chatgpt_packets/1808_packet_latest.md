# INDIVIDUAL STOCK CHATGPT PACKET - 1808 潤隆

## Metadata
- generated_at: 2026-09-19 15:52:24 Asia/Taipei
- stock_id: 1808
- stock_name: 潤隆
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 351
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 43
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1808_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1808_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1808.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1808.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1808.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1808.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1808_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1808_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1808_latest.md?ref=main

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
- date: 20260918
- open: 36
- high: 37.15
- low: 35.1
- close: 35.9
- volume: 4369682
- ma5: 33.98
- ema23_primary: 34.3
- distance_to_ema23_pct: 4.67
- ma20: 34.81
- ma60: 32.9
- ma120: 31.46
- return_5d: 4.21
- return_20d: -2.97
- volume_ratio: 1.88
- distance_to_ma20_pct_auxiliary: 3.12
- distance_to_high_60_pct: -5.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,37.05,37.35,35.4,35.7,3635477,33.2,7.52,33.1,31.73,1.8
20260825,35.6,36.55,35,36.35,2131106,33.46,8.62,33.34,31.84,1.02
20260826,36.15,36.35,34.65,35.6,2830968,33.64,5.82,33.55,31.95,1.31
20260827,35.25,36.25,35.05,35.95,1644881,33.83,6.25,33.72,32.06,0.77
20260828,35.9,35.95,34.65,34.8,2527720,33.91,2.61,33.81,32.13,1.21
20260831,34.65,35,33.95,34.1,2545863,33.93,0.5,33.86,32.17,1.21
20260901,34,34.9,34,34.85,3335679,34.01,2.48,33.98,32.23,1.57
20260902,34.75,35.45,34.75,35.45,2109015,34.13,3.88,34.13,32.31,0.96
20260903,35.45,36.1,34.8,35.8,2500291,34.27,4.48,34.33,32.39,1.11
20260904,35.5,35.5,34.55,34.7,1770833,34.3,1.16,34.41,32.44,0.78
20260907,35.05,35.05,34,34.25,1129564,34.3,-0.14,34.46,32.49,0.51
20260908,34.25,35.1,34.1,34.85,1180519,34.34,1.47,34.58,32.54,0.54
20260909,34.65,35.45,34.65,35.1,2570106,34.41,2.01,34.7,32.58,1.13
20260910,34.8,34.8,33.7,34.4,2554064,34.41,-0.02,34.76,32.62,1.09
20260911,33.95,34.45,33.6,34.45,2080015,34.41,0.12,34.85,32.66,0.86
20260914,34.05,34.3,33.1,33.2,1588085,34.31,-3.23,34.86,32.67,0.65
20260915,33.2,33.5,32.9,33,1211558,34.2,-3.51,34.87,32.71,0.49
20260916,33,33.75,33,33.65,2542566,34.15,-1.48,34.88,32.77,1.02
20260917,33.65,34.45,33.2,34.15,2117102,34.15,-0.01,34.87,32.82,0.86
20260918,36,37.15,35.1,35.9,4369682,34.3,4.67,34.81,32.9,1.88
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 80.85
- over_600_ratio: 79.78
- over_800_ratio: 79.25
- over_1000_ratio: 78.85
- over_400_change_1w: 0.03
- over_800_change_1w: 0.06
- over_1000_change_1w: -0.14
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,79.51,-0.14,78.1,0,77.6,0,8,False,False
20260709,79.66,0.15,78.2,0.1,77.59,-0.01,9,False,True
20260717,79.95,0.29,78.29,0.09,77.77,0.18,10,True,True
20260724,80.18,0.23,78.49,0.2,78.08,0.31,11,True,True
20260731,80.4,0.22,78.7,0.21,78.19,0.11,12,True,True
20260807,80.22,-0.18,78.57,-0.13,78.16,-0.03,0,False,False
20260814,80.47,0.25,78.82,0.25,78.31,0.15,1,True,True
20260821,80.63,0.16,79.04,0.22,78.54,0.23,2,True,True
20260828,80.85,0.22,79.35,0.31,78.86,0.32,3,True,True
20260904,80.82,-0.03,79.2,-0.15,78.8,-0.06,0,False,False
20260911,80.82,0,79.19,-0.01,78.99,0.19,1,False,True
20260918,80.85,0.03,79.25,0.06,78.85,-0.14,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1808 | 潤隆 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | repeated_but_no_breakout | 1.董事會決議日期:NA 2.減資基準日:115/08/20 3.減資換發股票作業計畫: 一、本公司為調整資本結構及提升股東權益報酬率，經115年6月9日股東常會決議通過     辦理現金減資，減資新台幣1,786,063,500元整，銷除股份178,606,350股，業經臺     灣證券交易所股份有限公司115年8月11日臺證上一字第1151803117號函申報生效在     案，並奉經濟部115年8月27日經授商字第11530137710號函核准變更登記。本公司「     減資換發股票作業計畫書」亦經臺灣證券交易所股份有限公司115年9月9日臺證上     一字第1150018164號函核准在案。 二、本次辦理現金減資換發股票作業之有價證券名稱、股數、每股面額及總額：     1.換發有價證券名稱：潤隆建設股份有限公司普通股。     2.換發股票總數：包括歷年已發行之全部股票，計普通股893,031,743股，每股面       額新台幣10元，共計新台幣8,930,317,430元。     3.減資股份總數及金額：銷除已發行股份178,606,350股，每股面額新台幣10元整，       共計新台幣1,786,063,500元整。     4.減資比率：20%，依減資換發股票基準日之股東名簿記載各股東持有股份分別計       算，每仟股換發800股（即每仟股減少200股）。減資後不足一股之畸零股，股東       可自行在減資換發股票停止過戶日前五日起至停止過戶日前一日止，向本公司股       務代理機構辦理整股之拼湊，拼湊不足一股之畸零股，按面額改發現金至元為止       （元以下捨去），並授權董事長洽特定人按面額承購之。凡參加帳簿劃撥配發股       票之股東，其未滿一股之畸零股款，將做為處理帳簿劃撥之費用。     5.每股退還股款金額：每股退還現金新台幣2元，發放至元為止(元以下捨去)。     6.減資後股份總數及金額：減資後換發股數計714,425,393股，每股面額新台幣10       元，共計新台幣7,144,253,930元。 三、本次現金減資換發之新股採無實體發行，其權利義務與原發行普通股股份相同。 四、減資換發股票日程如下：     1.舊股票最後交易日：115年11月11日。     2.舊股票停止在市場買賣期間：115年11月12日至115年11月20日。     3.舊股票最後過戶日：115年11月15日。     4.舊股票停止過戶期間：115年11月16日至115年11月20日。     5.減資換發股票基準日：115年11月20日。     6.換發新股票上市買賣日暨舊股票終止上市日：115年11月23日。     7.現金減資退還股款發放日：115年11月27日。     8.自新股上市買賣之日起，舊股票不得作為買賣交割之標的。 五、換發新股票之程序及手續：     1.本次換發之新股票，一律採無實體發行，故請尚未在證券商處所開設集保帳戶之       股東，儘速至往來證券商開立集保帳戶，以利辦理換發作業。     2.本公司股務代理機構印製減資換發通知書寄送各股東，憑以辦理換發新股。     3.已過戶舊股票換發：股東應持舊股票連同本公司股務代理機構群益金鼎證券股份       有限公司股務代理部寄發之股票換發申請書、原留印鑑及集保存簿等，至股務代       理機構辦理換發。     4.未過戶舊股票換發：凡自集中交易市場買進且尚未辦理過戶者請備妥舊股票、轉       讓過戶書、買進報告書或股票領回號碼清單或相關證明文件、身分證正反面影印       本乙份、原留印鑑及集保存簿至本公司股務代理機構辦理過戶及換發手續。     5.已存放在證券集保帳戶之股票，由臺灣集中保管結算所股份有限公司於新股上市　       買賣日統一換發，股東不需辦理任何手續換發新股票。 六、換發處所︰     本公司股務代理機構：群益金鼎證券股份有限公司股務代理部。     地址：106420台北市大安區敦化南路二段97號地下二樓。     電話：(02)2702-3999。 七、其他未盡事宜，悉依公司法及其他相關法令辦理。 4.換發股票基準日:115/11/20 5.停止過戶起始日期:115/11/16 6.停止過戶截止日期:115/11/20 7.減資後新股權利義務:與原發行普通股股份相同。 8.新股預計上市日:115/11/23 9.預計減資新股上市後之上市普通股股數:714,425,393股 10.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，   請說明股權流通性偏低之因應措施:不適用 12.其他應敘明事項:無。；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260918 | 1808 | 潤隆 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 26 | D_僅留完整清單 |  |  |  | repeated_but_no_breakout | 1.董事會決議日期:NA 2.減資基準日:115/08/20 3.減資換發股票作業計畫: 一、本公司為調整資本結構及提升股東權益報酬率，經115年6月9日股東常會決議通過     辦理現金減資，減資新台幣1,786,063,500元整，銷除股份178,606,350股，業經臺     灣證券交易所股份有限公司115年8月11日臺證上一字第1151803117號函申報生效在     案，並奉經濟部115年8月27日經授商字第11530137710號函核准變更登記。本公司「     減資換發股票作業計畫書」亦經臺灣證券交易所股份有限公司115年9月9日臺證上     一字第1150018164號函核准在案。 二、本次辦理現金減資換發股票作業之有價證券名稱、股數、每股面額及總額：     1.換發有價證券名稱：潤隆建設股份有限公司普通股。     2.換發股票總數：包括歷年已發行之全部股票，計普通股893,031,743股，每股面       額新台幣10元，共計新台幣8,930,317,430元。     3.減資股份總數及金額：銷除已發行股份178,606,350股，每股面額新台幣10元整，       共計新台幣1,786,063,500元整。     4.減資比率：20%，依減資換發股票基準日之股東名簿記載各股東持有股份分別計       算，每仟股換發800股（即每仟股減少200股）。減資後不足一股之畸零股，股東       可自行在減資換發股票停止過戶日前五日起至停止過戶日前一日止，向本公司股       務代理機構辦理整股之拼湊，拼湊不足一股之畸零股，按面額改發現金至元為止       （元以下捨去），並授權董事長洽特定人按面額承購之。凡參加帳簿劃撥配發股       票之股東，其未滿一股之畸零股款，將做為處理帳簿劃撥之費用。     5.每股退還股款金額：每股退還現金新台幣2元，發放至元為止(元以下捨去)。     6.減資後股份總數及金額：減資後換發股數計714,425,393股，每股面額新台幣10       元，共計新台幣7,144,253,930元。 三、本次現金減資換發之新股採無實體發行，其權利義務與原發行普通股股份相同。 四、減資換發股票日程如下：     1.舊股票最後交易日：115年11月11日。     2.舊股票停止在市場買賣期間：115年11月12日至115年11月20日。     3.舊股票最後過戶日：115年11月15日。     4.舊股票停止過戶期間：115年11月16日至115年11月20日。     5.減資換發股票基準日：115年11月20日。     6.換發新股票上市買賣日暨舊股票終止上市日：115年11月23日。     7.現金減資退還股款發放日：115年11月27日。     8.自新股上市買賣之日起，舊股票不得作為買賣交割之標的。 五、換發新股票之程序及手續：     1.本次換發之新股票，一律採無實體發行，故請尚未在證券商處所開設集保帳戶之       股東，儘速至往來證券商開立集保帳戶，以利辦理換發作業。     2.本公司股務代理機構印製減資換發通知書寄送各股東，憑以辦理換發新股。     3.已過戶舊股票換發：股東應持舊股票連同本公司股務代理機構群益金鼎證券股份       有限公司股務代理部寄發之股票換發申請書、原留印鑑及集保存簿等，至股務代       理機構辦理換發。     4.未過戶舊股票換發：凡自集中交易市場買進且尚未辦理過戶者請備妥舊股票、轉       讓過戶書、買進報告書或股票領回號碼清單或相關證明文件、身分證正反面影印       本乙份、原留印鑑及集保存簿至本公司股務代理機構辦理過戶及換發手續。     5.已存放在證券集保帳戶之股票，由臺灣集中保管結算所股份有限公司於新股上市　       買賣日統一換發，股東不需辦理任何手續換發新股票。 六、換發處所︰     本公司股務代理機構：群益金鼎證券股份有限公司股務代理部。     地址：106420台北市大安區敦化南路二段97號地下二樓。     電話：(02)2702-3999。 七、其他未盡事宜，悉依公司法及其他相關法令辦理。 4.換發股票基準日:115/11/20 5.停止過戶起始日期:115/11/16 6.停止過戶截止日期:115/11/20 7.減資後新股權利義務:與原發行普通股股份相同。 8.新股預計上市日:115/11/23 9.預計減資新股上市後之上市普通股股數:714,425,393股 10.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，   請說明股權流通性偏低之因應措施:不適用 12.其他應敘明事項:無。；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1808 | 潤隆 | 25 | 16 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

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
