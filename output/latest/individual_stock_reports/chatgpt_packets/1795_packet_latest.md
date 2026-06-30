# INDIVIDUAL STOCK CHATGPT PACKET - 1795 美時

## Metadata
- generated_at: 2026-06-30 22:26:27 Asia/Taipei
- stock_id: 1795
- stock_name: 美時
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 294
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1795_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1795_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1795_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1795_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1795_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1795_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1795_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1795.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1795.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1795.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1795.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1795_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1795_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1795_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260630
- open: 193
- high: 197
- low: 191
- close: 191.5
- volume: 1424000
- ma5: 189.5
- ema23_primary: 194.56
- distance_to_ema23_pct: -1.57
- ma20: 194.15
- ma60: 207.78
- ma120: 245.28
- return_5d: 0.52
- return_20d: -3.53
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: -1.36
- distance_to_high_60_pct: -20.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,198.5,198.5,194.5,196,1286683,203.59,-3.73,203.28,219.37,0.38
20260603,196.5,197.5,194.5,196,936074,202.96,-3.43,201.75,218.17,0.28
20260604,196.5,204,195.5,201,2967400,202.8,-0.89,200.15,217.29,0.91
20260605,202,206,197,198.5,2539516,202.44,-1.95,198.25,216.29,0.83
20260608,182,197.5,182,195.5,2146712,201.86,-3.15,196.38,215,0.72
20260609,196.5,203.5,196.5,201,1806850,201.79,-0.39,195.93,214.04,0.72
20260610,200,205.5,200,202,2507321,201.81,0.1,195.75,213.46,1.03
20260611,197.5,198,192.5,194,3292212,201.16,-3.56,195.53,212.82,1.43
20260612,197,200,195,196.5,1669722,200.77,-2.13,195.7,212.1,0.77
20260615,198,203,195.5,195.5,1620889,200.33,-2.41,196.07,211.23,0.76
20260616,196,196,191,191,1996999,199.55,-4.29,196.18,210.69,0.96
20260617,189.5,195,188.5,193.5,1402915,199.05,-2.79,196.22,210.35,0.68
20260618,193,196,193,193,972613,198.54,-2.79,195.95,210.14,0.49
20260622,194.5,194.5,191,191.5,1532359,197.96,-3.26,195.47,209.94,0.79
20260623,192,194,189,190.5,1383337,197.34,-3.46,195.12,209.58,0.74
20260624,189.5,194.5,189,193.5,1308810,197.02,-1.78,195.15,209.33,0.71
20260625,194,195,189,189,1585537,196.35,-3.74,195.03,208.9,0.87
20260626,188.5,188.5,183,183,2533725,195.24,-6.27,194.72,208.43,1.35
20260629,184.5,194.5,184.5,190.5,1829555,194.84,-2.23,194.5,208.15,1
20260630,193,197,191,191.5,1424000,194.56,-1.57,194.15,207.78,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 57.14
- over_600_ratio: 55.25
- over_800_ratio: 54.48
- over_1000_ratio: 52.68
- over_400_change_1w: -0.25
- over_800_change_1w: -0.51
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.44,,55.75,,54.68,,0,False,False
20260508,58.97,-0.47,55.77,0.02,55.03,0.35,1,False,True
20260515,57.68,-1.29,54.58,-1.19,53.49,-1.54,0,False,False
20260522,57.37,-0.31,54.33,-0.25,52.91,-0.58,0,False,False
20260529,57.34,-0.03,54.21,-0.12,53.12,0.21,1,False,True
20260605,57.45,0.11,54.58,0.37,53.15,0.03,2,True,True
20260612,57.48,0.03,55.01,0.43,52.93,-0.22,3,False,True
20260618,57.39,-0.09,54.99,-0.02,52.86,-0.07,0,False,False
20260626,57.14,-0.25,54.48,-0.51,52.68,-0.18,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1795 | 美時 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 本公司100%持股之韓國子公司Alvogen Korea Holdings Ltd.普通股 2.事實發生日:115/6/26~115/6/26 3.董事會通過日期: 民國115年6月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易單位數量：154,779股 每單位價格：美金85.57元 交易總金額：美金13,245,033.11元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: Alvogen Korea Holdings Ltd.為本公司100%持有之子公司。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 不適用 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格參酌會計師出具之交易價格合理性意見書，經本公司董事會同意後執行。 13.取得或處分有價證券標的公司每股淨值: 2,735.18元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 累積持股：1,611,378股 累積金額：新台幣5,277,342,848元 持股比例：100% 權利受限情形：無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 占總資產比例：51.63% 占歸屬於母公司業主之權益之比例：110.08% 營運資金數額：6,168,243,683元 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 提升營運資金使用效率 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:是 20.監察人承認或審計委員會同意日期: 民國115年6月25日 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 揚智聯合會計師事務所 23.會計師姓名: 胡湘寧 24.會計師開業證書字號: 中市會證字第0191號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 1.本次增資總額係本公司資金貸與Alvogen Korea Holdings Ltd.之債權轉為增資款。 2.實際增資發行股數依增資基準日轉換股數為準。 3.本次交易金額係以民國115年6月22日臺灣銀行牌告匯率1美元對31.64元台幣計算之。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1795 | 美時 | 6 | 6 | 5 | 9 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1795 | 美時 | 128 | 0 | 1872600.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
