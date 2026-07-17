# 營收改善但股價尚未反應：三時點位階與型態轉換矩陣

## 邊界

- `model_id`: `revenue_unreacted_range`
- `artifact_id`: `revenue_unreacted_range_position_shape_transition_matrix`
- 本 artifact 為 model-owned、research-only，只分析月營收改善後的價格狀態與轉換，不修改 production model、ranking、scoring、正式 operation adapter、readiness、PDF 或 packet。
- 固定消費 `revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv` 的 exact adopted baseline：`rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|d30|none_no_stop_reference`。
- exact baseline 必須為 `955` 筆 mature operations、`602` 檔股票、勝／和／敗 `535 / 7 / 413`、同股 overlap `0`。Primary 平均報酬 `9.1232%`、中位數 `2.0000%`、P10 `-14.8248%`、P90 `45.3562%`、報酬至少 `20%` 為 `201 / 21.0471%`。
- Primary 保留所有 unresolved anomaly candidates：source candidates `90` 筆、operation-return review candidates `25` 筆、unresolved price-path candidate `1` 筆；price-path candidate 與 source candidate 重疊，三類聯集為 `114` 筆。排除三類 candidates 聯集後的 `841` 筆只作 sensitivity，不得取代 Primary。
- 這是分層描述與假說建立，不是把十二格直接建立成十二個正式模型。樣本少只揭露，不得自動否決罕見但真實的型態。

## 三個 anchor

每筆 operation 固定計算三個互不偷換的觀察時點：

1. `revenue_available`：使用該 trigger 當時已知的 `asof_latest_qualifying_trade_date`，並保留 `asof_latest_qualifying_source_date` lineage。禁止使用 episode 結束後才知道的 `final_episode_latest_*` 欄位回填。
2. `pre_breakout_week_close`：正式 trigger 在同股交易日序列往前 exactly `5` 個交易日的收盤時點。
3. `formal_confirmation_close`：採用 adopted delayed-continuation grid 的 `confirmation_date` 收盤時點；正式 entry 仍是其後下一交易日開盤，不得改成 confirmation close 進場。

逐筆日期關係必須驗證：

所有列一律驗證 `official_source_date <= mapped_source_trade_date <= trigger_date < confirmation_date < entry_date <= exit_date`，且 `pre_breakout_week_close` 必須是 trigger 同股交易日序列 exactly 往前 `5` 格。

只有 `mapped_source_trade_date <= pre_breakout_week_close` 的列，才能另稱為 `source -> preweek -> confirmation` chronological transition；其餘列保留為三 anchor state comparison 並明列 `latest_source_arrived_after_preweek`。

若三時點不是同股有效交易日、offset 不精確或 source anchor 晚於 preweek anchor，該列不得冒充 chronological transition evidence。

以目前 exact baseline 驗收時，具備完整 120-prior-session 位階資料的筆數必須分別為：`revenue_available=462 / 955`、`pre_breakout_week_close=513 / 955`、`formal_confirmation_close=551 / 955`。其餘列保留為歷史不足，不得從分母消失。

## 120 日位階

- 每個 anchor 使用 anchor 以前 exactly `120` 個交易日，anchor 本身排除。
- 價格必須使用 model-owned corporate-action comparability resolution 後的 adjusted／analysis `high`、`low`、`close`，不得混用 raw 與 adjusted basis。
- 定義：`position_120d_pct = (anchor_adjusted_close - prior120_adjusted_low_min) / (prior120_adjusted_high_max - prior120_adjusted_low_min) * 100`。
- 若先前不足 `120` 個交易日、high／low 缺值或 prior range 不大於零，分類為 `insufficient_history`，不得硬塞入低／中／高位。
- `low_position`: `position_120d_pct <= 40`。
- `mid_position`: `40 < position_120d_pct <= 75`。
- `high_position`: `position_120d_pct > 75`。

位階只作本模型 research stratification，不共用或覆寫 volume breakout v2 的正式低／中／高位模型語意。

## 四種價格型態

型態計算全部使用 adjusted／analysis close，且保持以下固定 precedence：

