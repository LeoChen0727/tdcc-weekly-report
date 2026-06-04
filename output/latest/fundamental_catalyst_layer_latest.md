# 財報 / 事件催化層

- generated_at: `2026-06-04 22:39:30 Asia/Taipei`
- candidate_rows: `353`
- financial_source: `missing`
- event_source: `missing`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `0`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `46`

## 類事欣科型候選股

無。

## 財報 / 事件催化候選股

無。

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260603 | 1611 | 中電 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2493 | 揚博 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3406 | 玉晶光 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260608 | ex_dividend | 4 | priced_in | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260608; status=confirmed; proximity=within_7d |
| 20260603 | 5285 | 界霖 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260625 | ex_dividend | 21 | overheated | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_30d |
| 20260603 | 3346 | 麗清 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3027 | 盛達 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 6890 | 來億-KY | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 8454 | 富邦媒 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260611 | ex_dividend | 7 | overheated | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260611; status=confirmed; proximity=within_7d |
| 20260603 | 2457 | 飛宏 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2855 | 統一證 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260623 | ex_dividend | 19 | overheated | distribution_warning | False | True |  | calendar event: ex_dividend on 20260623; status=confirmed; proximity=within_30d |
| 20260603 | 1718 | 中纖 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2468 | 華經 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 6282 | 康舒 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3312 | 弘憶股 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 8070 | 長華* | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260617 | ex_dividend | 13 | overheated | strong_accumulation | False | True |  | calendar event: ex_dividend on 20260617; status=confirmed; proximity=within_14d |
