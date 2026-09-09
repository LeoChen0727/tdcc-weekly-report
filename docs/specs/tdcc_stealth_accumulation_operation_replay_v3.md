# TDCC 潛伏吸籌：方案 A 獨立研究操作回放 v3

使用者於 2026-09-09 採用方案 A；本契約僅適用研究 owner
`tdcc_stealth_accumulation_operation_replay`，不是正式模型 promotion。
`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。

## 固定來源與保留界線

- 原始 selector、36 個候選快照、價格及既有日曆：
  `7ef37a966280201a5ee236856306fdb513de7092`。
- 已接受 v2 detail 與六筆 price/PIT observation：
  `2244a0a36c4542cd62948b50f12ef98ade50e1df`。
- v2 detail SHA-256：
  `4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3`。
- 不重建或覆寫 v1/v2、price/PIT audit；既有訊號列加權報酬不是本版
  持倉績效。v2 的 enum 解讀保持 research-only，不改 production selector。
- 月營收只保留既有 lineage；EPS、毛利率、營益率、營業利益、業外損益、
  淨利及季度／年度財報均不在範圍。

## 日期、資訊與持倉

訊號在收盤後確認。逐特徵有效日不得晚於 signal_date，且每個實際使用
的特徵都必須有可接受的歷史可用證據，available_at 嚴格早於預定入場
交易日 08:30 Asia/Taipei。08:30 整不通過。Git commit、snapshot generated_at、
今日下載或回補均不自動證明逐特徵歷史可用。

入場為下一個交易所交易日開盤，該日為 D0；獨立 D+5/D+10/D+20 帳本
在入場後第 5/10/20 個交易所交易日收盤出場。不得跳到下一筆有價格的日子。
repo 日曆只作可重現的預定日期依據；缺官方原事件完整證據時須明列缺證，
不能把假設日曆標為已通過官方核驗。

每個帳本內同股最多一個持倉，不加碼、不排隊。持有中訊號保留但不成交；
再入場必須 signal_date > 上次 exit_date。缺預定出場價格、不可成交或公司行動
證據不足時保留 unresolved 持倉與鎖，不自動平倉。三個 horizon 的鎖互相獨立。
第一輪不設任何中途價格停損／停利，只採固定窗；不做跨股資金配置或跨模型排序。

同股同日多來源合併事件，保留全部來源列。比較真正解析後的訊號值及生效
分支：phase/status/boolean/enum 路徑、量比、5/20 日報酬、區間高低、收盤，
以及 attack 判定採用的 OHLC、20 日均量、previous close、breakout level、
daily return 與 volume_confirmed_breakout。各欄使用 v2 的 name/name_x/name_y
與 alias 優先序；未採用的備援值、path/hash/category 差異不構成訊號衝突。
欄位來源名稱另外保留 lineage；數值不同即保留衝突，不因兩列都 selected 而忽略。
有衝突事件不得任選一列建立可執行持倉。

## 成本與公司行動

Q=1000；各邊手續費率 0.001425、最低 20；賣出稅 0.003。
各邊滑價基準 0.001，另列 0 與 0.002 敏感度，三者交易集合必須一致。
全程 Decimal，不作中間四捨五入；CSV 保留計算精度，僅報告顯示可四捨五入。

`B=Q*open*(1+s)`；`S=verified_exit_shares*close*(1-s)`。
`buy_fee=max(20,B*0.001425)`；`sell_fee=max(20,S*0.001425)`。
`entry_cash=B+buy_fee`；`net_exit_cash=S-sell_fee-S*0.003+verified_cash_flows`。
`net_return_pct=(net_exit_cash-entry_cash)/entry_cash*100`。

毛額與淨額分列：`gross_pnl=verified_exit_shares*close+verified_cash_flows-Q*open`；
`gross_return_pct=gross_pnl/(Q*open)*100`。毛額使用原始未滑價價格及核實股數／
現金流，不含費用、交易稅或滑價。

僅核實的股數變更與現金流可套用；使用未還原價格並單次計入核實現金流，
禁止 adjusted price 再加現金股利。缺完整公司行動覆蓋不視為「沒有事件」。
現有 company event calendar 是提醒線索，不是已核實的持倉現金流 ledger。
各 horizon 只套用自己持有期間的已核實公司行動；窗外事件不妨礙較早的出場。
同日現金及股數變更混合時，若沒有各事件的唯一 sequence 與 sequence_evidence_ref，
不得用輸入列順序決定現金權利；保持 unresolved，不任選有利順序。

## 指標、異常與實際資料缺證

淨利正／零／負為勝／平／敗；分母為該窗全部已實現研究持倉。
未成熟、無法入場、資訊缺證與未結持倉分開列，不算成虧損或零報酬。
淨報酬 >=10% 為高報酬描述組，<=-10% 為重大虧損描述組，不是篩選門檻。
報告包括平均、中位、虧損率、尾部損失、樣本／事件／持倉／成熟／缺證數。

既有六筆 observation 均保留 `unresolved_anomaly_candidate`，依 price/PIT audit
的 observation_id 聯結，不只讀舊 detail.anomaly_disposition。六筆及其他數值
候選保留主結果；排除版只能明確稱 sensitivity，不是 corrected performance。

5,108 個真實事件須逐一對三個 horizon 評估日期、價格、衝突及證據狀態；
不能以空交易 CSV 代替回放。若歷史可用證據不足導致零可證明持倉，報酬
統計留空並揭露限制，不代表模型報酬為零，也不代表模型回測已具正式證據。

## 產物與執行介面

同一 prefix `output/research/tdcc_stealth_accumulation/tdcc_stealth_accumulation_operation_replay_`
只寫七份新產物：`signals_v3.csv`、`events_v3.csv`、`positions_v3.csv`、
`summary_v3.csv`、`evidence_v3.csv`、`manifest_v3.json`、`report_v3.md`。
manifest 綁定各份實際序列化 bytes SHA-256、兩個來源角色、全部讀取來源雜湊。

Producer：`python scripts/build_tdcc_stealth_accumulation_operation_replay.py`
使用 `--repository-root`、`--source-ref`（預設固定原始 SHA）、
`--artifact-source-ref`（預設固定 accepted v2 SHA）。不得合併兩個來源角色。

獨立驗證：`python scripts/validate_tdcc_stealth_accumulation_operation_replay.py`。
validator 不 import producer／production 商業函式，從實際檔案與固定來源獨立
重算日期、事件覆蓋、訊號衝突、資訊 cutoff、持倉、成本、指標、異常保留與 SHA。

workflow/CI 接線由 workflow owner 處理；不得改原 25 inputs、原 price/PIT workflow
與 GAS。正式 completion 仍需正常 PR/merge、post-merge main all 與實體產物驗證。
