# 營收改善尚未反應模型：重新武裝操作矩陣

- generated_at: `2026-08-23 07:21:17 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `rearmed_operation_grid_v2_20260822`
- 狀態：`research_only`，不修改 production registry、operation adapter 或 PDF。
- 基礎確認：訊號日收盤首次突破前 20 日最高收盤，且 MA60 > MA120；下一交易日開盤進場。
- 隔日續攻加分：只能在 D+1 收盤確認，若用於買進決策必須改為 D+2 開盤進場，不能回填成 D+1 開盤資訊。
- 重新武裝：前一筆實際出場後，最早從下一交易日重新尋找訊號；同股操作不得重疊。
- 出場矩陣：D+10 / D+15 / D+20 / D+30 固定收盤，分別比較無停損與 MA20/EMA23 四日收盤停損。
- 勝／和／敗：實現報酬 > 0 / = 0 / < 0。嚴格 +20% 發動標籤另列，不與操作勝率混用。
- 盤中 high/low 不作 entry、exit、stop 或 realized return basis。
- 月營收與財報分離：EPS、毛利率、營益率、營業利益、業外、淨利均未納入。

## 採用 lifecycle 的主要矩陣

| confirmation_variant_id | holding_days | stop_policy_id | mature_operation_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_return_pct | median_return_pct | realized_return_ge20_rate_pct | rearmed_operation_count | same_stock_overlap_pair_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| delayed_next_close_continuation_bonus | 30 | none_no_stop_reference | 989 | 54.8028 | 0.5056 | 44.6916 | 8.689 | 1.6736 | 21.7391 | 477 | 0 |
| base_close_confirmed | 30 | none_no_stop_reference | 1445 | 52.3183 | 0.6228 | 47.0588 | 8.4646 | 1.0072 | 21.5917 | 874 | 0 |
| delayed_next_close_continuation_bonus | 30 | ma20_ema23_close_stop_4d | 997 | 52.1565 | 0.5015 | 47.342 | 8.1939 | 0.9375 | 21.3641 | 489 | 0 |
| delayed_next_close_continuation_bonus | 20 | none_no_stop_reference | 1171 | 51.5798 | 0.6832 | 47.737 | 4.6557 | 0.7331 | 15.0299 | 608 | 0 |
| delayed_next_close_continuation_bonus | 20 | ma20_ema23_close_stop_4d | 1172 | 50.8532 | 0.6826 | 48.4642 | 4.4116 | 0.4249 | 15.0171 | 611 | 0 |
| base_close_confirmed | 30 | ma20_ema23_close_stop_4d | 1476 | 50.0678 | 0.542 | 49.3902 | 7.7734 | 0.1264 | 20.8672 | 912 | 0 |
| base_close_confirmed | 20 | none_no_stop_reference | 1802 | 48.4462 | 0.7769 | 50.7769 | 4.1527 | -0.4216 | 15.3163 | 1152 | 0 |
| base_close_confirmed | 15 | none_no_stop_reference | 2038 | 47.9882 | 0.9323 | 51.0795 | 2.949 | -0.342 | 11.5309 | 1350 | 0 |
| delayed_next_close_continuation_bonus | 15 | none_no_stop_reference | 1284 | 47.9751 | 0.9346 | 51.0903 | 2.8125 | -0.3178 | 11.215 | 691 | 0 |
| base_close_confirmed | 20 | ma20_ema23_close_stop_4d | 1806 | 47.7852 | 0.7752 | 51.4396 | 3.8482 | -0.5192 | 15.0055 | 1159 | 0 |
| base_close_confirmed | 15 | ma20_ema23_close_stop_4d | 2038 | 47.7429 | 0.9323 | 51.3248 | 2.8388 | -0.3839 | 11.5309 | 1352 | 0 |
| delayed_next_close_continuation_bonus | 15 | ma20_ema23_close_stop_4d | 1284 | 47.7414 | 0.9346 | 51.324 | 2.7634 | -0.3762 | 11.215 | 691 | 0 |
| base_close_confirmed | 10 | none_no_stop_reference | 2405 | 43.9085 | 1.1642 | 54.9272 | 0.9305 | -0.9862 | 7.1102 | 1675 | 0 |
| base_close_confirmed | 10 | ma20_ema23_close_stop_4d | 2405 | 43.9085 | 1.1642 | 54.9272 | 0.9115 | -0.9862 | 7.1102 | 1675 | 0 |
| delayed_next_close_continuation_bonus | 10 | ma20_ema23_close_stop_4d | 1430 | 43.4266 | 0.8392 | 55.7343 | 0.6966 | -1.2572 | 7.1329 | 816 | 0 |
| delayed_next_close_continuation_bonus | 10 | none_no_stop_reference | 1430 | 43.4266 | 0.8392 | 55.7343 | 0.6951 | -1.2572 | 7.1329 | 816 | 0 |

## 事欣科與南亞

| stock_id | stock_name | confirmation_variant_id | trigger_date | entry_date | exit_date | realized_return_pct | return_outcome | episode_trade_sequence | rearmed_trade_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | base_close_confirmed | 20260527 | 20260528 | 20260625 | 61.4583 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20251209 | 20251210 | 20260108 | 13.3462 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20260416 | 20260417 | 20260515 | 1.0448 | win | 2 | True |
| 4916 | 事欣科 | base_close_confirmed | 20260518 | 20260519 | 20260615 | 21.6381 | win | 3 | True |
| 4916 | 事欣科 | base_close_confirmed | 20260713 | nan | nan | nan | nan | 1 | True |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20251209 | 20251211 | 20260109 | 11.4943 | win | 1 | False |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20260416 | 20260420 | 20260518 | 8.4548 | win | 2 | True |

## 高報酬底層 review

- review rows: `101`。高低報酬只觸發查核，不直接判定異常。
