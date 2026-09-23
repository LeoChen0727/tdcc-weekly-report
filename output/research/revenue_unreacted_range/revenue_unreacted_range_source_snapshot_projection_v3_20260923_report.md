# 營收爆發但股價尚未反應模型：行情版本差異稽核

舊 v2 綁定 `4bcaa07123ef4a000c187dc2f19caefbec4cf252`；新 v3 候選綁定 `231d2e279a99a89f1888ece0361ea64d45f69ecd`。
兩版均以 2026/07/13 為觀察截止日，模型條件、事件組裝及計算規則不變。舊 v2 全部保留，v3 不取代 canonical latest。
補入歷史日期不代表證明當時已可取得這個資料版本；本次是固定資料版本的研究重播，不是首次發布版本的嚴格 PIT 證據。

行情有差異 856 檔；新增歷史列 29258；移除 0。
共同日期 raw OHLCV 變動 0 列；volume_ratio 變動 20393 列。
事件差異 12514 筆：{"added_episode": 4611, "changed_episode": 4157, "removed_episode": 3746}。
上述是版本差異分類，不是已查明資料錯誤或公司行動原因的判定。

## 同條件主要統計

| 版本 | 條件 | 事件數 | 可分類啟動率 % | D20 觀察數 | D20 均值 % | D20 中位 % | 未解候選數 |
|---|---|---:|---:|---:|---:|---:|---:|
| v2 | absolute_or_latest_yoy_ge15 | 1810 | 67.128 | 1589 | 3.7916 | -0.7444 | 142 |
| v2 | absolute_or_positive_accel20 | 1825 | 65.7754 | 1613 | 3.3964 | -0.7576 | 143 |
| v2 | absolute_or_turn_positive_accel20 | 1813 | 65.8318 | 1605 | 3.432 | -0.7576 | 142 |
| v2 | absolute_or_two_month_yoy_ge10 | 1677 | 65.233 | 1472 | 4.0231 | -0.7694 | 141 |
| v2 | absolute_or_two_month_yoy_ge12_5 | 1616 | 66.1049 | 1415 | 3.92 | -0.9217 | 141 |
| v2 | absolute_or_two_month_yoy_ge15 | 1557 | 66.6012 | 1370 | 3.9303 | -1.0413 | 141 |
| v2 | absolute_or_two_month_yoy_ge15_cumulative_improving | 1549 | 66.6667 | 1363 | 3.8935 | -1.0526 | 141 |
| v2 | absolute_or_two_month_yoy_ge17_5 | 1514 | 67.9592 | 1333 | 4.0546 | -1.0381 | 141 |
| v2 | absolute_or_two_month_yoy_ge18 | 1507 | 67.6892 | 1327 | 4.0232 | -1.0444 | 141 |
| v2 | absolute_or_two_month_yoy_ge20 | 1482 | 66.7355 | 1310 | 4.1396 | -1.0457 | 141 |
| v2 | absolute_or_two_month_yoy_ge25 | 1459 | 66.6667 | 1286 | 3.9875 | -1.0413 | 141 |
| v2 | absolute_strong | 1454 | 66.0297 | 1282 | 3.9749 | -1.0413 | 141 |
| v2 | two_month_yoy_ge15_only | 302 | 38.2353 | 238 | 3.701 | -0.1983 | 1 |
| v3_candidate | absolute_or_latest_yoy_ge15 | 1889 | 65.9021 | 1682 | 3.9683 | -0.5788 | 157 |
| v3_candidate | absolute_or_positive_accel20 | 1900 | 64.8265 | 1704 | 3.3016 | -0.7468 | 158 |
| v3_candidate | absolute_or_turn_positive_accel20 | 1888 | 64.8734 | 1695 | 3.3607 | -0.7386 | 157 |
| v3_candidate | absolute_or_two_month_yoy_ge10 | 1749 | 63.8978 | 1553 | 4.266 | -0.5005 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge12_5 | 1688 | 64.4518 | 1496 | 4.1759 | -0.6136 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge15 | 1625 | 64.7469 | 1447 | 4.1021 | -0.7812 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge15_cumulative_improving | 1618 | 64.6853 | 1441 | 4.1016 | -0.7916 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge17_5 | 1580 | 65.942 | 1408 | 4.2399 | -0.7565 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge18 | 1574 | 65.5797 | 1403 | 4.2098 | -0.7576 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge20 | 1548 | 64.652 | 1385 | 4.2981 | -0.7576 | 156 |
| v3_candidate | absolute_or_two_month_yoy_ge25 | 1524 | 64.6617 | 1360 | 4.1616 | -0.7498 | 156 |
| v3_candidate | absolute_strong | 1520 | 64.1651 | 1357 | 4.1374 | -0.7553 | 156 |
| v3_candidate | two_month_yoy_ge15_only | 327 | 36.0248 | 263 | 3.9131 | -0.1361 | 1 |

D20 是既有研究的突破收盤後固定期間觀察，不是正式買賣策略的實現報酬或正式勝率。
數值異常候選保留於 primary；另列的 candidate_exclusion_sensitivity_only 不得稱為修正績效。最小／最大值、虧損及高報酬比例均見 comparison.csv，不能僅憑數值大小判定資料錯誤。
本次不選出較佳條件、不調參、不升級模型；新資料版本是否採用仍待另行決定與必要的底層來源查核。
僅月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報均不在範圍。
正式 adapter、readiness、評分、排序、六份 PDF 與 Apps Script 未改動。
