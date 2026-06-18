# 每日全市場候選股監測報告 - 精華版

- 主資料日期：`20260618`
- 產生時間：`2026-06-18 21:27:02 Asia/Taipei`
- 是否可產出正式每日報告：`True`
- 判斷說明：core daily data dates match main_price_date
- 權證資料日期：`20260618`

## 精華版 PDF K 線圖狀態

- PDF K 線圖政策：`local_price_redraw_first`
- PDF K 線圖輸出目錄：`output/latest/charts/pdf_kline`
- PDF K 線圖狀態檔：`output/latest/pdf_kline_chart_status_latest.md`
- 精華版 PDF 會先使用 repo 內日價資料重畫半年視角 K 線圖（預設約 126 個交易日）；`chart_path` / `chart_url` 只是資料不足時的備援。
- 不得因候選資料內的 `chart_url` 下載失敗，就把精華版 PDF 判定為圖片下載失敗版。

## 今日分類摘要

| 分類 | 檔數 |
|---|---:|
| 嚴格突破 | 76 |
| 區間內轉強 / 挑戰前高觀察 | 158 |
| 營收爆發低反應股 | 33 |
| 營收成長股價回檔 | 202 |
| 回檔後短線轉強 | 51 |
| 型態觀察 | 236 |

## 財報 / 事件催化觀察

這是跨分類標籤層，不新增第七大分類；若沒有 EPS / 毛利率 / 重大事件資料來源，只標示待確認，不直接升級。

| 股票 | 原始分類 | 催化標籤 / 反應程度 | TDCC |
|---|---|---|---|
| 8210 勤誠 | 營收成長股價回檔 | score 44 / theme 100.0/5 / revenue_good_eps_unconfirmed;event_confirmed;low_reaction_after_catalyst;new_order;電腦及週邊設備業;d... | 大戶溫和增加 |
| 2301 光寶科 | 營收成長股價回檔 | score 44 / theme 100.0/5 / revenue_good_eps_unconfirmed;event_confirmed;low_reaction_after_catalyst;new_order;電腦及週邊設備業;m... | 大戶同步增加 |
| 2368 金像電 | 營收成長股價回檔 | score 40 / theme 100.0/5 / revenue_good_eps_unconfirmed;event_confirmed;low_reaction_after_catalyst;capacity_expansion;電... | 大戶溫和增加 |
| 2601 益航 | 型態觀察 | score 34 / theme 86.2/5 / event_confirmed;low_reaction_after_catalyst;new_order;航運業;shareholder_meeting_calendar;calenda... | 大戶溫和增加 |
| 8210 勤誠 | 型態觀察 | score 34 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;new_order;電腦及週邊設備業;dividend_calendar;calendar_ex_... | 大戶溫和增加 |
| 2498 宏達電 | 型態觀察 | score 34 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;new_order;通信網路業;dividend_calendar;calendar_ex_div... | 大戶同步增加 |
| 3303 岱稜 | 型態觀察 | score 34 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;new_order;其他電子業;monthly_revenue_calendar;calendar... | 大戶溫和增加 |
| 2891 中信金 | 型態觀察 | score 34 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;new_order;金融保險業;monthly_revenue_calendar;calendar... | 大戶溫和增加 |
| 2891 中信金 | 營收成長股價回檔 | score 34 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;new_order;金融保險業;monthly_revenue_calendar;calendar... | 大戶溫和增加 |
| 2633 台灣高鐵 | 型態觀察 | score 34 / theme 86.2/5 / event_confirmed;low_reaction_after_catalyst;new_order;航運業;monthly_revenue_calendar;calendar_mo... | 大戶溫和增加 |
| 2368 金像電 | 型態觀察 | score 30 / theme 100.0/5 / event_confirmed;low_reaction_after_catalyst;capacity_expansion;電子零組件業;dividend_calendar;calen... | 大戶溫和增加 |
| 2467 志聖 | 營收成長股價回檔 | score 28 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;dividend_calendar;calendar_ex_divide... | 大戶溫和增加 |

## 精華候選股

## 嚴格突破

