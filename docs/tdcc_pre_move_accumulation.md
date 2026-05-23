# TDCC Pre-Move Accumulation / ABM

ABM 是專門找「大戶持續增加，但股價尚未明顯反應」的 TDCC 潛伏吸籌模型。

輸出：

- `output/latest/tdcc_pre_move_accumulation_latest.md`
- `output/latest/tdcc_pre_move_accumulation_latest.csv`
- `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv`

## ABM Score

ABM 分數滿分 100，重點不是找已經大漲的股票，而是找：

- TDCC 四級距連續改善
- >800 / >1000 高門檻也改善
- 20 日股價漲幅不大
- 距離月線不遠
- 平台壓縮
- 量能健康但未爆量
- 同族群有多檔同步改善

若 5 日漲幅過大、20 日漲幅過大、距月線太遠或爆量失控，會扣分並降成 `overheated`。

## setup_type

- `quiet_accumulation`：大戶吸籌，股價尚未充分反應。
- `early_breakout`：剛突破平台或 20 日高點，但尚未過熱。
- `strong_momentum`：TDCC 強，但股價已明顯上漲。
- `overheated`：漲幅、乖離或量能過熱。
- `failed_signal`：未來若績效成熟後轉弱，可用此分類。
- `watch_only`：條件不足或資料不足。

## Why separate TDCC Strength and ABM

TDCC Strength Ranking 找籌碼最強的股票，可能已經漲很多。

ABM Ranking 找籌碼轉好但股價尚未充分反應的股票。兩者不能混在一起。

例如事欣科若已經 5 日或 20 日大漲，仍可在 TDCC Strength 排名前段，但 ABM 會標成 `strong_momentum` 或 `overheated`，不會列為潛伏吸籌第一名。

## Missing data

若個股價格歷史不足，ABM 欄位留空，setup type 會偏向 `watch_only`。缺資料不代表訊號失敗。
