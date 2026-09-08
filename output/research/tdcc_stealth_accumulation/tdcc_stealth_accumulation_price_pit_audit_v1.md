# TDCC 潛伏吸籌（`tdcc_stealth_accumulation`）價格異常與 PIT 查證

六筆 observation 的 repo 原始價格、列雜湊與 gross return 算式可核對；PIT、調整基礎與正式操作回放尚未成立，因此六筆仍為 `unresolved_anomaly_candidate`，全部留在既有主結果。這份稽核不發布修正績效。

code baseline：`e643a2ee9076c92cfa7139e05b03e1f232d497ed`；v2 artifact：`dde3ce9e39bc344297581223c6d2f10c802dc46c`；replay source：`7ef37a966280201a5ee236856306fdb513de7092`。

## 資料與時間口徑

v2 母體為 6821 signal rows、520 股票；按訊號列加權，不代表獨立交易、可執行部位或投組策略。

唯一 stock+signal_date 為 5108；同股同日多來源 groups=1437，涵蓋 3150 列，多於一列部分共 1713 列。snapshot path+row number 重複 groups=0。多 category 訊號與持倉窗重疊是不同問題，本次不去重或重算主績效。

snapshot generated_at 的日曆日期晚於 signal date：4609 列／24 snapshot 日期；晚於 signal close：6821 列。

有 entry date 的 6624 列中，generated_at 晚於 entry open：3426 列；日曆日 before/on/after entry date 分別 2200/2596/1828 列；無 entry date：197 列。以上僅為 metadata 時間比較，不能直接認定前視偏誤或資料錯誤。

## 六筆價格與根因狀態

|股票|signal|entry open|exit close|窗|gross return|enum 來源資料窗|disposition|
|---|---|---|---|---|---:|---|---|
|8261 富鼎|20260616|20260617 / 176.0|20260702 / 327.0|D10|85.795455%|20260430,20260508,20260515|unresolved_anomaly_candidate|
|2492 華新科|20260709|20260713 / 473.5|20260720 / 277.0|D5|-41.499472%|20260430,20260508,20260515|unresolved_anomaly_candidate|
|1447 力鵬|20260626|20260629 / 6.4|20260706 / 9.51|D5|48.593750%|20260430,20260508,20260515|unresolved_anomaly_candidate|
|3624 光頡|20260714|20260715 / 120.0|20260729 / 62.3|D10|-48.083333%|20260430,20260508,20260515|unresolved_anomaly_candidate|
|8358 金居|20260630|20260701 / 626.0|20260730 / 271.0|D20|-56.709265%|20260430,20260508,20260515|unresolved_anomaly_candidate|
|3653 健策|20260717|20260720 / 3175.0|20260817 / 5340.0|D20|68.188976%|20260618,20260626,20260703|unresolved_anomaly_candidate|

gross return = (exit close / entry open − 1) × 100；不含手續費、交易稅、滑價或現金股利。價格來源欄位是 repo 的來源標籤，並不等於本次取得獨立官方回應。數字大小只能觸發調查。

## 8261 富鼎：`d10_max_observed_return`

