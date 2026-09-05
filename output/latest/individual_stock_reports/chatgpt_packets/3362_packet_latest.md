# INDIVIDUAL STOCK CHATGPT PACKET - 3362 先進光

## Metadata
- generated_at: 2026-09-05 22:16:32 Asia/Taipei
- stock_id: 3362
- stock_name: 先進光
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3362_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3362_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3362_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3362_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3362_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3362_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3362_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3362.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3362.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3362.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3362.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3362_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3362_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3362_latest.md?ref=main

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
- date: 20260904
- open: 202.5
- high: 210
- low: 196
- close: 210
- volume: 1388000
- ma5: 204
- ema23_primary: 191.18
- distance_to_ema23_pct: 9.84
- ma20: 190.47
- ma60: 180.94
- ma120: 145.81
- return_5d: 5.26
- return_20d: 21.04
- volume_ratio: 0.25
- distance_to_ma20_pct_auxiliary: 10.25
- distance_to_high_60_pct: -3.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,176,180,175,178,665000,170.2,4.58,166.28,160.37,0.09
20260811,178.5,178.5,171,174.5,637000,170.56,2.31,166.4,161.4,0.08
20260812,174.5,179.5,172,179,958000,171.26,4.52,166.8,162.47,0.13
20260813,181,181.5,177.5,181,1439000,172.07,5.19,167.38,163.51,0.2
20260814,185.5,191.5,170.5,172,5669000,172.07,-0.04,168.18,164.48,0.77
20260817,173,186,171,178.5,7490000,172.6,3.42,169.68,165.44,0.98
20260818,180.5,185.5,175,175,4637000,172.8,1.27,170.85,166.36,0.59
20260819,171,184.5,171,181.5,3958000,173.53,4.59,172.1,167.43,0.5
20260820,183.5,194.5,182.5,186,12262000,174.57,6.55,173.25,168.62,1.47
20260821,186,200,180,194.5,9033000,176.23,10.37,175.45,169.98,1.03
20260824,190,202.5,188,188.5,12278000,177.25,6.35,176.6,171.28,1.36
20260825,187,198,181.5,195,8609000,178.73,9.1,178.45,172.7,1.05
20260826,192,214.5,192,202,30982000,180.67,11.81,179.88,174.05,3.6
20260827,202,205,197,204.5,2500000,182.66,11.96,182.28,175.47,0.33
20260828,207,207,196.5,199.5,1717000,184.06,8.39,183.65,176.61,0.24
20260831,197.5,204.5,194.5,202,1818000,185.55,8.86,184.75,177.57,0.28
20260901,202.5,206.5,200,200,919000,186.76,7.09,185.78,178.44,0.17
20260902,202.5,213,201,210,2301000,188.69,11.29,187.55,179.58,0.42
20260903,212.5,213,198,198,1196000,189.47,4.5,188.65,180.29,0.22
20260904,202.5,210,196,210,1388000,191.18,9.84,190.47,180.94,0.25
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 61.16
- over_600_ratio: 56.75
- over_800_ratio: 53.05
- over_1000_ratio: 50.48
- over_400_change_1w: 0.88
- over_800_change_1w: -0.32
- over_1000_change_1w: 0.8
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,62.25,1.16,52.53,0.12,50.62,0.82,3,True,True
20260626,62.23,-0.02,53.41,0.88,50.91,0.29,4,False,True
20260703,60.13,-2.1,52.1,-1.31,50.22,-0.69,0,False,False
20260709,59.43,-0.7,51.4,-0.7,49.45,-0.77,0,False,False
20260717,59.82,0.39,51.99,0.59,48.77,-0.68,1,False,True
20260724,59.32,-0.5,51.33,-0.66,48.78,0.01,2,False,True
20260731,58.54,-0.78,50.72,-0.61,48.08,-0.7,0,False,False
20260807,59.72,1.18,51.32,0.6,48.76,0.68,1,True,True
20260814,60.1,0.38,51.48,0.16,48.96,0.2,2,True,True
20260821,59.22,-0.88,50.92,-0.56,48.96,0,0,False,False
20260828,60.28,1.06,53.37,2.45,49.68,0.72,1,True,True
20260904,61.16,0.88,53.05,-0.32,50.48,0.8,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3362 | 先進光 | pattern | 型態觀察 | 46.0 |  |  | base_building |  |  | stale_signal | 1.重要子公司名稱:科雅光電股份有限公司 2.發生緣由(降低持股比例（或出資額）或喪失控制力):降低持股比例 3.降低持股（或出資額）比例之方式(請分別列示各次發生日期、發生原因 、方式、降低持股比例、交易數量、每單位價格及交易總金額): 發生日期：115年5月7日及115年7月9日本公司董事會決議。 發生原因：配合科雅公司股票上(市)櫃規劃，依法令規定辦理股權分散。 方式：處分科雅光電公司10%股權，共計 3,680,000 股，處分後本公司仍 持有該子公司90%股權，仍保有實質控制權與經營決策影響力。 降低持股比例：10% 交易數量：3,680,000股 每單位價格：每股新台幣68元 交易總金額：新台幣250,240千元 4.喪失控制力之方式(請列示發生日期、發生原因及方式):不適用 5.股權(或出資額)受讓對象或所洽特定對象(請分別列示各次交易對象): 大立光電股份有限公司 6.與交易對象之關係(請分別列示各次交易對象與公司之關係):無 7.處分利益(或損失)(請分別列示各次處分損益，若無處分損益請填寫不適用): 不適用 8.迄目前為止(含本次交易)，對重要子公司累積降低持股比例:10% 9.迄目前為止(含本次交易)，對重要子公司持股比例:90% 10.獨立專家姓名及其就歷次價格合理性之意見: 勝傑會計師事務所塗勝傑會計師/價格尚屬合理。 11.獨立專家姓名及其就降低持股或喪失控制力對上櫃公司股東權益影響之意見: 勝傑會計師事務所塗勝傑會計師 降低持股對本公司之股東權益並無重大影響。 12.是否影響母公司繼續上櫃:否 13.審計委員會決議日期:115/05/07及115/07/09 14.審計委員會決議內容:本案經全體出席委員同意照案通過。 15.董事會決議日期:115/05/07及115/07/09 16.董事會決議內容:本案經全體出席董事同意照案通過。 17.其他應敘明事項: 1.本次補充公告所洽特定對象、每單位價格及交易總金額。 2.本次處分案若有其他未盡事宜，擬授權董事長視實際情況 依相關法令規定辦理及擬授權董事長代表本公司簽署一切有 關辦理契約及文件，並代表本公司辦理相關事項。 3.科雅釋股案己經115年6月29日股東會決議通過。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3362 | 先進光 | 1 | 1 | 3 | 6 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
