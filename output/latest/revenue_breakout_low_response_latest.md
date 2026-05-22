# 營收爆發低反應股

- 產生時間：`2026-05-22 10:52:08 Asia/Taipei`
- 輸出 CSV：`output/latest/revenue_breakout_low_response_latest.csv`
- Debug：`output/latest/revenue_breakout_low_response_debug_latest.md`

## 篩選邏輯

- 單月營收 YoY >= 80%，或單月 YoY >= 50% 且累計 YoY >= 20%。
- 近 5 日漲幅 <= 8%，且距 20MA / 23EMA 不超過 10%。
- 距前 60 日高點不可超過 +3%，避免已經明顯突破後才列入。
- 排除中期已反應個股：近20日漲幅>25%、近60日漲幅>40%、距60日低點反彈>50%、近120日漲幅>70%、距120日低點反彈>80%。
- 成交量需達 1000 張以上，避免太冷門。
- 金融、食品、營建、觀光、生技、紡織等防禦 / 傳產類股直接排除。
- 主流成長題材需 score >= 10；景氣循環 / 一般產業需 score >= 11。
- TDCC近幾週累積列入評分；若籌碼轉弱，候選股會降級。

## 完整名單

| rank | stock_id | stock_name | industry | theme_group | theme_score | revaluation_priority | score | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | close | volume_lots | volume_ratio | tdcc_judgement | price_data_warning | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5410 | 國眾 | 資訊服務業 | mainstream_growth | 3 | A_優先追蹤 | 22 | 122.27 | 37.89 | 3.48 | 19.84 | 27.98 | 27.98 | 32.82 | 32.82 | False |  | 9.36 | 9.03 | -0.9 | strong_accumulation | 1.99 | 2.66 | 2 | 2 | 38.65 | 1013.0 | 1.14 |  | ok | 單月營收YoY>=100%；累計營收YoY>=30%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價仍在20MA/23EMA附近；尚未突破前60日高點；站上20MA/23EMA；接近前高但未大幅過熱；TDCC近幾週400張與1000張同步累積；主流成長題材 |
| 2 | 6125 | 廣運 | 光電業 | mainstream_growth | 3 | A_優先追蹤 | 16 | 56.78 | 37.58 | -3.42 | -2.25 | -10.32 | -11.44 | 9.71 | 9.71 | False |  | -1.29 | -1.51 | -15.42 | mild_accumulation | 0.47 | 0.16 | 2 | 1 | 56.5 | 1606.0 | 0.8 |  | ok | 單月營收YoY 50%~80%；累計營收YoY>=30%；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；TDCC近幾週大戶溫和增加；主流成長題材 |
| 3 | 7777 | 能率亞洲 | 其他 | neutral | 0 | B_可觀察 | 20 | 1298.03 | 202.09 | -3.81 | 16.7 | -5.47 |  | 41.59 |  | False |  | 9.35 | 7.81 | -12.05 | mild_accumulation | 0.17 | -0.03 | 1 | 1 | 32.85 | 1658.0 | 0.52 |  | available_days_less_than_120 | 單月營收YoY>=150%；累計營收YoY>=50%；單月YoY大幅高於累計YoY，近期明顯加速；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；站上20MA/23EMA；TDCC近幾週大戶溫和增加；一般產業 |
| 4 | 4772 | 台特化 | 化學工業 | cyclical_turnaround | 1 | B_可觀察 | 18 | 210.12 | 266.45 | -2.3 | -8.87 | -3.09 | 3.11 | 9.36 | 9.36 | False |  | -2.92 | -2.27 | -14.86 | mild_accumulation | 0.12 | 0.07 | 1 | 1 | 298.0 | 1370.0 | 0.61 |  | ok | 單月營收YoY>=150%；累計營收YoY>=50%；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價貼近20MA/23EMA；尚未突破前60日高點；TDCC近幾週大戶溫和增加；景氣循環 / 報價轉機 |
| 5 | 1815 | 富喬 | 電子零組件業 | mainstream_growth | 3 | D_降級_TDCC轉弱 | 10 | 53.16 | 40.48 | -4.69 | -11.35 | 5.07 | 18.57 | 7.75 | 32.68 | False |  | -5.67 | -5.05 | -21.62 | distribution_warning | -5.96 | -5.6 | 0 | 0 | 101.5 | 12471.0 | 0.33 |  | ok | 單月營收YoY 50%~80%；累計營收YoY>=30%；近3日漲幅低於5%，股價低反應；近5日漲幅低於8%；股價仍在20MA/23EMA附近；尚未突破前60日高點；主流成長題材；TDCC近幾週大戶籌碼轉弱 |