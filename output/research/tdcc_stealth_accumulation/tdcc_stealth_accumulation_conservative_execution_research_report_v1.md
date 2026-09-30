# TDCC 潛伏吸籌：保守成交假設研究 v1

本次為 frozen-ledger replay；原 primary 全保留，不是實際成交、正式勝率或正式升級。
已看過 validation 非未見 OOS；current-version 非首次發布 PIT。

政策固定：2026-09-30T15:29:39+00:00；replay_started_at=2026-09-30T15:36:32.607823+00:00。

## 固定比較與分母

common_12 / validation / D20 / 1,000股 / 10bps；雙邊費率0.001425最低20，賣出稅0.003。
所有列的 execution_evidence_state=unknown、actual_fill_verified=False；下表可計算只代表已假設完成。
全市場例外清單未核實，不把一般假設稱 verified_normal。

| 策略 | 統計母體 | N | 候選數 | 勝/中立/失敗 | 平均% | 中位數% | >=10%比例 | <=-10%比例 |
|---|---|---:|---:|---|---:|---:|---:|---:|
| baseline_4 | original_primary_proxy | 4981 | 235 | 2028/0/2953 | 0.593261 | -1.607320 | 14.896607 | 17.305762 |
| baseline_4 | assumed_completed_subset | 4979 | 233 | 2027/0/2952 | 0.592952 | -1.607320 | 14.882507 | 17.292629 |
| baseline_4 | original_candidate_exclusion_sensitivity | 4746 | 0 | 1807/0/2939 | -1.807143 | -1.948009 | 10.977665 | 17.867678 |
| baseline_4 | assumed_completed_candidate_exclusion_sensitivity | 4746 | 0 | 1807/0/2939 | -1.807143 | -1.948009 | 10.977665 | 17.867678 |
| trend_8 | original_primary_proxy | 2986 | 144 | 1303/0/1683 | 1.354579 | -1.233290 | 17.682518 | 16.610851 |
| trend_8 | assumed_completed_subset | 2982 | 141 | 1302/0/1680 | 1.330359 | -1.230229 | 17.672703 | 16.566063 |
| trend_8 | original_candidate_exclusion_sensitivity | 2842 | 0 | 1168/0/1674 | -1.077427 | -1.663814 | 13.828290 | 17.135820 |
| trend_8 | assumed_completed_candidate_exclusion_sensitivity | 2841 | 0 | 1168/0/1673 | -1.075079 | -1.663456 | 13.833157 | 17.141851 |

原候選排除僅為既有敏感度，不是修正主績效；假設完成子集的平均／勝率不能代表全母體。

## 全母體狀態

- baseline_4：原primary 4981；不可計算 2（0.040153%）；狀態 {'assumed_closed': 4979, 'entry_unknown': 1, 'exit_unknown': 1}。
- trend_8：原primary 2986；不可計算 4（0.133958%）；狀態 {'assumed_closed': 2982, 'entry_unknown': 1, 'exit_unknown': 1, 'lock_blocked': 2}。

## 已證例外與傳遞鎖

例外按股票及官方日期套用全部 ledger 列，不使用報酬挑選或用TickType/成交量推論成交。
同模型/strategy/固定common12-validation/stock按日期處理；unknown/partial及未完成exit保留鎖；後續受阻列不刪除。

| 策略 | 股票 | signal | entry | exit | entry狀態 | exit狀態 | 最終狀態 | 原primary% | 新proxy% | 阻擋trade_id |
|---|---|---|---|---|---|---|---|---:|---:|---|
| baseline_4 | 2492 | 20260421 | 20260422 | 20260521 | assumed_regular_price_proxy | unknown | exit_unknown | 77.126006994920303522659259693717135486774824544007 |  |  |
| baseline_4 | 6806 | 20260515 | 20260518 | 20260615 | unknown | not_evaluated_entry_unresolved | entry_unknown | -74.400542778646685206172456413816212757525657106388 |  |  |
| trend_8 | 6806 | 20260410 | 20260413 | 20260512 | unknown | not_evaluated_entry_unresolved | entry_unknown | -7.7496257330248130645699703013370020935088171902830 |  |  |
| trend_8 | 2492 | 20260430 | 20260504 | 20260601 | assumed_regular_price_proxy | unknown | exit_unknown | 208.01757427822747428875860040554828094524325902075 |  |  |
| trend_8 | 6806 | 20260515 | 20260518 | 20260615 | blocked_existing_lock | not_evaluated_entry_unresolved | lock_blocked | -74.400542778646685206172456413816212757525657106388 |  | common_12:trend_8:20260410:6806:D20:S10 |
| trend_8 | 2492 | 20260708 | 20260709 | 20260807 | blocked_existing_lock | not_evaluated_entry_unresolved | lock_blocked | -48.225536276217901056352417009634321119301176565728 |  | common_12:trend_8:20260430:2492:D20:S10 |

## 數值警訊及結論界線

沿用已完成的候選／價位／費稅查核，所有235/144舊候選留在primary，不新增cutoff，不把大幅報酬判錯。
不能將排除未知交易後的子集變化解讀成策略變好或變差；特殊制度與正負交易都可能使樣本無法計算。
四日OHLC既有官方對帳相符；Tick與日量盤別範圍不同，總量差不等於漏檔，也不是1,000股分配證明。
6806公告6/23下市不是本輪已核實執行；已知制度未核實結束日只維持研究unknown。
不補舊nonoverlap略過訊號，無法推論完整訊號序列重播結果；不新增試單/延後買賣/改D20。
月營收及季年財報不納入；formal_use=False、promotion_evidence_allowed=False。

## 重現

`python -B scripts/build_tdcc_stealth_accumulation_conservative_execution_research.py --source-ledger <唯讀既有F來源>`
`python -B scripts/validate_tdcc_stealth_accumulation_conservative_execution_research.py --source-ledger <同一來源>`
新主表保留每個原欄位與source_trade_row_sha256；source_manifest列來源、政策hash、精確產物hash。付費raw CSV不納repo。
