# 財報 / 事件催化層

- generated_at: `2026-06-11 20:06:04 Asia/Taipei`
- candidate_rows: `191`
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
- 利多已反應 / 過熱需降級: `32`

## 類事欣科型候選股

無。

## 財報 / 事件催化候選股

無。

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260611 | 2597 | 潤弘 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260618 | ex_dividend | 7 | overheated | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260618; status=confirmed; proximity=within_7d |
| 20260611 | 2414 | 精技 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 3022 | 威強電 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 2243 | 宏旭-KY | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 7722 | LINEPAY | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260615 | ex_dividend | 4 | overheated | mild_accumulation | False | True |  | calendar event: ex_dividend on 20260615; status=confirmed; proximity=within_7d |
| 20260611 | 8021 | 尖點 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 1714 | 和桐 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 2483 | 百容 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 3042 | 晶技 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260616 | ex_dividend | 5 | overheated | distribution_warning | False | True |  | calendar event: ex_dividend on 20260616; status=confirmed; proximity=within_7d |
| 20260611 | 2484 | 希華 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 7788 | 松川精密 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 2478 | 大毅 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 3550 | 聯穎 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 20 | overheated | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260611 | 6585 | 鼎基 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260625 | ex_dividend | 14 | overheated | distribution_warning | False | True |  | calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_14d |
| 20260611 | 9910 | 豐泰 | 嚴格突破 | 0 | 0 | dividend_calendar;calendar_ex_dividend | 0 |  |  | dividend_calendar;calendar_ex_dividend | 20260615 | ex_dividend | 4 | overheated | distribution_warning | False | True |  | calendar event: ex_dividend on 20260615; status=confirmed; proximity=within_7d |
