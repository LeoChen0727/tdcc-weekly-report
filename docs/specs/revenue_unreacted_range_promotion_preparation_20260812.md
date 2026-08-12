# revenue_unreacted_range promotion preparation（2026-08-12）

## 決策

本文件只凍結 promotion preparation，不是正式模型核准、排名變更、production promotion、PDF 整合或 Apps Script 變更。

使用者於 2026-08-12 決定不等待 forward holdout 先成熟，選定 `revenue_unreacted_range` 的 `source_mid_falling` 作為本輪唯一 promotion candidate。`source_low_falling` 與 low+mid falling union 是同一模型的挑戰 variant，不得計成另外兩個獨立模型。

候選狀態固定為 `selected_pending_anomaly_resolution_and_formal_adapter`。`approved_for_daily=False`、`presentation_allowed=False`、`formal_model_use_allowed=False`、`production_change=False`。

## 凍結規則與歷史主結果

- 月營收來源：`absolute_or_two_month_yoy_ge15`。此 identifier 的 exact predicate 是 `(latest_revenue_yoy_pct >= 30 OR cumulative_revenue_yoy_pct >= 20) OR ((period_ordinal(revenue_period) - period_ordinal(previous_revenue_period)) = 1 AND latest_revenue_yoy_pct >= 15 AND previous_latest_revenue_yoy_pct >= 15)`；第一段是 `absolute_strong_flag`，第二段要求前期恰為上一個曆月，所有門檻均為 inclusive `>=`。
- anchor 固定為 `revenue_available`，即 qualifying 月營收 available date 對應的第一個交易 session。
- 位階視窗固定為 anchor 前恰好 120 個 adjusted-price 交易 sessions，不含 anchor；`mid_pos_40_75` 的公式為 `40 < position_120d_pct <= 75`。
- `falling` 的必要公式為 `shape_return20_pct < -5` 且 `shape_ema23_slope5_pct < 0`。
- qualifying source 到 trigger 固定為 0～60 個交易日。
- trigger 固定為 `analysis_close` 向上穿越 prior-20 `analysis_close` high，且 trigger day `MA60 > MA120`。
- 分析基礎：`primary_candidate_retaining`；anomaly candidate 全數留在主結果，排除只可稱 sensitivity analysis。
- lifecycle：`rearm_after_realized_exit_next_trade_day`；同股票下一次 entry 必須晚於前次 realized exit。
- timing：D+1 `analysis_close > trigger analysis_close` 才確認 `delayed_next_close_continuation_bonus`，D+2 以 `analysis_open` entry；固定持有 30 個交易 session，exit offset 29，以 D+30 `analysis_close`／`fixed_future_close` 出場；`none_no_stop_reference`。
- 歷史主結果：N=52、47 檔股票、47 個 episode、41 勝、0 中立、11 敗；勝率 78.8462%、平均 15.8235%、中位數 10.9837%、p10 -10.8794%、p90 42.41%、最小 -19.6694%、最大 82.5095%；`>=20%` 19 筆、`<=-20%` 0 筆。
- 8 筆 combined anomaly candidate 仍留在主結果；其逐筆 worklist 由 `config/revenue_unreacted_range_anomaly_disposition_registry.csv` 凍結。

上述完整公式（包含展開後的 `revenue_rule`）canonical text SHA-256 為 `1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633`，contract version 為 `revenue_unreacted_range_promotion_preparation_contract_v2_20260812`。registry 另精確綁定 selected summary 的 data contract、四個 producer semantics、月營收來源、source/rearmed/price/detail row-set 與 slice SHA-256；任何一項漂移都必須失敗，不能只靠模型名稱或勝率對上。

## 資料與語意邊界

本輪只使用 point-in-time 月營收與調整後價格資料。EPS、毛利率、營業利益率、營業利益、業外損益、淨利及其他季／年財報欄位全部排除，不得從月營收推論，也不得成為條件、評分、排序、PDF 指標或 promotion evidence。

正式 operation 語意只能使用收盤後已知的確認與固定未來收盤出場。本候選不以盤中 high/low 作為 entry、exit、stop、勝負或 realized return 價格。

