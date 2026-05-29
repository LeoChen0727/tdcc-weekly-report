# Stock Theme Taxonomy Review / 族群分類校對清單

- generated_at: 2026-05-29 23:54:29 Asia/Taipei
- source_candidates: output/latest/all_candidates_latest.csv
- source_taxonomy: output/latest/stock_theme_taxonomy_latest.csv

## How To Read

- `市場族群=待補`：目前只有官方產業，還沒有市場所謂題材族群。這類股票不可直接進主流資金線。
- `industry_core_needs_market_theme`：官方產業像電子 / 半導體 / 通訊，但仍缺市場族群，例如低軌衛星、光通訊、機器人、被動元件、PCB/CCL。
- `core_ai_related_theme`：已明確對應到 AI / 電子 / 機器人 / 被動元件 / PCB / 低軌衛星 / 光通訊 / 半導體等核心族群。
- `industry_non_mainstream_only`：目前只看得到非主流產業，且沒有核心題材覆蓋。
- `non_mainstream_theme`：已明確標示為非主流市場族群。
- `mapped_needs_review`：已有映射，但信心較低或需要人工複查。

## Why Some Rows Are Blank

空白不是程式壞掉，而是代表 `data/theme_events/stock_theme_taxonomy.csv` 還沒有這檔股票的人工市場族群映射。已分類的股票來自這份 taxonomy 主檔；未分類股票只能暫時依官方產業與當日訊號列入待校對。

## Summary

| taxonomy_review_status           |   count |
|:---------------------------------|--------:|
| core_ai_related_theme            |     133 |
| industry_core_needs_market_theme |     259 |
| industry_non_mainstream_only     |     211 |
| mapped_needs_review              |       5 |
| non_mainstream_theme             |       1 |


## Needs Market Theme Mapping

_No rows._

## Industry Core But Market Theme Missing

_rows shown: 120 / 259_

