# TDCC 目前版本：D30／D40／D60 有界研究延伸 v1

research_only；formal_use=False；promotion_evidence_allowed=False；full_period_pit_complete=False。
不是 strict PIT、正式操作勝率、已核實 total-return 或模型 promotion evidence。
原始訊號區間 20250910–20260909；as_of=20260909；D60共同訊號截止=20260612。
全區間原始訊號 210140；共同區間原始訊號 158545。
來源、selector／features、1000股、雙邊0.001425/min20、sell tax0.003、slippage0/10/20bps完全沿用凍結v1。
D0為訊號後下一session open；D+h為entry_index+h close。各profile/horizon由原始訊號獨立重建非重疊帳本；出場日訊號仍阻擋。
未成熟、缺入場、缺出場與持倉阻擋分列，不算失敗；未成熟且超過既有calendar的exit_date留空並保留target index，不假造未來日曆。

## 主要結果（10 bps，保留所有未解候選）

| 區間 | D+h | 部位 | 平均淨proxy% | 中位% | proxy正報酬% | 未成熟／缺出場 |
|---|---:|---:|---:|---:|---:|---:|
| full_period | 30 | 9871 | 1.9192773111546335 | -1.691660434966491 | 41.52568128862324 | 1414／77 |
| full_period | 40 | 7717 | 2.4979307604614647 | -2.1553705453407273 | 41.60943371776597 | 1485／49 |
| full_period | 60 | 5115 | 6.123883715662154 | -2.04270153792085 | 43.577712609970675 | 1704／33 |
| common_d60 | 5 | 27061 | -0.3554860650680348 | -1.1289071026300126 | 36.558146409962674 | 0／94 |
| common_d60 | 10 | 17686 | 0.19350748416825686 | -1.2637985117246435 | 39.13830148139771 | 0／87 |
| common_d60 | 20 | 11300 | 1.3444474652499019 | -1.394623640596384 | 41.88495575221239 | 0／48 |
| common_d60 | 30 | 8507 | 2.8866439537100193 | -1.304996379423216 | 43.41130833431292 | 0／61 |
| common_d60 | 40 | 6944 | 3.484915720507938 | -1.663172398346121 | 43.59158986175115 | 0／38 |
| common_d60 | 60 | 5115 | 6.123883715662154 | -2.04270153792085 | 43.577712609970675 | 0／33 |

## 排除候選敏感性對照（10 bps，不取代primary）

| 區間 | D+h | sensitivity部位 | 平均淨proxy% | 中位% | proxy正報酬% |
|---|---:|---:|---:|---:|---:|
| full_period | 30 | 9509 | -0.7375417272460604 | -2.0077042894527977 | 39.40477442422968 |
| full_period | 40 | 7445 | -0.7283758761368487 | -2.5108214825965725 | 39.543317662860986 |
| full_period | 60 | 4892 | 0.8533275213879898 | -2.6567896337163397 | 41.067048242027795 |
| common_d60 | 5 | 26324 | -0.9909677475341659 | -1.2155915086561673 | 34.97188877070354 |
| common_d60 | 10 | 17186 | -0.7970298350275316 | -1.4029080893642643 | 37.466542534621205 |
| common_d60 | 20 | 10887 | -0.6275541640684097 | -1.6349728579157472 | 39.799761183062365 |
| common_d60 | 30 | 8183 | 0.03278812154636275 | -1.623624316858492 | 41.25626298423561 |
| common_d60 | 40 | 6687 | 0.03791924564741831 | -2.116876875836787 | 41.48347540002991 |
| common_d60 | 60 | 4892 | 0.8533275213879898 | -2.6567896337163397 | 41.067048242027795 |

## 未入場／未成熟／缺出場原因分布