### 2838 聯邦銀
- 族群：金融保險業
- 分數 / 排名：148.0 / 
- 優先級：
- 連續上榜：連續 17 日；近5日 5；近10日 10；多分類 pullback_rebound|revenue_pullback|true_breakout
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / shareholder_meeting;金融保險業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / shareholder_meeting;...
- 摘要：突破 / 量能2.88x / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；嚴格突破；量比2.88x；月營收YoY 61.1%；累計YoY 32.2%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2458 義隆
- 族群：半導體業
- 分數 / 排名：136.0 / 
- 優先級：
- 連續上榜：連續上榜但過熱；近5日 5；近10日 8；多分類 true_breakout
- TDCC：大戶溫和增加
- 權證：call_strong_inflow / 2.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;半導體業 / monthly_revenue_calendar;calendar_monthly...
- 摘要：突破 / 量能3.87x / 大戶溫和增加 / call_strong_inflow / 2.0
- 完整原因：近幾週其中一項大戶級距增加；call_strong_inflow；認購權證成交金額明顯升溫；嚴格突破；量比3.87x；月營收YoY 3.6%；累計YoY 4.0%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6177 達麗
- 族群：建材營造
- 分數 / 排名：131.0 / 
- 優先級：
- 連續上榜：連續 2 日；近5日 4；近10日 9；多分類 true_breakout
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / shareholder_meeting;建材營造;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / shareholder_meeting;建...
- 摘要：突破 / 量能3.19x / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；no_signal；權證金流未見明顯高於近期平均的變化；嚴格突破；量比3.19x；月營收YoY 149.2%；累計YoY 540.7%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 8081 致新
- 族群：半導體業
- 分數 / 排名：121.0 / 
- 優先級：
- 連續上榜：連續 2 日；近5日 2；近10日 5；多分類 true_breakout
- TDCC：大戶溫和增加
- 權證：call_strong_inflow / 2.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;半導體業 / monthly_revenue_calendar;calendar_monthly...
- 摘要：突破 / 量能2.97x / 大戶溫和增加 / call_strong_inflow / 2.0
- 完整原因：近幾週400張與1000張合計增加；call_strong_inflow；認購權證成交金額明顯升溫；嚴格突破；量比2.97x；月營收YoY -3.3%；累計YoY -2.9%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6179 亞通
- 族群：其他
- 分數 / 排名：119.0 / 
- 優先級：
- 連續上榜：首次上榜；近5日 1；近10日 3；多分類 pullback_rebound|revenue_pullback|true_breakout
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 0 / theme 97.1/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;其他 / monthly_revenue_calendar;calendar_monthly_re...
- 摘要：突破 / 量能4.15x / 大戶溫和增加
- 完整原因：近幾週400張與1000張合計增加；嚴格突破；量比4.15x；月營收YoY 121.8%；累計YoY 68.3%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

## 區間內轉強 / 挑戰前高觀察

### 1301 台塑
- 族群：塑膠工業
- 分數 / 排名：69.0 / 
- 優先級：
- 連續上榜：連續上榜但過熱；近5日 2；近10日 4；多分類 range_rebound
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / dividend_calendar;calendar_ex_dividend;塑膠工業 / dividend_calendar;calendar_ex_dividend / calendar ex_dividend 202606...
- 摘要：區間轉強 / 距前高-8.17% / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；異常放量上漲；量比4.41x；月營收YoY 0.7%；累計YoY -3.8%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 1802 台玻
- 族群：玻璃陶瓷
- 分數 / 排名：69.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 range_rebound
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 26.4/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;玻璃陶瓷 / monthly_revenue_calendar;calendar_monthly_...
- 摘要：區間轉強 / 距前高-12.19% / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；區間內轉強；量比1.23x；月營收YoY 17.7%；累計YoY 8.6%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2388 威盛
- 族群：半導體業
- 分數 / 排名：69.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 range_rebound
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / dividend_calendar;calendar_ex_dividend;半導體業 / dividend_calendar;calendar_ex_dividend / calendar ex_dividend 202606...
- 摘要：區間轉強 / 距前高-10.84% / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；區間內轉強；量比2.96x；月營收YoY 88.1%；累計YoY 34.3%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2409 友達
- 族群：光電業
- 分數 / 排名：69.0 / 
- 優先級：
- 連續上榜：反覆上榜未突破；近5日 4；近10日 6；多分類 range_rebound
- TDCC：大戶溫和增加
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / investor_conference;光電業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / investor_conference;光電...
- 摘要：區間轉強 / 距前高-4.9% / 大戶溫和增加 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張合計增加；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；區間內轉強；量比1.62x；月營收YoY -1.4%；累計YoY -3.7%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 3034 聯詠
- 族群：半導體業
- 分數 / 排名：69.0 / 
- 優先級：
- 連續上榜：反覆上榜未突破；近5日 4；近10日 8；多分類 range_rebound
- TDCC：大戶同步增加
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / material_information;半導體業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / material_information...
- 摘要：區間轉強 / 距前高-0.58% / 大戶同步增加 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步累積；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；挑戰前高；量比1.65x；月營收YoY 9.4%；累計YoY -6.8%；TDCC近幾週400張與1000張同步累積
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