- `3311` 閎暉｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=6.79
- `3050` 鈺德｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=1.48
- `6224` 聚鼎｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=1.59
- `3027` 盛達｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.71
- `8070` 長華*｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.54
- `4545` 銘鈺｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=4.95
- `2425` 承啟｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.54
- `2419` 仲琦｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.23
- `6438` 迅得｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.76
- `6672` 騰輝電子-KY｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.61
- `2332` 友訊｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.54
- `1582` 信錦｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.87
- `6206` 飛捷｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `3356` 奇偶｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.6
- `3060` 銘異｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.6
- `2425` 承啟｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.54
- `3591` 艾笛森｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.91
- `8213` 志超｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.87
- `2438` 翔耀｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=5.08
- `3030` 德律｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.64
- `5309` 系統電｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6104` 創惟｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6226` 光鼎｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.31
- `2342` 茂矽｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.16
- `6202` 盛群｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.0
- `6438` 迅得｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.76
- `2347` 聯強｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.2
- `3028` 增你強｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.63
- `3406` 玉晶光｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6209` 今國光｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `3356` 奇偶｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.6
- `3031` 佰鴻｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.06
- `6206` 飛捷｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `6116` 彩晶｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.27
- `3588` 通嘉｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.44
- `6438` 迅得｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pullback_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.76
- `2426` 鼎元｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.43
- `3518` 柏騰｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.04
- `7769` 鴻勁｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.63
- `8162` 微矽電子-創｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.87
- `4949` 有成精密｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `6573` 虹揚-KY｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=5.16
- `2406` 國碩｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.22
- `2467` 志聖｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.94
- `4934` 太極｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.74
- `3702` 大聯大｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.71
- `2363` 矽統｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.64
- `6426` 統新｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.51
- `2465` 麗臺｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.5
- `3406` 玉晶光｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.46
- `8021` 尖點｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.2
- `3066` 李洲｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `3550` 聯穎｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `4749` 新應材｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `4931` 新盛力｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `4976` 佳凌｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `5452` 佶優｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `5471` 松翰｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6126` 信音｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6411` 晶焱｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6451` 訊芯-KY｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6462` 神盾｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `8249` 菱光｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6830` 汎銓｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.87
- `2363` 矽統｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `3217` 優群｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2352` 佳世達｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `2385` 群光｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.85
- `3390` 旭軟｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `3030` 德律｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.64
- `3059` 華晶科｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.55
- `5371` 中光電｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2476` 鉅祥｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `3003` 健和興｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.28
- `3550` 聯穎｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.52
- `2455` 全新｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.23
- `6282` 康舒｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.98
- `2362` 藍天｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `3045` 台灣大｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `5471` 松翰｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.74
- `2379` 瑞昱｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.9
- `3592` 瑞鼎｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.84
- `8109` 博大｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2498` 宏達電｜產業=通信網路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.48
- `2476` 鉅祥｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `2405` 輔信｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.3
- `3003` 健和興｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.28
- `8039` 台虹｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.28
- `2406` 國碩｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.22
- `4952` 凌通｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.12
- `3022` 威強電｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.95
- `2467` 志聖｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.94
- `4949` 有成精密｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.92
- `3321` 同泰｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=3.57
- `3702` 大聯大｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.71
- `3312` 弘憶股｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.86
- `6695` 芯鼎｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.8
- `3034` 聯詠｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.78
- `7769` 鴻勁｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.63
- `8215` 明基材｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.69
- `3028` 增你強｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.63
- `6515` 穎崴｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=2.38
- `8163` 達方｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.38
- `2329` 華泰｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.49
- `6531` 愛普*｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.92
- `8112` 至上｜產業=電子通路業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.87
- `3257` 虹冠電｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6155` 鈞寶｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2328` 廣宇｜產業=電子零組件業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.69
- `2303` 聯電｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.51
- `3041` 揚智｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.76
- `3094` 聯傑｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.66
- `3545` 敦泰｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.66
- `6526` 達發｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.52
- `6698` 旭暉應材｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.98
- `3016` 嘉晶｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.0
- `6209` 今國光｜產業=光電業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.65
- `2465` 麗臺｜產業=電腦及週邊設備業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.5
- `8021` 尖點｜產業=其他電子業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.2
- `6799` 來頡｜產業=半導體業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.29

## Core AI-Related Theme

_rows shown: 120 / 133_

- `2485` 兆赫｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=low｜分類=revenue_pullback；評級=B_confirm_needed；風險桶=normal；量比=0.9｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2485` 兆赫｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=low｜分類=pattern；評級=C_watch_only；風險桶=normal；量比=0.9｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6284` 佳邦｜產業=電子零組件業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=low｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6235` 華孚｜產業=電腦及週邊設備業｜市場族群=AI伺服器/機構件｜bucket=ai_server_mechanical_theme｜信心=medium｜分類=range_rebound；評級=A_priority_watch；風險桶=normal；量比=2.45｜註記=AI機構件觀察
- `2353` 宏碁｜產業=電腦及週邊設備業｜市場族群=AI PC/品牌通路｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=range_rebound；評級=B_confirm_needed；風險桶=risk_watch；量比=1.74｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6862` 三集瑞-KY｜產業=電子零組件業｜市場族群=被動元件｜bucket=passive_component_theme｜信心=high｜分類=range_rebound；評級=B_confirm_needed；風險桶=risk_watch；量比=2.82｜註記=族群優先於官方產業；被動元件/電感
- `2420` 新巨｜產業=電子零組件業｜市場族群=電源供應鏈｜bucket=power_supply_theme｜信心=high｜分類=range_rebound；評級=B_confirm_needed；風險桶=risk_watch；量比=1.6｜註記=電源供應鏈
- `2317` 鴻海｜產業=其他電子業｜市場族群=機器人/AI製造｜bucket=robotics_ai_manufacturing_theme｜信心=medium｜分類=pattern；評級=B_confirm_needed；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2353` 宏碁｜產業=電腦及週邊設備業｜市場族群=AI PC/品牌通路｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=pattern；評級=B_confirm_needed；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `1597` 直得｜產業=電機機械｜市場族群=機器人/精密傳動｜bucket=robotics_precision_motion_theme｜信心=medium｜分類=revenue_pullback；評級=B_confirm_needed；風險桶=risk_watch；量比=1.82｜註記=機器人精密傳動觀察
- `3583` 辛耘｜產業=半導體業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=high｜分類=pattern；評級=B_confirm_needed；風險桶=normal；量比=1.55｜註記=半導體設備材料主流供應鏈
- `4576` 大銀微系統｜產業=電機機械｜市場族群=機器人/精密傳動｜bucket=robotics_precision_motion_theme｜信心=high｜分類=revenue_pullback；評級=B_confirm_needed；風險桶=normal；量比=0.76｜註記=族群優先於官方產業；與上銀同屬精密傳動/機器人供應鏈
- `3019` 亞光｜產業=光電業｜市場族群=機器人/光學感測｜bucket=robotics_optics_sensor_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=1.16｜註記=機器人光學感測觀察
- `2317` 鴻海｜產業=其他電子業｜市場族群=機器人/AI製造｜bucket=robotics_ai_manufacturing_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.81｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8374` 羅昇｜產業=電機機械｜市場族群=機器人/自動化｜bucket=robotics_automation_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.53｜註記=機器人自動化元件觀察
- `2357` 華碩｜產業=電腦及週邊設備業｜市場族群=AI PC/電競｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=AI PC與電競觀察
- `6412` 群電｜產業=電子零組件業｜市場族群=電源供應鏈｜bucket=power_supply_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=電源供應鏈觀察
- `2049` 上銀｜產業=電機機械｜市場族群=機器人/精密傳動｜bucket=robotics_precision_motion_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=normal；量比=1.18｜註記=族群優先於官方產業；機器人與精密傳動代表股
- `2367` 燿華｜產業=電子零組件業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=normal；量比=1.15｜註記=低軌衛星PCB觀察
- `2375` 凱美｜產業=電子零組件業｜市場族群=被動元件｜bucket=passive_component_theme｜信心=high｜分類=true_breakout；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.75｜註記=被動元件族群
- `2345` 智邦｜產業=通信網路業｜市場族群=網通/光通訊｜bucket=network_optical_datacenter_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=1.02｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2451` 創見｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.92｜註記=記憶體模組觀察
- `3413` 京鼎｜產業=半導體業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=半導體設備觀察
- `6862` 三集瑞-KY｜產業=電子零組件業｜市場族群=被動元件｜bucket=passive_component_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=族群優先於官方產業；被動元件/電感
- `4906` 正文｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=medium｜分類=true_breakout；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.74｜註記=低軌衛星/網通觀察
- `2376` 技嘉｜產業=電腦及週邊設備業｜市場族群=AI伺服器/AI PC｜bucket=ai_server_pc_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.97｜註記=AI伺服器/AI PC交集
- `2357` 華碩｜產業=電腦及週邊設備業｜市場族群=AI PC/電競｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.71｜註記=AI PC與電競觀察
- `3680` 家登｜產業=半導體業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=半導體設備材料觀察
- `2368` 金像電｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.86｜註記=高階PCB/AI伺服器板
- `1590` 亞德客-KY｜產業=電機機械｜市場族群=機器人/氣動自動化｜bucket=robotics_automation_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=1.45｜註記=族群優先於官方產業；亞德客-KY屬機器人與工業自動化供應鏈
- `6414` 樺漢｜產業=電腦及週邊設備業｜市場族群=機器人/工業電腦｜bucket=robotics_ipc_edge_ai_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.63｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2382` 廣達｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=1.3｜註記=AI伺服器主流供應鏈
- `3044` 健鼎｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=1.02｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2383` 台光電｜產業=電子零組件業｜市場族群=高速CCL/低軌衛星｜bucket=high_speed_ccl_satellite_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.88｜註記=可同時屬高階CCL與低軌衛星材料供應鏈
- `2374` 佳能｜產業=光電業｜市場族群=機器人/光學感測｜bucket=robotics_optics_sensor_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.72｜註記=族群優先於官方產業；佳能屬機器人光學感測/機器視覺供應鏈
- `6215` 和椿｜產業=其他電子業｜市場族群=機器人/自動化｜bucket=robotics_precision_motion_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.5｜註記=機器人自動化觀察
- `2374` 佳能｜產業=光電業｜市場族群=機器人/光學感測｜bucket=robotics_optics_sensor_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=族群優先於官方產業；佳能屬機器人光學感測/機器視覺供應鏈
- `3483` 力致｜產業=電腦及週邊設備業｜市場族群=散熱｜bucket=thermal_solution_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6485` 點序｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3035` 智原｜產業=半導體業｜市場族群=ASIC/先進製程｜bucket=asic_advanced_process_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3019` 亞光｜產業=光電業｜市場族群=機器人/光學感測｜bucket=robotics_optics_sensor_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=1.16｜註記=機器人光學感測觀察
- `2317` 鴻海｜產業=其他電子業｜市場族群=機器人/AI製造｜bucket=robotics_ai_manufacturing_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.81｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `1597` 直得｜產業=電機機械｜市場族群=機器人/精密傳動｜bucket=robotics_precision_motion_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=1.82｜註記=機器人精密傳動觀察
- `8028` 昇陽半導體｜產業=半導體業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.38｜註記=半導體服務/材料觀察
- `6223` 旺矽｜產業=半導體業｜市場族群=半導體測試介面｜bucket=semiconductor_test_interface_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2395` 研華｜產業=電腦及週邊設備業｜市場族群=機器人/工業電腦｜bucket=robotics_ipc_edge_ai_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.86｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3715` 定穎投控｜產業=電子零組件業｜市場族群=PCB/車用高頻板｜bucket=pcb_ccl_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=risk_watch；量比=0.6｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2376` 技嘉｜產業=電腦及週邊設備業｜市場族群=AI伺服器/AI PC｜bucket=ai_server_pc_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.97｜註記=AI伺服器/AI PC交集
- `8210` 勤誠｜產業=電腦及週邊設備業｜市場族群=AI伺服器/機殼｜bucket=ai_server_mechanical_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=normal；量比=0.65｜註記=AI伺服器機殼供應鏈
- `3044` 健鼎｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=1.02｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2451` 創見｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.92｜註記=記憶體模組觀察
- `2356` 英業達｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=AI伺服器供應鏈觀察
- `4906` 正文｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=低軌衛星/網通觀察
- `2383` 台光電｜產業=電子零組件業｜市場族群=高速CCL/低軌衛星｜bucket=high_speed_ccl_satellite_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.88｜註記=可同時屬高階CCL與低軌衛星材料供應鏈
- `2395` 研華｜產業=電腦及週邊設備業｜市場族群=機器人/工業電腦｜bucket=robotics_ipc_edge_ai_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.86｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2359` 所羅門｜產業=其他電子業｜市場族群=機器人/自動化｜bucket=robotics_automation_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.8｜註記=機器人系統整合觀察
- `6414` 樺漢｜產業=電腦及週邊設備業｜市場族群=機器人/工業電腦｜bucket=robotics_ipc_edge_ai_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.63｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3661` 世芯-KY｜產業=半導體業｜市場族群=ASIC/先進製程｜bucket=asic_advanced_process_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=normal；量比=1.05｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3380` 明泰｜產業=通信網路業｜市場族群=網通/光通訊｜bucket=network_optical_datacenter_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=2.26｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8271` 宇瞻｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.71｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3596` 智易｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.74｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3704` 合勤控｜產業=通信網路業｜市場族群=網通/通訊｜bucket=network_communication_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8374` 羅昇｜產業=電機機械｜市場族群=機器人/自動化｜bucket=robotics_automation_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.53｜註記=機器人自動化元件觀察
- `2365` 昆盈｜產業=電腦及週邊設備業｜市場族群=機器人/周邊零組件｜bucket=robotics_component_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.66｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3533` 嘉澤｜產業=電子零組件業｜市場族群=高速傳輸/連接器｜bucket=high_speed_interconnect_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.63｜註記=高速連接器主流供應鏈
- `4938` 和碩｜產業=電腦及週邊設備業｜市場族群=AI PC/消費電子｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.23｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2356` 英業達｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.78｜註記=AI伺服器供應鏈觀察
- `2481` 強茂｜產業=半導體業｜市場族群=半導體｜bucket=semiconductor_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.68｜註記=auto mapped from theme_tags=power_discrete_theme;diodes;diode;power discrete
- `6215` 和椿｜產業=其他電子業｜市場族群=機器人/自動化｜bucket=robotics_precision_motion_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.5｜註記=機器人自動化觀察
- `3338` 泰碩｜產業=電子零組件業｜市場族群=散熱｜bucket=thermal_solution_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.71｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6108` 競國｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=medium｜分類=range_rebound；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=1.18｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2408` 南亞科｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=high｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.42｜註記=記憶體族群
- `2368` 金像電｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=risk_watch；量比=0.86｜註記=高階PCB/AI伺服器板
- `8271` 宇瞻｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.71｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8271` 宇瞻｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pullback_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.71｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3704` 合勤控｜產業=通信網路業｜市場族群=網通/通訊｜bucket=network_communication_theme｜信心=medium｜分類=range_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.28｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `4967` 十銓｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.04｜註記=記憶體模組觀察
- `6139` 亞翔｜產業=其他電子業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.96｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3231` 緯創｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.81｜註記=AI伺服器主流供應鏈
- `5388` 中磊｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.78｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3380` 明泰｜產業=通信網路業｜市場族群=網通/光通訊｜bucket=network_optical_datacenter_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `4938` 和碩｜產業=電腦及週邊設備業｜市場族群=AI PC/消費電子｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3017` 奇鋐｜產業=電腦及週邊設備業｜市場族群=散熱｜bucket=thermal_solution_theme｜信心=high｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=0.84｜註記=AI散熱主流供應鏈
- `6213` 聯茂｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=2.43｜註記=CCL材料
- `2449` 京元電子｜產業=半導體業｜市場族群=AI晶片測試｜bucket=ai_chip_testing_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.59｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8046` 南電｜產業=電子零組件業｜市場族群=ABF載板/IC載板｜bucket=abf_substrate_theme｜信心=high｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=1.17｜註記=ABF載板主流題材，不與一般PCB混同
- `2449` 京元電子｜產業=半導體業｜市場族群=AI晶片測試｜bucket=ai_chip_testing_theme｜信心=high｜分類=pullback_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.59｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `1815` 富喬｜產業=電子零組件業｜市場族群=玻纖布/CCL｜bucket=glass_fiber_ccl_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=玻纖布主流題材
- `2301` 光寶科｜產業=電腦及週邊設備業｜市場族群=電源/光電｜bucket=power_supply_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=電源供應鏈觀察
- `2324` 仁寶｜產業=電腦及週邊設備業｜市場族群=AI PC/消費電子｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2377` 微星｜產業=電腦及週邊設備業｜市場族群=AI PC/電競｜bucket=ai_pc_consumer_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2382` 廣達｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=AI伺服器主流供應鏈
- `2392` 正崴｜產業=電子零組件業｜市場族群=高速傳輸/連接器｜bucket=high_speed_interconnect_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2449` 京元電子｜產業=半導體業｜市場族群=AI晶片測試｜bucket=ai_chip_testing_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3324` 雙鴻｜產業=其他電子業｜市場族群=散熱｜bucket=thermal_solution_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=AI散熱主流供應鏈
- `5351` 鈺創｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=auto mapped from theme_tags=memory_theme;DRAM IC;IC design
- `5443` 均豪｜產業=半導體業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=半導體設備觀察
- `6127` 九豪｜產業=電子零組件業｜市場族群=被動元件｜bucket=passive_component_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6269` 台郡｜產業=電子零組件業｜市場族群=FPC/軟板｜bucket=fpc_flexible_pcb_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8088` 品安｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `4540` 全球傳動｜產業=電機機械｜市場族群=機器人/精密傳動｜bucket=robotics_precision_motion_theme｜信心=medium｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=0.45｜註記=機器人精密傳動觀察
- `2408` 南亞科｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=high｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.42｜註記=記憶體族群
- `3006` 晶豪科｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=revenue_pullback；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.94｜註記=auto mapped from theme_tags=memory_theme;DRAM IC;DRAM
- `3491` 昇達科｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=低軌衛星射頻供應鏈
- `2344` 華邦電｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=high｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=記憶體族群
- `5469` 瀚宇博｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.9｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6125` 廣運｜產業=光電業｜市場族群=機器人/自動化設備｜bucket=robotics_automation_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2408` 南亞科｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=high｜分類=pullback_rebound；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.42｜註記=記憶體族群
- `6152` 百一｜產業=通信網路業｜市場族群=低軌衛星｜bucket=low_earth_orbit_satellite_theme｜信心=medium｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=0.77｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6414` 樺漢｜產業=電腦及週邊設備業｜市場族群=機器人/工業電腦｜bucket=robotics_ipc_edge_ai_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6239` 力成｜產業=半導體業｜市場族群=記憶體封測｜bucket=memory_packaging_testing_theme｜信心=medium｜分類=true_breakout；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=2.72｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2451` 創見｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow｜註記=記憶體模組觀察
- `3443` 創意｜產業=半導體業｜市場族群=ASIC/先進製程｜bucket=asic_advanced_process_theme｜信心=high｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=1.38｜註記=ASIC/先進製程觀察
- `6108` 競國｜產業=電子零組件業｜市場族群=PCB/CCL｜bucket=pcb_ccl_theme｜信心=medium｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=1.18｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `6669` 緯穎｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=high｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=0.93｜註記=AI伺服器主流供應鏈
- `2449` 京元電子｜產業=半導體業｜市場族群=AI晶片測試｜bucket=ai_chip_testing_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.59｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `1303` 南亞｜產業=塑膠工業｜市場族群=玻纖布/CCL｜bucket=glass_fiber_ccl_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.23｜註記=族群優先於官方產業；南亞可歸玻纖布/CCL題材
- `6139` 亞翔｜產業=其他電子業｜市場族群=半導體設備/材料｜bucket=semiconductor_equipment_material_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.96｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3231` 緯創｜產業=電腦及週邊設備業｜市場族群=AI伺服器｜bucket=ai_server_ipc_theme｜信心=high｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=0.81｜註記=AI伺服器主流供應鏈
- `4967` 十銓｜產業=半導體業｜市場族群=記憶體/HBM｜bucket=memory_hbm_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.04｜註記=記憶體模組觀察