| 區間 | D+h | 類別 | 原因 | 訊號數 |
|---|---:|---|---|---:|
| common_d60 | 5 | operation_censored | open_unresolved_exit_price | 94 |
| common_d60 | 5 | operation_no_entry | blocked_active_position | 113001 |
| common_d60 | 5 | operation_no_entry | blocked_exit_day | 18293 |
| common_d60 | 5 | operation_no_entry | entry_price_missing_or_invalid | 96 |
| common_d60 | 10 | operation_censored | open_unresolved_exit_price | 87 |
| common_d60 | 10 | operation_no_entry | blocked_active_position | 130248 |
| common_d60 | 10 | operation_no_entry | blocked_exit_day | 10452 |
| common_d60 | 10 | operation_no_entry | entry_price_missing_or_invalid | 72 |
| common_d60 | 20 | operation_censored | open_unresolved_exit_price | 48 |
| common_d60 | 20 | operation_no_entry | blocked_active_position | 141717 |
| common_d60 | 20 | operation_no_entry | blocked_exit_day | 5428 |
| common_d60 | 20 | operation_no_entry | entry_price_missing_or_invalid | 52 |
| common_d60 | 30 | operation_censored | open_unresolved_exit_price | 61 |
| common_d60 | 30 | operation_no_entry | blocked_active_position | 146146 |
| common_d60 | 30 | operation_no_entry | blocked_exit_day | 3788 |
| common_d60 | 30 | operation_no_entry | entry_price_missing_or_invalid | 43 |
| common_d60 | 40 | operation_censored | open_unresolved_exit_price | 38 |
| common_d60 | 40 | operation_no_entry | blocked_active_position | 148676 |
| common_d60 | 40 | operation_no_entry | blocked_exit_day | 2851 |
| common_d60 | 40 | operation_no_entry | entry_price_missing_or_invalid | 36 |
| common_d60 | 60 | operation_censored | open_unresolved_exit_price | 33 |
| common_d60 | 60 | operation_no_entry | blocked_active_position | 151492 |
| common_d60 | 60 | operation_no_entry | blocked_exit_day | 1863 |
| common_d60 | 60 | operation_no_entry | entry_price_missing_or_invalid | 42 |
| full_period | 30 | operation_censored | open_immature | 1414 |
| full_period | 30 | operation_censored | open_unresolved_exit_price | 77 |
| full_period | 30 | operation_no_entry | blocked_active_position | 193697 |
| full_period | 30 | operation_no_entry | blocked_exit_day | 5015 |
| full_period | 30 | operation_no_entry | entry_after_as_of | 16 |
| full_period | 30 | operation_no_entry | entry_price_missing_or_invalid | 50 |
| full_period | 40 | operation_censored | open_immature | 1485 |
| full_period | 40 | operation_censored | open_unresolved_exit_price | 49 |
| full_period | 40 | operation_no_entry | blocked_active_position | 197037 |
| full_period | 40 | operation_no_entry | blocked_exit_day | 3789 |
| full_period | 40 | operation_no_entry | entry_after_as_of | 14 |
| full_period | 40 | operation_no_entry | entry_price_missing_or_invalid | 49 |
| full_period | 60 | operation_censored | open_immature | 1704 |
| full_period | 60 | operation_censored | open_unresolved_exit_price | 33 |
| full_period | 60 | operation_no_entry | blocked_active_position | 200717 |
| full_period | 60 | operation_no_entry | blocked_exit_day | 2516 |
| full_period | 60 | operation_no_entry | entry_after_as_of | 2 |
| full_period | 60 | operation_no_entry | entry_price_missing_or_invalid | 53 |

immutable v1 baseline候選 2181 列維持原SHA來源；僅新profile實際匹配的同日／同股／同horizon延續旗標，未代表候選不灌入新分母。
新anomalies共 33742 列（含paired觀察候選）；old candidates與Q1/Q3±3IQR只觸發調查，全部保留primary；排除版只作sensitivity，不是corrected/cleaned performance。
54組完整成本與primary/sensitivity、勝／平／負、>=10%／<=-10%、極值、缺日分組見summary；不同帳本分母不能合成單一策略績效。

## 新帳本數值調查候選（10 bps，每組列出最高與最低）

