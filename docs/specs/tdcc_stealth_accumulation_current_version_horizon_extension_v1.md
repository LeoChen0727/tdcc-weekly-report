# TDCC 目前版本持有期延伸 v1

這是單一模型 `tdcc_stealth_accumulation` 的有界 research-only 延伸，不是 strict PIT、正式操作勝率、已核實 total-return 或 promotion evidence。不得調參或新增選股／風控門檻；不使用月營收或任何季度／年度財報欄位。

## 唯一 opt-in 入口與版本隔離

既有 `scripts/build_tdcc_stealth_accumulation_current_version_annual_replay.py` 增加明確 `--horizon-extension-contract`，分派 `scripts/tdcc_stealth_accumulation_current_version_horizon_extension.py`。`--input-root` 仍為必要。沒有此flag時，原v1 contract、build與九檔流程完全不變。沒有新owner、framework或workflow。

契約：`config/tdcc_stealth_accumulation_current_version_horizon_extension_v1.json`。只允許exact canonical contract hash，不接受自由horizon／來源／日期覆寫。

本次明確授權同模型相依：引用原annual producer的 immutable Git reader、external exactpath/SHA讀取、canonical價格／補充價格技術轉換、價格有效性、固定成本現金流及序列化函式；這些函式不修改。新帳本、profile、摘要與配對由本module持有。validator不匯入producer業務函式。

原v1九份artifact的HEAD Git mapping及實體存在／SHA在整個guard前後比較，新writer另要求exact7 byte payloads與原registered output directory，不允許寫入retained-evidence或symlink。新檔前綴不同於old `annual_replay_`，不污染old validator exact-nine glob。

## 固定來源與訊號

base artifact ref=`d2f3ccfaf95562b5179f433af0b4b41d62bfee17`；base contract、source_manifest、全signals、anomalies、features經Git blob與SHA綁定。不從D20交易列選訊號，不複製全features/signals，不重算selector或phase。

日價、結果及兩份Git calendar固定 `07d992bbd9afa283355d8828a294da4524efb56d`；只讀 `data/daily_price/YYYYMMDD.csv`、`config/twse_non_trading_days.csv`、`data/market_calendar/exceptional_non_trading_days.csv`。沿原contract逐份驗65個external exactpaths/SHA；不下載、不改原receipt或付費CSV。年度／暖機範圍、55週TDCC、七股八JSON與唯一absent day recovery全部沿用，無新source。

完整驗證模式是 `immutable_v1_signals_and_independent_horizon_source_replay_not_selector_revalidation`：引用已驗證immutable signals，本輪獨立重建horizon帳本，不冒稱再驗selector／features。published-only可由固定Git行情與唯一20250915 immutable v1features行情列核對；這是明列單日published verification來源，不是一般來源fallback，也不代替full模式原recovered CSV及65hash驗證。

## 主帳本與共同日期區間

- `full_period`：原訊號20250910–20260909，D30／D40／D60。
- `common_d60`：先依D60預定出場不晚於as_of=20260909的最大signal_date截相同原始signals，再分別建立D5／D10／D20／D30／D40／D60。截止日由calendar計算，不硬編碼，不以股票結果有效性決定。

每個(profile,horizon)從空持倉鎖開始。D0=next session open；D+h=`calendar[entry_index+h]` close，entry/target index皆從history_start所建calendar零起算。同股signal必須嚴格晚於prior exit，出場日仍阻擋，無queue、intraday、stop或take-profit。

先比較target index與as_of index判成熟，再索引日期。超過原calendar_end=20261030且未成熟的exit_date留空、保留exit_target_index；不假造未來calendar。缺entry不建倉；未成熟或缺有效exit保持proxy lock，分別列open_immature／open_unresolved_exit_price。strict因input availability未認證而保持阻擋；proxy出場不得解除strict鎖。

固定1000股，雙邊fee0.001425/min20、sell tax0.003、slippage0/10/20bps，Decimal precision50；都只是raw unadjusted price cashflow proxy。

## 候選保留與配對

immutable v1完整anomalies的SHA及候選數保存在manifest。只有本profile確有相同(signal_date,stock_id,horizon)交易者延續候選旗標；未代表者保存在baseline audit，不複製到新profile分母，不跨horizon推定。各profile/horizon的10bps Q1/Q3±3IQR只能新增調查候選。候選全部保留primary；主summary排除候選版只是sensitivity，不是corrected/cleaned performance。

配對從common原始signals開始，同股同entry且六種horizon皆有效exit才收事件；可重疊、無持倉鎖，是觀察性complete-case選樣，不是portfolio，不影響主帳本。18列=6h×3cost，固定相同eventset。eventset SHA為依(signal_date,stock_id)排序的`[[signal_date,stock_id,entry_date],...]`，以sorted-key/indent2/UTF8/final-LF canonical JSON計算。每筆先以Decimal算對D20差值，再彙總平均／中位／正零負；不是兩個不同樣本平均相減。

配對只有primary，沒有配對sensitivity。沿用相同key舊候選及配對母體的新IQR候選、可能91開頭TDR數均揭露，不依幅度刪除；pair候選profile為`paired_common_d60`，不代表main non-overlap proxy trade。零完整事件保留18列空摘要與不足標籤，不阻塞主帳本。

## 七份新產物

位置 `output/research/tdcc_stealth_accumulation/`，前綴 `tdcc_stealth_accumulation_current_version_horizon_extension_`：

1. `source_manifest_v1.json`：固定contract、base/Git/external bindings、calendar、cutoff、counts及其餘六檔最終bytes SHA。
2. `trades_v1.csv.gz`：原trade schema加profile、entry_index、exit_target_index。
3. `blocked_v1.csv.gz`：原blocked schema加profile及indices；每signal先strict再可選proxy阻擋／censor。
4. `summary_v1.csv`：54列，profile、cutoff、成本與primary/sensitivity完整分布。
5. `anomalies_v1.csv`：原anomaly schema加profile；primary全部保留。
6. `paired_summary_v1.csv`：18列，同eventset、配對差、候選/TDR數及非portfolio標籤。
7. `report_v1.md`：結果與限制。

gzip deterministic mtime=0；blocked/trades序列化不建立未壓縮CSV副本。原私有CSV不發布，原v1九檔不重算或改寫。所有formal/PIT/promotion/完整coverage旗標為False；沒有PDF、adapter、readiness、approval或production同步。

## 執行

```text
python -B scripts/build_tdcc_stealth_accumulation_current_version_annual_replay.py --horizon-extension-contract config/tdcc_stealth_accumulation_current_version_horizon_extension_v1.json --input-root <authorized-private-input-root> --price-repository-root <fixed-source-git-repository>
```

僅授權後在exact model guard之下執行；code-only測試使用合成資料，不代表真實來源或PIT驗證。
