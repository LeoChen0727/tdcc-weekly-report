# Structured Neckline Strict 45/90 Follow-Through Audit

- generated_at: `2026-06-29 03:30:15 Asia/Taipei`
- research_id: `structured_neckline_strict_45_90_follow_through_audit`
- source_research_id: `structured_neckline_strict_45_90_review_packet`
- source_parameter_set_id: `structured_neckline_strict_45_90_review_packet_20260629`
- follow_through_scope_id: `post_entry_close_follow_through_diagnostic_grid`
- sample: `48`
- data_available: `47`
- data_unavailable: `1`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Boundary

The follow-through values are known only after the original entry date. Therefore these rows must not be used as original-entry filters. They are research-only diagnostics for a possible later confirmation-entry model or a risk label. Rows without enough price-history coverage stay in the event index as `follow_through_data_status=unavailable` and are excluded from rule-rate denominators.

## Rule Grid

| rule_id | accepted_count | accepted_win_count | accepted_neutral_count | accepted_loss_count | unavailable_count | accepted_neutral_inclusive_success_rate_pct | accepted_avg_return_pct | loss_rejection_rate_pct | success_or_neutral_rejection_rate_pct | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| max_close_ge_5pct_within_1_sessions | 6 | 3 | 3 | 0 | 1 | 100.0000 | 8.6235 | 100.0000 | 83.7838 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_5pct_within_5_sessions | 26 | 19 | 7 | 0 | 1 | 100.0000 | 9.9001 | 100.0000 | 29.7297 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_5pct_within_3_sessions | 21 | 14 | 7 | 0 | 1 | 100.0000 | 9.7343 | 100.0000 | 43.2432 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_5pct_within_2_sessions | 16 | 9 | 7 | 0 | 1 | 100.0000 | 8.5632 | 100.0000 | 56.7568 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_3pct_within_5_sessions | 28 | 20 | 7 | 1 | 1 | 96.4286 | 9.4210 | 90.0000 | 27.0270 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_3pct_within_3_sessions | 25 | 17 | 7 | 1 | 1 | 96.0000 | 9.3134 | 90.0000 | 35.1351 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_3pct_within_2_sessions | 21 | 13 | 7 | 1 | 1 | 95.2381 | 8.5161 | 90.0000 | 45.9459 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_3pct_within_1_sessions | 11 | 7 | 3 | 1 | 1 | 90.9091 | 8.9018 | 90.0000 | 72.9730 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_1pct_within_3_sessions | 32 | 20 | 10 | 2 | 1 | 93.7500 | 8.3152 | 80.0000 | 18.9189 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_1pct_within_2_sessions | 30 | 19 | 9 | 2 | 1 | 93.3333 | 8.4146 | 80.0000 | 24.3243 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_2pct_within_5_sessions | 30 | 20 | 8 | 2 | 1 | 93.3333 | 8.3338 | 80.0000 | 24.3243 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_2pct_within_3_sessions | 27 | 17 | 8 | 2 | 1 | 92.5926 | 8.1133 | 80.0000 | 32.4324 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_2pct_within_2_sessions | 23 | 14 | 7 | 2 | 1 | 91.3043 | 7.4628 | 80.0000 | 43.2432 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_1pct_within_1_sessions | 19 | 12 | 5 | 2 | 1 | 89.4737 | 7.5569 | 80.0000 | 54.0541 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_2pct_within_1_sessions | 15 | 9 | 4 | 2 | 1 | 86.6667 | 7.0981 | 80.0000 | 64.8649 | use_as_confirmation_entry_hypothesis_or_risk_label_only |
| max_close_ge_1pct_within_5_sessions | 37 | 24 | 10 | 3 | 1 | 91.8919 | 8.2826 | 70.0000 | 8.1081 | use_as_confirmation_entry_hypothesis_or_risk_label_only |

## Event Features