| 區間 | D+h | 訊號日 | 股票 | 淨proxy% | 狀態 |
|---|---:|---|---|---:|---|
| full_period | 30 | 20260708 | 5904 | -89.690820982125225043501645786903938389535848303548 | unresolved_anomaly_candidate；保留primary |
| full_period | 30 | 20260527 | 2380 | 248.28666582231228668941979522184300341296928327645 | unresolved_anomaly_candidate；保留primary |
| full_period | 40 | 20260708 | 5904 | -90.022928762566828532033136392426496079000465270950 | unresolved_anomaly_candidate；保留primary |
| full_period | 40 | 20260130 | 6217 | 309.14309033785172040735182845304787516517244953193 | unresolved_anomaly_candidate；保留primary |
| full_period | 60 | 20250919 | 8422 | -87.784817158443409377536788689463966390326227056374 | unresolved_anomaly_candidate；保留primary |
| full_period | 60 | 20260122 | 6830 | 412.71457794083443594343076547415810892730583846721 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 5 | 20251114 | 8277 | -43.214828314637036575363067706415145175670920155915 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 5 | 20260306 | 4973 | 72.521200851107205140942359523528416679206215881160 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 10 | 20260203 | 2230 | -56.891837499058416148115051315921110945959157946731 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 10 | 20260203 | 6861 | 99.071427381478816610719940609679192872299998016638 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 20 | 20251029 | 8422 | -90.078280059307095780121718160013589027244568098851 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 20 | 20251117 | 7717 | 160.16954511150282176569716824853255439669799207458 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 30 | 20251219 | 7780 | -83.942077880601638093366226929745070241017362523063 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 30 | 20260527 | 2380 | 248.28666582231228668941979522184300341296928327645 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 40 | 20251231 | 7780 | -89.069753581819080790738486214740245054739208262745 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 40 | 20260130 | 6217 | 309.14309033785172040735182845304787516517244953193 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 60 | 20250919 | 8422 | -87.784817158443409377536788689463966390326227056374 | unresolved_anomaly_candidate；保留primary |
| common_d60 | 60 | 20260122 | 6830 | 412.71457794083443594343076547415810892730583846721 | unresolved_anomaly_candidate；保留primary |

## 同事件配對觀察（10 bps）

配對採common原始signals，同股同entry且六種horizon都有有效exit的相同事件集。事件可以重疊，屬觀察性complete-case選樣、不是portfolio績效；不影響主帳本。
| D+h | 同事件數 | 平均淨proxy% | 對D20平均差（百分點） | 對D20中位差 |
|---|---:|---:|---:|---:|
| 5 | 154252 | -0.47649429593446374 | -1.5312608287920761 | 0.3821081101818461 |
| 10 | 154252 | -0.02360718176570839 | -1.0783737146233208 | 0.33294362217090284 |
| 20 | 154252 | 1.0547665328576123 | 0.0 | 0.0 |
| 30 | 154252 | 2.1767165619484694 | 1.1219500290908568 | -0.29705748325427855 |
| 40 | 154252 | 3.4840252702491004 | 2.4292587373914882 | -0.25440307540238216 |
| 60 | 154252 | 5.8723446188560855 | 4.8175780859984725 | -0.32423921374813414 |

paired_summary保留全部事件，不依異常幅度刪除；沒有配對sensitivity。18列使用完全相同eventset_sha256。零事件表示資料不足，不阻塞主帳本。
配對common原始訊號 158545；六horizon共同有效事件 154252；缺有效入場／任一出場排除 4293；可能91開頭TDR事件 356。候選數逐horizon列在paired_summary，不轉為錯誤資料判決。
原發布版本可得性、普通股身分、完整休市與公司行動coverage均未認證；strict ledger仍blocked_input_availability_unproven，proxy出場不解除strict鎖。
不調參、不新增選股或風控gate，不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利、季度及年度財報全部排除。
不生成PDF、formal adapter、readiness、approval、Pages或workflow。原v1九檔保持不變。
