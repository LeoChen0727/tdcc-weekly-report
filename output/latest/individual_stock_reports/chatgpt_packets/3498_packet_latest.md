# INDIVIDUAL STOCK CHATGPT PACKET - 3498 陽程

## Metadata
- generated_at: 2026-07-10 22:27:20 Asia/Taipei
- stock_id: 3498
- stock_name: 陽程
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 166
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3498.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3498.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3498_latest.md?ref=main

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
- date: 20260709
- open: 124
- high: 131
- low: 124
- close: 126.5
- volume: 4601000
- ma5: 123.4
- ema23_primary: 122.83
- distance_to_ema23_pct: 2.98
- ma20: 120.6
- ma60: 117.96
- ma120: 89.62
- return_5d: 2.85
- return_20d: 2.85
- volume_ratio: 2.76
- distance_to_ma20_pct_auxiliary: 4.89
- distance_to_high_60_pct: -23.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,119,121,112,115.5,3671000,129.56,-10.86,141.45,103.74,2.23
20260612,123,125.5,119,121,1246000,128.85,-6.09,140.05,104.52,0.93
20260615,127,131,124,125.5,1060000,128.57,-2.39,139.1,105.38,1.16
20260616,129,130.5,119.5,120.5,1531000,127.9,-5.78,138.3,106.14,1.68
20260617,118,120.5,116.5,119,805000,127.16,-6.42,137.07,106.91,0.91
20260618,119,125,119,123,979000,126.81,-3.01,135.9,107.76,1.1
20260622,125,129.5,122.5,123,1143000,126.49,-2.76,134.05,108.61,1.22
20260623,125.5,126,117.5,118.5,942000,125.83,-5.82,132.03,109.27,0.96
20260624,118,127,117.5,122.5,1162000,125.55,-2.43,130.4,110.06,1.13
20260625,122.5,122.5,115,118.5,1092000,124.96,-5.17,128.55,110.79,1.02
20260626,117.5,118.5,113,113,727000,123.97,-8.85,126.95,111.43,0.66
20260629,113,116.5,113,114.5,527000,123.18,-7.04,125.12,112.19,0.47
20260630,121,122.5,118,118.5,744000,122.79,-3.49,123.85,112.95,0.65
20260701,120.5,122.5,118,119,682000,122.47,-2.83,122.78,113.72,0.57
20260702,117,127.5,116,123,1659000,122.52,0.4,122.03,114.57,1.31
20260703,123,124.5,120.5,124,966000,122.64,1.11,121.6,115.36,0.74
20260706,125.5,128,124,124,1114000,122.75,1.02,121.28,116.03,0.82
20260707,125.5,136,122.5,123,5016000,122.77,0.18,121.05,116.75,3.45
20260708,124,130.5,116.5,119.5,3647000,122.5,-2.45,120.42,117.28,2.39
20260709,124,131,124,126.5,4601000,122.83,2.98,120.6,117.96,2.76
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 51.84
- over_600_ratio: 49.53
- over_800_ratio: 48.31
- over_1000_ratio: 46.89
- over_400_change_1w: 1.24
- over_800_change_1w: 0.59
- over_1000_change_1w: 1.88
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.12,,43.66,,40.56,,0,False,False
20260508,45.03,-1.09,43.34,-0.32,40.43,-0.13,0,False,False
20260515,51.96,6.93,47.64,4.3,46.04,5.61,1,True,True
20260522,54.51,2.55,51.9,4.26,49.07,3.03,2,True,True
20260529,54.6,0.09,50.24,-1.66,48.83,-0.24,3,False,False
20260605,52.18,-2.42,47.69,-2.55,47.69,-1.14,0,False,False
20260612,51.42,-0.76,47.35,-0.34,47.35,-0.34,0,False,False
20260618,51.39,-0.03,46.76,-0.59,45.14,-2.21,0,False,False
20260626,50.6,-0.79,47.72,0.96,45.01,-0.13,1,False,True
20260703,51.84,1.24,48.31,0.59,46.89,1.88,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3498 | 陽程 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | 1.法律事件之當事人:上海陽程科技有限公司 2.法律事件之法院名稱或處分機關:河南省林州市人民法院 3.法律事件之相關文書案號:河南省林州市人民法院判決書                        （2025）豫0581民初7776號 4.事實發生日:115/07/09 5.發生原委(含爭訟標的):本公司之子公司上海陽程科技有限公司於2020年9月委由 北京市道成律師事務所，處理上海陽程科技有限公司與林州致遠電子科技有限公司間 承攬合同糾紛案說判決說明。 判決結果： 我方總計須在判決生效後 15 日內支付給原告人民幣23,998,347.23元，明細如下： ‧賠償金：人民幣23,163,739.23元（含已維修費、未維修貶值、停產及品質損失）。 ‧鑑定費：人民幣689,900元。 ‧案件受理費：人民幣139,708元。 ‧保全申請費：人民幣5,000元。 6.處理過程:提出上訴並持續與律師溝通。 7.對公司財務業務影響及預估影響金額:本案本公司已提列足額損失準備， 對財務業務無重大影響。因先前對造超額聲請財產保全應付予本公司貨款， 若依本次判決結果，本公司可聲請發還約人民幣789萬元之款項。 8.因應措施及改善情形: 本公司認為，原審裁判結果顯流於地方保護主義，對於本公司提出之多處明顯爭點未予 審酌，更刻意迴避訴訟時效等重大法律事實，在無法律依據下全盤採納對造主張，其 認事用法顯失公正。 為維護本公司權益擬提起上訴。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):不適用 |
| 20260709 | 3498 | 陽程 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.法律事件之當事人:上海陽程科技有限公司 2.法律事件之法院名稱或處分機關:河南省林州市人民法院 3.法律事件之相關文書案號:河南省林州市人民法院判決書                        （2025）豫0581民初7776號 4.事實發生日:115/07/09 5.發生原委(含爭訟標的):本公司之子公司上海陽程科技有限公司於2020年9月委由 北京市道成律師事務所，處理上海陽程科技有限公司與林州致遠電子科技有限公司間 承攬合同糾紛案說判決說明。 判決結果： 我方總計須在判決生效後 15 日內支付給原告人民幣23,998,347.23元，明細如下： ‧賠償金：人民幣23,163,739.23元（含已維修費、未維修貶值、停產及品質損失）。 ‧鑑定費：人民幣689,900元。 ‧案件受理費：人民幣139,708元。 ‧保全申請費：人民幣5,000元。 6.處理過程:提出上訴並持續與律師溝通。 7.對公司財務業務影響及預估影響金額:本案本公司已提列足額損失準備， 對財務業務無重大影響。因先前對造超額聲請財產保全應付予本公司貨款， 若依本次判決結果，本公司可聲請發還約人民幣789萬元之款項。 8.因應措施及改善情形: 本公司認為，原審裁判結果顯流於地方保護主義，對於本公司提出之多處明顯爭點未予 審酌，更刻意迴避訴訟時效等重大法律事實，在無法律依據下全盤採納對造主張，其 認事用法顯失公正。 為維護本公司權益擬提起上訴。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):不適用 |
| 20260709 | 3498 | 陽程 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.法律事件之當事人:上海陽程科技有限公司 2.法律事件之法院名稱或處分機關:河南省林州市人民法院 3.法律事件之相關文書案號:河南省林州市人民法院判決書                        （2025）豫0581民初7776號 4.事實發生日:115/07/09 5.發生原委(含爭訟標的):本公司之子公司上海陽程科技有限公司於2020年9月委由 北京市道成律師事務所，處理上海陽程科技有限公司與林州致遠電子科技有限公司間 承攬合同糾紛案說判決說明。 判決結果： 我方總計須在判決生效後 15 日內支付給原告人民幣23,998,347.23元，明細如下： ‧賠償金：人民幣23,163,739.23元（含已維修費、未維修貶值、停產及品質損失）。 ‧鑑定費：人民幣689,900元。 ‧案件受理費：人民幣139,708元。 ‧保全申請費：人民幣5,000元。 6.處理過程:提出上訴並持續與律師溝通。 7.對公司財務業務影響及預估影響金額:本案本公司已提列足額損失準備， 對財務業務無重大影響。因先前對造超額聲請財產保全應付予本公司貨款， 若依本次判決結果，本公司可聲請發還約人民幣789萬元之款項。 8.因應措施及改善情形: 本公司認為，原審裁判結果顯流於地方保護主義，對於本公司提出之多處明顯爭點未予 審酌，更刻意迴避訴訟時效等重大法律事實，在無法律依據下全盤採納對造主張，其 認事用法顯失公正。 為維護本公司權益擬提起上訴。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):不適用；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3498 | 陽程 | 4 | 4 | 4 | 5 | 7 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

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
