# revenue_unreacted_range/source_mid_falling formal operation v2

## 結論與邊界

此規格新增 model-owned、append-only 的正式 runtime adapter：
`revenue_unreacted_range_source_mid_falling_v2_operation_v2`。它不修改或覆寫
既有 disabled v1，也不從舊的 cross-model monolith、candidate signal、
`research_backtest`、`output/latest` 或 `docs/latest` 反推正式操作列。

正式訊號生效日固定為 `formal_signal_effective_from=20260831`，亦即 4A–4C
授權後第一個交易日。任何早於此日的歷史訊號不得回填為
`confirmed_operation` 或 `active_operation`；生效日前執行只會產生完整的
model-owned empty-state artifact。

`forward_holdout_v2` 是上線後監控，並維持 `no_tuning`。它不是 adapter
執行的 hard gate，不得拿來新增條件、調整門檻、重新選樣或更改排序。

## Runtime 客觀資料

producer 只讀：

- `data/monthly_revenue_history/monthly_revenue_history.csv`
- `data/stock_price_history/<stock_id>.csv`
- `config/stock_theme_map.csv`
- `config/stock_theme_taxonomy_manual.csv`
- `config/stock_theme_authorized_seed.csv`
- 本 adapter 自己先前寫出的 append-only formal confirmed history；此項僅用來
  證明 `active_operation` 曾經是正式且 `buy_rank_eligible=True` 的
  `confirmed_operation`。

月營收與季度／年度財報基本面必須分開。此模型只使用月營收；EPS、毛利率、
營益率、營業利益、業外損益、淨利及季度／年度財報欄位均不得進入條件、
分數、排序、promotion evidence 或 PDF operation row。producer 若在月營收
source 看見上述欄位會 fail closed。

股票 taxonomy 只決定 `mainstream` 或 `non_mainstream` 報表線；缺少明確
mainstream 標籤時，fail closed 到 `non_mainstream`，不改變模型條件。

## 凍結規則

`rule_spec_id=revenue_unreacted_range_source_mid_falling_d30_v1`，
`rule_canonical_sha256=1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633`。

1. 月營收 source 必須 PIT-ready，並符合下列凍結條件之一：
   - 當月年增率至少 30%；或
   - 累計年增率至少 20%；或
   - 連續兩個曆月的當月年增率均至少 15%。
2. source anchor 是 `source_table_date` 當日或之後第一個可用交易日。
3. source position 使用 anchor 以前 120 個交易日的 high/low，排除 anchor
   當日；`source_mid` 固定為 `40 < position_pct <= 75`。
4. `falling` 固定為 anchor close 相對 20 個交易日前 close 的報酬小於 -5%，
   且 EMA23 相對五個交易日前的斜率小於 0%。
5. trigger 必須在 source anchor 後 0–60 個交易日內；trigger close 必須由
   未突破轉為突破前 20 個交易日的最高 close，且當日 MA60 > MA120。
6. 價格特徵由客觀 OHLC history 重新計算；不信任 source 檔中的既有
   indicator 欄位。

規則不包含 add-score、deduct-score、重新排序或額外篩選。所有相同股票的
base trigger 會先執行全域 non-overlap，再判斷 `source_mid_falling` membership，
避免未選變體的重疊訊號讓正式樣本重新挑選。

## 正式 lifecycle

| 階段 | 正式定義 |
| --- | --- |
| D0 | trigger close 完成後列為 `pending_confirmation`。 |
| D+1 | 僅當 D+1 close 高於 D0 trigger close，列為 `confirmed_operation`；不得使用 intraday high/low。 |
| D+2 | 使用 D+2 open 作為正式 entry；轉成 `active_operation` 前，必須從 append-only history 找到生效日起較早的同一 `operation_key`、`confirmed_operation`、`buy_rank_eligible=True` row 與正確 canonical row SHA。 |
| D30 | entry 日為第 1 個持有交易日，固定在 entry index + 29 的 close 出場。 |

正式操作不設 stop。`stop_loss_rule_id=none_no_stop_reference`、
`stop_loss_price` 必須為空；intraday high/low 不得成為正式 entry、exit、stop、
win、failure 或 realized return 價格。

同一股票在既有 position 出場前不得建立新 position；同一報表日、報表線及
PDF view 也不得同時出現在 `confirmed_operation` 與 `active_operation`。
`confirmed_unranked_operation` 在沒有額外授權前永遠只輸出 empty state，
不得把未排名列日後升格為 active。

## Artifact 與 schema

正式輸出：

- `output/latest/daily_revenue_unreacted_range_operation_section_latest.csv`
- `output/latest/daily_revenue_unreacted_range_operation_section_latest.md`
- `docs/latest/daily_revenue_unreacted_range_operation_section_latest.csv`
- `docs/latest/daily_revenue_unreacted_range_operation_section_latest.md`
- `output/history/daily_model_snapshots/daily_revenue_unreacted_range_operation_section_<YYYYMMDD>_<semantic_sha256>.csv`

history snapshot 將 `generated_at` 留空，以完整 CSV bytes 的 SHA-256 命名；同名
內容碰撞必須 fail closed，既有 snapshot 不得覆寫。

schema 同時提供：

- `pdf_view=highlight|full`
- `pdf_section=confirmed_operation|confirmed_unranked_operation|pending_confirmation|active_operation`
- `row_type=data|empty_state` 與 section-specific `empty_text_zh`
- module/schema/lifecycle/rule/approval metadata
- report line、stock identity、PIT source、position/shape、signal/confirmation/
  entry/exit sequence、objective source hashes、history proof 與 canonical row hash
- common entry/stop/exit consumer 欄位與完整 13 欄 `row_metric_*` contract
- `formal_model_use_allowed=True`、`approved_for_daily=True`、
  `presentation_allowed=True`、`production_allowed=True`

highlight 只提供 `confirmed_operation` 與 `active_operation`；full 另提供
`pending_confirmation` 與 `confirmed_unranked_operation`。每一個預期 section
即使沒有 data row 也必須恰有一列 empty state，PDF 不得從 candidate signal
合成 lifecycle。

## 績效揭露，不是排序條件

固定規則的整體 provisional gross historical baseline 為：sample size 53、
win 77.3585%、neutral 0.0000%、failure 22.6415%、average return +14.8950%、
median return +9.4077%。其 source 是
`config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_manifest.csv`。

這組數字只可作 model header disclosure，狀態為
`provisional_gross_historical_header_disclosure_only`；它不是個股 row-level
績效，也不得影響排序。data row 必須設定：

- `row_metric_status=unavailable_no_approved_add_score_metric`
- `row_metric_selection_status=baseline_not_permitted_in_operation_row`
- 其餘 row-level metric payload 留空

empty row 必須設定 `row_metric_status=not_applicable_empty_state`。

## 驗證

獨立 validator 不 import producer 或模型商業函式。它必須檢查 exact schema、
固定 metadata、full empty-state coverage、canonical row SHA、客觀 runtime
sources、無 pre-effective backfill、D0/D+1/D+2/D30 index、no-stop、same-stock
non-overlap、row-metric baseline 禁用，以及 active row 的先前正式 confirmed
append-only proof。

```text
python scripts/build_daily_revenue_unreacted_range_operation_section.py
python scripts/validate_daily_revenue_unreacted_range_operation_section.py
python -m pytest tests/test_daily_revenue_unreacted_range_operation_section.py -q
```

本檔與上述兩個 scripts 僅建立 model-owned formal adapter infrastructure；
readiness、workflow、PDF renderer 與 production consumer 的接線由各自 owner
的獨立 promotion integration change 負責。