## 營收爆發低反應股

### 1808 潤隆
- 族群：一般產業
- 分數 / 排名：24.0 / 12.0
- 優先級：B_可觀察
- 連續上榜：反覆上榜未突破；近5日 5；近10日 10；多分類 range_rebound|revenue_breakout_low_response|revenue_pullback
- TDCC：大戶同步增加
- 權證：
- 財報 / 事件催化：score 15 / theme 94.3/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;monthly_revenue_calendar;calendar_monthly_revenue_expecte...
- 摘要：B 可觀察 / 營收強 / 近期加速 / 低反應 / 貼近均線
- 完整原因：B_可觀察；近幾週400張與1000張同步累積；單月營收YoY>=150%；累計營收YoY>=50%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；仍在平台整理區；站上20MA/23EMA；接近前高但未大幅過熱；TDCC近幾週400張與1000張同步累積；一般產業；TDCC近幾週400張與1000張同步累積；營建/交屋認列型營收需基本面...
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 4934 太極
- 族群：主流成長題材
- 分數 / 排名：23.0 / 1.0
- 優先級：A_優先追蹤
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 revenue_breakout_low_response|revenue_pullback
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 28 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;monthly_revenue_calendar;calendar_monthly_revenue_expect...
- 摘要：A 優先追蹤 / 營收強 / 近期加速 / 低反應 / 貼近均線
- 完整原因：A_優先追蹤；近幾週其中一項大戶級距增加；單月營收YoY>=150%；累計營收YoY>=50%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；站上20MA/23EMA；TDCC近幾週大戶溫和增加；主流成長題材；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2347 聯強
- 族群：主流成長題材
- 分數 / 排名：23.0 / 2.0
- 優先級：A_優先追蹤
- 連續上榜：反覆上榜未突破；近5日 5；近10日 10；多分類 range_rebound|revenue_breakout_low_response|revenue_pullback
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 28 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;material_information;mainstream_growth;monthly_revenue_c...
- 摘要：A 優先追蹤 / 營收強 / 近期加速 / 低反應 / 貼近均線
- 完整原因：A_優先追蹤；近幾週其中一項大戶級距增加；no_signal；權證金流未見明顯高於近期平均的變化；單月營收YoY>=100%；累計營收YoY>=50%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；站上20MA/23EMA；接近前高但未大幅過熱；TDCC近幾週大戶溫和增加；主流成長題材；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2542 興富發
- 族群：一般產業
- 分數 / 排名：22.0 / 13.0
- 優先級：B_可觀察
- 連續上榜：反覆上榜未突破；近5日 5；近10日 10；多分類 revenue_breakout_low_response|revenue_pullback
- TDCC：大戶同步增加
- 權證：
- 財報 / 事件催化：score 15 / theme 94.3/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;material_information;neutral;monthly_revenue_calendar;cal...
- 摘要：B 可觀察 / 營收強 / 近期加速 / 低反應 / 貼近均線
- 完整原因：B_可觀察；近幾週400張與1000張同步累積；no_signal；權證金流未見明顯高於近期平均的變化；單月營收YoY>=150%；累計營收YoY>=50%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；站上20MA/23EMA；接近前高但未大幅過熱；TDCC近幾週400張與1000張同步累積；一般產業；TDCC近幾週400張與1000...
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2406 國碩
- 族群：主流成長題材
- 分數 / 排名：20.0 / 3.0
- 優先級：A_優先追蹤
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern|revenue_breakout_low_response|revenue_pullback
- TDCC：大戶同步增加
- 權證：
- 財報 / 事件催化：score 28 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;shareholder_meeting_calendar;calendar_shareholder_meetin...
- 摘要：A 優先追蹤 / 營收強 / 低反應 / 貼近均線 / 未過前高
- 完整原因：A_優先追蹤；近幾週400張與1000張同步累積；單月營收YoY>=100%；累計營收YoY>=50%；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；TDCC近幾週400張與1000張同步累積；主流成長題材；TDCC近幾週400張與1000張同步累積
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

