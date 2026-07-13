# 營收改善尚未反應模型：重新武裝操作矩陣

- generated_at: `2026-07-13 20:57:37 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `rearmed_operation_grid_v1_20260713`
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
| delayed_next_close_continuation_bonus | 30 | none_no_stop_reference | 952 | 55.9874 | 0.7353 | 43.2773 | 9.1348 | 1.9804 | 21.1134 | 455 | 0 |
| base_close_confirmed | 30 | none_no_stop_reference | 1405 | 52.9537 | 0.6406 | 46.4057 | 8.6657 | 1.3333 | 21.5658 | 839 | 0 |
| delayed_next_close_continuation_bonus | 30 | ma20_ema23_close_stop_4d | 960 | 52.9167 | 0.625 | 46.4583 | 8.5782 | 1.0202 | 20.9375 | 467 | 0 |
| delayed_next_close_continuation_bonus | 20 | none_no_stop_reference | 1131 | 51.7241 | 0.7958 | 47.4801 | 4.857 | 0.9238 | 15.0309 | 581 | 0 |
| delayed_next_close_continuation_bonus | 20 | ma20_ema23_close_stop_4d | 1132 | 51.0601 | 0.7951 | 48.1449 | 4.6051 | 0.5002 | 15.0177 | 584 | 0 |
| base_close_confirmed | 30 | ma20_ema23_close_stop_4d | 1432 | 50.9078 | 0.6285 | 48.4637 | 8.0866 | 0.3855 | 21.0894 | 873 | 0 |
| base_close_confirmed | 20 | none_no_stop_reference | 1756 | 49.6014 | 0.6264 | 49.7722 | 4.1946 | 0.0 | 15.4897 | 1111 | 0 |
| base_close_confirmed | 20 | ma20_ema23_close_stop_4d | 1758 | 49.033 | 0.6257 | 50.3413 | 3.9523 | -0.2397 | 15.2446 | 1116 | 0 |
| delayed_next_close_continuation_bonus | 15 | none_no_stop_reference | 1230 | 48.6179 | 0.8943 | 50.4878 | 3.1447 | -0.2294 | 11.5447 | 655 | 0 |
| delayed_next_close_continuation_bonus | 15 | ma20_ema23_close_stop_4d | 1230 | 48.374 | 0.8943 | 50.7317 | 3.0881 | -0.2736 | 11.5447 | 655 | 0 |
| base_close_confirmed | 15 | none_no_stop_reference | 1969 | 48.3494 | 0.965 | 50.6856 | 3.0876 | -0.2157 | 11.7318 | 1293 | 0 |
| base_close_confirmed | 15 | ma20_ema23_close_stop_4d | 1969 | 48.0447 | 0.965 | 50.9904 | 2.9345 | -0.3279 | 11.7318 | 1295 | 0 |
| base_close_confirmed | 10 | none_no_stop_reference | 2332 | 44.1252 | 1.3722 | 54.5026 | 1.0272 | -0.9259 | 7.1612 | 1608 | 0 |
| base_close_confirmed | 10 | ma20_ema23_close_stop_4d | 2332 | 44.1252 | 1.3722 | 54.5026 | 1.0119 | -0.9259 | 7.1612 | 1608 | 0 |
| delayed_next_close_continuation_bonus | 10 | ma20_ema23_close_stop_4d | 1383 | 43.6732 | 0.7954 | 55.5315 | 0.7995 | -1.1538 | 7.086 | 780 | 0 |
| delayed_next_close_continuation_bonus | 10 | none_no_stop_reference | 1383 | 43.6732 | 0.7954 | 55.5315 | 0.7988 | -1.1538 | 7.086 | 780 | 0 |

## 事欣科與南亞

| stock_id | stock_name | confirmation_variant_id | trigger_date | entry_date | exit_date | realized_return_pct | return_outcome | episode_trade_sequence | rearmed_trade_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | base_close_confirmed | 20260527 | 20260528 | 20260625 | 61.4583 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20251209 | 20251210 | 20260108 | 13.3462 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20260416 | 20260417 | 20260515 | 1.0448 | win | 2 | True |
| 4916 | 事欣科 | base_close_confirmed | 20260518 | 20260519 | 20260615 | 21.6381 | win | 3 | True |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20251209 | 20251211 | 20260109 | 11.4943 | win | 1 | False |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20260416 | 20260420 | 20260518 | 8.4548 | win | 2 | True |

## 高報酬底層 review

- review rows: `101`。高低報酬只觸發查核，不直接判定異常。
