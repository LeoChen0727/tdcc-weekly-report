# 財報 / 事件催化層

- generated_at: `2026-06-17 23:11:24 Asia/Taipei`
- candidate_rows: `319`
- financial_source: `data/fundamental_catalysts/quarterly_catalyst.csv`
- event_source: `data/event_catalysts/event_catalyst_log.csv`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `2`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `13`

## 類事欣科型候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 2886 | 兆豐金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;shareholder_meeting_calendar;calenda... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260618 | shareholder_meeting | 1 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: Schuldschein Loans授信資產之轉讓。 2.事實發生日:115/6/16~115/... |
| 20260617 | 2368 | 金像電 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;capacity_expansion;dividend_calendar;calendar_... | 30 | event_confirmed;low_reaction_after_catalyst | capacity_expansion | dividend_calendar;calendar_ex_dividend | 20260623 | ex_dividend | 6 |  | mild_accumulation | True | False | confirmed_event | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公... |

## 財報 / 事件催化候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 8163 | 達方 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_divide... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_dividend | 20260617 | ex_dividend | 0 |  | mild_accumulation | True | False | confirmed_event | 1.主管機關核准減資日期:115/06/01 2.辦理資本變更登記完成日期:115/06/01 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)... |
| 20260617 | 2891 | 中信金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 金融機構債權(放款) 2.事實發生日:114/6/17~115/6/16 3.董事會通過日期:... |
| 20260617 | 2886 | 兆豐金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;shareholder_meeting_calendar;calenda... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260618 | shareholder_meeting | 1 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: Schuldschein Loans授信資產之轉讓。 2.事實發生日:115/6/16~115/... |
| 20260617 | 2368 | 金像電 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;capacity_expansion;dividend_calendar;calendar_... | 30 | event_confirmed;low_reaction_after_catalyst | capacity_expansion | dividend_calendar;calendar_ex_dividend | 20260623 | ex_dividend | 6 |  | mild_accumulation | True | False | confirmed_event | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公... |
| 20260617 | 2498 | 宏達電 | 型態觀察 | 4 | 24 | event_confirmed;new_order;dividend_calendar;calendar_ex_dividend | 24 | event_confirmed | new_order | dividend_calendar;calendar_ex_dividend | 20260622 | ex_dividend | 5 | mild | strong_accumulation | False | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: Strategic Investors Fund XII Cayman L.P. 2.事實發... |
| 20260617 | 9933 | 中鼎 | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 1 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:開發國際投資股份有限公司 標的物之性質:普通股 2.事實發生日:115/6/15~... |

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3406 | 玉晶光 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 3717 | 聯嘉投控 | 型態觀察 | 2 | 0 | shareholder_meeting;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | shareholder_meeting | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:現金股利，每股配發新台幣0.... |
| 20260617 | 3532 | 台勝科 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 2305 | 全友 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 3504 | 揚明光 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 0055 | 元大MSCI金融 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in |  | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 6209 | 今國光 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 2399 | 映泰 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | shareholder_meeting_calendar;calendar_shareholder_meeting | 0 |  |  | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260617 | shareholder_meeting | 0 | priced_in | distribution_warning | False | True |  | calendar event: shareholder_meeting on 20260617; status=confirmed; proximity=within_3d |
| 20260617 | 1907 | 永豐餘 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 3019 | 亞光 | 型態觀察 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260624 | ex_dividend | 7 | priced_in | strong_accumulation | False | True |  | calendar event: ex_dividend on 20260624; status=confirmed; proximity=within_7d |
| 20260617 | 2464 | 盟立 | 型態觀察 | 2 | 0 | material_information;monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  | material_information | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | 1.董事會決議日期:115/06/16 2.增資資金來源:現金增資發行普通股 3.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 4.全案發行總金額及股數(如屬盈餘或公... |
| 20260617 | 2483 | 百容 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260617 | 1310 | 台苯 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 14 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
