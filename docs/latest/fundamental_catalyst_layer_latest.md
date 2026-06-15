# 財報 / 事件催化層

- generated_at: `2026-06-16 05:37:15 Asia/Taipei`
- candidate_rows: `301`
- financial_source: `data/fundamental_catalysts/quarterly_catalyst.csv`
- event_source: `data/event_catalysts/event_catalyst_log.csv`
- theme_mapping_source: `data/theme_events/company_theme_mapping.csv`
- event_calendar_source: `output/latest/upcoming_catalyst_calendar_latest.csv`
- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。
- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。
- note: 公司題材 mapping 只提供背景標籤；沒有公告、法說、訂單、財報或可信事件來源時，不會單獨升級為 confirmed catalyst。

## 今日催化層摘要

- 類事欣科型候選: `0`
- 營收好但 EPS 尚未確認: `0`
- 利多已反應 / 過熱需降級: `35`

## 類事欣科型候選股

無。

## 財報 / 事件催化候選股

無。

## 營收好但 EPS 尚未確認

無。

## 利多已反應 / 過熱需降級

| date | stock_id | stock_name | category_cn | theme_strength_score | catalyst_strength_score | catalyst_tags | fundamental_catalyst_score | fundamental_catalyst_tags | event_catalyst_tags | event_calendar_tags | nearest_event_date | nearest_event_type | days_to_nearest_event | price_reaction_level | tdcc_accumulation_signal | low_reaction_after_catalyst | already_reacted_to_catalyst | catalyst_quality | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | 2483 | 百容 | 嚴格突破 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 2413 | 環科 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | shareholder_meeting_calendar;calendar_shareholder_meeting | 0 |  |  | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260616 | shareholder_meeting | 0 | priced_in | distribution_warning | False | True |  | calendar event: shareholder_meeting on 20260616; status=confirmed; proximity=within_3d |
| 20260615 | 3014 | 聯陽 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 3576 | 聯合再生 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 6901 | 鑽石投資 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 8105 | 凌巨 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | strong_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 7788 | 松川精密 | 區間內轉強 / 挑戰前高觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 2345 | 智邦 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 2406 | 國碩 | 型態觀察 | 0 | 0 | shareholder_meeting_calendar;calendar_shareholder_meeting | 0 |  |  | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260626 | shareholder_meeting | 10 | priced_in | mild_accumulation | False | True |  | calendar event: shareholder_meeting on 20260626; status=confirmed; proximity=within_14d |
| 20260615 | 2409 | 友達 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 2886 | 兆豐金 | 型態觀察 | 0 | 0 | shareholder_meeting_calendar;calendar_shareholder_meeting | 0 |  |  | shareholder_meeting_calendar;calendar_shareholder_meeting | 20260618 | shareholder_meeting | 2 | priced_in | mild_accumulation | False | True |  | calendar event: shareholder_meeting on 20260618; status=confirmed; proximity=within_3d |
| 20260615 | 3231 | 緯創 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 3550 | 聯穎 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | mild_accumulation | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 3665 | 貿聯-KY | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
| 20260615 | 6443 | 元晶 | 型態觀察 | 0 | 0 | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 0 |  |  | monthly_revenue_calendar;calendar_monthly_revenue_expected_window | 20260701 | monthly_revenue_expected_window | 15 | priced_in | distribution_warning | False | True |  | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proxi... |
