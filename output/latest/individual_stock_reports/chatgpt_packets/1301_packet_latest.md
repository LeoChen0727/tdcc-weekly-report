# INDIVIDUAL STOCK CHATGPT PACKET - 1301 台塑

## Metadata
- generated_at: 2026-07-15 22:26:22 Asia/Taipei
- stock_id: 1301
- stock_name: 台塑
- packet_status: standard_180d_window_packet
- latest_price_date: 20260715
- price_rows: 304
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1301_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1301_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1301_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1301_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1301_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1301_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1301_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1301.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1301.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1301.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1301.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1301_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1301_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1301_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260715
- open: 64
- high: 66.4
- low: 63
- close: 65.7
- volume: 146834938
- ma5: 60.46
- ema23_primary: 55.99
- distance_to_ema23_pct: 17.35
- ma20: 55.84
- ma60: 50.75
- ma120: 48.93
- return_5d: 14.66
- return_20d: 39.05
- volume_ratio: 1.86
- distance_to_ma20_pct_auxiliary: 17.65
- distance_to_high_60_pct: -1.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260616,47.3,48.65,46.65,46.75,26097670,47.07,-0.67,46.77,48.24,0.84
20260617,46.7,48,46.35,47.95,18656628,47.14,1.72,46.9,48.24,0.6
20260618,48.4,51.8,48.4,51.7,188508912,47.52,8.79,47.19,48.36,4.73
20260622,52.7,53.5,51.7,52.4,51915785,47.93,9.33,47.55,48.48,1.24
20260623,52.8,53.2,49.25,49.55,36737370,48.06,3.09,47.79,48.55,0.86
20260624,49.1,54.5,48.15,54.5,79265972,48.6,12.14,48.27,48.66,1.74
20260625,55,59.8,54.3,58,146735751,49.38,17.45,48.9,48.85,2.84
20260626,57.5,57.5,52.2,52.2,62630829,49.62,5.21,49.26,48.91,1.16
20260629,52.7,53.5,52.1,53.2,21674448,49.92,6.58,49.55,49.03,0.41
20260630,53.5,55,53,54.5,36485840,50.3,8.35,49.77,49.17,0.71
20260701,54.9,55.4,52.8,54.3,44833315,50.63,7.25,49.94,49.31,0.88
20260702,53.2,59.7,52.8,59.7,112956008,51.39,16.18,50.33,49.51,2.09
20260703,60.6,64,59,62.1,190058976,52.28,18.78,50.89,49.76,3.11
20260706,63.2,63.3,60,60.4,75892637,52.96,14.06,51.47,49.97,1.19
20260707,60.1,60.2,57,57.3,47904642,53.32,7.47,52.04,50.15,0.75
20260708,57,58.5,56.5,58,44630328,53.71,7.99,52.66,50.26,0.68
20260709,58.4,58.4,54.7,54.8,56581393,53.8,1.86,53.18,50.27,0.85
20260713,56,60.2,56,60.2,52147050,54.33,10.8,54,50.4,0.77
20260714,61.5,63.6,59.4,63.6,140549256,55.11,15.42,54.92,50.55,1.91
20260715,64,66.4,63,65.7,146834938,55.99,17.35,55.84,50.75,1.86
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 74.8
- over_600_ratio: 73.76
- over_800_ratio: 72.9
- over_1000_ratio: 72.19
- over_400_change_1w: 0.25
- over_800_change_1w: 0.35
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,73.72,,71.75,,71.12,,0,False,False
20260508,73.75,0.03,71.81,0.06,71.16,0.04,1,True,True
20260515,73.19,-0.56,71.18,-0.63,70.58,-0.58,0,False,False
20260522,73.02,-0.17,70.95,-0.23,70.32,-0.26,0,False,False
20260529,72.89,-0.13,70.84,-0.11,70.18,-0.14,0,False,False
20260605,73.36,0.47,71.3,0.46,70.67,0.49,1,True,True
20260612,72.57,-0.79,70.47,-0.83,69.81,-0.86,0,False,False
20260618,72.83,0.26,70.78,0.31,70.18,0.37,1,True,True
20260626,74.55,1.72,72.55,1.77,71.92,1.74,2,True,True
20260703,74.8,0.25,72.9,0.35,72.19,0.27,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1301 | 台塑 | true_breakout | 嚴格突破 | 84.0 |  |  | platform_breakout |  | call_put_bullish | continued_overheated | 1.事實發生日:115/07/09 2.公司名稱:台灣塑膠工業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司2026年第2季自結合併損益 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 一、2026年第2季自結合併損益與2026年第1季比較： （一）2026年第2季合併營業額472億元，比上季增加52億元，成長12.5％，說明如下： 1.銷售價差方面，增加127.5億元： 2月底美伊戰爭爆發，荷姆茲海峽遭封鎖，波斯灣原油及輕油供應中斷，推升2026年 第2季布蘭特原油、乙烯及丙烯合約價格，分別比第1季上漲23.3％、36.8％及37.8％， 因此，本公司2026年第2季各主要產品平均價格比第1季上漲，幅度介於27~64％。 2.銷售量差方面，減少74.8億元： 2月底美伊戰爭，中東原油及輕油無法透過荷姆茲海峽出口，中油及台塑石化公司乙烯、 丙烯打折供應，本公司調降各產品開工率，且6月中東局勢趨緩，原油價格走跌，客戶 採購觀望，石化產品需求萎縮，因此，本公司2026年第2季各主要產品銷售量，合計 比第1季減少28萬噸。 （二）2026年第2季本業利益28億元，比上季虧損13億元，增加41億元，合併稅前利益 108億元，比上季增加74億元，每股稅前盈餘為1.71元，合併稅後利益106億元，比上季 增加73億元，歸屬母公司每股稅後盈餘為1.67元，說明如下： 1.受美伊戰爭影響，推升石化產品價格，加上本公司有前期低成本的庫存，產品利差 明顯改善，致使第2季本業轉虧為盈。 2.認列權益法投資收益83.5億元，比上季增加33億元，主要係： A.台塑石化公司：認列59.1億元，比上季增加2.1億元； B.台塑美國公司：認列18.8億元，比上季增加20億元，主要係美伊戰爭導致石化產品 價格大漲，但美國天然氣及能源價格漲幅相對較小，產品利差擴大所致。 C.台塑烯烴美國公司：認列11.1億元，比上季增加9.1億元，主要係原料乙烷價格漲幅 小於產品乙烯漲幅，利差擴大所致。 3.第2季有現金股利收入2.3億元。 4.第2季兌換利益0.3億元，比第1季兌換利益2.3億元，減少利益2億元。 二、2026年上半年自結合併損益與2025年上半年比較： （一）2026年上半年合併營業額892億元，比去年同期減少33億元，衰退3.6％， 說明如下： 1.銷售量差方面，減少114.9億元： 2026年上半年受美伊戰爭，以及中油天然氣管線施工、四輕歲修與新三輕設備故障等 影響，中油及台塑石化公司乙烯、丙烯打折供應，本公司開工率降低，因此，2026年 上半年各主要產品銷售量，合計比去年同期減少39.1萬噸。 2.銷售價差方面，增加81.4億元： 2026年上半年因美伊戰爭，原油及乙烯、丙烯價格大漲，本公司為反應原料成本，調漲 各產品售價，因此，本公司2026年上半年各主要產品平均價格比去年同期上漲，幅度 介於6~19％。 （二）2026年上半年本業利益15億元，比去年同期虧損25億元，增加40億元，合併 稅前利益142億元，比去年同期增加209億元，每股稅前盈餘為2.24元，合併稅後利益 139億元，比去年同期增加204億元，歸屬母公司每股稅後盈餘為2.19元，說明如下： 1.去年上半年因美國實施對等關稅，客戶採購保守，且石化同業新增產能陸續投產， 壓低石化產品市場行情，本業產生虧損，今年受美伊戰爭影響，國際原油及石化產品 價格上漲，利差明顯改善，因此，今年上半年本業轉虧為盈。 2.認列權益法投資收益133.9億元，比去年同期認列虧損12.1億元，增加146億元， 主要係： A.認列台塑石化公司比去年同期增加126億元。 B.認列台塑美國公司比去年同期增加23億元，主要因各產品售價上漲，產品利差擴大。 3.現金股利收入2.3億元，比去年同期增加0.7億元。 4.今年上半年兌換利益2.6億元，比去年同期兌換損失17.1億元，增加利益19.7億元。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1301 | 台塑 | 4 | 1 | 4 | 6 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1301 | 台塑 | 109 | 4 | 39714590.0 | 176470.0 | 225.05 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
