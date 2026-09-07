# Non-Revenue Momentum Watch

## Metadata
- generated_at: `2026-09-07 11:42:43 UTC`
- main_price_date: `20260907`
- section_type: `specialty_section_not_core_category`
- model_effect_allowed: `False`
- allowed_use: `reporting_priority_and_follow_up_only`
- rule: This is not a seventh core daily category. It is a specialty overlay for stocks where price/theme/fund flow is moving before revenue confirmation.

## Interpretation Rules
- `A_fund_flow_confirmed_revenue_unconfirmed`: price/volume or theme support is present, but EPS/gross margin/revenue confirmation is still required.
- `B_turnaround_theme_watch`: theme or fund-flow support is emerging, but price confirmation is incomplete.
- `C_hot_money_watch`: hot-money or technical movement exists, but fundamentals are not confirmed.
- `D_overheated_or_failed_risk`: risk, overheated, distribution, or failed-breakout warning exists; do not promote to main attack list.
- These rows should be discussed separately from the six fixed categories and must not be used as core weight changes.

## Type Counts
| non_revenue_momentum_type | count |
| --- | --- |
| D_overheated_or_failed_risk | 18 |
| C_hot_money_watch | 2 |
| A_fund_flow_confirmed_revenue_unconfirmed | 1 |

## Current Watch List
| non_revenue_momentum_type | stock_id | stock_name | theme_name | presentation_priority | model_score | revenue_confirmation_status | theme_final_status | theme_structural_status | theme_mainstream_label | theme_volume_attack_status | volume_breakout_type | volume_ratio | tdcc_status | warrant_flow_signal | interpretation | next_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_fund_flow_confirmed_revenue_unconfirmed | 0050 | 元大台灣50 | TWSE |  | 69.0 | revenue_data_missing | mainstream_leader | non_mainstream_theme | non_mainstream_flow_active |  |  | 1.53 |  | call_inflow | 量價或族群資金已確認，但營收/EPS/毛利仍需補確認 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若放量突破後隔日仍守住突破區，才可維持短線高優先觀察。 |
| C_hot_money_watch | 2254 | 巨鎧精密-創 | 汽車工業 |  | 69.0 | revenue_negative | emerging_theme | non_mainstream_theme | non_mainstream_flow_active |  |  | 6.88 |  |  | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| C_hot_money_watch | 2201 | 裕隆 | 汽車工業 |  | 54.0 | revenue_negative | emerging_theme | non_mainstream_theme | non_mainstream_flow_active |  |  | 0.96 |  | call_inflow | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| D_overheated_or_failed_risk | 6620 | 漢達 | 生技醫療業 |  | 79.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 5.63 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 6538 | 倉和 | 電子零組件業 |  | 72.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.87 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3021 | 鴻名 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 10.59 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 8240 | 華宏 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 6.1 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 6667 | 信紘科 | 其他電子業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 4.82 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 8064 | 東捷 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated | overheated_volume_theme | bottom_volume_attack | 4.38 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1569 | 濱川 | 電腦及週邊設備業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 3.98 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 8431 | 匯鑽科 | 其他電子業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 3.33 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2409 | 友達 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 2.94 |  | call_put_bullish | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 4157 | 太景*-KY | 生技醫療業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 2.45 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1721 | 三晃 | 化學工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 2.02 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2511 | 太子 | 建材營造 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.6 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 4927 | 泰鼎-KY | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.56 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3481 | 群創 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.2 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 6451 | 訊芯-KY | 半導體業 |  | 54.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.08 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 6456 | GIS-KY | 光電業 |  | 53.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 0.55 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2371 | 大同 | 電機機械 |  | 53.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 0.5 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2392 | 正崴 | 電子零組件業 |  | 53.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 0.5 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