## 營收成長股價回檔

### 8271 宇瞻
- 族群：半導體業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern|revenue_pullback
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;shareholder_meeting;半導體業;dividend_calendar;calendar_ex_di...
- 摘要：TDCC轉弱 / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比0.45x；月營收YoY 224.4%；累計YoY 264.0%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2360 致茂
- 族群：其他電子業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern|revenue_pullback
- TDCC：大戶轉弱
- 權證：call_inflow / 1.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / revenue_good_eps_unconfirmed;material_information;其他電子業;monthly_revenue_calendar;calendar_monthly_revenue_expected...
- 摘要：TDCC轉弱 / 大戶轉弱 / call_inflow / 1.0
- 完整原因：近幾週400張與1000張同步減少；call_inflow；認購權證資金升溫；量比0.62x；月營收YoY 133.1%；累計YoY 94.4%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6770 力積電
- 族群：半導體業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 pattern|revenue_pullback
- TDCC：大戶轉弱
- 權證：call_inflow / 1.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / revenue_good_eps_unconfirmed;event_confirmed;product_certification;半導體業;monthly_revenue_calendar;calendar_monthly_...
- 摘要：TDCC轉弱 / 大戶轉弱 / call_inflow / 1.0
- 完整原因：近幾週400張與1000張同步減少；call_inflow；認購權證資金升溫；量比0.77x；月營收YoY 58.9%；累計YoY 31.4%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 1597 直得
- 族群：電機機械
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 pattern|revenue_pullback
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 18 / theme 100.0/5 / revenue_good_eps_unconfirmed;monthly_revenue_calendar;calendar_monthly_revenue_expected_window;電機機械 / revenue_goo...
- 摘要：TDCC增加 / 大戶溫和增加
- 完整原因：近幾週400張與1000張合計增加；no_signal；權證金流未見明顯高於近期平均的變化；量比0.57x；月營收YoY 51.4%；累計YoY 44.1%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2406 國碩
- 族群：光電業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern|revenue_breakout_low_response|revenue_pullback
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 28 / theme 100.0/5 / revenue_good_eps_unconfirmed;low_reaction_after_catalyst;shareholder_meeting_calendar;calendar_shareholder_meetin...
- 摘要：TDCC增加 / 大戶溫和增加
- 完整原因：近幾週400張與1000張合計增加；量比0.56x；月營收YoY 121.2%；累計YoY 152.0%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

## 回檔後短線轉強

