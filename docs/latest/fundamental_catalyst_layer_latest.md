# 財報 / 事件催化層

- generated_at: `2026-06-25 08:06:17 Asia/Taipei`
- candidate_rows: `372`
- financial_source: `data/fundamental_catalysts/quarterly_catalyst.csv`
- event_source: `data/event_catalysts/event_catalyst_log.csv`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `1`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `234`

## 類事欣科型候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 1216 | 統一 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;product_certification;monthly_revenue_calendar... | 30 | event_confirmed;low_reaction_after_catalyst | product_certification | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 永豐銀行(中國)人民幣 365 天期結構性存款 2.事實發生日:115/6/23~115/6/2... |

## 財報 / 事件催化候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 2610 | 華航 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 747-400F貨機 2.事實發生日:115/6/23~115/6/23 3.董事會通過日期: 民國114年1... |
| 20260624 | 1216 | 統一 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;product_certification;monthly_revenue_calendar... | 30 | event_confirmed;low_reaction_after_catalyst | product_certification | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 永豐銀行(中國)人民幣 365 天期結構性存款 2.事實發生日:115/6/23~115/6/2... |
| 20260624 | 4147 | 中裕 | 嚴格突破 | 3 | 20 | event_confirmed;mass_production;monthly_revenue_calendar;calendar_monthly_revenue_expected... | 20 | event_confirmed | mass_production | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | mild | strong_accumulation | False | False | confirmed_event | 1.事實發生日:115/06/22 2.契約或承諾相對人:Samsung Biologics Co., Ltd. 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:115/... |
| 20260624 | 9933 | 中鼎 | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 1 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:開發國際投資股份有限公司 標的物之性質:普通股 2.事實發生日:115/6/15~... |

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 6488 | 環球晶 | 型態觀察 | 2 | 0 | material_information;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | material_information | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | strong_accumulation | False | True |  | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: 一、基本資料 (一)單月                    ... |
| 20260624 | 6282 | 康舒 | 型態觀察 | 2 | 0 | shareholder_meeting;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | shareholder_meeting | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | strong_accumulation | False | True |  | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:無 3.重要決議事項二、章程修訂:通過修正「公司章程」案 4.重要決議事項三、營業報告書及財務報表:通... |
| 20260624 | 6274 | 台燿 | 型態觀察 | 2 | 0 | shareholder_meeting;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | shareholder_meeting | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | 1.股東常會日期:115/06/17 2.重要決議事項一、盈餘分配或盈虧撥補: 承認114年度盈餘分派案，普通股每股配發現金股利7.506577元。 3.重要決議事項二、章程修訂:... |
| 20260624 | 6271 | 同欣電 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 6196 | 帆宣 | 型態觀察 | 2 | 0 | material_information;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | material_information | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | 1.董事會決議日期:115/06/17 2.發放股利種類及金額:現金股利美金11,420,000元 3.其他應敘明事項:無；calendar event: monthly_reve... |
| 20260624 | 6180 | 橘子 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 6164 | 華興 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 6548 | 長科* | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 6141 | 柏承 | 型態觀察 | 2 | 0 | shareholder_meeting;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | shareholder_meeting | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認一一四年度虧損撥補案 3.重要決議事項二、章程修訂:NA 4.重要決議事項三、營業報告書及財務... |
| 20260624 | 6120 | 達運 | 型態觀察 | 2 | 0 | material_information;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | material_information | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | 1.董事會決議日期或發生變動日期:115/06/17 2.人員別（請輸入董事長或總經理）:董事長 3.舊任者姓名:蔡國新 4.舊任者簡歷:本公司董事長暨策略長 5.新任者姓名:蔡國... |
| 20260624 | 6104 | 創惟 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 5864 | 致和證 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 5483 | 中美晶 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260624 | 5452 | 佶優 | 型態觀察 | 2 | 0 | shareholder_meeting;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | shareholder_meeting | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | 1.董事會、股東會決議或公司決定日期:115/06/17 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:普通股現金股利新台幣36,9... |
| 20260624 | 5426 | 振發 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 6 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
