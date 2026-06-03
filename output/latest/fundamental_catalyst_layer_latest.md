# 財報 / 事件催化層

- generated_at: `2026-06-04 01:47:19 Asia/Taipei`
- candidate_rows: `543`
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
- 利多已反應 / 過熱需降級: `40`

## 類事欣科型候選股

無。

## 財報 / 事件催化候選股

無。

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260603 | 1303 | 南亞 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2331 | 精英 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2353 | 宏碁 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260617 | ex_dividend | 13 | overheated | strong_accumulation | False | True |  | calendar event: ex_dividend on 20260617; status=confirmed; proximity=within_14d |
| 20260603 | 2356 | 英業達 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2357 | 華碩 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2362 | 藍天 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260625 | ex_dividend | 21 | overheated | strong_accumulation | False | True |  | calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_30d |
| 20260603 | 2377 | 微星 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2405 | 輔信 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 2409 | 友達 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3021 | 鴻名 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | neutral | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3231 | 緯創 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3321 | 同泰 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | priced_in | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 3338 | 泰碩 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 4545 | 銘鈺 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | neutral | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
| 20260603 | 5484 | 慧友 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260601 | monthly_revenue_expected_window | -3 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proxi... |
