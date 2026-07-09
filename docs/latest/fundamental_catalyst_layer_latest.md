# 財報 / 事件催化層

- generated_at: `2026-07-10 01:33:48 Asia/Taipei`
- candidate_rows: `270`
- financial_source: `data/fundamental_catalysts/quarterly_catalyst.csv`
- event_source: `data/event_catalysts/event_catalyst_log.csv`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `3`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `167`

## 類事欣科型候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2912 | 統一超 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order | 34 | event_confirmed;low_reaction_after_catalyst | new_order |  |  |  |  |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 台中市西屯區潮洋里朝富路116號部份之不動產使用權資產 2.事實發生日:115/6/23~115/6/23 3... |
| 20260709 | 2913 | 農林 | 區間內轉強 / 挑戰前高觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order | 34 | event_confirmed;low_reaction_after_catalyst | new_order |  |  |  |  |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 苗栗縣三義鄉西湖段663地號18筆、育英段19地號198筆,合計216筆土地 2.事實發生日:115/7/8~1... |
| 20260709 | 2356 | 英業達 | 區間內轉強 / 挑戰前高觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_divide... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_dividend | 20260715 | ex_dividend | 5 |  | strong_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 桃園大溪廠區之廠務工程及研發設備 2.事實發生日:115/6/30~115/6/30 3.董事會通過日期: 民... |

