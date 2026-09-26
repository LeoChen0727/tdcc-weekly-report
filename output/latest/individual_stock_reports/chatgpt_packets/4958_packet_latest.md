# INDIVIDUAL STOCK CHATGPT PACKET - 4958 臻鼎-KY

## Metadata
- generated_at: 2026-09-26 15:52:28 Asia/Taipei
- stock_id: 4958
- stock_name: 臻鼎-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4958_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4958_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4958.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4958.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4958.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4958.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4958_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4958_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4958_latest.md?ref=main

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
- date: 20260924
- open: 473.5
- high: 480.5
- low: 472
- close: 475.5
- volume: 20619766
- ma5: 476.1
- ema23_primary: 482.21
- distance_to_ema23_pct: -1.39
- ma20: 488.2
- ma60: 495.48
- ma120: 472.6
- return_5d: -0.1
- return_20d: -0.31
- volume_ratio: 0.66
- distance_to_ma20_pct_auxiliary: -2.6
- distance_to_high_60_pct: -27.52

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,482.5,494,468,480.5,34242675,472.47,1.7,466.77,522.67,0.99
20260831,471,504,468,500,49093086,474.76,5.32,470.7,522.8,1.43
20260901,512,550,508,535,71767430,479.78,11.51,475.25,523.32,1.99
20260902,530,531,505,507,29619988,482.05,5.18,476.2,523.23,0.81
20260903,520,525,462,464,40982476,480.55,-3.44,475.3,521.88,1.14
20260904,476,477.5,446.5,463,33930146,479.09,-3.36,474.8,521.23,0.94
20260907,472.5,508,469,501,34247775,480.91,4.18,476.32,520.77,0.95
20260908,516,524,500,505,33442577,482.92,4.57,477.07,519.98,0.93
20260909,508,515,502,502,18639881,484.51,3.61,478.6,518.52,0.54
20260910,504,512,493.5,494.5,16351309,485.34,1.89,479.45,516.36,0.5
20260911,482,504,478,495,18746769,486.15,1.82,479.73,513.96,0.61
20260914,480,498,475.5,489.5,18946773,486.43,0.63,479.05,511.42,0.64
20260915,485.5,493.5,476,477.5,19168557,485.68,-1.68,479.23,509.01,0.67
20260916,482.5,498,471,493.5,21886748,486.33,1.47,481.05,507.45,0.78
20260917,496,504,475,476,26008525,485.47,-1.95,481.7,505.6,0.92
20260918,486,491,472,473,29899628,484.43,-2.36,483.3,503.45,1.06
20260921,476.5,482,463.5,470,26718285,483.23,-2.74,485.02,501.62,0.92
20260922,480,505,480,489,45198008,483.71,1.09,487.27,500.22,1.48
20260923,471.5,482.5,470,473,39517300,482.82,-2.03,488.27,497.6,1.24
20260924,473.5,480.5,472,475.5,20619766,482.21,-1.39,488.2,495.48,0.66
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 70.2
- over_600_ratio: 68.37
- over_800_ratio: 66.83
- over_1000_ratio: 64.94
- over_400_change_1w: -1.13
- over_800_change_1w: -0.83
- over_1000_change_1w: -0.78
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,72.7,-0.35,68.29,-0.31,66.36,0.12,1,False,True
20260717,74.2,1.5,69.61,1.32,67.29,0.93,2,True,True
20260724,72.76,-1.44,68.25,-1.36,65.94,-1.35,0,False,False
20260731,73.19,0.43,68.75,0.5,66.66,0.72,1,True,True
20260807,72.84,-0.35,68.57,-0.18,66.7,0.04,2,False,True
20260814,71.39,-1.45,67.36,-1.21,65.54,-1.16,0,False,False
20260821,70.74,-0.65,66.69,-0.67,64.98,-0.56,0,False,False
20260828,70.78,0.04,66.93,0.24,65.14,0.16,1,True,True
20260904,70.95,0.17,67,0.07,65.2,0.06,2,True,True
20260911,71.15,0.2,67.43,0.43,65.78,0.58,3,True,True
20260918,71.33,0.18,67.66,0.23,65.72,-0.06,4,False,True
20260924,70.2,-1.13,66.83,-0.83,64.94,-0.78,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4958 | 臻鼎-KY | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/09/22 2.公司名稱:臻鼎科技控股股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司海外第六次無擔保轉換公司債完成訂價 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 依據金融監督管理委員會115年9月14日金管證發字第1150354528號函公告: 一、募集海外公司債總額、債券每張金額、發行價格及預定發行日期：     (一)募集海外公司債總額：美金800,000,000元。     (二)債券每張金額：         美金200,000元，如超過美金200,000元，為美金100,000元之整數倍數。     (三)發行價格：依面額100%發行。     (四)預定發行日期: 115年9月29日。 二、募集海外公司債利率：票面利率為0%。 三、募集海外公司債償還方法及期限：     (一)除本公司債已被提前贖回、購回並經註銷或債券持有人行使轉換權利情況         外，本公司債於到期日，發行公司將依面額加計年利率0%之收益率(每半年         計算一次），以美金將本公司債全數償還贖回。到期贖回金額為債券面額         的100%。     (二)期限：自發行日起滿五年之日為到期日，到期日為120年9月29日。 四、轉換辦法及重要約定事項：     (一)轉換期間：除本公司債已提前贖回、購回並經註銷、債券持有人行使轉換權         、法令規定及受託契約另行約定之停止過戶期間外，於本公司債發行日後屆         滿三個月之翌日起至(1)到期日前十日止或(2)債券持有人行使賣回權之日或         發行公司行使提前贖回權之日(不含到期日)前第五個營業日止，債券持有人         得向發行公司請求將本公司債轉換為發行公司新發行之普通股股份。         現行法令規定不得轉換之停止過戶期間如下：         1.自發行公司無償配股停止過戶日首日、現金股息停止過戶日首日或現金增           資認股停止過戶日首日前十五個營業日起，至前述權利分派基準日止。         2.如發行公司辦理減資，自發行公司辦理減資之減資基準日起至減資換發股           票開始交易日前一日止。         3.如發行公司辦理股票變更面額，自發行公司辦理股票變更面額之停止轉換           起始日至新股換發股票開始交易日前一日止。         4.其他依中華民國法律或台灣證券交易所或英屬開曼群島法律規定之停止過           戶期間。         前述有關中華民國停止過戶期間之法令如有變更時，應依修訂後法令辦理。     (二)轉換價格：本公司債之轉換價格為每股新台幣550.13元。轉換價格為參考價         格之112.5%。參考價格係指發行公司普通股於台灣證券交易所訂價日當日收         盤價新台幣489元。     (三)轉換普通股股數：轉換時，以本公司債發行面額乘以訂價日決定之新台幣兌         美金固定匯率，再除以請求轉換時之每股轉換價格，計算出可轉換為發行公         司之普通股股數。         所謂固定匯率係指本公司債訂價日當日上午十一時參考Taipei Forex Inc.所         顯示之定盤匯率，訂為1美元兌換新台幣31.715元。     (四)轉換價格之調整：本公司債發行後，轉換價格應依受託契約相關反稀釋條款         調整之。     (五)債券持有人賣回權：除下列情事發生，債券持有人不得要求發行公司於到期         日前將其持有之本公司債全部或部分贖回：         1.除已被提前贖回、買回並經註銷或債券持有人行使轉換權外，債券持有人           得於本公司債發行第三週年日，要求發行公司以本公司債之債券面額加計           年利率0%(每半年計算一次)所計算之利息補償金(以下簡稱「提前賣           回價格」)，贖回全部或部份之本公司債。         2.發行公司之普通股股票於台灣證券交易所終止上市或停止買賣時，債券持           有人得請求發行公司按提前賣回價格將本公司債全部或部份贖回。         3.發行公司有本公司債受託契約所定義之控制權變動之情事，債券持有人得           要求發行公司以提前賣回價格將本公司債全部或部份贖回。        債券持有人行使前述賣回權，及發行公司受理債券持有人之賣回請求，均應依        照受託契約約定之程序為之。本公司債提前賣回價格之付款，將由本公司依受        託契約規定之付款日以現金支付。    (六)發行公司之提前贖回權：發行公司於下列情況，得提前贖回本公司債：        1.在發行第三週年日起，如發行公司普通股在台灣證券交易所之收盤價格連續          二十個交易日（如遇除權或除息者，於除權或除息交易日至除權或除息基準          日之間，採用之收盤價格，應先設算為除權或除息前之價格）達提前贖回價          格乘以當時轉換價格再除以債券面額後所得之總數之125%時，發行公司得於          五日內發出債券贖回通知書，以提前贖回價格將本公司債全部或部份贖回；        2.超過百分之九十之本公司債已被贖回、購回並經註銷或經債券持有人行使轉          換權利時，發行公司得以提前贖回價格將本公司債全部贖回；及        3.當中華民國或英屬開曼群島或其他發行公司因稅務目的而設立或營運所在地          之稅務法令變更，致使發行公司於發行日後因本公司債而稅務負擔增加或必          須支付額外之利息費用或增加成本時，發行公司得以提前贖回價格將本公司          債全部贖回。        4.「提前贖回價格」為本公司債於相關事項發生時，發行公司依本公司債之債          券面額加計年利率0%之收益率（每半年計算一次）從發行日起計算到相          關事項發生時當天之實際經過日數（依每年360日及每月30日為基礎）計算的          金額。 五、發行及交易地點 : 新加坡證券交易所。 六、發行方式若有約定由特定人認購之情事，應公告洽特定人認購之目的，特定人認     購之張數、總金額及發行人與特定人之關係：無。 七、資金運用計劃及預計可能產生效益：充實營運資金。 八、對股東權益之主要影響：本次所發行之海外無擔保轉換公司債若於今年度全數轉     換，股本稀釋比率約為3.92%，尚無重大稀釋致影響股東權益之情事。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 4958 | 臻鼎-KY | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/09/22 2.公司名稱:臻鼎科技控股股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司海外第六次無擔保轉換公司債完成訂價 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 依據金融監督管理委員會115年9月14日金管證發字第1150354528號函公告: 一、募集海外公司債總額、債券每張金額、發行價格及預定發行日期：     (一)募集海外公司債總額：美金800,000,000元。     (二)債券每張金額：         美金200,000元，如超過美金200,000元，為美金100,000元之整數倍數。     (三)發行價格：依面額100%發行。     (四)預定發行日期: 115年9月29日。 二、募集海外公司債利率：票面利率為0%。 三、募集海外公司債償還方法及期限：     (一)除本公司債已被提前贖回、購回並經註銷或債券持有人行使轉換權利情況         外，本公司債於到期日，發行公司將依面額加計年利率0%之收益率(每半年         計算一次），以美金將本公司債全數償還贖回。到期贖回金額為債券面額         的100%。     (二)期限：自發行日起滿五年之日為到期日，到期日為120年9月29日。 四、轉換辦法及重要約定事項：     (一)轉換期間：除本公司債已提前贖回、購回並經註銷、債券持有人行使轉換權         、法令規定及受託契約另行約定之停止過戶期間外，於本公司債發行日後屆         滿三個月之翌日起至(1)到期日前十日止或(2)債券持有人行使賣回權之日或         發行公司行使提前贖回權之日(不含到期日)前第五個營業日止，債券持有人         得向發行公司請求將本公司債轉換為發行公司新發行之普通股股份。         現行法令規定不得轉換之停止過戶期間如下：         1.自發行公司無償配股停止過戶日首日、現金股息停止過戶日首日或現金增           資認股停止過戶日首日前十五個營業日起，至前述權利分派基準日止。         2.如發行公司辦理減資，自發行公司辦理減資之減資基準日起至減資換發股           票開始交易日前一日止。         3.如發行公司辦理股票變更面額，自發行公司辦理股票變更面額之停止轉換           起始日至新股換發股票開始交易日前一日止。         4.其他依中華民國法律或台灣證券交易所或英屬開曼群島法律規定之停止過           戶期間。         前述有關中華民國停止過戶期間之法令如有變更時，應依修訂後法令辦理。     (二)轉換價格：本公司債之轉換價格為每股新台幣550.13元。轉換價格為參考價         格之112.5%。參考價格係指發行公司普通股於台灣證券交易所訂價日當日收         盤價新台幣489元。     (三)轉換普通股股數：轉換時，以本公司債發行面額乘以訂價日決定之新台幣兌         美金固定匯率，再除以請求轉換時之每股轉換價格，計算出可轉換為發行公         司之普通股股數。         所謂固定匯率係指本公司債訂價日當日上午十一時參考Taipei Forex Inc.所         顯示之定盤匯率，訂為1美元兌換新台幣31.715元。     (四)轉換價格之調整：本公司債發行後，轉換價格應依受託契約相關反稀釋條款         調整之。     (五)債券持有人賣回權：除下列情事發生，債券持有人不得要求發行公司於到期         日前將其持有之本公司債全部或部分贖回：         1.除已被提前贖回、買回並經註銷或債券持有人行使轉換權外，債券持有人           得於本公司債發行第三週年日，要求發行公司以本公司債之債券面額加計           年利率0%(每半年計算一次)所計算之利息補償金(以下簡稱「提前賣           回價格」)，贖回全部或部份之本公司債。         2.發行公司之普通股股票於台灣證券交易所終止上市或停止買賣時，債券持           有人得請求發行公司按提前賣回價格將本公司債全部或部份贖回。         3.發行公司有本公司債受託契約所定義之控制權變動之情事，債券持有人得           要求發行公司以提前賣回價格將本公司債全部或部份贖回。        債券持有人行使前述賣回權，及發行公司受理債券持有人之賣回請求，均應依        照受託契約約定之程序為之。本公司債提前賣回價格之付款，將由本公司依受        託契約規定之付款日以現金支付。    (六)發行公司之提前贖回權：發行公司於下列情況，得提前贖回本公司債：        1.在發行第三週年日起，如發行公司普通股在台灣證券交易所之收盤價格連續          二十個交易日（如遇除權或除息者，於除權或除息交易日至除權或除息基準          日之間，採用之收盤價格，應先設算為除權或除息前之價格）達提前贖回價          格乘以當時轉換價格再除以債券面額後所得之總數之125%時，發行公司得於          五日內發出債券贖回通知書，以提前贖回價格將本公司債全部或部份贖回；        2.超過百分之九十之本公司債已被贖回、購回並經註銷或經債券持有人行使轉          換權利時，發行公司得以提前贖回價格將本公司債全部贖回；及        3.當中華民國或英屬開曼群島或其他發行公司因稅務目的而設立或營運所在地          之稅務法令變更，致使發行公司於發行日後因本公司債而稅務負擔增加或必          須支付額外之利息費用或增加成本時，發行公司得以提前贖回價格將本公司          債全部贖回。        4.「提前贖回價格」為本公司債於相關事項發生時，發行公司依本公司債之債          券面額加計年利率0%之收益率（每半年計算一次）從發行日起計算到相          關事項發生時當天之實際經過日數（依每年360日及每月30日為基礎）計算的          金額。 五、發行及交易地點 : 新加坡證券交易所。 六、發行方式若有約定由特定人認購之情事，應公告洽特定人認購之目的，特定人認     購之張數、總金額及發行人與特定人之關係：無。 七、資金運用計劃及預計可能產生效益：充實營運資金。 八、對股東權益之主要影響：本次所發行之海外無擔保轉換公司債若於今年度全數轉     換，股本稀釋比率約為3.92%，尚無重大稀釋致影響股東權益之情事。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4958 | 臻鼎-KY | 12 | 12 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4958 | 臻鼎-KY | 369 | 21 | 31472430.0 | 857720.0 | 36.69 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
