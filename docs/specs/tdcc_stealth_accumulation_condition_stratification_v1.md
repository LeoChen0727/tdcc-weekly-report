# TDCC 潛伏吸籌條件分層研究 v1：事前契約

## 決策範圍

本研究只回答既有 `tdcc_stealth_accumulation` current-version proxy 訊號的五個小型單項假說是否具有可重現的報酬或尾部風險差異，不變更正式模型、不promotion。買賣規則、1000股成本、0/10/20bps情境、原始signals與既有16份證據凍結。既有全年aggregate已經看過，因此20260401以後只能稱time-split validation／robustness，不能稱完全盲測。

權威機器契約：`config/tdcc_stealth_accumulation_condition_stratification_v1.json`。程式基線129b8669ef17cb1a678dd71b87097cbbff084c82；immutable annual evidence d2f3ccfaf95562b5179f433af0b4b41d62bfee17；price source07d992bbd9afa283355d8828a294da4524efb56d；as_of20260909。缺證的首次發布PIT、普通股分類、休市與公司行動完整性旗標皆False。

事前契約於2026-09-13T05:36:49.2596794Z、第一次績效運算前凍結：canonical SHA-256 `1449b79b9778e7b1ecdf39f874f90e29d970fa1e728ae4427dddfcd0683e191d`。不得在看到後段結果後為配合結果修改契約、切點、候選或投影。

## 先描述，再固定單項條件

使用baseline D20、slippage10bps、entry及exit均早於20260401的成熟部位，分high>=10%、low<=-10%、middle比較特徵。對照包含TDCC兩級距淨變化與增加次數、5/20有效觀測報酬與價格狀態、20有效觀測寬度、今日是否創前20觀測新低、缺日與缺特徵。每一欄列有效/缺少分母，不能把missing當False或0。

主對話事前唯讀對照提供線索：7272成熟部位、1840股、110訊號日期；high863、low950、middle5459。雙淨增在高低組僅約42.87%／41.05%，不是強效果；寬度median高低約17.91%／18.97%，middle約12.10%，所以極窄篩選可能同時拿掉高報酬。這些只是舊baseline交易描述，不能當新策略回測。新成果必須重現其來源與分母，差異先查明，不默認filter有效。

有限集合固定為以下五個，每個各自對baseline，絕不彼此組合：

1. `tdcc_both_net_positive`：400/1000四批期間各自淨增。
2. `tdcc_both_up_count_ge2`：兩級距在三個相鄰批次變化中各至少兩次增加，獨立於net-positive；不是連續、同週或逐週同步。
3. `price_5obs_nonnegative`：5個有效觀測收盤報酬>=0。
4. `range_20obs_le_training_q75`：20有效觀測寬度<=訓練baseline primary有效寬度Q75；type7線性插值，保存精確Decimal門檻、分母、算法，後段不調。
5. `no_new_low_previous20obs`：today low>=前20有效觀測low最小值，只叫當日未創新低。

兩級距存在包含關係，不是互斥投資群。up_weeks是增加次數，不是連續週數。價格窗口沿v1的`observed_history_dates`，不把20 observations改稱連續20 sessions；保留history_gap_count但不另設排除條件。新width以immutable high_20/low_20帶入真正max(high)/min(low)-1公式，Decimal precision50且不再round，不沿用幾乎不約束寬度的in_range。return5/20保留原four-decimal序列化語意。觀測價格或欄位缺失時僅其依賴variant不成立並明列unsupported，不刪baseline訊號、不前填。價格狀態只是描述，不能宣稱底部完成。

### 有限暖機來源參考

所有窗口需389283個日期／股票配對。固定Git價格加唯一既有20250915 recovery後，65個配對只在原始6份暖機JSON，影響44個訊號（4804/4987/6171/6236/6747，20250910–20250926）。契約內`published_warmup_low_projection`是績效運算前由獨立來源讀取器計算的44個前20觀測最低價，只有exact(signal_date,stock_id,observed_dates)鍵、必要最低價和原來源hash；不公開private raw。44 rows canonical SHA-256=`7e1cfc119bd5a1cbe36a399651f4dc8e664dcd883760f590b6ec7d0ba97c22a5`。

Full producer及full independent validator各自由原raw重算44筆，逐值與此事前參考核對。Published-only只驗exact44固定衍生投影及其餘Git來源，不能宣稱CI重讀private raw。缺鍵、多鍵、重複鍵、日期序列或來源hash不符皆fail-closed；此精確來源參考不能擴成通用missing-price fallback。

## 時間切分與完整新帳本

先從210140個frozen signals chronology建立baseline，完成前段對照與Q75並保存candidate_rules，才跑其餘五個variant。各variant與D20/D60各有獨立same-stock locks，每次完整replay，不能篩選原D20 trades冒充新策略。D0為訊號後下一凍結日曆session open，D+h為entry_index+h close；signal_date須嚴格晚於既有proxy exit_date。缺exit的未解鎖維持。切分不重置鎖、不把跨界持倉清空，也不把confirmed-unavailable訊號放入queue。

- training：entry_date<20260401且scheduled_exit_date<20260401；只有成熟有效exit進入已實現分母。
- purged_cross_split：entry<20260401、exit>=20260401，單獨揭露，既不進training也不進validation績效，仍保留跨界lock。
- validation：entry_date>=20260401，未成熟及缺價分開揭露。
- D20為主要結論，D60僅robustness；二者有不同成熟度／重入場限制，不能把不同樣本平均差當同筆交易延長效果。

不依勝率最大值挑模型，不以全年異常標記或排除候選後績效選閾值，不追加grid或條件堆疊。若沒有可重現改善，就交付「目前無證據支持改條件」。

## 指標、候選與交付

各variant/horizon/slippage/partition分開primary與candidate-exclusion sensitivity：成熟部位數、股票數、訊號/入場日期數、正/零/負報酬count與rate、平均/中位數net realized proxy、高報酬>=10%命中率、loss<0及<=-10%尾部比例、未成熟/缺entry/缺exit/unsupported/filter-rejected/overlap。零分母為空/資料不足，不是0%績效。原主樣本保留全部未解候選；新quantile或幅度警訊只能標記`unresolved_anomaly_candidate`，不決定資料錯誤或正式排除。敏感度永遠不是修正或清洗績效。

候選新增規則沿用每個完整variant/horizon帳本slip10成熟列的Q1/Q3±3IQR，不另按partition找閾值。保留annual D20及horizon full_period D60同key候選；training_contrasts的排除敏感度只用immutable annual舊旗標，與新帳本全期旗標清楚區分。任何旗標均不回流Q75或候選選擇。

九份精確產物由機器契約列出：source manifest、signal-feature panel、training contrasts、frozen candidate rules、逐筆trades、blocked原因、summary、anomalies及本模型report。source manifest記錄實際source pins/hash、契約、切分／Q75及驗證範圍。保護舊annual9與horizon7、兩舊契約與其他模型產物；只允許新九份由本模式寫入。

獨立validator不import producer業務邏輯；自行重算features、Q75來源/分母、判斷、dates/locks/costs及所有summary。既有annual tests新增新九份required published消費測試，缺檔fail而非skip。全源驗證與published可查來源的範圍各自標示，不冒稱首次發布PIT。必要repo登錄與四份audit只反映新family。無workflow YAML、PDF、Apps Script、正式selector/adapter/readiness或營收／財報改動。
