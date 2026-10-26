# Stock Model Contract Governance

## Purpose

`config/stock_model_contract_registry.csv` is the formal contract registry for production stock models. It gives TDCC weekly, daily PDF, individual PDF, and research/backtest consumers a stable way to identify which model outputs they may read.

The registry records ownership and consumer approval. It does not define model conditions, scoring weights, ranking rules, or promotion decisions.

## Ownership

- `owner_lane` owns the contract row and consumer approval flags.
- `production_source_file` points to the production implementation source.
- `condition_function`, `score_function`, and `score_profile_id` must match `config/daily_model_condition_spec.csv` for existing production models.
- Any field that cannot be proven from current source must use `pending_review`.

## Consumer Rules

- Daily PDF consumers may use rows with `approved_for_daily_pdf=true`.
- TDCC weekly consumers may use rows with `approved_for_tdcc_weekly_pdf=true`.
- Individual PDF consumers may use rows with `approved_for_individual_pdf=true`.
- Consumers must not treat a missing approval as implicit permission.
- Research/backtest may compare against this registry, but must not write research recommendations into production baseline tables without an explicit promotion PR.
- Research/backtest contract parity validation reads this registry directly as the source of truth. It does not require or recreate `output/latest/stock_model_contract_snapshot_latest.json`.
- Changing a model condition, score function, score profile, or approval flag requires a reviewed PR and validation evidence.
- Formal operation buy/sell/stop/profit-taking rules must be close-confirmed by default. Formal model operation contracts may realize trades only at the next trading day open after a qualifying close confirmation, at the same-day close when the rule explicitly waits for that close, or at a fixed future close exit.
- Formal operation contracts must not use intraday high/low as formal entry, exit, stop, profit-taking, win, failure, or realized-return prices. Intraday high/low may be used only for research-only observation, MFE/MAE, risk audit, liquidity/slippage diagnostics, candle-quality features, or non-operation watch statistics.
- Intraday high/low research evidence must stay advisory unless a later reviewed promotion PR rewrites the model-specific contract into explicit operation semantics. For `price_pullback_23ema`, intraday previous-high touch may be tested only as `research_only_intraday_trigger` with same-day close exit, while close-confirmed previous-high breakout must exit at the next trading day open. `close_prev20_high_break_same_day_close` is invalid because the close-confirmed breakout is known only after that close.
- A model promotion that changes daily PDF visibility or operation-oriented PDF presentation must define a model-owned daily operation-row adapter contract before PDF use. Required scope includes artifact path, schema, lifecycle section semantics, empty-state rows, readiness fields, validators, and PDF-safe consumer fields.
- `approved_for_daily_pdf=true` or a registry approval flag is not sufficient to invent PDF operation rows. The promotion must keep `presentation_allowed=False` until `model_operation_readiness_latest.csv` reports `pdf_integration_status=pdf_integrated_daily_adapter` for the model or an explicitly approved equivalent.
- The daily PDF renderer must not infer buyable, active, pending, exit, or stop-loss lifecycle rows from candidate signal rows, research/backtest variants, or advisory recommendation artifacts.

## Validation

### 23EMA 固定核准證據與追蹤契約

`docs/specs/price_pullback_23ema_operation_candidate_spec.md` 是已釘選的歷史核准證據，
不得加入後續追蹤契約或直接更新核准 hash。2026-10-23 原始確認歷史 consumer
啟用契約獨立保存在
`docs/specs/price_pullback_23ema_confirmation_history_consumer_activation_spec.md`。
此分離不改動正式規則、核准績效、原始發布綁定或任何模型的執行行為。

### 頸線核准中繼資料更正

2026-10-26 依原凍結明細確認：正式頸線研究有 51 筆交易、50 檔股票。
2368 的兩筆交易不重疊，兩筆均保留；不改價格、報酬或任何操作條件。
核准摘要、正式推薦中繼資料與 parity 的股票數同步為 50，交易數維持 51。
原核准 spec 與 evidence pin 保持歷史版本，不以修正文書為由重設固定 hash。
同模型另一研究母體的 8590 筆／1722 檔不屬本次更正。

Run:

```text
python scripts/validate_stock_model_contract_registry.py
```

The validator checks the registry schema, unique `model_id`, strict true/false values for the three `approved_for_*` columns, source-file existence, and alignment with `config/daily_model_condition_spec.csv`.

`input_columns` must list the source-backed model inputs used by each model's condition and scoring path. Include fallback alias columns that helper functions read, and use explicit source prefixes such as `stock_price_history.*` when a model depends on sibling data outside the current candidate row. Do not return an audited model to `pending_review` unless the source path changes and the field list can no longer be proven.
