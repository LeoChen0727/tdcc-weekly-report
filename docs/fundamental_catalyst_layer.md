# 財報 / 事件催化層

此層用於每日全市場候選股模型，目標是標示「利多出現、股價尚未完全反應、且 TDCC / 量價沒有轉壞」的候選股。

它不是第七大分類。候選股仍保留原本六大分類：

1. 嚴格突破
2. 區間內轉強 / 挑戰前高觀察
3. 營收爆發低反應股
4. 營收成長股價回檔
5. 回檔後短線轉強
6. 型態觀察

## 目前資料來源

- 已使用：每日候選股、月營收、價格反應、TDCC、權證、產業 / 題材欄位。
- 預留：`data/fundamentals/quarterly_financials.csv`、`data/fundamentals/eps_quarterly.csv`。
- 預留：`data/events/catalyst_events.csv`、`data/events/material_events.csv`。

目前 repo 尚未有結構化 EPS、毛利率、季報或重大事件資料，因此系統不會只靠營收把股票升級為「類事欣科型」。

## 主要欄位

- `fundamental_catalyst_score`
- `fundamental_catalyst_tags`
- `event_catalyst_tags`
- `similar_to_shihsinko_flag`
- `revenue_good_eps_unconfirmed_flag`
- `low_reaction_after_catalyst`
- `already_reacted_to_catalyst`
- `catalyst_quality`
- `catalyst_confidence`

## 判讀原則

- 有 EPS surprise、毛利率改善、獲利轉強或事件催化，才可進入較高信心催化觀察。
- 營收好但 EPS 尚未確認，只標示為「等 EPS 確認」。
- 利多已反應、短線過熱、TDCC 轉弱，必須降級。
- 營建 / 交屋認列型不能只因單月營收 YoY 暴增就標示為類事欣科型。
- 金融 / 資產型營收不與出貨型營收同權重比較。