## Industry Non-Mainstream Only

_rows shown: 80 / 211_

- `1339` 昭輝｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=5.55
- `8454` 富邦媒｜產業=數位雲端｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=2.88
- `6005` 群益證｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=hard_exclusion；量比=1.52
- `1455` 集盛｜產業=紡織纖維｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=3.09
- `2618` 長榮航｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=B_confirm_needed；風險桶=non_mainstream_observe_only；量比=2.1
- `1522` 堤維西｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.31
- `2610` 華航｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.94
- `4551` 智伸科｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.89
- `2201` 裕隆｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.71
- `1710` 東聯｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.64
- `0050` 元大台灣50｜產業=未知｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.51
- `1524` 耿鼎｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.71
- `5522` 遠雄｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `2915` 潤泰全｜產業=貿易百貨｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.12
- `2637` 慧洋-KY｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.95
- `6214` 精誠｜產業=資訊服務業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.58
- `1319` 東陽｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.32
- `1810` 和成｜產業=玻璃陶瓷｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.77
- `2929` 淘帝-KY｜產業=貿易百貨｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=3.52
- `1709` 和益｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.74
- `2206` 三陽工業｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.6
- `2882` 國泰金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.54
- `2891` 中信金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.2
- `1533` 車王電｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.75
- `1568` 倉佑｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.64
- `3708` 上緯投控｜產業=綠能環保｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `2886` 兆豐金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.39
- `2017` 官田鋼｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.3
- `2645` 長榮航太｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=range_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.09
- `5522` 遠雄｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `2883` 凱基金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.43
- `1304` 台聚｜產業=塑膠工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2881` 富邦金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6005` 群益證｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `4755` 三福化｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.07
- `2542` 興富發｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.08
- `1409` 新纖｜產業=紡織纖維｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=5.78
- `5522` 遠雄｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pullback_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.46
- `3004` 豐達科｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.13
- `1563` 巧新｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=4.2
- `2867` 三商壽｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.07
- `1305` 華夏｜產業=塑膠工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `1313` 聯成｜產業=塑膠工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2892` 第一金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.87
- `1530` 亞崴｜產業=電機機械｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=true_breakout；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=7.4
- `4743` 合一｜產業=生技醫療業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `1522` 堤維西｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.31
- `2637` 慧洋-KY｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.95
- `6214` 精誠｜產業=資訊服務業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.58
- `2891` 中信金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6214` 精誠｜產業=資訊服務業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `1402` 遠東新｜產業=紡織纖維｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6861` 睿生光電｜產業=生技醫療業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.12
- `1522` 堤維西｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pullback_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=2.31
- `2637` 慧洋-KY｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pullback_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.95
- `2882` 國泰金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.54
- `2891` 中信金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.2
- `2606` 裕民｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2101` 南港｜產業=橡膠工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.97
- `2027` 大成鋼｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.59
- `2891` 中信金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pullback_rebound；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.2
- `4764` 雙鍵｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.38
- `9958` 世紀鋼｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.13
- `1808` 潤隆｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.08
- `4142` 國光生｜產業=生技醫療業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.06
- `2022` 聚亨｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.94
- `4739` 康普｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.89
- `2851` 中再保｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.71
- `1714` 和桐｜產業=化學工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=0.56
- `1810` 和成｜產業=玻璃陶瓷｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2645` 長榮航太｜產業=航運業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2882` 國泰金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `3551` 世禾｜產業=綠能環保｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `5009` 榮剛｜產業=鋼鐵工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `5213` 亞昕｜產業=建材營造｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6015` 宏遠證｜產業=金融業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `6179` 亞通｜產業=其他｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2206` 三陽工業｜產業=汽車工業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only
- `2886` 兆豐金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.39
- `2885` 元大金｜產業=金融保險業｜市場族群=待補｜bucket=待補｜信心=未標示｜分類=revenue_pullback；評級=C_watch_only；風險桶=non_mainstream_observe_only；量比=1.35

