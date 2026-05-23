# TDCC Signal Tracking

這份文件說明 TDCC 週報旁邊新增的結構化追蹤資料。

## Raw signal vs normalized signal

- `output/history/tdcc_signals/tdcc_signal_log.csv`
  - 保留既有 threshold raw signal。
  - 同一檔股票如果同時進入 >400、>600、>800、>1000，可能會有多列。

- `output/history/tdcc_signals/tdcc_normalized_signal_log.csv`
  - 每檔股票每個 TDCC 週只保留一筆 normalized signal。
  - key 是 `signal_id = {signal_date}_{code}_normalized`。
  - 用於週報分級、族群廣度與月度有效性分析，避免同一股票被四個 threshold 重複統計。

## Snapshot

`output/history/tdcc_signals/tdcc_signal_snapshot.csv` 保存每週訊號當下狀態，包含：

- threshold 是否改善：`has_400`、`has_600`、`has_800`、`has_1000`
- 連續週數：`tdcc_400_streak_weeks` 到 `tdcc_1000_streak_weeks`
- 高點比例：`tdcc_800_ratio_20w_high`、`tdcc_1000_ratio_20w_high`
- 價格反應：`price_return_5d`、`price_return_20d`
- 均線與壓縮：`distance_ma20_pct`、`price_range_20d_pct`
- ABM 欄位：`abm_score`、`setup_type`

缺價格或歷史資料時欄位留空，不讓 workflow 失敗。

## Theme breadth

`output/history/tdcc_signals/theme_breadth_history.csv` 每個 `signal_date + primary_theme` 一列。

族群廣度不是只看最大單檔增幅，而是看：

- 同族群有幾檔同步增加
- >800 / >1000 是否同步改善
- 是否有連續兩週 / 三週同步增加
- 是否只是 single-name concentration

`theme_priority` 使用 `A`、`B`、`C`、`Weakening`、`Neutral`。

## Performance maturity

`output/history/tdcc_signals/tdcc_signal_performance.csv` 保留既有 D+1 / D+2 / D+5 / D+10 / D+20 追蹤。

最新批次如果還沒滿 D+N，狀態是 pending 或 partial。pending 只代表尚未成熟，不應被解讀為正面或負面。

## Monthly effectiveness

`output/latest/tdcc_signal_effectiveness_latest.md` 和 `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` 用來比較 factor group：

- 四級距同步
- 連續兩週 / 三週同步
- 過熱 vs 非過熱
- 族群廣度 A/B/C
- 價格確認 vs 未確認
- ABM setup type

sample size 太小時標示 `insufficient_sample`，不硬下結論。