| outcome_result | stock_id | stock_name | retest_entry_date | entry_price | follow_through_data_status | return_pct | max_close_return_1_session_pct | max_close_return_2_session_pct | max_close_return_3_session_pct | max_close_return_5_session_pct | first_close_ge_3pct_session | first_close_ge_5pct_session | weak_follow_through_5d_lt5pct | early_adverse_3d_le_minus5pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| win | 6016 | 康和證 | 20260505 | 20.1000 | available | 19.6517 | -0.4975 | 1.4925 | 8.9552 | 19.6517 | 3 | 3 | false | false |
| win | 6173 | 信昌電 | 20260420 | 93.5000 | available | 18.7166 | -2.9947 | -2.9947 | -2.9947 | -2.9947 |  |  | true | true |
| win | 1447 | 力鵬 | 20260521 | 5.8900 | available | 18.3362 | 0.1698 | 1.8676 | 1.8676 | 1.8676 |  |  | true | false |
| win | 6234 | 高僑 | 20260422 | 35.6000 | available | 18.1180 | 7.4438 | 18.1180 | 23.1742 | 26.4045 | 1 | 1 | false | false |
| win | 1802 | 台玻 | 20250724 | 18.9500 | available | 17.9420 | 6.8602 | 9.4987 | 17.9420 | 17.9420 | 1 | 1 | false | false |
| win | 6291 | 沛亨 | 20260210 | 241.0000 | available | 14.7303 | 4.3568 | 14.7303 | 17.0124 | 20.3320 | 1 | 2 | false | false |
| win | 8383 | 千附 | 20260416 | 54.7000 | available | 14.0768 | 3.8391 | 14.0768 | 25.4113 | 32.3583 | 1 | 2 | false | false |
| win | 6209 | 今國光 | 20250811 | 29.5000 | available | 13.2203 | 1.8644 | 1.8644 | 5.7627 | 13.2203 | 3 | 3 | false | false |
| win | 6207 | 雷科 | 20260506 | 68.3000 | available | 13.0307 | 0.5857 | 1.0249 | 1.0249 | 1.0249 |  |  | true | true |
| win | 4707 | 磐亞 | 20260416 | 14.6000 | available | 12.6712 | -2.3973 | 3.0822 | 8.5616 | 12.6712 | 2 | 3 | false | false |
| win | 2404 | 漢唐 | 20250625 | 653.0000 | available | 12.4043 | -2.6034 | -2.6034 | -2.6034 | -2.6034 |  |  | true | true |
| win | 3044 | 健鼎 | 20250624 | 243.0000 | available | 12.1399 | -0.2058 | -0.2058 | 0.0000 | 1.8519 |  |  | true | false |
| win | 6175 | 立敦 | 20260420 | 65.9000 | available | 12.1396 | -0.4552 | 0.4552 | 0.4552 | 0.4552 |  |  | true | false |
| win | 4908 | 前鼎 | 20260312 | 94.6000 | available | 12.0507 | 2.3256 | 12.0507 | 12.0507 | 12.0507 | 2 | 2 | false | false |
| win | 3317 | 尼克森 | 20260508 | 66.2000 | available | 11.7825 | -6.0423 | 3.0211 | 3.0211 | 11.7825 | 2 | 5 | false | true |
| win | 6217 | 中探針 | 20260204 | 63.1000 | available | 11.7274 | -2.6941 | -2.6941 | -2.6941 | 1.4263 |  |  | true | true |
| win | 8033 | 雷虎 | 20250728 | 78.0000 | available | 11.1538 | 1.1538 | 11.1538 | 22.1795 | 24.4872 | 2 | 2 | false | false |
| win | 2317 | 鴻海 | 20250801 | 175.0000 | available | 11.1429 | 3.7143 | 3.7143 | 5.4286 | 11.1429 | 1 | 3 | false | false |
| win | 3163 | 波若威 | 20260205 | 485.0000 | available | 10.7216 | -2.6804 | 0.8247 | 10.7216 | 21.4433 | 3 | 3 | false | false |
| win | 4973 | 廣穎電通 | 20260317 | 80.7000 | available | 10.6568 | 0.6196 | 10.6568 | 21.6853 | 21.6853 | 2 | 2 | false | false |
| win | 2328 | 廣宇 | 20250820 | 48.1000 | available | 10.6029 | 0.7277 | 10.6029 | 12.2661 | 28.8981 | 2 | 2 | false | false |
| win | 6488 | 環球晶 | 20260428 | 603.0000 | available | 10.4478 | -3.8143 | -3.8143 | -3.8143 | 10.4478 | 5 | 5 | false | true |
| win | 2308 | 台達電 | 20250711 | 471.0000 | available | 10.4034 | 2.5478 | 2.5478 | 4.8832 | 6.1571 | 3 | 4 | false | false |
| win | 8289 | 泰藝 | 20260302 | 35.1000 | available | 10.3989 | 10.3989 | 15.3846 | 15.3846 | 15.3846 | 1 | 1 | false | false |
| win | 2376 | 技嘉 | 20260416 | 280.0000 | available | 10.3571 | 0.3571 | 0.5357 | 0.5357 | 3.0357 | 4 |  | true | false |
| win | 8163 | 達方 | 20260515 | 32.3500 | available | 10.2009 | 4.6368 | 4.6368 | 4.6368 | 9.8918 | 1 | 5 | false | false |
| win | 3704 | 合勤控 | 20250829 | 33.5000 | available | 10.1493 | 1.3433 | 1.3433 | 1.3433 | 6.8657 | 5 | 5 | false | true |
| neutral | 2368 | 金像電 | 20250707 | 299.5000 | available | 4.8414 | -0.5008 | 5.3422 | 7.8464 | 7.8464 | 2 | 2 | false | false |
| neutral | 4904 | 遠傳 | 20251003 | 89.0000 | available | 3.8202 | 0.0000 | 1.7978 | 2.4719 | 2.4719 |  |  | true | false |
| neutral | 3017 | 奇鋐 | 20250611 | 704.0000 | available | 3.6932 | 2.8409 | 7.8125 | 8.3807 | 8.3807 | 2 | 2 | false | false |
| neutral | 3260 | 威剛 | 20250226 | 87.7000 | unavailable | 3.3067 |  |  |  |  |  |  | unknown | unknown |
| neutral | 1727 | 中華化 | 20250728 | 31.0000 | available | 3.2258 | 7.7419 | 7.7419 | 7.7419 | 7.7419 | 1 | 1 | false | false |
| neutral | 1313 | 聯成 | 20250724 | 10.2500 | available | 2.9268 | -2.9268 | -2.9268 | 1.9512 | 1.9512 |  |  | true | false |
| neutral | 6706 | 惠特 | 20250930 | 83.9000 | available | 2.8605 | 6.3170 | 6.3170 | 6.3170 | 6.3170 | 1 | 1 | false | false |
| neutral | 2316 | 楠梓電 | 20250730 | 76.2000 | available | 2.6247 | -1.0499 | 7.6115 | 7.6115 | 7.6115 | 2 | 2 | false | false |
| neutral | 2301 | 光寶科 | 20250710 | 116.0000 | available | 2.5862 | 1.2931 | 1.7241 | 1.7241 | 1.7241 |  |  | true | false |
| neutral | 6197 | 佳必琪 | 20260316 | 178.5000 | available | 0.8403 | -1.6807 | 7.2829 | 9.2437 | 9.8039 | 2 | 2 | false | false |
| neutral | 8358 | 金居 | 20260420 | 373.0000 | available | -0.8043 | 8.3110 | 8.3110 | 8.3110 | 8.3110 | 1 | 1 | false | false |
| loss | 6139 | 亞翔 | 20250625 | 342.0000 | available | -0.8772 | -1.1696 | -1.1696 | -1.1696 | -1.1696 |  |  | true | true |
| loss | 6213 | 聯茂 | 20250527 | 90.3000 | available | -2.8793 | -0.5537 | -0.5537 | -0.5537 | -0.5537 |  |  | true | false |
| loss | 2324 | 仁寶 | 20250925 | 35.2500 | available | -3.9716 | 3.2624 | 3.2624 | 3.2624 | 3.2624 | 1 |  | true | true |
| loss | 2867 | 三商壽 | 20250826 | 6.0400 | available | -4.3046 | -3.6424 | -3.6424 | -3.6424 | 1.1589 |  |  | true | true |
| loss | 9105 | 泰金寶-DR | 20260120 | 6.6400 | available | -8.1325 | -1.8072 | -1.8072 | -1.8072 | -1.8072 |  |  | true | false |
| loss | 2409 | 友達 | 20250926 | 14.0500 | available | -13.5231 | -2.8470 | -2.8470 | -2.1352 | -1.7794 |  |  | true | false |
| loss | 6290 | 良維 | 20260306 | 233.0000 | available | -17.5966 | 2.7897 | 2.7897 | 2.7897 | 2.7897 |  |  | true | true |
| loss | 2344 | 華邦電 | 20250627 | 21.2000 | available | -18.1604 | -0.2358 | -0.2358 | -0.2358 | -0.2358 |  |  | true | true |
| loss | 3047 | 訊舟 | 20250904 | 22.9500 | available | -18.3007 | -5.0109 | -5.0109 | -5.0109 | -5.0109 |  |  | true | true |
| loss | 3019 | 亞光 | 20260129 | 165.0000 | available | -25.4545 | -4.2424 | -0.9091 | -0.9091 | -0.9091 |  |  | true | true |

## Reading Notes

- `within_1_session` means the entry-date close after buying at the entry-date open.
- These diagnostics can support a future `confirmation_next_open` backtest, but are not themselves a production rule.
- `weak_follow_through_5d_lt5pct` is the direct test of whether a row failed to reach +5% close return within the first five sessions.
