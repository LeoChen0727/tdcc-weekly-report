# 營收改善尚未反應模型：重新武裝操作矩陣

- generated_at: `2026-07-14 14:39:13 Asia/Taipei`
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
| delayed_next_close_continuation_bonus | 30 | none_no_stop_reference | 955 | 56.0209 | 0.733 | 43.2461 | 9.1232 | 2.0 | 21.0471 | 462 | 0 |
| base_close_confirmed | 30 | none_no_stop_reference | 1408 | 52.983 | 0.6392 | 46.3778 | 8.6443 | 1.3474 | 21.5199 | 848 | 0 |
| delayed_next_close_continuation_bonus | 30 | ma20_ema23_close_stop_4d | 963 | 52.9595 | 0.6231 | 46.4174 | 8.5684 | 1.0292 | 20.8723 | 474 | 0 |
| delayed_next_close_continuation_bonus | 20 | none_no_stop_reference | 1133 | 51.6328 | 0.7944 | 47.5728 | 4.8419 | 0.8759 | 15.0044 | 588 | 0 |
| delayed_next_close_continuation_bonus | 20 | ma20_ema23_close_stop_4d | 1134 | 50.97 | 0.7937 | 48.2363 | 4.5906 | 0.4685 | 14.9912 | 591 | 0 |
| base_close_confirmed | 30 | ma20_ema23_close_stop_4d | 1435 | 50.9408 | 0.6272 | 48.4321 | 8.0669 | 0.3922 | 21.0453 | 882 | 0 |
| base_close_confirmed | 20 | none_no_stop_reference | 1757 | 49.5731 | 0.6261 | 49.8008 | 4.1854 | 0.0 | 15.4809 | 1119 | 0 |
| base_close_confirmed | 20 | ma20_ema23_close_stop_4d | 1759 | 49.0051 | 0.6254 | 50.3695 | 3.9433 | -0.2632 | 15.2359 | 1124 | 0 |
| delayed_next_close_continuation_bonus | 15 | none_no_stop_reference | 1237 | 48.5044 | 0.9701 | 50.5255 | 3.1159 | -0.2506 | 11.4794 | 662 | 0 |
| delayed_next_close_continuation_bonus | 15 | ma20_ema23_close_stop_4d | 1237 | 48.2619 | 0.9701 | 50.768 | 3.0597 | -0.2833 | 11.4794 | 662 | 0 |
| base_close_confirmed | 15 | none_no_stop_reference | 1979 | 48.2567 | 0.9601 | 50.7832 | 3.0376 | -0.2587 | 11.6726 | 1303 | 0 |
| base_close_confirmed | 15 | ma20_ema23_close_stop_4d | 1979 | 47.9535 | 0.9601 | 51.0864 | 2.8853 | -0.3529 | 11.6726 | 1305 | 0 |
| base_close_confirmed | 10 | none_no_stop_reference | 2335 | 44.1542 | 1.3704 | 54.4754 | 1.0467 | -0.9259 | 7.2377 | 1617 | 0 |
| base_close_confirmed | 10 | ma20_ema23_close_stop_4d | 2335 | 44.1542 | 1.3704 | 54.4754 | 1.0315 | -0.9259 | 7.2377 | 1617 | 0 |
| delayed_next_close_continuation_bonus | 10 | ma20_ema23_close_stop_4d | 1384 | 43.6416 | 0.7948 | 55.5636 | 0.7851 | -1.1613 | 7.0809 | 788 | 0 |
| delayed_next_close_continuation_bonus | 10 | none_no_stop_reference | 1384 | 43.6416 | 0.7948 | 55.5636 | 0.7843 | -1.1613 | 7.0809 | 788 | 0 |

## 事欣科與南亞

| stock_id | stock_name | confirmation_variant_id | trigger_date | entry_date | exit_date | realized_return_pct | return_outcome | episode_trade_sequence | rearmed_trade_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | base_close_confirmed | 20260527 | 20260528 | 20260625 | 61.4583 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20251209 | 20251210 | 20260108 | 13.3462 | win | 1 | False |
| 4916 | 事欣科 | base_close_confirmed | 20260416 | 20260417 | 20260515 | 1.0448 | win | 2 | True |
| 4916 | 事欣科 | base_close_confirmed | 20260518 | 20260519 | 20260615 | 21.6381 | win | 3 | True |
| 4916 | 事欣科 | base_close_confirmed | 20260713 |  |  |  |  | 1 | True |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20251209 | 20251211 | 20260109 | 11.4943 | win | 1 | False |
| 4916 | 事欣科 | delayed_next_close_continuation_bonus | 20260416 | 20260420 | 20260518 | 8.4548 | win | 2 | True |

## 高報酬底層 review

- review rows: `101`。高低報酬只觸發查核，不直接判定異常。