## Forward holdout 與硬閘門

既有 low/mid falling forward holdout 繼續 append-only 監控，但依 `user_decision_20260812` 改為 `monitoring_non_hard_gate`，不再阻止 promotion preparation。第一次績效解讀仍以至少 20 筆 mature 為最低討論門檻；在此之前只報 mature/right-censored，不宣稱樣本外績效成立。

這項決策不解除 anomaly disposition 硬閘門。8 筆候選在下列八項 root checks 未全部完成前，維持 `unresolved_anomaly_candidate` 並阻擋正式 promotion：

1. identity 與 same-stock non-overlap。
2. formal entry/exit/stop replay。
3. point-in-time 日期與交易日曆連續性。
4. raw-source lineage 與 immutable row hashes。
5. 單位、公式與調整基礎。
6. 權威 corporate action／business event history。
7. 獨立來源交叉佐證。
8. 可重播 evidence reference。

每筆 source anomaly candidate 另凍結「實際造成 anomaly 的 qualifying source event」period、available date、canonical row SHA-256 與 raw file SHA-256，不得用 trigger 前最新 source 取代。尤其 `5484` 必須指向 202512／20260117／`e91f324a5d4c664bf1ca2e329f094212294de006eec1b3395cec5b7b4ff8324c`，不得誤綁較新的 202603／`be6be56b...`；`2478` 是 operation-return review，source attribution 明確為 `not_applicable`。

disposition 的處置與 promotion gate 精確遵守 `config/daily_model_numerical_anomaly_disposition_contract.csv`：

- `unresolved_anomaly_candidate`：`retain_in_primary_metrics_and_allow_exclusion_sensitivity_only`／`blocked_pending_root_cause`。
- `verified_real_extreme`：`retain_in_primary_metrics`／`eligible_only_after_all_other_model_gates`。
- `verified_data_error`：`repair_source_and_rerun_old_metrics_forbidden`／`blocked_until_repaired_rerun`。
- `verified_non_comparable`：`exclude_only_with_approved_reason_and_rerun`／`requires_model_governance_review`。

任何 `verified_*` final disposition 都必須八項全為 `pass`，並使用 `evidence_id=<id>;path=<approved repo-relative immutable path>;sha256=<64 lowercase hex>` 格式的可重播 evidence reference；`verified_non_comparable` 還必須另有同格式的 approved reason reference。Validator 不只檢查字串格式，也會拒絕 absolute path、dot segment 與 repository escape，限制 evidence 位於 model-owned 的 `docs/evidence/revenue_unreacted_range/` 或 `data/revenue_unreacted_range/evidence/`，要求目標為實際檔案，並重新計算 raw bytes SHA-256。未來新增 evidence registry 時必須沿用這兩個 model-owned roots，或以另一次治理變更同步修改本規格與 validator。統計數值偏大本身只能觸發調查，不能當成資料錯誤或排除理由。

正式推進仍需要獨立、model-owned 的 formal operation module／adapter 與相符的 contract、readiness、evidence pin、parity 和 post-main validation。本文件不建立或啟用這些 production surfaces。

本契約由 `scripts/validate_revenue_unreacted_range_promotion_preparation.py` 獨立驗證；research workflow 在 low/mid candidate audit 後以 `--require-source-artifacts` 綁定 exact summary/detail，PR sparse validation 則至少驗證凍結 registry 與 anomaly worklist。

## 下一輪研究議程

- low/mid forward holdout 達至少 20 筆 mature 後，重看勝率、平均、中位數、p10/p90、`>=20%`、`<=-20%` 與信賴區間。
- `source_low_falling` 與 `source_mid_falling` 以相同 timing、holding、anomaly basis 做正式比較；不可把兩者描述成不同模型。
- high×falling 若另行研究，必須獨立預註冊 prospective holdout，固定規則且不混入既有 low/mid holdout；至少 20～30 筆 mature 後才第一次解讀。
- 在改任何 gate、score、ranking 或 operation rule 前，先比較同一 entry/exit 基礎下高報酬與低報酬交易的特徵差異，避免只追勝率或事後調參。