### 3324 雙鴻
- 族群：其他電子業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 1；近10日 3；多分類 pattern|pullback_rebound|revenue_breakout_low_response|revenue_pullback
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;其他電子業 / monthly_revenue_calendar;calendar_monthl...
- 摘要：回檔轉強 / pullback_rebound / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；量比1.21x；月營收YoY 93.8%；累計YoY 80.5%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6265 方土昶
- 族群：電子通路業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 1；近10日 3；多分類 pattern|pullback_rebound|revenue_pullback
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;電子通路業 / monthly_revenue_calendar;calendar_monthl...
- 摘要：回檔轉強 / pullback_rebound / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；量比1.49x；月營收YoY 1076.3%；累計YoY 648.4%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6727 亞泰金屬
- 族群：電子零組件業
- 分數 / 排名：90.0 / 
- 優先級：
- 連續上榜：首次上榜；近5日 1；近10日 1；多分類 pullback_rebound|revenue_pullback
- TDCC：大戶溫和增加
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;電子零組件業 / monthly_revenue_calendar;calendar_month...
- 摘要：回檔轉強 / pullback_rebound / 大戶溫和增加
- 完整原因：近幾週其中一項大戶級距增加；量比1.53x；月營收YoY 54.1%；累計YoY 112.7%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 3081 聯亞
- 族群：通信網路業
- 分數 / 排名：84.0 / 
- 優先級：
- 連續上榜：首次上榜；近5日 1；近10日 1；多分類 pullback_rebound|revenue_pullback
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / shareholder_meeting;通信網路業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / shareholder_meeting;...
- 摘要：回檔轉強 / pullback_rebound / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；量比2.02x；月營收YoY 118.8%；累計YoY 107.1%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 3260 威剛
- 族群：半導體業
- 分數 / 排名：84.0 / 
- 優先級：
- 連續上榜：首次上榜；近5日 1；近10日 1；多分類 pattern|pullback_rebound|revenue_pullback
- TDCC：大戶轉弱
- 權證：
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;半導體業 / monthly_revenue_calendar;calendar_monthly...
- 摘要：回檔轉強 / pullback_rebound / 大戶轉弱
- 完整原因：近幾週400張與1000張同步減少；量比2.15x；月營收YoY 210.4%；累計YoY 175.8%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

## 型態觀察

### 1503 士電
- 族群：電機機械
- 分數 / 排名：54.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 4；近10日 7；多分類 pattern
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / shareholder_meeting;電機機械;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / shareholder_meeting;電...
- 摘要：pattern_watch / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比0.88x；月營收YoY 8.4%；累計YoY 14.9%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2338 光罩
- 族群：半導體業
- 分數 / 排名：54.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 pattern
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;半導體業 / monthly_revenue_calendar;calendar_monthly...
- 摘要：pattern_watch / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比0.76x；月營收YoY -7.5%；累計YoY -6.1%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 2363 矽統
- 族群：半導體業
- 分數 / 排名：54.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern|revenue_pullback
- TDCC：大戶溫和增加
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / monthly_revenue_calendar;calendar_monthly_revenue_expected_window;半導體業 / monthly_revenue_calendar;calendar_monthly...
- 摘要：pattern_watch / 大戶溫和增加 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張合計增加；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比0.73x；月營收YoY 88.8%；累計YoY 107.9%；TDCC近幾週大戶溫和增加
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 3006 晶豪科
- 族群：半導體業
- 分數 / 排名：54.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 9；多分類 pattern|revenue_pullback
- TDCC：大戶同步增加
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / material_information;半導體業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window;memory_theme;DRAM IC;D...
- 摘要：pattern_watch / 大戶同步增加 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步累積；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比0.75x；月營收YoY 296.8%；累計YoY 223.5%；TDCC近幾週400張與1000張同步累積
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）

### 6213 聯茂
- 族群：電子零組件業
- 分數 / 排名：54.0 / 
- 優先級：
- 連續上榜：訊號鈍化；近5日 5；近10日 10；多分類 pattern
- TDCC：大戶轉弱
- 權證：call_put_bullish / 3.0
- 財報 / 事件催化：score 0 / theme 100.0/5 / shareholder_meeting;電子零組件業;monthly_revenue_calendar;calendar_monthly_revenue_expected_window / shareholder_meeting...
- 摘要：pattern_watch / 大戶轉弱 / call_put_bullish / 3.0
- 完整原因：近幾週400張與1000張同步減少；call_put_bullish；認購成交金額明顯大於認售，且認購資金明顯升溫；量比1.39x；月營收YoY 29.3%；累計YoY 20.9%；TDCC近幾週大戶籌碼轉弱
- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）
