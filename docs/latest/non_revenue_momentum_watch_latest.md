# Non-Revenue Momentum Watch

## Metadata
- generated_at: `2026-08-31 11:42:47 UTC`
- main_price_date: `20260831`
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
| D_overheated_or_failed_risk | 40 |
| C_hot_money_watch | 5 |
| A_fund_flow_confirmed_revenue_unconfirmed | 1 |

## Current Watch List
| non_revenue_momentum_type | stock_id | stock_name | theme_name | presentation_priority | model_score | revenue_confirmation_status | theme_final_status | theme_structural_status | theme_mainstream_label | theme_volume_attack_status | volume_breakout_type | volume_ratio | tdcc_status | warrant_flow_signal | interpretation | next_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_fund_flow_confirmed_revenue_unconfirmed | 2201 | 裕隆 | 汽車工業 |  | 69.0 | revenue_negative | emerging_theme | non_mainstream_theme | non_mainstream_flow_active |  |  | 2.67 |  | call_strong_inflow | 量價或族群資金已確認，但營收/EPS/毛利仍需補確認 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若放量突破後隔日仍守住突破區，才可維持短線高優先觀察。 |
| C_hot_money_watch | 5321 | 美而快 | 數位雲端 |  | 101.0 | revenue_negative | mainstream_leader | non_mainstream_theme | non_mainstream_flow_active |  |  | 2.3 |  |  | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| C_hot_money_watch | 2723 | 美食-KY | 觀光餐旅 |  | 96.0 | revenue_negative | single_name_signal | non_mainstream_theme | non_mainstream_single_name |  |  | 1.92 |  |  | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| C_hot_money_watch | 2033 | 佳大 | 鋼鐵工業 |  | 84.0 | revenue_negative | mainstream_follow_through | non_mainstream_theme | non_mainstream_flow_active |  |  | 2.3 |  |  | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| C_hot_money_watch | 2023 | 燁輝 | 鋼鐵工業 |  | 69.0 | revenue_negative | mainstream_follow_through | non_mainstream_theme | non_mainstream_flow_active |  |  | 2.05 |  |  | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| C_hot_money_watch | 1319 | 東陽 | 汽車工業 |  | 54.0 | revenue_negative | emerging_theme | non_mainstream_theme | non_mainstream_flow_active |  |  | 0.45 |  | call_inflow | 價格或題材有資金推動，但基本面確認不足，避免當主攻理由 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。 |
| D_overheated_or_failed_risk | 2887 | 台新新光金 | 金融保險業 |  | 143.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 3.29 |  | call_strong_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2883 | 凱基金 | TWSE |  | 140.0 | revenue_data_missing | mainstream_leader | non_mainstream_theme | non_mainstream_flow_active | overheated_volume_theme | bottom_volume_attack | 2.4 |  | call_strong_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1104 | 環泥 | 水泥工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 7.85 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2477 | 美隆電 | 其他電子業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 6.86 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1312 | 國喬 | 塑膠工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 5.37 |  | call_strong_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3645 | 達邁 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 4.99 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 4716 | 大立 | 化學工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 4.78 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3380 | 明泰 | 通信網路業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 4.41 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 8431 | 匯鑽科 | 其他電子業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 3.77 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3339 | 泰谷 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated | overheated_volume_theme | bottom_volume_attack | 3.59 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 6205 | 詮欣 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 3.32 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3548 | 兆利 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 3.25 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3576 | 聯合再生 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 3.14 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3543 | 州巧 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 2.93 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2882 | 國泰金 | 金融保險業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated | overheated_volume_theme | bottom_volume_attack | 2.89 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2392 | 正崴 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 2.38 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3540 | 曜越 | 電腦及週邊設備業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 2.36 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 5871 | 中租-KY | 其他 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 2.35 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2434 | 統懋 | 半導體業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 2.3 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1301 | 台塑 | 塑膠工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated | overheated_volume_theme | bottom_volume_attack | 2.23 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1304 | 台聚 | 塑膠工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.98 |  | call_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3455 | 由田 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.9 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3685 | 元創精密 | 電機機械 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.88 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 4906 | 正文 | 通信網路業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.85 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1309 | 台達化 | 塑膠工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.84 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3376 | 新日興 | 電子零組件業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.82 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3024 | 憶聲 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.77 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 9941 | 裕融 | 其他 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.77 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 8111 | 立碁 | 光電業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.76 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 3363 | 上詮 | 通信網路業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.68 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1305 | 華夏 | 塑膠工業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.66 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 2881 | 富邦金 | 金融保險業 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.64 |  | no_signal | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 4938 | 和碩 | 電腦及週邊設備業 |  | 69.0 | revenue_negative | mainstream_overheated | core_mainstream_theme | core_mainstream_overheated |  |  | 1.57 |  | call_strong_inflow | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
| D_overheated_or_failed_risk | 1440 | 南紡 | 紡織纖維 |  | 69.0 | revenue_negative | mainstream_overheated | non_mainstream_theme | non_mainstream_overheated |  |  | 1.56 |  |  | 題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察 | 等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。; 若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。 |
