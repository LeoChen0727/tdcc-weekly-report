# 財報 / 事件催化層

- generated_at: `2026-06-18 13:05:25 Asia/Taipei`
- candidate_rows: `319`
- financial_source: `data/fundamental_catalysts/quarterly_catalyst.csv`
- event_source: `data/event_catalysts/event_catalyst_log.csv`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `4`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `1`

## 類事欣科型候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 2633 | 台灣高鐵 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 核心系統電力設備控制與電驛系統(CRP)設備更新專案第二期 2.事實發生日:115/6/17~115/6/17... |
| 20260617 | 2498 | 宏達電 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_divide... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_dividend | 20260622 | ex_dividend | 4 |  | strong_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: Strategic Investors Fund XII Cayman L.P. 2.事實發... |
| 20260617 | 2886 | 兆豐金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;shareholder_meeting_calendar;calenda... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260618 | shareholder_meeting | 0 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: Schuldschein Loans授信資產之轉讓。 2.事實發生日:115/6/16~115/... |
| 20260617 | 2368 | 金像電 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;capacity_expansion;dividend_calendar;calendar_... | 30 | event_confirmed;low_reaction_after_catalyst | capacity_expansion | dividend_calendar;calendar_ex_dividend | 20260623 | ex_dividend | 5 |  | mild_accumulation | True | False | confirmed_event | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公... |

## 財報 / 事件催化候選股

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 8163 | 達方 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 |  | mild_accumulation | True | False | confirmed_event | 1.主管機關核准減資日期:115/06/01 2.辦理資本變更登記完成日期:115/06/01 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)... |
| 20260617 | 2633 | 台灣高鐵 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 核心系統電力設備控制與電驛系統(CRP)設備更新專案第二期 2.事實發生日:115/6/17~115/6/17... |
| 20260617 | 2498 | 宏達電 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_divide... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_dividend | 20260622 | ex_dividend | 4 |  | strong_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: Strategic Investors Fund XII Cayman L.P. 2.事實發... |
| 20260617 | 2891 | 中信金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 金融機構債權(放款) 2.事實發生日:114/6/17~115/6/16 3.董事會通過日期:... |
| 20260617 | 2886 | 兆豐金 | 型態觀察 | 4 | 34 | event_confirmed;low_reaction_after_catalyst;new_order;shareholder_meeting_calendar;calenda... | 34 | event_confirmed;low_reaction_after_catalyst | new_order | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260618 | shareholder_meeting | 0 |  | mild_accumulation | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: Schuldschein Loans授信資產之轉讓。 2.事實發生日:115/6/16~115/... |
| 20260617 | 2368 | 金像電 | 型態觀察 | 3 | 30 | event_confirmed;low_reaction_after_catalyst;capacity_expansion;dividend_calendar;calendar_... | 30 | event_confirmed;low_reaction_after_catalyst | capacity_expansion | dividend_calendar;calendar_ex_dividend | 20260623 | ex_dividend | 5 |  | mild_accumulation | True | False | confirmed_event | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公... |
| 20260617 | 2313 | 華通 | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order;dividend_calendar;calendar_ex_right | 1 | event_confirmed;low_reaction_after_catalyst | new_order | dividend_calendar;calendar_ex_right | 20260622 | ex_right | 4 |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 雷射鑽孔機一批 2.事實發生日:115/5/8~115/6/16 3.董事會通過日期: 不適用 4.其他核決... |
| 20260617 | 9933 | 中鼎 | 型態觀察 | 4 | 1 | event_confirmed;low_reaction_after_catalyst;new_order;monthly_revenue_calendar;calendar_mo... | 1 | event_confirmed;low_reaction_after_catalyst | new_order | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 |  | distribution_warning | True | False | confirmed_event | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:開發國際投資股份有限公司 標的物之性質:普通股 2.事實發生日:115/6/15~... |

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 0055 | 元大MSCI金融 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 13 | priced_in |  | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