1. `rising`：`return20_pct > 5` 且 `ema23_slope5_pct > 0`。
2. `falling`：`return20_pct < -5` 且 `ema23_slope5_pct < 0`。
3. `consolidation`：`abs(return20_pct) <= 5` 且 `range23_pct <= 15`。
4. `mixed_or_turn`：完整可觀測但未命中前三類的剩餘狀態。

- `return20_pct` 比較 anchor close 與 anchor 往前 `20` 個交易日的 close。
- `ema23_slope5_pct` 比較 anchor 的 EMA23 與 anchor 往前 `5` 個交易日的 EMA23。
- `range23_pct` 的 23-session window 必須包含 anchor，亦即 anchor 與其前 `22` 個交易日；公式為 `(window_adjusted_close_max / window_adjusted_close_min - 1) * 100`，不得誤用只到 anchor 前一日的區間。
- 計算型態所需資料不完整時使用 `insufficient_history`，不得推定成盤整或 mixed。
- 此四類是 revenue model-owned descriptive taxonomy，不得匯入 W 底、頸線或 volume breakout v2 的 shape business semantics。

## 狀態矩陣與 chronological transition

- 每個 anchor 都要輸出低／中／高位 × 盤整／上升／下降／混合轉折的十二格，歷史不足另列且不強行分類。
- `all_sample_state_comparison` 在每個 anchor 使用所有該 anchor 可觀測 operations，回答同一時點不同位階與型態的績效差異。它不是時間轉換證據。
- `chronological_transition` 只納入 `revenue_available <= pre_breakout_week_close < formal_confirmation_close` 且三 anchor 完整可觀測的相同 operation，逐筆輸出 source → preweek → confirmation 的位階與型態路徑。
- 不得以各 anchor 的獨立橫斷面比例推論股票真的從某格轉到另一格；transition 必須使用同一 operation 的 chronological anchors。
- 同一 operation 在同一 anchor／analysis basis 只能出現一次。每個 anchor 的十二格加歷史不足必須守恆回到該 analysis basis 的 exact operation count。

## 固定績效與異常口徑

每格至少輸出：

- operation count、unique stock count。
- 勝／和／敗 count 與 rate。
- 平均與中位 realized return、P10、P90。
- realized return 至少 `20%` 的 count 與 rate。
- source anomaly candidate count、operation-return review candidate count、unresolved price-path candidate count及三類聯集 count。
- same-stock overlap pair count 與 unclassified count。

勝／和／敗及 realized return 必須沿用 exact adopted 955-operation baseline，不得因本矩陣重新定義 entry、exit、stop、holding window 或 non-overlap。數字幅度、分位數或小樣本只能建立 `anomaly_candidate`，不能自動 disposition 或從 Primary 移除。

## Lineage 與 hash

- 每次產出記錄 source artifact path 與當次 immutable canonical-text SHA-256；CSV bytes 先把 CRLF 正規化為 LF，避免同一 Git 內容因 Windows／Ubuntu checkout 行尾不同而產生假 lineage drift，其他 bytes 不得改寫。
- 另以固定欄位、固定排序、固定型別且排除 `generated_at` 的 955-row canonical projection 計算 `source_semantic_sha256`，防止 full producer 只因時間戳重建而誤判 baseline 漂移。
- Validator 必須同時確認當次 source file SHA、canonical semantic SHA、955-row identity、602 stocks、固定績效、三 anchor offsets、matrix conservation 與 transition chronology。
- Summary、transition、history 與 docs mirrors 必須 byte-identical；detail 是 row-level audit evidence，不寫入正式 model 或 PDF surface。

## 財務資料排除

- 本輪只使用月營收 point-in-time lineage 與股價資料。
- EPS、毛利率、營益率、營業利益、業外、淨利及季／年財務報表欄位全部排除。
- Historical financial-statement PIT 尚未通過以前，上述欄位不得成為本矩陣的 gate、score、ranking、PDF metric、operation directive 或 promotion evidence。
- 本矩陣不得讀取 current-snapshot financial statement artifacts，也不得把財報 source audit 的公告時間、PDF 時間或 current XBRL 當成 company filed-at feature。

## Formal-use flags

- `approved_for_daily=False`
- `formal_model_use_allowed=False`
- `production_change=False`
- `presentation_allowed=False`
- `promotion_readiness=research_only_not_promotion_evidence`
