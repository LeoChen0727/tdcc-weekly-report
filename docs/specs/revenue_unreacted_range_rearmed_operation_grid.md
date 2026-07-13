# 營收改善尚未反應：重新武裝操作矩陣規格

## 邊界

- `model_id`: `revenue_unreacted_range`
- `artifact_id`: `revenue_unreacted_range_rearmed_operation_grid`
- 狀態固定為 `research_only`。本 artifact 不修改 production registry、正式 operation adapter、排名、PDF 或 packet。
- 來源母體固定使用 `absolute_or_two_month_yoy_ge15` 的 model-owned source-first episodes。
- 只研究月營收。EPS、毛利率、營益率、營業利益、業外與淨利未納入；若未來需要，必須先建立正式 PIT 財報資料層。

## 候選與確認

- 基礎訊號為訊號日收盤首次突破前 20 日最高收盤，且訊號日 `MA60 > MA120`。
- `base_close_confirmed` 在訊號日收盤確認，下一交易日開盤進場。
- `delayed_next_close_continuation_bonus` 必須等 D+1 收盤高於訊號日收盤，最早只能在 D+2 開盤進場。
- 隔日續攻在 D+1 開盤時尚不可知，因此不得回填成 D+1 買進的 hidden gate、加分或績效。
- 南亞 1303 的 `20260527` 必須保留在基礎確認；因隔日續攻未成立，不得出現在該日的 delayed bonus。

## Lifecycle

- `episode_first_match_once` 是不重新武裝的比較基準，每個 episode 與 grid 最多一筆。
- `rearm_after_realized_exit_next_trade_day` 是使用者採用的研究 lifecycle。
- 前一筆操作未實際出場前，不得接受同股新訊號。
- 實際出場後，最早從下一交易日重新掃描；所有同股操作必須 non-overlap。
- 事欣科 4916 必須保留 `20251209` 的較早訊號，也必須在前筆退出後允許 `20260518` 再次發動；不得用後來成功回頭覆蓋先前操作。

## 出場與停損

- 固定收盤矩陣為 D+10、D+15、D+20、D+30。
- `none_no_stop_reference` 只在固定未來交易日收盤出場。
- `ma20_ema23_close_stop_4d` 沿用 23EMA 的停損語意：收盤連續 4 天小於等於 MA20／EMA23 較低者的 96%，下一交易日開盤出場。
- 訊號、確認與停損判定使用 `analysis_close`；進場與停損執行使用 `analysis_open`；固定出場使用 `analysis_close`。
- 盤中 high／low 不得作為 entry、exit、stop、勝敗或 realized return basis。

## 績效與異常

- 操作勝／和／敗定義為實現報酬 `> 0`、`= 0`、`< 0`。
- 嚴格發動另列：訊號後 D+15 內收盤達 +20%，且至 D+20 不再跌回 +20% 以下。它不是操作勝率。
- 樣本數只揭露，不得單獨作為否定條件。
- 絕對操作報酬達 80% 只會觸發 bottom-level review，不得只因數值高低直接判定異常。
- Primary 保留尚未完成根因判定的 review candidates；另列排除未解決來源或報酬候選的 sensitivity。
- 2380 虹光的 2026-06-29 raw 價格跳升已查明為彌補虧損減資換股；必須用 TWSE 參考價與 `0.27658171` 換股比例調整停牌前價格，不得把價格尺度變更計成操作利潤。

## 防錯

- 每個 summary grid 必須同時列 primary 與 sensitivity。
- 每個 detail operation key 必須唯一，且 `same_stock_overlap_pair_count = 0`。
- 多次重新武裝必須有連續的同股 sequence，第二筆起明確標示 `rearmed_trade_flag=True`。
- Summary、history 與 docs mirrors 必須一致；detail 必須小於 50 MB。
- Validator 必須逐列驗證 D+1／D+2 進場、固定出場、停損後隔日開盤與 review replay。
