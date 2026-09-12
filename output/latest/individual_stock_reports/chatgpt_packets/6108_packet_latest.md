# INDIVIDUAL STOCK CHATGPT PACKET - 6108 競國

## Metadata
- generated_at: 2026-09-12 22:17:14 Asia/Taipei
- stock_id: 6108
- stock_name: 競國
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6108_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6108_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6108.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6108.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6108.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6108.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6108_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6108_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6108_latest.md?ref=main

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
- open: 22.4
- high: 22.8
- low: 22
- close: 22.15
- volume: 2309114
- ma5: 22.8
- ema23_primary: 22.54
- distance_to_ema23_pct: -1.74
- ma20: 23.67
- ma60: 19.94
- ma120: 19.28
- return_5d: -3.49
- return_20d: 0.23
- volume_ratio: 0.56
- distance_to_ma20_pct_auxiliary: -6.41
- distance_to_high_60_pct: -16.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,22.4,23.35,22.2,22.9,3090934,18.9,21.15,18.12,18.56,2.35
20260818,23.1,24,23,23.6,3495620,19.29,22.32,18.47,18.63,2.41
20260819,23.75,25.8,23.35,24.75,5933400,19.75,25.33,18.88,18.71,3.47
20260820,25.25,26.6,24.15,26,9855505,20.27,28.27,19.34,18.82,4.55
20260821,26.55,26.55,24.8,25.95,6326680,20.74,25.11,19.8,18.93,2.57
20260824,24.7,24.7,23.4,23.4,3904718,20.96,11.62,20.12,18.98,1.49
20260825,22.45,23.6,21.9,22.85,5723486,21.12,8.19,20.44,19.03,2
20260826,22.85,23.3,22.45,22.75,3947429,21.26,7.02,20.76,19.07,1.31
20260827,23.85,24.6,23.1,23.8,4277452,21.47,10.86,21.14,19.15,1.35
20260828,24.3,26.15,24.1,25.7,11060642,21.82,17.77,21.59,19.25,3.01
20260831,26,26.15,23.7,23.85,6633776,21.99,8.46,21.94,19.32,1.67
20260901,24,24.45,23.6,23.9,2663045,22.15,7.9,22.29,19.39,0.65
20260902,23.55,24.6,23.5,23.9,2557023,22.3,7.2,22.61,19.47,0.61
20260903,24.25,24.25,23.05,23.05,2740157,22.36,3.09,22.86,19.54,0.64
20260904,23.25,23.5,22.7,22.95,1378795,22.41,2.42,23.07,19.62,0.32
20260907,23.3,23.6,22.8,22.95,1804750,22.45,2.21,23.28,19.7,0.41
20260908,22.8,22.9,22.15,22.25,1446413,22.44,-0.83,23.41,19.76,0.34
20260909,22.25,23.7,22.1,23.35,2008941,22.51,3.72,23.59,19.82,0.47
20260910,23.5,23.85,22.7,23.3,1572181,22.58,3.2,23.66,19.89,0.38
20260911,22.4,22.8,22,22.15,2309114,22.54,-1.74,23.67,19.94,0.56
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 56.55
- over_600_ratio: 53.76
- over_800_ratio: 50.2
- over_1000_ratio: 48.55
- over_400_change_1w: 0.46
- over_800_change_1w: -0.97
- over_1000_change_1w: -1.53
- tdcc_consecutive_up_weeks: 15
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,52.56,-0.06,44.27,-0.61,42.43,-0.59,4,False,False
20260703,52.14,-0.42,44.19,-0.08,42.46,0.03,5,False,True
20260709,52.52,0.38,44.67,0.48,41.71,-0.75,6,False,True
20260717,52.64,0.12,44.07,-0.6,42.2,0.49,7,False,True
20260724,52.46,-0.18,46.38,2.31,44.46,2.26,8,False,True
20260731,53.01,0.55,46,-0.38,44.12,-0.34,9,False,False
20260807,52.89,-0.12,45.9,-0.1,43.42,-0.7,10,False,False
20260814,54.38,1.49,48.01,2.11,45.54,2.12,11,True,True
20260821,55.89,1.51,50.26,2.25,48.57,3.03,12,True,True
20260828,56.28,0.39,50.9,0.64,49.81,1.24,13,True,True
20260904,56.09,-0.19,51.17,0.27,50.08,0.27,14,False,True
20260911,56.55,0.46,50.2,-0.97,48.55,-1.53,15,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6108 | 競國 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會決議日期:NA 2.減資基準日:115/08/13 3.減資換發股票作業計畫:  一、本公司於民國115年6月17日經股東常會決議通過，辦理現金減資退還股款案，經      臺灣證券交易所股份有限公司民國115年7月31日臺證上一字第1150013727號函申      報生效在案，並奉經濟部115年8月31日經授商字第11530138570號函核准變更登      記。茲依據「臺灣證券交易所股份有限公司上市公司換發有價證券作業程序」之      規定，訂定本作業計畫。  二、本次辦理換發股份作業之相關明細     （一）本公司目前已發行普通股股份為154,494,311股，每股面額新台幣壹拾元，           共計新台幣1,544,943,110元。     （二）本次現金減資新台幣463,482,930元，消除普通股股數46,348,293股，現金           減資比例30%。     （三）減資後發行普通股股份為108,146,018股，每股面額新台幣壹拾元，共計新           台幣1,081,460,180元。     （四）普通股依「減資換股基準日」股東名簿記載各股東持有股份分別計算，每           千股換發新股700股（即每千股消除300股），每股退還現金3元，減資後不           足壹股之畸零股，股東得於減資換股停止過戶日前五日起至停止過戶日前           一日止，向本公司股務代理機構辦理拼湊登記，股東未辦理拼湊或拼湊後           仍不足壹股之畸零股，由本公司按股票面額折付現金至元為止（元以下四           捨五入），不足壹股之畸零股授權董事長洽特定人按面額承購之。     （五）本次減資換發之股份，全部採無實體發行，其權利義務與原發行股份相同。  三、減資換發股票日程     （一）減資基準日：115年08月13日（向經濟部申請辦理減資變更登記之用）     （二）減資股票市場買賣最後交易日：115年12月09日     （三）減資股票市場停止買賣期間：115年12月10日至115年12月17日     （四）減資股票最後過戶日：115年12月11日     （五）減資股票停止過戶期間：115年12月13日至115年12月17日     （六）減資換股基準日：115年12月17日（無實體發行）     （七）換發新股及上市買賣日：115年12月18日（舊股票停止上市日）     （八）現金減資退還股款發放日：115年12月23日  四、換發手續相關事宜     （一）本公司之股票已採無實體發行，屆時將不再發行現券，故請尚未在證券商           開設集保戶之股東，務必儘速至往來證券商開立集保帳戶，以利辦理換發           作業。     （二）股東若持有現股股票者，或舊股票尚未領取者，請於歷年未領取股票領取           單蓋妥原留印鑑後，再檢附換發股票相關文件至本公司股務代理機構辦理           股票換發手續。     （三）原已存放於證券集保帳戶之股票，由臺灣集中保管結算所股份有限公司新           股上市買賣日統一換發為無實體新股，股東不需辦理任何手續換發新股票。     （四）辦理過戶方式：凡持有股票尚未過戶者，最後過戶日民國115年12月11日下           午5時00分前親臨本公司股務代理機構，辦理過戶手續，掛號郵寄以民國           115年12月11日(最後過戶日)郵戳日期為憑，郵寄申請換發新股票者，請用           掛號郵寄，如發生郵遞失誤情形，請 貴股東自行辦理股票掛失手續。凡           參加臺灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務           代理人將依其送交資料逕行辦理過戶手續。     （五）股票換發處所︰本公司股務代理機構「凱基證券股份有限公司股務代理部」           地址：台北市中正區重慶南路一段2號4樓，電話：(02)2314-8800。     （六）其他未盡事宜，擬依公司法及其他相關法令辦理。  五、上述減資基準日俟呈奉經濟部核准資本額變更登記後，向臺灣證券交易所股份有      限公司提報減資換股計劃，俟其核備後，即依該計劃辦理減資換發股票作業；如      因主管機關要求或實際需要得調整內容或相關日程變動時，授權董事長全權處理。 4.換發股票基準日:115/12/17 5.停止過戶起始日期:115/12/13 6.停止過戶截止日期:115/12/17 7.減資後新股權利義務:與原發行普通股股份相同。 8.新股預計上市日:115/12/18 9.預計減資新股上市後之上市普通股股數:108,146,018股。 10.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，   請說明股權流通性偏低之因應措施:不適用。 12.其他應敘明事項:本次修訂係依115年8月7日董事會決議授權董事長辦理，除前開作業   日程調整外，其餘減資計畫及相關事項仍依原董事會決議辦理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 6108 | 競國 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期:NA 2.減資基準日:115/08/13 3.減資換發股票作業計畫:  一、本公司於民國115年6月17日經股東常會決議通過，辦理現金減資退還股款案，經      臺灣證券交易所股份有限公司民國115年7月31日臺證上一字第1150013727號函申      報生效在案，並奉經濟部115年8月31日經授商字第11530138570號函核准變更登      記。茲依據「臺灣證券交易所股份有限公司上市公司換發有價證券作業程序」之      規定，訂定本作業計畫。  二、本次辦理換發股份作業之相關明細     （一）本公司目前已發行普通股股份為154,494,311股，每股面額新台幣壹拾元，           共計新台幣1,544,943,110元。     （二）本次現金減資新台幣463,482,930元，消除普通股股數46,348,293股，現金           減資比例30%。     （三）減資後發行普通股股份為108,146,018股，每股面額新台幣壹拾元，共計新           台幣1,081,460,180元。     （四）普通股依「減資換股基準日」股東名簿記載各股東持有股份分別計算，每           千股換發新股700股（即每千股消除300股），每股退還現金3元，減資後不           足壹股之畸零股，股東得於減資換股停止過戶日前五日起至停止過戶日前           一日止，向本公司股務代理機構辦理拼湊登記，股東未辦理拼湊或拼湊後           仍不足壹股之畸零股，由本公司按股票面額折付現金至元為止（元以下四           捨五入），不足壹股之畸零股授權董事長洽特定人按面額承購之。     （五）本次減資換發之股份，全部採無實體發行，其權利義務與原發行股份相同。  三、減資換發股票日程     （一）減資基準日：115年08月13日（向經濟部申請辦理減資變更登記之用）     （二）減資股票市場買賣最後交易日：115年12月09日     （三）減資股票市場停止買賣期間：115年12月10日至115年12月17日     （四）減資股票最後過戶日：115年12月11日     （五）減資股票停止過戶期間：115年12月13日至115年12月17日     （六）減資換股基準日：115年12月17日（無實體發行）     （七）換發新股及上市買賣日：115年12月18日（舊股票停止上市日）     （八）現金減資退還股款發放日：115年12月23日  四、換發手續相關事宜     （一）本公司之股票已採無實體發行，屆時將不再發行現券，故請尚未在證券商           開設集保戶之股東，務必儘速至往來證券商開立集保帳戶，以利辦理換發           作業。     （二）股東若持有現股股票者，或舊股票尚未領取者，請於歷年未領取股票領取           單蓋妥原留印鑑後，再檢附換發股票相關文件至本公司股務代理機構辦理           股票換發手續。     （三）原已存放於證券集保帳戶之股票，由臺灣集中保管結算所股份有限公司新           股上市買賣日統一換發為無實體新股，股東不需辦理任何手續換發新股票。     （四）辦理過戶方式：凡持有股票尚未過戶者，最後過戶日民國115年12月11日下           午5時00分前親臨本公司股務代理機構，辦理過戶手續，掛號郵寄以民國           115年12月11日(最後過戶日)郵戳日期為憑，郵寄申請換發新股票者，請用           掛號郵寄，如發生郵遞失誤情形，請 貴股東自行辦理股票掛失手續。凡           參加臺灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務           代理人將依其送交資料逕行辦理過戶手續。     （五）股票換發處所︰本公司股務代理機構「凱基證券股份有限公司股務代理部」           地址：台北市中正區重慶南路一段2號4樓，電話：(02)2314-8800。     （六）其他未盡事宜，擬依公司法及其他相關法令辦理。  五、上述減資基準日俟呈奉經濟部核准資本額變更登記後，向臺灣證券交易所股份有      限公司提報減資換股計劃，俟其核備後，即依該計劃辦理減資換發股票作業；如      因主管機關要求或實際需要得調整內容或相關日程變動時，授權董事長全權處理。 4.換發股票基準日:115/12/17 5.停止過戶起始日期:115/12/13 6.停止過戶截止日期:115/12/17 7.減資後新股權利義務:與原發行普通股股份相同。 8.新股預計上市日:115/12/18 9.預計減資新股上市後之上市普通股股數:108,146,018股。 10.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，   請說明股權流通性偏低之因應措施:不適用。 12.其他應敘明事項:本次修訂係依115年8月7日董事會決議授權董事長辦理，除前開作業   日程調整外，其餘減資計畫及相關事項仍依原董事會決議辦理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6108 | 競國 | 7 | 7 | 5 | 8 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
