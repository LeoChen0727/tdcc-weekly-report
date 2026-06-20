# INDIVIDUAL STOCK CHATGPT PACKET - 3092 鴻碩

## Metadata
- generated_at: 2026-06-20 22:54:12 Asia/Taipei
- stock_id: 3092
- stock_name: 鴻碩
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3092_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3092_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3092_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3092_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3092_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3092_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3092_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3092.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3092.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3092.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3092.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3092_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3092_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3092_latest.md?ref=main

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
- date: 20260618
- open: 31.95
- high: 32.8
- low: 31.25
- close: 31.3
- volume: 2106591
- ma5: 30.29
- ema23_primary: 30.07
- distance_to_ema23_pct: 4.09
- ma20: 29.96
- ma60: 30.67
- ma120: 28.79
- return_5d: 11.79
- return_20d: 7.93
- volume_ratio: 2.59
- distance_to_ma20_pct_auxiliary: 4.46
- distance_to_high_60_pct: -19.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,28.95,31.9,28.95,30.7,1042808,30.52,0.6,30.75,31.65,1.7
20260525,31,31.4,30.05,30.3,750162,30.5,-0.65,30.68,31.71,1.22
20260526,30.05,30.4,29.8,30.3,566796,30.48,-0.6,30.6,31.73,0.94
20260527,30.5,30.85,29.4,29.5,607302,30.4,-2.96,30.4,31.69,1.1
20260528,29.5,30.5,28.75,28.9,503097,30.28,-4.54,30.22,31.58,0.92
20260529,29,29.6,29,29.15,475090,30.18,-3.42,30.07,31.45,0.86
20260601,29.45,32.05,29.3,31.95,1596687,30.33,5.35,30.11,31.36,2.66
20260602,31.95,32.35,30.4,30.75,988678,30.36,1.27,30.03,31.24,1.57
20260603,31.3,31.3,30.15,30.6,491862,30.38,0.71,29.99,31.19,0.8
20260604,30.9,31.95,30.15,30.85,981838,30.42,1.41,29.93,31.19,1.55
20260605,31.2,31.2,29.95,30.15,574112,30.4,-0.82,29.89,31.18,0.92
20260608,27.15,29.55,27.15,29,720177,30.28,-4.24,29.83,31.13,1.14
20260609,29,29.5,28.7,29.2,409822,30.19,-3.29,29.75,31.08,0.64
20260610,29.2,29.9,28.5,28.5,489546,30.05,-5.16,29.67,31.02,0.77
20260611,28.05,28.7,27.6,28,330700,29.88,-6.29,29.6,30.9,0.53
20260612,28.55,29,28.4,28.8,255675,29.79,-3.33,29.58,30.79,0.42
20260615,28.85,29.85,28.85,29.85,300833,29.8,0.18,29.61,30.72,0.5
20260616,30.5,30.55,29,29.3,485182,29.75,-1.53,29.64,30.66,0.8
20260617,29.7,32.2,29.7,32.2,2568489,29.96,7.48,29.85,30.65,3.54
20260618,31.95,32.8,31.25,31.3,2106591,30.07,4.09,29.96,30.67,2.59
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 36.39
- over_600_ratio: 33.48
- over_800_ratio: 30.07
- over_1000_ratio: 29.21
- over_400_change_1w: 0.13
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.36,,30.05,,29.19,,0,False,False
20260508,33.88,-0.48,30.05,0,29.19,0,0,False,False
20260515,34.34,0.46,30.05,0,29.19,0,1,False,False
20260522,34.55,0.21,30.05,0,29.19,0,2,False,False
20260529,34.85,0.3,30.05,0,29.19,0,3,False,False
20260605,35.66,0.81,30.05,0,29.19,0,4,False,False
20260612,36.26,0.6,30.06,0.01,29.2,0.01,5,True,True
20260618,36.39,0.13,30.07,0.01,29.21,0.01,6,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3092 | 鴻碩 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.事實發生日:自民國115/6/16至民國115/6/16 2.本次新增（減少）投資方式: 現金增資 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.交易單位數量、每單位價格及交易總金額: 交易總金額：人民幣2000萬元(約新台幣92,640,000元) 6.大陸被投資公司之公司名稱: 鴻碩精密電工(湖北)有限公司 7.前開大陸被投資公司之實收資本額: 人民幣2億2000萬元 8.前開大陸被投資公司本次擬新增資本額: 人民幣2000萬元 9.前開大陸被投資公司主要營業項目: 生產經營銅品、3C產品連接線、訊號線、電動汽車用充電槍、高壓線及新能源材料 10.前開大陸被投資公司最近年度財務報表會計師意見型態: 不適用 11.前開大陸被投資公司最近年度財務報表權益總額: 民國114年12月31日財務報表權益總額為人民幣123,447仟元。 12.前開大陸被投資公司最近年度財務報表損益金額: 民國114年度財務報表稅後淨損為人民幣60,805仟元。 13.迄目前為止，對前開大陸被投資公司之實際投資金額: 人民幣2億2000萬元 14.交易相對人及其與公司之關係: 100%持有之母子公司 15.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉 之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期及移轉金額: 不適用 16.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取得 及處分日期、價格及交易當時與公司之關係: 不適用 17.處分利益（或損失）: 不適用 18.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定事項: 依資金需求匯入 19.本次交易之決定方式、價格決定之參考依據及決策單位: 交易之決定方式:現金增資 價格決定之參考依據:不適用 決策單位:董事會 20.經紀人: 不適用 21.取得或處分之具體目的: 為營運擴充及長期業務發展之需要。 22.本次交易表示異議董事之意見: 無 23.本次交易為關係人交易:是 24.監察人承認或審計委員會同意日期: 不適用 25.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）: 迄目前為止，經濟部投審會核准投資金額新台幣636,262仟元 26.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 實收資本額之比率: 59.66% 27.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 總資產之比率: 12.72% 28.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 歸屬於母公司業主之權益之比率: 47.14% 29.迄目前為止，實際赴大陸地區投資總額: 迄目前為止，赴大陸地區投資總額新台幣305,952仟元 30.迄目前為止，實際赴大陸地區投資總額占最近期財務報表實收資本額之比率: 28.69% 31.迄目前為止，實際赴大陸地區投資總額占最近期財務報表總資產之比率: 6.12% 32.迄目前為止，實際赴大陸地區投資總額占最近期財務報表歸屬於母公司業主之權益之比率: 22.67% 33.最近三年度認列投資大陸損益金額: 112年度：認列投資損失新台幣145,913仟元 113年度：認列投資損失新台幣248,452仟元 114年度：認列投資損失新台幣442,536仟元 34.最近三年度獲利匯回金額: 112年度：新台幣0仟元 113年度：新台幣0仟元 114年度：新台幣0仟元 35.本次交易會計師出具非合理性意見:不適用 36.會計師事務所名稱: 不適用 37.會計師姓名: 不適用 38.會計師開業證書字號: 不適用 39.前已就同一件事件發布重大訊息日期: 不適用 40.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3092 | 鴻碩 | 2 | 2 | 2 | 3 | 4 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