## Non-Mainstream Theme

_rows shown: 1 / 1_

- `1536` 和大｜產業=汽車工業｜市場族群=車用電子/EV｜bucket=automotive_ev_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=non_mainstream_observe_only｜註記=market theme taxonomy expansion; market theme overrides exchange industry

## Mapped But Needs Review

_rows shown: 5 / 5_

- `3227` 原相｜產業=半導體業｜市場族群=感測IC/機器人｜bucket=sensor_ic_robotics_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `4961` 天鈺｜產業=半導體業｜市場族群=驅動IC/AI邊緣｜bucket=driver_power_ic_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=risk_watch｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `8996` 高力｜產業=電機機械｜市場族群=散熱/能源設備｜bucket=thermal_energy_theme｜信心=medium｜分類=revenue_pullback；評級=D_risk_downgrade；風險桶=hard_exclusion；量比=1.25｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `2354` 鴻準｜產業=其他電子業｜市場族群=機器人/機構件｜bucket=robotics_mechanical_theme｜信心=medium｜分類=pattern；評級=D_risk_downgrade；風險桶=hard_exclusion｜註記=market theme taxonomy expansion; market theme overrides exchange industry
- `3481` 群創｜產業=光電業｜市場族群=消費性電子/面板｜bucket=consumer_electronics_display_theme｜信心=medium｜分類=pattern；評級=C_watch_only；風險桶=high_momentum_risk_follow；量比=1.61｜註記=auto mapped from theme_tags=consumer electronics;panel;display