## 財報 / 事件催化候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2912 | 統一超 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order | 34 | event_confirmed;low_reaction_after_catalyst | new_order |  |  |  |  |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 台中市西屯區潮洋里朝富路116號部份之不動產使用權資產 2.事實發生日:115/6/23~115/6/23 3... |
| 20260709 | 2913 | 農林 | 區間內轉強 / 挑戰前高觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order | 34 | event_confirmed;low_reaction_after_catalyst | new_order |  |  |  |  |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 苗栗縣三義鄉西湖段663地號18筆、育英段19地號198筆,合計216筆土地 2.事實發生日:115/7/8~1... |
| 20260709 | 2356 | 英業達 | 區間內轉強 / 挑戰前高觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_divide... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_dividend | 20260715 | ex_dividend | 5 |  | strong_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 桃園大溪廠區之廠務工程及研發設備 2.事實發生日:115/6/30~115/6/30 3.董事會通過日期: 民... |
| 20260709 | 2610 | 華航 | 型態觀察 | 4 | 24 | event_confirmed;new_order;dividend_calendar;calendar_ex_dividend | 24 | event_confirmed | new_order | dividend_calendar;calendar_ex_dividend | 20260710 | ex_dividend | 0 | mild | mild_accumulation | False | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 坐落於633 Third Ave., Unit 8A, New York, NY 10017, USA之房舍 2... |
| 20260709 | 2887 | 台新新光金 | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_right_... | 1 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_right_dividend | 20260721 | ex_right_dividend | 11 |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 聯合授信案之授信資產轉讓 2.事實發生日:115/4/8~115/7/8 3.董事會通過日期:... |
| 20260709 | 4958 | 臻鼎-KY | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order | 1 | event_confirmed;low_reaction_after_catalyst | new_order |  |  |  |  |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 機器設備 2.事實發生日:115/6/23~115/7/6 3.董事會通過日期: 不適用 4.其他核決日期:... |

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3088 | 艾訊 | 型態觀察 | 2 | 0 | shareholder_meeting | 0 |  | shareholder_meeting |  |  |  |  | priced_in | mild_accumulation | False | True |  | 1.董事會或股東會決議日期:115/07/07 2.原發放股利種類及金額: 現金股利新台幣(以下同)325,488,050元，每股配發2.93644855元。 3.變更後發放股利種... |
| 20260709 | 6215 | 和椿 | 型態觀察 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260715 | ex_dividend | 5 | priced_in | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260715; status=confirmed; proximity=within_7d |
| 20260709 | 8042 | 金山電 | 型態觀察 | 2 | 0 | material_information;passive_component_theme;capacitors;capacitor | 0 |  | material_information;passive_component_theme;capacitors;capacitor |  |  |  |  | priced_in | strong_accumulation | False | True |  | 1.事實發生日:115/06/17 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊:金山電六(80426)可轉債相關資訊 到期日期：117/12/16... |
| 20260709 | 6509 | 聚和 | 型態觀察 | 2 | 0 | shareholder_meeting | 0 |  | shareholder_meeting |  |  |  |  | priced_in | strong_accumulation | False | True |  | 1.董事會、股東會決議或公司決定日期:115/07/02 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放普通股現金股利新台... |
| 20260709 | 6207 | 雷科 | 型態觀察 | 2 | 0 | shareholder_meeting | 0 |  | shareholder_meeting |  |  |  |  | priced_in | strong_accumulation | False | True |  | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 盈餘分配之現金股利新台幣55,775,937元 (每股配發0.7元)。 3.變更後發放股利種類及金額: 盈餘分配之現金... |
| 20260709 | 5434 | 崇越 | 型態觀察 | 2 | 0 | shareholder_meeting;dividend_calendar;calendar_ex_dividend | 0 |  | shareholder_meeting | dividend_calendar;calendar_ex_dividend | 20260716 | ex_dividend | 6 | priced_in | distribution_warning | False | True |  | 1.董事會、股東會決議或公司決定日期:115/06/30 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:盈餘發放現金股利 (1)原發... |
| 20260709 | 5302 | 太欣 | 型態觀察 | 2 | 0 | material_information | 0 |  | material_information |  |  |  |  | priced_in | mild_accumulation | False | True |  | 1.董事會決議日期或發生變動日期:115/07/07 2.人員別（請輸入董事長或總經理）:董事長 3.舊任者姓名:王國肇 4.舊任者簡歷:太欣半導體股份有限公司董事長 5.新任者姓... |
| 20260709 | 9958 | 世紀鋼 | 型態觀察 | 2 | 0 | material_information;dividend_calendar;calendar_ex_dividend | 0 |  | material_information | dividend_calendar;calendar_ex_dividend | 20260723 | ex_dividend | 13 | priced_in | mild_accumulation | False | True |  | 1.事實發生日:115/07/08 2.公司名稱:世紀鋼鐵結構股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:因配發現金股利，... |
| 20260709 | 5483 | 中美晶 | 型態觀察 | 0 | 0 |  | 0 |  |  |  |  |  |  | priced_in | mild_accumulation | False | True |  |  |
| 20260709 | 6573 | 虹揚-KY | 型態觀察 | 2 | 0 | material_information | 0 |  | material_information |  |  |  |  | overheated | distribution_warning | False | True |  | 1.事實發生日:115/07/07 2.發生緣由:依據臺灣證券交易所股份有限公司通知辦理。 3.財務業務資訊:    期間　　　　　月　　　　　　　　　　　季　　　　　　  　最近... |
| 20260709 | 1905 | 華紙 | 型態觀察 | 4 | 0 | event_confirmed;new_order | 0 | event_confirmed | new_order |  |  |  |  | priced_in | distribution_warning | False | True | confirmed_event | 1.事實發生日:115/06/22 2.發生緣由:本公司接獲台灣證券交易所股份有限公司通知辦理 3.財務業務資訊:  期間           (月)               ... |
| 20260709 | 3624 | 光頡 | 型態觀察 | 2 | 0 | material_information;passive_component_theme;resistors;resistor | 0 |  | material_information |  |  |  |  | priced_in | strong_accumulation | False | True |  | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理公告。 3.財務業務資訊: (1)單月                         ... |
| 20260709 | 7788 | 松川精密 | 型態觀察 | 2 | 0 | shareholder_meeting;dividend_calendar;calendar_ex_dividend | 0 |  | shareholder_meeting | dividend_calendar;calendar_ex_dividend | 20260724 | ex_dividend | 14 | priced_in | distribution_warning | False | True |  | 1.董事會、股東會決議或公司決定日期:115/07/07 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:現金股利新台幣159,491... |
| 20260709 | 2409 | 友達 | 型態觀察 | 2 | 0 | shareholder_meeting | 0 |  | shareholder_meeting |  |  |  |  | priced_in | mild_accumulation | False | True |  | 1.股東常會日期:115/06/25 2.重要決議事項一、盈餘分配或盈虧撥補:無 3.重要決議事項二、章程修訂:核准修訂公司章程案 4.重要決議事項三、營業報告書及財務報表:無 5... |
| 20260709 | 6120 | 達運 | 型態觀察 | 2 | 0 | material_information | 0 |  | material_information |  |  |  |  | priced_in | distribution_warning | False | True |  | 1.董事會決議日期或發生變動日期:115/06/17 2.人員別（請輸入董事長或總經理）:董事長 3.舊任者姓名:蔡國新 4.舊任者簡歷:本公司董事長暨策略長 5.新任者姓名:蔡國... |
