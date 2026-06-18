# 2026-06-18 放量攻擊操作評分工作目標

## 目標

本次工作要把「放量攻擊模型」從單純命中排序，推進到可以由歷史回測支撐的操作排序欄位。研究端與每日任務端必須使用同一套 lifecycle / trigger / score contract，避免 daily production 與 research/backtest 對同一檔股票給出不同解讀。

## 本次結論

1. 放量攻擊第一次命中後，不應直接等同正式買進；必須先依固定 lifecycle 區分 `pending_confirmation`、`confirmed_operation`、`active_operation`、`expired`。
2. 一個 signal 只能有一個 `selected_trigger_id`。若多個確認訊號同時成立，先選最早 confirmation date；同日再依 trigger priority 選定。
3. 勝率、平均報酬、中位數報酬只能用 mature samples 計算，不可把尚未成熟或仍 pending 的樣本混入正式勝率。
4. daily production 可以使用 research-derived 的操作排序欄位，但必須保留可追溯欄位：base score、operation score、TDCC score、pattern score、risk penalty、final rank score、entry/stop/exit rule。
5. 每日任務另存的 as-published snapshot 必須保存上述欄位，未來回測才可以用「當時報告實際發布的資料」檢驗排名，而不是用最新程式重算過去。
6. PDF 這次不重排、不改 renderer；PDF 後續只能讀 structured artifact，不准在 PDF 端重算模型或直接讀 preview / pending queue / research-only artifact。

## 本次需交付

1. `scripts/volume_breakout_operation_utils.py` 成為 research/backtest 與 daily adapter 共用的 lifecycle / trigger contract。
2. `output/latest/volume_breakout_formal_operation_backtest_latest.csv` 重建，且只用 formal lifecycle 的 mature samples 計算績效。
3. `output/latest/daily_volume_breakout_operation_section_latest.csv` 增加操作欄位，但只作 structured output，不碰 PDF layout。
4. `output/latest/daily_candidate_model_signals_for_report_latest.csv` 保存放量攻擊操作排序欄位，讓每日排名可追溯。
5. `output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_YYYYMMDD.csv` 與 `daily_volume_breakout_operation_section_YYYYMMDD.csv` 保存同一組欄位。
6. 測試必須證明 research/backtest 的 event 選擇與 daily adapter 的 lifecycle 判斷一致。

## 非本次範圍

1. 不修改 PDF renderer 或六份 PDF 版型。
2. 不修改 `generate_repo_chatgpt_side_reports.py`。
3. 不把 research-only artifact 直接接進 daily/PDF。
4. 不宣稱其他模型已完成買賣建議；其他模型只維持 research baseline / parity 檢查狀態。

## 驗收條件

1. Local tests 通過。
2. `validate_volume_breakout_confirmed_operation_backtest.py` 通過。
3. `validate_daily_volume_breakout_operation_section.py` 通過。
4. `validate_daily_published_model_snapshots.py` 通過。
5. `validate_daily_published_snapshot_ranking_backtest.py` 通過。
6. `validate_daily_candidate_model_layer.py`、daily selection audit、pipeline integrity audit 通過，且 PDF-facing 欄位不可出現 raw English slug。
7. Branch Actions 通過：Research Backtest Pipeline 與 Daily Full Pipeline。
8. Merge 後 main 再跑 Daily Full Pipeline 成功。