identity：snapshot `20260616` row `323`、category=`pattern`；同股同 signal date 有 1 列，categories=`pattern`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-06-30 16:25:30 Asia/Taipei`；pipeline commit time=`2026-06-17T06:31:40Z`；相對 entry open，generated_after=True、pipeline_after=True。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`b5871b7857b1990f381ddd6385ca1f9237b24adc`，time=`2026-06-16T10:26:47Z`，早於 entry open=`True`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`none`。enum 分支=`blank_candidate_enum_filled_from_trend_debug`；candidate 顯示的 tdcc_date=`20260612.0`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 11 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`20260619`，其中 repo 已登錄休市=`20260619`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260616.csv row 323](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260616.csv)；file SHA-256=`6f1beeb74170bccc08ede70642329d5823ecb4895f415afd9f99cb772236781c`；canonical row SHA-256=`8e3ad29c1ff61351972688af8e3a669c2964379b41ada891dcb70baa6f2dc6f6`。
- [output/latest/all_candidates_latest.csv row 323](https://github.com/LeoChen0727/tdcc-weekly-report/blob/578a5ddac6a5ca01f2581925a5859d37ae04a939/output/latest/all_candidates_latest.csv)；file SHA-256=`050af7096d1637344263379bc1a93eac14607d535af9d6f1d3893cd7e7cce975`；canonical row SHA-256=`8e3ad29c1ff61351972688af8e3a669c2964379b41ada891dcb70baa6f2dc6f6`。
- [output/latest/all_candidates_latest.csv row 323](https://github.com/LeoChen0727/tdcc-weekly-report/blob/b5871b7857b1990f381ddd6385ca1f9237b24adc/output/latest/all_candidates_latest.csv)；file SHA-256=`a667f65e3eeddc7edd03cd8079698eed8b0928ba89adf0c8486fea3757b3b0b7`；canonical row SHA-256=`74a6799948e9dc5ad3bb639926c843cac6a1f76146af1d574699d8cb0f7f4de6`。
- [data/daily_price/20260617.csv row 2051](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260617.csv)；file SHA-256=`6f1d791b49276f0f5455d848e788066591491fd512012e44309be0fbdff133a4`；canonical row SHA-256=`92cbe67baa4ff981d1b29b41dff5257a57bfe48ebf94c6255707cb5da4a33900`。
- [data/daily_price/20260702.csv row 2048](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260702.csv)；file SHA-256=`43d77ac58ef33b3e8d9ed75395a229cf4a308f1d60d1449198f2a7ac703ab58c`；canonical row SHA-256=`8c714e4c0d2388a8a8c6d0baf400b190964ac0fa427b836d1c73a3764c3a279b`。
- [output/latest/daily_pattern_watch_latest.csv row 32](https://github.com/LeoChen0727/tdcc-weekly-report/blob/578a5ddac6a5ca01f2581925a5859d37ae04a939/output/latest/daily_pattern_watch_latest.csv)；file SHA-256=`906e589f6258ac5382e18e007fd6df9925cf70ad67cc90711bf96355e3d673b1`；canonical row SHA-256=`bc36904e58a26dbae4f37815039418a59c04ab56bf458109277df86dd32c162e`。
- [output/latest/tdcc_trend_debug_latest.csv row 1836](https://github.com/LeoChen0727/tdcc-weekly-report/blob/578a5ddac6a5ca01f2581925a5859d37ae04a939/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`a4c79cb0871ef1d052030cc2cd6380c573e8521246572cead60e05c41b13498d`。

## 2492 華新科：`d5_min_observed_return`

identity：snapshot `20260709` row `243`、category=`revenue_pullback`；同股同 signal date 有 1 列，categories=`revenue_pullback`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-07-14 04:43:10 Asia/Taipei`；pipeline commit time=`2026-07-14T04:39:32+08:00`；相對 entry open，generated_after=True、pipeline_after=True。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`8782faae617e8a703d396ad1c2e5d2aaefbaeb85`，time=`2026-07-11T01:52:56Z`，早於 entry open=`True`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`none`。enum 分支=`blank_candidate_enum_filled_from_trend_debug`；candidate 顯示的 tdcc_date=`20260703.0`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 6 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`20260710`，其中 repo 已登錄休市=`20260710`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260709.csv row 243](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260709.csv)；file SHA-256=`7daceccf407b5976a6b7b6e5ecf7f73d6a77f793d98a05693e68fcd7b613ab82`；canonical row SHA-256=`da5abb2a435f4d6611e414256cb833de42906e420a72bedfa7e37c7b0c1b1f3a`。
- [output/latest/all_candidates_latest.csv row 243](https://github.com/LeoChen0727/tdcc-weekly-report/blob/8b8b84ae22d2cbda6c39a6b4f92b296da555e8b3/output/latest/all_candidates_latest.csv)；file SHA-256=`7daceccf407b5976a6b7b6e5ecf7f73d6a77f793d98a05693e68fcd7b613ab82`；canonical row SHA-256=`da5abb2a435f4d6611e414256cb833de42906e420a72bedfa7e37c7b0c1b1f3a`。
- [output/latest/all_candidates_latest.csv row 240](https://github.com/LeoChen0727/tdcc-weekly-report/blob/8782faae617e8a703d396ad1c2e5d2aaefbaeb85/output/latest/all_candidates_latest.csv)；file SHA-256=`fe212c612047d892942ab0350d262d066904057a2a52ffc3a2f68c7d93e1d3b2`；canonical row SHA-256=`10b49e0bdfbb815821ed4b3a2af49e63b68eca4053ed63870355761ee55b05a4`。
- [data/daily_price/20260713.csv row 1439](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260713.csv)；file SHA-256=`d6ffdaa42cccb33cdd74a55ee2d1cf468d37268d2459ebcbd43ce7840a47cbc7`；canonical row SHA-256=`1c2546b8c75414d2a97ee6a2f5a63bf88e6d5fc73afd1e746664abc43f1bc8a7`。
- [data/daily_price/20260720.csv row 1436](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260720.csv)；file SHA-256=`57229ad0aca43d78cbd9c6b333ebbb84b4ddf52ab16cb54e0bcc311d472cf898`；canonical row SHA-256=`557d39224d579de227f36c1f07c2138743675dba64ea94a4307886d957edfbc4`。
- [output/latest/revenue_pullback_latest.csv row 139](https://github.com/LeoChen0727/tdcc-weekly-report/blob/8b8b84ae22d2cbda6c39a6b4f92b296da555e8b3/output/latest/revenue_pullback_latest.csv)；file SHA-256=`4a4e5ee39f905c21a509e0b2c3971bb63eeebaad57b035b853c2400b0079bcee`；canonical row SHA-256=`6cc5f9e7424f1ce7cda70a187bb93465e24f5ae3b6a492eb04fc4bd47e77c7aa`。
- [output/latest/tdcc_trend_debug_latest.csv row 434](https://github.com/LeoChen0727/tdcc-weekly-report/blob/8b8b84ae22d2cbda6c39a6b4f92b296da555e8b3/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`abaa2212298a01ddd65befcd61b0ed127cc86ed66af44ca37e1a6bf694f3fb0d`。

## 1447 力鵬：`d5_max_observed_return`

identity：snapshot `20260626` row `324`、category=`pattern`；同股同 signal date 有 1 列，categories=`pattern`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-06-30 16:25:30 Asia/Taipei`；pipeline commit time=`2026-06-29T00:17:09Z`；相對 entry open，generated_after=True、pipeline_after=False。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`179dc72812f7162f4cdaf2b12759ee4e455fa997`，time=`2026-06-27T13:36:25Z`，早於 entry open=`True`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`none`。enum 分支=`blank_candidate_enum_filled_from_trend_debug`；candidate 顯示的 tdcc_date=`20260618.0`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 6 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`none`，其中 repo 已登錄休市=`none`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260626.csv row 324](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260626.csv)；file SHA-256=`88a8585070eeed21ddd8c39c1f2f4da9e405b1bfaae53c0906185eac648f2863`；canonical row SHA-256=`e2415e739bc50c8d90fb32fd02f0b2d49e0faed9eccf0c6515edb68525e2ea15`。
- [output/latest/all_candidates_latest.csv row 324](https://github.com/LeoChen0727/tdcc-weekly-report/blob/514294fd97375f97fb3cfb03d7633da18c98f01e/output/latest/all_candidates_latest.csv)；file SHA-256=`488bfe015ae9029e5d913e42ee1620ff4f517b9b7347b7ac2a4802b607f66e84`；canonical row SHA-256=`e2415e739bc50c8d90fb32fd02f0b2d49e0faed9eccf0c6515edb68525e2ea15`。
- [output/latest/all_candidates_latest.csv row 324](https://github.com/LeoChen0727/tdcc-weekly-report/blob/179dc72812f7162f4cdaf2b12759ee4e455fa997/output/latest/all_candidates_latest.csv)；file SHA-256=`4b8d7624f72c8b66be02c23c44ada0d8c58b0d5fc8813f18b7789ddfcb1a36ba`；canonical row SHA-256=`936f13137fcdc394e645836e6c13f418d69d7f9d72e94e2d0f578456cedbbe38`。
- [data/daily_price/20260629.csv row 1124](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260629.csv)；file SHA-256=`b1291bf7f405b215e0a800e2ef35a363e1848ec9db716977020cd1edbfe91b83`；canonical row SHA-256=`dac610fe750875e0741d753c68686673875532e184227181e0cc738db3c5476b`。
- [data/daily_price/20260706.csv row 1129](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260706.csv)；file SHA-256=`c7e3aeba582481aa00f8a18553ca5651b853a8fd8fb2e52397d1d40c3e37adcd`；canonical row SHA-256=`b27cd4e395ec5897ee4c2785b9e141064ecc18e59e1ea767dd457fbb71dddb14`。
- [output/latest/daily_pattern_watch_latest.csv row 84](https://github.com/LeoChen0727/tdcc-weekly-report/blob/514294fd97375f97fb3cfb03d7633da18c98f01e/output/latest/daily_pattern_watch_latest.csv)；file SHA-256=`1a990b6df7988cec13cdf42b13fed2948d62be79f5dd025fd480673ed9869053`；canonical row SHA-256=`f5901ec0360e99ab4f93012b427ac5e63583fb2fa1ebf11d39f3fc0ccd8b7f63`。
- [output/latest/tdcc_trend_debug_latest.csv row 85](https://github.com/LeoChen0727/tdcc-weekly-report/blob/514294fd97375f97fb3cfb03d7633da18c98f01e/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`6d05ca031172b590949a859fc225a7d0ee74b86382110cf36ac678a6f4425137`。

## 3624 光頡：`d10_min_observed_return`

identity：snapshot `20260714` row `290`、category=`revenue_pullback`；同股同 signal date 有 1 列，categories=`revenue_pullback`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-07-15 18:16:06 Asia/Taipei`；pipeline commit time=`2026-07-15T06:14:00Z`；相對 entry open，generated_after=True、pipeline_after=True。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`676690873e6123b49491864d0b3aed10ea6a5901`，time=`2026-07-15T04:48:39Z`，早於 entry open=`False`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`catalyst_tags,event_catalyst_tags,theme_strength_score`。enum 分支=`blank_candidate_enum_filled_from_trend_debug`；candidate 顯示的 tdcc_date=`20260703`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 11 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`none`，其中 repo 已登錄休市=`none`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260714.csv row 290](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260714.csv)；file SHA-256=`888e17ae8474d975ca3f4c4695e7a31ec9c09a6d287701835dc2fd2f2a887838`；canonical row SHA-256=`88b8d57aafcf2f6132940c3e439418f5f68b2ce4a84c754fd1f2fdc9790deeff`。
- [output/latest/all_candidates_latest.csv row 290](https://github.com/LeoChen0727/tdcc-weekly-report/blob/45303542983d2a1b665b7736c7143b4038751c0e/output/latest/all_candidates_latest.csv)；file SHA-256=`cb8d88889c930ce921cd4df50b0370d9d80991df1e52b327e2651f82db6214fb`；canonical row SHA-256=`0c28ef31c4031a688f7b99da3e9f60a6b1c62e9ef49ef74103e58951d0d6e13a`。
- [output/latest/all_candidates_latest.csv row 290](https://github.com/LeoChen0727/tdcc-weekly-report/blob/676690873e6123b49491864d0b3aed10ea6a5901/output/latest/all_candidates_latest.csv)；file SHA-256=`1b5ddaea3a6f57a2a9c9e5b9667e8fb2bbc649cb70967cd49b039dddda4d40e2`；canonical row SHA-256=`48adca041a826aa6141320d689f85fd39cd0a3c13d5a64976cdbead011c85d3f`。
- [data/daily_price/20260715.csv row 226](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260715.csv)；file SHA-256=`52e4773de2880da63becd84c41439e4d577d0fd1900c8a56e176086a109448e9`；canonical row SHA-256=`ede204e25848fbfdeb23a94c7355b4ebe733d42b93da0a5827d24e6eea200285`。
- [data/daily_price/20260729.csv row 228](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260729.csv)；file SHA-256=`c73c5a0617fe7cab53c97ce9a53cef1e1f1252d612748f70b438cf678c987d84`；canonical row SHA-256=`b601d66cc69f7ca31b18809349ab61b8acd5ac1eb2b4b888836bd0550f49daff`。
- [output/latest/revenue_pullback_latest.csv row 168](https://github.com/LeoChen0727/tdcc-weekly-report/blob/45303542983d2a1b665b7736c7143b4038751c0e/output/latest/revenue_pullback_latest.csv)；file SHA-256=`7191fa716663697026a293a6bc9f08a1b627585f4a3512c5b9dd1d383ce4c343`；canonical row SHA-256=`74124abc428acdb58bdaed9fa2e648f5ed2d2fca17cf09b89c543be0a6791da2`。
- [output/latest/tdcc_trend_debug_latest.csv row 841](https://github.com/LeoChen0727/tdcc-weekly-report/blob/45303542983d2a1b665b7736c7143b4038751c0e/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`a31714ea698dc20dbbe4514ff0bdbe965c0ce0c04a90c387a9c997eb1eafc792`。

## 8358 金居：`d20_min_observed_return`

identity：snapshot `20260630` row `214`、category=`revenue_pullback`；同股同 signal date 有 2 列，categories=`revenue_pullback;pullback_rebound`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-07-01 13:49:33 Asia/Taipei`；pipeline commit time=`2026-07-01T13:29:39+08:00`；相對 entry open，generated_after=True、pipeline_after=True。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`3387e34244bfbf8eccd27b3b95996f5ffa4f23fb`，time=`2026-06-30T06:45:08Z`，早於 entry open=`True`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`none`。enum 分支=`blank_candidate_enum_filled_from_trend_debug`；candidate 顯示的 tdcc_date=`20260626.0`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 21 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`20260710`，其中 repo 已登錄休市=`20260710`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260630.csv row 214](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260630.csv)；file SHA-256=`411489f72c1ee981cf1473e7cee0e57917da396ce941d2bbff79a5f14cadc6d0`；canonical row SHA-256=`99209c8d5d03fa58d429e44e1c31605a2a7df1279f3f29a141cea0a4ab819c69`。
- [output/latest/all_candidates_latest.csv row 214](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7a53a9acb96456afbea750fc531d11af52c89494/output/latest/all_candidates_latest.csv)；file SHA-256=`411489f72c1ee981cf1473e7cee0e57917da396ce941d2bbff79a5f14cadc6d0`；canonical row SHA-256=`99209c8d5d03fa58d429e44e1c31605a2a7df1279f3f29a141cea0a4ab819c69`。
- [output/latest/all_candidates_latest.csv row 211](https://github.com/LeoChen0727/tdcc-weekly-report/blob/3387e34244bfbf8eccd27b3b95996f5ffa4f23fb/output/latest/all_candidates_latest.csv)；file SHA-256=`e4ba610804f99c25d1021acef082e6f7e3549178ebb38378ff2d9b837d816705`；canonical row SHA-256=`4041e2549ab06d347d743834bde886b3fd645892ecafa4a9a9e15f3bf4aeb2c6`。
- [data/daily_price/20260701.csv row 846](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260701.csv)；file SHA-256=`1cf8d05ccc3edb9f2a861b2942a3b4159f5e3ecb18aaa80b20e6b6240e894553`；canonical row SHA-256=`3540e76ad4496dec932bb7f15f5197865e90f9a1a93053bf67f62cc4f7684069`。
- [data/daily_price/20260730.csv row 831](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260730.csv)；file SHA-256=`8362199c0bd89bbcbb1b1557706634d929a0c7a335851074f64df75bc02bf6c9`；canonical row SHA-256=`61e5c8b43b8a2d757efd2a5ad7f2520029cc16634d4944289a4f5647311572fd`。
- [output/latest/revenue_pullback_latest.csv row 45](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7a53a9acb96456afbea750fc531d11af52c89494/output/latest/revenue_pullback_latest.csv)；file SHA-256=`03247b32d4882babbb9bde17f52bbc3d2f9702d2e38e26e83afafccb26c4e76f`；canonical row SHA-256=`032baf9379b17acb11ed86b78808b20a11350f482d99ef8d3ead1dc60e628858`。
- [output/latest/tdcc_trend_debug_latest.csv row 1849](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7a53a9acb96456afbea750fc531d11af52c89494/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`ca2ad3f4f21874dc08227e0afaaf90eee7d324be771d375f36d2b9180b8ee5dc`。

## 3653 健策：`d20_max_observed_return`

identity：snapshot `20260717` row `64`、category=`revenue_breakout_low_response`；同股同 signal date 有 1 列，categories=`revenue_breakout_low_response`。重複訊號不等於 byte duplicate，也未依持倉窗去重。

generated_at=`2026-07-18 08:19:29 Asia/Taipei`；pipeline commit time=`2026-07-17T21:15:44Z`；相對 entry open，generated_after=False、pipeline_after=False。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。

有界查得相同 selector inputs 的歷史 candidate commit：`4f261ce76707955699cd9ac8c0059cd00abc07ff`，time=`2026-07-17T15:46:29Z`，早於 entry open=`True`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。

snapshot 與 pipeline candidate 的 selector input 差異 0；其他共同欄位差異：`catalyst_date,days_to_nearest_event,gap_up_failed_after_catalyst,long_upper_shadow_after_catalyst,price_reaction_after_catalyst,price_return_1d_after_catalyst,theme_strength_score,volume_ratio_after_catalyst`。enum 分支=`existing_candidate_enum_preserved`；candidate 顯示的 tdcc_date=`20260703`，不可直接當作 enum 的來源窗。

entry 至 exit 的 source sequence 21 列（含 entry）；個股缺列日期=`none`；repo 無日期檔的平日=`none`，其中 repo 已登錄休市=`none`；未有休市登錄的缺檔平日=`none`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。

enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。

|八項根因檢查|本次狀態|
|---|---|
|`identity_dedup_non_overlap`|`partial`|
|`formal_operation_replay`|`not_established_user_decision_pending`|
|`point_in_time_and_trading_calendar`|`partial`|
|`raw_source_lineage_and_hash`|`verified_commit_row_lineage`|
|`units_formula_and_adjustment_basis`|`partial`|
|`authoritative_business_event_history`|`partial`|
|`independent_source_corroboration`|`partial`|
|`reproducible_evidence_reference`|`verified_commit_row_lineage`|

可重現來源：

- [output/history/daily_model_snapshots/all_candidates_20260717.csv row 64](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/output/history/daily_model_snapshots/all_candidates_20260717.csv)；file SHA-256=`0084a246ef84fd1f1a228bd4fb74a6a987e93d98cf98aad44782ed931ab67bac`；canonical row SHA-256=`f14af1fdbf81866f77b7a5e5ce8fb85f300f30e3181102d69bb5d7e864953d19`。
- [output/latest/all_candidates_latest.csv row 64](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/latest/all_candidates_latest.csv)；file SHA-256=`25cb77951ebfa55b37a5046d7ba08ffd2a6c9c004778932f72775ee3ddbbfe4b`；canonical row SHA-256=`93db77c698ea19992dfc7720adf3ccb9d8c6e2178c23a223a0198137615d473d`。
- [output/latest/all_candidates_latest.csv row 64](https://github.com/LeoChen0727/tdcc-weekly-report/blob/4f261ce76707955699cd9ac8c0059cd00abc07ff/output/latest/all_candidates_latest.csv)；file SHA-256=`25cb77951ebfa55b37a5046d7ba08ffd2a6c9c004778932f72775ee3ddbbfe4b`；canonical row SHA-256=`93db77c698ea19992dfc7720adf3ccb9d8c6e2178c23a223a0198137615d473d`。
- [data/daily_price/20260720.csv row 1672](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260720.csv)；file SHA-256=`57229ad0aca43d78cbd9c6b333ebbb84b4ddf52ab16cb54e0bcc311d472cf898`；canonical row SHA-256=`89c977a90c07e15355b3f624ebe9dada377b8ac6dffbc412769c141ac85a2210`。
- [data/daily_price/20260817.csv row 1671](https://github.com/LeoChen0727/tdcc-weekly-report/blob/7ef37a966280201a5ee236856306fdb513de7092/data/daily_price/20260817.csv)；file SHA-256=`584c81a07e0564d854a559ff7b1ce376a005f1827385d00b31ea52480c0b7ef0`；canonical row SHA-256=`df525678318e57e97c406e8cdfa45331477e277e80819bc8544dea8367a67ea9`。
- [output/latest/revenue_breakout_low_response_latest.csv row 8](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/latest/revenue_breakout_low_response_latest.csv)；file SHA-256=`3f073cab504a56170a31dbb949cfe3931e83c8bf36ec883c8f11dd422486686e`；canonical row SHA-256=`9100e8baa30cb48209da6f95fbd7df4896be59b1af74352ca7fc651f4b09dab3`。
- [output/latest/tdcc_trend_debug_latest.csv row 851](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/latest/tdcc_trend_debug_latest.csv)；file SHA-256=`5e446aeea5d77006ff602f5217eb57f744f32cbf99d48654d1755c3c2e576747`；canonical row SHA-256=`492ae5fcf580b4969609c931c6d071767e5759c88ad167003d622d4d8d218fec`。
- [output/history/tdcc/tdcc_holder_ratio_20260618.csv row 850](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/history/tdcc/tdcc_holder_ratio_20260618.csv)；file SHA-256=`b45930638a87d990ae950a76423fa797618d7766c7f08aa209f6187aad1573a7`；canonical row SHA-256=`a19be650947ac35d38af542df05e28a44b5a92b694efd3f66f1abbbf0deedfdf`。
- [output/history/tdcc/tdcc_holder_ratio_20260626.csv row 848](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/history/tdcc/tdcc_holder_ratio_20260626.csv)；file SHA-256=`b7c69249e9cfb98d56e000020cab32e781195c56d0685267da333f6497cadf59`；canonical row SHA-256=`1c921e6f8442f05f002c6ca21ad20dd1ee3c02225e64789f83a9b32e2fc64d67`。
- [output/history/tdcc/tdcc_holder_ratio_20260703.csv row 850](https://github.com/LeoChen0727/tdcc-weekly-report/blob/a45c1a25e7e03fb8040d903339045892742cb3c0/output/history/tdcc/tdcc_holder_ratio_20260703.csv)；file SHA-256=`fa4528266ad053a05b4b72a19e82a315f71b5ec60770b38c5186e9dbe9b0afea`；canonical row SHA-256=`c1b6ef145d6f81426add4a8b6bb686a538fbcfca4a70aa7cffe4109e92bea203`。

## 外部事件證據與取得限制

- 8358：[金居公司股利資訊](https://www.co-tech.com/tw/ir/board)；status=`company_html_event_observation`。114年度現金股利每股NT$2；20260717除權息交易日、20260721–25停止過戶、20260820發放。 停止過戶不是停牌；頁面未載原公告發布時間，此事件不能證明626至271變化的根因或完整調整基礎。
- 3624：[光頡公司股利查詢入口](https://www.viking.com.tw/zh-TW/investors/Investors-T0304.html)；status=`company_html_mops_link_only`。頁面只提供MOPS股利分派查詢入口及操作說明。 未取得對應期間完整公司事件資料，不能推論沒有事件。
- 3653：[健策公司股利沿革查詢](https://www.jentech.com.tw/zh/shareholder-corner/dividend-history)；status=`root_fetch_timeout_coordinator_coverage_incomplete`。本次主執行者web.open逾時；總管先前讀取頁面未涵蓋本次完整2026期間。 覆蓋不足或逾時均不代表該期間無公司事件。
- 3624：[櫃買公告11503018581查詢線索](https://www.tpex.org.tw/storage/eb_data/11507/11503018581.html)；status=`coordinator_search_visible_lead_raw_unavailable_403`。總管搜尋線索指出20260709公告、20260720納入富櫃200；原頁403，僅保留查詢線索。 未取得公告原始bytes，未證明與價格變化的因果關係。
- all_six：[TWSE每日股價查詢入口](https://www.twse.com.tw/zh/trading/historical/stock-day.html)；status=`official_ohlc_verification_not_completed`。總管已撤回另一路徑取得OHLC的完成核驗判定；本報告不採納該批JSON為已接受的獨立官方價格佐證。 查詢表單本身無OHLC結果；六筆仍缺已接受的官方獨立價格核驗。
- all_six：[TWSE天然災害休市一般規則](https://www.twse.com.tw/zh/about/suspended_faq.html)；status=`coordinator_general_rule_observed_not_specific_event_proof`。總管可讀一般規則：台北市全日或上午停止上班，集中市場全日休市。 一般規則不是20260710實際停班事件證明；該日CAP URL被non-retryable safe-open拒絕。

## Snapshot 換行與雜湊基礎

舊 replay 的 snapshot_sha256 沿用 snapshot manifest；既有 producer 接受 raw、LF、CRLF 三種換行表示。本 audit 另以 source_manifest 鎖定 raw Git bytes，逐筆列出舊摘要匹配基礎；換行差異不等於價格、欄位內容或歷史版本變更。

- 8261：v2 snapshot_sha256=`6f1beeb74170bccc08ede70642329d5823ecb4895f415afd9f99cb772236781c`；raw Git SHA-256=`6f1beeb74170bccc08ede70642329d5823ecb4895f415afd9f99cb772236781c`；matching_bases=`raw_git_bytes;lf`。
- 2492：v2 snapshot_sha256=`1258dab3123fb95746063e555b0f8cad00a902c9dca4f2ece4315506c7d9db98`；raw Git SHA-256=`7daceccf407b5976a6b7b6e5ecf7f73d6a77f793d98a05693e68fcd7b613ab82`；matching_bases=`lf`。
- 1447：v2 snapshot_sha256=`88a8585070eeed21ddd8c39c1f2f4da9e405b1bfaae53c0906185eac648f2863`；raw Git SHA-256=`88a8585070eeed21ddd8c39c1f2f4da9e405b1bfaae53c0906185eac648f2863`；matching_bases=`raw_git_bytes;lf`。
- 3624：v2 snapshot_sha256=`aadbc3a7608f56c423fb5315aa17aa876643a679e6a074bb18a16a33fb72f173`；raw Git SHA-256=`888e17ae8474d975ca3f4c4695e7a31ec9c09a6d287701835dc2fd2f2a887838`；matching_bases=`lf`。
- 8358：v2 snapshot_sha256=`ba13db2c39763d43ab0d018866a8505310b558b518755e1b96c0cc87bef012a2`；raw Git SHA-256=`411489f72c1ee981cf1473e7cee0e57917da396ce941d2bbff79a5f14cadc6d0`；matching_bases=`lf`。
- 3653：v2 snapshot_sha256=`1cc63fffc379e65ec5fcff05644b67fdac4cf9af30222dae44f6f14da08a1b88`；raw Git SHA-256=`0084a246ef84fd1f1a228bd4fb74a6a987e93d98cf98aad44782ed931ab67bac`；matching_bases=`lf`。

## v2 原有 artifact digest 差異

detail 實際 SHA-256=`4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3`；summary 內嵌值=`2d7f7b3b3a1428e1e453893a7dba31b6ff405a642343115adeb894dbe08dcf64`。embedded_hash_mismatch=True。

僅在記憶體清空 6 列的 observation code/status 兩欄、其餘內容與欄序不變，重新序列化得到 `2d7f7b3b3a1428e1e453893a7dba31b6ff405a642343115adeb894dbe08dcf64`，與內嵌值相符=True。v2 wrapper 在 base.build 計算 digest 後才加標籤；這是摘要綁定缺陷，不是價格或報酬算術錯誤。本次沿用實際 Git bytes 雜湊，未修寫舊 artifacts。

## 判讀與後續界線

八項檢查中的 formal_operation_replay 尚未成立：正式 entry/exit、成本與同股重疊處理仍待使用者決定。價格調整基礎、官方停復牌／事件覆蓋、獨立 OHLC 佐證與原始輸入可用時間亦有缺口。因此本稽核可供研究查證，不構成模型 promotion 證據。

EPS、毛利率、營業利益率、營業利益、業外損益、稅後淨利與季度／年度財報不在本次範圍；月營收僅在既有 candidate producer lineage 需要時作來源追溯。

若要修復共享 source 或制定正式 operation 規則，須由使用者另定範圍；本次只保存查證結果。舊 v1 零訊號與 v2 原始績效未覆寫，formal_use=False、trade_eligible=False、promotion_evidence_allowed=False。

機器可核對證據：`tdcc_stealth_accumulation_price_pit_audit_v1.json`；六筆表格：`tdcc_stealth_accumulation_price_pit_audit_v1.csv`。JSON 包含原始列、Git blob、file/row SHA-256、各段價格序列與 producer function 位置。
