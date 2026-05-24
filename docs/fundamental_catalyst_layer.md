# 財報 / 事件催化資料層

這一層是每日全市場候選股模型的跨分類標籤，不新增第七大分類。股票仍保留原本六大分類：

1. 嚴格突破
2. 區間內轉強 / 挑戰前高觀察
3. 營收爆發低反應股
4. 營收成長股價回檔
5. 回檔後短線轉強
6. 型態觀察

## 資料表

- `data/theme_events/theme_event_calendar.csv`
- `data/theme_events/company_theme_mapping.csv`
- `data/fundamental_catalysts/quarterly_catalyst.csv`
- `data/event_catalysts/event_catalyst_log.csv`
- `output/history/catalyst_performance/catalyst_performance.csv`

`company_theme_mapping.csv` 可由 `config/stock_theme_map.csv` 初始化，但它只提供背景題材。若沒有公告、法說、訂單、財報或可信事件來源，不會單獨升級為 confirmed catalyst。

## 候選股欄位

- `theme_strength_score`
- `catalyst_strength_score`
- `catalyst_tags`
- `fundamental_catalyst_score`
- `fundamental_catalyst_tags`
- `event_catalyst_tags`
- `price_reaction_level`
- `low_reaction_after_catalyst`
- `already_reacted_to_catalyst`
- `catalyst_overheated`
- `similar_to_shihsinko_flag`
- `catalyst_summary`
- `catalyst_confidence`

## 判斷原則

- 核心是「利多出現 + 股價尚未完全反應 + TDCC 未轉弱」。
- EPS surprise、毛利率改善、虧轉盈、訂單、客戶、量產、技術驗證等事件，必須有資料來源。
- 只有新聞或題材 mapping，不等於高信心利多。
- 營收好但 EPS 未確認時，標示 `revenue_good_eps_unconfirmed_flag=True`，不自動升級。
- 營建認列型、交屋認列型不能只靠單月營收暴增被標為類事欣科型。
- TDCC `distribution_warning`、利多已反應、過熱，都不得被標為 `similar_to_shihsinko_flag=True`。

## 追蹤

`scripts/update_catalyst_performance.py` 追蹤事件後 D+1 / D+3 / D+5 / D+10 / D+20 報酬、相對 TWSE / TPEx / benchmark 報酬、MFE / MAE、TDCC 狀態與價格反應層級。

`scripts/validate_catalyst_layer.py` 檢查資料表 schema、候選股欄位、packet 連結、催化摘要與禁止升級條件。
